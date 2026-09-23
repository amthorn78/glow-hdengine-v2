"""Pins after the round-a4 repairs. R1-R3 edit validate_flowmaster.py only, so no pinned artifact moves: each is
re-measured against its round-a4 reviewed value, and SKILL_TREE_SHA256 is re-stamped last.

usage: PYTHONDONTWRITEBYTECODE=1 python3 pin_repairs_a4.py <skills-root>
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
KEEP = {  # the round-a4 reviewed values
    FVD / "references/r1-successor-source-20260923.md": "8b443eb17180f85e8d615ba56ed6e1d1d78802fcd1a49aa3be3b5dd638bc4d04",
    FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json": "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52",
    CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json": "aa6ed8e34363b77e08e8467d9f31b4dc795c2c9fa2c2c3c7ed1cea6cf4202ee4",
    FVD / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json": "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d",
    CFD / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json": "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d",
    FVD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json": "6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718",
    CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json": "6902924a2de7f3d348e75951fd5562632bcb690e3c4687c473695261b70f3718",
    FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json": "1ef9b56f1edc87c30d40f6923f8001614c52136f86fa91022e23ab30bd78950b",
    FVD / "fixtures/gcfpe-20260914.1-091426.1/scenarios.json": "c433aa09d63b4c8c42891d03086096a771f1092d8c24c325f1706ab00932fe71",
}
for p, v in KEEP.items():
    assert sha(p) == v, (p, sha(p))
sys.path.insert(0, str(FVD / "scripts"))
from validate_gcfpe_20260914 import skill_tree_digest  # noqa: E402
md = FVD / "SKILL.md"; t = md.read_text(encoding="utf-8")
old = re.search(r"(?m)^SKILL_TREE_SHA256: ([0-9a-f]{64})$", t).group(1)
d = skill_tree_digest(FVD)
t2, n = re.subn(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + d, t); assert n == 1
md.write_text(t2, encoding="utf-8"); assert skill_tree_digest(FVD) == d
print(json.dumps({"unchanged": len(KEEP), "SKILL_TREE_SHA256": {"old": old, "new": d}}, indent=1))
