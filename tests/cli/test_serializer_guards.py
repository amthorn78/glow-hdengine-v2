from __future__ import annotations

import os
import subprocess
import sys
import textwrap
from pathlib import Path

ENV_PINS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def _env() -> dict[str, str]:
    env = dict(os.environ)
    env.update(ENV_PINS)
    return env


def test_guards_pass_on_repo_state(tmp_path: Path) -> None:
    serializer_log = tmp_path / "serializer.log"
    proof_log = tmp_path / "proof.log"

    ser = subprocess.run(
        [sys.executable, "tools/cli/serializer_grep_guard.py", "--output", str(serializer_log)],
        env=_env(),
        capture_output=True,
        text=True,
    )
    proof = subprocess.run(
        [sys.executable, "tools/cli/emitter_symbol_proof.py", "--output", str(proof_log)],
        env=_env(),
        capture_output=True,
        text=True,
    )

    assert ser.returncode == 0, ser.stderr
    assert proof.returncode == 0, proof.stderr
    serializer_body = serializer_log.read_text(encoding="utf-8")
    proof_body = proof_log.read_text(encoding="utf-8")
    assert "summary: PASS" in serializer_body
    assert "summary:PASS" in proof_body
    assert "adapter/http_reader.py" in serializer_body
    assert "canonical_emitters:emit_reader_public_envelope,emitter.emit_public" in proof_body
    assert "showcompat:showcompat:emit_reader_public_envelope,emitter.emit_public" in proof_body


def test_serializer_guard_detects_violation(tmp_path: Path) -> None:
    bad_file = tmp_path / "bad.py"
    bad_file.write_text("import json\njson.dumps({'x':1})\n", encoding="utf-8")
    log = tmp_path / "serializer.log"

    proc = subprocess.run(
        [
            sys.executable,
            "tools/cli/serializer_grep_guard.py",
            "--paths",
            str(tmp_path),
            "--output",
            str(log),
        ],
        env=_env(),
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    body = log.read_text(encoding="utf-8")
    assert "summary: FAIL" in body
    assert "bad.py" in body


def test_emitter_proof_detects_missing_emitter(tmp_path: Path) -> None:
    cli_file = tmp_path / "cli.py"
    cli_file.write_text(
        textwrap.dedent(
            """
            def showcompat(args):
                return 0

            def aux_preview(args):
                return 0

            def bg_resolve(args):
                return 0
            """
        ),
        encoding="utf-8",
    )
    log = tmp_path / "proof.log"

    proc = subprocess.run(
        [
            sys.executable,
            "tools/cli/emitter_symbol_proof.py",
            "--cli-path",
            str(cli_file),
            "--output",
            str(log),
        ],
        env=_env(),
        capture_output=True,
        text=True,
    )

    assert proc.returncode == 1
    body = log.read_text(encoding="utf-8")
    assert "summary:FAIL" in body
    assert "<none>" in body
