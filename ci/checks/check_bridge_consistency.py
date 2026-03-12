#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load_json(rel: str) -> dict:
    path = ROOT / rel
    if not path.exists():
        sys.exit(f"missing file: {rel}")
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _require_schema(
    label: str,
    payload: dict,
    expected_prefix: str | None = "v2",
    *,
    allowed_prefixes: tuple[str, ...] | None = None,
) -> None:
    value = payload.get("schema")
    prefixes = allowed_prefixes or ((expected_prefix,) if expected_prefix is not None else tuple())
    if not isinstance(value, str) or not any(value.startswith(prefix) for prefix in prefixes):
        expected = prefixes[0] if len(prefixes) == 1 else " or ".join(repr(prefix) for prefix in prefixes)
        sys.exit(f"{label} schema expected prefix {expected}, found {value!r}")


def _selection(payload: dict) -> tuple[str | None, list[dict]]:
    selection = payload.get("selection_result") or payload.get("final_selection") or {}
    provider = selection.get("provider")
    attempts = selection.get("attempts") or []
    return provider, attempts if isinstance(attempts, list) else []


def _require_all_errors(label: str, attempts: list[dict]) -> None:
    successes = [attempt for attempt in attempts if isinstance(attempt, dict) and attempt.get("status") == "ok"]
    if successes:
        providers = sorted({attempt.get("provider") for attempt in successes})
        sys.exit(f"{label} reported successful attempts despite selected 'none': {providers}")


def main() -> None:
    adapter = _load_json("artifacts/db_bridge/adapter_selection.snapshot.json")
    env = _load_json("artifacts/runtime/env_connectivity.snapshot.json")
    parity = _load_json("artifacts/db_bridge/provider_parity.proof.json")

    _require_schema("adapter_selection", adapter, allowed_prefixes=("v2", "v1"))
    _require_schema("env_connectivity", env)
    _require_schema("provider_parity", parity)
    if "selection_result" not in env:
        sys.exit("env_connectivity snapshot missing selection_result field")

    if not env.get("dev_only", False):
        sys.exit("env_connectivity snapshot must be dev-only")

    adapter_selected = adapter.get("selected")
    adapter_attempts = adapter.get("attempts") or []
    env_selected, env_attempts = _selection(env)
    parity_selected = parity.get("selected")
    parity_attempts = parity.get("attempts") or []

    if adapter_selected is None:
        sys.exit("adapter_selection snapshot missing selected provider")

    if adapter_selected == "none":
        _require_all_errors("adapter_selection", adapter_attempts)
        _require_all_errors("env_connectivity", env_attempts)
        _require_all_errors("provider_parity", parity_attempts)
        if env_selected not in {None, "none"}:
            sys.exit("adapter selected none but env_connectivity chose a provider")
        if parity_selected not in {None, "none"}:
            sys.exit("adapter selected none but provider_parity chose a provider")
        return

    if adapter_selected != env_selected:
        sys.exit(f"adapter selected {adapter_selected!r} but env_connectivity selected {env_selected!r}")

    if adapter_selected != parity_selected:
        sys.exit(f"adapter selected {adapter_selected!r} but provider_parity selected {parity_selected!r}")


if __name__ == "__main__":
    main()
