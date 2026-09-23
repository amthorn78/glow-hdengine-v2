import json, re
S = "/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/v2/s6.md"
t = open(S, encoding="utf-8").read()
blocks = re.findall(r"^```json\n(.*?)\n```", t, re.S | re.M)
ok = 0
for b in blocks:
    json.loads(b); ok += 1
print("json blocks parsed:", ok, "of", len(blocks))
c = json.load(open("/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"))
after_tc = next(json.loads(b) for b in blocks if '"artifact_repository_paths_with_labels"' in b)
print("transition_contract keys before/after:", len(c["transition_contract"]), len(after_tc))
g = json.load(open("/home/user/glow-hdengine-v2/docs/graph/parts/global.json"))
gp = g["handoff_contract"]["prohibited"] + ["branch", "commit", "restated artifact content"]
print("graph prohibited today:", len(g["handoff_contract"]["prohibited"]), "; after subset:", set(gp) <= set(after_tc["prohibited_references"]), "; equal:", set(gp) == set(after_tc["prohibited_references"]), len(set(gp)))
rc = next(json.loads(b) for b in blocks if '"PR-20": {' in b and '"RS-30"' in b)
print("receivers today:", len(c["receiver_compatibility"]), "after:", len(rc))
print("unchanged four equal today:", all(rc[k] == c["receiver_compatibility"][k] for k in ["PR-30", "RS-20", "RS-30", "RS-40"]))
print("entries accepting PR_WORK_UNIT_LINEAGE_REVIEW:", [k for k, v in rc.items() if "PR_WORK_UNIT_LINEAGE_REVIEW" in json.dumps(v)])
rg = next(json.loads(b) for b in blocks if '"pr35_merge_pending_fallback"' in b)
print("route_graph unchanged keys equal today:", all(rg[k] == c["route_graph"][k] for k in c["route_graph"] if k != "ordinary_pr_work_unit"), len(rg))
print("semantics keys today:", sorted(c["route_graph_semantics"]))
