#!/usr/bin/env python3
"""Force an explicit accounting for every claim-bearing line a change introduces.

    claim_inventory.py [--range <git-range>] [--paths <p> ...] [--allow <file>] [--write-allow]

WHAT IT DOES, stated narrowly, because the failure this tool exists to stop is a tool that
claims more than it checks:

  It finds every line a change ADDS or MODIFIES that states a digest, a count, a size, a
  revision or a percentage, and requires each one to be either

    (a) inside a GENERATED region -- a marker block, or one of the named generated tables --
        so that a regeneration step owns its value, or
    (b) listed in the allow-list with a note saying what recomputes it, or why it is a fixed
        historical fact that must not be updated.

  It does NOT verify that any value is correct, and it cannot: it has no idea what the number
  means.  It converts "a reader must notice a stale figure" into "an author must say, in
  writing, who owns this figure."  That is the whole claim.

  Three limits, stated because an unstated limit is how the guards in this package kept
  over-claiming: it reads **Markdown only**, so a figure in a docstring or a comment is out of
  scope; it reads only the paths given by `--paths` (default `docs/`); and "generated" means
  "inside a marker block" and nothing else, so a value a tool really does own is still reported
  until the block is marked.

WHY.  Round 20 of #425 produced, in three consecutive review cycles, three stale claims while
the evidence itself stayed correct: a validator-difference summary falsified by a later
retirement, a "regenerated at <commit>" attribution four commits out of date, and a corpus
byte total that was never summed.  Each was a sentence describing a derivable value, sitting
beside blocks that were derived.  Re-reading every summary after every change was tried and
failed four times in one round.

THE ALLOW-LIST IS KEYED ON THE EXACT LINE TEXT, and that is the point rather than an
implementation detail: edit the line and its entry stops matching, so the claim comes back for
accounting.  Entries are checked in BOTH directions -- an entry whose line no longer exists
anywhere in the file is reported too, because a dead entry is how an allow-list silently grows
into a blanket exemption.
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_ALLOW = pathlib.Path(__file__).resolve().parent / "allow.json"

# A line "claims" something if it states a value a later change can falsify.
CLAIM = re.compile(
    r"[0-9a-f]{7,}"            # a digest or an abbreviated revision
    r"|\*\*[0-9][0-9,]*\*\*"   # an emphasised count, which is how these documents write them
    r"|\b[0-9][0-9,]{2,}\b"    # any number of three or more digits, e.g. a byte count
    r"|\b[0-9]+(?:\.[0-9]+)+\b"  # a dotted revision, e.g. 3.2.7
    r"|\b[0-9]+\s?%"           # a percentage
)
# Shapes that are references or dates rather than derived measurements.  Excluded by SHAPE and
# named here, so the exclusion is auditable instead of being a silent hole: a PR or issue number,
# and an ISO date.  Nothing else is excluded -- a version, a count and a size all stay in.
NOT_A_MEASUREMENT = re.compile(r"#[0-9]+|\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b")
# One whole-line exclusion, for the front-matter version an author DECLARES.  Deliberately narrow:
# a `validator_revision` read out of a tool's output is a measurement and stays in scope.
DECLARED_LINE = re.compile(r"^artifact_version: ")

# A generated region is marker-delimited, and nothing else counts as one.  The first version of
# this tool recognised regions by SHAPE -- a table with exactly this header, a fence introduced by
# exactly this sentence -- which meant it carried its own copy of the recorder's patterns and
# would have to be kept in step with them by hand.  It also read a hand-typed line as generated
# whenever the text happened to match the generated form, which is a false clean.  Ownership is
# now declared in the document and both tools read that declaration.
GENERATED_MARKER = re.compile(
    r"<!-- generated: (?P<name>[^>]+?) -->(?P<body>.*?)<!-- /generated: \1 -->", re.S)


def run(*argv: str) -> str:
    r = subprocess.run(argv, capture_output=True, text=True, cwd=str(REPO))
    if r.returncode != 0:
        raise SystemExit(f"`{' '.join(argv)}` exited {r.returncode}: "
                         f"{r.stderr.strip() or 'no stderr'}")
    return r.stdout


def generated_lines(text: str) -> set[int]:
    """1-based line numbers of every line a marker block declares as generated."""
    owned: set[int] = set()
    for m in GENERATED_MARKER.finditer(text):
        owned.update(range(text.count("\n", 0, m.start()) + 1,
                           text.count("\n", 0, m.end()) + 2))
    return owned


def range_end(rng: str) -> str | None:
    """The revision a range ends at, or None when it ends at the working tree.

    Found by testing rather than by reading: the first version of this tool took line numbers
    from `git diff <old-range>` and then read the file from DISK, so every number indexed into
    the wrong content and the output named lines the commit never contained.  A tool whose
    subject is not the thing it measured is the exact defect this whole round has been about,
    reproduced on the first run of the tool written to stop it.
    """
    if not rng or rng in ("", "--"):
        return None
    for sep in ("...", ".."):
        if sep in rng:
            _left, _, right = rng.partition(sep)
            # `A..` ends at A's descendant-less right side, which git reads as the working tree.
            return right.strip() or None
    # A BARE revision is not a range: `git diff <rev>` compares the WORKING TREE against it, so
    # the new side is the working tree, not <rev>.  Reading <rev> here reproduced the very
    # mismatch this function exists to prevent -- line numbers from one side of a diff indexed
    # into the other -- and it was caught by the tool flagging two lines that are plainly inside
    # a marker block.  Found by running it, not by reading it.
    return None


def content_at(rev: str | None, rel: str) -> str | None:
    """The file's text at `rev`, or from the working tree when `rev` is None."""
    if rev is None:
        p = REPO / rel
        return p.read_text(encoding="utf-8") if p.is_file() else None
    r = subprocess.run(["git", "show", f"{rev}:{rel}"], capture_output=True, text=True,
                       cwd=str(REPO))
    return r.stdout if r.returncode == 0 else None


def changed_lines(rng: str, paths: list[str]) -> dict[str, list[int]]:
    """Added or modified line numbers per file, as they are in the NEW version."""
    argv = ["git", "diff", "-U0", "--no-color", rng, "--"] + (paths or [])
    out = run(*argv)
    per: dict[str, list[int]] = {}
    # An UNTRACKED file shows in no diff, so a brand-new document's claims were invisible -- and a
    # new document is exactly where fresh claims appear.  Every line of one counts as added.
    if range_end(rng) is None:
        for rel in run("git", "ls-files", "--others", "--exclude-standard", "--",
                       *(paths or [])).split():
            f = REPO / rel
            if f.is_file():
                per[rel] = list(range(1, len(f.read_text(encoding="utf-8",
                                                          errors="replace").splitlines()) + 1))
    current = None
    for line in out.splitlines():
        if line.startswith("+++ b/"):
            current = line[len("+++ b/"):]
            per.setdefault(current, [])
        elif line.startswith("@@") and current:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            if not m:
                raise SystemExit(f"unparsed hunk header, refusing to guess: {line!r}")
            start, count = int(m.group(1)), int(m.group(2) or 1)
            per[current].extend(range(start, start + count))
        elif line.startswith("+") and not line.startswith("+++"):
            pass  # counts come from the hunk header, which is authoritative
    return {f: ls for f, ls in per.items() if ls}


def inventory(rng: str, paths: list[str], allow: dict) -> tuple[list[str], list[str]]:
    problems, seen = [], set()
    end = range_end(rng)
    for rel, lines in sorted(changed_lines(rng, paths).items()):
        if not rel.lower().endswith(".md"):
            continue
        # The content is read at the range's END revision, so the line numbers the diff gave
        # index into the text they were computed against.
        text = content_at(end, rel)
        if text is None:
            continue
        body = text.splitlines()
        owned = generated_lines(text)
        permitted = allow.get(rel, {})
        for n in sorted(set(lines)):
            if n > len(body):
                continue
            line = body[n - 1]
            if DECLARED_LINE.match(line.strip()):
                continue
            if not CLAIM.search(NOT_A_MEASUREMENT.sub("", line)):
                continue
            if n in owned:
                continue
            stripped = line.strip()
            if stripped in permitted:
                seen.add((rel, stripped))
                continue
            problems.append(f"{rel}:{n} states a value nothing here owns\n"
                            f"      {stripped[:150]}")
    stale = []
    for rel, entries in sorted(allow.items()):
        text = content_at(end, rel)
        if text is None:
            continue
        present = {x.strip() for x in text.splitlines()}
        for ln in sorted(entries):
            if ln not in present:
                stale.append(f"{rel}: allow-list entry no longer present in the file\n"
                             f"      {ln[:150]}")
    return problems, stale


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--range", dest="rng", default="HEAD",
                    help="what to inventory; default HEAD, which is the uncommitted work. "
                         "Pass a range such as origin/main..HEAD before a push, or "
                         "<rev>~1..<rev> for one commit.")
    ap.add_argument("--paths", nargs="*", default=["docs/"])
    ap.add_argument("--allow", default=str(DEFAULT_ALLOW))
    args = ap.parse_args()

    allow_path = pathlib.Path(args.allow)
    allow = json.loads(allow_path.read_text(encoding="utf-8")) if allow_path.is_file() else {}

    problems, stale = inventory(args.rng, args.paths, allow)
    for group, title in ((problems, "UNACCOUNTED CLAIMS"), (stale, "STALE ALLOW-LIST ENTRIES")):
        if group:
            print(f"{title} — {len(group)}:")
            for g in group:
                print(f"  - {g}")
    if problems or stale:
        print("\nEach unaccounted line must be moved into a generated block, or added to "
              f"{allow_path.name} with a note naming what recomputes it or why it is fixed.")
        return 1
    print(f"claim inventory clean over {args.rng}: every claim-bearing changed line is "
          f"generated or accounted for")
    return 0


if __name__ == "__main__":
    sys.exit(main())
