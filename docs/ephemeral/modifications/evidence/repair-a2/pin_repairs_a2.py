"""Pins after the round-a2 repairs, in the §5.11 order. S1-S4 change no pinned artifact: the matrix, successor
oracle, successor map, graph, contract, profile and 091426.1 fixtures keep their E2 bytes, and no pin reads the
PR-skill, change-flow, relay, tw or amthor files. Steps 1-8 are therefore verified unchanged here (each E2 value is
re-measured and every pin site is re-read), and step 9, SKILL_TREE_SHA256, is re-stamped last. Identical to
pin_repairs_a1.py apart from this docstring.

usage: PYTHONDONTWRITEBYTECODE=1 python3 pin_repairs_a2.py <skills-root>
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
E2 = {  # the E2 values the round-a1 reviewers measured
    "MATRIX": "8b443eb17180f85e8d615ba56ed6e1d1d78802fcd1a49aa3be3b5dd638bc4d04",
    "SUCC_ORACLE": "ede635b1",
    "SUCC_MAP": "aa6ed8e3",
    "GRAPH": "ae2bd159",
    "CONTRACT": "7a7fd028",
    "FIXTURES": "c433aa09",
}
MATRIX_P = FVD / "references/r1-successor-source-20260923.md"
ORACLE_P = FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json"
MAP_P = CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
GRAPH_P = FVD / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json"
CONTRACT_P = FVD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
PROFILE_P = FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"
FIXTURE_P = FVD / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json"
m, o, mp, g, c, fx = map(sha, (MATRIX_P, ORACLE_P, MAP_P, GRAPH_P, CONTRACT_P, FIXTURE_P))
# 1-3 matrix, oracle, map
assert m == E2["MATRIX"] and o.startswith(E2["SUCC_ORACLE"]) and mp.startswith(E2["SUCC_MAP"]), (m, o, mp)
assert json.loads(ORACLE_P.read_bytes())["authority"]["successor_source_matrix_sha256"] == m
# 4-5 graph and contract, both copies
assert g.startswith(E2["GRAPH"]) and c.startswith(E2["CONTRACT"]), (g, c)
for p in (GRAPH_P, CONTRACT_P):
    assert p.read_bytes() == (CFD / "references" / p.name).read_bytes(), p.name
# 6 and 8 profile and fixtures
prof = json.loads(PROFILE_P.read_bytes())
assert prof["protected_identities"]["r1_oracle_sha256"] == o and prof["protected_identities"]["r1_runtime_map_sha256"] == mp
assert prof["candidate_contract"]["sha256"] == c and prof["frozen_graph"]["sha256"] == g
assert fx.startswith(E2["FIXTURES"]) and prof["fixtures"]["sha256"] == fx
# 7 literals
vf = (FVD / "scripts/validate_flowmaster.py").read_text(encoding="utf-8")
assert f'"{o}"' in vf and f'"{mp}"' in vf
v4 = (FVD / "scripts/validate_gcfpe_20260914.py").read_text(encoding="utf-8")
assert v4.count(o) == 3 and v4.count(mp) == 2 and f'EXPECTED_FIXTURE_SHA256 = "{fx}"' in v4
assert f'EXPECTED_INSTALLED_RUNTIME_MAP_SHA256 = "{mp}"' in (FVD / "scripts/validate_gcfpe_current.py").read_text(encoding="utf-8")
md_text = (FVD / "SKILL.md").read_text(encoding="utf-8")
assert f"R1_ORACLE_SHA256: {o}" in md_text and m in md_text
assert f"SHA-256 `{mp}`" in (CFD / "SKILL.md").read_text(encoding="utf-8")

# 9 SKILL_TREE_SHA256, last.
sys.path.insert(0, str(FVD / "scripts"))
from validate_gcfpe_20260914 import skill_tree_digest  # noqa: E402

md = FVD / "SKILL.md"
old = re.search(r"(?m)^SKILL_TREE_SHA256: ([0-9a-f]{64})$", md_text).group(1)
d = skill_tree_digest(FVD)
t2, n = re.subn(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + d, md_text)
assert n == 1
md.write_text(t2, encoding="utf-8")
assert skill_tree_digest(FVD) == d
print(json.dumps({"unchanged": {"MATRIX": m, "SUCC_ORACLE": o, "SUCC_MAP": mp, "graph": g, "contract": c,
                                "fixtures_sha256": fx, "profile_sha256": sha(PROFILE_P)},
                  "SKILL_TREE_SHA256": {"old": old, "new": d}}, indent=1))
