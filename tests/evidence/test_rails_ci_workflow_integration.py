from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest

from ci.checks import run_rails_job_definitions as runner
from tools.evidence import generate_rails_gate_evidence as producer

ROOT = Path(__file__).resolve().parents[2]
CMD = "python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml"
DEFS = [
    ROOT / "ci/jobs/rails_closed_refusal.yml",
    ROOT / "ci/jobs/rails_open_conformance.yml",
    ROOT / "ci/jobs/logs_keys_only_redaction.yml",
]


def test_workflow_contains_closed_default_rails_policy_job() -> None:
    text = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    assert "rails-policy-gates:" in text
    assert text.count(CMD) == 1
    start = text.index("  rails-policy-gates:")
    end = text.index("  sanity-pipeline:", start)
    job = text[start:end]
    for needle in ["LC_ALL: C", "LANG: C", "TZ: UTC", 'SAFE_MODE: "1"', 'ALLOW_NETWORK: "0"']:
        assert needle in job
    assert "secrets:" not in job
    assert "${{ secrets." not in job.lower()


def test_job_definitions_are_reusable_secret_free_and_live_forbidden() -> None:
    expected = ["rails_closed_refusal", "rails_open_conformance", "logs_keys_only_redaction"]
    for path, name in zip(DEFS, expected):
        assert path.exists()
        job = runner.validate(path)
        assert job["name"] == name
        assert "hde-epic031" not in job["scope"].lower()
        assert job["live_vendor_calls"] == "forbidden"
        text = path.read_text(encoding="utf-8").lower()
        assert "${{ secrets." not in text
    open_job = runner.validate(DEFS[1])
    assert "fixture-backed" in open_job["scope"] and "non-live" in open_job["scope"]


def _write_def(path: Path, name: str, safe: str, allow: str, command: str, scope: str = "reusable-fixture-backed-mocked-non-live") -> None:
    path.write_text(
        f'''name: {name}\nrails:\n  SAFE_MODE: "{safe}"\n  ALLOW_NETWORK: "{allow}"\n  LC_ALL: C\n  LANG: C\n  TZ: UTC\nscope: {scope}\nlive_vendor_calls: forbidden\nsteps:\n  - command: {command}\n    proves:\n      - local proof\n''',
        encoding="utf-8",
    )


def test_runner_orders_steps_and_isolates_open_environment(tmp_path: Path) -> None:
    probe = tmp_path / "probe.py"
    out = tmp_path / "out.txt"
    probe.write_text(
        "import os,sys,pathlib\npathlib.Path(sys.argv[1]).open('a').write(sys.argv[2]+':' + os.environ['SAFE_MODE'] + ':' + os.environ['ALLOW_NETWORK'] + '\\n')\n",
        encoding="utf-8",
    )
    a, b, c = tmp_path / "a.yml", tmp_path / "b.yml", tmp_path / "c.yml"
    _write_def(a, "rails_closed_refusal", "1", "0", f"{sys.executable} {probe} {out} closed", "reusable-closed")
    _write_def(b, "rails_open_conformance", "0", "1", f"{sys.executable} {probe} {out} open")
    _write_def(c, "logs_keys_only_redaction", "1", "0", f"{sys.executable} {probe} {out} logs", "reusable-logs")
    assert runner.main([str(a), str(b), str(c)]) == 0
    assert out.read_text(encoding="utf-8").splitlines() == ["closed:1:0", "open:0:1", "logs:1:0"]
    assert os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1"


def test_runner_scrubs_ambient_vendor_credentials_from_child_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for key in runner.CREDENTIAL_ENV_NAMES:
        monkeypatch.setenv(key, f"ambient-{key.lower()}")
    probe = tmp_path / "probe.py"
    out = tmp_path / "out.txt"
    probe.write_text(
        "import os,sys,pathlib\nkeys=sys.argv[2:]\npathlib.Path(sys.argv[1]).write_text('\\n'.join(k for k in keys if os.environ.get(k))+'\\n', encoding='utf-8')\n",
        encoding="utf-8",
    )
    job = {
        "name": "rails_open_conformance",
        "rails": {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"},
        "steps": [{"command": f"{sys.executable} {probe} {out} " + " ".join(sorted(runner.CREDENTIAL_ENV_NAMES))}],
    }

    assert runner.run_job(job) == 0
    assert out.read_text(encoding="utf-8") == "\n"
    for key in runner.CREDENTIAL_ENV_NAMES:
        assert os.environ[key] == f"ambient-{key.lower()}"


@pytest.mark.parametrize(
    "mutate, expected",
    [
        (lambda s: s.replace("rails_closed_refusal", "unknown_identity"), "unknown"),
        (lambda s: s.replace("reusable-closed", "hde-epic031-pr-01"), "EPIC031"),
        (lambda s: s.replace("live_vendor_calls: forbidden", "live_vendor_calls: allowed"), "live_vendor_calls"),
        (lambda s: s + "secrets:\n  HD_API_KEY: value\n", "credential"),
        (lambda s: s.replace("local proof", "${{ secrets.HD_API_KEY }}"), "secrets"),
        (lambda s: s.replace("steps:\n  - command:", "steps:\n  - nope:"), "step"),
    ],
)
def test_runner_rejects_invalid_definitions(tmp_path: Path, mutate, expected: str) -> None:
    good = '''name: rails_closed_refusal\nrails:\n  SAFE_MODE: "1"\n  ALLOW_NETWORK: "0"\n  LC_ALL: C\n  LANG: C\n  TZ: UTC\nscope: reusable-closed\nlive_vendor_calls: forbidden\nsteps:\n  - command: python -c 'print("ok")'\n    proves:\n      - local proof\n'''
    bad = tmp_path / "bad.yml"
    bad.write_text(mutate(good), encoding="utf-8")
    with pytest.raises(Exception) as excinfo:
        runner.validate(bad)
    assert expected.lower() in str(excinfo.value).lower()


def test_runner_rejects_duplicate_and_stops_on_failure(tmp_path: Path) -> None:
    a, b = tmp_path / "a.yml", tmp_path / "b.yml"
    _write_def(a, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'raise SystemExit(3)'", "reusable-closed")
    _write_def(b, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'print(1)'", "reusable-closed")
    assert runner.main([str(a), str(b)]) == 2
    c, d = tmp_path / "c.yml", tmp_path / "d.yml"
    _write_def(c, "rails_closed_refusal", "1", "0", f"{sys.executable} -c 'raise SystemExit(3)'", "reusable-closed")
    _write_def(d, "rails_open_conformance", "0", "1", f"{sys.executable} -c 'print(1)'")
    assert runner.run_job(runner.validate(c)) == 3


def test_producer_check_mode_does_not_modify_files() -> None:
    paths = [ROOT / producer.OPS_REFUSAL_REL, ROOT / producer.RETRY_AFTER_REL, ROOT / producer.KEYS_ONLY_REL]
    before = {p: p.read_bytes() for p in paths if p.exists()}
    producer.generate(check=True)
    after = {p: p.read_bytes() for p in paths if p.exists()}
    assert before == after


def test_producer_validation_failure_leaves_existing_output_unchanged(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    target = tmp_path / "sample.txt"
    target.write_text("original\n", encoding="utf-8")
    monkeypatch.setattr(producer, "KEYS_ONLY_REL", str(target.relative_to(ROOT)) if target.is_relative_to(ROOT) else producer.KEYS_ONLY_REL)
    monkeypatch.setattr(producer, "expected_outputs", lambda: (_ for _ in ()).throw(SystemExit("boom")))
    with pytest.raises(SystemExit):
        producer.generate(check=False)
    assert target.read_text(encoding="utf-8") == "original\n"


def test_refusal_proof_forces_closed_env_without_leaking(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    text = producer.build_ops_refusal()
    assert "x-rails-mode: closed" in text
    assert "rails remain closed" in text
    assert os.environ["SAFE_MODE"] == "0"
    assert os.environ["ALLOW_NETWORK"] == "1"


def test_rails_keys_only_uses_dedicated_vendor_artifact_path() -> None:
    assert producer.KEYS_ONLY_REL == "artifacts/vendor/rails_gate_keys_only.logs.sample"
    assert producer.KEYS_ONLY_REL != "artifacts/bodygraph/keys_only.logs.sample"
    assert (ROOT / "scripts/bodygraph/run_refresh_worker.py").read_text(encoding="utf-8").find("artifacts/bodygraph/keys_only.logs.sample") > -1


def test_fixture_backed_open_rails_tests_do_not_reach_real_network() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/bodygraph/test_vendor_client.py", "-q"],
        cwd=ROOT,
        env={**os.environ, "SAFE_MODE": "0", "ALLOW_NETWORK": "1", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"},
        text=True,
        capture_output=True,
        timeout=120,
    )
    assert result.returncode == 0, result.stdout + result.stderr
