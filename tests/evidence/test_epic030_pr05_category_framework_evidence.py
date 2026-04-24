from __future__ import annotations

import importlib
import json
from pathlib import Path


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_pr05_binding_passes_when_index_and_mirror_include_pr05_artifacts(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr05_category_framework_evidence")

    test_root = mod.ROOT / "tmp" / "pytest_epic030_pr05_binding"
    out_dir = test_root / "audit" / "qa" / "hde-epic030" / "pr-05"

    _write(
        test_root / "catalog" / "channels_v1.json",
        '{"channels":[{"id":"20-10","gates":[20,10],"circuit_primary":"collective"}]}' + "\n",
    )
    _write(
        test_root / "artifacts" / "compat" / "AB.json",
        json.dumps(
            {
                "categories": [{"id": category, "band": "Cool", "score": 1, "personal_key": "a", "shared_key": "b"} for category in mod.CATEGORIES_ORDER_V1],
                "meta": {"engine_tag": "dev", "release_id": "dev", "invocation_tag": "INV-DEV"},
            },
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n",
    )
    _write(
        test_root / "artifacts" / "audit" / "a7" / "reader_200_body.json",
        '{"categories":[{"band":"Warm","id":"harmony"}],"eligible":true,"idempotence_hash":"x","meta":{"engine_tag":"d","invocation_tag":"i"},"reader_version":"v1","release_id":"r"}'
        + "\n",
    )

    index_rows = [{"artifact_key": key, "discovered_physical_path": "x"} for key in mod.PR05_ARTIFACT_KEYS]
    _write(test_root / "docs" / "evidence" / "INDEX.json", json.dumps(index_rows, separators=(",", ":"), sort_keys=True) + "\n")
    mirror_rows = "\n".join(json.dumps({"artifact_key": key}, separators=(",", ":"), sort_keys=True) for key in mod.PR05_ARTIFACT_KEYS) + "\n"
    _write(test_root / "artifacts" / "evidence_index.jsonl", mirror_rows)

    monkeypatch.setattr(mod, "OUT_DIR", out_dir)
    monkeypatch.setattr(mod, "CHANNELS_PATH", test_root / "catalog" / "channels_v1.json")
    monkeypatch.setattr(mod, "COMPAT_AB_PATH", test_root / "artifacts" / "compat" / "AB.json")
    monkeypatch.setattr(mod, "READER_A7_PATH", test_root / "artifacts" / "audit" / "a7" / "reader_200_body.json")
    monkeypatch.setattr(mod, "INDEX_PATH", test_root / "docs" / "evidence" / "INDEX.json")
    monkeypatch.setattr(mod, "MIRROR_PATH", test_root / "artifacts" / "evidence_index.jsonl")
    monkeypatch.setattr(mod, "ensure_determinism_env", lambda: None)

    mod.generate()

    binding = (out_dir / "category_framework_binding.log").read_text(encoding="utf-8")
    mechanics = json.loads((out_dir / "per_channel_mechanics.json").read_text(encoding="utf-8"))

    assert "status: PASS\n" in binding
    assert mechanics["channels"][0]["channel_id"] == "10-20"
    assert mechanics["channels"][0]["compromise_direction"] == "10->20"
