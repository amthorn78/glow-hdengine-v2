"""Repair round a4 (R1-R3) on the E2 scratch tree, after round a4: SFR-A4-1 SKILL_FIT_CONFIRMED, SFR-A4-2
SKILL_REPAIR_REQUIRED. Nathan approved the repair set as listed ("yes", 2026-09-23).

Applies, to validate_flowmaster.py only (pin_repairs_a4.py re-stamps SKILL_TREE_SHA256 afterwards):
  R1 (SFR-A4-2 F1, SFR-A4-1 A4-2)
        FMV-GCF-DISPATCH-001 no longer strips HTML comments. Round a3's stripping let a comment carrying a
        contradicting instruction sit inside the pinned passage, and an unclosed `<!--` hide the rest of a
        rendered file. Now every count reads the raw file, and any `<!--`, `-->` or `--!>` in a carrying file
        other than a whole-line `<!-- FLOWMASTER_* -->` section marker is a finding.
  R2 (SFR-A4-1 A4-1, SFR-A4-2 F2)
        the successor map's key-order check moves outside the dict-equality guard, where a pure reorder
        never reached it.
  R3 (SFR-A4-1 A4-3, SFR-A4-2 F3)
        FMV-ORACLE-022 also rejects <xmp>, <listing>, <textarea> and <plaintext>, and any indented code line
        (four spaces or a tab) outside the matrix's fenced blocks.
Every edit asserts its anchor count, so a second run or a moved tree fails instead of drifting.

usage: PYTHONDONTWRITEBYTECODE=1 python3 apply_repairs_a4.py <skills-root>
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
VF = root / "flowmaster-validate/scripts/validate_flowmaster.py"


def edit(path, pairs):
    s = path.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, (path.name, old[:90], n)
        s = s.replace(old, new)
    path.write_text(s, encoding="utf-8")


# The reviewed texts hold no comment other than whole-line FLOWMASTER markers, so R1 finds nothing today.
import re  # noqa: E402
MARKER = re.compile(r"(?m)^<!-- FLOWMASTER_[A-Z_]+ -->$")
for skill, rel in (("glow-hde-pr-development", "SKILL.md"), ("change-flow", "SKILL.md"),
                   ("session-relay-flowmaster", "SKILL.md"), ("tw-flowmaster", "SKILL.md"),
                   ("flowmaster-validate", "SKILL.md"), ("amthor-workspace-governance-audit", "SKILL.md"),
                   ("amthor-workspace-governance-audit", "references/interoperability-contracts.md"),
                   ("glow-hde-pr-development", "references/behavior-cases.md"),
                   ("amthor-workspace-governance-audit", "references/behavioral-fixtures.md")):
    residue = MARKER.sub("", (root / skill / rel).read_text(encoding="utf-8"))
    assert not any(t in residue for t in ("<!--", "-->", "--!>")), (skill, rel)

edit(VF, [
    # ---- R1
    ("# occurs once inside its own sentence context. HTML comments are removed before counting.\n",
     "# occurs once inside its own sentence context. Every count reads the raw file, and any HTML comment other\n"
     "# than a whole-line FLOWMASTER section marker is a finding: a comment can hide text from a rendered file\n"
     "# or carry a contradicting instruction inside the pinned passage.\n"),
    ('HTML_COMMENT_RE = re.compile(r"(?s)<!--.*?-->")\n',
     'DISPATCH_ALLOWED_COMMENT_RE = re.compile(r"(?m)^<!-- FLOWMASTER_[A-Z_]+ -->$")\n'),
    ('            text = HTML_COMMENT_RE.sub("", path.read_text(encoding="utf-8"))\n',
     '            text = path.read_text(encoding="utf-8")\n'),
    ("        problems = []\n        if text.count(DISPATCH_PREDICATE) != predicate_count:\n",
     "        problems = []\n"
     '        residue = DISPATCH_ALLOWED_COMMENT_RE.sub("", text)\n'
     '        if any(token in residue for token in ("<!--", "-->", "--!>")):\n'
     "            problems.append(\n"
     '                "an HTML comment other than a whole-line FLOWMASTER section marker is present; "\n'
     '                "it can hide or contradict the pinned text"\n'
     "            )\n"
     "        if text.count(DISPATCH_PREDICATE) != predicate_count:\n"),
    # ---- R2
    ("        if list(contract_map) != list(expected_projection):\n"
     "            results.append(\n"
     "                finding(\n"
     '                    "FMV-GCF-MAP-005",\n'
     "                    subject,\n"
     '                    f"runtime map top-level keys {list(contract_map)} are not the projection keys "\n'
     '                    f"{list(expected_projection)}",\n'
     "                )\n"
     "            )\n"
     "    rows = contract_map.get(",
     "    # Outside the guard above: dict equality ignores key order, so a pure reorder never enters it.\n"
     "    if contract_map and list(contract_map) != list(expected_projection):\n"
     "        results.append(\n"
     "            finding(\n"
     '                "FMV-GCF-MAP-005",\n'
     "                subject,\n"
     '                f"runtime map top-level keys {list(contract_map)} are not the projection keys "\n'
     '                f"{list(expected_projection)}, in that order",\n'
     "            )\n"
     "        )\n"
     "    rows = contract_map.get("),
    # ---- R3
    ('MATRIX_PRE_RE = re.compile(r"(?i)<pre[\\s>]")\n',
     'MATRIX_PRE_RE = re.compile(r"(?i)<(?:pre|xmp|listing|textarea|plaintext)[\\s>/]")\n'),
    ("def r1_row_digest(row: dict) -> str:\n",
     "def matrix_indented_code_lines(text: str) -> int:\n"
     '    """Non-blank lines outside fenced blocks that start with four spaces or a tab (an indented code block)."""\n'
     "\n"
     "    count, in_fence = 0, False\n"
     '    for line in text.split("\\n"):\n'
     '        stripped = MATRIX_CONTAINER_PREFIX_RE.sub("", line, count=1).lstrip()\n'
     '        if stripped.startswith(("```", "~~~")):\n'
     "            in_fence = not in_fence\n"
     "            continue\n"
     '        if not in_fence and line.strip() and (line.startswith("    ") or line.startswith("\\t")):\n'
     "            count += 1\n"
     "    return count\n"
     "\n"
     "\n"
     "def r1_row_digest(row: dict) -> str:\n"),
    ('                    "matrix contains an HTML <pre> block; only the three JSON blocks may render as code",\n'
     "                ))\n",
     '                    "matrix contains an HTML <pre>, <xmp>, <listing>, <textarea> or <plaintext> element; only "\n'
     '                    "the three JSON blocks may render as code",\n'
     "                ))\n"
     '            indented = matrix_indented_code_lines(matrix_bytes.decode("utf-8"))\n'
     "            if indented:\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-022", str(matrix_path),\n'
     '                    f"matrix has {indented} indented code lines outside the fenced blocks; only the three JSON "\n'
     '                    "blocks may render as code",\n'
     "                ))\n"),
])
print("R1-R3 applied to", root)
