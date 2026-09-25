import json
import os
import pathlib
import subprocess
import sysconfig

import pytest

from engine.cli.main import cli
from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from engine.runtime.identity import identity_meta
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams

pytestmark = pytest.mark.epic006


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    return env


def test_missing_file_returns_64_and_stderr():
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", "no_such.json"], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr


def test_bad_json_returns_64_and_stderr(tmp_path: pathlib.Path):
    bad = tmp_path / "bad.json"
    bad.write_text("{bad}\n", encoding="utf-8")
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", str(bad)], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert result.stderr


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-usage-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-usage-pack"))


def test_success_writes_stdout_only(monkeypatch, capsys, tmp_path: pathlib.Path, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    payload = {"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps(payload), encoding="utf-8")
    exit_code = cli(["showcompat", "--pair-file", str(pair)])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.err == ""
    assert captured.out.endswith("\n")
    assert captured.out.strip()


def test_usage_error_writes_stderr_only():
    result = subprocess.run(["hdctl"], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 64
    assert result.stdout == ""
    assert "usage" in result.stderr.lower()


def test_engine_error_writes_stderr_only():
    # Closed rails: the vendor acquisition is refused before any I/O; the
    # stderr token equals the error_v1 code for the same failure (PF05 §4.1.4).
    result = subprocess.run(
        [
            "hdctl", "showcompat", "--source", "vendor",
            "--birthdate-a", "2000-01-01", "--birthtime-a", "00:00", "--location-a", "Moon",
            "--birthdate-b", "2000-02-02", "--birthtime-b", "01:01", "--location-b", "Sun",
        ],
        capture_output=True,
        text=True,
        env=_cli_env(),
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == "PROVIDER_REFUSED\n"


def test_admission_refusal_is_a_single_stderr_token(monkeypatch, capsys, tmp_path: pathlib.Path):
    # The repository root is the admitted complete release, so the subprocess
    # evaluates the pair through the real admission owner and prints exactly one
    # canonical result document.  The admission refusal remains a single stderr
    # token; it is asserted through the evaluation provider seam because the
    # public owner derives its root from execution provenance, never from the
    # working directory or an environment variable.
    payload = {"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps(payload), encoding="utf-8")
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", str(pair)], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 0
    assert result.stderr == ""
    document = json.loads(result.stdout)
    assert result.stdout.encode("utf-8") == sercanon(document, sort_keys=True)
    assert set(document) == {"categories", "config_id", "pair_key", "release_id", "schema", "signals"}
    assert document["release_id"] == identity_meta()["release_id"]

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)
    assert cli(["showcompat", "--pair-file", str(pair)]) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "INCOMPLETE_RELEASE_ROSTER\n"
