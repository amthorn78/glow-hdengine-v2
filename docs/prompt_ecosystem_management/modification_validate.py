#!/usr/bin/env python3
"""Structure and gate checks for a GCFPE Modification.

    PYTHONDONTWRITEBYTECODE=1 python3 modification_validate.py <file.md> [more.md ...]
    PYTHONDONTWRITEBYTECODE=1 python3 modification_validate.py docs/ephemeral/modifications/

Exit 0 when every file passes, 1 when any fails, 2 on a usage error.

This exists because narrating a rule is not applying it. The mode gates in D20 are only real if
something refuses to let a mode start before its entry condition holds, and that something has to
be a script. Requires PyYAML.

What it checks, and the rule each check enforces:

  frontmatter parses, and carries every required key
  status is in the vocabulary
  coupling is ATOMIC or INDEPENDENT, and gate_tier is 0, 1 or 2
  the section for the declared status is present, and says something beyond the template's own
    headings and guidance
  ENTRY GATE  analyze_approved_by is non-empty before PLANNING or later
  ENTRY GATE  plan_approved_by is non-empty before EXECUTING or later
  every item has an id and a statement
  every item has a disposition once status is COMPLETE
  scope freeze: items may not be added after approval -- checked by item_count_at_approval
  COMPLETE requires interaction_cost_actual to be set, which is what calibrates the prediction
  a Modification citing new scope sets spawned_from rather than widening its own items

readiness is ADVISORY and never blocks. It reports what ANALYZE concluded; it does not refuse.
The gates here exist to stop a SESSION proceeding on its own judgement, never to stop the Product
Owner. A policy gate -- scope freeze above all -- is waived by a recorded override block:

    override:
      by: Nathan
      overrides: [scope_freeze]
      reason: "needed now"

The reason is for a successor session reading the record, not a justification anyone is owed.
An override waives a policy gate; it cannot make a malformed record well-formed.

An INTAKE draft is held to what triage writes, and nothing more: the required keys, one statement
per item, triage's proposed coupling, an `## Intake` section saying why the items belong
together, and an intake_record that exists beside it and lists it. Triage names an apparent
surface; it does not measure scope. That is why the intake prompt needs no contract of its own.

--selftest runs the injected regressions, then validates the shipped templates themselves, so the
templates cannot drift away from this script unnoticed (PAIR-001).
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("modification_validate: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

STATUSES = ["INTAKE", "ANALYZING", "ANALYZED", "PLANNING", "PLANNED",
            "EXECUTING", "COMPLETE", "BLOCKED", "ABANDONED"]
COUPLINGS = ["ATOMIC", "INDEPENDENT"]
READINESS = ["READY", "SPLIT_RECOMMENDED", "NEEDS_RULING"]
# Policy gates the Product Owner may waive with a recorded override. Everything else this
# script checks is well-formedness: an override cannot make a malformed record well-formed.
OVERRIDABLE = ["scope_freeze", "readiness", "modification_class", "gate_tier", "deferral"]
TARGETS = ["prompt", "skill", "rule", "graph", "registry", "notion_control"]
DISPOSITIONS = ["APPLIED", "VERIFIED", "BLOCKED", "NOT_APPLICABLE"]

# status -> (section that must exist, the approval field that gates reaching this status)
SECTION_FOR = {"ANALYZED": "## §A", "PLANNED": "## §P", "COMPLETE": "## §E"}
NEEDS_ANALYZE_APPROVAL = ["PLANNING", "PLANNED", "EXECUTING", "COMPLETE"]
NEEDS_PLAN_APPROVAL = ["EXECUTING", "COMPLETE"]
# statuses at or past the point where scope is frozen
FROZEN = ["PLANNING", "PLANNED", "EXECUTING", "COMPLETE"]
# Terminal states can be reached from ANY point -- a Modification can be abandoned during
# analysis. They carry no progression, so the ordered checks below must not treat their position
# in STATUSES as meaning every earlier stage was completed.
TERMINAL = ["BLOCKED", "ABANDONED"]

REQUIRED_ALWAYS = ["artifact_type", "modification_id", "status", "request", "items"]
REQUIRED_BEYOND_INTAKE = ["coupling", "targets", "gate_tier", "modification_class", "readiness"]


def split_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    return text[3:end], text[end + 4:]


def _template_section(marker):
    """The shipped template's text for section `marker`, or "" if the template cannot be read."""
    try:
        doc = Path(__file__).resolve().with_name("modification-template.md").read_text(encoding="utf-8")
        text = _fenced(doc, "## TEMPLATE BEGINS")
    except (OSError, IndexError):
        return ""
    return text.split(marker, 1)[1].split("\n## ", 1)[0] if marker in text else ""


def _own_text(seg, marker):
    """What a section says beyond the template's own headings and guidance for that section."""
    template = {line.strip() for line in _template_section(marker).splitlines() if line.strip()}
    return "".join(line.strip() for line in seg.splitlines()
                   if line.strip() and line.strip() not in template)


def _intake_checks(path, fm, body, mid):
    """What a triage draft must carry at INTAKE, so the run's conclusions live in files."""
    bad = []
    if fm.get("coupling") not in COUPLINGS:
        bad.append(f"INTAKE: coupling must carry triage's proposal, one of {COUPLINGS}; "
                   f"got {fm.get('coupling')!r}")
    text = "\n" + body
    if "\n## Intake" not in text:
        bad.append("INTAKE: section '## Intake' is absent; why these items belong together goes in the file")
    elif len(text.split("\n## Intake", 1)[1].split("\n## ", 1)[0].strip()) < 40:
        bad.append("INTAKE: section '## Intake' is present but empty")
    record = str(fm.get("intake_record") or "").strip()
    if not record:
        bad.append("INTAKE: intake_record is empty; every triage run writes one, holding every item")
        return bad
    record_path = Path(path).parent / Path(record).name
    if not record_path.is_file():
        bad.append(f"INTAKE: intake_record {record} is not beside this Modification")
        return bad
    rec_text, _ = split_frontmatter(record_path.read_text(encoding="utf-8"))
    try:
        rec = yaml.safe_load(rec_text) if rec_text else None
    except yaml.YAMLError:
        rec = None
    listed = rec.get("modifications") if isinstance(rec, dict) else None
    if not isinstance(listed, list) or mid not in listed:
        bad.append(f"INTAKE: intake_record {record} does not list {mid}")
    return bad


def check(path):
    """Return a list of failure strings; empty means the file passes."""
    bad = []
    raw = Path(path).read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(raw)
    if fm_text is None:
        return ["no YAML frontmatter"]
    try:
        fm = yaml.safe_load(fm_text) or {}
    except yaml.YAMLError as exc:
        return [f"frontmatter does not parse: {exc}"]
    if not isinstance(fm, dict):
        return ["frontmatter is not a mapping"]

    for key in REQUIRED_ALWAYS:
        if key not in fm:
            bad.append(f"missing required key: {key}")
    if fm.get("artifact_type") != "GCFPE_MODIFICATION_RECORD":
        bad.append(f"artifact_type must be GCFPE_MODIFICATION_RECORD, got {fm.get('artifact_type')!r}")

    status = fm.get("status")
    if status not in STATUSES:
        bad.append(f"status {status!r} not in {STATUSES}")
        return bad  # every later check keys off status

    mid = str(fm.get("modification_id") or "")
    if not mid.startswith("MODIFICATION-"):
        bad.append(f"modification_id must start with MODIFICATION-, got {mid!r}")

    items = fm.get("items") or []
    if not isinstance(items, list) or not items:
        bad.append("items must be a non-empty list")
        items = []
    for n, item in enumerate(items, 1):
        if not isinstance(item, dict):
            bad.append(f"item {n} is not a mapping")
            continue
        if not item.get("id"):
            bad.append(f"item {n} has no id")
        if not str(item.get("statement") or "").strip():
            bad.append(f"item {item.get('id', n)} has no statement")

    if status == "INTAKE":
        # A triage draft is held to what triage writes, and nothing further. Everything triage
        # concludes goes in a file -- the coupling it proposes, why the items belong together, and
        # an intake record holding every item, including those that did not become drafts. The
        # 2026-09-22 comparison test found all three living only in chat.
        return bad + _intake_checks(path, fm, body, mid)

    for key in REQUIRED_BEYOND_INTAKE:
        if fm.get(key) in (None, ""):
            bad.append(f"missing required key beyond INTAKE: {key}")

    if fm.get("coupling") not in COUPLINGS and "coupling" in fm:
        bad.append(f"coupling {fm.get('coupling')!r} not in {COUPLINGS}")
    if fm.get("readiness") not in READINESS and fm.get("readiness"):
        bad.append(f"readiness {fm.get('readiness')!r} not in {READINESS}")
    if fm.get("gate_tier") not in (0, 1, 2) and fm.get("gate_tier") is not None:
        bad.append(f"gate_tier {fm.get('gate_tier')!r} must be 0, 1 or 2")
    for tgt in fm.get("targets") or []:
        if tgt not in TARGETS:
            bad.append(f"target {tgt!r} not in {TARGETS}")

    if status in TERMINAL:
        # Nothing further is asserted: an abandoned or blocked Modification is a record of where
        # it stopped, and demanding the sections it never reached would be demanding a lie.
        return bad

    # --- the entry gates: this is the whole point of the script ---
    if status in NEEDS_ANALYZE_APPROVAL and not str(fm.get("analyze_approved_by") or "").strip():
        bad.append(f"ENTRY GATE: status {status} requires analyze_approved_by; PLAN may not start")
    if status in NEEDS_PLAN_APPROVAL and not str(fm.get("plan_approved_by") or "").strip():
        bad.append(f"ENTRY GATE: status {status} requires plan_approved_by; EXECUTE may not start")

    # --- the section for the declared status must exist and carry something ---
    for reached in [s for s in ("ANALYZED", "PLANNED", "COMPLETE")
                    if STATUSES.index(status) >= STATUSES.index(s)]:
        marker = SECTION_FOR[reached]
        if marker not in body:
            bad.append(f"status {status} requires section {marker}, which is absent")
        else:
            seg = body.split(marker, 1)[1].split("\n## ", 1)[0]
            if len(seg.strip()) < 40:
                bad.append(f"section {marker} is present but empty")
            elif len(_own_text(seg, marker)) < 40:
                # The template's own headings and guidance run past 40 characters, so a section
                # copied from it and never filled passed as written. Found by the 2026-09-23
                # triage rerun; only what the section says beyond the template counts.
                bad.append(f"section {marker} holds only the template's placeholder text")

    # --- the Product Owner's override, if one is recorded ---
    # The template ships this block with every field empty and says to keep the keys, so an
    # all-empty block is the template, not an override. Treating it as one failed every
    # Modification the moment it left INTAKE -- found by both runs of the 2026-09-22 triage
    # comparison test, and missed by the fixture below because it was hand-written (PAIR-001).
    override = fm.get("override") or {}
    if not isinstance(override, dict):
        bad.append("override must be a block with by, overrides and reason")
        override = {}
    raw = override.get("overrides") or []
    waived = [raw] if isinstance(raw, str) else list(raw)
    by = str(override.get("by") or "").strip()
    reason = str(override.get("reason") or "").strip()
    if by or waived or reason:
        if not by:
            bad.append("override present but has no 'by'; an unattributed override is not one")
        if not waived:
            bad.append("override present but names no gate; say which policy gate it waives")
        for w in waived:
            if w not in OVERRIDABLE:
                bad.append(f"override names {w!r}, which is not a policy gate; overridable: {OVERRIDABLE}")
        if not reason:
            bad.append("override present but has no 'reason'; the record needs to say it was deliberate")

    # --- scope freeze ---
    # The field is REQUIRED once scope is frozen. Without that, the guard is opt-in: a
    # Modification that simply never sets it can grow items freely after approval, and scope
    # freeze is the rule that bounds the review loops. Found by the stage 4 pilot; PAIR-001.
    frozen_at = fm.get("item_count_at_approval")
    if status in FROZEN and "scope_freeze" in waived:
        pass  # waived by the Product Owner, and the override block records it
    elif status in FROZEN:
        if frozen_at in (None, ""):
            bad.append(
                f"SCOPE FREEZE: status {status} requires item_count_at_approval; without it the "
                "freeze is unenforced and items can be added after approval")
        elif len(items) != frozen_at:
            bad.append(
                f"SCOPE FREEZE: {len(items)} items but item_count_at_approval is {frozen_at}; "
                "new scope is a new Modification with spawned_from set, never a wider one")

    if status == "COMPLETE":
        for item in items:
            if isinstance(item, dict) and item.get("disposition") not in DISPOSITIONS:
                bad.append(f"item {item.get('id')} has no disposition; COMPLETE requires one per item")
        if fm.get("interaction_cost_actual") in (None, ""):
            bad.append("COMPLETE requires interaction_cost_actual; it is what calibrates the prediction")

    return bad


# --------------------------------------------------------------------------------------------
# Injected regressions. A guard that has never been fired by a regression is not a guard
# (GUARD-001). Each case below is a defect this script must catch; SELFTEST asserts it does.
# --------------------------------------------------------------------------------------------

_GOOD = """---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260922-selftest
status: COMPLETE
coupling: INDEPENDENT
targets: [skill]
gate_tier: 0
readiness: READY
modification_class: B
interaction_cost_predicted: 4
interaction_cost_actual: 4
item_count_at_approval: 1
items:
  - id: ITEM-01
    statement: "a real statement"
    disposition: VERIFIED
request: "the request"
analyze_approved_by: Nathan
plan_approved_by: Nathan
---
# t
## §A — Analysis
enough text here to clear the emptiness check on this section, comfortably.
## §P — Plan
enough text here to clear the emptiness check on this section, comfortably.
## §E — Execution
enough text here to clear the emptiness check on this section, comfortably.
"""

_REGRESSIONS = [
    ("analyze approval missing blocks PLAN",
     lambda s: s.replace("analyze_approved_by: Nathan", 'analyze_approved_by: ""'), "ENTRY GATE"),
    ("plan approval missing blocks EXECUTE",
     lambda s: s.replace("plan_approved_by: Nathan", 'plan_approved_by: ""'), "ENTRY GATE"),
    ("scope grew after approval",
     lambda s: s.replace("  - id: ITEM-01",
                         '  - id: ITEM-00\n    statement: "smuggled in"\n    disposition: VERIFIED\n  - id: ITEM-01'),
     "SCOPE FREEZE"),
    ("scope freeze unenforced because the field was never set",
     lambda s: s.replace("item_count_at_approval: 1\n", ""), "requires item_count_at_approval"),
    ("terminal state wrongly required to carry every section",
     lambda s: s.replace("status: COMPLETE", "status: ABANDONED")
                .replace("## §P — Plan\nenough text here to clear the emptiness check on this section, comfortably.\n", "")
                .replace("## §E — Execution\nenough text here to clear the emptiness check on this section, comfortably.\n", ""),
     None),  # None = this must PASS, not fail
    ("override with no attribution",
     lambda s: s.replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  overrides: [scope_freeze]\n  reason: "x"'),
     "no 'by'"),
    ("override with no reason",
     lambda s: s.replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  by: Nathan\n  overrides: [scope_freeze]'),
     "no 'reason'"),
    ("override claiming to waive a well-formedness check",
     lambda s: s.replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  by: Nathan\n  overrides: [missing_sections]\n  reason: "x"'),
     "not a policy gate"),
    ("override that names no gate",
     lambda s: s.replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  by: Nathan\n  overrides: []\n  reason: "x"'),
     "names no gate"),
    ("the template's empty override block wrongly treated as an override",
     lambda s: s.replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  by: ""\n  overrides: []\n  reason: ""'),
     None),  # must PASS: the template ships this block empty

    ("item has no disposition at COMPLETE",
     lambda s: s.replace("    disposition: VERIFIED", '    disposition: ""'), "no disposition"),
    ("actual cost missing at COMPLETE",
     lambda s: s.replace("interaction_cost_actual: 4", 'interaction_cost_actual: ""'), "calibrates"),
    ("declared section absent",
     lambda s: s.replace("## §E — Execution", "## Something else"), "requires section"),
    ("declared section present but empty",
     lambda s: s.replace("## §P — Plan\nenough text here to clear the emptiness check on this section, comfortably.",
                         "## §P — Plan\n"), "present but empty"),
    ("analysis section copied from the template and never filled",
     lambda s: s.replace("## §A — Analysis\nenough text here to clear the emptiness check on this section, comfortably.",
                         "## §A" + _template_section("## §A").rstrip("\n")), "only the template's placeholder text"),
    ("template guidance kept, with real analysis written beneath it",
     lambda s: s.replace("## §A — Analysis\nenough text here to clear the emptiness check on this section, comfortably.",
                         "## §A" + _template_section("## §A").rstrip("\n")
                         + "\nclosure.py returned radius 1 (PR-10); Tier 1, because the output artifact changes."),
     None),  # must PASS: keeping the guidance is fine; what counts is what was added
    ("bad status vocabulary",
     lambda s: s.replace("status: COMPLETE", "status: DONE"), "not in"),
    ("bad coupling vocabulary",
     lambda s: s.replace("coupling: INDEPENDENT", "coupling: BASKET"), "coupling"),
    ("bad gate tier",
     lambda s: s.replace("gate_tier: 0", "gate_tier: 7"), "gate_tier"),
    ("wrong artifact_type",
     lambda s: s.replace("GCFPE_MODIFICATION_RECORD", "GCFPE_CHANGE_RECORD"), "artifact_type"),
    ("item with no statement",
     lambda s: s.replace('statement: "a real statement"', 'statement: ""'), "no statement"),
]

_GOOD_INTAKE = """---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-selftest-intake
status: INTAKE
intake_record: docs/ephemeral/modifications/INTAKE-20260923-selftest.md
coupling: ATOMIC
items:
  - id: ITEM-01
    statement: "a real statement"
    source: AF-000
request: "what was pasted"
---
# MODIFICATION-20260923-selftest-intake
One sentence.
## Intake
why these items belong together, in enough words to clear the emptiness check.
"""

_GOOD_INTAKE_RECORD = """---
artifact_type: GCFPE_INTAKE_RECORD
intake_id: INTAKE-20260923-selftest
modifications: [MODIFICATION-20260923-selftest-intake]
---
# INTAKE-20260923-selftest
"""

_INTAKE_REGRESSIONS = [
    ("triage left its proposed coupling out of the draft",
     lambda s: s.replace("coupling: ATOMIC\n", ""), "INTAKE: coupling"),
    ("the reason for the grouping exists only in chat",
     lambda s: s.split("## Intake")[0], "'## Intake' is absent"),
    ("no intake record named",
     lambda s: s.replace("docs/ephemeral/modifications/INTAKE-20260923-selftest.md", '""'),
     "intake_record is empty"),
    ("intake record named but never written",
     lambda s: s.replace("INTAKE-20260923-selftest.md", "INTAKE-20260923-missing.md"), "is not beside"),
    ("intake record does not list this draft",
     lambda s: s.replace("modification_id: MODIFICATION-20260923-selftest-intake",
                         "modification_id: MODIFICATION-20260923-another"), "does not list"),
]


def selftest():
    import tempfile
    failures = 0
    with tempfile.TemporaryDirectory() as td:
        good = Path(td) / "MODIFICATION-good.md"
        good.write_text(_GOOD, encoding="utf-8")
        problems = check(good)
        if problems:
            print("SELFTEST FAIL: the known-good fixture did not pass:")
            for pr in problems:
                print(f"        {pr}")
            failures += 1
        else:
            print("ok    known-good fixture passes")
        for name, mutate, expect in _REGRESSIONS:
            f = Path(td) / "MODIFICATION-regression.md"
            f.write_text(mutate(_GOOD), encoding="utf-8")
            found = check(f)
            if expect is None:                       # must PASS
                if found:
                    print(f"SELFTEST FAIL: should have passed: {name} -> {found}")
                    failures += 1
                else:
                    print(f"ok    correctly allowed: {name}")
            elif any(expect in pr for pr in found):
                print(f"ok    caught: {name}")
            else:
                print(f"SELFTEST FAIL: NOT caught: {name} (expected {expect!r}, got {found})")
                failures += 1
        # A triage draft at INTAKE, beside its intake record.
        (Path(td) / "INTAKE-20260923-selftest.md").write_text(_GOOD_INTAKE_RECORD, encoding="utf-8")
        f = Path(td) / "MODIFICATION-intake.md"
        f.write_text(_GOOD_INTAKE, encoding="utf-8")
        problems = check(f)
        if problems:
            print(f"SELFTEST FAIL: the known-good triage draft did not pass: {problems}")
            failures += 1
        else:
            print("ok    known-good triage draft passes")
        for name, mutate, expect in _INTAKE_REGRESSIONS:
            f.write_text(mutate(_GOOD_INTAKE), encoding="utf-8")
            found = check(f)
            if any(expect in pr for pr in found):
                print(f"ok    caught: {name}")
            else:
                print(f"SELFTEST FAIL: NOT caught: {name} (expected {expect!r}, got {found})")
                failures += 1
        # PAIR-001: every fixture above is hand-written, so none of them can notice the shipped
        # templates drifting away from this script. Validate the templates themselves: the
        # Modification filled as triage fills it, beside the intake record as shipped, and filled
        # in the minimum ANALYZE fills.
        template_cases = _template_cases()
        for name, text, extras in template_cases:
            if text is None:
                print(f"SELFTEST FAIL: {name}")
                failures += 1
                continue
            for fname, ftext in extras.items():
                (Path(td) / fname).write_text(ftext, encoding="utf-8")
            f = Path(td) / "MODIFICATION-template.md"
            f.write_text(text, encoding="utf-8")
            found = check(f)
            if found:
                print(f"SELFTEST FAIL: the shipped template fails validation: {name} -> {found}")
                failures += 1
            else:
                print(f"ok    shipped template passes: {name}")
    total = len(_REGRESSIONS) + 1 + len(_INTAKE_REGRESSIONS) + 1 + len(template_cases)
    print(f"\n{total - failures}/{total} selftest cases passed")
    return 1 if failures else 0


def _fenced(doc, begins):
    """The first ```markdown block after the heading `begins`."""
    return doc.split(begins, 1)[1].split("```markdown\n", 1)[1].split("\n```\n", 1)[0] + "\n"


def _template_cases():
    """The shipped templates in modification-template.md, as (name, text, extra files) cases."""
    import re
    path = Path(__file__).resolve().with_name("modification-template.md")
    try:
        doc = path.read_text(encoding="utf-8")
        text = _fenced(doc, "## TEMPLATE BEGINS")
        record = _fenced(doc, "## INTAKE RECORD BEGINS")
    except (OSError, IndexError):
        return [("templates not found, or not fenced where expected, in " + path.name, None, {})]

    def fill(src, pairs):
        for key, value in pairs:
            src = re.sub(rf"^{key}:[^\n]*", f"{key}: {value}", src, count=1, flags=re.M)
        return src

    record_name = re.search(r"^intake_id:\s*(\S+)", record, flags=re.M)
    record_file = (record_name.group(1) if record_name else "INTAKE-missing") + ".md"
    at_intake = fill(text, (("coupling", "ATOMIC"), ("intake_record", record_file)))
    at_analyzing = fill(text.replace("status: INTAKE", "status: ANALYZING", 1),
                        (("coupling", "ATOMIC"), ("targets", "[prompt]"), ("gate_tier", "1"),
                         ("readiness", "READY"), ("modification_class", "B")))
    return [("filled as triage fills it, beside the shipped intake record, at INTAKE",
             at_intake, {record_file: record}),
            ("filled as ANALYZE fills it, at ANALYZING", at_analyzing, {})]


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__.strip())
        return 2  # no arguments is a usage error
    targets, scanned_dirs = [], []
    for arg in args:
        p = Path(arg)
        if p.is_dir():
            scanned_dirs.append(p)
            targets.extend(sorted(p.glob("MODIFICATION-*.md")))
        else:
            targets.append(p)
    if not targets:
        # A directory with no Modifications in it is a legitimate state, not a usage error.
        # It is the state on the day this lands, and the intake prompt tells the operator to
        # run exactly this command.
        for d in scanned_dirs:
            print(f"ok    {d}: no Modifications to check")
        return 0
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
