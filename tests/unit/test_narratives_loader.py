import hashlib
import json
import shutil
from pathlib import Path

import pytest

from engine.narratives import get_pack


def _canonical_sha(path: Path) -> str:
    if path.suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        canonical = json.dumps(data, separators=(",", ":"), sort_keys=True).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_pack_loads_and_mounts():
    pack = get_pack()
    manifest_path = Path("catalog/narratives/manifest.json")
    assert pack.pack_sha == _canonical_sha(manifest_path)
    assert pack.mount_path.exists()
    # Ensure mount contains the sealed files
    for name in [
        "keys.json",
        "templates.json",
        "palettes.json",
        "suppression_map.json",
        "manifest.json",
    ]:
        assert (pack.mount_path / name).exists()
        assert (pack.mount_path / f"{name}.sha256").exists()


def test_narrative_registry_diff_artifact_is_canonical_and_keys_only():
    from tools.evidence import generate_narrative_registry_diff as generator

    payload, _identity_text = generator.build_artifacts()
    rendered = generator._canonical_json_bytes(payload, trailing_lf=True)

    expected = (
        json.dumps(json.loads(rendered), separators=(",", ":"), sort_keys=True).encode("utf-8")
        + b"\n"
    )
    assert rendered == expected
    assert payload["identity"]["pack_sha"] == _canonical_sha(
        Path("catalog/narratives/manifest.json")
    )
    assert payload["identity"]["two_run_identity"]["match"] is True
    assert payload["diff"]["status"] == "no_prior_baseline_current_manifest_verified"
    assert "templates" not in payload
    rendered_text = rendered.decode("utf-8")
    template_values = json.loads(
        Path("catalog/narratives/templates.json").read_text(encoding="utf-8")
    ).values()
    assert all(value not in rendered_text for value in template_values)


def test_narrative_pack_identity_two_run_matches_manifest_sha():
    from tools.evidence import generate_narrative_registry_diff as generator

    _payload, identity_text = generator.build_artifacts()
    lines = dict(line.split("=", 1) for line in identity_text.splitlines() if "=" in line)

    expected = _canonical_sha(Path("catalog/narratives/manifest.json"))
    assert lines["pack_sha"] == expected
    assert lines["manifest_canonical_sha256"] == expected
    assert lines["two_run_first"] == expected
    assert lines["two_run_second"] == expected
    assert lines["two_run_match"] == "true"


def test_registry_diff_rejects_unexpected_manifest_rows(tmp_path, monkeypatch):
    from tools.evidence import generate_narrative_registry_diff as generator

    catalog_copy = tmp_path / "catalog" / "narratives"
    shutil.copytree(Path("catalog/narratives"), catalog_copy)
    manifest_path = catalog_copy / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["files"].append(
        {
            "path": "catalog/narratives/extra.json",
            "sha256": "0" * 64,
            "size_bytes": 2,
        }
    )
    manifest_path.write_text(
        json.dumps(manifest, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(generator, "ROOT", tmp_path)
    monkeypatch.setattr(generator, "CATALOG_ROOT", catalog_copy)
    monkeypatch.setattr(generator, "MANIFEST_PATH", manifest_path)
    monkeypatch.setattr(generator, "KEYS_PATH", catalog_copy / "keys.json")

    with pytest.raises(generator.RegistryDiffError, match="unexpected manifest paths"):
        generator._require_manifest()


def test_registry_diff_rejects_swapped_manifest_rows_with_current_sidecar(tmp_path):
    from tools.evidence import generate_narrative_registry_diff as generator

    catalog_copy = tmp_path / "catalog" / "narratives"
    shutil.copytree(Path("catalog/narratives"), catalog_copy)
    manifest_path = catalog_copy / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"][0], manifest["files"][1] = (
        manifest["files"][1],
        manifest["files"][0],
    )
    manifest_bytes = generator._canonical_json_bytes(manifest, trailing_lf=False)
    manifest_path.write_bytes(manifest_bytes)
    manifest_path.with_suffix(".json.sha256").write_text(
        hashlib.sha256(manifest_bytes).hexdigest() + "\n", encoding="utf-8"
    )

    with pytest.raises(
        generator.RegistryDiffError,
        match="manifest paths must match required ASCII order",
    ):
        generator.validate_registry_snapshot(catalog_copy, repo_root=tmp_path)


def test_registry_diff_rejects_unknown_category_and_band():
    from tools.evidence import generate_narrative_registry_diff as generator

    records = json.loads(Path("catalog/narratives/keys.json").read_text(encoding="utf-8"))
    records[0] = {**records[0], "category": "unknown", "category_slug": "unknown"}
    with pytest.raises(generator.RegistryDiffError, match="unknown category_slug"):
        generator._identity_table(records)

    records = json.loads(Path("catalog/narratives/keys.json").read_text(encoding="utf-8"))
    records[0] = {**records[0], "band": "Unknown"}
    with pytest.raises(generator.RegistryDiffError, match="unknown band"):
        generator._identity_table(records)


def test_registry_diff_rejects_incomplete_category_band_perspective_slot_grid():
    from tools.evidence import generate_narrative_registry_diff as generator

    records = json.loads(Path("catalog/narratives/keys.json").read_text(encoding="utf-8"))
    incomplete = [
        record
        for record in records
        if not (
            record["category_slug"] == "heat"
            and record["band"] == "Cool"
            and record["perspective"] == "personal"
            and record["slot"] == 3
        )
    ]

    with pytest.raises(generator.RegistryDiffError, match="missing required registry identities"):
        generator._identity_table(incomplete)
