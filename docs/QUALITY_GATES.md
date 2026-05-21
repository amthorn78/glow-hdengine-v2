# Quality Gates (local, repeatable)

This repository's canonical pre-deploy quality-gate command is:

```bash
./scripts/run_quality_gates.sh
```

## What it runs

1. `python -m pip install -r requirements-dev.txt`
2. `python -m pytest --version`
3. `python -m pytest -q tests/http/test_compat_endpoint_contract.py tests/http/test_reader_a7_transport.py tests/http/test_endpoint_catalog.py`
4. `git diff --check`

Optional full suite:

```bash
RUN_FULL_TEST_SUITE=1 ./scripts/run_quality_gates.sh
```

## Security/log posture

- Never paste secrets, tokens, private URLs, credentials, or private env values into logs, issues, chat, or PRs.
- Default rails remain closed (`SAFE_MODE=1`, `ALLOW_NETWORK=0`).
- This is repository quality-gate support only; it is not deployment-readiness proof by itself.

## Non-blocking/downstream ownership notes

- Deployment/runtime domain and production hardening decisions remain downstream.
- Full runtime/live browseability verification remains downstream.
