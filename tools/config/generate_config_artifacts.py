#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import hashlib
import os
import sys
import tempfile
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.registry_loader import _capture_registry_config, _capture_mechanics_config  # noqa: E402
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import (  # noqa: E402
    BAND_EDGES_PATH, GOLDENS_DEFAULT_PATH, MAGIC10_CONFIG_PATH, GoldenComparisonRefusal,
    build_band_edges, build_magic10_config, compare_goldens, render_golden_report,
    require_closed_rails, _destination_state, _publish_prepared,
)
from tools.generate_registry_report import REPORT_PATH, _build_registry_report, _verify_report_source  # noqa: E402

_CONFIG_PATHS = (
    "artifacts/registry/registry_report.json",
    "artifacts/thresholds/magic10_config.json",
    "artifacts/thresholds/band_edges.json",
)
_CATALOG_LOG_PATHS = (
    "artifacts/catalog/catalog_schema_validation.log",
    "artifacts/catalog/domain_closure_report.log",
)


def _expected_config_artifacts(capture) -> dict[Path, bytes]:
    payloads = (_build_registry_report(capture), build_magic10_config(capture.config),
                build_band_edges(capture.root, _capture=capture))
    return {capture.root / name: canon.sercanon(payload, sort_keys=True)
            for name, payload in zip(_CONFIG_PATHS, payloads, strict=True)}


def expected_config_artifacts(root: Path | None = None, *, allow_aliases: bool = False,
                              alias_ledger: Mapping[str, str] | None = None) -> dict[Path, bytes]:
    capture = _capture_registry_config(root or ROOT, allow_aliases=allow_aliases,
                                      alias_ledger=alias_ledger)
    expected = _expected_config_artifacts(capture)
    capture.verify_unchanged()
    _verify_report_source(capture)
    return expected


def _check_expected(base: Path, expected: Mapping[Path, bytes]) -> dict[Path, object]:
    before = _destination_state(base, expected)
    stale = [path.relative_to(base).as_posix() for path, data in expected.items()
             if before[path] is None or before[path][0] != data]
    if stale:
        raise SystemExit("STALE:" + ",".join(stale))
    return before


def _verify_checked_outputs(base: Path, before: Mapping[Path, object], capture) -> None:
    capture.verify_unchanged()
    _verify_report_source(capture)
    if _destination_state(base, before) != dict(before):
        raise RuntimeError("CONFIG_CHECK_DESTINATION_CHANGED")


def check_config_artifacts(root: Path | None = None, *, allow_aliases: bool = False,
                           alias_ledger: Mapping[str, str] | None = None) -> None:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    capture = _capture_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    before = _check_expected(base, _expected_config_artifacts(capture))
    _verify_checked_outputs(base, before, capture)


def generate_config_artifacts(root: Path | None = None, *, allow_aliases: bool = False,
                              alias_ledger: Mapping[str, str] | None = None) -> dict[str, Path]:
    """Keep the existing three-primary authoring API, with coupled preparation."""
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    before = _destination_state(base, [base / name for name in _CONFIG_PATHS])
    capture = _capture_registry_config(base, allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    expected = _expected_config_artifacts(capture)
    _publish_prepared(base, expected, before=before, verify=capture.verify_unchanged)
    return dict(zip(("registry_report", "magic10_config", "band_edges"), expected, strict=True))


def _expected_catalog_logs(capture) -> dict[Path, bytes]:
    """Render diagnostics only after the actual complete local candidate validates.

    These logs describe construction checks, not immutable runtime admission,
    classifier execution, release activation or an independent QA verdict.
    """
    common = [f"source: {name} sha256={source.sha256} size_bytes={source.size_bytes}"
              for name, source in sorted(capture.sources.items())]
    schema = ["catalog schema validation v1", "status: PASS",
              "scope: PR01 local raw JSON and owning schema validation",
              "validation: duplicate-aware UTF-8, canonical bytes, local schemas, exact integer domains",
              *common]
    closure = ["catalog domain closure v1", "status: PASS",
               "scope: PR01 exact catalog and initial configuration construction",
               f"channels: {len(capture.registry.channels)}", f"gates: {len(capture.registry.gates)}",
               "validation: per-ID taxonomy, Gate/Center bindings, retained Product metadata, initial profiles and joins",
               *common]
    return {capture.root / name: ("\n".join(lines) + "\n").encode("utf-8")
            for name, lines in zip(_CATALOG_LOG_PATHS, (schema, closure), strict=True)}


def generate_catalog_logs(root: Path | None = None, *, check: bool = False) -> None:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    before = _destination_state(base, [base / name for name in _CATALOG_LOG_PATHS])
    capture = _capture_mechanics_config(base)
    expected = _expected_catalog_logs(capture)
    if check:
        before = _check_expected(base, expected)
        _verify_checked_outputs(base, before, capture)
    else:
        _publish_prepared(base, expected, before=before, verify=capture.verify_unchanged)


def publish_config_family(root: Path | None = None) -> None:
    """Publish the exact PR01 config family through its existing evidence owner.

    The current listed manifest consequences are refreshed before derived data.
    Final checks and all caught failures share one rollback boundary; interrupted
    mixed candidates must be recovered, never treated as an active release.
    """
    require_closed_rails()
    from engine.config import bundles, registry_loader
    from scripts import cut_release_manifest, release_id_recompute
    from tools import generate_registry_report
    from tools.config import artifacts, generate_bundles
    from tools.evidence import generate_arrays_as_sets_report as arrays
    from tools.evidence import run_canonical_json_gate as gate
    from tools.evidence import update_evidence_index as updater
    from tools.evidence import orientation_demo

    base = Path(os.path.abspath(root or ROOT))
    modules = (bundles, registry_loader, cut_release_manifest, release_id_recompute,
               generate_registry_report, artifacts, generate_bundles, arrays, gate,
               updater, orientation_demo)
    if base != ROOT or any(Path(module.ROOT) != base for module in modules if hasattr(module, "ROOT")):
        raise RuntimeError("CONFIG_PUBLICATION_ROOT_MISMATCH")
    if gate.update_evidence_index is not updater:
        raise RuntimeError("CONFIG_PUBLICATION_UPDATER_IDENTITY_MISMATCH")
    if os.environ.get("HDE_ISOLATED_RELEASE_BUILD"):
        raise RuntimeError("CONFIG_PUBLICATION_ISOLATED_RELEASE_MODE_FORBIDDEN")

    initial = _capture_mechanics_config(base)
    initial.verify_unchanged()
    manifest_source = initial.sources["catalog/manifest.json"]
    manifest = manifest_source.data
    immutable_paths = {base / name for name in initial.sources if name != "catalog/manifest.json"}
    immutable_paths.update(base / entry["path"] for entry in manifest["files"])
    immutable_paths.update(base / target.rel_path for target in gate.TARGETS
                           if target.rel_path != "catalog/manifest.json")
    immutable_paths.update(Path(module.__file__).absolute() for module in modules)
    immutable_paths.add(Path(__file__).absolute())
    # The preserved consumer documents are an exact-byte input even though their
    # owning format permits pretty-printing. Capture them before any output write.
    immutable_paths.update(base / name for name in (
        "docs/schemas/config_bundle_be.json", "docs/schemas/config_bundle_fe.json",
        "engine/serializer/canon.py", "engine/stable/sercanon.py", "engine/mech/helpers.py",
        "schemas/magic10_result_v1.schema.json", "schemas/magic10_compat_result_v1.schema.json",
        "artifacts/identity/service_identity.json"))
    immutable_before = _destination_state(base, immutable_paths)
    if any(value is None for value in immutable_before.values()):
        raise RuntimeError("CONFIG_PUBLICATION_SOURCE_MISSING")
    initial.verify_unchanged()
    # Verify the existing cutter's expected postimage from the captured member
    # bytes; the cutter remains the only writer of the actual manifest.
    cut_expected = copy.deepcopy(manifest)
    for entry in cut_expected["files"]:
        member_bytes = immutable_before[base / entry["path"]][0]
        entry["sha256"] = hashlib.sha256(member_bytes).hexdigest()
        entry["size"] = len(member_bytes)
    cut_expected["files"].sort(key=lambda entry: entry["path"])
    cut_expected_bytes = canon.sercanon(cut_expected, sort_keys=True)
    gate_paths = (
        "audit/gates/canonical_json/json_canonical_check.log",
        "audit/gates/canonical_json/json_canon_compare.log",
        "audit/gates/canonical_json/canonical_json.gate.json",
        "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
        "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
        "audit/gates/json_gate/canonical/json_gate_structured_record.json",
    )
    names = ("catalog/manifest.json", *_CONFIG_PATHS, *_CATALOG_LOG_PATHS,
             "artifacts/config_bundles/be_bundle.json", "artifacts/config_bundles/fe_bundle.json",
             "artifacts/canonical/arrays_as_sets_report.log", *gate_paths)
    publication_before = _destination_state(base, [base / name for name in names])
    after_manifest = []

    def before_owner(relative_paths) -> None:
        paths = tuple(base / name for name in relative_paths)
        updater._ACTIVE_WRITE_TRANSACTION.assert_unchanged(paths)
        expected = {path: publication_before[path] for path in paths}
        if _destination_state(base, expected) != expected:
            raise RuntimeError("CONFIG_OWNER_DESTINATION_CHANGED")


    def source_verify() -> None:
        if _destination_state(base, immutable_paths) != immutable_before:
            raise RuntimeError("CONFIG_PUBLICATION_SOURCE_CHANGED")
        expected_manifest = after_manifest[0] if after_manifest else manifest_source.raw
        if (base / "catalog/manifest.json").read_bytes() != expected_manifest:
            raise RuntimeError("CONFIG_PUBLICATION_MANIFEST_CHANGED")

    def produce() -> None:
        source_verify()
        before_owner(("catalog/manifest.json",))
        manifest_path = base / "catalog/manifest.json"

        def publish_manifest(path: Path, content: bytes) -> None:
            if path != manifest_path or content != cut_expected_bytes:
                raise RuntimeError("CONFIG_MANIFEST_PREPARED_BYTES_MISMATCH")
            source_verify()
            # The cutter owns the validated bytes; the existing updater owns
            # atomic replacement and its exact postimage/rollback receipt.
            # A partial temporary write cannot truncate the original manifest.
            updater._publish_staged({path: content})
            after_manifest[:] = [content]
            source_verify()

        if cut_release_manifest.cut_manifest(manifest_path, version=manifest["version"],
                built_at_utc=manifest["built_at_utc"], check=True) != 0:
            if cut_release_manifest.cut_manifest(manifest_path, version=manifest["version"],
                    built_at_utc=manifest["built_at_utc"], _publish=publish_manifest) != 0:
                raise RuntimeError("CONFIG_MANIFEST_REFRESH_FAILED")
        after_manifest[:] = [cut_expected_bytes]
        source_verify()
        if release_id_recompute.check_manifest_only(base / "catalog/manifest.json") != 0:
            raise RuntimeError("CONFIG_MANIFEST_CHECK_FAILED")
        before_owner(_CONFIG_PATHS)
        generate_config_artifacts(base)
        before_owner(_CATALOG_LOG_PATHS)
        generate_catalog_logs(base)
        before_owner(("artifacts/config_bundles/be_bundle.json", "artifacts/config_bundles/fe_bundle.json"))
        bundles.generate_bundles(base)
        before_owner(("artifacts/canonical/arrays_as_sets_report.log",))
        arrays.write_report()
        before_owner(gate_paths)
        if gate.main([]) != 0:
            raise RuntimeError("CONFIG_CANONICAL_GATE_FAILED")

    def verify() -> None:
        check_config_artifacts(base)
        generate_catalog_logs(base, check=True)
        generate_bundles.check_bundles(base)
        arrays.write_report(check=True)
        if gate.main(["--check-only"]) != 0:
            raise RuntimeError("CONFIG_CANONICAL_GATE_CHECK_FAILED")
        if release_id_recompute.check_manifest_only(base / "catalog/manifest.json") != 0:
            raise RuntimeError("CONFIG_MANIFEST_CHECK_FAILED")
        orientation_demo.generate_orientation(check=True)

    updater.publish_config_family(root=base, primary_paths=[base / name for name in names],
                                  produce=produce, verify=verify, source_verify=source_verify)


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR05: read-only golden comparison mode.  It dispatches only to
# ``compare_goldens``/``render_golden_report`` and the external report writer;
# it never reaches the generation, check or publication paths above.
# ---------------------------------------------------------------------------
GOLDEN_COMPARISON_MISMATCH_EXIT_CODE = 1
GOLDEN_COMPARISON_REFUSAL_EXIT_CODE = 5


def _golden_report_destination(report_path: Path, candidate_root: Path) -> Path:
    """Refuse a report path inside the candidate root or the repository, or unsafe on disk."""
    parent = Path(os.path.realpath(Path(os.path.abspath(report_path)).parent))
    destination = parent / Path(report_path).name
    forbidden = (Path(os.path.realpath(candidate_root)), Path(os.path.realpath(ROOT)))
    if (not destination.name or destination.name in {".", ".."} or not parent.is_dir()
            or destination.is_symlink() or (destination.exists() and not destination.is_file())
            or any(destination == root or destination.is_relative_to(root) for root in forbidden)):
        raise GoldenComparisonRefusal("REPORT_PATH_INVALID")
    return destination


def _write_golden_report(destination: Path, payload: bytes) -> None:
    descriptor, temporary = tempfile.mkstemp(dir=destination.parent, prefix=".golden-report-", suffix=".tmp")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
        os.replace(temporary, destination)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise


def _compare_goldens_main(candidate_root: Path, goldens: Path, report: Path | None) -> int:
    try:
        try:
            require_closed_rails()
        except SystemExit as exc:
            raise GoldenComparisonRefusal(str(exc.code)) from None
        destination = _golden_report_destination(report, candidate_root) if report is not None else None
        result = compare_goldens(candidate_root, goldens)
        payload = render_golden_report(result)
        if destination is not None:
            _write_golden_report(destination, payload)
    except GoldenComparisonRefusal as exc:
        sys.stderr.write(f"{exc.code}\n")
        return GOLDEN_COMPARISON_REFUSAL_EXIT_CODE
    if result.ok:
        sys.stdout.buffer.write(payload)
        sys.stdout.flush()
        return 0
    sys.stderr.write(f"GOLDEN_COMPARISON_MISMATCH:{len(result.mismatches)}\n")
    return GOLDEN_COMPARISON_MISMATCH_EXIT_CODE


def _main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate governed config artifacts under closed rails")
    parser.add_argument("--allow-aliases", action="store_true", help="Enable explicit input-only alias allow-list mode")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true", help="Validate committed three-primary bytes without writing")
    modes.add_argument("--publish-family", action="store_true", help="Publish the scoped config, catalog logs, bundles and required evidence companions from this checkout")
    modes.add_argument("--compare-goldens", metavar="CANDIDATE_ROOT", help="Read-only: admit the explicit candidate root and compare the PF01 §9.5 golden collection through the canonical entrypoints; exit 0 on match, 1 on mismatch, 5 on refusal")
    parser.add_argument("--goldens", metavar="PATH", help="Golden collection for --compare-goldens (default: tests/fixtures/magic10/v1/goldens.json)")
    parser.add_argument("--report", metavar="PATH", help="With --compare-goldens: write the complete canonical report to this path outside the candidate root and the repository")
    args = parser.parse_args(argv)
    if args.compare_goldens is not None:
        if args.allow_aliases:
            parser.error("--compare-goldens requires the canonical goldens without aliases")
        return _compare_goldens_main(
            Path(args.compare_goldens),
            Path(args.goldens) if args.goldens else GOLDENS_DEFAULT_PATH,
            Path(args.report) if args.report else None,
        )
    if args.goldens or args.report:
        parser.error("--goldens and --report apply only to --compare-goldens")
    if args.publish_family:
        if args.allow_aliases:
            parser.error("--publish-family requires the canonical source without aliases")
        publish_config_family(ROOT)
    elif args.check:
        check_config_artifacts(ROOT, allow_aliases=args.allow_aliases)
    else:
        generate_config_artifacts(ROOT, allow_aliases=args.allow_aliases)
    return 0


main = _main

if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(_main())
