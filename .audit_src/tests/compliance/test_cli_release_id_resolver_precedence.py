import os, subprocess, sys, json, pathlib

CLI = [sys.executable, "scripts/hd_cli.py"]
A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

def _run(env=None):
    p = subprocess.check_output(CLI + [A,B], env=env)
    d = json.loads(p.decode("utf-8"))
    return d

def test_env_precedence_over_file(tmp_path, monkeypatch):
    # Prepare file value (should be ignored)
    art = pathlib.Path("artifacts"); art.mkdir(exist_ok=True)
    (art/"release_id.txt").write_text("file_rel_12345678\n", encoding="utf-8")

    env = dict(os.environ)
    env["RELEASE_ID"] = "devlocal_abcdef12"
    d = _run(env=env)
    assert d["release_id"] == "devlocal_abcdef12"

    # cleanup
    (art/"release_id.txt").unlink(missing_ok=True)

def test_file_used_when_env_missing(tmp_path, monkeypatch):
    art = pathlib.Path("artifacts"); art.mkdir(exist_ok=True)
    (art/"release_id.txt").write_text("file_rel_12345678\n", encoding="utf-8")

    env = dict(os.environ)
    env.pop("RELEASE_ID", None)
    d = _run(env=env)
    assert d["release_id"] == "file_rel_12345678"

    # cleanup
    (art/"release_id.txt").unlink(missing_ok=True)

def test_synth_when_neither_env_nor_file(monkeypatch):
    art = pathlib.Path("artifacts"); art.mkdir(exist_ok=True)
    (art/"release_id.txt").unlink(missing_ok=True)

    env = dict(os.environ)
    env.pop("RELEASE_ID", None)
    d = _run(env=env)
    rid = d["release_id"]
    assert rid.startswith("rel_dev_")
    assert len(rid) >= 8
