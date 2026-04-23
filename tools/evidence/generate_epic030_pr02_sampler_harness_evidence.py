#!/usr/bin/env python3
"""Generate governed EPIC030 PR-02 dev sampler harness evidence."""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.factory import create_app
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-02"


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(payload, sort_keys=True))


def _post(client, payload: dict[str, object]):
    return client.post(
        "/internal/dev/sampler",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )


def main() -> None:
    ensure_determinism_env()
    os.environ["APP_ENV"] = "dev"

    app = create_app()
    base_payload = {
        "viewer_id": "viewer-epic030-pr02",
        "candidate_ids": ["charlie", "alpha", "bravo"],
    }

    with app.test_client() as client:
        resp = _post(client, {**base_payload, "seed": "seed-pr02"})
        first = _post(client, {**base_payload, "seed": "seed-pr02"})
        second = _post(client, {**base_payload, "seed": "seed-pr02"})
        seed_a = _post(client, {**base_payload, "seed": "111"})
        seed_b = _post(client, {**base_payload, "seed": "222"})

    if resp.status_code != 200:
        raise SystemExit(f"EXPECTED_200_GOT_{resp.status_code}")

    body_bytes = resp.data
    if not body_bytes.endswith(b"\n"):
        raise SystemExit("STDOUT_MISSING_LF")

    body_payload = json.loads(body_bytes)
    expected_body = {
        "viewer_id": "viewer-epic030-pr02",
        "meta": {"seed": "seed-pr02"},
        "candidate_ids": ["alpha", "bravo", "charlie"],
    }
    if body_payload != expected_body:
        raise SystemExit("UNEXPECTED_BODY_PAYLOAD")

    if body_bytes != sercanon(body_payload, sort_keys=True):
        raise SystemExit("NON_CANONICAL_JSON")

    headers_text = "\n".join(
        [
            "route=/internal/dev/sampler",
            "method=POST",
            f"status={resp.status_code}",
            f"content-type={resp.headers.get('Content-Type', '')}",
            f"cache-control={resp.headers.get('Cache-Control', '')}",
            f"etag-present={'etag' in {k.lower() for k in resp.headers.keys()}}",
            "app_env=dev",
            "",
        ]
    )

    two_run = {
        "schema": "epic030_dev_sampler_two_run_identity.v1",
        "first_sha256": hashlib.sha256(first.data).hexdigest(),
        "second_sha256": hashlib.sha256(second.data).hexdigest(),
        "two_run_equal": first.data == second.data,
    }
    if not two_run["two_run_equal"]:
        raise SystemExit("TWO_RUN_MISMATCH")

    seed_a_payload = json.loads(seed_a.data)
    seed_b_payload = json.loads(seed_b.data)
    seed_only = {
        "schema": "epic030_dev_sampler_seed_only.v1",
        "candidate_ids_equal": seed_a_payload["candidate_ids"] == seed_b_payload["candidate_ids"],
        "seed_a": seed_a_payload["meta"]["seed"],
        "seed_b": seed_b_payload["meta"]["seed"],
        "response_a": seed_a_payload,
        "response_b": seed_b_payload,
    }
    if not seed_only["candidate_ids_equal"]:
        raise SystemExit("SEED_AFFECTED_RANKING")

    _write_text(OUT_DIR / "dev_sampler_http_headers.txt", headers_text)
    (OUT_DIR / "dev_sampler_http_body.json").write_bytes(body_bytes)
    _write_json(OUT_DIR / "dev_sampler_two_run_identity.json", two_run)
    _write_json(OUT_DIR / "dev_sampler_seed_only.json", seed_only)


if __name__ == "__main__":
    main()
