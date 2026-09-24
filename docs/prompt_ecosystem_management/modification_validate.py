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
  status is in the vocabulary; gate_tier is 0, 1 or 2
  one run is one Modification (D21): every item is in exactly one part, each part names only real
    items, and `after` names real parts without ordering them in a cycle
  each part carries a class A-E once past INTAKE (a Modification with no parts is one part, and
    carries modification_class instead)
  the section for the declared status is present, and says something beyond the template's own
    headings and guidance
  ENTRY GATE  analyze_approved_by is non-empty before PLANNING or later
  ENTRY GATE  plan_approved_by is non-empty before EXECUTING or later
  every item has an id and a statement
  every item has a disposition once status is COMPLETE
  a part lands whole or not at all: no part may be partly applied and partly blocked
  scope freeze: items may not be added after approval -- checked by item_count_at_approval
  COMPLETE requires interaction_cost_actual to be set, which is what calibrates the prediction

For a record with `format: "2.1"` or later (D26), and never for a legacy record with no format:
  `reviews` is a list of {mode, kind, date, required_open, outcome}: every ANALYZE, PLAN and SKILL
    review round, in order
  REVIEW CAP     per mode, at most 2 FULL reviews and 1 DIFF_CHECK, unless the override names
                 review_cap
  DRY RUN FIRST  PLAN's first FULL review comes after a PLAN DRY_RUN, unless the override names
                 dry_run
  ESTIMATE       `estimate` carries plan and execute from ANALYZED on, except in a terminal state
The session behaviours D26 also asks for -- stopping when defects do not halve, re-pricing at twice
the estimate, naming who set an exit rule -- have no mechanical check here, and D26 says so.

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
per item, the parts, and an `## Intake` section holding every item handed in and why the parts
are shaped as they are. Triage names an apparent surface; it does not measure scope. That is why
the intake prompt needs no contract of its own.

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
COUPLINGS = ["ATOMIC", "INDEPENDENT"]  # legacy only: D21 retired coupling in favour of parts
CLASSES = ["A", "B", "C", "D", "E"]
APPLIED = {"APPLIED", "VERIFIED"}
READINESS = ["READY", "SPLIT_RECOMMENDED", "NEEDS_RULING"]
# Policy gates the Product Owner may waive with a recorded override. Everything else this
# script checks is well-formedness: an override cannot make a malformed record well-formed.
OVERRIDABLE = ["scope_freeze", "readiness", "modification_class", "gate_tier", "deferral",
               "review_cap", "dry_run"]
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
REQUIRED_BEYOND_INTAKE = ["targets", "gate_tier", "readiness"]

# Format 2.1 (D26): the review ledger, its caps, the dry run and the estimate. A record with no
# `format` is a legacy record and is checked exactly as before.
FORMAT_D26 = (2, 1)
REVIEW_MODES = ["ANALYZE", "PLAN", "SKILL"]
REVIEW_KINDS = ["DRY_RUN", "FULL", "DIFF_CHECK"]
REVIEW_CAP = {"FULL": 2, "DIFF_CHECK": 1}
NEEDS_ESTIMATE = ["ANALYZED", "PLANNING", "PLANNED", "EXECUTING", "COMPLETE"]


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


def _intake_checks(fm, body):
    """What a triage draft must carry at INTAKE, so the run's conclusions live in the file."""
    bad = []
    if not fm.get("parts"):
        bad.append("INTAKE: parts are absent; triage puts every item into a part, so the run's "
                   "grouping lives in the file and not only in chat")
    text = "\n" + body
    if "\n## Intake" not in text:
        bad.append("INTAKE: section '## Intake' is absent; every item handed in, and why the parts "
                   "are shaped as they are, goes in the file")
    elif len(text.split("\n## Intake", 1)[1].split("\n## ", 1)[0].strip()) < 40:
        bad.append("INTAKE: section '## Intake' is present but empty")
    return bad


def _parts_checks(fm, items):
    """One run is one Modification, and its parts carry failure (D21). Returns (failures, parts)."""
    parts = fm.get("parts")
    if parts in (None, [], ""):
        return [], []  # a Modification with no parts is a single part
    if not isinstance(parts, list):
        return ["parts must be a list"], []
    bad, part_ids, owner = [], [], {}
    item_ids = [i.get("id") for i in items if isinstance(i, dict) and i.get("id")]
    for n, part in enumerate(parts, 1):
        if not isinstance(part, dict) or not part.get("id"):
            bad.append(f"part {n} has no id")
            continue
        pid = part["id"]
        if pid in part_ids:
            bad.append(f"part id {pid} is used twice")
        part_ids.append(pid)
        members = part.get("items")
        if not isinstance(members, list) or not members:
            bad.append(f"part {pid} has no items")
            continue
        for iid in members:
            if iid not in item_ids:
                bad.append(f"part {pid} names {iid}, which is not an item")
            elif iid in owner:
                bad.append(f"{iid} is in both {owner[iid]} and {pid}; an item belongs to exactly one part")
            else:
                owner[iid] = pid
    for iid in item_ids:
        if iid not in owner:
            bad.append(f"{iid} is in no part; every item belongs to exactly one part")
    order = {}
    for part in parts:
        if not isinstance(part, dict) or not part.get("id"):
            continue
        after = part.get("after") or []
        if not isinstance(after, list):
            bad.append(f"part {part['id']} has an 'after' that is not a list")
            continue
        for dep in after:
            if dep == part["id"]:
                bad.append(f"part {part['id']} is ordered after itself")
            elif dep not in part_ids:
                bad.append(f"part {part['id']} is ordered after {dep}, which is not a part")
        order[part["id"]] = [d for d in after if d in part_ids and d != part["id"]]
    # Parts ordered in a cycle can never land: peel off parts with nothing left to wait for.
    waiting = {pid: set(deps) for pid, deps in order.items()}
    while True:
        ready = [pid for pid, deps in waiting.items() if not deps]
        if not ready:
            break
        for pid in ready:
            del waiting[pid]
        for deps in waiting.values():
            deps.difference_update(ready)
    if waiting:
        bad.append(f"parts are ordered in a cycle and can never land: {sorted(waiting)}")
    return bad, [p for p in parts if isinstance(p, dict) and p.get("id")]


def _half_applied(parts, items):
    """A part lands whole or not at all (D21-B)."""
    disposition = {i.get("id"): i.get("disposition") for i in items if isinstance(i, dict)}
    bad = []
    for part in parts:
        seen = {disposition.get(iid) for iid in part.get("items") or []}
        if seen & APPLIED and "BLOCKED" in seen:
            bad.append(f"part {part['id']} is half applied; a part lands whole or not at all -- "
                       "roll back what was applied, or unblock the rest")
    return bad


def _format(fm):
    """(version tuple or None for a legacy record, failure string or None)."""
    raw = fm.get("format")
    if raw in (None, ""):
        return None, None
    try:
        return tuple(int(n) for n in str(raw).split(".")), None
    except ValueError:
        return None, f"format {raw!r} is not a version such as \"2.1\""


def _waived(fm):
    """The policy gates an attributed override waives for the D26 checks.

    An override counts only with a `by` and a `reason`. check() reports a malformed override only
    past INTAKE and short of a terminal state, so without this an unattributed block on an INTAKE or
    ABANDONED record would waive the review cap silently."""
    override = fm.get("override") or {}
    if not isinstance(override, dict):
        return []
    if not (str(override.get("by") or "").strip() and str(override.get("reason") or "").strip()):
        return []
    raw = override.get("overrides")
    return [raw] if isinstance(raw, str) else list(raw or [])


def _reviews_shape(fm):
    """The ledger is a list of well-formed rounds. Returns (failures, rounds that parsed)."""
    if "reviews" not in fm:
        return ["format 2.1 requires reviews, the review ledger: [] when no round has run (D26)"], []
    rounds = fm.get("reviews")
    if rounds is None:
        rounds = []
    if not isinstance(rounds, list):
        return ["reviews must be a list of rounds"], []
    bad, good = [], []
    for n, r in enumerate(rounds, 1):
        if not isinstance(r, dict):
            bad.append(f"review {n} is not a mapping")
            continue
        before = len(bad)
        if r.get("mode") not in REVIEW_MODES:
            bad.append(f"review {n} mode {r.get('mode')!r} not in {REVIEW_MODES}")
        if r.get("kind") not in REVIEW_KINDS:
            bad.append(f"review {n} kind {r.get('kind')!r} not in {REVIEW_KINDS}")
        if not str(r.get("date") or "").strip():
            bad.append(f"review {n} has no date")
        opened = r.get("required_open")
        if isinstance(opened, bool) or not isinstance(opened, int) or opened < 0:
            bad.append(f"review {n} required_open must be a count of 0 or more, got {opened!r}")
        if not str(r.get("outcome") or "").strip():
            bad.append(f"review {n} has no outcome")
        if len(bad) == before:
            good.append(r)
    return bad, good


def _review_caps(rounds, waived):
    """At most two full reviews and one diff check per mode (D26-A rule 2)."""
    if "review_cap" in waived:
        return []
    bad = []
    for mode in REVIEW_MODES:
        for kind, cap in REVIEW_CAP.items():
            n = sum(1 for r in rounds if r["mode"] == mode and r["kind"] == kind)
            if n > cap:
                bad.append(f"REVIEW CAP: {n} {mode} {kind} rounds, cap {cap}; the output goes to Nathan "
                           "with its open findings listed, and a further round is his override "
                           "(review_cap)")
    return bad


def _dry_run_first(rounds, waived):
    """PLAN's first full review comes after a PLAN dry run (D26-A rule 1)."""
    if "dry_run" in waived:
        return []
    for r in rounds:
        if r["mode"] == "PLAN" and r["kind"] == "DRY_RUN":
            return []
        if r["mode"] == "PLAN" and r["kind"] == "FULL":
            return ["DRY RUN FIRST: PLAN's first FULL review precedes any PLAN DRY_RUN; run every "
                    "normal-path gate read-only before a full review, or record Nathan's override (dry_run)"]
    return []


def _estimate_check(fm, status):
    """ANALYZE prices PLAN and EXECUTE before anything is approved (D26-D)."""
    if status not in NEEDS_ESTIMATE:
        return []
    est = fm.get("estimate")
    if not isinstance(est, dict) or not all(str(est.get(k) or "").strip() for k in ("plan", "execute")):
        return [f"ESTIMATE: status {status} requires estimate with plan and execute set, the time and "
                "tokens each will take; it is what re-pricing at twice the estimate is measured against"]
    return []


def _d26_checks(fm, status):
    """Format 2.1 only. A legacy record never reaches here."""
    bad, rounds = _reviews_shape(fm)
    waived = _waived(fm)
    return bad + _review_caps(rounds, waived) + _dry_run_first(rounds, waived) + _estimate_check(fm, status)


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

    parts_bad, parts = _parts_checks(fm, items)
    bad.extend(parts_bad)

    version, format_bad = _format(fm)
    if format_bad:
        bad.append(format_bad)
    elif version is not None and version >= FORMAT_D26:
        bad.extend(_d26_checks(fm, status))

    if status == "INTAKE":
        # A triage draft is held to what triage writes, and nothing further: its parts, and an
        # Intake section holding every item handed in. The 2026-09-22 comparison test found a
        # run's conclusions living only in chat.
        return bad + _intake_checks(fm, body)

    # A Modification can stop from any point. One abandoned at INTAKE never had an analysis, so its
    # stopping is not a reason to demand the analysis fields -- that would be demanding a lie.
    if status not in TERMINAL:
        for key in REQUIRED_BEYOND_INTAKE:
            if fm.get(key) in (None, ""):
                bad.append(f"missing required key beyond INTAKE: {key}")
        # A batch mixes classes -- a rule change beside a prompt defect -- so the class is per part.
        if parts:
            for part in parts:
                if part.get("class") in (None, ""):
                    bad.append(f"part {part['id']} has no class; ANALYZE sets one of {CLASSES}")
        elif fm.get("modification_class") in (None, ""):
            bad.append("missing required key beyond INTAKE: modification_class, or parts each with a class")
    for part in parts:
        if part.get("class") not in (None, "") and part.get("class") not in CLASSES:
            bad.append(f"part {part['id']} class {part.get('class')!r} not in {CLASSES}")

    if fm.get("coupling") not in COUPLINGS and "coupling" in fm:
        bad.append(f"coupling {fm.get('coupling')!r} not in {COUPLINGS}")
    if fm.get("readiness") not in READINESS and fm.get("readiness"):
        bad.append(f"readiness {fm.get('readiness')!r} not in {READINESS}")
    if fm.get("gate_tier") not in (0, 1, 2) and fm.get("gate_tier") is not None:
        bad.append(f"gate_tier {fm.get('gate_tier')!r} must be 0, 1 or 2")
    for tgt in fm.get("targets") or []:
        if tgt not in TARGETS:
            bad.append(f"target {tgt!r} not in {TARGETS}")

    if status in ("COMPLETE", "BLOCKED"):
        bad.extend(_half_applied(parts, items))

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
    # freeze is the rule that bounds scope (review rounds are bounded by D26, below). Found by the
    # stage 4 pilot; PAIR-001.
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

_GOOD_BATCH = """---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-selftest-batch
status: COMPLETE
targets: [skill, prompt]
gate_tier: 1
readiness: READY
interaction_cost_predicted: 5
interaction_cost_actual: 5
item_count_at_approval: 3
items:
  - id: ITEM-01
    statement: "one rule, first surface"
    disposition: APPLIED
  - id: ITEM-02
    statement: "one rule, second surface"
    disposition: VERIFIED
  - id: ITEM-03
    statement: "an unrelated change, blocked"
    disposition: BLOCKED
parts:
  - id: PART-01
    items: [ITEM-01, ITEM-02]
    class: B
  - id: PART-02
    items: [ITEM-03]
    class: D
    after: [PART-01]
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
# The fixture itself proves parts land independently: PART-02 is blocked beside a landed PART-01.

_BATCH_REGRESSIONS = [
    ("an item in no part",
     lambda s: s.replace("items: [ITEM-01, ITEM-02]", "items: [ITEM-01]"), "is in no part"),
    ("an item in two parts",
     lambda s: s.replace("items: [ITEM-03]", "items: [ITEM-03, ITEM-02]"), "in both"),
    ("a part naming an item that does not exist",
     lambda s: s.replace("items: [ITEM-03]", "items: [ITEM-03, ITEM-09]"), "which is not an item"),
    ("a part ordered after a part that does not exist",
     lambda s: s.replace("after: [PART-01]", "after: [PART-07]"), "which is not a part"),
    ("parts ordered in a cycle",
     lambda s: s.replace("    class: B\n", "    class: B\n    after: [PART-02]\n"), "cycle"),
    ("a part with no class past INTAKE",
     lambda s: s.replace("    class: D\n", ""), "has no class"),
    ("a part half applied",
     lambda s: s.replace("    disposition: VERIFIED", "    disposition: BLOCKED"), "half applied"),
    ("a part left half applied when the whole Modification stopped",
     lambda s: s.replace("status: COMPLETE", "status: BLOCKED")
                .replace("    disposition: VERIFIED", "    disposition: BLOCKED"), "half applied"),
    ("a part with one item applied and one not needed",
     lambda s: s.replace("    disposition: VERIFIED", "    disposition: NOT_APPLICABLE"),
     None),  # must PASS: NOT_APPLICABLE is not a failure to land
]

_GOOD_INTAKE = """---
artifact_type: GCFPE_MODIFICATION_RECORD
modification_id: MODIFICATION-20260923-selftest-intake
status: INTAKE
items:
  - id: ITEM-01
    statement: "a real statement"
    source: AF-000
  - id: ITEM-02
    statement: "another real statement"
    source: AF-001
parts:
  - id: PART-01
    items: [ITEM-01]
  - id: PART-02
    items: [ITEM-02]
    after: [PART-01]
request: "what was pasted"
---
# MODIFICATION-20260923-selftest-intake
One sentence.
## Intake
every item handed in, and why the parts are shaped as they are, in enough words.
"""

_INTAKE_REGRESSIONS = [
    ("triage wrote no parts, so its grouping lived only in chat",
     lambda s: s.split("parts:\n", 1)[0] + "request:" + s.split("request:", 1)[1], "INTAKE: parts are absent"),
    ("the items handed in, and the reasons, exist only in chat",
     lambda s: s.split("## Intake")[0], "'## Intake' is absent"),
    ("a draft abandoned at INTAKE, before any analysis existed",
     lambda s: s.replace("status: INTAKE", "status: ABANDONED"),
     None),  # must PASS: a record of where it stopped, not a demand for fields it never reached
    ("an item triage put in no part",
     lambda s: s.replace("    items: [ITEM-02]\n    after: [PART-01]\n", "    items: [ITEM-01]\n"), "is in no part"),
]

_GOOD_D26 = """---
artifact_type: GCFPE_MODIFICATION_RECORD
format: "2.1"
modification_id: MODIFICATION-20260924-selftest-d26
status: COMPLETE
targets: [skill]
gate_tier: 0
readiness: READY
modification_class: B
interaction_cost_predicted: 6
interaction_cost_actual: 6
estimate:
  plan: "2 h, 0.5M tokens"
  execute: "3 h, 1M tokens"
reviews:
  - mode: ANALYZE
    kind: FULL
    date: 2026-09-24
    required_open: 1
    outcome: "one required defect; repaired"
  - mode: ANALYZE
    kind: FULL
    date: 2026-09-24
    required_open: 0
    outcome: "clean"
  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 0
    outcome: "every normal-path gate passed read-only"
  - mode: PLAN
    kind: FULL
    date: 2026-09-24
    required_open: 2
    outcome: "two required defects; repaired"
  - mode: PLAN
    kind: DIFF_CHECK
    date: 2026-09-24
    required_open: 0
    outcome: "repair diff clean; to Nathan with two accepted risks"
  - mode: SKILL
    kind: FULL
    date: 2026-09-24
    required_open: 0
    outcome: "SKILL_FIT_CONFIRMED twice"
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

_THIRD_PLAN_FULL = """  - mode: SKILL
    kind: FULL"""
_EXTRA_PLAN_FULLS = """  - mode: PLAN
    kind: FULL
    date: 2026-09-24
    required_open: 1
    outcome: "after repair"
  - mode: PLAN
    kind: FULL
    date: 2026-09-24
    required_open: 1
    outcome: "a third round"
""" + _THIRD_PLAN_FULL

_D26_REGRESSIONS = [
    ("format 2.1 record with no review ledger",
     lambda s: s.split("reviews:\n", 1)[0] + "item_count_at_approval:" + s.split("item_count_at_approval:", 1)[1],
     "requires reviews"),
    ("format 2.1 record with an empty review ledger",
     lambda s: s.split("reviews:\n", 1)[0] + "reviews: []\nitem_count_at_approval:" + s.split("item_count_at_approval:", 1)[1],
     None),  # must PASS: [] is the ledger before any round has run
    ("review ledger that is not a list",
     lambda s: s.split("reviews:\n", 1)[0] + "reviews: three rounds\nitem_count_at_approval:" + s.split("item_count_at_approval:", 1)[1],
     "must be a list"),
    ("review round with a mode outside the vocabulary",
     lambda s: s.replace("  - mode: SKILL", "  - mode: EXECUTE"), "mode 'EXECUTE' not in"),
    ("review round with a kind outside the vocabulary",
     lambda s: s.replace("    kind: DIFF_CHECK", "    kind: LIGHT_TOUCH"), "kind 'LIGHT_TOUCH' not in"),
    ("review round with no date",
     lambda s: s.replace("    date: 2026-09-24\n    required_open: 0\n    outcome: \"clean\"",
                         "    date: \"\"\n    required_open: 0\n    outcome: \"clean\""), "has no date"),
    ("review round with a negative required count",
     lambda s: s.replace("required_open: 2", "required_open: -2"), "required_open must be"),
    ("review round with a required count that is not a number",
     lambda s: s.replace("required_open: 2", "required_open: some"), "required_open must be"),
    ("review round with no outcome",
     lambda s: s.replace('outcome: "clean"', 'outcome: ""'), "has no outcome"),
    ("a third full PLAN review",
     lambda s: s.replace(_THIRD_PLAN_FULL, _EXTRA_PLAN_FULLS), "REVIEW CAP"),
    ("a second diff check in one mode",
     lambda s: s.replace(_THIRD_PLAN_FULL, """  - mode: PLAN
    kind: DIFF_CHECK
    date: 2026-09-24
    required_open: 0
    outcome: "a second diff check"
""" + _THIRD_PLAN_FULL), "REVIEW CAP"),
    ("a third full PLAN review that Nathan overrode",
     lambda s: s.replace(_THIRD_PLAN_FULL, _EXTRA_PLAN_FULLS).replace(
         "item_count_at_approval: 1",
         'item_count_at_approval: 1\noverride:\n  by: Nathan\n  overrides: [review_cap]\n  reason: "one more"'),
     None),  # must PASS: the cap stops a session, never Nathan
    ("two full reviews in each of two modes",
     lambda s: s.replace("""  - mode: SKILL
    kind: FULL
    date: 2026-09-24
    required_open: 0""", """  - mode: SKILL
    kind: FULL
    date: 2026-09-24
    required_open: 1
    outcome: "SKILL_REPAIR_REQUIRED"
  - mode: SKILL
    kind: FULL
    date: 2026-09-24
    required_open: 0"""),
     None),  # must PASS: the cap is per mode
    ("a full PLAN review with no dry run before it",
     lambda s: s.replace("""  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 0
    outcome: "every normal-path gate passed read-only"
""", ""), "DRY RUN FIRST"),
    ("a full PLAN review whose only dry run came after it",
     lambda s: s.replace("""  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 0
    outcome: "every normal-path gate passed read-only"
""", "").replace(_THIRD_PLAN_FULL, """  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 0
    outcome: "late"
""" + _THIRD_PLAN_FULL), "DRY RUN FIRST"),
    ("an ANALYZE dry run taken for PLAN's",
     lambda s: s.replace("""  - mode: PLAN
    kind: DRY_RUN""", """  - mode: ANALYZE
    kind: DRY_RUN"""), "DRY RUN FIRST"),
    ("a third full review waived by an unattributed override on an abandoned record",
     lambda s: s.replace("status: COMPLETE", "status: ABANDONED").replace(_THIRD_PLAN_FULL, _EXTRA_PLAN_FULLS)
                .replace("item_count_at_approval: 1",
                         'item_count_at_approval: 1\noverride:\n  overrides: [review_cap]\n  reason: "x"'),
     "REVIEW CAP"),
    ("a full PLAN review with no dry run, which Nathan overrode",
     lambda s: s.replace("""  - mode: PLAN
    kind: DRY_RUN
    date: 2026-09-24
    required_open: 0
    outcome: "every normal-path gate passed read-only"
""", "").replace(
         "item_count_at_approval: 1",
         'item_count_at_approval: 1\noverride:\n  by: Nathan\n  overrides: [dry_run]\n  reason: "x"'),
     None),  # must PASS
    ("no estimate past ANALYZE",
     lambda s: s.replace('  execute: "3 h, 1M tokens"', '  execute: ""'), "ESTIMATE"),
    ("an estimate that is not a mapping",
     lambda s: s.replace('estimate:\n  plan: "2 h, 0.5M tokens"\n  execute: "3 h, 1M tokens"', "estimate: soon"),
     "ESTIMATE"),
    ("no estimate on a record abandoned during analysis",
     lambda s: s.replace("status: COMPLETE", "status: ABANDONED").replace('  plan: "2 h, 0.5M tokens"', '  plan: ""'),
     None),  # must PASS: a terminal record is not asked for fields it never reached
    ("a format that is not a version",
     lambda s: s.replace('format: "2.1"', 'format: "two point one"'), "is not a version"),
    ("a legacy record, with no format, that ran three full reviews and set no estimate",
     lambda s: s.replace('format: "2.1"\n', "").replace(_THIRD_PLAN_FULL, _EXTRA_PLAN_FULLS)
                .replace('  execute: "3 h, 1M tokens"', '  execute: ""'),
     None),  # must PASS: legacy records validate exactly as before D26
]


def _run_cases(td, name, fixture, regressions, filename):
    """Validate a known-good fixture, then each injected regression against it."""
    failures = 0
    f = Path(td) / filename
    f.write_text(fixture, encoding="utf-8")
    problems = check(f)
    if problems:
        print(f"SELFTEST FAIL: the known-good {name} did not pass: {problems}")
        failures += 1
    else:
        print(f"ok    known-good {name} passes")
    for case, mutate, expect in regressions:
        f.write_text(mutate(fixture), encoding="utf-8")
        found = check(f)
        if expect is None:                       # must PASS
            if found:
                print(f"SELFTEST FAIL: should have passed: {case} -> {found}")
                failures += 1
            else:
                print(f"ok    correctly allowed: {case}")
        elif any(expect in pr for pr in found):
            print(f"ok    caught: {case}")
        else:
            print(f"SELFTEST FAIL: NOT caught: {case} (expected {expect!r}, got {found})")
            failures += 1
    return failures, 1 + len(regressions)


def selftest():
    import tempfile
    failures = total = 0
    with tempfile.TemporaryDirectory() as td:
        for name, fixture, regressions, filename in (
                ("record with no parts", _GOOD, _REGRESSIONS, "MODIFICATION-single.md"),
                ("batch with parts", _GOOD_BATCH, _BATCH_REGRESSIONS, "MODIFICATION-batch.md"),
                ("triage draft", _GOOD_INTAKE, _INTAKE_REGRESSIONS, "MODIFICATION-intake.md"),
                ("format 2.1 record", _GOOD_D26, _D26_REGRESSIONS, "MODIFICATION-d26.md")):
            f, t = _run_cases(td, name, fixture, regressions, filename)
            failures += f
            total += t
        # PAIR-001: every fixture above is hand-written, so none of them can notice the shipped
        # template drifting away from this script. Validate the template itself: as shipped, at
        # INTAKE, and filled in the minimum ANALYZE fills, at ANALYZING.
        for name, text in _template_cases():
            total += 1
            if text is None:
                print(f"SELFTEST FAIL: {name}")
                failures += 1
                continue
            f = Path(td) / "MODIFICATION-template.md"
            f.write_text(text, encoding="utf-8")
            found = check(f)
            if found:
                print(f"SELFTEST FAIL: the shipped template fails validation: {name} -> {found}")
                failures += 1
            else:
                print(f"ok    shipped template passes: {name}")
    print(f"\n{total - failures}/{total} selftest cases passed")
    return 1 if failures else 0


def _fenced(doc, begins):
    """The first ```markdown block after the heading `begins`."""
    return doc.split(begins, 1)[1].split("```markdown\n", 1)[1].split("\n```\n", 1)[0] + "\n"


def _template_cases():
    """The shipped template in modification-template.md, as (name, text) cases."""
    import re
    path = Path(__file__).resolve().with_name("modification-template.md")
    try:
        text = _fenced(path.read_text(encoding="utf-8"), "## TEMPLATE BEGINS")
    except (OSError, IndexError):
        return [("template not found, or not fenced where expected, in " + path.name, None)]
    at_analyzing = text.replace("status: INTAKE", "status: ANALYZING", 1)
    for key, value in (("targets", "[prompt]"), ("gate_tier", "1"), ("readiness", "READY")):
        at_analyzing = re.sub(rf"^{key}:[^\n]*", f"{key}: {value}", at_analyzing, count=1, flags=re.M)
    at_analyzing = re.sub(r"^(\s+class:)[^\n]*", r"\1 B", at_analyzing, count=1, flags=re.M)
    # At ANALYZED the analysis is written and the estimate is set (D26-D); nothing is approved yet.
    at_analyzed = at_analyzing.replace("status: ANALYZING", "status: ANALYZED", 1)
    at_analyzed = at_analyzed.replace('  plan: ""', '  plan: "2 h, 0.5M tokens"', 1)
    at_analyzed = at_analyzed.replace('  execute: ""', '  execute: "3 h, 1M tokens"', 1)
    at_analyzed = at_analyzed.replace("### Readiness and interaction cost\n",
                                      "### Readiness and interaction cost\n\ninteraction_cost = 0 + 2 + 1 + 0 + 1 = 4; "
                                      "READY.\n", 1)
    return [("as shipped, at INTAKE", text), ("filled as ANALYZE fills it, at ANALYZING", at_analyzing),
            ("filled at ANALYZED, with the estimate set", at_analyzed)]


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
