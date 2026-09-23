"""Pins after the round-a3 hardening, in the §5.11 order. H5 changes one contract-only value, so the contract's
sha256 and byte count move (profile candidate_contract, EXPECTED_CANDIDATE_CONTRACT_SHA256/BYTES). Nothing else
pinned moves: the matrix, successor oracle, successor map, graph and fixtures keep their bytes, and the contract's
own pins (r1_oracle_sha256, frozen_candidate_graph) are unchanged. SKILL_TREE_SHA256 is re-stamped last.

usage: PYTHONDONTWRITEBYTECODE=1 python3 pin_repairs_a3.py <skills-root>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
root = Path(sys.argv[1])
FVD, CFD = root / "flowmaster-validate", root / "change-flow"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
OLD_C, OLD_CB = "7a7fd0285730622217cc2e2d117552a002f57f9e391eac1c3d94b553fabbb675", 613162
KEEP = {"MATRIX": "8b443eb17180f85e8d615ba56ed6e1d1d78802fcd1a49aa3be3b5dd638bc4d04",
        "SUCC_ORACLE": "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52",
        "SUCC_MAP": "aa6ed8e34363b77e08e8467d9f31b4dc795c2c9fa2c2c3c7ed1cea6cf4202ee4",
        "GRAPH": "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d",
        "FIXTURES": "c433aa09d63b4c8c42891d03086096a771f1092d8c24c325f1706ab00932fe71"}
P = {"MATRIX": FVD / "references/r1-successor-source-20260923.md",
     "SUCC_ORACLE": FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json",
     "SUCC_MAP": CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json",
     "GRAPH": FVD / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
     "FIXTURES": FVD / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json"}
for k, p in P.items():
    assert sha(p) == KEEP[k], (k, sha(p))
CONTRACT_P = FVD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
assert CONTRACT_P.read_bytes() == (CFD / "references" / CONTRACT_P.name).read_bytes()
C, CB = sha(CONTRACT_P), len(CONTRACT_P.read_bytes())
c = json.loads(CONTRACT_P.read_bytes())
assert c["protected_identities"]["r1_oracle_sha256"] == KEEP["SUCC_ORACLE"]
assert c["source_snapshot"]["frozen_candidate_graph"]["sha256"] == KEEP["GRAPH"]

PROFILE_P = FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"
raw = PROFILE_P.read_bytes(); prof = json.loads(raw)
ser = lambda o: (json.dumps(o, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")  # noqa: E731
assert ser(prof) == raw and prof["candidate_contract"]["sha256"] == OLD_C and prof["candidate_contract"]["byte_count"] == OLD_CB
prof["candidate_contract"].update(sha256=C, byte_count=CB)
PROFILE_P.write_bytes(ser(prof))

FV = FVD / "scripts/validate_gcfpe_20260914.py"
s = FV.read_text(encoding="utf-8")
old = f'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "{OLD_C}"\nEXPECTED_CANDIDATE_CONTRACT_BYTES = {OLD_CB}\n'
assert s.count(old) == 1 and s.count(OLD_C) == 1
FV.write_text(s.replace(old, f'EXPECTED_CANDIDATE_CONTRACT_SHA256 = "{C}"\nEXPECTED_CANDIDATE_CONTRACT_BYTES = {CB}\n'), encoding="utf-8")
for p in root.rglob("*"):
    if p.is_file() and p.suffix in (".py", ".json", ".md"):
        assert OLD_C not in p.read_text(encoding="utf-8", errors="replace"), p

sys.path.insert(0, str(FVD / "scripts"))
from validate_gcfpe_20260914 import skill_tree_digest  # noqa: E402
md = FVD / "SKILL.md"; t = md.read_text(encoding="utf-8")
old_d = re.search(r"(?m)^SKILL_TREE_SHA256: ([0-9a-f]{64})$", t).group(1)
d = skill_tree_digest(FVD)
t2, n = re.subn(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + d, t); assert n == 1
md.write_text(t2, encoding="utf-8"); assert skill_tree_digest(FVD) == d
print(json.dumps({"contract": {"old": [OLD_C, OLD_CB], "new": [C, CB]}, "profile_sha256": sha(PROFILE_P),
                  "SKILL_TREE_SHA256": {"old": old_d, "new": d}}, indent=1))
