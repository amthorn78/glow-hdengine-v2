"""§10 review round a1 repairs R1-R5 on the E2 scratch tree (SKILL_REPAIR_REQUIRED from SFR-A1-1 and SFR-A1-2).

Applies, to the skill files only (no pin moves here; pin_repairs_a1.py moves SKILL_TREE_SHA256 afterwards):
  R1 (F1)       validate_flowmaster.py: FMV-ORACLE-018, the matrix `source_row_sha256:` lines.
  R2 (F2, V1)   validate_flowmaster.py: FMV-ORACLE-019 (successor-row change set and row positions) and
                FMV-ORACLE-020 (top-level oracle keys; the spec-listed token and authority changes, exactly).
  R3 (V2)       validate_glow_hde_pr_development.py: required literals for the two SKILL.md fallback sites.
  R4 (V3)       flowmaster-validate SKILL.md :157, :212, :382 and the FMV-GCF-CURRENT-FIXTURE-001 message.
  R5 (F3)       the D23 successor sentence "PR-40 is entered once per merge", appended to C-DISPATCH at every
                skill site that carries it, with a required literal in the PR-skill validator.
Every edit asserts its anchor count, so a second run or a moved tree fails instead of drifting.

usage: PYTHONDONTWRITEBYTECODE=1 python3 apply_repairs_a1.py <skills-root>
"""
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
REPO = Path(__file__).resolve().parents[5]
FVD = root / "flowmaster-validate"


def edit(rel, pairs):
    p = root / rel
    s = p.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        assert n == 1, (rel, old[:90], n)
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8")


# ---- the approved sentence, read from the decision record (never re-authored) -------------------------
DR = (REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md").read_text(encoding="utf-8")
head = "### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)"
assert DR.count(head) == 1
sec = DR[DR.index(head):]
sec = sec[:sec.index("\n## ")]
ONCE = " ".join(line[2:].strip() for line in sec.split("\n") if line.startswith("> "))
assert ONCE == ("PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise "
                "the fallback block. Once either has been pasted, the other is void."), ONCE

# ---- R5: C-DISPATCH gains the sentence at every skill site that carries C-DISPATCH ------------------------
ANCHOR = ("`PR-40` still verifies the merged state and landed lineage independently. "
          "No agent merges, and no session is created by an agent.")
C_DISPATCH_SITES = [
    "glow-hde-pr-development/SKILL.md",
    "change-flow/SKILL.md",
    "session-relay-flowmaster/SKILL.md",
    "tw-flowmaster/SKILL.md",
    "flowmaster-validate/SKILL.md",
    "amthor-workspace-governance-audit/SKILL.md",
    "amthor-workspace-governance-audit/references/interoperability-contracts.md",
]
for rel in C_DISPATCH_SITES:
    assert ONCE not in (root / rel).read_text(encoding="utf-8"), rel
    edit(rel, [(ANCHOR, ANCHOR + " " + ONCE)])

# ---- R3 and R5: PR-skill validator literals ---------------------------------------------------------------
edit("glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py", [(
    '        "no agent-created session": "no session is created by an agent",\n',
    '        "no agent-created session": "no session is created by an agent",\n'
    '        "merge fallback predicate": "which is usable only after he merges and only where no `MERGE_OBSERVED` '
    'result was returned for this merge",\n'
    '        "conditional PR-40 fallback predicate": "only after Nathan has manually merged the identified PR and '
    'only where no `MERGE_OBSERVED` result was returned for this merge",\n'
    f'        "PR-40 once per merge": "{ONCE}",\n',
)])

# ---- R4: the re-pointed current overlay (§12 S-5); history stays worded as history -----------------------
edit("flowmaster-validate/SKILL.md", [
    ("and 55-member frozen graph whose sole addition is PR-35 while the selected alias remains "
     "`GCFPE-20260913.1 / 091326.2 / 54` until promotion.",
     "and 55-member frozen graph whose sole addition is PR-35. The 54-member `GCFPE-20260913.1 / 091326.2` "
     "alias is kept as a historical record and is validated only when passed explicitly."),
    ("The suite always runs the selected-alias regression first, then additionally validates",
     "The suite always runs the current-overlay regression first, then additionally validates"),
    ("Candidate inputs never replace, redirect, or relax selected-alias validation, and the candidate validator "
     "proves the predecessor alias remains selected during staging.",
     "Candidate inputs never replace, redirect, or relax the current-overlay validation, which always runs the "
     "091426.1 contract and its fixtures first."),
])
edit("flowmaster-validate/scripts/validate_flowmaster.py", [
    ("    # The selected-production alias is always regression-tested first.  An\n"
     "    # explicit successor is additive evidence and never replaces this check.\n",
     "    # The current overlay (the 091426.1 contract, §12 S-5) is always regression-tested\n"
     "    # first.  An explicit successor is additive evidence and never replaces this check.\n"),
    ('                "selected-alias fixture suite failed",\n',
     '                "current-overlay fixture suite failed",\n'),
])

# ---- R1 and R2: validate_flowmaster.py successor-oracle checks -------------------------------------------
VF = "flowmaster-validate/scripts/validate_flowmaster.py"
edit(VF, [
    # constants
    ('    "r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS",\n}\nCANDIDATE_VALIDATOR_RELATIVE',
     '    "r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS",\n}\n'
     "# FMV-ORACLE-019: the A1-1 table (spec v2 §5.3). Each successor row may differ from its historical row\n"
     "# only in these fields, and it keeps its historical row position.\n"
     "SUCCESSOR_CHANGED_FIELDS = {\n"
     '    "GCF-14": ("consumes", "source_row_sha256"),\n'
     '    "GCF-17": ("name", "actor", "session", "failure_stop_condition", "source_row_sha256"),\n'
     '    "GCF-17.LINEAGE": ("next", "failure_stop_condition", "source_row_sha256"),\n'
     "}\n"
     "# FMV-ORACLE-020: every other top-level key is copied verbatim (spec v2 §5.3 step 3). These three change,\n"
     "# and only as §5.2, §5.3 step 2 and §5.5 list.\n"
     'SUCCESSOR_CHANGED_TOP_LEVEL = ("profile_id", "required_global_tokens", "authority")\n'
     'SUCCESSOR_AUTHORITY_KEYS = ("successor_source_matrix_sha256", "successor_rows", "successor_authority")\n'
     'SUCCESSOR_AUTHORITY = "D23-D, D23-F; Product Owner 2026-09-23"\n'
     "CANDIDATE_VALIDATOR_RELATIVE"),
    ('MATRIX_BLOCK_RE = re.compile(r"(?ms)^```json\\n(.*?)\\n```$")\n',
     'MATRIX_BLOCK_RE = re.compile(r"(?ms)^```json\\n(.*?)\\n```$")\n'
     'MATRIX_DIGEST_LINE_RE = re.compile(r"(?m)source_row_sha256: ([0-9a-f]{64})$")\n'
     'MATRIX_ANY_DIGEST_LINE_RE = re.compile(r"(?m)^source_row_sha256:")\n'),
    # docstring
    ('    """N1 and N3-N10 (FMV-ORACLE-008 to -016) and the R1-literal tie check (FMV-ORACLE-017)."""\n',
     '    """N1 and N3-N10 (FMV-ORACLE-008 to -016), the R1-literal tie check (FMV-ORACLE-017), the matrix\n'
     '    digest lines (FMV-ORACLE-018) and the successor change set (FMV-ORACLE-019 and -020)."""\n'),
    # history is trusted for field-level comparison only when its bytes are the pinned historical bytes
    ('    history: dict[str, object] = {}\n    history_path = skill_dir / HISTORICAL_ORACLE_RELATIVE\n',
     '    history: dict[str, object] = {}\n    history_ok = False\n'
     '    history_path = skill_dir / HISTORICAL_ORACLE_RELATIVE\n'),
    ('        if history_sha256 != HISTORICAL_ORACLE_SHA256:\n            results.append(finding(\n'
     '                "FMV-ORACLE-008", str(history_path),\n',
     '        history_ok = history_sha256 == HISTORICAL_ORACLE_SHA256\n'
     '        if not history_ok:\n            results.append(finding(\n'
     '                "FMV-ORACLE-008", str(history_path),\n'),
    # R1: FMV-ORACLE-018
    ('        else:\n            blocks = {block["id"]: block for block in parsed_blocks}\n',
     '        else:\n            blocks = {block["id"]: block for block in parsed_blocks}\n'
     "            # FMV-ORACLE-018 (spec v2 §12 Addendum, v2, §5): exactly one `source_row_sha256: <hex>` line\n"
     "            # directly after each JSON block, three in all, in block order, each equal to the oracle\n"
     "            # row's source_row_sha256.\n"
     '            matrix_text = matrix_bytes.decode("utf-8")\n'
     "            digest_lines = []\n"
     "            for match in MATRIX_BLOCK_RE.finditer(matrix_text):\n"
     "                following = MATRIX_DIGEST_LINE_RE.match(matrix_text, match.end() + 1)\n"
     "                digest_lines.append(following.group(1) if following else None)\n"
     "            line_count = len(MATRIX_ANY_DIGEST_LINE_RE.findall(matrix_text))\n"
     "            if line_count != len(SUCCESSOR_ROWS) or None in digest_lines:\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-018", str(matrix_path),\n'
     '                    f"matrix must carry exactly {len(SUCCESSOR_ROWS)} `source_row_sha256: <hex>` lines, one "\n'
     '                    f"directly after each JSON block; found {line_count} such lines, "\n'
     '                    f"{sum(line is not None for line in digest_lines)} directly after a block",\n'
     "                ))\n"
     "            else:\n"
     "                for block, line in zip(parsed_blocks, digest_lines):\n"
     '                    row_digest = (by_id.get(block["id"]) or {}).get("source_row_sha256")\n'
     "                    if line != row_digest:\n"
     "                        results.append(finding(\n"
     '                            "FMV-ORACLE-018", str(matrix_path),\n'
     '                            f"row={block[\'id\']}; matrix source_row_sha256 line {line} is not the oracle "\n'
     '                            f"row\'s source_row_sha256 {row_digest}",\n'
     "                        ))\n"),
    # R2: FMV-ORACLE-019 and -020, after N9 and before N10
    ('    for key, value in HISTORICAL_R1_AUTHORITY.items():  # N10\n',
     "    if history_ok and history_rows:  # FMV-ORACLE-019: the successor rows' change set and positions\n"
     "        ids = [row.get(\"id\") for row in rows]\n"
     "        history_ids = [row.get(\"id\") for row in history_rows]\n"
     "        position_findings = 0\n"
     "\n"
     "        def neighbours(sequence, row_id):  # the ids before and after; a moved row changes at least one\n"
     "            at = sequence.index(row_id)\n"
     "            return (sequence[at - 1] if at else None, sequence[at + 1] if at + 1 < len(sequence) else None)\n"
     "\n"
     "        for row_id, allowed in SUCCESSOR_CHANGED_FIELDS.items():\n"
     "            row, old = by_id.get(row_id), history_by_id.get(row_id)\n"
     "            if row is None or old is None:\n"
     "                continue\n"
     "            changed = sorted(\n"
     "                key for key in set(row) | set(old) if key not in allowed and row.get(key) != old.get(key)\n"
     "            )\n"
     "            if changed:\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-019", str(oracle_path),\n'
     '                    f"row={row_id}; fields outside the A1-1 change set differ from the historical R1 row: "\n'
     '                    f"{changed}; only {list(allowed)} may change",\n'
     "                ))\n"
     "            if neighbours(ids, row_id) != neighbours(history_ids, row_id):\n"
     "                position_findings += 1\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-019", str(oracle_path),\n'
     '                    f"row={row_id}; successor row is not at its historical position: neighbours "\n'
     '                    f"{neighbours(ids, row_id)}, historical {neighbours(history_ids, row_id)}",\n'
     "                ))\n"
     "        if ids != history_ids and not position_findings:\n"
     "            results.append(finding(\n"
     '                "FMV-ORACLE-019", str(oracle_path),\n'
     '                "runtime_rows ids are not the historical ids in the historical order",\n'
     "            ))\n"
     "    if history_ok and history:  # FMV-ORACLE-020: the top-level keys\n"
     "        if list(oracle) != list(history):\n"
     "            results.append(finding(\n"
     '                "FMV-ORACLE-020", str(oracle_path),\n'
     '                f"top-level keys {list(oracle)} are not the historical keys in the historical order "\n'
     '                f"{list(history)}",\n'
     "            ))\n"
     "        for key in dict.fromkeys(list(history) + list(oracle)):\n"
     '            if key == "runtime_rows" or key in SUCCESSOR_CHANGED_TOP_LEVEL:\n'
     "                continue\n"
     "            if oracle.get(key) != history.get(key):\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-020", str(oracle_path),\n'
     '                    f"top-level key {key} differs from the historical R1 oracle; it is copied verbatim",\n'
     "                ))\n"
     '        history_profile = history.get("profile_id")\n'
     '        history_tokens = history.get("required_global_tokens")\n'
     "        expected_tokens = (\n"
     "            [EXPECTED_ORACLE_PROFILE if token == history_profile else token for token in history_tokens]\n"
     "            if isinstance(history_tokens, list) else None\n"
     "        )\n"
     '        if oracle.get("required_global_tokens") != expected_tokens:\n'
     "            results.append(finding(\n"
     '                "FMV-ORACLE-020", str(oracle_path),\n'
     '                f"required_global_tokens must be the historical list with only the historical profile_id {history_profile} "\n'
     '                f"replaced in place by {EXPECTED_ORACLE_PROFILE}",\n'
     "            ))\n"
     '        history_authority = history.get("authority")\n'
     "        expected_keys = (\n"
     "            list(history_authority) + list(SUCCESSOR_AUTHORITY_KEYS) if isinstance(history_authority, dict) else None\n"
     "        )\n"
     "        if list(authority) != expected_keys:\n"
     "            results.append(finding(\n"
     '                "FMV-ORACLE-020", str(oracle_path),\n'
     '                f"authority keys {list(authority)} must be the historical keys followed by "\n'
     '                f"{list(SUCCESSOR_AUTHORITY_KEYS)}",\n'
     "            ))\n"
     '        if authority.get("successor_authority") != SUCCESSOR_AUTHORITY:\n'
     "            results.append(finding(\n"
     '                "FMV-ORACLE-020", str(oracle_path),\n'
     '                f"authority.successor_authority={authority.get(\'successor_authority\')!r}; "\n'
     '                f"expected {SUCCESSOR_AUTHORITY!r}",\n'
     "            ))\n"
     "    for key, value in HISTORICAL_R1_AUTHORITY.items():  # N10\n"),
])
print("R1-R5 applied to", root)
