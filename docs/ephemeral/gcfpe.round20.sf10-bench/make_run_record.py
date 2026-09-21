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
import difflib
import hashlib
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

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
FLOWMASTER_REL = "flowmaster-validate/scripts/validate_flowmaster.py"
REGISTRY_DEFAULT_REL = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"


def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def regular_files(root: pathlib.Path, label: str) -> list[pathlib.Path]:
    """Every REGULAR file under `root`, refusing any symlink.

    One root cause behind three findings: `is_file()` FOLLOWS symlinks and `sha()` then hashes
    the target, so every traversal in this file erased node type.  A symlink at a frozen path
    pointing to byte-identical content preserved the file count, the relative-path digest and
    the tree diff; and the documented freeze recipe is `find . -type f`, which does not match a
    symlink at all, so the implementation and the recipe it claims to implement disagreed.

    The recipe is implemented exactly -- symlinks are not counted -- AND a symlink anywhere in
    a supplied tree is refused, because a digest computed over regular files cannot see one
    being added.  The freeze provably contains none today, so this is a guard against
    reintroduction rather than a fix to a current tree.
    """
    links = sorted(q for q in root.rglob("*") if q.is_symlink())
    if links:
        raise SystemExit(f"{label} contains {len(links)} symlink(s), which the freeze recipe "
                         f"(`find . -type f`) does not count and a content digest cannot see: "
                         f"{[q.relative_to(root).as_posix() for q in links[:5]]}")
    return sorted(q for q in root.rglob("*") if q.is_file())


def payload_map(root: pathlib.Path, label: str) -> dict[str, str]:
    """Every regular file under `root`, as relative path -> sha256."""
    return {q.relative_to(root).as_posix(): sha(q)
            for q in regular_files(root, label)}


def canonical_patch(text: str, base: pathlib.Path = None, work: pathlib.Path = None) -> str:
    """A patch's content without its per-run mtimes.

    `diff -ru` writes `--- base/path\t<mtime>` and `+++ work/path\t<mtime>`, so two runs over
    identical trees produce different bytes.  Dropping the tab-separated timestamp leaves the
    part that is actually the change, which is what the committed patch is supposed to be.
    """
    subs = []
    if base is not None:
        subs.append((str(pathlib.Path(base)).rstrip("/"), "base"))
    if work is not None:
        subs.append((str(pathlib.Path(work)).rstrip("/"), "work"))
    out = []
    for line in text.splitlines():
        if line.startswith(("--- ", "+++ ")) and "\t" in line:
            line = line.split("\t", 1)[0]
        # How the trees were ADDRESSED is not part of the change.  The committed patch was
        # generated from a parent directory with relative `base`/`work` arguments; regenerating
        # with absolute paths produced different header text and the comparison failed on a
        # difference that was not a difference.  Normalising both sides to the same tokens is
        # what makes the content comparison mean what it claims.
        for actual, token in subs:
            line = line.replace(actual, token)
        out.append(line)
    return "\n".join(out)


def flowmaster_diff(base: pathlib.Path,
                    work: pathlib.Path) -> tuple[str, int, tuple[int, int]]:
    """Run the whole-ecosystem validator on both trees and return the difference itself.

    The records used to SUMMARISE this run in prose -- "the whole report differs in 2 lines,
    the fixture-source path and the validator revision" -- and nothing recomputed it.  The
    SF10-04 roster retirement landed in this same round and removed a six-line
    `flowmaster-propagate` block from the work-side report, so the summary became false in
    both documents while the commit that falsified it sat a few hundred lines away in one of
    them.  Same family as every other defect in this file: a claim about an output, asserted
    rather than derived.  So the output is regenerated and embedded instead of described, the
    way the bench's stdout already is.

    Each tree's OWN copy of the validator is used, because `DEFAULT_ROOT` is the tree holding
    the script -- that is what makes a scratch copy validate itself rather than the install.

    The two tree root paths are normalised to `<tree>`.  The report prints `fixture_source` as
    an absolute path, so without that the diff would carry a difference that is only where the
    copies happen to live.  The substitution is of those two exact roots, not a pattern, so it
    cannot mask anything else.
    """
    out, exits = {}, {}
    for label, root in (("base", base), ("work", work)):
        # Resolved, because the run sets `cwd` to the tree: a relative `--base` would then be
        # re-interpreted against the new working directory and Python would exit 2 on a script
        # it could not open -- which is exactly what happened, and is why the exit status is
        # checked rather than the output being parsed for a verdict.
        root = pathlib.Path(root).resolve()
        script = root / FLOWMASTER_REL
        if not script.is_file():
            raise SystemExit(f"--{label} has no {FLOWMASTER_REL} to run")
        r = subprocess.run([sys.executable, str(script)], capture_output=True, text=True,
                           cwd=str(root))
        out[label], exits[label] = r.stdout, r.returncode
    roots = sorted((str(pathlib.Path(base).resolve()), str(pathlib.Path(work).resolve())),
                   key=len, reverse=True)

    def norm(text: str) -> str:
        for r in roots:
            text = text.replace(r, "<tree>")
        return text

    d = difflib.unified_diff(norm(out["base"]).splitlines(), norm(out["work"]).splitlines(),
                             "base", "work", lineterm="", n=1)
    body = list(d)
    changed = sum(1 for line in body[2:] if line[:1] in "+-")
    return "\n".join(body), changed, (exits["base"], exits["work"])


def tree_identity(root: pathlib.Path, label: str) -> tuple[int, int, str]:
    """Total regular files, files excluding manifest.json, and the freeze digest of `root`."""
    files = regular_files(root, label)
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
    rows, one_sided, unparsed = [], [], []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        m = re.match(r"Files (.+) and (.+) differ", line)
        if m:
            rel = str(pathlib.Path(m.group(1)).relative_to(base))
            rows.append((rel, sha(pathlib.Path(m.group(1))), sha(pathlib.Path(m.group(2)))))
            continue
        if line.startswith("Only in "):
            one_sided.append(line)
            continue
        # Anything else is refused rather than ignored.  `diff -rq` has output shapes beyond
        # "Files ... differ" and "Only in ...": a file-type change prints "File X is a regular
        # file while file Y is a directory", and symlink or unreadable-file notices print their
        # own forms.  The old parser recognised two shapes and let every other line fall through
        # silently, so a roster missing a real difference was certified from the rows that did
        # parse.  Recognising some inputs and ignoring the rest is the same defect as accepting
        # a subprocess's output without its status.
        unparsed.append(line)
    if one_sided:
        raise SystemExit("the trees differ by added or deleted files, which the reviewed "
                         "package does not contain:\n  " + "\n  ".join(one_sided))
    if unparsed:
        raise SystemExit("diff -rq produced output this parser does not recognise; refusing to "
                         "certify a possibly incomplete roster:\n  " + "\n  ".join(unparsed))
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
    # Refused HERE, not in check().  An ordinary failing case exits nonzero without printing
    # HARNESS FAILURE, and with the refusal living only in check() the --write path recorded
    # "Exit 1" and then exited 0 -- so the report's claim that failures are rejected before
    # anything is recorded was true of --check and false of --write.  Both modes now stop at
    # the same point, before any record is touched.
    failed = out.count("[FAIL]")
    if proc.returncode != 0 or failed:
        raise SystemExit(
            f"the bench exited {proc.returncode} with {failed} case(s) not as expected; "
            f"refusing to record or check against a failing bench")
    return out.rstrip(), proc.returncode


def identities(args) -> dict:
    """Gather every identity, and REFUSE any input that is not what it claims to be.

    This is the single gate both `--write` and `--check` pass through, and that placement is
    the point.  Input validation used to sit wherever it was first written -- the freeze
    count and digest were asserted in `check()` only, so `--write` could derive changed-file
    rows from a stale or modified base tree and still return success, leaving the record's
    fixed base identity in place.  The same mistake had already been found once and fixed
    once, for the bench refusal, and not propagated to its siblings.  Validating an input
    where it enters, rather than in whichever mode happened to grow the check, is what stops
    that recurring.
    """
    base, work = pathlib.Path(args.base), pathlib.Path(args.work)
    pkg = pathlib.Path(args.pkg)
    bodies = sorted(pathlib.Path(args.bodies).glob("*.md"))
    bench, bench_exit = run_bench(args)

    total, counted, digest = tree_identity(base, "--base")
    if (total, counted) != (FREEZE_FILES, FREEZE_FILES_EXCL_MANIFEST):
        raise SystemExit(f"--base holds {total} files ({counted} excluding manifest.json); the "
                         f"freeze is {FREEZE_FILES} ({FREEZE_FILES_EXCL_MANIFEST})")
    if digest != FREEZE_DIGEST:
        raise SystemExit(f"--base does not reproduce the frozen tree digest: got {digest}, "
                         f"expected {FREEZE_DIGEST}")

    fm_text, fm_changed, fm_exits = flowmaster_diff(base, work)
    # The records state exit 0 for both copies.  A nonzero run must not be summarised as a
    # difference count -- that is the harness-reports-success shape again, one level up.
    if fm_exits != (0, 0):
        raise SystemExit(f"validate_flowmaster.py exited {fm_exits[0]} on --base and "
                         f"{fm_exits[1]} on --work; the records claim 0 on both")

    ids = {
        "base_tree": (total, counted, digest),
        "base_pyc": sum(1 for q in base.rglob("*.pyc")),
        "fm_diff": fm_text,
        "fm_changed": fm_changed,
        "files": differing(base, work),
        "bodies": [(p.stem, sha(p), p.stat().st_size) for p in bodies],
        "bodies_bytes": sum(p.stat().st_size for p in bodies),
        "packages": [],
        "patch_lines": len(PATCH.read_text(encoding="utf-8").splitlines()),
        "patch_sha": hashlib.sha256(
            canonical_patch(PATCH.read_text(encoding="utf-8"), base, work).encode()).hexdigest(),
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
        # The archive must be READABLE, not merely present.  `unzip -Z1` exits nonzero on a
        # corrupt or non-ZIP file and prints nothing, and treating that empty stdout as a
        # zero-file package let an unusable deliverable be recorded successfully.  Existence
        # was enforced; integrity was not.
        listing = subprocess.run(["unzip", "-Z1", str(p)], capture_output=True, text=True)
        if listing.returncode != 0:
            raise SystemExit(f"{name} is present but not a readable archive (unzip exited "
                             f"{listing.returncode}): {listing.stderr.strip() or 'no stderr'}")
        count = sum(1 for x in listing.stdout.splitlines() if not x.endswith("/"))
        if count == 0:
            raise SystemExit(f"{name} contains no files; refusing to record an empty package")

        # Entry TYPES are read from the archive's own metadata, before extraction, because
        # extracting first and using `is_file()` follows the link: a symlink entry whose target
        # happens to hold the expected bytes ON THIS HOST hashed equal and the package was
        # certified, while what installs is a link that can break or resolve elsewhere.  The
        # bench never ran against a link at any of these paths.  `unzip -Z1` prints a name for
        # a symlink exactly as for a file, so the name listing cannot tell them apart.
        with zipfile.ZipFile(p) as zf:
            linked = [i.filename for i in zf.infolist()
                      if stat.S_ISLNK(i.external_attr >> 16)]
        if linked:
            raise SystemExit(f"{name} contains {len(linked)} symlink entr(ies); the tested tree "
                             f"has only regular files and a link's bytes are the host's, not the "
                             f"archive's: {linked[:5]}")

        # The archive's PAYLOAD must be the tree the bench exercised.  Readability was
        # enforced; identity was not -- so a valid but stale or wrongly built ZIP could be
        # recorded, and published, while the tests that passed had run against `--work`.
        # The report already claimed each archive was recursively identical to its source,
        # and that claim rested on a manual step rather than on anything checked here.  This
        # is the link between "the tests passed" and "these are the bytes you install", so it
        # is the one binding in this file that concerns the deliverable rather than the record.
        skill = name[:-len(".skill")] if name.endswith(".skill") else name
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="pkgcheck-"))
        try:
            unpack = subprocess.run(["unzip", "-qq", str(p), "-d", str(tmp)],
                                    capture_output=True, text=True)
            if unpack.returncode != 0:
                raise SystemExit(f"{name} could not be extracted (unzip exited "
                                 f"{unpack.returncode}): {unpack.stderr.strip()}")
            # The COMPLETE extracted archive is compared, not just its `<skill>/` subtree.
            # Reading `got` from `tmp / skill` left everything outside that root uncompared, so
            # an archive holding the right subtree PLUS an extra top-level file or sibling
            # directory passed the payload check -- and `--write` then recorded its new count,
            # size and digest and reported success, certifying a package that installs bytes
            # the bench never ran against.  Proven before fixing: a 22-entry `change-flow.skill`
            # carrying a `README-EXTRA.txt` was written into the record with exit 0.  Rooting
            # `got` at the extraction directory and prefixing `want` with `<skill>/` rejects
            # every entry outside the one expected root by construction, rather than by a list
            # of shapes someone thought of.
            got = payload_map(tmp, f"the extracted {name}")
            want = {f"{skill}/{rel}": h
                    for rel, h in payload_map(work / skill, f"--work/{skill}").items()}
            if not want:
                raise SystemExit(f"--work has no {skill}/ subtree to compare {name} against")
            if got != want:
                only_pkg = sorted(set(got) - set(want))
                only_work = sorted(set(want) - set(got))
                changed = sorted(k for k in set(got) & set(want) if got[k] != want[k])
                detail = []
                if changed:
                    detail.append(f"{len(changed)} file(s) differ: {changed[:5]}")
                if only_pkg:
                    detail.append(f"{len(only_pkg)} only in the archive: {only_pkg[:5]}")
                if only_work:
                    detail.append(f"{len(only_work)} only in --work: {only_work[:5]}")
                raise SystemExit(f"{name} does not contain the tested {skill} tree; the bench "
                                 f"ran against --work and this archive is different. "
                                 + "; ".join(detail))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

        ids["packages"].append((name, count, p.stat().st_size, sha(p)))

    # The committed patch must BE the diff of the supplied trees, not merely have the same
    # number of lines.  The report calls it the complete change and the only repository-resident
    # substitute for the trees, which cannot be committed -- so a stale or substituted patch
    # sends a reviewer to inspect bytes the bench never exercised.  A line count cannot detect
    # that; the canonical content can.
    regenerated = subprocess.run(["diff", "-ru", str(base), str(work)],
                                 capture_output=True, text=True)
    if regenerated.returncode not in (0, 1):
        raise SystemExit(f"diff -ru failed with status {regenerated.returncode}: "
                         f"{regenerated.stderr.strip() or 'no stderr'}")
    live = hashlib.sha256(canonical_patch(regenerated.stdout, base, work).encode()).hexdigest()
    if live != ids["patch_sha"]:
        raise SystemExit(
            f"repairs.patch is not the diff of the supplied trees: committed canonical sha256 "
            f"{ids['patch_sha']}, regenerated {live}. Re-generate it with "
            f"`diff -ru <base> <work> > repairs.patch`.")
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


def freeze_summary(ids: dict) -> str:
    """The frozen tree's three identity fields, from the tree.

    `check()` used to ask only whether the DIGEST occurred somewhere in the document, so the
    recorded 321 and 320 were never compared with what `identities()` had just counted: input
    validation recomputed them and record validation threw them away.  All three are one block
    now, generated and asserted whole, because a count that disagrees with its own digest is
    exactly the kind of record a reader trusts without checking.
    """
    total, counted, digest = ids["base_tree"]
    return (f"- files: **{total}**, of which **{counted}** excluding `manifest.json`\n"
            f"- `.pyc` files: **{ids['base_pyc']}**\n"
            f"- recorded freeze digest: `{digest}`")


def corpus_summary(ids: dict) -> str:
    """The corpus roster's two summary lines, from the corpus itself.

    The body TABLE was generated and every row asserted, but the `total bytes` figure above it
    was typed once and never summed -- so `--check` could report that every identity was
    mechanically current while the summary named a corpus that was not supplied.  The aggregate
    is the same species as the rows it sits above; it just happened to be written in prose.
    """
    return (f"- bodies: **{len(ids['bodies'])}**\n"
            f"- total bytes: **{ids['bodies_bytes']:,}**")


def replace_marked(doc: str, name: str, body: str) -> str:
    """Replace the content between `<!-- generated: name -->` and its closing marker.

    Every generated region is marker-delimited, and that is a correctness property rather than
    tidiness.  The shape-matching patterns this replaced -- "a table whose header is exactly
    this", "a fence introduced by this sentence" -- had to be duplicated into the claim-inventory
    tool so that it could tell a generated value from a typed one.  Two copies of one rule is
    how the guard drift in this package began.  The markers put ownership in the document, where
    both tools read the same statement of it instead of each carrying its own.
    """
    open_t, close_t = f"<!-- generated: {name} -->", f"<!-- /generated: {name} -->"
    pat = re.compile(re.escape(open_t) + r".*?" + re.escape(close_t), re.S)
    if not pat.search(doc):
        raise SystemExit(f"cannot find the `{name}` generated block in the run record")
    return pat.sub(lambda _m: f"{open_t}\n{body}\n{close_t}", doc, count=1)


def write_records(ids: dict) -> int:
    doc = RUN_RECORD.read_text(encoding="utf-8")
    doc = replace_marked(doc, "changed-files", files_table(ids))
    doc = replace_marked(doc, "packages", packages_table(ids))
    doc = replace_marked(doc, "bodies", bodies_table(ids))
    doc = replace_marked(doc, "flowmaster-diff", "```diff\n" + ids["fm_diff"] + "\n```")
    doc = replace_marked(doc, "corpus-summary", corpus_summary(ids))
    doc = replace_marked(doc, "freeze-summary", freeze_summary(ids))
    doc = replace_marked(doc, "bench", bench_block(ids))
    RUN_RECORD.write_text(doc, encoding="utf-8")
    print(f"run record regenerated: {len(ids['files'])} changed files, "
          f"{len(ids['bodies'])} bodies, {len(ids['packages'])} packages, "
          f"bench {ids['bench_cases']} cases, flowmaster diff {ids['fm_changed']} lines")
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

    # `check()` asserts what the RECORDS say.  The freeze count and digest of `--base` are
    # properties of an INPUT, enforced in `identities()`, which BOTH modes traverse --
    # asserting them only here is precisely what let `--write` bypass them.
    if freeze_summary(ids) not in rr:
        total, counted, digest = ids["base_tree"]
        problems.append(f"run-record does not state the frozen tree as measured: {total} files, "
                        f"{counted} excluding manifest.json, {ids['base_pyc']} .pyc, "
                        f"{digest[:16]}…")

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

    # Every identity is compared as a COMPLETE ROW, binding each value to its file and its
    # side.  Membership tests were used first -- "does this digest occur somewhere in the
    # record" -- and they cannot tell a correct record from one that pairs a real digest with
    # the wrong file, or swaps a file's base and work hashes: both digests still "occur".
    # Same class of hole as every other defect found in this file: an assertion weaker than
    # the claim it backs.
    for rel, bh, wh in ids["files"]:
        row = f"| `{rel}` | `{bh}` | `{wh}` |"
        if row not in rr:
            problems.append(f"run-record has no row binding {rel} to base {bh[:16]}… and "
                            f"work {wh[:16]}…; a swapped or misattributed pair would not be "
                            f"caught by a membership test")
        # The report abbreviates digests to 16 characters, so its row is matched in that
        # form -- but as a ROW, binding the file to both sides.  A membership test survived
        # on the report side after the run-record fix, so two rows could exchange their
        # repaired prefixes and still pass, every expected prefix being present somewhere.
        rp_row = f"| `{rel}` | `{bh[:16]}…` | `{wh[:16]}…` |"
        if rp_row not in rp:
            problems.append(f"report has no row binding {rel} to base {bh[:16]}… and work "
                            f"{wh[:16]}…; a swapped or misattributed pair would not be "
                            f"caught by a membership test")
    for name, count, size, h in ids["packages"]:
        # The file COUNT is asserted too.  It was computed and unpacked but never compared,
        # which left the one identity the report relies on to detect accidentally included
        # bytecode outside the check -- the .pyc incident earlier in this package was caught
        # by that count, so leaving it unasserted removed the very signal that worked.
        row = f"| `{name}` | {count} | {size} | `{h}` |"
        if row not in rr:
            problems.append(f"run-record has no row binding {name} to {count} files, "
                            f"{size} bytes and sha256 {h[:16]}…")
        # Both records use the identical row format, so both are asserted as COMPLETE ROWS.
        # The report side was three fragment tests -- digest somewhere, size somewhere, a
        # `| count | size |` fragment somewhere -- so swapping the two packages' digests
        # between rows left every fragment present and passed.  That is the same defect fixed
        # for the changed-file rows one cycle earlier and not carried across to packages:
        # the fourth time a fix of mine covered the instance shown and not its sibling.
        if row not in rp:
            problems.append(f"report has no row binding {name} to {count} files, {size} bytes "
                            f"and sha256 {h[:16]}…; swapped package digests would not be "
                            f"caught by a membership test")
    # The whole-ecosystem validator's difference is asserted VERBATIM in the run record, and
    # as a count in the report, which states it in prose.  Both sides drifted together when the
    # SF10-04 retirement changed the roster, because neither was derived; the count is also
    # checked NEGATIVELY, so a superseded figure left in place fails rather than merely not
    # matching -- the same treatment the bench's case count needed for the same reason.
    if ids["fm_diff"] not in rr:
        problems.append(f"run-record does not contain the current validate_flowmaster.py "
                        f"difference verbatim ({ids['fm_changed']} changed line(s))")
    fm_phrase = f"differs in exactly {ids['fm_changed']} lines"
    if fm_phrase not in rp:
        problems.append(f"report does not state the validate_flowmaster.py difference: "
                        f"expected the phrase {fm_phrase!r}")
    for other in range(1, 61):
        if other != ids["fm_changed"] and f"differs in exactly {other} lines" in rp:
            problems.append(f"report still states a superseded validate_flowmaster.py "
                            f"difference: {other} lines where it should be "
                            f"{ids['fm_changed']}")

    # A LABELLED sentence, not the bare digits.  `str(411) in rp` passed on any occurrence of
    # "411" anywhere in a 1100-line document -- including a control description that happened to
    # restate the same number -- so the summary sentence it was meant to protect could go stale
    # while the check stayed green.  The duplicate mention was removed rather than bound twice.
    patch_phrase = f"**{ids['patch_lines']} patch lines**"
    if patch_phrase not in rp:
        problems.append(f"report does not state the patch's current line count: expected "
                        f"{patch_phrase!r}")
    for other in re.findall(r"\*\*(\d+) patch lines\*\*", rp):
        if int(other) != ids["patch_lines"]:
            problems.append(f"report states a superseded patch line count: {other} where it "
                            f"should be {ids['patch_lines']}")
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
    # The WHOLE rendered block, which binds the exit status, both counts and the verbatim stdout
    # together.  Two fragment tests stood here -- "**19 cases," somewhere, and the stdout
    # somewhere -- and a fragment cannot tell a consistent record from one whose headline and
    # output disagree.
    if bench_block(ids) not in rr:
        problems.append(f"run-record does not contain the bench block as measured: exit "
                        f"{ids['bench_exit']}, {n} cases, {ids['bench_failed']} not as expected, "
                        f"with its stdout verbatim")

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
    # The aggregate is asserted as a COMPLETE pair of lines, so a stale body count and a stale
    # byte total cannot each look plausible beside the other.
    summary = corpus_summary(ids)
    if summary not in rr:
        problems.append(f"run-record does not state the corpus summary: expected "
                        f"{len(ids['bodies'])} bodies totalling {ids['bodies_bytes']:,} bytes")

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
          f"exit {ids['bench_exit']}), flowmaster diff {ids['fm_changed']} lines, "
          f"base tree {ids['base_tree'][0]} files / {ids['base_tree'][2][:16]}…")
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
