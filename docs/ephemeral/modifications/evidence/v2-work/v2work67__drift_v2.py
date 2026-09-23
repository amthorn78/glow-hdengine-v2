import copy, json, os, sys
sys.path.insert(0, "/tmp/claude-0/v2work67/wga/scripts")
from audit_workspace_governance import load_data
D = "/tmp/claude-0/v2work67"
old, new = load_data(D + "/registry.md"), load_data(D + "/registry.new.md")
parts = lambda d: {f[:-5]: json.load(open(d + "/prompts/" + f)) for f in os.listdir(d + "/prompts")}
def drift(reg, P):
    out = []
    for r in reg["prompts"]:
        part = P[r["prompt_key"]]
        want = sorted({e["to"] for e in part["edges"] if e["to_kind"] == "prompt" and e["to"] != part["id"]})
        cons = {c for o in r["outputs"] for c in (o.get("consumers") or [])}
        st = {s for o in r["outputs"] for s in (o.get("states") or [])}
        if sorted(cons) != want or r["required_interfaces"] != want or st != set(part["node"]["result_states"]): out.append(r["prompt_key"])
    return out
P0, P1 = parts(D + "/parts_base"), parts(D + "/parts_new")
print("today's registry vs today's parts:", drift(old, P0))
print("edited registry vs simulated parts:", drift(new, P1))
print("unedited registry vs simulated parts:", drift(old, P1))
n = copy.deepcopy(new); {r["prompt_key"]: r for r in n["prompts"]}["PR-40"]["outputs"][0]["consumers"] = ["PR-10", "PR-30", "RS-10"]
print("PR-30 re-injected into PR-40 consumers:", drift(n, P1))
n = copy.deepcopy(new); {r["prompt_key"]: r for r in n["prompts"]}["RS-40"]["outputs"][0]["states"].remove("MERGE_OBSERVED")
print("MERGE_OBSERVED removed from RS-40 states:", drift(n, P1))
