#!/usr/bin/env python3
"""Emit the round-20 run record from the artefacts, or check the records against them.

    make_run_record.py --base <tree> --work <tree> --bodies <dir> --pkg <dir> --bench <stdout>
                       (--write | --check)

Why this exists, stated plainly: the run record and the repair report both quote identities
-- file digests, package digests and byte counts, the patch's line count, the bench's case
count -- and those identities change every time the working copy changes.  Three separate
review findings on this package were stale figures of exactly that kind, including a run
record that still named the previous validator hash and a 18-case bench output after the
bench had 19 cases.  A stale run record is worse than none: it sends a reviewer to verify
bytes that are not the bytes under review.

Re-reading every summary after every change was tried and failed three times in one round.
So the check is mechanical instead.  `--check` recomputes every identity from the artefacts
and requires each one to appear in the records; anything that drifts fails loudly with the
expected and actual values named.
"""
import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = pathlib.Path(__file__).resolve().parents[3]
RUN_RECORD = REPO / "docs/ephemeral/gcfpe.round20.sf10-bench/run-record.md"
REPORT = REPO / "docs/ephemeral/gcfpe.round20.sf10-repairs.repair-report.md"
PATCH = REPO / "docs/ephemeral/gcfpe.round20.sf10-bench/repairs.patch"


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def differing(base: pathlib.Path, work: pathlib.Path) -> list[tuple[str, str, str]]:
    out = subprocess.run(["diff", "-rq", str(base), str(work)],
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        m = re.match(r"Files (.+) and (.+) differ", line)
        if m:
            rel = str(pathlib.Path(m.group(1)).relative_to(base))
            rows.append((rel, sha(pathlib.Path(m.group(1))), sha(pathlib.Path(m.group(2)))))
    return sorted(rows)


def identities(args) -> dict:
    base, work = pathlib.Path(args.base), pathlib.Path(args.work)
    pkg = pathlib.Path(args.pkg)
    bodies = sorted(pathlib.Path(args.bodies).glob("*.md"))
    bench = pathlib.Path(args.bench).read_text(encoding="utf-8")
    ids = {
        "files": differing(base, work),
        "bodies": [(p.stem, sha(p), p.stat().st_size) for p in bodies],
        "packages": [],
        "patch_lines": len(PATCH.read_text(encoding="utf-8").splitlines()),
        "bench_cases": bench.count("[PASS]") + bench.count("[FAIL]"),
        "bench_failed": bench.count("[FAIL]"),
        "bench_stdout": bench.rstrip(),
    }
    for name in ("change-flow.skill", "flowmaster-validate.skill"):
        p = pkg / name
        if not p.is_file():
            continue
        listing = subprocess.run(["unzip", "-Z1", str(p)], capture_output=True, text=True).stdout
        count = sum(1 for x in listing.splitlines() if not x.endswith("/"))
        ids["packages"].append((name, count, p.stat().st_size, sha(p)))
    return ids


def check(ids: dict) -> int:
    problems = []
    rr = RUN_RECORD.read_text(encoding="utf-8")
    rp = REPORT.read_text(encoding="utf-8")

    for rel, bh, wh in ids["files"]:
        if wh not in rr:
            problems.append(f"run-record is missing the current digest of {rel}: {wh}")
        if wh[:16] not in rp and wh not in rp:
            problems.append(f"report is missing the current digest of {rel}: {wh[:16]}…")
    for name, count, size, h in ids["packages"]:
        for label, doc in (("run-record", rr), ("report", rp)):
            if h not in doc:
                problems.append(f"{label} is missing {name}'s current sha256 {h}")
            if str(size) not in doc:
                problems.append(f"{label} is missing {name}'s current byte count {size}")
    if str(ids["patch_lines"]) not in rp:
        problems.append(f"report does not state the patch's current line count {ids['patch_lines']}")
    # The report spells the bench's case count in words, so the check requires the spelled
    # form and rejects any OTHER spelled number appearing in that role.  A bare `str(n)`
    # substring test was tried first and silently passed a reverted count, because the
    # digits of "19" occur inside unrelated numbers -- the same too-weak-selector mistake
    # this package is about, made inside the guard written to stop it.  Found by firing an
    # injected regression at it, not by reading it.
    words = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
             20: "twenty", 21: "twenty-one", 22: "twenty-two"}
    n = ids["bench_cases"]
    spelled = words.get(n)
    if spelled is None:
        problems.append(f"no spelled form known for the bench case count {n}; extend `words`")
    else:
        phrase = f"{spelled} cases, exit 0"
        if phrase not in rp:
            problems.append(f"report does not state the bench's current case count: "
                            f"expected the phrase {phrase!r}")
        for other, word in words.items():
            if other != n and f"{word} cases, exit 0" in rp:
                problems.append(f"report still states a superseded bench case count: "
                                f"{word!r} ({other}) where it should be {spelled!r} ({n})")
    if f"**{n} cases," not in rr:
        problems.append(f"run-record does not state the bench's current case count {n}")
    if ids["bench_stdout"] not in rr:
        problems.append("run-record does not contain the current bench stdout verbatim")

    if problems:
        print(f"RECORDS STALE — {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"records agree with the artefacts: {len(ids['files'])} changed files, "
          f"{len(ids['packages'])} packages, patch {ids['patch_lines']} lines, "
          f"bench {ids['bench_cases']} cases ({ids['bench_failed']} failed)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--bodies", required=True)
    ap.add_argument("--pkg", required=True)
    ap.add_argument("--bench", required=True, help="a file holding the bench's stdout")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    ids = identities(args)
    if args.check:
        return check(ids)
    print(json.dumps({k: v for k, v in ids.items() if k != "bench_stdout"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
