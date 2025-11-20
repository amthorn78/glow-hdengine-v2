import json
from pathlib import Path


SNAPSHOT_PATH = Path("artifacts/bodygraph/refresh_policy.snapshot.json")


def test_refresh_policy_snapshot_matches_adr():
    data = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))

    assert data["schema"] == "v1"
    assert data["ttl_s"] == 604800
    assert data["swr_s"] == 86400

    rate_limit = data["rate_limit"]
    assert rate_limit["requests_per_window"] == 60
    assert rate_limit["window_s"] == 60

    circuit_breaker = data["circuit_breaker"]
    assert circuit_breaker["fail_threshold"] == 5
    assert circuit_breaker["window_s"] == 300
    assert circuit_breaker["cooldown_s"] == 900

    sample_counts = data["sample_counts"]
    assert sample_counts["refresh_attempts"] == 2
    assert sample_counts["refresh_successes"] == 1
    assert sample_counts["refresh_failures"] == 1
    assert sample_counts["breaker_tripped"] == 0
    assert sample_counts["rate_limit_hits"] == 0
