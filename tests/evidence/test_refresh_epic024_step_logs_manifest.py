from __future__ import annotations

from pathlib import Path

from tools.evidence.refresh_epic024_step_logs_manifest import (
    build_manifest_payload,
    collect_check_entries,
    collect_check_ids,
    render_manifest,
)


def _touch(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("log\n", encoding="utf-8")


def test_collect_check_ids_sorted(tmp_path: Path) -> None:
    checks_root = tmp_path / "checks"
    _touch(checks_root / "D02" / "primary.log")
    _touch(checks_root / "D01" / "primary.log")

    check_ids = collect_check_ids(checks_root)
    assert check_ids == ["D01", "D02"]

    check_entries = collect_check_entries(checks_root)
    payload = build_manifest_payload(check_entries)
    assert payload["D01"]["log_path"] == "checks/D01/primary.log"
    assert payload["D02"]["log_path"] == "checks/D02/primary.log"

    rendered = render_manifest(payload)
    assert rendered.endswith(b"\n")


def test_manifest_payload_includes_transcripts(tmp_path: Path) -> None:
    checks_root = tmp_path / "checks"
    _touch(checks_root / "D01" / "primary.log")
    _touch(checks_root / "D01" / "transcript.txt")

    check_entries = collect_check_entries(checks_root)
    payload = build_manifest_payload(check_entries)
    assert payload["D01"]["transcript_path"] == "checks/D01/transcript.txt"
