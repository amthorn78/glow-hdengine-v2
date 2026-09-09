import hashlib
import json
from dataclasses import replace

import pytest

from engine.config.registry_loader import load_registry_config
from engine.serializer.canon import sercanon
from tools.generate_registry_report import _build_registry_inputs, build_registry_report


def _render_current_report() -> bytes:
    return sercanon(build_registry_report(), sort_keys=True)


def test_registry_report_two_run_identity() -> None:
    first = _render_current_report()
    second = _render_current_report()
    assert first == second
    data = json.loads(first.decode("utf-8"))
    assert data["schema"] == "registry_report.v1"
    assert first.endswith(b"\n")
    assert hashlib.sha256(first).hexdigest() == hashlib.sha256(second).hexdigest()


def test_registry_report_is_independent_of_release_manifest_identity() -> None:
    config = load_registry_config()
    changed_manifest = replace(
        config.manifest,
        version="999.0.0",
        built_at_utc="2099-01-01T00:00:00Z",
    )
    changed = replace(config, manifest=changed_manifest)

    expected = _build_registry_inputs(config)
    assert _build_registry_inputs(changed) == expected
    assert set(expected) == {"catalogs"}


def test_selected_root_report_uses_own_seed_hash_payload_and_timestamp(tmp_path, monkeypatch) -> None:
    from tests.config.helpers import catalog_root, write_canonical

    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    roots = [catalog_root(tmp_path / name) for name in ("first", "second")]
    for index, root in enumerate(roots):
        seeds_path = root / "catalog/magic10_seeds.json"
        seeds = json.loads(seeds_path.read_bytes())
        first_seed = next(iter(seeds))
        seeds[first_seed]["seed_version"] = f"root-{index}"
        write_canonical(seeds_path, seeds)
        report_path = root / "artifacts/registry/registry_report.json"
        write_canonical(report_path, {"generated_at_utc": f"200{index}-01-01T00:00:00Z"})
        result = build_registry_report(root)
        assert result["generated_at_utc"] == f"200{index}-01-01T00:00:00Z"
        assert result["inputs"]["catalogs"]["magic10_seeds"]["sha256"] == hashlib.sha256(seeds_path.read_bytes()).hexdigest()
        assert result["artifacts"]["registry"]["magic10"]["seeds"][first_seed]["seed_version"] == f"root-{index}"
        assert result["inputs"]["catalogs"]["magic10_seeds"]["path"] == "catalog/magic10_seeds.json"
    assert build_registry_report(roots[0]) != build_registry_report(roots[1])
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "0")
    assert build_registry_report(roots[1])["generated_at_utc"] == "1970-01-01T00:00:00Z"


@pytest.mark.parametrize("initially_present", [False, True])
def test_report_build_refuses_prior_timestamp_source_change(tmp_path, monkeypatch, initially_present) -> None:
    from engine.config.registry_loader import _RegistryCapture
    from tests.config.helpers import catalog_root, write_canonical

    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    root = catalog_root(tmp_path)
    report = root / "artifacts/registry/registry_report.json"
    if initially_present:
        write_canonical(report, {"generated_at_utc": "2000-01-01T00:00:00Z"})
    original = _RegistryCapture.verify_unchanged
    changed = []

    def verify_then_change_prior(capture):
        original(capture)
        if hasattr(capture, "_registry_report_before") and not changed:
            write_canonical(report, {"generated_at_utc": "2001-01-01T00:00:00Z"})
            changed.append(report.read_bytes())

    monkeypatch.setattr(_RegistryCapture, "verify_unchanged", verify_then_change_prior)
    with pytest.raises(RuntimeError, match="REGISTRY_REPORT_SOURCE_CHANGED"):
        build_registry_report(root)
    assert report.read_bytes() == changed[0]


def test_report_retains_malformed_prior_timestamp_fallback(tmp_path, monkeypatch) -> None:
    from tests.config.helpers import catalog_root

    monkeypatch.delenv("SOURCE_DATE_EPOCH", raising=False)
    root = catalog_root(tmp_path)
    report = root / "artifacts/registry/registry_report.json"
    report.parent.mkdir(parents=True)
    report.write_bytes(b"malformed historical report\n")
    before = report.read_bytes(), report.stat().st_mtime_ns
    assert build_registry_report(root)["generated_at_utc"] == "1970-01-01T00:00:00Z"
    assert (report.read_bytes(), report.stat().st_mtime_ns) == before
