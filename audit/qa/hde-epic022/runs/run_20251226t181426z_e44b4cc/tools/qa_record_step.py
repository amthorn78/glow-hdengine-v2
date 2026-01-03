#!/usr/bin/env python3
import argparse
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    if not path.exists():
        return ""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def load_manifest(path: Path) -> dict:
    data = {"steps": []}
    if path.exists():
        try:
            loaded = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                data.update(loaded)
            elif isinstance(loaded, list):
                data["steps"] = loaded
        except Exception:
            data = {"steps": []}
    if "steps" not in data or not isinstance(data["steps"], list):
        data["steps"] = []
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--epic-id", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--check-id", required=True)
    parser.add_argument("--step-name", required=True)
    parser.add_argument("--command-json", required=True)
    parser.add_argument("--captured-env-json", required=True)
    parser.add_argument("--rails", required=True)
    parser.add_argument("--pf-refs-json", required=True)
    parser.add_argument("--intended-tokens-json", required=True)
    parser.add_argument("--claimed-tokens-json", required=True)
    parser.add_argument("--status", required=True)
    parser.add_argument("--exit-code", required=True)
    parser.add_argument("--started-at-utc", required=True)
    parser.add_argument("--ended-at-utc", required=True)
    parser.add_argument("--stdout-path", required=True)
    parser.add_argument("--stderr-path", required=True)
    parser.add_argument("--log-path", required=True)
    parser.add_argument("--manifest-path", required=True)
    args = parser.parse_args()

    exit_code = int(args.exit_code)
    stdout_path = Path(args.stdout_path)
    stderr_path = Path(args.stderr_path)
    log_path = Path(args.log_path)
    manifest_path = Path(args.manifest_path)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)

    stdout_text = read_text(stdout_path)
    stderr_text = read_text(stderr_path)

    header = {
        "epic_id": args.epic_id,
        "run_id": args.run_id,
        "check_id": args.check_id,
        "step_name": args.step_name,
        "command": json.loads(args.command_json),
        "captured_env": json.loads(args.captured_env_json),
        "rails": args.rails,
        "pf_refs": json.loads(args.pf_refs_json),
        "intended_tokens": json.loads(args.intended_tokens_json),
        "claimed_tokens": json.loads(args.claimed_tokens_json),
        "status": args.status,
        "exit_code": exit_code,
        "started_at_utc": args.started_at_utc,
        "ended_at_utc": args.ended_at_utc,
        "stdout_sha256": sha256_file(stdout_path),
        "stderr_sha256": sha256_file(stderr_path),
    }

    with log_path.open("w", encoding="utf-8") as f:
        f.write(json.dumps(header, ensure_ascii=False) + "\n\n")
        f.write("---- STDOUT ----\n")
        f.write(stdout_text)
        if not stdout_text.endswith("\n"):
            f.write("\n")
        f.write("\n---- STDERR ----\n")
        f.write(stderr_text)
        if not stderr_text.endswith("\n"):
            f.write("\n")

    manifest = load_manifest(manifest_path)
    manifest.setdefault("steps", [])
    manifest["steps"].append(
        {
            "check_id": args.check_id,
            "step_name": args.step_name,
            "run_id": args.run_id,
            "log_path": str(log_path),
            "status": args.status,
            "recorded_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "exit_code": exit_code,
        }
    )
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
