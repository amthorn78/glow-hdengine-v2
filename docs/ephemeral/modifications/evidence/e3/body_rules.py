#!/usr/bin/env python3
"""E3 body rules (spec v2 §3, §0 E3; A1-4 item 2): {id: body} JSON on stdin -> {id: edited_body} JSON on stdout.

Holds canonical texts (read verbatim from the v2 execution specification's §3 code blocks, never
re-authored) and anchor patterns (regexes naming headings and sentences by pattern). It holds no
body text. A per-body edit report (rule ids, counts, anchors not found) goes to stderr as JSON.
Nothing is written anywhere: bodies live only in this process's memory (D22).

usage: <bodies JSON> | PYTHONDONTWRITEBYTECODE=1 python3 body_rules.py [--registry <registry.md>] | <consumer>

Rule ids (spec step numbers; §P and child steps):
  S42   delete release-bound header lines in the header window (first 8 nonblank lines)
  S03   C-NOTION replaces the CONTROL_NOTION sentence (PR-10, PR-20, PR-30, PR-40, OPS-10/20/30)
  S04   QA-10: "Notion and repository persistence" -> step-4 literal (6 occurrences)
  S05   STEP5 bodies: delete ", or its direct Notion URL for a Notion-resident artifact"
  S08   C-ART first in the result/output section (NPH53)
  S13   C-HANDOFF replaces the field list after the NEXT_PROMPT_HANDOFF sentence (NPH53)
  S13V  "contain(s)" -> "ends with" in that sentence (step 18's 16 bodies)
  S13P  PR-30 step 6 / PR-35 Required inputs: drop worktree, branch, head, commits as handoff content
  S18   C-PLACE after the handoff paragraph (NPH53 minus ASK4)
  S18A  ASK OK? variant after the handoff paragraph (ASK4) and the old "end `ASK OK?`" clause removed
  S20   C-DEC after C-ART (PR-30, PR-35, RS-40)
  S22   C-LAT once in the section that sends findings to RS; "material boundary" -> step-22 literal
        in that section's routing sentences (LAT10)
  S32   C-SESSION replaces the continuity-list sentence(s)
  S37   C-SUB (PR-35 review section; RS-40 PR-35 phase)
  S39   C-DISPATCH after the "MERGE_PENDING — Ready to merge" line (PR-35, RS-40)
  W4    PR-40 entry: the W-4 sentence replaces the manual-merge assertion sentence
  CTOP  C-TOP after the handoff placement (NPH53) / beside PR-50's return rule
  C4R   PR-40: C-REPLAN replaces the "existing PR owner" branch
  C4E   PR-20: C-PR20-ENTRY added to its entry
  C4P   PR-30: C-PR30-ENTRY replaces its PR-40 return context
  C4Q   C-PROCEED replaces the single-Proceed sentence wherever it is carried
"""
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True

SPEC_PATH = Path(__file__).resolve().parents[2] / "specs" / "EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md"
SPEC = SPEC_PATH.read_text(encoding="utf-8")
S3 = SPEC[SPEC.index("## §3 Canonical wording, final"):SPEC.index("## §4 Graph transforms")]


def block_after(marker, nth=0):
    """The nth ```text block after a unique marker in §3 (same reader as e2/texts.py)."""
    assert S3.count(marker) == 1, marker
    i = S3.index(marker)
    for _ in range(nth + 1):
        j = S3.index("```text\n", i)
        k = S3.index("\n```", j + 8)
        val = S3[j + 8:k]
        i = k + 4
    return val


T = {
    "C-NOTION": block_after("**C-NOTION** (PART-02)"),
    "C-ART": block_after("**C-ART** (PART-03)"),
    "C-HANDOFF": block_after("**C-HANDOFF** (PART-04"),
    "C-PLACE": block_after("**C-PLACE** (PART-05)"),
    "C-DEC": block_after("**C-DEC** (PART-06"),
    "C-LAT": block_after("**C-LAT** (PART-07"),
    "C-SESSION": block_after("**C-SESSION** (PART-09), amended"),
    "C-SUB": block_after("**C-SUB** (PART-10), A1-5"),
    "C-DISPATCH": block_after("**C-DISPATCH** (PART-11), A1-5"),
    "C-TOP": block_after("**C-TOP** (A1-8), new"),
    "ASK-VARIANT": block_after("**C-PLACE, `ASK OK?` variant**"),
    "C-REPLAN": block_after("**C-REPLAN**"),
    "C-PROCEED": block_after("**C-PROCEED** (the single-Proceed rule"),
    "C-PR20-ENTRY": block_after("**C-PR20-ENTRY**"),
    "C-PR30-ENTRY": block_after("**C-PR30-ENTRY**"),
    "STEP4": block_after("**Step 4** — QA-10"),
    "STEP22": block_after("**Step 22** — the C-LAT bodies"),
    "W4": block_after("**PR-40 entry wording**"),
    "PR35-ROLE": block_after("**PR-35 role** (§12 W-1)"),
    "RS40-ROLE": block_after("**RS-40 role** (§12 W-2"),
}
# Settled by the plan's author after the first E4 (coordinator, 2026-09-23): the replacement for a
# "material boundary" routing sentence that precedes C-LAT, where "(as defined above)" would be false.
T["STEP22-BEFORE"] = "material change (D23-C)"
assert T["ASK-VARIANT"].startswith(T["C-PLACE"] + " ")
assert "\n\n" in T["C-LAT"] and "\n" not in T["C-HANDOFF"]

# ---- row selectors (spec §7.1) ------------------------------------------------------------
ALL = None  # every body supplied
STEP3 = {"PR-10", "PR-20", "PR-30", "PR-40", "OPS-10", "OPS-20", "OPS-30"}
STEP3_EXTRA = {"QA-10"}  # settled item 3: QA-10's CONTROL_NOTION sentence takes C-NOTION too
STEP5 = {"CF-C-10", "CF-C-20", "CF-C-30", "CF-C-40", "CF-E-10", "CF-E-20", "CF-E-30", "CF-E-40", "CF-PO-10", "MGR-10"}
LAT10 = {"PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"}
ASK4 = {"QA-60", "QA-80", "RS-10", "RS-30"}
# Settled item 5: bodies outside ASK4 whose "end `ASK OK?`" describes the final response take the same
# treatment. QA-50 does; OPS-30 and ESC-30 describe a saved artifact ("ending `ASK OK?`") and are left.
ASK_EXTRA = {"QA-50"}
ASK_BODIES = ASK4 | ASK_EXTRA
DEC3 = {"PR-30", "PR-35", "RS-40"}
NOT_MAIN = {"GCFPE-MGMT-10"}
NO_HANDOFF = {"GCFPE-MGMT-10", "PR-50"}  # complement of NPH53 (registry-audit:2); checked against the registry


def nph_from_registry(path):
    """NPH53: rows whose required_literals contain NEXT_PROMPT_HANDOFF (spec §7.1 selector)."""
    sys.path.insert(0, "/tmp/claude-0/e2/skills/amthor-workspace-governance-audit/scripts")
    import audit_workspace_governance as A  # noqa: E402
    reg = A.load_data(path)
    return {r["prompt_key"] for r in reg["prompts"]
            if any((x.get("value") if isinstance(x, dict) else x) == "NEXT_PROMPT_HANDOFF"
                   for x in (r["audit_assertions"].get("required_literals") or []))}, \
        {r["prompt_key"]: [o.get("artifact") for o in r["outputs"]] for r in reg["prompts"]}


# ---- anchor patterns ----------------------------------------------------------------------
HEADING = re.compile(r"^#{1,6} ")
RELEASE_KEY = re.compile(
    r"^[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?`?(?:Prompt [Vv]ersion|Ecosystem release|Set)(?:\*\*|__|`)?[ \t]*:")
CONTROL_NOTION_SENTENCE = re.compile(r"Concise authorized operational state and pointers remain `CONTROL_NOTION`\.")
STEP4_OLD = "Notion and repository persistence"
STEP5_OLD = ", or its direct Notion URL for a Notion-resident artifact"
RESULT_HEADING = re.compile(r"(?i)^#{1,6} .*\b(?:results?|outputs?)\b")
# the block-shape sentence: one fenced block whose first line is NEXT_PROMPT_HANDOFF
TOKEN_SENTENCE = re.compile(r"(?i)\bfenced\b[^.\n]*NEXT_PROMPT_HANDOFF|NEXT_PROMPT_HANDOFF[^.\n]*\bfenced\b")
FENCED_BLOCK = re.compile(r"(?i)\bexactly one\b[^.\n]*\bfenced\b[^.\n]*\bblock\b")
FIELD_LIST_START = re.compile(r"^(?:The block|It|Its)\b")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z`*\"“(])")
# a sentence after the field list that states terminal/no-block behaviour or a boundary is kept
KEEP_SENTENCE = re.compile(
    r"(?i)\bterminal\b|\bemits? no\b|\bno continuation\b|\bcontains? no\b|\bmust contain no\b|\bgrants? no\b|"
    r"\bdoes not (?:supply|grant)\b|\btransports?\b")
VERB_CONTAIN = [(re.compile(r"\bmust contain exactly one\b"), "must end with exactly one"),
                (re.compile(r"\bcontains exactly one\b"), "ends with exactly one"),
                (re.compile(r"\bmust contain one\b"), "must end with one"),
                (re.compile(r"\bcontains one\b"), "ends with one")]
OLD_ASK = re.compile(r",?\s*(?:and\s+)?\bends?\s+`ASK OK\?`")
RS_HEADING = re.compile(r"(?i)^#{1,6} .*(?:rescope|→\s*RS-\d|\bRS-(?:10|20)\b)")
MATERIAL_HEADING = re.compile(r"(?i)^#{1,6} .*\bmaterial\b")
ROUTE_TO_RS = re.compile(
    r"(?i)\b(?:continue|continues|hand(?:s|ed)?\s+off|handoff|route|routes|through|goes|go)\b"
    r"[^.\n]*\bRS-(?:10|20)\b")
ROUTE_TO_ANY_RS = re.compile(
    r"(?i)\b(?:continue|continues|hand(?:s|ed)?\s+off|handoff|route|routes|through|goes|go)\b"
    r"[^.\n]*\bRS-\d+\b")
ROUTING = re.compile(r"(?i)\bRS-\d+\b|rescope")
MATERIAL_BOUNDARY = re.compile(r"\bmaterial boundary\b")
CONTINUITY_SENTENCE = re.compile(
    r"[^.\n]*(?:continuity list|canonical list|shared_exactly_one|preserves? exactly one)[^.\n]*"
    r"dedicated PR-development session[^.\n]*\.")
TWO_PHASES_LEAD = re.compile(r"`?PR-30`? and `?PR-35`? are two phases of one [^.\n]*\.")
REVIEW_HEADING = re.compile(r"(?i)^#{1,6} .*\breview")
PR35_PHASE_HEADING = re.compile(r"^#{1,6} .*PR_RETURN_PHASE: PR-35")
READY_LINE = re.compile(r"MERGE_PENDING — Ready to merge")
W4_OLD = re.compile(r"Nathan's later invocation of PR-40 [^.\n]*asserts that Nathan manually merged the identified PR[^.\n]*\.")
REPLAN_HEADING = re.compile(r"^#{1,6} PRECISE IN-SCOPE DEFECT → existing PR owner\s*$")
PROCEED_SENTENCE = re.compile(r"The original (?:Product Owner )?Proceed remains the sole implementation authority[^.\n]*\.")
PR30_RETURN_CONTEXT = re.compile(r"[^.\n]*\bPR-40\b[^.\n]*\b(?:returns?|REJECT|reject(?:ed|ion)?)\b[^.\n]*\bPR-30\b[^.\n]*\.")
PR20_ENTRY_HEADING = re.compile(r"(?i)^#{1,6} .*(?:inputs?|entry|intake)")
RETURN_RULE = re.compile(r"(?i)\breturn control\b|\bemits? no continuation\b")
HANDOFF_CONTENT_ITEMS = re.compile(r"(?:workspace/worktree|branch|(?:local and )?remote head|commits), ")


class Body:
    def __init__(self, pid, text):
        self.pid, self.lines = pid, text.split("\n")
        self.report = {"applied": {}, "not_found": [], "notes": []}

    def text(self):
        return "\n".join(self.lines)

    def hit(self, rule, n=1):
        self.report["applied"][rule] = self.report["applied"].get(rule, 0) + n

    def miss(self, rule, why):
        self.report["not_found"].append(f"{rule}: {why}")

    def note(self, msg):
        self.report["notes"].append(msg)

    def headings(self):
        return [i for i, line in enumerate(self.lines) if HEADING.match(line)]

    def section_end(self, h):
        nxt = [i for i in self.headings() if i > h]
        return nxt[0] if nxt else len(self.lines)

    def section_index(self, i):
        return sum(1 for h in self.headings() if h <= i)


# ---- rules ------------------------------------------------------------------------------
def s42(b):
    nonblank = [i for i, line in enumerate(b.lines) if line.strip()][:8]
    drop = [i for i in nonblank if RELEASE_KEY.match(b.lines[i])]
    for i in reversed(drop):
        del b.lines[i]
    b.hit("S42", len(drop)) if drop else b.miss("S42", "no release-bound header line in the header window")


def sub_all(b, rule, pattern, repl, expected=None):
    text = b.text()
    new, n = (pattern.subn(lambda m: repl, text) if hasattr(pattern, "subn")
              else (text.replace(pattern, repl), text.count(pattern)))
    if n:
        b.lines = new.split("\n")
        b.hit(rule, n)
    else:
        b.miss(rule, "anchor sentence absent")
    if expected is not None and n != expected:
        b.note(f"{rule}: {n} occurrences replaced, expected {expected}")


def find_result_section(b, artifacts):
    heads = [h for h in b.headings() if RESULT_HEADING.match(b.lines[h])]
    names = [a for x in artifacts for a in re.split(r"\s*/\s*", x or "") if a]

    def names_artifact(h):
        seg = "\n".join(b.lines[h:b.section_end(h)])
        return any(re.search(r"(?<![A-Z_])" + re.escape(a) + r"(?![A-Z_])", seg) for a in names)
    for h in heads:
        if names_artifact(h):
            return h, "result heading naming the output artifact"
    if heads:
        return heads[0], "first result heading (artifact not named in it)"
    for h in b.headings():
        if names_artifact(h):
            return h, "first section naming the output artifact (no result heading)"
    return None, None


def s08_s20(b, artifacts):
    h, how = find_result_section(b, artifacts)
    if h is None:
        b.miss("S08", "no result/output heading and no section naming the output artifact")
        return
    ins = [T["C-ART"]]
    if b.pid in DEC3:
        ins.append(T["C-DEC"])
    b.lines[h + 1:h + 1] = ins
    b.hit("S08")
    b.note(f"S08: section #{b.section_index(h)} ({how})")
    if b.pid in DEC3:
        b.hit("S20")


def block_shape(sents):
    """Index range [a, b) of the block-shape sentence(s): one sentence naming a fenced block with
    NEXT_PROMPT_HANDOFF, or a fenced-block sentence followed by one naming NEXT_PROMPT_HANDOFF."""
    for k, x in enumerate(sents):
        if TOKEN_SENTENCE.search(x):
            return k, k + 1
        if FENCED_BLOCK.search(x) and k + 1 < len(sents) and "NEXT_PROMPT_HANDOFF" in sents[k + 1]:
            return k, k + 2
    return None


def field_run(sents, end):
    j = end
    while j < len(sents) and not KEEP_SENTENCE.search(sents[j]):
        j += 1
    return j


def next_line_field_list(b, i):
    """True when line i ends with the block shape and line i+1 opens with a field-list sentence."""
    return (i + 1 < len(b.lines) and FIELD_LIST_START.match(b.lines[i + 1])
            and field_run(SENT_SPLIT.split(b.lines[i + 1]), 0) > 0)


def handoff_line(b):
    """Lines carrying the block-shape sentence(s) followed by at least one field-list sentence,
    in the same line or (block shape ending its line) as the next line's opening sentences."""
    found = []
    for i, line in enumerate(b.lines):
        if "NEXT_PROMPT_HANDOFF" not in line:
            continue
        sents = SENT_SPLIT.split(line)
        rng = block_shape(sents)
        if rng and (field_run(sents, rng[1]) > rng[1] or (rng[1] == len(sents) and next_line_field_list(b, i))):
            found.append(i)
    return found


def s13_s18(b):
    idx = handoff_line(b)
    if len(idx) != 1:
        b.miss("S13", f"{len(idx)} lines carry the NEXT_PROMPT_HANDOFF block-shape sentence followed by a field list (need exactly 1)")
        return None
    i = idx[0]
    sents = SENT_SPLIT.split(b.lines[i])
    a, e = block_shape(sents)
    shape = sents[a:e]
    for rx, rep in VERB_CONTAIN:
        new, n = rx.subn(rep, shape[0])
        if n:
            shape[0] = new
            b.hit("S13V", n)
            break
    j = field_run(sents, e)
    if j > e:
        consumed, kept = j - e, len(sents) - j
        b.lines[i] = " ".join(sents[:a] + shape + [T["C-HANDOFF"]] + sents[j:])
        where = "same line"
    else:
        nxt = SENT_SPLIT.split(b.lines[i + 1])
        j2 = field_run(nxt, 0)
        consumed, kept = j2, len(nxt) - j2
        b.lines[i] = " ".join(sents[:a] + shape + [T["C-HANDOFF"]])
        if kept:
            b.lines[i + 1] = " ".join(nxt[j2:])
        else:
            del b.lines[i + 1]
        where = "field list on the next line"
    b.hit("S13")
    b.note(f"S13: section #{b.section_index(i)} ({where}); {consumed} field-list sentence(s) replaced, {kept} kept after it")
    return i


def s18_ctop(b, i):
    if b.pid in ASK_BODIES:
        text = b.text()
        new, n = OLD_ASK.subn("", text)
        if n:
            b.lines = new.split("\n")
            b.hit("S18A-old-clause-removed", n)
        else:
            b.miss("S18A", "old `ASK OK?` clause absent")
        i = handoff_line(b)[0] if len(handoff_line(b)) == 1 else i
        place, rule = T["ASK-VARIANT"], "S18A"
    else:
        place, rule = T["C-PLACE"], "S18"
    # settled: C-PLACE (or its variant) and C-TOP form their own paragraph, with a blank line before and after
    b.lines[i + 1:i + 1] = ["", place + " " + T["C-TOP"], ""]
    b.hit(rule)
    b.hit("CTOP")


def ctop_pr50(b):
    heads = [h for h in b.headings() if RESULT_HEADING.match(b.lines[h])]
    for h in reversed(heads):
        for k in range(h + 1, b.section_end(h)):
            if RETURN_RULE.search(b.lines[k]):
                b.lines[k + 1:k + 1] = ["", T["C-TOP"], ""]
                b.hit("CTOP")
                return
    b.miss("CTOP", "no return rule in a result section")


def s13p(b):
    if b.pid == "PR-35":
        h = next((h for h in b.headings() if re.match(r"(?i)^#{1,6} Required inputs", b.lines[h])), None)
        rng = range(h + 1, b.section_end(h)) if h is not None else range(0)
        targets = [k for k in rng if b.lines[k].lstrip().startswith("- ") and HANDOFF_CONTENT_ITEMS.search(b.lines[k])]
    elif b.pid == "PR-30":
        h = next((h for h in b.headings() if re.match(r"^#{1,6} Execute\s*$", b.lines[h])), None)
        rng = range(h + 1, b.section_end(h)) if h is not None else range(0)
        targets = [k for k in rng if b.lines[k].startswith("6. ") and HANDOFF_CONTENT_ITEMS.search(b.lines[k])]
    else:
        return
    n = 0
    for k in targets:
        b.lines[k], m = HANDOFF_CONTENT_ITEMS.subn("", b.lines[k])
        n += m
    b.hit("S13P", n) if n else b.miss("S13P", "handoff-content list (worktree/branch/head/commits) not found")


def s22(b):
    heads = [h for h in b.headings() if RS_HEADING.match(b.lines[h])]
    how = "heading names rescope or an RS route"
    if not heads:
        heads = [h for h in b.headings()
                 if any(ROUTE_TO_RS.search(x) for line in b.lines[h + 1:b.section_end(h)] for x in SENT_SPLIT.split(line))]
        how = "first section with a sentence routing to RS-10/RS-20"
    if not heads:
        heads = [h for h in b.headings()
                 if any(ROUTE_TO_ANY_RS.search(x) for line in b.lines[h + 1:b.section_end(h)] for x in SENT_SPLIT.split(line))]
        how = "first section with a sentence routing to an RS prompt"
    if not heads:
        heads = [h for h in b.headings() if MATERIAL_HEADING.match(b.lines[h])]
        how = "no section routes to RS; first heading naming 'material'"
    if not heads:
        b.miss("S22", "no section sends findings to RS")
        return
    h = heads[0]
    lat = T["C-LAT"].split("\n")
    b.lines[h + 1:h + 1] = lat
    b.hit("S22")
    if b.lines[h + 1 + len(lat)].lstrip()[:3] in {"1. ", "- "}:
        b.note("S22: the section's own text begins with a list directly after C-LAT")
    n = 0
    before = 0
    for k in range(0, h):
        if ROUTING.search(b.lines[k]):
            b.lines[k], m = MATERIAL_BOUNDARY.subn(T["STEP22-BEFORE"], b.lines[k])
            before += m
    b.hit("S22-before", before) if before else None
    for k in range(h + 1 + len(lat), len(b.lines)):
        # a routing sentence: its line (one Notion paragraph or list item) sends the finding to RS
        if ROUTING.search(b.lines[k]):
            b.lines[k], changed = MATERIAL_BOUNDARY.subn(T["STEP22"], b.lines[k])
            n += changed
    total = len(MATERIAL_BOUNDARY.findall(b.text()))
    b.hit("S22-literal", n) if n else None
    b.note(f"S22: section #{b.section_index(h)} ({how}); 'material boundary' replaced {n} in routing sentences after C-LAT;"
           f" {before} before C-LAT replaced by 'material change (D23-C)'; {total} occurrence(s) remain in the body")


def s32(b):
    n = 0
    for k, line in enumerate(b.lines):
        sents = SENT_SPLIT.split(line)
        hits = [q for q, x in enumerate(sents) if CONTINUITY_SENTENCE.fullmatch(x)]
        if not hits:
            continue
        q0, q1 = hits[0], hits[-1]
        if q0 > 0 and TWO_PHASES_LEAD.fullmatch(sents[q0 - 1]):
            q0 -= 1
        b.lines[k] = " ".join(sents[:q0] + [T["C-SESSION"]] + sents[q1 + 1:])
        n += 1
    b.hit("S32", n) if n else b.miss("S32", "no continuity-list sentence naming the dedicated PR-development session")


def s37(b):
    if b.pid == "PR-35":
        heads = [h for h in b.headings() if REVIEW_HEADING.match(b.lines[h]) and "input" not in b.lines[h].lower()]
    else:
        heads = [h for h in b.headings() if PR35_PHASE_HEADING.match(b.lines[h])]
    if not heads:
        b.miss("S37", "no PR-35 review/phase heading")
        return
    b.lines[heads[0] + 1:heads[0] + 1] = [T["C-SUB"]]
    b.hit("S37")
    b.note(f"S37: section #{b.section_index(heads[0])}")


def s39(b):
    k = next((k for k, line in enumerate(b.lines) if READY_LINE.search(line)), None)
    if k is None:
        b.miss("S39", "no 'MERGE_PENDING — Ready to merge' line")
        return
    b.lines[k + 1:k + 1] = [T["C-DISPATCH"]]
    b.hit("S39")
    b.note(f"S39: section #{b.section_index(k)}")


def c4r(b):
    h = next((h for h in b.headings() if REPLAN_HEADING.match(b.lines[h])), None)
    if h is None:
        b.miss("C4R", "no 'existing PR owner' branch heading")
        return
    end = b.section_end(h)
    b.lines[h:end] = [T["C-REPLAN"]]
    b.hit("C4R")
    b.note(f"C4R: branch of {end - h} lines replaced")


def c4e(b):
    heads = [h for h in b.headings() if PR20_ENTRY_HEADING.match(b.lines[h])]
    if not heads:
        b.miss("C4E", "no entry/inputs heading")
        return
    end = b.section_end(heads[0])
    b.lines[end:end] = [T["C-PR20-ENTRY"]]
    b.hit("C4E")
    b.note(f"C4E: end of section #{b.section_index(heads[0])}")



# ---- settled item 2: converge every statement that PR-35 shares PR-30's session ------------------------
# Each class is (id, pattern, replacement). A line saying the same/dedicated PR-development session covers
# PR-35 is rewritten to name each phase's own session in C-SESSION's wording. Lines where PR-20 and PR-30
# share one planning-and-build session, and PR-35's re-entry into its own session, are not matched.
OWN35 = "PR-35 in its own dedicated session"
CONVERGE = [
    ("X01", re.compile(r"continues in the same session to PR-35"), "continues to " + OWN35),
    ("X02", re.compile(r"same-session PR-35 (review/CI convergence)"), r"PR-35 \1 in its own dedicated session"),
    ("X03", re.compile(r"\bhands the same dedicated PR-development session to PR-35 without another Proceed, session, "),
     "hands off to " + OWN35 + " without another Proceed, "),
    ("X04", re.compile(r"\bbranch preserves the same session, workspace/worktree"),
     "branch preserves the recorded phase's own dedicated session, workspace/worktree"),
    ("X05", re.compile(r"resumes the recorded phase in the same PR session"),
     "resumes the recorded phase in its own dedicated session"),
    ("X06", re.compile(r"\bthe same session/workspace/worktree/branch/open PR"),
     "the recorded phase's own dedicated session and the same workspace/worktree/branch/open PR"),
    ("X07", re.compile(r"\bsame session/workspace/worktree/branch/open PR"),
     "recorded phase's own dedicated session and the same workspace/worktree/branch/open PR"),
    ("X08", re.compile(r"exactly one complete same-session handoff to (selected )?PR-35\b"),
     r"exactly one complete handoff to \1PR-35 in its own dedicated session"),
    ("X09", re.compile(r"\bsame-session PR-35 handoff"), "PR-35 handoff to PR-35's own dedicated session"),
    ("X10", re.compile(r"directly to this same dedicated PR-development session"), "directly to PR-35's own dedicated session"),
    ("X11", re.compile(r"(`PR-35 —[^\n]*?) in this same dedicated PR-development session"),
     r"\1 in PR-35's own dedicated session"),
    ("X12", re.compile(r"according to the recorded phase, in the same PR session"),
     "according to the recorded phase, in that phase's own dedicated session"),
    ("X13", re.compile(r"You are the same dedicated PR engineering session for the exact suspended work unit\."), "RS40-ROLE"),
    ("X14", re.compile(r"original Product Owner Proceed; same dedicated PR-development session, "),
     "original Product Owner Proceed; the recorded phase's own dedicated session, "),
    ("X15", re.compile(r"You are the same dedicated PR-development session that produced or recovered the exact "
                       r"`PR_CANDIDATE_PUBLISHED` result for one proceeded work unit\."), "PR35-ROLE-1"),
    ("X16", re.compile(r"PR-35 is a same-session continuation inside"), "PR-35 is a phase continuation, in its own dedicated session, inside"),
    ("X17", re.compile(r"(PR-35\b[^\n]*?(?:adds no|neither merges nor adds a) [^.\n]*?\b)session, "),
     r"\1session beyond its own dedicated PR-35 session, "),
    ("X17b", re.compile(r"(PR-35[^.\n]*adds no [^.\n]*?), ([^,.\n]+), or cross-session route"), r"\1, or \2"),
    ("X18", re.compile(r"Require one complete same-session package containing:"), "Require one complete PR-35 handoff package containing:"),
    ("X19", re.compile(r"the same dedicated PR-session reference and `session_disposition: RETAIN_EXISTING`"),
     "the dedicated PR-35 session reference and `session_disposition: NEW_DEDICATED` (`RETAIN_EXISTING` on re-entry to that PR-35 session)"),
    ("X20", re.compile(r"PR-30 and PR-35 are same-session phases of one PR work unit and original Proceed\."),
     "PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions, under one original Proceed."),
    ("X21", re.compile(r"Preserve PR-30/PR-35 as one PR work unit, dedicated session, vehicle,"),
     "Preserve PR-30/PR-35 as two phases of one PR work unit, run in two dedicated sessions, with one vehicle,"),
    ("X22", re.compile(r"hands the same dedicated PR-development session, ([^.\n]*?directly to PR-35 — Resolve PR Reviews and Reach Merge Readiness)\."),
     r"hands the \1, which runs in its own dedicated session."),
    ("X23", re.compile(r"\bone dedicated PR-development session(, Product Owner PR Proceed and manual-merge boundaries, PR-30/PR-35 phase ownership)"),
     r"the PR-30 and PR-35 phases' two dedicated sessions\1"),
    ("X24", re.compile(r"^(#{1,6} )PR-35 SAME-SESSION REVIEW AND READINESS PHASE\s*$", re.M), r"\1PR-35 REVIEW AND READINESS PHASE IN ITS OWN DEDICATED SESSION"),
    ("X25", re.compile(r"the exact PR-30 result; one continuing PR-development session;"),
     "the exact PR-30 result; PR-35's own dedicated session, entered from PR-30's handoff;"),
    ("X26", re.compile(r"and hand the same dedicated PR-development session to PR-35\."), "and hand off to " + OWN35 + "."),
    ("X27", re.compile(r"the dedicated PR session identity\b"), "the PR-30 and PR-35 session identities"),
    ("X28", re.compile(r"\bdedicated PR session and whole-change IA context"), "PR-30 and PR-35 sessions and whole-change IA context"),
    ("X29a", re.compile(r"\bone PR session per planned PR work unit(?=\.)"),
     "one planned PR work unit run in two dedicated sessions, PR-30's and PR-35's"),
    ("X29", re.compile(r"\bone PR session per planned PR work unit"),
     "one planned PR work unit run in two dedicated sessions, PR-30's and PR-35's,"),
    ("X30", re.compile(r"(PR-35[^\n]*?) in that same session/open PR\."),
     r"\1 in the recorded phase's own dedicated session and the same open PR."),
    ("X31", re.compile(r"preserving the same PR session when one exists"),
     "preserving the recorded phase's own dedicated session when one exists"),
]


def converge(b):
    text = b.text()
    for cid, rx, rep in CONVERGE:
        if rep == "RS40-ROLE":
            rep = T["RS40-ROLE"].replace("\\", "\\\\")
        elif rep == "PR35-ROLE-1":
            rep = T["PR35-ROLE"].split("; you continue its existing pull request.")[0] + "; you continue its existing pull request."
        text, n = rx.subn(rep, text)
        if n:
            b.hit("CONV-" + cid, n)
    b.lines = text.split("\n")


REGISTRY = "/home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md"


def apply(bodies, reg_path=REGISTRY):
    """{id: body} -> ({id: edited body}, {id: report}). Pure, in memory."""
    nph, outputs = nph_from_registry(reg_path)
    assert nph == set(outputs) - NO_HANDOFF and len(nph) == 53, "NPH53 selector disagrees with the registry"
    out, report = {}, {}
    for pid in sorted(bodies):
        b = Body(pid, bodies[pid])
        s42(b)
        if pid in STEP3 | STEP3_EXTRA:
            sub_all(b, "S03", CONTROL_NOTION_SENTENCE, T["C-NOTION"])
        if pid == "QA-10":
            sub_all(b, "S04", STEP4_OLD, T["STEP4"], expected=6)
        if pid in STEP5:
            sub_all(b, "S05", STEP5_OLD, "")
        if pid in {"PR-30", "PR-35", "RS-40"} or CONTINUITY_SENTENCE.search(b.text()):
            s32(b)
        converge(b)
        if pid == "PR-40":
            c4r(b)
            sub_all(b, "W4", W4_OLD, T["W4"])
        if pid == "PR-20":
            c4e(b)
        if pid == "PR-30":
            if PR30_RETURN_CONTEXT.search(b.text()):
                sub_all(b, "C4P", PR30_RETURN_CONTEXT, T["C-PR30-ENTRY"])
            else:
                b.note("C4P: NOT_APPLICABLE (settled): PR-30 has no PR-40 return context, so C-PR30-ENTRY is not placed")
        if PROCEED_SENTENCE.search(b.text()):
            sub_all(b, "C4Q", PROCEED_SENTENCE, T["C-PROCEED"])
        if pid in {"PR-30", "PR-35"}:
            s13p(b)
        if pid in {"PR-35", "RS-40"}:
            s37(b)
            s39(b)
        if pid in LAT10:
            s22(b)
        if pid in nph:
            s08_s20(b, outputs.get(pid, []))
            i = s13_s18(b)
            if i is not None:
                s18_ctop(b, i)
            else:
                b.miss("S18/CTOP", "not placed because the handoff paragraph was not found")
        elif pid == "PR-50":
            ctop_pr50(b)
        out[pid] = b.text()
        b.report["placed_once"] = placement_counts(pid, out[pid], nph)
        report[pid] = b.report
    return out, report


def placement_counts(pid, text, nph):
    """How many times each canonical text that this body should carry occurs in the edited body."""
    want = []
    if pid in nph:
        want += ["C-ART", "C-HANDOFF", "C-TOP", "ASK-VARIANT" if pid in ASK_BODIES else "C-PLACE"]
    if pid == "PR-50":
        want.append("C-TOP")
    if pid in STEP3 | STEP3_EXTRA:
        want.append("C-NOTION")
    if pid in DEC3:
        want += ["C-DEC", "C-SESSION"]
    if pid in LAT10:
        want.append("C-LAT")
    if pid in {"PR-35", "RS-40"}:
        want += ["C-SUB", "C-DISPATCH"]
    if pid == "PR-40":
        want += ["C-REPLAN", "W4"]
    if pid == "PR-20":
        want.append("C-PR20-ENTRY")
    return {k: text.count(T[k]) for k in want}


def main():
    reg_path = sys.argv[sys.argv.index("--registry") + 1] if "--registry" in sys.argv else REGISTRY
    out, report = apply(json.load(sys.stdin), reg_path)
    json.dump(out, sys.stdout, ensure_ascii=False)
    json.dump(report, sys.stderr, indent=1, ensure_ascii=False)
    sys.stderr.write("\n")


if __name__ == "__main__":
    main()
