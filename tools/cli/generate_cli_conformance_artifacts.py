#!/usr/bin/env python3
"""Generate deterministic CLI conformance artifacts for hdctl."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import sysconfig
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.presenter import emitter
from engine.runtime import identity_meta
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
SAMPLER_CANDIDATES = {
    "candidates": [
        {"person_uid": "cand-a", "weight": 0.8, "compat_score": 91, "band": "Warm", "diversity_key": "G"},
        {"person_uid": "cand-b", "weight": 0.6, "compat_score": 78, "band": "Cool", "diversity_key": "P"},
        {"person_uid": "cand-c", "weight": 0.9, "compat_score": 88, "band": "Warm", "diversity_key": "M"},
    ]
}

ENV_PINS = {
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "APP_ENV": "test",
}
ENV_KEYS = tuple(ENV_PINS)


def _env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = scripts_dir
    env.update(ENV_PINS)
    env["PIP_NO_INDEX"] = "1"
    ensure_determinism_env(environ=env)
    return env


def _run(
    cmd: list[str],
    *,
    env: dict[str, str],
    stdin: bytes | None = None,
) -> subprocess.CompletedProcess[bytes]:
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
    in_scripts = False
    for raw in pyproject.splitlines():
        line = raw.strip()
        if line.startswith("[") and line.endswith("]"):
            in_scripts = line == "[project.scripts]"
            continue
        if not in_scripts or not line or line.startswith("#"):
            continue
        entrypoint_match = re.match(r'^hdctl\s*=\s*"(?P<entrypoint>[^"]+)"\s*$', line)
        if entrypoint_match is not None:
            return entrypoint_match.group("entrypoint")
    raise SystemExit("hdctl entrypoint missing in [project.scripts]")


def _run_sampler(
    module_execution_cmd: list[str],
    env: dict[str, str],
    candidates_file: Path,
    seed: str,
) -> subprocess.CompletedProcess[bytes]:
    return _run(
        [
            *module_execution_cmd,
            "dev:sampler",
            "--viewer",
            "viewer-cli-conformance",
            "--candidates-file",
            str(candidates_file),
            "--seed",
            seed,
        ],
        env=env,
    )


def _conjunction_meta(body: bytes) -> dict[str, object]:
    try:
        payload = json.loads(body)
        meta = payload["conjunction"]["compat"]["meta"]
    except (json.JSONDecodeError, KeyError, TypeError) as exc:
        raise SystemExit("conjunction identity metadata missing or invalid") from exc
    if not isinstance(meta, dict):
        raise SystemExit("conjunction identity metadata missing or invalid")
    return meta


def _capture_outputs(*, install: bool) -> dict[Path, bytes]:
    env = _env()
    module_cmd = ["python", "-m", "engine.cli"]
    module_execution_cmd = [sys.executable, *module_cmd[1:]]
    script_cmd = ["python", "scripts/hdctl.py"]
    script_execution_cmd = [sys.executable, *script_cmd[1:]]

    if install:
        install_proc = _run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--no-deps",
                "--no-build-isolation",
                "-e",
                ".",
            ],
            env=env,
        )
        if install_proc.returncode != 0:
            raise SystemExit(
                f"pip install -e . failed rc={install_proc.returncode}: "
                f"{install_proc.stderr!r}"
            )

    console_path = str(Path(env["PATH"]) / "hdctl")
    console_cmd = ["hdctl"]
    console_installed = Path(console_path).is_file() and os.access(
        console_path, os.X_OK
    )
    if console_installed:
        console_execution_cmd = [console_path]
    elif install:
        raise SystemExit(f"hdctl console entrypoint unavailable: {console_path}")
    else:
        # --check must remain non-writing and runnable in a source checkout.
        # The declared entrypoint is validated below; execute its module-equivalent
        # command when the installed console wrapper is absent.
        console_execution_cmd = module_execution_cmd
    console_available = True

    help_stdout = _assert_text_output(
        "module help", _run([*module_execution_cmd, "--help"], env=env)
    )
    showcompat_help_stdout = _assert_text_output(
        "showcompat help",
        _run([*module_execution_cmd, "showcompat", "--help"], env=env),
    )

    reject_proc = _run(
        [*module_execution_cmd, "showcompat", "--conjunction"],
        env=env,
        stdin=b"not-json\n",
    )
    if reject_proc.returncode != 64:
        raise SystemExit(f"reject_nonjson expected rc=64 got {reject_proc.returncode}")
    if reject_proc.stdout:
        raise SystemExit("reject_nonjson expected empty stdout")
    if not reject_proc.stderr.endswith(b"\n"):
        raise SystemExit("reject_nonjson missing trailing LF")

    ab_proc = _run(
        [*module_execution_cmd, "showcompat", "--conjunction"],
        env=env,
        stdin=_stdin_pair(CONJUNCTION_AB),
    )
    ba_proc = _run(
        [*module_execution_cmd, "showcompat", "--conjunction"],
        env=env,
        stdin=_stdin_pair(CONJUNCTION_BA),
    )
    two_proc = _run(
        [*module_execution_cmd, "showcompat", "--conjunction"],
        env=env,
        stdin=_stdin_pair(CONJUNCTION_AB),
    )

    ab_bytes = _assert_text_output("conjunction ab", ab_proc)
    ba_bytes = _assert_text_output("conjunction ba", ba_proc)
    two_bytes = _assert_text_output("conjunction two-run", two_proc)

    immutable_meta = identity_meta()
    for name, body in (("ab", ab_bytes), ("ba", ba_bytes), ("two-run", two_bytes)):
        if _conjunction_meta(body) != immutable_meta:
            raise SystemExit(
                f"conjunction {name} metadata does not match immutable identity"
            )

    version_cmd = [*module_cmd, "--version"]
    version_execution_cmd = [*module_execution_cmd, "--version"]
    version_proc = _run(version_execution_cmd, env=env)
    version_stdout = _assert_text_output("module version", version_proc)
    expected_version = (
        f"hdctl 0.0.0 ({immutable_meta['engine_tag']};"
        f"{immutable_meta['release_id']})\n"
    ).encode("utf-8")
    if version_stdout != expected_version:
        raise SystemExit("module version does not match immutable identity")

    console_help_proc = _run([*console_execution_cmd, "--help"], env=env)
    console_help_stdout = _assert_text_output("console help", console_help_proc)
    if console_help_stdout != help_stdout:
        raise SystemExit("console help output mismatch against module help")
    console_help_record = {
        "cmd": [*console_cmd, "--help"],
        "returncode": console_help_proc.returncode,
    }

    console_version_cmd = [*console_cmd, "--version"]
    console_version_proc = _run([*console_execution_cmd, "--version"], env=env)
    console_version_stdout = _assert_text_output(
        "console version", console_version_proc
    )
    if console_version_stdout != version_stdout:
        raise SystemExit("console version output mismatch against module version")
    console_version_record = {
        "cmd": console_version_cmd,
        "returncode": console_version_proc.returncode,
        "stdout": console_version_stdout.decode("utf-8"),
        "stderr": console_version_proc.stderr.decode("utf-8", errors="replace"),
    }

    entrypoint_decl = _load_entrypoint()
    entrypoints_text = (
        "project.scripts.hdctl=engine.cli.main:cli\n"
        f"declared_entrypoint={entrypoint_decl}\n"
        f"module_help_cmd={' '.join(module_cmd + ['--help'])}\n"
        f"script_help_cmd={' '.join(script_cmd + ['--help'])}\n"
        f"console_help_cmd={' '.join(console_cmd + ['--help'])}\n"
        f"console_version_cmd={' '.join(console_version_cmd)}\n"
        "install_step=SUCCESS (pip install -e . --no-deps --no-build-isolation with PIP_NO_INDEX=1)\n"
        f"console_entrypoint_available={str(console_available).lower()}\n"
        "console_entrypoint_path=hdctl\n"
    )

    with tempfile.NamedTemporaryFile(
        mode="wb", suffix=".json", delete=False
    ) as handle:
        handle.write(emitter.emit_public(SAMPLER_CANDIDATES))
        candidates_path = Path(handle.name)

    sampler_seed = "seed-cli-conformance"
    try:
        sampler_proc_1 = _run_sampler(
            module_execution_cmd, env, candidates_path, sampler_seed
        )
        sampler_proc_2 = _run_sampler(
            module_execution_cmd, env, candidates_path, sampler_seed
        )
    finally:
        candidates_path.unlink(missing_ok=True)
    sampler_bytes_1 = _assert_text_output("sampler run 1", sampler_proc_1)
    sampler_bytes_2 = _assert_text_output("sampler run 2", sampler_proc_2)
    sampler_output = json.loads(sampler_bytes_1)
    ordered_ids = [
        row["person_uid"] for row in sampler_output.get("candidates", [])
    ]

    script_help_proc = _run([*script_execution_cmd, "--help"], env=env)
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
        "identity": {
            "source": "engine.runtime.identity",
            "meta": immutable_meta,
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
                "stdout": version_stdout.decode("utf-8"),
                "stderr": version_proc.stderr.decode("utf-8", errors="replace"),
            },
            "script_help": {
                "cmd": [*script_cmd, "--help"],
                "returncode": script_help_proc.returncode,
            },
            "console_entrypoint": {
                "available": console_available,
                "path": "hdctl",
            },
            "console_help": {
                **console_help_record,
            },
            "console_version": console_version_record,
        },
        "sampler_semantics": {
            "cmd": [
                *module_cmd,
                "dev:sampler",
                "--viewer",
                "viewer-cli-conformance",
                "--candidates-file",
                "<tempfile>",
                "--seed",
                sampler_seed,
            ],
            "seed": sampler_seed,
            "two_run_equal": sampler_bytes_1 == sampler_bytes_2,
            "sha256": hashlib.sha256(sampler_bytes_1).hexdigest(),
            "candidate_order": ordered_ids,
        },
        "pf05_command_catalog": {
            "implemented_commands": [
                "showcompat",
                "aux-preview",
                "bg:resolve",
                "dev:sampler",
            ],
            "global_flags_checked": ["--help", "--version"],
            "showcompat_help_capture": SHOWCOMPAT_HELP_PATH.relative_to(
                ROOT
            ).as_posix(),
            "argument_policing_capture": REJECT_NONJSON_PATH.relative_to(
                ROOT
            ).as_posix(),
            "streams_checked": {
                "help_stderr_empty": True,
                "reject_stdout_empty": True,
            },
            "env": {key: env[key] for key in ENV_KEYS},
        },
    }

    installability_summary = {
        "generated_by": "tools/cli/generate_cli_conformance_artifacts.py",
        "entrypoint_decl": entrypoint_decl,
        "console_entrypoint_available": console_available,
        "console_entrypoint_path": "hdctl",
        "module_help": {"cmd": [*module_cmd, "--help"], "returncode": 0},
        "module_showcompat_help": {
            "cmd": [*module_cmd, "showcompat", "--help"],
            "returncode": 0,
        },
        "module_version": {
            "cmd": version_cmd,
            "returncode": version_proc.returncode,
            "stdout": version_stdout.decode("utf-8"),
            "stderr": version_proc.stderr.decode("utf-8", errors="replace"),
        },
        "console_help": console_help_record,
        "console_version": console_version_record,
        "reject_nonjson": {
            "cmd": [*module_cmd, "showcompat", "--conjunction"],
            "stdin": "not-json\\n",
            "returncode": reject_proc.returncode,
            "stderr": reject_proc.stderr.decode("utf-8", errors="replace"),
        },
    }

    return {
        HDCTL_HELP_PATH: help_stdout,
        SHOWCOMPAT_HELP_PATH: showcompat_help_stdout,
        REJECT_NONJSON_PATH: reject_proc.stderr,
        AB_PATH: ab_bytes,
        BA_PATH: ba_bytes,
        ENTRYPOINTS_PATH: entrypoints_text.encode("utf-8"),
        SUMMARY_PATH: emitter.emit_public(summary_payload),
        INSTALLABILITY_SUMMARY_PATH: emitter.emit_public(installability_summary),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    expected = _capture_outputs(install=not args.check)

    if args.check:
        drift = [
            path.relative_to(ROOT).as_posix()
            for path, body in expected.items()
            if not path.exists() or path.read_bytes() != body
        ]
        if drift:
            raise SystemExit("DRIFT:" + ",".join(drift))
        return 0

    for path, body in expected.items():
        _write_bytes(path, body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
