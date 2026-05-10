# HDE-EPIC031 PR-01 provider policy pins

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
