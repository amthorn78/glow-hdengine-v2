"""Canonical texts this Modification places, read verbatim from their repository homes (never re-authored).

- spec v2 §3 (docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md);
- the D23 successor "PR-40 is entered once per merge" in gcfpe.decision-record.md, bounded at the next heading
  (P-21: a later successor's lines are never read into it).
"""
import json
import re
from pathlib import Path

REPO = next(p for p in Path(__file__).resolve().parents if (p / ".git").exists())  # the repository root
_SPEC = (REPO / "docs/ephemeral/modifications/specs/EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md").read_text(encoding="utf-8")
S3 = _SPEC[_SPEC.index("## §3 Canonical wording, final"):_SPEC.index("## §4 Graph transforms")]


def block_after(marker, nth=0):
    assert S3.count(marker) == 1, marker
    i = S3.index(marker)
    for _ in range(nth + 1):
        j = S3.index("```text\n", i)
        k = S3.index("\n```", j + 8)
        val = S3[j + 8:k]
        i = k + 4
    return val


_DR = (REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md").read_text(encoding="utf-8")
_H = "### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)"
assert _DR.count(_H) == 1
_SEC = _DR[_DR.index(_H) + len(_H):]
_SEC = _SEC[:min(i for i in (_SEC.find("\n### "), _SEC.find("\n## ")) if i >= 0)]
_Q = [line[2:].strip() for line in _SEC.split("\n") if line.startswith("> ")]
assert len(_Q) == 2, _Q
ONCE = " ".join(_Q)

W4 = block_after("**PR-40 entry wording**")
CDISP = block_after("**C-DISPATCH** (PART-11), A1-5")
PRED = "only where no `MERGE_OBSERVED` result was returned for this merge"
assert PRED in CDISP
STEP16 = block_after("**Step 16**")
CLAT = block_after("**C-LAT** (PART-07")
CLAT_DECIDE = CLAT.split("\n\n")[1]
assert CLAT_DECIDE.startswith("**Decide it during work:**")
CREPLAN = block_after("**C-REPLAN**")
REPLAN_HEAD = "**PRECISE IN-SCOPE DEFECT → re-plan.**"
assert CREPLAN.startswith(REPLAN_HEAD)
_G = json.loads(S3[S3.index("```json\n") + 8:S3.index("\n```", S3.index("```json\n"))])
COND35 = _G["PR-35/merge_observed (new edge to PR-40)"]
COND40 = _G["RS-40/merge_observed (new edge to PR-40)"]
NAMES = ["C-NOTION", "C-ART", "C-HANDOFF", "C-PLACE", "C-DEC", "C-LAT", "C-SESSION", "C-SUB", "C-DISPATCH", "C-TOP",
         "C-REPLAN", "C-PROCEED", "C-PR20-ENTRY", "C-PR30-ENTRY", "W-4"]
_M = ["**C-NOTION** (PART-02)", "**C-ART** (PART-03)", "**C-HANDOFF** (PART-04", "**C-PLACE** (PART-05)",
      "**C-DEC** (PART-06", "**C-LAT** (PART-07", "**C-SESSION** (PART-09), amended", "**C-SUB** (PART-10), A1-5",
      "**C-DISPATCH** (PART-11), A1-5", "**C-TOP** (A1-8), new", "**C-REPLAN**", "**C-PROCEED** (the single-Proceed rule",
      "**C-PR20-ENTRY**", "**C-PR30-ENTRY**", "**PR-40 entry wording**"]
CANON = dict(zip(NAMES, [block_after(m) for m in _M]))
CANON["ONCE"] = ONCE


def collapse(x):
    """As Notion stores it: a blank line between paragraphs reads back as one line break."""
    return re.sub(r"\n{2,}", "\n", x)
