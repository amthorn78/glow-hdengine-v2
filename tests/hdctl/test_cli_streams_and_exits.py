from __future__ import annotations
import subprocess, sys

# PF05 CLI/API/Vendor Ref §3.3 and §3.4 Validation (binary): usage errors exit 64,
# stdout empty, stderr a short human synopsis ending with one LF.
USAGE_PREFIX = b"usage: hdctl "

def run(*argv: str):
    p = subprocess.run([sys.executable, "scripts/hdctl.py", *argv],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def test_help_exit0_stdout():
    rc, out, err = run("--help")
    assert rc == 0
    assert out.endswith(b"\n") and len(out) > 1
    assert err == b""

def test_usage_exit64_stderr_no_stdout_on_bad_command():
    rc, out, err = run()  # no args triggers usage
    assert rc == 64
    assert out == b""
    assert err.startswith(USAGE_PREFIX) and err.endswith(b"\n") and not err.endswith(b"\n\n")

    rc2, out2, err2 = run("bogus")
    assert rc2 == 64 and out2 == b""
    assert err2.startswith(USAGE_PREFIX) and err2.endswith(b"\n") and not err2.endswith(b"\n\n")
