"""The current recipe for the shipped 091426.1 contract (SFR-A4-1 A4-O1): regenerate_contract.py `generate`, which
still produces the E2 contract 7a7fd028..., followed by the round-a3 H5 step, which sets the contract-only value
route_graph_semantics.pr40_entry to the E2 value (regenerate_contract.W4) plus the D23-E sentence, read from the
decision record. regenerate_contract.py stays as committed in E2; this is its successor step, not an edit of it.

usage: PYTHONDONTWRITEBYTECODE=1 python3 contract_recipe.py <graph-md> <template-contract> <oracle-file> <out-contract>
       [--check <shipped-contract> ...]   exit 1 unless every named contract is byte-equal to the recipe's output
"""
import hashlib
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
EV = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[5]
spec = importlib.util.spec_from_file_location("regenerate_contract", EV / "regenerate_contract.py")
rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)

DR = (REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md").read_text(encoding="utf-8")
head = "### Successor, 2026-09-23 — PR-40 is entered once per merge (D23-E)"
assert DR.count(head) == 1
sec = DR[DR.index(head):]; sec = sec[:sec.index("\n## ")]
ONCE = " ".join(line[2:].strip() for line in sec.split("\n") if line.startswith("> "))

args = sys.argv[1:]
checks = args[args.index("--check") + 1:] if "--check" in args else []
graph_md, template, oracle, out = (args[:args.index("--check")] if checks else args)[:4]
with tempfile.TemporaryDirectory() as d:
    e2_out = Path(d) / "e2-contract.json"
    assert rc.generate(graph_md, template, oracle, [str(e2_out)]) in (0, None)
    e2 = e2_out.read_bytes()
print("E2 regenerator output", hashlib.sha256(e2).hexdigest(), len(e2))
canon = lambda obj: (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")  # noqa: E731
c = json.loads(e2)
assert canon(c) == e2 and c["route_graph_semantics"]["pr40_entry"] == rc.W4
c["route_graph_semantics"]["pr40_entry"] = rc.W4 + " " + ONCE
new = canon(c)
Path(out).write_bytes(new)
print("recipe output", hashlib.sha256(new).hexdigest(), len(new))
bad = [p for p in checks if Path(p).read_bytes() != new]
for p in checks:
    print(("EQUAL    " if p not in bad else "DIFFERENT"), p)
raise SystemExit(1 if bad else 0)
