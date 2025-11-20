"""Admin-only QA harness for vendor + DB BodyGraph parity checks."""
from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Sequence
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

AUDIT_PATH = Path("artifacts/ops/admin_vendor_calls.jsonl")
RAILS_STATE_CLOSED = "closed"
RAILS_STATE_OPEN = "open"

VENDOR_OUTPUT = Path("artifacts/bodygraph/vendor_upsert.alice.json")
DB_OUTPUT = Path("artifacts/bodygraph/db_resolve.alice.json")
VENDOR_COMPAT_OUTPUT = Path("artifacts/compat/vendor_pair.json")
DB_COMPAT_OUTPUT = Path("artifacts/compat/db_pair.json")
VIEWER_PREFS_PATH = Path("artifacts/compat/viewer.json")
PARITY_LOG_PATH = Path("artifacts/presenter/json_canon_compare.log")
NARRATIVE_TEXT_PATH = Path("artifacts/narratives/vendor_pair.txt")
NARRATIVE_SIDECAR_PATH = Path("artifacts/narratives/vendor_pair.sidecar.json")

VENDOR_PERSON = {
    "birthdate": "03-Jan-1980",
    "birthtime": "09:30",
    "location": "Paris, FR",
}
DB_IDS = {
    "user_a": "alice-test-id",
    "user_b": "bob-test-id",
}
COMPAT_PERSON_B = {
    "birthdate": "05-May-1982",
    "birthtime": "14:45",
    "location": "Vienna, AT",
}


def _rails_state() -> str:
    safe = os.getenv("SAFE_MODE")
    network = os.getenv("ALLOW_NETWORK")
    if safe == "0" and network == "1":
        return RAILS_STATE_OPEN
    return RAILS_STATE_CLOSED


def _redacted_host(url: str | None) -> str:
    if not url:
        return "<unset>"
    parsed = urlsplit(url)
    if parsed.netloc:
        return parsed.netloc
    return url


def _print_rails_summary() -> None:
    print(f"SAFE_MODE={os.getenv('SAFE_MODE', '<unset>')}")
    print(f"ALLOW_NETWORK={os.getenv('ALLOW_NETWORK', '<unset>')}")
    print(f"HDAPI_BASE_URL={_redacted_host(os.getenv('HDAPI_BASE_URL'))}")


def _write_viewer_prefs(path: Path) -> None:
    weights = {
        "alignment": 50,
        "balance": 50,
        "comfort": 50,
        "communication": 50,
        "consistency": 50,
        "creativity": 50,
        "drive": 50,
        "expansion": 50,
        "harmony": 50,
        "heat": 50,
    }
    data = {"top_category": "harmony", "weights": weights}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, separators=(",", ":"), sort_keys=True) + "\n", encoding="utf-8")


def _append_audit(step: str, source: str, route: str, status: str = "success") -> None:
    entry = {
        "at": f"{datetime.utcnow().isoformat(timespec='seconds')}Z",
        "env_rails": _rails_state(),
        "route": route,
        "source": source,
        "status": status,
        "step": step,
    }
    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, separators=(",", ":")) + "\n")


def _run_command(cmd: Sequence[str], stdout_path: Path | None = None) -> None:
    print("Running:", " ".join(cmd))
    stdout_handle = None
    try:
        if stdout_path is not None:
            stdout_path.parent.mkdir(parents=True, exist_ok=True)
            stdout_handle = stdout_path.open("w", encoding="utf-8")
        result = None
        try:
            result = subprocess.run(cmd, check=False, stdout=stdout_handle)
        except Exception as exc:
            raise SystemExit(f"Command {' '.join(cmd)} failed to execute: {exc}") from exc
    finally:
        if stdout_handle is not None:
            stdout_handle.close()
    if result and result.returncode != 0:
        raise SystemExit(f"Command {' '.join(cmd)} failed with exit code {result.returncode}")


def _run_parity_check() -> None:
    cmd = (
        "python",
        "-m",
        "presenter.json_canon_compare",
        str(VENDOR_OUTPUT),
        str(DB_OUTPUT),
        "--log",
        str(PARITY_LOG_PATH),
    )
    _run_command(cmd)


def _run_vendor_dry_run() -> None:
    cmd = (
        "python",
        "-m",
        "engine.cli",
        "bg:resolve",
        "--source",
        "vendor",
        "--birthdate",
        VENDOR_PERSON["birthdate"],
        "--birthtime",
        VENDOR_PERSON["birthtime"],
        "--location",
        VENDOR_PERSON["location"],
        "--dry-run",
        "--upsert",
    )
    _run_command(cmd, stdout_path=VENDOR_OUTPUT)
    _append_audit("vendor_upsert", source="vendor", route="bg:resolve")


def _run_db_resolve() -> None:
    cmd = (
        "python",
        "-m",
        "engine.cli",
        "bg:resolve",
        "--source",
        "db",
        "--user",
        DB_IDS["user_a"],
    )
    _run_command(cmd, stdout_path=DB_OUTPUT)
    _append_audit("db_resolve", source="db", route="bg:resolve")


def _run_showcompat_vendor() -> None:
    cmd = (
        "python",
        "-m",
        "engine.cli",
        "showcompat",
        "--source",
        "vendor",
        "--birthdate-a",
        VENDOR_PERSON["birthdate"],
        "--birthtime-a",
        VENDOR_PERSON["birthtime"],
        "--location-a",
        VENDOR_PERSON["location"],
        "--birthdate-b",
        COMPAT_PERSON_B["birthdate"],
        "--birthtime-b",
        COMPAT_PERSON_B["birthtime"],
        "--location-b",
        COMPAT_PERSON_B["location"],
        "--viewer-prefs-file",
        str(VIEWER_PREFS_PATH),
    )
    _run_command(cmd, stdout_path=VENDOR_COMPAT_OUTPUT)
    _append_audit("compat_vendor", source="vendor", route="showcompat")


def _run_showcompat_db() -> None:
    cmd = (
        "python",
        "-m",
        "engine.cli",
        "showcompat",
        "--source",
        "db",
        "--user-a",
        DB_IDS["user_a"],
        "--user-b",
        DB_IDS["user_b"],
        "--viewer-prefs-file",
        str(VIEWER_PREFS_PATH),
    )
    _run_command(cmd, stdout_path=DB_COMPAT_OUTPUT)
    _append_audit("compat_db", source="db", route="showcompat")


def _run_aux_preview() -> None:
    cmd = (
        "python",
        "-m",
        "engine.cli",
        "aux-preview",
        "--pair-file",
        str(VENDOR_COMPAT_OUTPUT),
        "--show-narrative",
        "--admin-out",
        str(NARRATIVE_SIDECAR_PATH),
    )
    _run_command(cmd, stdout_path=NARRATIVE_TEXT_PATH)
    _append_audit("narratives_vendor", source="vendor", route="aux-preview")


def _print_refusal_instructions() -> None:
    steps = [
        "After closing rails (SAFE_MODE=1, ALLOW_NETWORK=0), run:",
        "python -m engine.cli bg:resolve --source vendor \\",
        "  --birthdate \"03-Jan-1980\" --birthtime \"09:30\" --location \"Paris, FR\" \\",
        "  --dry-run > /tmp/closed.out 2> /tmp/closed.err",
        "Copy the refusal response to artifacts/proofs/ops_refusal_proof.txt with the canonical PF10 format:",
        "lower-case headers, blank line, LF-terminated JSON body.",
    ]
    print("\n".join(steps))


def main() -> int:
    _print_rails_summary()
    _write_viewer_prefs(VIEWER_PREFS_PATH)
    _run_vendor_dry_run()
    _run_db_resolve()
    _run_showcompat_vendor()
    _run_showcompat_db()
    _run_parity_check()
    _run_aux_preview()
    _print_refusal_instructions()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # pragma: no cover - unexpected failure
        print(f"ERROR: {exc}")
        sys.exit(1)
