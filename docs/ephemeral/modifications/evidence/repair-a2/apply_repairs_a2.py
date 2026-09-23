"""§10 review round a2 repairs S1-S4 on the E2 scratch tree (SKILL_REPAIR_REQUIRED from SFR-A2-1 and SFR-A2-2).
Nathan approved the repair set as listed ("yes, run the repair set as listed", 2026-09-23).

Applies, to the skill files only (pin_repairs_a2.py moves SKILL_TREE_SHA256 afterwards):
  S1 (SFR-A2-1 R2-1, SFR-A2-2 F1)
                validate_flowmaster.py: FMV-GCF-DISPATCH-001. At each of the seven C-DISPATCH sites the fallback
                predicate occurs its exact number of times, the fallback clause of C-DISPATCH once, and C-DISPATCH
                ends with the D23-E sentence once; at the two fixture texts the predicate occurs its exact
                number of times and the D23-E sentence once. amthor run_fixture_suite.py gains the same test for
                its own three files. The PR-skill literal for the sentence becomes its C-DISPATCH anchor form,
                so that the S4(d) copy in behavior-cases.md cannot satisfy it for SKILL.md.
  S2 (SFR-A2-1 R2-2, SFR-A2-2 advisory P4b)
                validate_flowmaster.py: FMV-ORACLE-021, the three approved successor row digests as constants.
  S3 (SFR-A2-2 F2)
                validate_flowmaster.py: duplicate JSON keys are rejected when the successor and historical
                oracles, the matrix blocks and the successor map are parsed. The runtime-map projection reads
                the oracle with .get(), so an unreadable oracle yields the suite's report rather than a
                KeyError traceback (a baseline defect that U3 exposed).
  S4 minor      (a) FMV-ORACLE-022: matrix blocks in oracle row order, no other code fence, block key order,
                    and every oracle row's key order equal to its historical row (SFR-A2-1 R2-3);
                (b) validate_gcfpe_20260914.py (flowmaster-validate): the exact value of
                    historical_non_executable_references (SFR-A2-1 R2-4, SFR-A2-2 advisory);
                (c) CONTRACT_REQUIRED for the relay: both "Outside a GCFPE main-ecosystem stage," sentences
                    (SFR-A2-1 R2-5);
                (d) the D23-E sentence added to behavior-cases.md "Observed merge" and to the amthor
                    behavioral-fixtures.md PR-40 entry fixture (SFR-A2-2 advisory).
Every edit asserts its anchor count, so a second run or a moved tree fails instead of drifting.

usage: PYTHONDONTWRITEBYTECODE=1 python3 apply_repairs_a2.py <skills-root>
"""
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
REPO = Path(__file__).resolve().parents[5]


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
PRED = "only where no `MERGE_OBSERVED` result was returned for this merge"
FALLBACK = "which is usable only after he merges and " + PRED
ANCHOR_ONCE = "No agent merges, and no session is created by an agent. " + ONCE

# ---- S4(d): the two fixture texts gain the D23-E sentence -------------------------------------------------
edit("glow-hde-pr-development/references/behavior-cases.md", [(
    "The conditional PR-40 block stays usable only after Nathan merges and " + PRED + ". No agent merges or creates a session.",
    "The conditional PR-40 block stays usable only after Nathan merges and " + PRED + ". " + ONCE
    + " No agent merges or creates a session.",
)])
edit("amthor-workspace-governance-audit/references/behavioral-fixtures.md", [(
    "Reject an agent merge, automatic dispatch, an agent-created session, and PR-40 entry before any merge.\n",
    "Reject an agent merge, automatic dispatch, an agent-created session, and PR-40 entry before any merge. "
    + ONCE + " Reject a second PR-40 entry for the same merge.\n",
)])

# The sites and their counts, measured after S4(d); the table is written into the validator as constants.
SITES = (  # (skill, relative path, predicate count, carries C-DISPATCH)
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
for skill, rel, n, carries in SITES:
    t = (root / skill / rel).read_text(encoding="utf-8")
    assert t.count(PRED) == n, (skill, rel, t.count(PRED))
    if carries:
        assert t.count(ANCHOR_ONCE) == 1 and t.count(FALLBACK) == 1, (skill, rel)
    else:
        assert t.count(ONCE) == 1, (skill, rel)

# ---- the approved successor row digests, read from the oracle the round-a2 reviewers measured ----------
FVD = root / "flowmaster-validate"
oracle = json.loads((FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json").read_bytes())
ROW_SHA = {r["id"]: r["source_row_sha256"] for r in oracle["runtime_rows"] if r["id"] in ("GCF-14", "GCF-17", "GCF-17.LINEAGE")}
assert ROW_SHA == {
    "GCF-14": "42db7a9e614ecf943f042a9c012112fd3934f12e504cd4b980f404735b9cfe6b",
    "GCF-17": "6774529046ba5050b2e62b8cf01b024766c5e99d343d0fcfdd32b0367fb99602",
    "GCF-17.LINEAGE": "73a133c18b13682cbc57d813b37caacda7ed15b183437515867166bcda70e83e",
}, ROW_SHA

VF = "flowmaster-validate/scripts/validate_flowmaster.py"
site_lines = "".join(f'    ("{s}", "{r}", {n}, {c}),\n' for s, r, n, c in SITES)
edit(VF, [
    # ---- constants: S2, S1, S4(a)
    ('SUCCESSOR_AUTHORITY = "D23-D, D23-F; Product Owner 2026-09-23"\n',
     'SUCCESSOR_AUTHORITY = "D23-D, D23-F; Product Owner 2026-09-23"\n'
     "# FMV-ORACLE-021: the approved successor row digests (Amendment 1, A1-1). A re-stamp moves every file pin,\n"
     "# never these, so an allowed field cannot take an unapproved value.\n"
     "SUCCESSOR_ROW_SHA256 = {\n"
     + "".join(f'    "{k}": "{v}",\n' for k, v in ROW_SHA.items())
     + "}\n"
     "# FMV-ORACLE-022: the matrix block key order (spec v2 §5.4).\n"
     'MATRIX_BLOCK_KEYS = (*R1_ROW_CONTENT_FIELDS, "supersedes_source_row_sha256")\n'
     'MATRIX_FENCE_RE = re.compile(r"(?m)^ {0,3}(?:`{3,}|~{3,})")\n'
     "# FMV-GCF-DISPATCH-001: C-DISPATCH and the D23-E sentence (PR-40 is entered once per merge) at every\n"
     "# skill site that carries them. Counts are exact, so deleting any one occurrence fails.\n"
     f"DISPATCH_ONCE = {json.dumps(ONCE, ensure_ascii=False)}\n"
     f"DISPATCH_PREDICATE = {json.dumps(PRED, ensure_ascii=False)}\n"
     'DISPATCH_FALLBACK = "which is usable only after he merges and " + DISPATCH_PREDICATE\n'
     'DISPATCH_ANCHOR_ONCE = "No agent merges, and no session is created by an agent. " + DISPATCH_ONCE\n'
     "DISPATCH_SITES = (  # (skill, file, fallback predicate count, carries C-DISPATCH)\n"
     + site_lines
     + ")\n"),
    # ---- S3: duplicate-key rejection
    ('def r1_row_digest(row: dict) -> str:\n',
     "def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:\n"
     "    result: dict[str, object] = {}\n"
     "    for key, value in pairs:\n"
     "        if key in result:\n"
     '            raise json.JSONDecodeError(f"duplicate key {key!r}", "", 0)\n'
     "        result[key] = value\n"
     "    return result\n"
     "\n"
     "\n"
     "def strict_json_loads(text: str) -> object:\n"
     '    """json.loads that rejects a duplicate key instead of keeping the last value."""\n'
     "\n"
     "    return json.loads(text, object_pairs_hook=_reject_duplicate_keys)\n"
     "\n"
     "\n"
     "def dispatch_contract_findings(skills: dict[str, Path]) -> list[dict[str, str]]:\n"
     '    """FMV-GCF-DISPATCH-001: the fallback predicate, C-DISPATCH and the D23-E sentence at every site."""\n'
     "\n"
     "    results: list[dict[str, str]] = []\n"
     "    for skill, relative, predicate_count, carries_dispatch in DISPATCH_SITES:\n"
     "        if skill not in skills:  # absence is FMV-SKILL-STRUCTURE-001's to report\n"
     "            continue\n"
     "        path = skills[skill].parent / relative\n"
     "        try:\n"
     '            text = path.read_text(encoding="utf-8")\n'
     "        except (OSError, UnicodeError) as exc:\n"
     '            results.append(finding("FMV-GCF-DISPATCH-001", str(path), f"unreadable: {exc}"))\n'
     "            continue\n"
     "        problems = []\n"
     "        if text.count(DISPATCH_PREDICATE) != predicate_count:\n"
     "            problems.append(\n"
     '                f"the fallback predicate occurs {text.count(DISPATCH_PREDICATE)} times; expected {predicate_count}"\n'
     "            )\n"
     "        if carries_dispatch:\n"
     "            if text.count(DISPATCH_FALLBACK) != 1:\n"
     '                problems.append(f"the C-DISPATCH fallback clause occurs {text.count(DISPATCH_FALLBACK)} times; expected 1")\n'
     "            if text.count(DISPATCH_ANCHOR_ONCE) != 1:\n"
     "                problems.append(\n"
     '                    f"C-DISPATCH ends with the D23-E once-per-merge sentence {text.count(DISPATCH_ANCHOR_ONCE)} "\n'
     '                    "times; expected 1"\n'
     "                )\n"
     "        elif text.count(DISPATCH_ONCE) != 1:\n"
     '            problems.append(f"the D23-E once-per-merge sentence occurs {text.count(DISPATCH_ONCE)} times; expected 1")\n'
     "        if problems:\n"
     '            results.append(finding("FMV-GCF-DISPATCH-001", str(path), "; ".join(problems)))\n'
     "    return results\n"
     "\n"
     "\n"
     "def r1_row_digest(row: dict) -> str:\n"),
    ('        oracle = json.loads(oracle_bytes.decode("utf-8"))\n',
     '        oracle = strict_json_loads(oracle_bytes.decode("utf-8"))\n'),
    ('            parsed = json.loads(history_bytes.decode("utf-8"))\n',
     '            parsed = strict_json_loads(history_bytes.decode("utf-8"))\n'),
    ('                parsed_blocks.append(json.loads(raw))\n',
     '                parsed_blocks.append(strict_json_loads(raw))\n'),
    ('        parsed_map = json.loads(map_bytes.decode("utf-8"))\n',
     '        parsed_map = strict_json_loads(map_bytes.decode("utf-8"))\n'),
    # An unreadable oracle (FMV-ORACLE-001) reaches this projection as {}; the baseline raised KeyError here and
    # the suite printed a traceback instead of its report. Found by U3; the baseline behaves the same.
    ('    expected_projection = {\n        key: oracle[key]\n        for key in ("profile_id", "authority", "coverage", "runtime_rows")\n',
     '    expected_projection = {\n        key: oracle.get(key)\n        for key in ("profile_id", "authority", "coverage", "runtime_rows")\n'),
    # ---- S4(a): matrix layout, after the shape check succeeds
    ("        else:\n            blocks = {block[\"id\"]: block for block in parsed_blocks}\n",
     "        else:\n            blocks = {block[\"id\"]: block for block in parsed_blocks}\n"
     "            # FMV-ORACLE-022 (spec v2 §5.4): blocks in oracle row order, their keys in the row order, and\n"
     "            # no code fence besides the three blocks.\n"
     '            oracle_order = [row.get("id") for row in rows if row.get("id") in SUCCESSOR_ROWS]\n'
     '            block_order = [block["id"] for block in parsed_blocks]\n'
     "            if block_order != oracle_order:\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-022", str(matrix_path),\n'
     '                    f"matrix blocks {block_order} are not in oracle row order {oracle_order}",\n'
     "                ))\n"
     "            for block in parsed_blocks:\n"
     "                if list(block) != list(MATRIX_BLOCK_KEYS):\n"
     "                    results.append(finding(\n"
     '                        "FMV-ORACLE-022", str(matrix_path),\n'
     "                        f\"row={block['id']}; matrix block keys {list(block)} are not in the order \"\n"
     '                        f"{list(MATRIX_BLOCK_KEYS)}",\n'
     "                    ))\n"
     '            fences = len(MATRIX_FENCE_RE.findall(matrix_bytes.decode("utf-8")))\n'
     "            if fences != 2 * len(SUCCESSOR_ROWS):\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-022", str(matrix_path),\n'
     '                    f"matrix has {fences} code-fence lines; exactly {2 * len(SUCCESSOR_ROWS)}, the three JSON "\n'
     '                    "blocks, are allowed",\n'
     "                ))\n"),
    # ---- S2: pinned row digests, in the per-row loop
    ("        if row.get(\"source_row_sha256\") != r1_row_digest(row):\n",
     "        if row.get(\"source_row_sha256\") != SUCCESSOR_ROW_SHA256[row_id]:\n"
     "            results.append(finding(\n"
     '                "FMV-ORACLE-021", str(oracle_path),\n'
     "                f\"row={row_id}; source_row_sha256 {row.get('source_row_sha256')} is not the approved \"\n"
     '                f"successor row digest {SUCCESSOR_ROW_SHA256[row_id]}",\n'
     "            ))\n"
     "        if row.get(\"source_row_sha256\") != r1_row_digest(row):\n"),
    # ---- S4(a): row key order, every row, against its historical row
    ("    if history_ok and history_rows:  # FMV-ORACLE-019: the successor rows' change set and positions\n",
     "    if history_ok and history_rows:  # FMV-ORACLE-022: every row keeps its historical key order\n"
     "        for row in rows:\n"
     '            old = history_by_id.get(row.get("id"))\n'
     "            if old is not None and list(row) != list(old):\n"
     "                results.append(finding(\n"
     '                    "FMV-ORACLE-022", str(oracle_path),\n'
     "                    f\"row={row.get('id')}; key order {list(row)} is not the historical key order {list(old)}\",\n"
     "                ))\n"
     "    if history_ok and history_rows:  # FMV-ORACLE-019: the successor rows' change set and positions\n"),
    # ---- S1: call the dispatch check
    ('        oracle, oracle_findings = load_change_oracle(\n            skills["flowmaster-validate"].parent\n        )\n',
     '        oracle, oracle_findings = load_change_oracle(\n            skills["flowmaster-validate"].parent\n        )\n'
     "        oracle_findings.extend(dispatch_contract_findings(skills))\n"),
    ('    """N1 and N3-N10 (FMV-ORACLE-008 to -016), the R1-literal tie check (FMV-ORACLE-017), the matrix\n'
     '    digest lines (FMV-ORACLE-018) and the successor change set (FMV-ORACLE-019 and -020)."""\n',
     '    """N1 and N3-N10 (FMV-ORACLE-008 to -016), the R1-literal tie check (FMV-ORACLE-017), the matrix\n'
     '    digest lines (FMV-ORACLE-018), the successor change set (FMV-ORACLE-019 and -020), the approved\n'
     '    row digests (FMV-ORACLE-021) and the layout (FMV-ORACLE-022)."""\n'),
])

# ---- S4(c): the relay's GCFPE scoping of SESSION_PROVISIONING_REQUIRED ------------------------------------
RELAY_1 = ("Outside a GCFPE main-ecosystem stage, when a required participant does not exist or cannot be confirmed "
           "reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster.")
RELAY_2 = ("This specialization cannot create a session. Outside a GCFPE main-ecosystem stage, when a required "
           "participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop")
relay = (root / "session-relay-flowmaster/SKILL.md").read_text(encoding="utf-8")
assert relay.count(RELAY_1) == 1 and relay.count(RELAY_2) == 1
edit(VF, [(
    '        "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",\n',
    '        "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",\n'
    f"        {json.dumps(RELAY_1, ensure_ascii=False)},\n"
    f"        {json.dumps(RELAY_2, ensure_ascii=False)},\n",
)])

# ---- S4(b): historical_non_executable_references, exact value ----------------------------------------------
contract = json.loads((FVD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
REFS = contract["historical_non_executable_references"]
assert REFS == [
    "integrated-qa-readiness-correction.json", "final-cycle-scan-extension.json",
    "alpha-feedback-correction.json", "strength-analyzer-middleware-correction.json",
    "epic-alpha-repair-correction.json", "epic-reengineering-correction.json",
    "glow-hde-canonical-change-flow-r1.json", "glow-hde-canonical-change-flow-r1-runtime-map.json"], REFS
edit("flowmaster-validate/scripts/validate_gcfpe_20260914.py", [
    ("def validate_contract(contract: dict[str, Any]) -> list[str]:\n",
     "# Contract revision 4.1.0 (spec v2 §6.3): the historical, non-executable references, exactly. The live\n"
     "# successor oracle and map must never be listed here.\n"
     "EXPECTED_HISTORICAL_NON_EXECUTABLE_REFERENCES = frozenset({\n"
     + "".join(f'    "{r}",\n' for r in REFS)
     + "})\n\n\n"
     "def validate_contract(contract: dict[str, Any]) -> list[str]:\n"),
    ('    }, "CONTRACT_IDENTITY")\n    status = contract.get("status")\n',
     '    }, "CONTRACT_IDENTITY")\n'
     '    references = contract.get("historical_non_executable_references")\n'
     "    if (\n"
     "        not isinstance(references, list)\n"
     "        or len(references) != len(set(map(str, references)))\n"
     "        or set(references) != EXPECTED_HISTORICAL_NON_EXECUTABLE_REFERENCES\n"
     "    ):\n"
     '        errors.append("HISTORICAL_NON_EXECUTABLE_REFERENCES")\n'
     '    status = contract.get("status")\n'),
])

# ---- S1: the PR-skill literal becomes the C-DISPATCH anchor form. After S4(d) behavior-cases.md carries the
# sentence too, and the validator checks SKILL.md and behavior-cases.md together, so the bare sentence would
# stop guarding SKILL.md (round-a1 regressions R-ONCE and R-ONCE-VOID would pass). The anchor form occurs only
# in SKILL.md.
edit("glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py", [(
    f'        "PR-40 once per merge": "{ONCE}",\n',
    f'        "PR-40 once per merge": "{ANCHOR_ONCE}",\n',
)])
assert (root / "glow-hde-pr-development/references/behavior-cases.md").read_text(encoding="utf-8").count(ANCHOR_ONCE) == 0

# ---- S1: the amthor suite guards its own three files --------------------------------------------------------
edit("amthor-workspace-governance-audit/scripts/run_fixture_suite.py", [
    ('        self.assertIn("exactly one fenced `text` `NEXT_PROMPT_HANDOFF`", interoperability)\n',
     '        self.assertIn("exactly one fenced `text` `NEXT_PROMPT_HANDOFF`", interoperability)\n'
     "\n"
     "    def test_pr40_once_per_merge_parity(self) -> None:\n"
     "        # D23-E: PR-40 is entered once per merge, and the fallback is usable only where no MERGE_OBSERVED\n"
     "        # result was returned for this merge. Exact counts, so deleting any one occurrence fails.\n"
     f"        once = {json.dumps(ONCE, ensure_ascii=False)}\n"
     f"        predicate = {json.dumps(PRED, ensure_ascii=False)}\n"
     '        dispatch = "No agent merges, and no session is created by an agent. " + once\n'
     '        fallback = "which is usable only after he merges and " + predicate\n'
     '        for relative in ("SKILL.md", "references/interoperability-contracts.md"):\n'
     '            text = (SKILL_ROOT / relative).read_text(encoding="utf-8")\n'
     "            self.assertEqual(text.count(dispatch), 1, relative)\n"
     "            self.assertEqual(text.count(fallback), 1, relative)\n"
     "            self.assertEqual(text.count(predicate), 2, relative)\n"
     '        fixtures = (SKILL_ROOT / "references/behavioral-fixtures.md").read_text(encoding="utf-8")\n'
     "        self.assertEqual(fixtures.count(once), 1)\n"
     "        self.assertEqual(fixtures.count(predicate), 2)\n"),
])
print("S1-S4 applied to", root)
