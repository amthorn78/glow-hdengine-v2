"""Hardening round a3 (H1-H5) on the E2 scratch tree, after round a3 returned SKILL_FIT_CONFIRMED from SFR-A3-1 and
SFR-A3-2 with non-blocking findings. Nathan chose to fold them in now ("we may as well do it now", 2026-09-23).

Applies, to the skill files only (pin_repairs_a3.py moves the contract pins and SKILL_TREE_SHA256 afterwards):
  H1 (SFR-A3-2 A3-1, SFR-A3-1 F1)
        FMV-ORACLE-022 counts every code-fence line after stripping block-quote and list-item prefixes, and
        rejects an HTML <pre> block, so no fourth block can render in the matrix unchecked.
  H2 (SFR-A3-2 A3-2, SFR-A3-1 limit)
        FMV-GCF-DISPATCH-001 pins positions, not only counts: the whole C-DISPATCH passage (identical at the
        seven carrying sites, ending with the D23-E sentence) occurs exactly once, and every other fallback
        predicate and every fixture-text D23-E sentence is pinned by its own sentence context. HTML comments
        are removed before any count, so moving text into a comment is a deletion.
  H3 (SFR-A3-1 V1)
        FMV-GCF-DISPATCH-001 reports a missing carrying skill instead of skipping it.
  H4 (SFR-A3-1 V2)
        FMV-GCF-MAP-005 requires the successor map's top-level keys to be exactly the oracle projection's
        keys, in order.
  H5 (SFR-A3-2 A3-3, SFR-A3-1 limit)
        the contract-only value route_graph_semantics.pr40_entry gains the D23-E sentence, and
        validate_gcfpe_20260914.py expects it. route_graph_semantics is outside the graph and outside the
        routing surface, so the graph (ae2bd159...) and the routing surface (fecc319b.../284) do not change.
Every edit asserts its anchor count, so a second run or a moved tree fails instead of drifting.

usage: PYTHONDONTWRITEBYTECODE=1 python3 apply_repairs_a3.py <skills-root>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
REPO = Path(__file__).resolve().parents[5]
FVD, CFD = root / "flowmaster-validate", root / "change-flow"
VF = "flowmaster-validate/scripts/validate_flowmaster.py"


def edit(rel, pairs):
    p = root / rel
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, (rel, old[:90], n)
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")


def between(text, start, end):
    a = text.index(start)
    b = text.index(end, a) + len(end)
    assert text.count(start) == 1
    return text[a:b]


# ---- the approved sentence, read from the decision record (never re-authored) -------------------------
DR = (REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md").read_text(encoding="utf-8")
head = "### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)"
assert DR.count(head) == 1
sec = DR[DR.index(head):]
sec = sec[:sec.index("\n## ")]
ONCE = " ".join(line[2:].strip() for line in sec.split("\n") if line.startswith("> "))
assert ONCE == ("PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise "
                "the fallback block. Once either has been pasted, the other is void."), ONCE
PRED = "only where no `MERGE_OBSERVED` result was returned for this merge"

# ---- H2: derive the C-DISPATCH passage and the sentence contexts from the reviewed a3 texts ---------------
SITES = (  # (skill, file, predicate count, carries C-DISPATCH)
    ("glow-hde-pr-development", "SKILL.md", 2, True),
    ("change-flow", "SKILL.md", 4, True),
    ("session-relay-flowmaster", "SKILL.md", 1, True),
    ("tw-flowmaster", "SKILL.md", 1, True),
    ("flowmaster-validate", "SKILL.md", 2, True),
    ("amthor-workspace-governance-audit", "SKILL.md", 2, True),
    ("amthor-workspace-governance-audit", "references/interoperability-contracts.md", 2, True),
    ("glow-hde-pr-development", "references/behavior-cases.md", 2, False),
    ("amthor-workspace-governance-audit", "references/behavioral-fixtures.md", 2, False),
)
t0 = (root / "glow-hde-pr-development/SKILL.md").read_text(encoding="utf-8")
end = t0.index(ONCE) + len(ONCE)
BLOCK = t0[t0.rfind("At `MERGE_PENDING`, return control with the result", 0, end):end]
assert BLOCK.startswith("At `MERGE_PENDING`") and BLOCK.count(PRED) == 1 and BLOCK.endswith(ONCE), BLOCK[:80]
site_rows = []
for skill, rel, n, carries in SITES:
    raw = (root / skill / rel).read_text(encoding="utf-8")
    t = re.sub(r"(?s)<!--.*?-->", "", raw)  # as the check reads it; no guarded text sits in a comment
    assert all(raw.count(x) == t.count(x) for x in (PRED, ONCE, BLOCK)), (skill, rel)
    assert t.count(PRED) == n, (skill, rel)
    if carries:
        assert t.count(BLOCK) == 1, (skill, rel)
        t = t.replace(BLOCK, "\x00")
    contexts, i = [], 0
    while (i := t.find(PRED, i)) != -1:  # each remaining predicate, from a word boundary ~70 chars before
        start = t.rfind(" ", 0, max(0, i - 70)) + 1
        z = t.rfind("\x00", start, i)
        if z != -1:
            start = z + 2
        c = t[start:i + len(PRED) + 1]
        assert "\x00" not in c and t.count(c) == 1, (skill, rel, c)
        contexts.append(c)
        i += 1
    if not carries:  # the fixture texts' D23-E sentence, with the sentence before it
        i = t.index(ONCE)
        start = t.rfind(" ", 0, i - 40) + 1
        c = t[start:i + len(ONCE) + 1]
        assert t.count(c) == 1
        contexts.append(c)
    site_rows.append((skill, rel, n, carries, tuple(contexts)))

J = lambda v: json.dumps(v, ensure_ascii=False)  # noqa: E731
sites_src = "".join(
    f"    (\n        {J(s)}, {J(r)}, {n}, {c},\n        ("
    + "".join(f"\n            {J(x)}," for x in ctx)
    + ("\n        " if ctx else "")
    + "),\n    ),\n"
    for s, r, n, c, ctx in site_rows
)

vf = (root / VF).read_text(encoding="utf-8")
old_constants = between(vf, "# FMV-GCF-DISPATCH-001: C-DISPATCH and the D23-E sentence", "    (\"amthor-workspace-governance-audit\", \"references/behavioral-fixtures.md\", 2, False),\n)\n")
old_function = between(vf, "def dispatch_contract_findings(skills: dict[str, Path]) -> list[dict[str, str]]:\n", "            results.append(finding(\"FMV-GCF-DISPATCH-001\", str(path), \"; \".join(problems)))\n    return results\n")
new_constants = (
    "# FMV-GCF-DISPATCH-001: C-DISPATCH and the D23-E sentence (PR-40 is entered once per merge) at every\n"
    "# skill site that carries them. Positions are pinned, not only counts: the whole C-DISPATCH passage occurs\n"
    "# once at each carrying site, and every other fallback predicate, and the fixture texts' D23-E sentence,\n"
    "# occurs once inside its own sentence context. HTML comments are removed before counting.\n"
    f"DISPATCH_ONCE = {J(ONCE)}\n"
    f"DISPATCH_PREDICATE = {J(PRED)}\n"
    "DISPATCH_BLOCK = (\n"
    + "".join(f"    {J(BLOCK[k:k + 100])}\n" for k in range(0, len(BLOCK), 100))
    + ")\n"
    "DISPATCH_SITES = (  # (skill, file, fallback predicate count, carries C-DISPATCH, sentence contexts)\n"
    + sites_src
    + ")\n"
    'HTML_COMMENT_RE = re.compile(r"(?s)<!--.*?-->")\n'
)
new_function = (
    "def dispatch_contract_findings(skills: dict[str, Path]) -> list[dict[str, str]]:\n"
    '    """FMV-GCF-DISPATCH-001: C-DISPATCH, the fallback predicate and the D23-E sentence at every site."""\n'
    "\n"
    "    results: list[dict[str, str]] = []\n"
    "    for skill, relative, predicate_count, carries_dispatch, contexts in DISPATCH_SITES:\n"
    "        if skill not in skills:\n"
    "            results.append(finding(\n"
    '                "FMV-GCF-DISPATCH-001", skill,\n'
    '                f"skill {skill} carries C-DISPATCH or the D23-E sentence and is not active in the skills root",\n'
    "            ))\n"
    "            continue\n"
    "        path = skills[skill].parent / relative\n"
    "        try:\n"
    '            text = HTML_COMMENT_RE.sub("", path.read_text(encoding="utf-8"))\n'
    "        except (OSError, UnicodeError) as exc:\n"
    '            results.append(finding("FMV-GCF-DISPATCH-001", str(path), f"unreadable: {exc}"))\n'
    "            continue\n"
    "        problems = []\n"
    "        if text.count(DISPATCH_PREDICATE) != predicate_count:\n"
    "            problems.append(\n"
    '                f"the fallback predicate occurs {text.count(DISPATCH_PREDICATE)} times; expected {predicate_count}"\n'
    "            )\n"
    "        if carries_dispatch and text.count(DISPATCH_BLOCK) != 1:\n"
    '            problems.append(f"the C-DISPATCH passage occurs {text.count(DISPATCH_BLOCK)} times; expected 1")\n'
    "        if text.count(DISPATCH_ONCE) != 1:\n"
    '            problems.append(f"the D23-E once-per-merge sentence occurs {text.count(DISPATCH_ONCE)} times; expected 1")\n'
    "        for context in contexts:\n"
    "            if text.count(context) != 1:\n"
    '                problems.append(f"sentence context occurs {text.count(context)} times; expected 1: {context[:80]}")\n'
    "        if problems:\n"
    '            results.append(finding("FMV-GCF-DISPATCH-001", str(path), "; ".join(problems)))\n'
    "    return results\n"
)
vf = vf.replace(old_constants, new_constants).replace(old_function, new_function)
(root / VF).write_text(vf, encoding="utf-8")

# ---- H1: fence lines inside containers, and <pre> -------------------------------------------------------
edit(VF, [
    ('MATRIX_FENCE_RE = re.compile(r"(?m)^ {0,3}(?:`{3,}|~{3,})")\n',
     "# A fence line after any block-quote or list-item prefix still opens a rendered code block.\n"
     'MATRIX_CONTAINER_PREFIX_RE = re.compile(r"^(?:[ \\t]*(?:>|[-*+](?=[ \\t])|\\d{1,9}[.)](?=[ \\t])))+[ \\t]*")\n'
     'MATRIX_PRE_RE = re.compile(r"(?i)<pre[\\s>]")\n'),
    ("def r1_row_digest(row: dict) -> str:\n",
     "def matrix_fence_lines(text: str) -> int:\n"
     '    """Lines that open or close a code block once block-quote and list-item prefixes are removed."""\n'
     "\n"
     "    count = 0\n"
     "    for line in text.split(\"\\n\"):\n"
     '        stripped = MATRIX_CONTAINER_PREFIX_RE.sub("", line, count=1).lstrip()\n'
     '        if stripped.startswith(("```", "~~~")):\n'
     "            count += 1\n"
     "    return count\n"
     "\n"
     "\n"
     "def r1_row_digest(row: dict) -> str:\n"),
    ('            fences = len(MATRIX_FENCE_RE.findall(matrix_bytes.decode("utf-8")))\n',
     '            fences = matrix_fence_lines(matrix_bytes.decode("utf-8"))\n'
     '            if MATRIX_PRE_RE.search(matrix_bytes.decode("utf-8")):\n'
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-022", str(matrix_path),\n'
     '                    "matrix contains an HTML <pre> block; only the three JSON blocks may render as code",\n'
     "                ))\n"),
])

# ---- H4: the successor map's top-level keys ----------------------------------------------------------------
edit(VF, [(
    '                        f"projection field {key} differs from pinned R1 oracle",\n'
    "                    )\n"
    "                )\n",
    '                        f"projection field {key} differs from pinned R1 oracle",\n'
    "                    )\n"
    "                )\n"
    "        if list(contract_map) != list(expected_projection):\n"
    "            results.append(\n"
    "                finding(\n"
    '                    "FMV-GCF-MAP-005",\n'
    "                    subject,\n"
    '                    f"runtime map top-level keys {list(contract_map)} are not the projection keys "\n'
    '                    f"{list(expected_projection)}",\n'
    "                )\n"
    "            )\n",
)])

# ---- H5: route_graph_semantics.pr40_entry gains the D23-E sentence -----------------------------------------
W4 = ("PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session "
      "as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion "
      "that he manually merged it.")
W4_A3 = W4 + " " + ONCE
CNAME = "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
canon = lambda obj: (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")  # noqa: E731
cb = (FVD / CNAME).read_bytes()
assert cb == (CFD / CNAME).read_bytes()
assert hashlib.sha256(cb).hexdigest() == "7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675"
c = json.loads(cb)
assert canon(c) == cb and c["route_graph_semantics"]["pr40_entry"] == W4
c["route_graph_semantics"]["pr40_entry"] = W4_A3
ncb = canon(c)
before, after = json.loads(cb), json.loads(ncb)
after["route_graph_semantics"]["pr40_entry"] = W4
assert before == after  # the one value is the only change
for d in (FVD, CFD):
    (d / CNAME).write_bytes(ncb)
edit("flowmaster-validate/scripts/validate_gcfpe_20260914.py", [(
    f'    "pr40_entry": {J(W4)},\n',
    f'    "pr40_entry": {J(W4_A3)},\n',
)])
print("H1-H5 applied to", root, "; contract", hashlib.sha256(ncb).hexdigest(), len(ncb))
