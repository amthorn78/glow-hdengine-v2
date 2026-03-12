from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import pytest


def _load_check_module():
    spec = importlib.util.spec_from_file_location(
        "check_bridge_consistency", Path("ci/checks/check_bridge_consistency.py")
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def _write_payloads(tmp_path: Path, adapter: dict, env: dict, parity: dict) -> None:
    _write_json(tmp_path / "artifacts/db_bridge/adapter_selection.snapshot.json", adapter)
    _write_json(tmp_path / "artifacts/runtime/env_connectivity.snapshot.json", env)
    _write_json(tmp_path / "artifacts/db_bridge/provider_parity.proof.json", parity)


def test_legacy_v1_keeps_adapter_to_env_parity_consistency_check(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "psycopg", "attempts": [{"provider": "psycopg", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {"provider": "sqlite", "attempts": [{"provider": "sqlite", "status": "ok"}]},
        },
        parity={"schema": "v2", "selected": "sqlite", "attempts": [{"provider": "sqlite", "status": "ok"}]},
    )

    with pytest.raises(SystemExit, match="adapter selected 'psycopg' but env_connectivity selected 'sqlite'"):
        module.main()


def test_none_selection_rejects_successful_adapter_attempts(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "none", "attempts": [{"provider": "sqlite", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {
                "provider": "none",
                "attempts": [{"provider": "sqlite", "status": "error", "reason": "refused"}],
            },
        },
        parity={
            "schema": "v2",
            "selected": "none",
            "attempts": [{"provider": "sqlite", "status": "error", "reason": "refused"}],
        },
    )

    with pytest.raises(SystemExit, match="adapter_selection reported successful attempts despite selected 'none'"):
        module.main()
