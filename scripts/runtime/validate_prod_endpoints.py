#!/usr/bin/env python3
"""Validate docs/run/PROD_ENDPOINTS.json and emit a runtime audit file."""
from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path
from typing import Dict, Any


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> None:
    repo_root = _repo_root()
    prod_file = repo_root / "docs/run/PROD_ENDPOINTS.json"
    if not prod_file.is_file():
        raise SystemExit(f"Missing production endpoints file: {prod_file}")

    payload: Dict[str, Any] = json.loads(prod_file.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise SystemExit("Production endpoints file must contain a JSON object")

    lines = []
    env_total = 0
    services_total = 0
    for env_name in sorted(payload):
        env_value = payload[env_name]
        if not isinstance(env_value, dict):
            raise SystemExit(f"Environment '{env_name}' must map to an object")
        env_total += 1
        for service_name in sorted(env_value):
            services_total += 1
            service_meta = env_value[service_name]
            if not isinstance(service_meta, dict):
                raise SystemExit(f"Service '{service_name}' in env '{env_name}' must be an object")
            base_url = service_meta.get("base_url")
            if not isinstance(base_url, str) or not base_url:
                raise SystemExit(f"Service '{service_name}' in env '{env_name}' missing base_url")
            lines.append(f"{env_name}.{service_name}.base_url={base_url}")

    timestamp = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    output_lines = [
        f"timestamp_utc={timestamp}",
        f"environments={env_total}",
        f"services={services_total}",
        *lines,
    ]

    output_path = repo_root / "artifacts/runtime/prod_endpoints_check.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(output_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
