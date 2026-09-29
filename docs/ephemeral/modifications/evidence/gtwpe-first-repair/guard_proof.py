#!/usr/bin/env python3
"""Guard proof for gtwpe_record_check.py: each check, disabled in a scratch copy, fails its own cases.

    PYTHONDONTWRITEBYTECODE=1 python3 guard_proof.py <gtwpe_record_check.py> <repository root>

First the unmodified tool's --selftest must pass in a scratch tree that holds copies of the repository's
modification_validate.py and modification-template.md. Then, for each check function below, a copy has
that function's body replaced by `return []`, and its --selftest must report exactly the cases listed as
NOT caught, and no other failure. Exit 0 when all five runs hold. It writes only under a temporary
directory, which it removes. Evidence for MODIFICATION-20260929-gtwpe-first-repair (GUARD-001).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED = {
    "_shared_check": {"a shared rule broken: PLAN approval missing at COMPLETE"},
    "_ecosystem_check": {"ecosystem key absent", "ecosystem names another ecosystem"},
    "_harness_check": {"§A has no Harness files subsection", "§P has no Harness files subsection",
                       "§E has no Harness files subsection at COMPLETE",
                       "§A's Harness files heading has no content", "§A's Harness files moved under §P"},
    "_dry_run_check": {"an ANALYZE dry run with no Dry run subsection in §A",
                       "a PLAN dry run with no Dry run subsection in §P",
                       "a SKILL dry run with no Dry run subsection in §E"},
}


def run(tool_text, repo, name):
    with tempfile.TemporaryDirectory() as td:
        pem = Path(td) / "docs" / "prompt_ecosystem_management"
        (pem / "gtwpe").mkdir(parents=True)
        for f in ("modification_validate.py", "modification-template.md"):
            shutil.copyfile(repo / "docs" / "prompt_ecosystem_management" / f, pem / f)
        tool = pem / "gtwpe" / "gtwpe_record_check.py"
        tool.write_text(tool_text, encoding="utf-8")
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        out = subprocess.run([sys.executable, str(tool), "--selftest"], capture_output=True, text=True,
                             env=env).stdout
    not_caught = set(re.findall(r"^SELFTEST FAIL: NOT caught: (.+?) \(expected", out, re.M))
    other = [line for line in out.splitlines()
             if line.startswith("SELFTEST FAIL") and not line.startswith("SELFTEST FAIL: NOT caught")]
    summary = [line for line in out.splitlines() if "selftest cases passed" in line]
    return not_caught, other, summary[-1] if summary else "(no summary line)"


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip())
        return 2
    text = Path(argv[1]).read_text(encoding="utf-8")
    repo = Path(argv[2]).resolve()
    failures = 0
    not_caught, other, summary = run(text, repo, "unmodified")
    if not_caught or other:
        print(f"FAIL  unmodified tool: {summary}; not caught {sorted(not_caught)}; other {other}")
        failures += 1
    else:
        print(f"ok    unmodified tool: {summary}")
    for name, expected in EXPECTED.items():
        pattern = re.compile(rf"^(def {name}\([^)]*\):\n)", re.M)
        if len(pattern.findall(text)) != 1:
            print(f"FAIL  {name}: its def line is not found exactly once")
            failures += 1
            continue
        disabled = pattern.sub(r"\1    return []\n", text, count=1)
        not_caught, other, summary = run(disabled, repo, name)
        if not_caught == expected and not other:
            print(f"ok    {name} disabled: exactly its {len(expected)} case(s) fail ({summary})")
        else:
            print(f"FAIL  {name} disabled: not caught {sorted(not_caught)}, expected {sorted(expected)}; "
                  f"other failures {other}")
            failures += 1
    print(f"\n{1 + len(EXPECTED) - failures}/{1 + len(EXPECTED)} guard-proof runs held")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
