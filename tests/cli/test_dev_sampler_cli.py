import json
import os
import subprocess
import sys


def _rails_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "APP_ENV": "dev",
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        }
    )
    return env


def _write_candidates(tmp_path) -> str:
    payload = {
        "candidates": [
            {"person_uid": "alpha", "weight": 2, "compat_score": 70, "band": "Warm"},
            {"person_uid": "bravo", "weight": 2, "compat_score": 80, "band": "Glow"},
            {"person_uid": "charlie", "weight": 1, "compat_score": 90, "band": "Glow"},
        ]
    }
    path = tmp_path / "candidates.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return str(path)


def _run_sampler(tmp_path, seed: str | None = None) -> subprocess.CompletedProcess:
    candidates_path = _write_candidates(tmp_path)
    cmd = [
        sys.executable,
        "-m",
        "engine.cli",
        "dev:sampler",
        "--viewer",
        "viewer-001",
        "--candidates-file",
        candidates_path,
    ]
    if seed is not None:
        cmd.extend(["--seed", seed])
    return subprocess.run(cmd, capture_output=True, text=True, env=_rails_env())


def test_dev_sampler_two_run_identity(tmp_path):
    first = _run_sampler(tmp_path, seed="111")
    second = _run_sampler(tmp_path, seed="111")

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    assert first.stdout == second.stdout

    payload = json.loads(first.stdout)
    assert payload["seed"] == "111"
    assert [c["person_uid"] for c in payload["candidates"]] == ["bravo", "alpha", "charlie"]


def test_dev_sampler_seed_echo_changes_only_seed(tmp_path):
    with_seed_a = _run_sampler(tmp_path, seed="111")
    with_seed_b = _run_sampler(tmp_path, seed="222")

    assert with_seed_a.returncode == 0, with_seed_a.stderr
    assert with_seed_b.returncode == 0, with_seed_b.stderr

    payload_a = json.loads(with_seed_a.stdout)
    payload_b = json.loads(with_seed_b.stdout)

    assert payload_a["seed"] == "111"
    assert payload_b["seed"] == "222"
    assert payload_a["candidates"] == payload_b["candidates"]


def test_dev_sampler_command_is_namespaced(tmp_path):
    result = subprocess.run(
        [sys.executable, "-m", "engine.cli", "--help"], capture_output=True, text=True, env=_rails_env()
    )
    assert result.returncode == 0
    assert "dev:sampler" in result.stdout
    assert "DEV/ADMIN ONLY" in result.stdout
