#!/usr/bin/env python3
"""GUARD-001 proof for D26: each format 2.1 check in modification_validate.py fires.

    PYTHONDONTWRITEBYTECODE=1 python3 docs/ephemeral/pe37.stage5/guard_proof.py

For each check, copy the validator to a temporary directory beside a copy of the template, replace
that one check's body with `return []` (or `return [], ...` for the ledger shape), run --selftest
from the copy, and count the cases that now fail. A check whose removal fails no case is not
guarded. The repository copy is never modified. Exit 0 when every check is proven, 1 otherwise.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
PEM = HERE.parents[2] / "prompt_ecosystem_management"

# check -> the stub that disables it
DISABLE = {
    "_format": "return None, None",
    "_reviews_shape": "return [], [r for r in (fm.get('reviews') or []) if isinstance(r, dict)]",
    "_review_caps": "return []",
    "_dry_run_first": "return []",
    "_estimate_check": "return []",
    "_d26_checks": "return []",
}


def selftest(src):
    with tempfile.TemporaryDirectory() as td:
        shutil.copy(PEM / "modification-template.md", td)
        (Path(td) / "modification_validate.py").write_text(src, encoding="utf-8")
        out = subprocess.run([sys.executable, "modification_validate.py", "--selftest"], cwd=td,
                             capture_output=True, text=True, env={"PYTHONDONTWRITEBYTECODE": "1"})
    m = re.search(r"(\d+)/(\d+) selftest cases passed", out.stdout)
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def main():
    original = (PEM / "modification_validate.py").read_text(encoding="utf-8")
    passed, total = selftest(original)
    print(f"intact validator: {passed}/{total}")
    ok = passed == total
    for name, stub in DISABLE.items():
        # each check opens with a one-line docstring; the stub goes directly after it
        pat = re.compile(rf"def {name}\([^)]*\):\n    \"\"\"[^\n]*\"\"\"\n")
        m = pat.search(original)
        if not m:
            print(f"{name}: NOT FOUND")
            ok = False
            continue
        src = original[:m.end()] + f"    {stub}\n" + original[m.end():]
        p, t = selftest(src)
        failing = None if p is None else t - p
        print(f"{name} disabled: {p}/{t} pass, {failing} case(s) fail")
        ok = ok and bool(failing)
    print("GUARD-001: every D26 check fires" if ok else "GUARD-001: NOT PROVEN")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
