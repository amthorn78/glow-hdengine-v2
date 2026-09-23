#!/usr/bin/env python3
"""Scratch simulation of the amendment's exact routing changes. Copies docs/graph/parts to a
scratch dir, applies the transforms, builds with graph_parts.py, and reports the routing-surface
digest/rows plus a readable diff of every changed route row. Writes only under the scratch dir."""
import copy, json, os, shutil, subprocess, sys

sys.dont_write_bytecode = True
REPO = "/home/user/glow-hdengine-v2"
SK = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
W = "/tmp/claude-0/v2work/routesim"
GP = SK + "/glow-graph-contract/scripts/graph_parts.py"
FVS = W + "/fvscripts"
shutil.rmtree(W, ignore_errors=True)
os.makedirs(W)
shutil.copytree(SK + "/flowmaster-validate/scripts", FVS)
sys.path.insert(0, FVS)
import validate_gcfpe_20260914 as V  # noqa: E402

MAT = "(D23-C)"
CHANGES = {
    # PART-07: 'material' means a change to the Epic-level commitment
    ("PR-10", "material_boundary"): f"a material change to the Epic-level commitment {MAT} is substantiated",
    ("PR-20", "material_boundary"): f"the planning result substantiates a material change to the Epic-level commitment {MAT}",
    ("PR-40", "reject_material_boundary_proposal"): f"a substantiated material change to the Epic-level commitment {MAT} requires a new bounded rescope proposal",
    ("DOC-10", "material_boundary"): f"repository evidence proves a complete bounded material change to the Epic-level commitment {MAT}",
    # PART-09: PR-35 runs in its own dedicated session
    ("PR-30", "pr_candidate_published"): "one complete PR-35 handoff to the dedicated PR-35 session for the same work unit and pull request",
    ("RS-40", "recovery_pr30"): "recorded resumed phase is PR-30_POSTPUBLICATION; PR-30 session/vehicle re-entry",
    ("RS-40", "recovery_pr35"): "recorded resumed phase is PR-35; PR-35 session/vehicle re-entry",
    # PART-11: the manual-merge boundary stays as the fallback where no subscription exists
    ("PR-35", "merge_pending"): "conditional PR-40 invocation for Nathan, usable only after he manually merges and only where no MERGE_OBSERVED result was returned for this merge",
    ("RS-40", "merge_pending"): "recorded PR-35 phase result; historical pre-merge evidence; its conditional PR-40 invocation is usable only where no MERGE_OBSERVED result was returned for this merge",
    # CHILD: the PR-20 plan awaits the Proceed for that plan
    ("PR-20", "awaiting_po_proceed"): "one complete executable approved-scope plan awaits the Product Owner Proceed for that plan",
}
PROCEED = "the explicit Proceed for the exact approved per-PR plan; never a second Proceed for the same plan"
MERGE_ASSERT = "Nathan has manually merged the identified PR, no MERGE_OBSERVED result was returned for this merge, and he invokes the conditional PR-40 block"
NEW_PR35_EDGE_COND = "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
RS40_EDGE_COND = "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
REPLAN_COND = ("a precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new "
               "per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed")


def load(d):
    g = json.load(open(d + "/global.json"))
    p = {f[:-5]: json.load(open(d + "/prompts/" + f)) for f in os.listdir(d + "/prompts")}
    return g, p


def save(d, g, p):
    os.makedirs(d + "/prompts", exist_ok=True)
    open(d + "/global.json", "w").write(json.dumps(g, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    for k, v in p.items():
        open(d + "/prompts/" + k + ".json", "w").write(json.dumps(v, indent=2, sort_keys=True, ensure_ascii=False) + "\n")


def build(g, p, tag):
    d = W + "/parts_" + tag
    save(d, g, p)
    out = W + "/graph_" + tag + ".md"
    r = subprocess.run([sys.executable, GP, "build", d, out], capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if r.returncode:
        sys.exit(r.stderr)
    raw = open(out, encoding="utf-8").read().split("\n")
    s = next(i for i, l in enumerate(raw) if l.strip() == "```json")
    e = len(raw) - 1
    while raw[e].strip() != "```":
        e -= 1
    block = ("\n".join(raw[s + 1:e]) + "\n").encode()
    return json.loads(block), block, r.stdout.strip()


def apply(g, p):
    seen = set()
    for pid, part in p.items():
        for e in part["edges"]:
            for b in e["route_branches"]:
                k = (pid, b["branch_id"])
                if k in CHANGES:
                    b["condition"] = CHANGES[k]
                    seen.add(k)
    missing = set(CHANGES) - seen
    assert not missing, missing
    # CHILD: PR-40 reject goes to PR-20 for a re-plan; the edge is replaced in place (index kept)
    for e in p["PR-40"]["edges"]:
        if e["to"] == "PR-30":
            e["to"] = "PR-20"
            b = e["route_branches"][0]
            assert b["branch_id"] == "reject_existing_pr_owner"
            b["branch_id"] = "reject_replan"
            b["condition"] = REPLAN_COND
    o = p["PR-40"]["state_route_order"]
    o[o.index("reject_existing_pr_owner")] = "reject_replan"
    for e in g["_other_edges"]:
        if e["branch_id"] == "original_proceed":
            e["condition"] = PROCEED
        if e["branch_id"] == "manual_merge_then_lineage_review":
            e["condition"] = MERGE_ASSERT
    for b in g["boundary_transitions"]["NATHAN_PROCEED"]:
        b["condition"] = PROCEED
    for b in g["boundary_transitions"]["NATHAN_MANUAL_MERGE_ASSERTION"]:
        b["condition"] = MERGE_ASSERT
    # PART-11: new PR-35 result MERGE_OBSERVED and a prompt edge PR-35 -> PR-40 (a paste, like every edge)
    tmpl = copy.deepcopy(next(e for e in p["PR-35"]["edges"] if e["to"] == "RS-20"))
    tmpl["to"] = "PR-40"
    tmpl["state_predicates"] = ["MERGE_OBSERVED"]
    b = tmpl["route_branches"][0]
    b.update({"applicable_states": ["MERGE_OBSERVED"], "branch_id": "merge_observed",
              "condition": NEW_PR35_EDGE_COND, "state": "MERGE_OBSERVED"})
    p["PR-35"]["edges"].append(tmpl)
    o = p["PR-35"]["state_route_order"]
    o.insert(o.index("merge_pending") + 1, "merge_observed")
    p["PR-35"]["state_vocabularies"]["PR-35_RESULT"].insert(1, "MERGE_OBSERVED")
    p["PR-35"]["node"]["result_states"].insert(1, "MERGE_OBSERVED")
    # RS-40 resumes the PR-35 phase in the subscribed PR-35 session, so it mirrors PR-35
    t2 = copy.deepcopy(next(e for e in p["RS-40"]["edges"] if e["to"] == "RS-20"))
    t2["to"] = "PR-40"
    t2["state_predicates"] = ["MERGE_OBSERVED"]
    b2 = t2["route_branches"][0]
    b2.update({"applicable_states": ["MERGE_OBSERVED"], "branch_id": "merge_observed",
               "condition": RS40_EDGE_COND, "state": "MERGE_OBSERVED"})
    p["RS-40"]["edges"].append(t2)
    o = p["RS-40"]["state_route_order"]
    o.insert(o.index("merge_pending") + 1, "merge_observed")
    for k, v in p["RS-40"]["state_vocabularies"].items():
        if "MERGE_PENDING" in v:
            v.insert(v.index("MERGE_PENDING") + 1, "MERGE_OBSERVED")
    rs = p["RS-40"]["node"].get("result_states")
    if rs is not None and "MERGE_PENDING" in rs:
        rs.insert(rs.index("MERGE_PENDING") + 1, "MERGE_OBSERVED")


def rows(graph):
    out = []
    for e in graph["edges"]:
        for b in e.get("route_branches") or [e]:
            out.append(("EDGE", e["from"], b["branch_id"], e["to"], b.get("state") or b.get("origin_state"), b["condition"]))
    return out


g0, p0 = load(REPO + "/docs/graph/parts")
G0, B0, T0 = build(g0, p0, "base")
g1, p1 = copy.deepcopy(g0), copy.deepcopy(p0)
apply(g1, p1)
G1, B1, T1 = build(g1, p1, "new")
surf = lambda G: V.routing_surface({"route_edges": G["edges"], "state_routes": G["state_routes"]})
print("BASE", T0.replace("\n", " | "), surf(G0))
print("NEW ", T1.replace("\n", " | "), surf(G1))
r0, r1 = set(rows(G0)), set(rows(G1))
print("\nREMOVED route rows:")
for r in sorted(r0 - r1):
    print("  -", r)
print("ADDED route rows:")
for r in sorted(r1 - r0):
    print("  +", r)
sr0 = {k: json.dumps(v, sort_keys=True) for k, v in G0["state_routes"].items()}
sr1 = {k: json.dumps(v, sort_keys=True) for k, v in G1["state_routes"].items()}
print("state_routes keys changed:", sorted(k for k in set(sr0) | set(sr1) if sr0.get(k) != sr1.get(k)))
print("edge count", len(G0["edges"]), "->", len(G1["edges"]))
