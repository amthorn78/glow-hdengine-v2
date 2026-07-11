import json
import subprocess
import sys

from tools.cli import generate_showcompat_artifacts as generator


def test_showcompat_generator_executes_with_active_interpreter(monkeypatch):
    stdout = generator.sercanon({"compat": {"meta": generator.identity_meta()}})
    captured = {}

    def fake_run(args, *, input, capture_output, env):
        captured["args"] = args
        captured["input"] = input
        captured["capture_output"] = capture_output
        captured["env"] = env
        return subprocess.CompletedProcess(args=args, returncode=0, stdout=stdout, stderr=b"")

    monkeypatch.setattr(generator.subprocess, "run", fake_run)

    outputs = generator._capture_outputs()
    args_payload = json.loads(outputs[generator.ARGS_PATH])

    assert captured["args"] == [sys.executable, "scripts/hdctl.py", "showcompat"]
    assert captured["input"] == generator._stdin_bytes()
    assert captured["capture_output"] is True
    assert {key: captured["env"][key] for key in generator.ENV_KEYS} == generator.ENV_PINS
    assert args_payload["argv"] == ["python", "scripts/hdctl.py", "showcompat"]
