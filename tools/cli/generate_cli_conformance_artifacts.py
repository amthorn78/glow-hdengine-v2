#!/usr/bin/env python3
"""Generate deterministic CLI conformance artifacts for hdctl."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import sysconfig
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.presenter import emitter
from engine.runtime.determinism_env import ensure_determinism_env

ARTIFACT_DIR = ROOT / "artifacts" / "cli"
HELP_DIR = ARTIFACT_DIR / "help"
INSTALL_DIR = ARTIFACT_DIR / "install"
AB_PATH = ARTIFACT_DIR / "ab.json"
BA_PATH = ARTIFACT_DIR / "ba.json"
SUMMARY_PATH = ARTIFACT_DIR / "summary.json"
HDCTL_HELP_PATH = HELP_DIR / "hdctl_help.txt"
SHOWCOMPAT_HELP_PATH = HELP_DIR / "showcompat_help.txt"
REJECT_NONJSON_PATH = HELP_DIR / "reject_nonjson.txt"
ENTRYPOINTS_PATH = INSTALL_DIR / "entrypoints.txt"
INSTALLABILITY_SUMMARY_PATH = INSTALL_DIR / "installability_summary.json"

CONJUNCTION_AB = {
    "left": {
        "person_uid": "left-user",
        "birthdate": "1990-01-10",
        "birthtime": "14:05",
        "location": "Chicago, US",
    },
    "right": {
        "person_uid": "right-user",
        "birthdate": "1992-03-04",
        "birthtime": "08:15",
        "location": "Berlin, DE",
    },
}
CONJUNCTION_BA = {"left": CONJUNCTION_AB["right"], "right": CONJUNCTION_AB["left"]}

ENV_KEYS = (
    "SAFE_MODE",
    "ALLOW_NETWORK",
    "LC_ALL",
    "LANG",
    "TZ",
    "ENGINE_TAG",
    "RELEASE_ID",
    "PRODUCT_INVOCATION_TAG",
)


def _env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "ENGINE_TAG": "hdengine-dev",
            "RELEASE_ID": "0" * 64,
            "PRODUCT_INVOCATION_TAG": "INV-CLI-CONFORMANCE",
        }
    )
    ensure_determinism_env(environ=env)
    return env


def _run(cmd: list[str], *, env: dict[str, str], stdin: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(cmd, input=stdin, capture_output=True, env=env, cwd=ROOT)


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _assert_text_output(name: str, proc: subprocess.CompletedProcess[bytes]) -> bytes:
    if proc.returncode != 0:
        raise SystemExit(f"{name} failed rc={proc.returncode}: {proc.stderr!r}")
    if proc.stderr:
        raise SystemExit(f"{name} emitted stderr: {proc.stderr!r}")
    if not proc.stdout.endswith(b"\n"):
        raise SystemExit(f"{name} missing trailing LF")
    return proc.stdout


def _stdin_pair(payload: dict[str, object]) -> bytes:
    return (json.dumps(payload, separators=(",", ":")) + "\n").encode("utf-8")


def _load_entrypoint() -> str:
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    section_match = re.search(
        r"^\[project\.scripts\]\s*(?P<body>(?:\n(?!\[).*)*)",
        pyproject,
        flags=re.MULTILINE,
    )
    if section_match is None:
        raise SystemExit("[project.scripts] missing in pyproject.toml")

    entrypoint_match = re.search(
        r'^hdctl\s*=\s*"(?P<entrypoint>[^"]+)"\s*$',
        section_match.group("body"),
        flags=re.MULTILINE,
    )
    if entrypoint_match is None:
        raise SystemExit("hdctl entrypoint missing in [project.scripts]")
    return entrypoint_match.group("entrypoint")


def main() -> int:
    env = _env()
    module_cmd = [sys.executable, "-m", "engine.cli"]
    script_cmd = [sys.executable, "scripts/hdctl.py"]
    console_cmd = ["hdctl"]

    help_stdout = _assert_text_output("module help", _run([*module_cmd, "--help"], env=env))
    showcompat_help_stdout = _assert_text_output(
        "showcompat help", _run([*module_cmd, "showcompat", "--help"], env=env)
    )

    reject_proc = _run([*module_cmd, "showcompat", "--conjunction"], env=env, stdin=b"not-json\n")
    if reject_proc.returncode != 64:
        raise SystemExit(f"reject_nonjson expected rc=64 got {reject_proc.returncode}")
    if reject_proc.stdout:
        raise SystemExit("reject_nonjson expected empty stdout")
    if not reject_proc.stderr.endswith(b"\n"):
        raise SystemExit("reject_nonjson missing trailing LF")

    ab_proc = _run([*module_cmd, "showcompat", "--conjunction"], env=env, stdin=_stdin_pair(CONJUNCTION_AB))
    ba_proc = _run([*module_cmd, "showcompat", "--conjunction"], env=env, stdin=_stdin_pair(CONJUNCTION_BA))
    two_proc = _run([*module_cmd, "showcompat", "--conjunction"], env=env, stdin=_stdin_pair(CONJUNCTION_AB))

    ab_bytes = _assert_text_output("conjunction ab", ab_proc)
    ba_bytes = _assert_text_output("conjunction ba", ba_proc)
    two_bytes = _assert_text_output("conjunction two-run", two_proc)

    _write_bytes(HDCTL_HELP_PATH, help_stdout)
    _write_bytes(SHOWCOMPAT_HELP_PATH, showcompat_help_stdout)
    _write_bytes(REJECT_NONJSON_PATH, reject_proc.stderr)
    _write_bytes(AB_PATH, ab_bytes)
    _write_bytes(BA_PATH, ba_bytes)

    console_path = shutil.which("hdctl", path=env.get("PATH"))
    console_available = bool(console_path)
    version_cmd = [*module_cmd, "--version"]
    version_proc = _run(version_cmd, env=env)

    entrypoint_decl = _load_entrypoint()
    entrypoints_text = (
        "project.scripts.hdctl=engine.cli.main:cli\n"
        f"declared_entrypoint={entrypoint_decl}\n"
        f"module_help_cmd={' '.join(module_cmd + ['--help'])}\n"
        f"script_help_cmd={' '.join(script_cmd + ['--help'])}\n"
        f"console_entrypoint_available={str(console_available).lower()}\n"
        f"console_entrypoint_path={console_path or 'UNAVAILABLE'}\n"
    )
    _write_bytes(ENTRYPOINTS_PATH, entrypoints_text.encode("utf-8"))

    summary_payload = {
        "ab_sha256": hashlib.sha256(ab_bytes).hexdigest(),
        "ba_sha256": hashlib.sha256(ba_bytes).hexdigest(),
        "ab_ba_equal": ab_bytes == ba_bytes,
        "two_run_sha256": hashlib.sha256(two_bytes).hexdigest(),
        "two_run_equal": ab_bytes == two_bytes,
        "commands": {
            "ab": [*module_cmd, "showcompat", "--conjunction"],
            "ba": [*module_cmd, "showcompat", "--conjunction"],
            "two_run": [*module_cmd, "showcompat", "--conjunction"],
        },
        "installability": {
            "entrypoint_decl": entrypoint_decl,
            "module_help": {
                "cmd": [*module_cmd, "--help"],
                "returncode": 0,
            },
            "module_showcompat_help": {
                "cmd": [*module_cmd, "showcompat", "--help"],
                "returncode": 0,
            },
            "module_version": {
                "cmd": version_cmd,
                "returncode": version_proc.returncode,
                "stdout": version_proc.stdout.decode("utf-8", errors="replace"),
                "stderr": version_proc.stderr.decode("utf-8", errors="replace"),
            },
            "script_help": {
                "cmd": [*script_cmd, "--help"],
                "returncode": _run([*script_cmd, "--help"], env=env).returncode,
            },
            "console_entrypoint": {
                "available": console_available,
                "path": console_path,
            },
        },
        "pf05_command_catalog": {
            "implemented_commands": ["showcompat", "aux-preview", "bg:resolve", "dev:sampler"],
            "global_flags_checked": ["--help"],
            "showcompat_help_capture": SHOWCOMPAT_HELP_PATH.relative_to(ROOT).as_posix(),
            "argument_policing_capture": REJECT_NONJSON_PATH.relative_to(ROOT).as_posix(),
            "streams_checked": {"help_stderr_empty": True, "reject_stdout_empty": True},
            "env": {key: env[key] for key in ENV_KEYS},
        },
    }
    _write_bytes(SUMMARY_PATH, emitter.emit_public(summary_payload))

    installability_summary = {
        "generated_by": "tools/cli/generate_cli_conformance_artifacts.py",
        "entrypoint_decl": entrypoint_decl,
        "console_entrypoint_available": console_available,
        "console_entrypoint_path": console_path,
        "module_help": {"cmd": [*module_cmd, "--help"], "returncode": 0},
        "module_showcompat_help": {"cmd": [*module_cmd, "showcompat", "--help"], "returncode": 0},
        "module_version": {
            "cmd": version_cmd,
            "returncode": version_proc.returncode,
            "stdout": version_proc.stdout.decode("utf-8", errors="replace"),
            "stderr": version_proc.stderr.decode("utf-8", errors="replace"),
        },
        "reject_nonjson": {
            "cmd": [*module_cmd, "showcompat", "--conjunction"],
            "stdin": "not-json\\n",
            "returncode": reject_proc.returncode,
            "stderr": reject_proc.stderr.decode("utf-8", errors="replace"),
        },
    }
    _write_bytes(INSTALLABILITY_SUMMARY_PATH, emitter.emit_public(installability_summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
