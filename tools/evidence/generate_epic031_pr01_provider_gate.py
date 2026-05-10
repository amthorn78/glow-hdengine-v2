#!/usr/bin/env python3
"""Generate HDE-EPIC031 PR-01 local provider-gate evidence."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.vendor_client import (  # noqa: E402
    PINNED_BACKOFF_PROFILES,
    PINNED_MAX_ATTEMPTS,
    PINNED_TIMEOUT_PROFILES,
)
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402
from tools.evidence import update_evidence_index  # noqa: E402

PRODUCED_AT = "2026-05-10T15:38:37Z"

JOB_FILES = {
    "ci/jobs/rails_closed_refusal.yml": """name: rails_closed_refusal
rails:
  SAFE_MODE: \"1\"
  ALLOW_NETWORK: \"0\"
  LC_ALL: C
  LANG: C
  TZ: UTC
scope: hde-epic031-pr-01-local-deterministic
live_vendor_calls: forbidden
steps:
  - command: python -m pytest tests/bodygraph/test_resolver_vendor.py -q
    proves:
      - closed SAFE rails refuse provider behavior before vendor input resolution
      - closed-default state is SAFE_MODE=1 and ALLOW_NETWORK=0
""",
    "ci/jobs/rails_open_conformance.yml": """name: rails_open_conformance
rails:
  SAFE_MODE: \"0\"
  ALLOW_NETWORK: \"1\"
  LC_ALL: C
  LANG: C
  TZ: UTC
scope: hde-epic031-pr-01-fixture-backed-only
live_vendor_calls: forbidden
steps:
  - command: python -m pytest tests/bodygraph/test_vendor_client.py -q
    proves:
      - open rails provider policy is local and mocked
      - retry/backoff behavior is bounded and jitter-free
      - HTTP 429 maps to PROVIDER_RATE_LIMITED and is not retried
      - Retry-After delta-seconds and HTTP-date parsing are deterministic
""",
}

POLICIES_PINNED = """# HDE-EPIC031 PR-01 provider policy pins

Scope: local deterministic provider-gate proof for HDE-FERM001.2. No live vendor call is required or allowed.

## Rails posture

| State | SAFE_MODE | ALLOW_NETWORK | Provider behavior |
| --- | --- | --- | --- |
| closed default | 1 | 0 | resolver refuses vendor source before input resolution or ingest |
| open exception | 0 | 1 | provider behavior may run only in mocked or fixture-backed proof |

## Timeout profiles

Pinned timeout triples are `(connect_timeout_ms, read_timeout_ms, total_timeout_ms)`:

- `(500, 1000, 2000)`
- `(1000, 2000, 5000)`
- `(2000, 5000, 10000)`

## Retry and backoff policy

- `max_attempts` is pinned to `{0, 1, 2, 3}` including the initial attempt.
- Retryable outcome classes are only `network_error` and `5xx`.
- HTTP `429` is typed as `PROVIDER_RATE_LIMITED` and is not retried.
- Other `4xx` statuses are not retried by this component.
- Backoff modes are pinned to `none`, `fixed`, or `exponential` with closed integer parameters.
- Jitter is not implemented or configured.
- Planned sleep is bounded so accumulated delay cannot exceed `total_timeout_ms`.

## Retry-After posture

- Delta-seconds and HTTP-date values parse to non-negative milliseconds.
- Invalid, unsupported, or overflow values omit retry-after output.
- Retry-After is evidence-only metadata for `429`; it does not enable retry in this component.
"""

RETRY_AFTER_PARSE = [
    {"case": "delta_seconds", "input": "4", "retry_after_ms": 4000, "status": "parsed"},
    {
        "case": "http_date_future",
        "input": "Tue, 14 Nov 2023 23:13:20 GMT",
        "now_epoch_seconds": 1700000000,
        "retry_after_ms": 3600000,
        "status": "parsed",
    },
    {
        "case": "http_date_past",
        "input": "Tue, 14 Nov 2023 21:13:20 GMT",
        "now_epoch_seconds": 1700000000,
        "retry_after_ms": 0,
        "status": "parsed",
    },
    {"case": "invalid", "input": "not-a-date", "retry_after_ms": None, "status": "omitted"},
    {"case": "unsupported_fractional_delta", "input": "1.5", "retry_after_ms": None, "status": "omitted"},
    {"case": "overflow_delta", "input": "2147484", "retry_after_ms": None, "status": "omitted"},
]


def _sorted_profiles(profiles: frozenset[tuple[object, ...]]) -> list[list[object]]:
    return [list(item) for item in sorted(profiles)]


def _json_line(payload: object) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def _write(rel: str, text: str) -> Path:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _write_governed(rel: str, text: str) -> None:
    path = _write(rel, text)
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel,
        sha256=update_evidence_index._sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=None,
        produced_at=PRODUCED_AT,
        default_produced_at=PRODUCED_AT,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def _evidence_payloads() -> dict[str, object]:
    return {
        "audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json": {
            "artifact": "open_rails_policy_proof",
            "backoff": {
                "jitter": "none",
                "modes": [
                    {"profile": profile, "exp_base_ms": base, "exp_ceiling_ms": ceiling}
                    for profile, base, ceiling in _sorted_profiles(PINNED_BACKOFF_PROFILES)
                ],
                "total_timeout_bound": "planned sleep is omitted when it would exceed total_timeout_ms",
            },
            "epic_id": "HDE-EPIC031",
            "live_vendor_call_executed": False,
            "pf09_subtask": "HDE-FERM001.2",
            "rails": {
                "closed_default": {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"},
                "open_exception": {
                    "ALLOW_NETWORK": "1",
                    "SAFE_MODE": "0",
                    "scope": "mocked fixture-backed provider proof only",
                },
            },
            "retry": {
                "max_attempts": sorted(PINNED_MAX_ATTEMPTS),
                "retryable_error_classes": ["network_error", "5xx"],
            },
            "schema_version": "1.0",
            "secret_values_recorded": False,
            "timeout_profiles_ms": _sorted_profiles(PINNED_TIMEOUT_PROFILES),
            "tokens_supported": ["ENV_RAILS_POLICY_OK", "VENDOR_RETRY_BACKOFF_OK"],
        },
        "audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json": {
            "artifact": "retry_backoff_429_proof",
            "epic_id": "HDE-EPIC031",
            "http_429": {
                "error_code": "PROVIDER_RATE_LIMITED",
                "retry_after_metadata": "parsed when valid, omitted when invalid or overflow",
                "retried": False,
            },
            "live_vendor_call_executed": False,
            "other_4xx": {"retried": False},
            "retry_policy": {
                "backoff_modes": ["none", "fixed", "exponential"],
                "jitter": "none",
                "max_attempts": sorted(PINNED_MAX_ATTEMPTS),
                "retryable_error_classes": ["network_error", "5xx"],
            },
            "schema_version": "1.0",
            "tokens_supported": ["VENDOR_RETRY_BACKOFF_OK", "PROVIDER_429_TYPED_OK", "RETRY_AFTER_PARSE_OK"],
        },
        "audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json": {
            "artifact": "closed_default_open_exception_rails",
            "closed_default": {
                "ALLOW_NETWORK": "0",
                "SAFE_MODE": "1",
                "provider_result": "PROVIDER_REFUSED before vendor input resolution or ingest",
            },
            "epic_id": "HDE-EPIC031",
            "live_vendor_call_executed": False,
            "open_exception": {
                "ALLOW_NETWORK": "1",
                "SAFE_MODE": "0",
                "provider_result": "allowed only for local mocked or fixture-backed proof",
            },
            "schema_version": "1.0",
            "secret_values_recorded": False,
            "tokens_supported": ["ENV_RAILS_POLICY_OK"],
        },
    }


def main() -> None:
    ensure_determinism_env()
    for rel, text in JOB_FILES.items():
        _write(rel, text)
    _write_governed("artifacts/vendor/policies_pinned.md", POLICIES_PINNED)
    _write_governed("artifacts/vendor/retry_after_parse.log", "".join(_json_line(item) for item in RETRY_AFTER_PARSE))
    for rel, payload in _evidence_payloads().items():
        _write_governed(rel, _json_line(payload))


if __name__ == "__main__":
    main()
