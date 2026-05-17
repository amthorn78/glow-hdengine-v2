import hashlib
import json
from pathlib import Path

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
