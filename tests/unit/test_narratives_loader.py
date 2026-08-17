import hashlib
import json
import shutil
from pathlib import Path

import pytest

from engine.narratives.lints import (
    check_inclusive_tone,
    run_all as run_narrative_lints,
)
from engine.narratives.loader import (
    NarrativePackError,
    _normalize_band,
    _select_primary,
    load_pack,
)
from engine.narratives.preview import emit_public_aux
from engine.narratives.router import route_keys


def _canonical_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_pack_loads_and_mounts(tmp_path):
    pack = load_pack(Path("catalog/narratives"), tmp_path / "mounted")
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


def test_pf17_directional_source_export_is_exact_and_current():
    from tools.evidence import generate_narrative_registry_diff as generator

    expected = generator.build_pf17_directional_pack()
    actual_keys = json.loads(Path("catalog/narratives/keys.json").read_bytes())
    actual_templates = json.loads(
        Path("catalog/narratives/templates.json").read_bytes()
    )

    assert actual_keys == expected["keys.json"]
    assert actual_templates == expected["templates.json"]
    assert len(actual_keys) == 360
    assert {
        perspective: sum(
            record["perspective"] == perspective for record in actual_keys
        )
        for perspective in ("a_to_b", "b_to_a", "shared")
    } == {"a_to_b": 120, "b_to_a": 120, "shared": 120}
    assert all("directions" not in record for record in actual_keys)
    assert all(record["perspective"] != "personal" for record in actual_keys)
    assert all(record["key"].startswith("nar.") for record in actual_keys)


def test_pf18_source_digest_is_pinned(tmp_path):
    from tools.evidence import generate_narrative_registry_diff as generator

    changed_source = tmp_path / "PF18.md"
    changed_source.write_bytes(generator.PF18_SOURCE_PATH.read_bytes() + b"\n")

    with pytest.raises(generator.RegistryDiffError, match="source digest mismatch"):
        generator._pf18_source_records(changed_source)


def test_directional_router_preserves_distinct_source_candidates(tmp_path, monkeypatch):
    from engine.narratives import state

    pack = load_pack(Path("catalog/narratives"), tmp_path / "mounted")
    monkeypatch.setattr(state, "_PACK", pack)

    ab = route_keys("alignment", "Cool", "a_to_b")
    ba = route_keys("alignment", "Cool", "b_to_a")

    assert ab["shared_key"] == ba["shared_key"]
    assert ab["personal_key"] == "nar.alignment.cool.a_to_b.1.face-01"
    assert ba["personal_key"] == "nar.alignment.cool.b_to_a.1.face-01"
    assert ab["personal_key"] != ba["personal_key"]


@pytest.mark.parametrize("candidate", ["cool", " Cool", "Cool "])
def test_pack_loader_does_not_repair_band_identity(candidate):
    with pytest.raises(NarrativePackError, match="unknown band"):
        _normalize_band(candidate)


def test_aux_emission_preserves_directional_copy_and_two_run_identity(
    tmp_path, monkeypatch
):
    from engine.narratives import state

    pack = load_pack(Path("catalog/narratives"), tmp_path / "mounted")
    monkeypatch.setattr(state, "_PACK", pack)

    def emit(perspective: str):
        return emit_public_aux(
            category="harmony",
            band="Cool",
            perspective=perspective,
            families_fired=(),
            release_id="a" * 64,
            pack_sha=pack.pack_sha,
        )

    ab_first = emit("a_to_b")
    ab_second = emit("a_to_b")
    ba = emit("b_to_a")
    shared = emit("shared")

    assert ab_first == ab_second
    assert all(not result.suppressed for result in (ab_first, ba, shared))
    assert {ab_first.pack_sha, ba.pack_sha, shared.pack_sha} == {pack.pack_sha}
    assert ab_first.key == "nar.harmony.cool.a_to_b.1.sage-01"
    assert ba.key == "nar.harmony.cool.b_to_a.1.sage-01"
    assert shared.key == "nar.harmony.cool.shared.1.sage-01"
    assert len({ab_first.key, ba.key, shared.key}) == 3
    assert len({ab_first.body, ba.body, shared.body}) == 3


def test_candidate_selection_advances_in_slot_order(tmp_path):
    pack = load_pack(Path("catalog/narratives"), tmp_path / "mounted")
    candidates = {
        record.slot: record
        for record in pack.keys.values()
        if record.category_slug == "balance"
        and record.band == "Glow"
        and record.perspective == "a_to_b"
    }
    suppression = {
        **pack.suppression_map,
        candidates[1].key: {
            "notes": "test-only slot block",
            "policy_reason": "conflict",
        },
    }

    selected = _select_primary(candidates, suppression, pack.templates)

    assert selected is not None
    assert selected.slot == 3


def test_ascii_hyphen_is_not_the_forbidden_em_dash():
    text = "You end with clean momentum. The work feels right-sized."
    assert tuple(run_narrative_lints(text)) == ()
    assert "NARR_NO_EM_DASH_OK" in tuple(
        run_narrative_lints(
            "You end with clean momentum. The work feels right—sized."
        )
    )


def test_inclusive_tone_rejects_whole_blame_token_without_substring_aliases():
    assert check_inclusive_tone("You rebalance without blame. Effort stays shared.") is False
    assert check_inclusive_tone("A flame feels gentle. The room stays clear.") is True


def test_historical_epic032_registry_evidence_is_frozen_and_write_refused():
    from tools.evidence import generate_narrative_registry_diff as generator

    assert not hasattr(generator, "build_artifacts")
    generator.write_artifacts(check=True)
    with pytest.raises(
        SystemExit,
        match="HISTORICAL_EPIC032_REGISTRY_WRITE_REFUSED",
    ):
        generator.write_artifacts()
    with pytest.raises(
        SystemExit,
        match="HISTORICAL_EPIC032_REGISTRY_WRITE_REFUSED",
    ):
        generator.main([])


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
            and record["perspective"] == "a_to_b"
            and record["slot"] == 3
        )
    ]

    with pytest.raises(generator.RegistryDiffError, match="missing required registry identities"):
        generator._identity_table(incomplete)
