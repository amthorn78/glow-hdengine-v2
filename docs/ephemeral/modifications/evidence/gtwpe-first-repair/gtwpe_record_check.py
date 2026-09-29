#!/usr/bin/env python3
"""The GTWPE's own checks on a Modification record, run on top of the shared validator.

    PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/gtwpe/gtwpe_record_check.py <record.md> [more.md ...]
    PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/gtwpe/gtwpe_record_check.py docs/ephemeral/modifications/
    PYTHONDONTWRITEBYTECODE=1 python3 docs/prompt_ecosystem_management/gtwpe/gtwpe_record_check.py --selftest

Exit 0 when every record passes, 1 when any fails, 2 on a usage error.

It first runs modification_validate.py's check() on the record, unchanged, so a GTWPE record is held to
every shared rule and this file keeps no second copy of them (DERIV-001). Then it adds the rules that
GTWPE-MGMT-10 states for its own records and the shared validator does not check:

  GTWPE      the record carries `ecosystem: GTWPE`. A GCFPE record is not this check's to judge
  HARNESS    each mode section the status has reached holds a `### Harness files` subsection with content:
             §A from ANALYZED, §P from PLANNED, §E at COMPLETE, the validator's own thresholds. The change
             prompt names every harness file there (D22 condition 5); the template has no such section
  DRY RUN    each mode with a DRY_RUN round in `reviews` holds a `### Dry run` subsection with content in its
             own section: ANALYZE in §A, PLAN in §P, SKILL in §E

A record in a terminal state (BLOCKED, ABANDONED) is held to the shared rules only, as the validator holds
it: demanding sections a stopped Modification never reached would be demanding a lie.

A directory argument checks every MODIFICATION-*.md in it whose front matter says `ecosystem: GTWPE`, and
says how many other records it left to the shared validator. A file argument is checked whatever it says.

--selftest validates a known-good record, then each injected regression against it (GUARD-001).
Requires PyYAML, as the validator does. Added by MODIFICATION-20260929-gtwpe-first-repair.
"""
import importlib.util
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("gtwpe_record_check: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

MIN_CONTENT = 40  # the validator's own threshold for a section that says something
REACHED = (("ANALYZED", "## §A"), ("PLANNED", "## §P"), ("COMPLETE", "## §E"))
DRY_RUN_SECTION = (("ANALYZE", "## §A"), ("PLAN", "## §P"), ("SKILL", "## §E"))


def _load_validator():
    """modification_validate.py, found by walking up to the repository's docs/ directory."""
    for base in Path(__file__).resolve().parents:
        cand = base / "docs" / "prompt_ecosystem_management" / "modification_validate.py"
        if cand.is_file():
            spec = importlib.util.spec_from_file_location("modification_validate", cand)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
    print("gtwpe_record_check: docs/prompt_ecosystem_management/modification_validate.py not found "
          "above this file", file=sys.stderr)
    sys.exit(2)


V = _load_validator()


def _lines_outside_fences(text):
    """(line, outside) pairs: `outside` is False for a fence line and for every line inside a fence.

    A record quotes page text in fenced blocks, and that text can hold `## ` headings of its own, as
    the pilot's §P does. A heading inside a fence is quoted text, never the record's structure."""
    inside = False
    for line in text.split("\n"):
        if line.startswith("```"):
            inside = not inside
            yield line, False
        else:
            yield line, not inside


def _section(body, marker):
    """The lines of section `marker` (a level-2 heading) with their fence flags, or None if absent."""
    seg, started = [], False
    for line, outside in _lines_outside_fences(body):
        if not started:
            started = outside and line.startswith(marker)
            continue
        if outside and line.startswith("## "):
            break
        seg.append((line, outside))
    return seg if started else None


def _subsection_holds(seg, heading):
    """True when a line starting with `heading` opens a subsection that says something."""
    for n, (line, outside) in enumerate(seg):
        if outside and line.startswith(heading):
            content = []
            for later, later_outside in seg[n + 1:]:
                if later_outside and (later.startswith("### ") or later.startswith("## ")):
                    break
                content.append(later.strip())
            if len("".join(content)) >= MIN_CONTENT:
                return True
    return False


def _shared_check(path):
    return list(V.check(path))


def _ecosystem_check(fm):
    if fm.get("ecosystem") != "GTWPE":
        return [f"GTWPE: ecosystem must be GTWPE, got {fm.get('ecosystem')!r}; this check is for GTWPE records"]
    return []


def _harness_check(fm, body, status):
    bad = []
    for reached, marker in REACHED:
        if V.STATUSES.index(status) >= V.STATUSES.index(reached):
            seg = _section(body, marker)
            if seg is not None and not _subsection_holds(seg, "### Harness files"):
                bad.append(f"HARNESS: status {status} requires a '### Harness files' subsection with content "
                           f"in {marker}; the change prompt names every harness file there (D22 condition 5)")
    return bad


def _dry_run_check(fm, body, status):
    rounds = fm.get("reviews") or []
    modes = {r.get("mode") for r in rounds if isinstance(r, dict) and r.get("kind") == "DRY_RUN"}
    bad = []
    for mode, marker in DRY_RUN_SECTION:
        if mode in modes:
            seg = _section(body, marker)
            if seg is None or not _subsection_holds(seg, "### Dry run"):
                bad.append(f"DRY RUN: reviews holds a {mode} DRY_RUN round, so {marker} requires a "
                           "'### Dry run' subsection with content recording its gates and results")
    return bad


def check(path):
    """Return a list of failure strings; empty means the record passes."""
    bad = _shared_check(path)
    fm_text, body = V.split_frontmatter(Path(path).read_text(encoding="utf-8"))
    if fm_text is None:
        return bad  # the shared check has already said so
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return bad
    if not isinstance(fm, dict):
        return bad
    ecosystem = _ecosystem_check(fm)
    if ecosystem:
        return bad + ecosystem
    status = fm.get("status")
    if status not in V.STATUSES or status in V.TERMINAL:
        return bad
    return bad + _harness_check(fm, body, status) + _dry_run_check(fm, body, status)


# --------------------------------------------------------------------------------------------------
# Injected regressions. A guard that has never been fired by a regression is not a guard (GUARD-001).
# --------------------------------------------------------------------------------------------------

_FILLER = "enough text here to clear the emptiness check on this section, comfortably."

_GOOD = f"""---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
ecosystem: GTWPE
modification_id: MODIFICATION-20260929-gtwpe-selftest
status: COMPLETE
targets: [tool]
gate_tier: 1
readiness: READY
interaction_cost_predicted: 6
interaction_cost_actual: 6
estimate:
  plan: "1 h, 0.5M tokens"
  execute: "1 h, 0.5M tokens"
reviews:
  - mode: ANALYZE
    kind: DRY_RUN
    date: 2026-09-29
    required_open: 0
    outcome: "dry run"
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-29
    required_open: 0
    outcome: "dry run"
item_count_at_approval: 1
items:
  - id: ITEM-01
    statement: "a real statement"
    disposition: VERIFIED
parts:
  - id: PART-01
    items: [ITEM-01]
    class: C
request: "the request"
analyze_approved_by: Nathan
plan_approved_by: Nathan
---
# t
## §A — Analysis
{_FILLER}
### Dry run (A6)
{_FILLER}
### Harness files (`D22` condition 5)
{_FILLER}
## §P — Plan
{_FILLER}
### Dry run (PL3)
{_FILLER}
### Harness files (`D22` condition 5), for `PLAN`
{_FILLER}
## §E — Execution
{_FILLER}
### Harness files (`D22` condition 5), for `EXECUTE`
{_FILLER}
"""

_A_HARNESS = f"### Harness files (`D22` condition 5)\n{_FILLER}\n## §P"
_P_HARNESS = f"### Harness files (`D22` condition 5), for `PLAN`\n{_FILLER}\n"
_E_HARNESS = f"### Harness files (`D22` condition 5), for `EXECUTE`\n{_FILLER}\n"
_A_DRY = f"### Dry run (A6)\n{_FILLER}\n"
_P_DRY = f"### Dry run (PL3)\n{_FILLER}\n"
_SKILL_ROUND = """  - mode: SKILL
    kind: DRY_RUN
    date: 2026-09-29
    required_open: 0
    outcome: "dry run"
item_count_at_approval: 1"""

def _at_analyzing(s):
    """The record as ANALYZE leaves it before A6: no round in the ledger, no Harness files yet."""
    head, tail = s.split("reviews:\n", 1)
    tail = "item_count_at_approval:" + tail.split("item_count_at_approval:", 1)[1]
    return (head + "reviews: []\n" + tail).replace("status: COMPLETE", "status: ANALYZING").replace(_A_HARNESS, "## §P")


_REGRESSIONS = [
    ("ecosystem key absent",
     lambda s: s.replace("ecosystem: GTWPE\n", ""), "GTWPE:"),
    ("ecosystem names another ecosystem",
     lambda s: s.replace("ecosystem: GTWPE", "ecosystem: GCFPE"), "GTWPE:"),
    ("§A has no Harness files subsection",
     lambda s: s.replace(_A_HARNESS, "## §P"), "HARNESS"),
    ("§P has no Harness files subsection",
     lambda s: s.replace(_P_HARNESS, ""), "HARNESS"),
    ("§E has no Harness files subsection at COMPLETE",
     lambda s: s.replace(_E_HARNESS, ""), "HARNESS"),
    ("§A's Harness files heading has no content",
     lambda s: s.replace(_A_HARNESS, "### Harness files (`D22` condition 5)\n## §P"), "HARNESS"),
    ("§A's Harness files moved under §P",
     lambda s: s.replace(_A_HARNESS, "## §P").replace(_P_HARNESS, _P_HARNESS + _A_HARNESS[:-5] + "\n"),
     "HARNESS"),
    ("an ANALYZE dry run with no Dry run subsection in §A",
     lambda s: s.replace(_A_DRY, ""), "DRY RUN"),
    ("a PLAN dry run with no Dry run subsection in §P",
     lambda s: s.replace(_P_DRY, ""), "DRY RUN"),
    ("a SKILL dry run with no Dry run subsection in §E",
     lambda s: s.replace("item_count_at_approval: 1", _SKILL_ROUND, 1), "DRY RUN"),
    ("a shared rule broken: PLAN approval missing at COMPLETE",
     lambda s: s.replace("plan_approved_by: Nathan", 'plan_approved_by: ""'), "ENTRY GATE"),
    ("at ANALYZING, before §A is due, with no Harness files and no dry run",
     _at_analyzing, None),  # None = this must PASS
    ("at PLANNED, before §E is due, with no §E at all",
     lambda s: s.replace("status: COMPLETE", "status: PLANNED").split("## §E", 1)[0],
     None),
    ("abandoned, with every Harness files and Dry run subsection gone",
     lambda s: s.replace("status: COMPLETE", "status: ABANDONED").replace(_A_HARNESS, "## §P")
                .replace(_P_HARNESS, "").replace(_E_HARNESS, "").replace(_A_DRY, "").replace(_P_DRY, ""),
     None),
    ("a fenced block in §P quoting a level-2 heading, as the pilot's §P does",
     lambda s: s.replace(_P_DRY, "```\n## Selected release — quoted page text\n```\n" + _P_DRY),
     None),
    ("headings written with a suffix, as the pilot's record writes them",
     lambda s: s.replace("### Dry run (A6)", "### Dry run (A6), before approval")
                .replace("### Harness files (`D22` condition 5)\n", "### Harness files, for `ANALYZE`\n", 1),
     None),
]


def selftest():
    import tempfile
    failures = 0
    total = 1 + len(_REGRESSIONS)
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "MODIFICATION-gtwpe-selftest.md"
        f.write_text(_GOOD, encoding="utf-8")
        problems = check(f)
        if problems:
            print(f"SELFTEST FAIL: the known-good record did not pass: {problems}")
            failures += 1
        else:
            print("ok    known-good GTWPE record passes")
        for case, mutate, expect in _REGRESSIONS:
            text = mutate(_GOOD)
            if text == _GOOD:
                print(f"SELFTEST FAIL: the mutation changed nothing: {case}")
                failures += 1
                continue
            f.write_text(text, encoding="utf-8")
            found = check(f)
            if expect is None:
                if found:
                    print(f"SELFTEST FAIL: should have passed: {case} -> {found}")
                    failures += 1
                else:
                    print(f"ok    correctly allowed: {case}")
            elif any(expect in problem for problem in found):
                print(f"ok    caught: {case}")
            else:
                print(f"SELFTEST FAIL: NOT caught: {case} (expected {expect!r}, got {found})")
                failures += 1
    print(f"\n{total - failures}/{total} selftest cases passed")
    return 1 if failures else 0


def _is_gtwpe(path):
    fm_text, _ = V.split_frontmatter(path.read_text(encoding="utf-8"))
    try:
        fm = yaml.safe_load(fm_text or "") or {}
    except yaml.YAMLError:
        return True  # let check() report the parse failure
    return isinstance(fm, dict) and fm.get("ecosystem") == "GTWPE"


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__.strip())
        return 2
    targets = []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            found = sorted(p.glob("MODIFICATION-*.md"))
            mine = [r for r in found if _is_gtwpe(r)]
            print(f"ok    {p}: {len(mine)} GTWPE records; {len(found) - len(mine)} others left to "
                  "modification_validate.py")
            targets.extend(mine)
        else:
            targets.append(p)
    failed = 0
    for path in targets:
        problems = check(path)
        if problems:
            failed += 1
            print(f"FAIL  {path}")
            for problem in problems:
                print(f"        {problem}")
        else:
            print(f"ok    {path}")
    print(f"\n{len(targets) - failed}/{len(targets)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
