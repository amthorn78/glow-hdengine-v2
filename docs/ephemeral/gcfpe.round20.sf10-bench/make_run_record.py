#!/usr/bin/env python3
"""Emit the round-20 run record from the artefacts, or check the records against them.

    make_run_record.py --base <tree> --work <tree> --bodies <dir> --pkg <dir>
                       [--registry <path>] (--write | --check)

The bench is RUN by this script, not supplied to it: its stdout and its exit status are
observed here, so neither can be asserted by the caller.

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
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = pathlib.Path(__file__).resolve().parents[3]
RUN_RECORD = REPO / "docs/ephemeral/gcfpe.round20.sf10-bench/run-record.md"
REPORT = REPO / "docs/ephemeral/gcfpe.round20.sf10-repairs.repair-report.md"
PATCH = REPO / "docs/ephemeral/gcfpe.round20.sf10-bench/repairs.patch"

# The frozen installed tree this package was prepared against.  A copy reproduces this
# digest exactly -- verified -- because the recipe hashes paths relative to the tree root:
#   find . -type f ! -name manifest.json -print0 | sort -z | xargs -0 sha256sum | sha256sum
# `manifest.json` is excluded because the sync rewrites it.
FREEZE_FILES = 321
FREEZE_FILES_EXCL_MANIFEST = 320
FREEZE_DIGEST = "c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb"
EXPECTED_PACKAGES = ("change-flow.skill", "flowmaster-validate.skill")
BENCH = REPO / "docs/ephemeral/gcfpe.round20.sf10-bench/bench.py"
REGISTRY_DEFAULT_REL = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tree_identity(root: pathlib.Path) -> tuple[int, int, str]:
    """Total files, files excluding manifest.json, and the freeze digest of `root`."""
    files = sorted(q for q in root.rglob("*") if q.is_file())
    counted = [q for q in files if q.name != "manifest.json"]
    h = hashlib.sha256()
    for q in sorted(counted, key=lambda x: x.relative_to(root).as_posix()):
        line = f"{sha(q)}  ./{q.relative_to(root).as_posix()}\n"
        h.update(line.encode())
    return len(files), len(counted), h.hexdigest()


def differing(base: pathlib.Path, work: pathlib.Path) -> list[tuple[str, str, str]]:
    """The two-way change roster between the trees, or a hard failure.

    Three holes closed here, each of which let `--check` certify a work tree that was not
    the reviewed one -- measured, not theorised:

      * `--work` pointing at the SAME tree as `--base` produced "0 changed files" and
        exit 0, so a tree containing NONE of the repairs was certified;
      * an added or deleted file makes `diff` print "Only in ...", which the old parser
        ignored entirely, so a one-sided change was invisible;
      * `--work` pointing at a nonexistent path produced "0 changed files" and exit 0,
        because the parser read stdout and never looked at the command's status.

    `diff -rq` exits 0 when the trees are identical, 1 when they differ, and 2 on error.
    Only 1 is acceptable here: the reviewed package differs from the freeze, and an
    identical or unreadable tree is a caller error rather than a finding.
    """
    for label, d in (("--base", base), ("--work", work)):
        if not d.is_dir():
            raise SystemExit(f"{label} is not a directory: {d}")
    proc = subprocess.run(["diff", "-rq", str(base), str(work)], capture_output=True, text=True)
    if proc.returncode == 0:
        raise SystemExit(f"--work is identical to --base ({work}); it carries none of the "
                         f"repairs, so there is nothing to record")
    if proc.returncode != 1:
        raise SystemExit(f"diff -rq failed with status {proc.returncode}: "
                         f"{proc.stderr.strip() or 'no stderr'}")
    rows, one_sided = [], []
    for line in proc.stdout.splitlines():
        m = re.match(r"Files (.+) and (.+) differ", line)
        if m:
            rel = str(pathlib.Path(m.group(1)).relative_to(base))
            rows.append((rel, sha(pathlib.Path(m.group(1))), sha(pathlib.Path(m.group(2)))))
            continue
        if line.startswith("Only in "):
            one_sided.append(line)
    if one_sided:
        raise SystemExit("the trees differ by added or deleted files, which the reviewed "
                         "package does not contain:\n  " + "\n  ".join(one_sided))
    if not rows:
        raise SystemExit("diff reported a difference but no changed files were parsed; "
                         "refusing to record an empty roster")
    return sorted(rows)


def run_bench(args) -> tuple[str, int]:
    """Run the bench and return its stdout and its ACTUAL exit status.

    The previous revision took the status as a `--bench-exit` integer and trusted it.  That
    was unenforced: a bench that exits nonzero before printing any `[FAIL]` -- a corpus gate
    refusal or an import failure, which print `HARNESS FAILURE` and stop -- could be recorded
    as a success by a caller passing 0.

    I declined to run the bench here in the previous round, on the grounds that it would put
    the subject and the recorder in one process and reintroduce the "harness tests its
    author's copy" problem.  **That reasoning was wrong.** A subprocess is not the same
    process: the bench is executed as its own interpreter against its own inputs, and the
    recorder observes only its stdout and status. Subprocess isolation is precisely what
    keeps them separate, so the objection did not apply and the status stayed trusted for a
    round longer than it should have.
    """
    cmd = [sys.executable, str(BENCH),
           "--base", args.base, "--work", args.work, "--bodies", args.bodies,
           "--registry", args.registry]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    out = proc.stdout
    if "HARNESS FAILURE" in out:
        raise SystemExit("the bench reported a HARNESS FAILURE; its output is not a result:\n"
                         + "\n".join(l for l in out.splitlines() if "HARNESS FAILURE" in l))
    if proc.returncode == 0 and "ALL CASES AS EXPECTED" not in out:
        raise SystemExit("the bench exited 0 without its terminal success marker; refusing to "
                         "record an unrecognised outcome")
    return out.rstrip(), proc.returncode


def identities(args) -> dict:
    base, work = pathlib.Path(args.base), pathlib.Path(args.work)
    pkg = pathlib.Path(args.pkg)
    bodies = sorted(pathlib.Path(args.bodies).glob("*.md"))
    bench, bench_exit = run_bench(args)
    total, counted, digest = tree_identity(base)
    ids = {
        "base_tree": (total, counted, digest),
        "files": differing(base, work),
        "bodies": [(p.stem, sha(p), p.stat().st_size) for p in bodies],
        "packages": [],
        "patch_lines": len(PATCH.read_text(encoding="utf-8").splitlines()),
        "bench_cases": bench.count("[PASS]") + bench.count("[FAIL]"),
        "bench_failed": bench.count("[FAIL]"),
        "bench_exit": bench_exit,
        "bench_stdout": bench.rstrip(),
    }
    # Both archives are required.  A silent skip let --check succeed with one package or
    # none, and let --write delete the absent rows from a record that claims identities for
    # both deliverables -- the same "computed then discarded" shape as the corpus defect.
    missing = [n for n in EXPECTED_PACKAGES if not (pkg / n).is_file()]
    if missing:
        raise SystemExit(f"missing package artefact(s) in {pkg}: {', '.join(missing)}")
    for name in EXPECTED_PACKAGES:
        p = pkg / name
        listing = subprocess.run(["unzip", "-Z1", str(p)], capture_output=True, text=True).stdout
        count = sum(1 for x in listing.splitlines() if not x.endswith("/"))
        ids["packages"].append((name, count, p.stat().st_size, sha(p)))
    return ids


MARK_FILES = ("| file | base sha256 | work sha256 |", "|---|---|---|")
MARK_PKG = ("| package | files | bytes | sha256 |", "|---|---|---|---|")
MARK_BODIES = ("| prompt | sha256 | bytes |", "|---|---|---|")


def render_table(header: tuple[str, str], rows: list[str]) -> str:
    return "\n".join([header[0], header[1], *rows])


def files_table(ids: dict) -> str:
    return render_table(MARK_FILES, [f"| `{r}` | `{b}` | `{w}` |" for r, b, w in ids["files"]])


def packages_table(ids: dict) -> str:
    return render_table(MARK_PKG,
                        [f"| `{n}` | {c} | {s} | `{h}` |" for n, c, s, h in ids["packages"]])


def bodies_table(ids: dict) -> str:
    return render_table(MARK_BODIES,
                        [f"| `{k}` | `{h}` | {s} |" for k, h, s in ids["bodies"]])


def bench_block(ids: dict) -> str:
    return (f"Exit {ids['bench_exit']}. **{ids['bench_cases']} cases, "
            f"{ids['bench_failed']} not as expected.** "
            f"Full stdout:\n\n```\n{ids['bench_stdout']}\n```")


def replace_table(doc: str, header: tuple[str, str], new_block: str, label: str) -> str:
    pat = re.compile(re.escape(header[0]) + r"\n" + re.escape(header[1]) + r"\n(?:\|[^\n]*\|\n?)+")
    m = pat.search(doc)
    if not m:
        raise SystemExit(f"cannot find the {label} table in the run record")
    return doc[:m.start()] + new_block + "\n" + doc[m.end():]


def write_records(ids: dict) -> int:
    doc = RUN_RECORD.read_text(encoding="utf-8")
    doc = replace_table(doc, MARK_FILES, files_table(ids), "changed-files")
    doc = replace_table(doc, MARK_PKG, packages_table(ids), "packages")
    doc = replace_table(doc, MARK_BODIES, bodies_table(ids), "bodies")
    pat = re.compile(r"Exit \d+\. \*\*\d+ cases, \d+ not as expected\.\*\* Full stdout:\n\n```\n.*?\n```",
                     re.S)
    m = pat.search(doc)
    if not m:
        raise SystemExit("cannot find the bench section in the run record")
    doc = doc[:m.start()] + bench_block(ids) + doc[m.end():]
    RUN_RECORD.write_text(doc, encoding="utf-8")
    print(f"run record regenerated: {len(ids['files'])} changed files, "
          f"{len(ids['bodies'])} bodies, {len(ids['packages'])} packages, "
          f"bench {ids['bench_cases']} cases")
    return 0


def check(ids: dict) -> int:
    problems = []
    rr = RUN_RECORD.read_text(encoding="utf-8")
    rp = REPORT.read_text(encoding="utf-8")

    # The bench's success is an observed exit status, never inferred from its stdout.  An
    # earlier revision hard-coded "Exit 0" into the rendered block and counted [FAIL]
    # without rejecting a nonzero count, so a FAILING bench could be written into the record
    # and then certified as agreeing with the artefacts.  That is the harness-reports-success
    # family this whole package exists to stop, in the recorder itself.
    if ids["bench_exit"] != 0:
        problems.append(f"the bench exited {ids['bench_exit']}, not 0; its result cannot be "
                        f"recorded as evidence")
    if ids["bench_failed"] != 0:
        problems.append(f"the bench reported {ids['bench_failed']} case(s) not as expected; "
                        f"its result cannot be recorded as evidence")

    # The base tree is identified in full, not merely diffed against work.  Both trees could
    # come from the same stale or corrupted freeze and every shared change would be invisible
    # to a relative diff.
    total, counted, digest = ids["base_tree"]
    if (total, counted) != (FREEZE_FILES, FREEZE_FILES_EXCL_MANIFEST):
        problems.append(f"--base holds {total} files ({counted} excluding manifest.json); "
                        f"the freeze is {FREEZE_FILES} ({FREEZE_FILES_EXCL_MANIFEST})")
    if digest != FREEZE_DIGEST:
        problems.append(f"--base does not reproduce the frozen tree digest: got {digest}, "
                        f"expected {FREEZE_DIGEST}")
    if FREEZE_DIGEST not in rr:
        problems.append("run-record does not state the frozen tree digest")

    # The roster is compared in both directions.  The old check only asked whether every
    # file it found was in the record, never whether every file in the record was found --
    # so a work tree with zero differences passed while the record claimed nine files.
    recorded_files = set(re.findall(r"^\| `([^`]+)` \| `[0-9a-f]{64}` \| `[0-9a-f]{64}` \|$",
                                    rr, re.M))
    found_files = {rel for rel, _b, _w in ids["files"]}
    for gone in sorted(recorded_files - found_files):
        problems.append(f"run record lists changed file {gone!r}, which the supplied trees do "
                        f"not differ in")
    for extra in sorted(found_files - recorded_files):
        problems.append(f"the supplied trees differ in {extra!r}, which the run record does "
                        f"not list")

    for rel, bh, wh in ids["files"]:
        if bh not in rr:
            problems.append(f"run-record is missing the BASE digest of {rel}: {bh}")
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

    # The corpus is verified, not merely computed.  An earlier revision of this checker
    # built `ids["bodies"]` -- 55 prompt ids, digests and byte counts -- and then never
    # read it, so `--check` could print "records agree with the artefacts" having compared
    # no body at all.  That is the bench's own original defect (a corpus accepted by count
    # while the docstring promised a digest check) reproduced inside the guard written to
    # stop stale records.  Roster first, then every digest and size.
    if not ids["bodies"]:
        problems.append("no bodies were supplied, so the corpus cannot be verified")
    if len(ids["bodies"]) != 55:
        problems.append(f"expected 55 bodies, found {len(ids['bodies'])}")
    missing_rows = [k for k, h, s in ids["bodies"] if f"| `{k}` | `{h}` | {s} |" not in rr]
    if missing_rows:
        problems.append(f"{len(missing_rows)} body row(s) in the run record do not match the "
                        f"supplied corpus: {missing_rows[:5]}"
                        + (" …" if len(missing_rows) > 5 else ""))
    recorded = set(re.findall(r"^\| `([A-Z][A-Z0-9-]*)` \| `[0-9a-f]{64}` \| \d+ \|$",
                              rr, re.M))
    supplied = {k for k, _h, _s in ids["bodies"]}
    for extra in sorted(recorded - supplied):
        problems.append(f"run record lists body {extra!r}, which the supplied corpus does not "
                        f"contain")

    if problems:
        print(f"RECORDS STALE — {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"records agree with the artefacts: {len(ids['files'])} changed files, "
          f"{len(ids['packages'])} packages, patch {ids['patch_lines']} lines, "
          f"bench {ids['bench_cases']} cases ({ids['bench_failed']} failed, "
          f"exit {ids['bench_exit']}), base tree {ids['base_tree'][0]} files / "
          f"{ids['base_tree'][2][:16]}…")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--bodies", required=True)
    ap.add_argument("--pkg", required=True)
    ap.add_argument("--registry", default=str(REPO / REGISTRY_DEFAULT_REL),
                    help="the prompt-contract registry the bench verifies the corpus against")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    ids = identities(args)
    if args.check:
        return check(ids)
    return write_records(ids)


if __name__ == "__main__":
    sys.exit(main())
