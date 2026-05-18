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


def test_psycopg_adapter_allows_bridge_fallback_when_env_selects_bridge(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "psycopg", "attempts": [{"provider": "psycopg", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {
                "provider": "bridge",
                "attempts": [
                    {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
                    {"provider": "bridge", "status": "ok"},
                ],
            },
        },
        parity={
            "schema": "v2",
            "selected": "bridge",
            "attempts": [
                {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"},
                {"provider": "bridge", "status": "ok"},
            ],
        },
    )

    module.main()


def test_provider_parity_must_match_env_selection(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "psycopg", "attempts": [{"provider": "psycopg", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {"provider": "bridge", "attempts": [{"provider": "bridge", "status": "ok"}]},
        },
        parity={"schema": "v2", "selected": "psycopg", "attempts": [{"provider": "psycopg", "status": "ok"}]},
    )

    with pytest.raises(SystemExit, match="env_connectivity selected 'bridge' but provider_parity selected 'psycopg'"):
        module.main()


def test_provider_parity_rejects_pass_when_direct_is_unavailable(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "bridge", "attempts": [{"provider": "bridge", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {"provider": "bridge", "attempts": [{"provider": "bridge", "status": "ok"}]},
        },
        parity={
            "schema": "v2",
            "selected": "bridge",
            "attempts": [{"provider": "bridge", "status": "ok"}],
            "capabilities": [
                {
                    "name": "select_one",
                    "direct": {"status": "missing"},
                    "bridge": {"status": "ok"},
                    "parity": "pass",
                }
            ],
        },
    )

    with pytest.raises(SystemExit, match="provider_parity reported pass with unavailable direct rows"):
        module.main()


def test_provider_parity_allows_skip_when_direct_is_unavailable(tmp_path: Path) -> None:
    module = _load_check_module()
    module.ROOT = tmp_path

    _write_payloads(
        tmp_path,
        adapter={"schema": "v1", "selected": "bridge", "attempts": [{"provider": "bridge", "status": "ok"}]},
        env={
            "schema": "v2",
            "dev_only": True,
            "selection_result": {"provider": "bridge", "attempts": [{"provider": "bridge", "status": "ok"}]},
        },
        parity={
            "schema": "v2",
            "selected": "bridge",
            "attempts": [{"provider": "bridge", "status": "ok"}],
            "capabilities": [
                {
                    "name": "select_one",
                    "direct": {"status": "missing"},
                    "bridge": {"status": "not_exercised"},
                    "parity": "skip",
                    "parity_reason": "direct_unavailable",
                }
            ],
        },
    )

    module.main()
