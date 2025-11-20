#!/usr/bin/env python3
"""Out-of-band BodyGraph refresh worker for EPIC011."""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Mapping

from engine.bodygraph.ingest import (
    VendorError,
    VendorInputs,
    gather_inputs_from_env,
    ingest_vendor_bodygraph,
    resolve_db_user_id,
)

# TODO: reconcile this POLICY shape (flat rate_limit and cb fields) with the
# v1 snapshot schema that uses nested rate_limit and circuit_breaker objects.
POLICY = {
    "schema": "v1",
    "ttl_s": 604800,
    "swr_s": 86400,
    "rate_limit": 60,
    "cb": {"fail": 5, "window_s": 300, "cooldown_s": 900},
}
STATE_PATH = Path("artifacts/bodygraph/refresh_state.json")
POLICY_SNAPSHOT = Path("artifacts/bodygraph/refresh_policy.snapshot.json")
METRICS_SNAPSHOT = Path("artifacts/bodygraph/metrics.snapshot.json")
REFRESH_LOG_SAMPLE = Path("artifacts/bodygraph/keys_only.logs.sample")
GLOBAL_KEYS_ONLY_LOG = Path("artifacts/logs/keys_only.sample.jsonl")


@dataclass
class RefreshState:
    refresh_attempts_total: int = 0
    refresh_success_total: int = 0
    refresh_failure_total: int = 0
    breaker_tripped_total: int = 0
    rate_limit_hit_total: int = 0
    last_success_at: float = 0.0
    last_duration_ms: float = 0.0
    window_start: float = 0.0
    attempts_in_window: int = 0
    breaker_open_until: float = 0.0
    failure_timestamps: list[float] = field(default_factory=list)

    @classmethod
    def load(cls) -> "RefreshState":
        if not STATE_PATH.exists():
            return cls()
        try:
            data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except Exception:
            return cls()
        return cls(
            refresh_attempts_total=data.get("refresh_attempts_total", 0),
            refresh_success_total=data.get("refresh_success_total", 0),
            refresh_failure_total=data.get("refresh_failure_total", 0),
            breaker_tripped_total=data.get("breaker_tripped_total", 0),
            rate_limit_hit_total=data.get("rate_limit_hit_total", 0),
            last_success_at=data.get("last_success_at", 0.0),
            last_duration_ms=data.get("last_duration_ms", 0.0),
            window_start=data.get("window_start", 0.0),
            attempts_in_window=data.get("attempts_in_window", 0),
            breaker_open_until=data.get("breaker_open_until", 0.0),
            failure_timestamps=[float(ts) for ts in data.get("failure_timestamps", [])],
        )

    def dump(self) -> None:
        STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "refresh_attempts_total": self.refresh_attempts_total,
            "refresh_success_total": self.refresh_success_total,
            "refresh_failure_total": self.refresh_failure_total,
            "breaker_tripped_total": self.breaker_tripped_total,
            "rate_limit_hit_total": self.rate_limit_hit_total,
            "last_success_at": self.last_success_at,
            "last_duration_ms": self.last_duration_ms,
            "window_start": self.window_start,
            "attempts_in_window": self.attempts_in_window,
            "breaker_open_until": self.breaker_open_until,
            "failure_timestamps": self.failure_timestamps,
        }
        STATE_PATH.write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def _truthy(value: object | None) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _utc_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + "Z"


def _append_keys_only(path: Path, record: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def _write_sample(path: Path, records: list[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records[-5:]:
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")


def _refresh_due(state: RefreshState, now: float) -> bool:
    if state.last_success_at <= 0:
        return True
    age = now - state.last_success_at
    return age >= POLICY["swr_s"]


def _maybe_reset_rate_limit(state: RefreshState, now: float) -> None:
    if now - state.window_start >= 60:
        state.window_start = now
        state.attempts_in_window = 0


def _prune_failures(state: RefreshState, now: float) -> None:
    window = POLICY["cb"]["window_s"]
    state.failure_timestamps = [ts for ts in state.failure_timestamps if now - ts <= window]


def run_refresh(env: Mapping[str, object] | None = None) -> None:
    env = env or os.environ
    safe_mode = _truthy(env.get("SAFE_MODE"))
    allow_network = _truthy(env.get("ALLOW_NETWORK"))
    now = time.time()
    state = RefreshState.load()
    _maybe_reset_rate_limit(state, now)
    _prune_failures(state, now)
    logs: list[Dict[str, Any]] = []
    status = 200
    duration_ms = 0.0
    attempt_reason = "eligible"

    if not _refresh_due(state, now):
        status = 304
        attempt_reason = "fresh_within_swr"
        attempt_allowed = False
    else:
        attempt_allowed = True

    if attempt_allowed and state.attempts_in_window >= POLICY["rate_limit"]:
        attempt_allowed = False
        status = 429
        attempt_reason = "rate_limited"
        state.rate_limit_hit_total += 1

    if attempt_allowed:
        if now < state.breaker_open_until:
            attempt_allowed = False
            status = 503
            attempt_reason = "breaker_cooldown"
            state.breaker_tripped_total += 1
        elif len(state.failure_timestamps) >= POLICY["cb"]["fail"]:
            attempt_allowed = False
            status = 503
            attempt_reason = "breaker_open"
            state.breaker_tripped_total += 1
            state.breaker_open_until = max(state.breaker_open_until, now + POLICY["cb"]["cooldown_s"])

    if attempt_allowed and safe_mode:
        attempt_allowed = False
        status = 412
        attempt_reason = "safe_mode"

    if attempt_allowed and not allow_network:
        attempt_allowed = False
        status = 503
        attempt_reason = "network_closed"

    outcome_details: Dict[str, Any] = {}
    if attempt_allowed:
        state.refresh_attempts_total += 1
        state.attempts_in_window += 1
        start = time.monotonic()
        try:
            inputs = gather_inputs_from_env()
            normalized_id = resolve_db_user_id(inputs.user_id)
            if normalized_id != inputs.user_id:
                inputs = VendorInputs(
                    user_id=normalized_id,
                    birthdate=inputs.birthdate,
                    birthtime=inputs.birthtime,
                    location=inputs.location,
                )
            outcome = ingest_vendor_bodygraph(inputs, env=env)
            duration_ms = (time.monotonic() - start) * 1000.0
            state.refresh_success_total += 1
            state.last_success_at = now
            state.last_duration_ms = duration_ms
            state.failure_timestamps = []
            state.breaker_open_until = 0.0
            status = 200
            attempt_reason = "success"
            outcome_details = {
                "input_fingerprint": outcome.input_fingerprint,
                "vendor": outcome.vendor,
                "vendor_version": outcome.vendor_version,
            }
        except VendorError as exc:
            duration_ms = (time.monotonic() - start) * 1000.0
            state.refresh_failure_total += 1
            state.failure_timestamps.append(now)
            if len(state.failure_timestamps) >= POLICY["cb"]["fail"]:
                state.breaker_open_until = max(state.breaker_open_until, now + POLICY["cb"]["cooldown_s"])
                state.breaker_tripped_total += 1
            status = 502
            attempt_reason = exc.code
            outcome_details = {"error_code": exc.code}

    log_record = {
        "at": _utc_iso(),
        "route": "ops.refresh.bodygraph",
        "status": status,
        "duration_ms": round(duration_ms, 3),
    }
    logs.append(log_record)
    _append_keys_only(GLOBAL_KEYS_ONLY_LOG, log_record)
    _write_sample(REFRESH_LOG_SAMPLE, logs)

    sample_counts = {
        "refresh_attempts": state.refresh_attempts_total,
        "refresh_successes": state.refresh_success_total,
        "refresh_failures": state.refresh_failure_total,
        "breaker_tripped": state.breaker_tripped_total,
        "rate_limit_hits": state.rate_limit_hit_total,
    }
    policy_snapshot = dict(POLICY)
    policy_snapshot["sample_counts"] = sample_counts
    POLICY_SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    POLICY_SNAPSHOT.write_text(
        json.dumps(policy_snapshot, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    metrics_payload = {
        "schema": "v1",
        "counters": {
            "refresh_attempts_total": state.refresh_attempts_total,
            "refresh_success_total": state.refresh_success_total,
            "refresh_failure_total": state.refresh_failure_total,
            "breaker_tripped_total": state.breaker_tripped_total,
            "rate_limit_hit_total": state.rate_limit_hit_total,
        },
        "timers_ms": {
            "refresh_duration_p95": int(round(state.last_duration_ms)),
        },
        "labels": {
            "env": (env.get("APP_ENV") or "dev"),
            "source": "hdapi",
            "reason": attempt_reason,
        },
    }
    METRICS_SNAPSHOT.parent.mkdir(parents=True, exist_ok=True)
    METRICS_SNAPSHOT.write_text(
        json.dumps(metrics_payload, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    state.dump()

    summary = {
        "status": attempt_reason,
        "http_status": status,
        "details": outcome_details,
        "counts": sample_counts,
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    run_refresh()
