from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Iterable, Mapping, MutableMapping

DETERMINISM_ENV_PINS: dict[str, str] = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


class DeterminismEnvError(RuntimeError):
    """Raised when the determinism environment rails are not satisfied."""


def _validate_status(status: str) -> str:
    if status not in {"success", "failure"}:
        raise DeterminismEnvError(f"invalid status: {status}")
    return status


def expected_env(environ: Mapping[str, str] | None = None) -> dict[str, str | None]:
    source = environ if environ is not None else os.environ
    return {key: source.get(key) for key in DETERMINISM_ENV_PINS}


def ensure_determinism_env(
    environ: MutableMapping[str, str] | None = None, *, apply: bool = False
) -> dict[str, str]:
    env = environ if environ is not None else os.environ
    values: dict[str, str] = {}
    mismatches: list[str] = []
    for key, expected in DETERMINISM_ENV_PINS.items():
        current = env.get(key)
        if apply and current != expected:
            env[key] = expected
            current = expected
        if current is None:
            mismatches.append(f"{key}:<unset>")
        elif current != expected:
            mismatches.append(f"{key}:{current}")
        else:
            values[key] = current
    if mismatches:
        raise DeterminismEnvError(
            "env pins mismatch; expected rails closed (LC_ALL=C, LANG=C, TZ=UTC, SAFE_MODE=1, ALLOW_NETWORK=0): "
            + ", ".join(sorted(mismatches))
        )
    return {key: env[key] for key in DETERMINISM_ENV_PINS}


def render_env_log(env: Mapping[str, str], suites: Iterable[str], status: str) -> str:
    # Schema v1: Use "rails" and "schema" fields for EPIC023+ acceptance
    payload = {
        "rails": {
            "SAFE_MODE": int(env["SAFE_MODE"]),
            "ALLOW_NETWORK": int(env["ALLOW_NETWORK"]),
            "LC_ALL": env["LC_ALL"],
            "LANG": env["LANG"],
            "TZ": env["TZ"],
        },
        "schema": "determinism_env_pins.v1",
        "status": _validate_status(status),
        "suites": list(suites),
    }
    return json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n"


def record_env_log(
    log_path: Path,
    suites: Iterable[str],
    *,
    status: str = "success",
    environ: MutableMapping[str, str] | None = None,
    apply: bool = False,
    check_only: bool = False,
) -> Path:
    env = ensure_determinism_env(environ=environ, apply=apply)
    expected = render_env_log(env, suites, status)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if check_only:
        if not log_path.exists():
            raise DeterminismEnvError(f"missing determinism log: {log_path}")
        current = log_path.read_text(encoding="utf-8")
        if current != expected:
            raise DeterminismEnvError(f"determinism log mismatch at {log_path}")
        return log_path

    log_path.write_text(expected, encoding="utf-8")
    return log_path


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify determinism env rails")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="apply canonical env pins before validation (default: check only)",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="validate env (and optional log) without rewriting artifacts",
    )
    parser.add_argument(
        "--log-path",
        type=Path,
        default=Path("audit/gates/determinism/env_pins.log"),
        help="determinism env log path (default: audit/gates/determinism/env_pins.log)",
    )
    parser.add_argument(
        "--suite",
        action="append",
        dest="suites",
        default=[],
        help="suite identifier to include in determinism evidence",
    )
    parser.add_argument(
        "--status",
        default="success",
        help="determinism status to record (success|failure)",
    )
    parser.add_argument(
        "--check-log",
        action="store_true",
        help="validate the existing log content instead of rewriting it",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    suites = args.suites or ["determinism"]
    try:
        record_env_log(
            args.log_path,
            suites,
            status=args.status,
            apply=args.apply,
            check_only=args.check_only or args.check_log,
        )
    except DeterminismEnvError as exc:  # pragma: no cover - CLI exit path
        raise SystemExit(str(exc)) from exc
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
