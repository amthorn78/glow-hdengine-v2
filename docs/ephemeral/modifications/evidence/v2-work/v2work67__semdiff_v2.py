import json, os, subprocess, sys, yaml
sys.path.insert(0, "/tmp/claude-0/v2work67/wga/scripts"); sys.path.insert(0, "/tmp/claude-0/v2work67")
from audit_workspace_governance import load_data
from guards_v2 import GUARDS
from apply_v2 import select
D = "/tmp/claude-0/v2work67"
old, new = load_data(D + "/registry.md"), load_data(D + "/registry.new.md")
print("top-level keys changed:", sorted(k for k in set(old) | set(new) if k != "prompts" and old.get(k) != new.get(k)))
O = {r["prompt_key"]: r for r in old["prompts"]}; N = {r["prompt_key"]: r for r in new["prompts"]}
print("row set and order kept:", list(O) == list(N))
ids = lambda l: [((x["value"], x.get("rule_id")) if isinstance(x, dict) else (x, None)) for x in l or []]
LISTS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")
RM = [("required_regex", ("Prompt [Vv]ersion: `?091426\\.1`?", "SRC-001")), ("required_regex", ("Ecosystem release: `?GCFPE-20260914\\.1`?", "INV-003"))]
exp = {k: [] for k in O}
for gid, kind, value, rid, sel, home in GUARDS:
    for k in select(old["prompts"], sel):
        exp[k].append((kind, (value, rid)))
bad, fields, order_bad = [], {}, []
for k in O:
    a, b = O[k], N[k]
    f = sorted(x for x in set(a) | set(b) if x != "audit_assertions" and a.get(x) != b.get(x))
    if f: fields[k] = f
    add = [(l, e) for l in LISTS for e in ids(b["audit_assertions"].get(l)) if e not in ids(a["audit_assertions"].get(l))]
    rm = [(l, e) for l in LISTS for e in ids(a["audit_assertions"].get(l)) if e not in ids(b["audit_assertions"].get(l))]
    if sorted(add) != sorted(exp[k]) or sorted(rm) != sorted(RM): bad.append(k)
    for l in LISTS:
        x, y = ids(a["audit_assertions"].get(l)), ids(b["audit_assertions"].get(l))
        if [e for e in y if e in x] != [e for e in x if e in y]: order_bad.append((k, l))
print("rows whose assertion diff != expected:", bad, "; kept-order violations:", order_bad)
print("non-assertion fields changed:", json.dumps(fields))
tot = lambda R: sum(len(r["audit_assertions"].get(l) or []) for r in R["prompts"] for l in LISTS)
print("assertions:", tot(old), "->", tot(new))
print("rows per guard:", {g[0]: sum(1 for r in new["prompts"] if (g[2], g[3]) in ids(r["audit_assertions"].get(g[1]))) for g in GUARDS})
print("inputs all str:", all(isinstance(x, str) for r in new["prompts"] for x in r.get("inputs") or []))
for k in ("PR-35", "RS-40"):
    print(k, "states:", [o.get("states") for o in N[k]["outputs"]])
r = subprocess.run([sys.executable, D + "/wga/scripts/validate_project_prompt_registry.py", D + "/registry.new.md"], capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
print("structure check exit", r.returncode, r.stdout.strip()[:200], r.stderr.strip()[:200])
