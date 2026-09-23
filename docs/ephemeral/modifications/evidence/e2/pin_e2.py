"""E2 pins, in the §5.11 order: (graph and contract already final) -> profile -> literals -> fixtures ->
SKILL_TREE_SHA256 last. Scratch copy only.

usage: PYTHONDONTWRITEBYTECODE=1 python3 pin_e2.py <skills-root>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
FVD, CFD = root / "flowmaster-validate", root / "change-flow"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
HIST_ORACLE = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
HIST_MAP = "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"
MATRIX_P = FVD / "references/r1-successor-source-20260923.md"
ORACLE_P = FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json"
MAP_P = CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
GRAPH_P = FVD / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json"
CONTRACT_P = FVD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
PROFILE_P = FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"
FIXTURE_P = FVD / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json"
assert GRAPH_P.read_bytes() == (CFD / "references" / GRAPH_P.name).read_bytes()
assert CONTRACT_P.read_bytes() == (CFD / "references" / CONTRACT_P.name).read_bytes()
MATRIX, SUCC_ORACLE, SUCC_MAP = sha(MATRIX_P), sha(ORACLE_P), sha(MAP_P)
GRAPH_SHA, GRAPH_BYTES = sha(GRAPH_P), len(GRAPH_P.read_bytes())
CONTRACT_SHA, CONTRACT_BYTES = sha(CONTRACT_P), len(CONTRACT_P.read_bytes())
assert json.loads(ORACLE_P.read_bytes())["authority"]["successor_source_matrix_sha256"] == MATRIX
assert json.loads(GRAPH_P.read_bytes())["protected_identities"]["r1_oracle_sha256"] == SUCC_ORACLE
assert json.loads(CONTRACT_P.read_bytes())["protected_identities"]["r1_oracle_sha256"] == SUCC_ORACLE
assert json.loads(CONTRACT_P.read_bytes())["source_snapshot"]["frozen_candidate_graph"]["sha256"] == GRAPH_SHA


def edit(path, pairs, count=1):
    s = path.read_text(encoding="utf-8")
    for old, new in pairs:
        n = s.count(old)
        assert n == count if isinstance(count, int) else n >= 1, (path, old[:100], n)
        s = s.replace(old, new)
    path.write_text(s, encoding="utf-8")


def ser_profile(obj):
    return (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def write_profile(fixture_sha=None):
    raw = PROFILE_P.read_bytes()
    prof = json.loads(raw)
    assert ser_profile(prof) == raw, "profile serialisation does not round-trip"
    prof["candidate_contract"].update(sha256=CONTRACT_SHA, byte_count=CONTRACT_BYTES)
    prof["frozen_graph"].update(sha256=GRAPH_SHA, byte_count=GRAPH_BYTES, edge_count=229)
    prof["installed_skill_revisions"] = {"change-flow": "3.3.0", "glow-hde-pr-development": "1.3.0"}
    prof["protected_identities"].update(r1_oracle_sha256=SUCC_ORACLE, r1_runtime_map_sha256=SUCC_MAP)
    prof["validator_revision"] = "3.3.0"
    if fixture_sha:
        prof["fixtures"].update(sha256=fixture_sha, count=37)
    PROFILE_P.write_bytes(ser_profile(prof))


# --- 6. Profile (graph, contract and R1 pins).
write_profile()

# --- 7. Literals.
FV = FVD / "scripts/validate_gcfpe_20260914.py"
fv = FV.read_text(encoding="utf-8")
assert fv.count(HIST_ORACLE) == 3 and fv.count(HIST_MAP) == 2
fv = fv.replace(HIST_ORACLE, SUCC_ORACLE).replace(HIST_MAP, SUCC_MAP)
FV.write_text(fv, encoding="utf-8")
edit(FV, [
    ('EXPECTED_FROZEN_GRAPH_SHA256 = "90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223"\nEXPECTED_FROZEN_GRAPH_BYTES = 569835\n'
     'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b"\nEXPECTED_CANDIDATE_CONTRACT_BYTES = 606657\n',
     f'EXPECTED_FROZEN_GRAPH_SHA256 = "{GRAPH_SHA}"\nEXPECTED_FROZEN_GRAPH_BYTES = {GRAPH_BYTES}\n'
     f'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "{CONTRACT_SHA}"\nEXPECTED_CANDIDATE_CONTRACT_BYTES = {CONTRACT_BYTES}\n'),
])
VF = FVD / "scripts/validate_flowmaster.py"
edit(VF, [
    ('EXPECTED_ORACLE_SHA256 = (\n    "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"\n)',
     f'EXPECTED_ORACLE_SHA256 = (\n    "{SUCC_ORACLE}"\n)'),
    ('EXPECTED_CHANGE_RUNTIME_MAP_SHA256 = (\n    "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e"\n)',
     f'EXPECTED_CHANGE_RUNTIME_MAP_SHA256 = (\n    "{SUCC_MAP}"\n)'),
])
edit(FVD / "scripts/validate_gcfpe_current.py", [('EXPECTED_INSTALLED_RUNTIME_MAP_SHA256 = "<SUCC_MAP>"', f'EXPECTED_INSTALLED_RUNTIME_MAP_SHA256 = "{SUCC_MAP}"')])
edit(CFD / "SKILL.md", [("SHA-256 `<SUCC_MAP>`", f"SHA-256 `{SUCC_MAP}`")])
edit(CFD / "scripts/validate_gcfpe_20260914.py", [
    ('EXPECTED_GRAPH_SHA = "90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223"', f'EXPECTED_GRAPH_SHA = "{GRAPH_SHA}"'),
])
edit(FVD / "SKILL.md", [
    ("R1_ORACLE_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1", "R1_ORACLE_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"),
    (f"R1_ORACLE_SHA256: {HIST_ORACLE}", f"R1_ORACLE_SHA256: {SUCC_ORACLE}"),
    ("The Change oracle is the bundled file references/glow-hde-canonical-change-flow-r1.json. It pins:",
     "The Change oracle is the bundled file references/glow-hde-canonical-change-flow-r1-20260923.json. It pins:"),
    (f"- projection SHA-256 {HIST_ORACLE};\n",
     f"- projection SHA-256 {SUCC_ORACLE};\n"
     f"- the successor source matrix references/r1-successor-source-20260923.md, SHA-256 {MATRIX}, which records the three successor rows GCF-14, GCF-17 and GCF-17.LINEAGE;\n"
     f"- the kept historical oracle references/glow-hde-canonical-change-flow-r1.json, SHA-256 {HIST_ORACLE}, whose 43 rows outside the successor set the successor keeps unchanged;\n"),
])

# --- 8. Fixtures pin (scenarios.json is final after apply_skill_edits.py).
FIX_SHA = sha(FIXTURE_P)
edit(FV, [('EXPECTED_FIXTURE_SHA256 = "a1a730623e5385a6214a6f3e18b8cef56acd0d227028b2236e56d586d822fa14"', f'EXPECTED_FIXTURE_SHA256 = "{FIX_SHA}"')])
write_profile(FIX_SHA)

# --- 9. SKILL_TREE_SHA256, last.
sys.path.insert(0, str(FVD / "scripts"))
from validate_gcfpe_20260914 import skill_tree_digest  # noqa: E402
md = FVD / "SKILL.md"
t = md.read_text(encoding="utf-8")
d = skill_tree_digest(FVD)
t2, n = re.subn(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + d, t)
assert n == 1
md.write_text(t2, encoding="utf-8")
assert skill_tree_digest(FVD) == d
print(json.dumps({"MATRIX": MATRIX, "SUCC_ORACLE": SUCC_ORACLE, "SUCC_MAP": SUCC_MAP,
                  "graph": [GRAPH_BYTES, GRAPH_SHA], "contract": [CONTRACT_BYTES, CONTRACT_SHA],
                  "fixtures_sha256": FIX_SHA, "profile_sha256": sha(PROFILE_P), "SKILL_TREE_SHA256": d}, indent=1))
