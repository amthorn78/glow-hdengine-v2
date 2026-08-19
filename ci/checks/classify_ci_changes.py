#!/usr/bin/env python3
"""Classify an exact Git change into the smallest safe CI lane set.

The classifier is deliberately repository-owned and fail-safe. Known paths select
only the lanes whose protected inputs they can affect. Unknown paths and Git
events without a usable comparison base select every lane rather than silently
skipping protection.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
LANES = ("product", "compat", "db", "rails", "evidence", "qa", "release")
SHA_RE = re.compile(r"[0-9a-fA-F]{40,64}\Z")

_FULL_VALIDATION_PREFIXES = (
    ".github/",
)
_FULL_VALIDATION_PATHS = {
    "ci/checks/classify_ci_changes.py",
    "pyproject.toml",
    "pytest.ini",
    "requirements-dev.txt",
    "requirements.txt",
    "tests/evidence/test_rails_ci_workflow_integration.py",
}
_HISTORICAL_PREFIXES = (
    ".audit_src/",
    "_archive/",
    "_backup_",
    "artifacts/architecture/",
    "artifacts/epic020/",
    "audit/history/",
    "audit/historical/",
    "audit/ops/",
)
_DOCUMENTATION_PREFIXES = (
    "docs/crd/",
    "docs/pfcanon/",
    "docs/plans/",
    "docs/qa/",
    "docs/run/",
)
_DOCUMENT_SUFFIXES = {".adoc", ".md", ".rst"}
_DOCUMENT_PATHS = {
    "LICENSE",
    "AcceptanceMap.md",
    "AGENTS.md",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "README.md",
}
_RELEASE_EVIDENCE_PREFIXES = (
    "artifacts/audit/",
    "artifacts/bodygraph/",
    "artifacts/cards/",
    "artifacts/cli/",
    "artifacts/config_bundles/",
    "artifacts/db/",
    "artifacts/identity/",
    "artifacts/math/",
    "artifacts/ops/",
    "artifacts/parity/",
    "artifacts/presenter/",
    "artifacts/proofs/",
    "artifacts/reader/",
    "artifacts/registry/",
    "artifacts/runtime/",
    "artifacts/thresholds/",
    "artifacts/vendor/",
    "audit/gates/",
    "docs/evidence/",
)
_RELEASE_IMPLEMENTATION_PATHS = {
    "ci/checks/check_evidence_index_hash.sh",
    "ci/checks/check_final_lf.sh",
    "ci/checks/check_mirror_schema.sh",
    "ci/checks/run_rails_job_definitions.py",
    "scripts/release_id_recompute.py",
    "tests/evidence/test_internal_version_manifest_captures.py",
    "tools/evidence/build_release_attestation.py",
    "tools/evidence/generate_a7_transport_proofs.py",
    "tools/evidence/generate_bodygraph_policy_proofs.py",
    "tools/evidence/generate_db_runtime_posture.py",
    "tools/evidence/generate_determinism_gate_proofs.py",
    "tools/evidence/generate_env_matrix_snapshot.py",
    "tools/evidence/generate_hde_epic038_direct_db_selection.py",
    "tools/evidence/generate_identity_provenance.py",
    "tools/evidence/generate_open_rails_abba_proof.py",
    "tools/evidence/generate_rails_gate_evidence.py",
    "tools/evidence/generate_release_bindings.py",
    "tools/evidence/generate_v2_mapped_cache_evidence.py",
    "tools/evidence/orientation_demo.py",
    "tools/evidence/regenerate_identity_closure.py",
    "tools/evidence/retained_evidence_safety.py",
    "tools/evidence/run_canonical_json_gate.py",
    "tools/evidence/run_sanity_pipeline.py",
    "tools/evidence/run_sanity_pipeline_gate.py",
    "tools/evidence/update_evidence_index.py",
    "tools/evidence/validate_evidence_paths.py",
}
_ARCHITECTURE_ANALYSIS_PATHS = {
    "tests/evidence/test_architecture_snapshot.py",
    "tools/evidence/generate_architecture_snapshot.py",
}
_RAILS_MARKERS = (
    "open_rails",
    "rails_",
    "resolver_vendor",
    "vendor_client",
)
_COMPAT_MARKERS = (
    "/adapter/",
    "/catalog/",
    "/cli/",
    "/compat",
    "/http/",
    "/serializer",
    "/schemas/",
    "/transport/",
    "emitter",
    "http_reader",
    "showcompat",
)
_DB_MARKERS = (
    "/db/",
    "/migrations/",
    "/sql/",
    "cache_keys",
    "db_access",
    "direct_db",
    "ingest",
    "mapped_cache",
    "ops03",
)
_PRODUCT_PREFIXES = (
    "adapter/",
    "catalog/",
    "config/",
    "engine/",
    "math/",
    "migrations/",
    "presenter/",
    "schemas/",
    "scripts/",
    "sql/",
)


@dataclass(frozen=True)
class Classification:
    flags: dict[str, bool]
    reason: str
    path_count: int


def _full(reason: str, path_count: int) -> Classification:
    flags = {lane: True for lane in LANES}
    flags["needs_python"] = True
    return Classification(flags=flags, reason=reason, path_count=path_count)


def _empty_flags() -> dict[str, bool]:
    flags = {lane: False for lane in LANES}
    flags["needs_python"] = False
    return flags


def _normalized_path(raw: str) -> str:
    if not raw or "\x00" in raw or "\n" in raw or "\r" in raw:
        raise ValueError("changed path is empty or contains a control character")
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("changed path is not repository-relative")
    normalized = path.as_posix()
    if normalized in {"", "."}:
        raise ValueError("changed path is empty")
    return normalized


def _contains_component(path: str, component: str) -> bool:
    return component in PurePosixPath(path).parts


def _lanes_for_path(path: str) -> set[str] | None:
    """Return known lanes for one path, or ``None`` for fail-safe full CI."""
    if path in _FULL_VALIDATION_PATHS or path.startswith(_FULL_VALIDATION_PREFIXES):
        return set(LANES)

    if path.startswith(_DOCUMENTATION_PREFIXES):
        return set()

    historical_namespace = path.startswith(("audit/", "artifacts/", "docs/", "reports/"))
    if path.startswith(_HISTORICAL_PREFIXES) or (
        historical_namespace
        and any(
            _contains_component(path, component)
            for component in ("history", "historical", "runs")
        )
    ):
        return {"evidence"}

    if path in _RELEASE_IMPLEMENTATION_PATHS:
        return {"evidence", "release"}

    if path in _ARCHITECTURE_ANALYSIS_PATHS:
        return {"evidence", "product"}

    if path.startswith("tools/qa/") or path.startswith("tests/qa/"):
        return {"evidence", "qa"}

    if path.startswith("tests/evidence/"):
        lanes = {"evidence"}
        if "release" in path or "sanity_pipeline" in path:
            lanes.add("release")
        if "rails" in path:
            lanes.add("rails")
        return lanes

    if path.startswith("tools/evidence/"):
        lanes = {"evidence"}
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        if path in _RELEASE_IMPLEMENTATION_PATHS or "release" in path:
            lanes.add("release")
        return lanes

    if path.startswith("ci/jobs/") and "rails" in path:
        return {"rails", "release"}
    if path.startswith("ci/checks/"):
        if "direct_db" in path:
            return {"db", "product", "release"}
        if any(name in path for name in ("evidence", "mirror", "final_lf")):
            return {"evidence"}
        if "cli" in path:
            return {"compat", "product"}
        if "rails" in path:
            return {"rails"}
        return None

    if path.startswith(("audit/", "artifacts/")):
        lanes = {"evidence"}
        if path.startswith(_RELEASE_EVIDENCE_PREFIXES) or path.startswith(
            ("artifacts/evidence_index",)
        ):
            lanes.add("release")
        return lanes

    if path.startswith("docs/acceptance_map_") and path.endswith(".json"):
        return {"evidence", "release"}
    if path.startswith("docs/evidence/"):
        return {"evidence", "release"}
    if path.startswith("reports/"):
        return {"evidence"}

    if path.startswith("tests/"):
        lanes = {"product"}
        if any(marker in f"/{path}" for marker in _COMPAT_MARKERS):
            lanes.add("compat")
        if any(marker in f"/{path}" for marker in _DB_MARKERS):
            lanes.add("db")
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        lanes.add("release")
        return lanes

    if path.startswith(_PRODUCT_PREFIXES):
        lanes = {"product", "release"}
        marked_path = f"/{path}"
        if any(marker in marked_path for marker in _COMPAT_MARKERS):
            lanes.add("compat")
        if any(marker in marked_path for marker in _DB_MARKERS):
            lanes.add("db")
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        return lanes

    if path in _DOCUMENT_PATHS or (
        path.startswith("docs/") and PurePosixPath(path).suffix.lower() in _DOCUMENT_SUFFIXES
    ) or PurePosixPath(path).suffix.lower() in _DOCUMENT_SUFFIXES:
        return set()

    return None


def classify_paths(paths: Iterable[str]) -> Classification:
    normalized = sorted({_normalized_path(path) for path in paths})
    if not normalized:
        return _full("empty_change_set_full_validation", 0)

    selected: set[str] = set()
    for path in normalized:
        lanes = _lanes_for_path(path)
        if lanes is None:
            return _full("unknown_path_full_validation", len(normalized))
        selected.update(lanes)

    flags = _empty_flags()
    for lane in selected:
        flags[lane] = True
    flags["needs_python"] = bool(selected)
    reason = "selected_lanes" if selected else "documentation_only"
    return Classification(flags=flags, reason=reason, path_count=len(normalized))


def _validate_sha(raw: str, *, allow_zero: bool = False) -> str:
    value = raw.strip()
    if not SHA_RE.fullmatch(value):
        raise ValueError("Git comparison identity is not a full hexadecimal SHA")
    if not allow_zero and set(value) == {"0"}:
        raise ValueError("Git head identity cannot be all zeroes")
    return value.lower()


def git_changed_paths(repo_root: Path, base: str, head: str) -> tuple[str, ...]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-status",
            "-z",
            "--diff-filter=ACDMRTUXB",
            base,
            head,
            "--",
        ],
        cwd=repo_root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git changed-path discovery failed: {message}")
    tokens = [item for item in result.stdout.split(b"\0") if item]
    paths: list[str] = []
    index = 0
    while index < len(tokens):
        try:
            status = tokens[index].decode("ascii")
        except UnicodeDecodeError as exc:
            raise RuntimeError("git changed-path status is not ASCII") from exc
        index += 1
        path_count = 2 if status.startswith(("R", "C")) else 1
        if not status or status[0] not in "ACDMRTUXB" or index + path_count > len(tokens):
            raise RuntimeError("git changed-path output is malformed")
        for raw in tokens[index : index + path_count]:
            paths.append(raw.decode("utf-8"))
        index += path_count
    return tuple(paths)


def classify_git_change(repo_root: Path, base: str, head: str) -> Classification:
    base_sha = _validate_sha(base, allow_zero=True)
    head_sha = _validate_sha(head)
    if set(base_sha) == {"0"}:
        return _full("unavailable_base_full_validation", 0)
    if base_sha == head_sha:
        return _full("identical_refs_full_validation", 0)
    return classify_paths(git_changed_paths(repo_root, base_sha, head_sha))


def write_github_output(path: Path, classification: Classification) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        for name in (*LANES, "needs_python"):
            stream.write(f"{name}={'true' if classification.flags[name] else 'false'}\n")
        stream.write(f"reason={classification.reason}\n")
        stream.write(f"path_count={classification.path_count}\n")


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--event-name", choices=("pull_request", "push"), required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument(
        "--github-output",
        type=Path,
        default=Path(os.environ["GITHUB_OUTPUT"]) if os.environ.get("GITHUB_OUTPUT") else None,
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    if args.github_output is None:
        print("CI_CHANGE_CLASSIFIER_GITHUB_OUTPUT_MISSING", file=sys.stderr)
        return 2
    try:
        classification = classify_git_change(
            args.repo_root.resolve(), args.base, args.head
        )
        write_github_output(args.github_output, classification)
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        print(f"CI_CHANGE_CLASSIFIER_ERROR:{exc}", file=sys.stderr)
        return 2
    enabled = ",".join(
        lane for lane in LANES if classification.flags[lane]
    ) or "none"
    print(
        "CI_CHANGE_CLASSIFICATION:"
        f"event={args.event_name};reason={classification.reason};"
        f"paths={classification.path_count};lanes={enabled}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
