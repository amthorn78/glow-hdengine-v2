import os
import socket
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
HEALTHCHECK = REPO_ROOT / "scripts" / "qa" / "dev_sampler_healthcheck.py"
def _find_open_port() -> int:
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    _, port = sock.getsockname()
    sock.close()
    return port


def test_dev_sampler_healthcheck_runs(tmp_path):
    port = _find_open_port()
    log_dir = tmp_path / "logs"
    log_path = log_dir / "healthcheck.log"
    env = os.environ.copy()
    env.update(
        {
            "DEV_SAMPLER_URL": f"http://127.0.0.1:{port}/internal/dev/sampler",
            "APP_ENV": "dev",
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "PORT": str(port),
            "DEV_SAMPLER_LOG_DIR": str(log_dir),
            "DEV_SAMPLER_LOG_PATH": str(log_path),
        }
    )

    result = subprocess.run(
        [sys.executable, str(HEALTHCHECK)],
        cwd=REPO_ROOT,
        env=env,
        text=True,
        capture_output=True,
        timeout=120,
    )

    assert result.returncode == 0, f"stdout: {result.stdout}\nstderr: {result.stderr}"

    log_text = log_path.read_text(encoding="utf-8")
    assert "sampler_response mode=dev" in log_text
    assert "status=200" in log_text
