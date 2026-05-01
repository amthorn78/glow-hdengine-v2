from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_pr01_fails_closed_when_valid_prefs_are_rejected(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr01_normalization_evidence")

    test_root = mod.ROOT / "tmp" / "pytest_epic030_pr01_fail_closed"
    out_dir = test_root / "audit" / "qa" / "hde-epic030" / "pr-01"

    monkeypatch.setattr(mod, "OUT_DIR", out_dir)
    monkeypatch.setattr(mod, "ensure_determinism_env", lambda: None)
    monkeypatch.setattr(mod, "_upsert_index_entries", lambda: None)
    monkeypatch.setattr(mod, "validate_viewer_prefs", lambda prefs: "simulated rejection")

    with pytest.raises(SystemExit, match="VALID_PREFS_REJECTED"):
        mod.generate()


def test_pr02_fails_closed_when_two_run_identity_is_contradicted(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr02_sampler_harness_evidence")

    test_root = mod.ROOT / "tmp" / "pytest_epic030_pr02_fail_closed"
    out_dir = test_root / "audit" / "qa" / "hde-epic030" / "pr-02"

    def payload(seed: str, candidate_ids: list[str]) -> bytes:
        return mod.sercanon(
            {
                "viewer_id": "viewer-epic030-pr02",
                "meta": {"seed": seed},
                "candidate_ids": candidate_ids,
            },
            sort_keys=True,
        )

    class FakeResponse:
        def __init__(self, data: bytes, status_code: int = 200) -> None:
            self.data = data
            self.status_code = status_code
            self.headers = {
                "Content-Type": "application/json; charset=utf-8",
                "Cache-Control": "no-store",
            }

    class FakeClientContext:
        def __enter__(self):
            return object()

        def __exit__(self, exc_type, exc, tb) -> bool:
            return False

    class FakeApp:
        def test_client(self) -> FakeClientContext:
            return FakeClientContext()

    responses = iter(
        [
            FakeResponse(payload("seed-pr02", ["alpha", "bravo", "charlie"])),
            FakeResponse(payload("seed-pr02", ["alpha", "bravo", "charlie"])),
            FakeResponse(payload("seed-pr02", ["alpha", "charlie", "bravo"])),
            FakeResponse(payload("111", ["alpha", "bravo", "charlie"])),
            FakeResponse(payload("222", ["alpha", "bravo", "charlie"])),
        ]
    )

    monkeypatch.setattr(mod, "OUT_DIR", out_dir)
    monkeypatch.setattr(mod, "ensure_determinism_env", lambda: None)
    monkeypatch.setattr(mod, "create_app", lambda: FakeApp())
    monkeypatch.setattr(mod, "_post", lambda client, request_payload: next(responses))

    with pytest.raises(SystemExit, match="TWO_RUN_MISMATCH"):
        mod.main()


def test_pr03_identity_binding_fails_when_identity_hash_is_stale(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr03_compat_evidence")

    test_root = mod.ROOT / "tmp" / "pytest_epic030_pr03_fail_closed_identity"
    out_dir = test_root / "audit" / "qa" / "hde-epic030" / "pr-03"

    compat_payload = {
        "categories": [
            {
                "id": category,
                "band": "Cool",
                "score": 1,
                "personal_key": "p",
                "shared_key": "s",
            }
            for category in mod.CATEGORIES_ORDER_V1
        ],
        "meta": {"engine_tag": "dev", "release_id": "dev", "invocation_tag": "INV-DEV"},
    }
    compat_text = json.dumps(compat_payload, separators=(",", ":"), sort_keys=True) + "\n"

    _write(test_root / "artifacts" / "compat" / "AB.json", compat_text)
    _write(test_root / "artifacts" / "compat" / "BA.json", compat_text)
    _write(test_root / "artifacts" / "compat" / "identity_hash.txt", "0" * 64 + "\n")
    _write(
        test_root / "artifacts" / "epic003" / "narrative_keys_table.json",
        json.dumps(
            [
                {"id": category, "band": "Cool", "personal_key": f"p-{index}", "shared_key": f"s-{index}"}
                for index, category in enumerate(mod.CATEGORIES_ORDER_V1, start=1)
            ],
            separators=(",", ":"),
            sort_keys=True,
        )
        + "\n",
    )

    monkeypatch.setattr(mod, "OUT_DIR", out_dir)
    monkeypatch.setattr(mod, "AB_PATH", test_root / "artifacts" / "compat" / "AB.json")
    monkeypatch.setattr(mod, "BA_PATH", test_root / "artifacts" / "compat" / "BA.json")
    monkeypatch.setattr(mod, "IDENTITY_HASH_PATH", test_root / "artifacts" / "compat" / "identity_hash.txt")
    monkeypatch.setattr(mod, "LEGACY_KEY_TABLE_PATH", test_root / "artifacts" / "epic003" / "narrative_keys_table.json")
    monkeypatch.setattr(mod, "KEY_TABLE_PATH", test_root / "artifacts" / "narratives" / "key_table_10x2.snapshot.json")
    monkeypatch.setattr(mod, "ensure_determinism_env", lambda: None)

    mod.generate()

    identity_log = (out_dir / "compat_identity_binding.log").read_text(encoding="utf-8")

    assert "identity_matches_ab: False\n" in identity_log
    assert "identity_matches_ba: False\n" in identity_log
    assert "status: FAIL\n" in identity_log