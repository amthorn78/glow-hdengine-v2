#!/usr/bin/env python3
"""E1 graph transform (execution spec v2, §4; commit 1 = every §4 edit except G16).

Reuses the routing transform of route_sim_final.py (sha256 e0854a55..., the A1-7 authority) and the
non-routing edits of v2-work/v2work__nonrouting.py, applied in the §4.9 order:
  1. routing transform (G1-G4, P35-1..5, R40-1..7, P40-1..3, P20-1, P20-2, P30-1, P10-1, D10-1),
     built to scratch and checked against the A1-7 checkpoint and the V3 first table;
  2. non-routing edits (G5, G6, G8-G10, G14, G15, P35-6..10, R40-8), built to scratch and checked
     against the V3 second table;
  3. only then are the changed part files written into docs/graph/parts, with the §4.1 writer.
G16 (protected_identities.r1_oracle_sha256) is NOT touched: it is E2, commit 2.

Usage: PYTHONDONTWRITEBYTECODE=1 python3 e1_graph_transform.py <scratch-dir> [--write]
Without --write it only builds and checks in scratch. It never builds into the repository."""
import copy, hashlib, json, os, shutil, subprocess, sys

sys.dont_write_bytecode = True
REPO = "/home/user/glow-hdengine-v2"
PARTS = REPO + "/docs/graph/parts"
SK = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
GP = SK + "/glow-graph-contract/scripts/graph_parts.py"
W = os.path.abspath(sys.argv[1])
WRITE = "--write" in sys.argv[2:]
FVS = W + "/fvscripts"
shutil.rmtree(W, ignore_errors=True)
os.makedirs(W)
shutil.copytree(SK + "/flowmaster-validate/scripts", FVS)
sys.path.insert(0, FVS)
import validate_gcfpe_20260914 as V  # noqa: E402

# ---- routing transform: verbatim from route_sim_final.py ------------------------------------
MAT = "(D23-C)"
CHANGES = {
    ("PR-10", "material_boundary"): f"a material change to the Epic-level commitment {MAT} is substantiated",
    ("PR-20", "material_boundary"): f"the planning result substantiates a material change to the Epic-level commitment {MAT}",
    ("PR-40", "reject_material_boundary_proposal"): f"a substantiated material change to the Epic-level commitment {MAT} requires a new bounded rescope proposal",
    ("DOC-10", "material_boundary"): f"repository evidence proves a complete bounded material change to the Epic-level commitment {MAT}",
    ("PR-30", "pr_candidate_published"): "one complete PR-35 handoff to the dedicated PR-35 session for the same work unit and pull request",
    ("RS-40", "recovery_pr30"): "recorded resumed phase is PR-30_POSTPUBLICATION; PR-30 session/vehicle re-entry",
    ("RS-40", "recovery_pr35"): "recorded resumed phase is PR-35; PR-35 session/vehicle re-entry",
    ("PR-35", "merge_pending"): "conditional PR-40 invocation for Nathan, usable only after he manually merges and only where no MERGE_OBSERVED result was returned for this merge",
    ("RS-40", "merge_pending"): "recorded PR-35 phase result; historical pre-merge evidence; its conditional PR-40 invocation is usable only where no MERGE_OBSERVED result was returned for this merge",
    ("PR-20", "awaiting_po_proceed"): "one complete executable approved-scope plan awaits the Product Owner Proceed for that plan",
}
PROCEED = "the explicit Proceed for the exact approved per-PR plan; never a second Proceed for the same plan"
MERGE_ASSERT = "Nathan has manually merged the identified PR, no MERGE_OBSERVED result was returned for this merge, and he invokes the conditional PR-40 block"
NEW_PR35_EDGE_COND = "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
RS40_EDGE_COND = "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan"
REPLAN_COND = ("a precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new "
               "per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed")


def apply_routing(g, p):
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


# ---- non-routing edits: from v2work__nonrouting.py (spec §4.3, §4.4) ------------------------
PR35_ROLE = ("You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its "
             "existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan "
             "pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.")
RS40_ROLE = ("You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, "
             "the PR-35 session for PR_RETURN_PHASE PR-35.")


def apply_nonrouting(g, p):
    hc = g["handoff_contract"]  # G5, G6
    assert hc["required"][:2] == ["exact selected prompt full name/version/direct Notion URL", "receiving role and exact session"]
    hc["required"] = ["exact selected prompt full name/version/direct Notion URL", "receiving role and exact session",
                      "input artifact repository paths with one-line labels",
                      "pull request reference when the receiver continues an existing PR",
                      "minimum exceptional context only for a condition the artifacts do not record"]
    assert len(hc["prohibited"]) == 9
    hc["prohibited"] += ["branch", "commit", "restated artifact content"]
    pc = g["pr_continuity_contract"]  # G8-G10
    pc["shared_exactly_one"].remove("dedicated PR-development session")
    assert pc["adds"]["session"] == 0 and pc["adds"]["cross_session_route"] == 0
    pc["adds"]["session"] = 1
    pc["adds"]["cross_session_route"] = 1
    pm = g["post_merge_three_event_contract"]  # G14, G15
    assert pm["direct_PR35_to_PR40_automatic_edge"] is False and pm["agent_merge_authorized"] is False
    pm["event_2"] = {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted",
                     "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge",
                     "value": True}
    assert "observed_merge_edges" not in pm
    pm["observed_merge_edges"] = [{"from": f, "to": "PR-40", "branch_id": "merge_observed", "state": "MERGE_OBSERVED",
                                   "automatic": False, "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"} for f in ("PR-35", "RS-40")]
    n = p["PR-35"]["node"]  # P35-6..10
    n["session_class"] = "DEDICATED_PR_REVIEW_SESSION"
    assert n["receiving_role"] == "Same dedicated PR engineer in the same PR-development session; no new role."
    n["receiving_role"] = PR35_ROLE
    assert n["adds_session"] is False and n["cross_session_route"] is False
    n["adds_session"] = True
    n["cross_session_route"] = True
    nf = n["native_function"]
    assert nf.endswith("and return MERGE_PENDING without merging.")
    n["native_function"] = nf[:-1] + "; return MERGE_OBSERVED when an active subscription observes Nathan's merge."
    r = p["RS-40"]["node"]  # R40-8
    assert r["receiving_role"] == "You are the same dedicated PR engineering session for the exact suspended work unit."
    r["receiving_role"] = RS40_ROLE


# ---- IO, build, checks ---------------------------------------------------------------------
def dump(o):
    return (json.dumps(o, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def load(d):
    g = json.load(open(d + "/global.json", encoding="utf-8"))
    p = {f[:-5]: json.load(open(d + "/prompts/" + f, encoding="utf-8")) for f in sorted(os.listdir(d + "/prompts"))}
    return g, p


def files(g, p):
    out = {"global.json": dump(g)}
    out.update({"prompts/%s.json" % k: dump(v) for k, v in p.items()})
    return out


def save(d, fs):
    os.makedirs(d + "/prompts", exist_ok=True)
    for k, b in fs.items():
        open(d + "/" + k, "wb").write(b)


def build(parts_dir, out):
    r = subprocess.run([sys.executable, GP, "build", parts_dir, out], capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    assert r.returncode == 0, r.stderr
    assert "WARNING" not in r.stdout + r.stderr, r.stdout + r.stderr
    raw = open(out, encoding="utf-8").read().split("\n")
    s = next(i for i, l in enumerate(raw) if l.strip() == "```json")
    e = len(raw) - 1
    while raw[e].strip() != "```":
        e -= 1
    block = ("\n".join(raw[s + 1:e]) + "\n").encode()
    G = json.loads(block)
    surf = V.routing_surface({"route_edges": G["edges"], "state_routes": G["state_routes"]})
    return {"stdout": r.stdout.strip().replace("\n", " | "), "nodes": len(G["nodes"]) if "nodes" in G else None,
            "edges": len(G["edges"]), "state_routes": len(G["state_routes"]), "bytes": len(block),
            "sha256": hashlib.sha256(block).hexdigest(), "surface": surf}


H = lambda b: (hashlib.sha256(b).hexdigest(), len(b))
BASE = {"global.json": ("9cc3b8852e2c0247ff9859c7f1f6728ca0006889f5ff40be0c68f465da92b76c", 28873),
        "prompts/DOC-10.json": ("04a6204f3c0e599942498168f47cae09d7cee7ed21275ce146241472af66b69a", 5737),
        "prompts/PR-10.json": ("a41e5e7ee60ac0cdba569878eb767c7c06204ea0234b46fd97255f936f1d145d", 6746),
        "prompts/PR-20.json": ("0a8051e302faad73232b91694937bf69f510fa2d17476e665f1ad2135915885e", 6848),
        "prompts/PR-30.json": ("51ef5f6b593f8f339a5e0e2806c95435ccf2d52897fff7fca7658d2328d4c885", 6298),
        "prompts/PR-35.json": ("2c1c7aa9be3413d19113f5dbd4847d4024646c8f6b8d05aba72e12973bb62b4c", 6657),
        "prompts/PR-40.json": ("cfe991001f13e5f6a1561901ffaef6febeb435b98f783b8bae38b6e8e1d1f493", 8488),
        "prompts/RS-40.json": ("3be8a22dfbd2d645f5bf44baf3a311063d04c2f961d046a614f28bf5e87250ff", 8806)}
SIM = {"global.json": ("87ccfb1c179ad2dea50f541fd35522a1564b9741d821f3b589433fb32e323124", 29037),
       "prompts/DOC-10.json": ("f715cee5815c3f7f149dd618f485e689636f154b204460af67715086a8c3a72a", 5772),
       "prompts/PR-10.json": ("a5ceb711b4d859ddd81734a3811ccb5ff4cb16ee61fbccce49d22193b7320a37", 6729),
       "prompts/PR-20.json": ("c7043b60c2f6f25a05fd8de26f323acf86570bd3dc72fad462165a8c9af99faf", 6844),
       "prompts/PR-30.json": ("0b062ecec0c67fd5e9f3a8190895218d9915819e999ca894250a49e51262aa4b", 6351),
       "prompts/PR-35.json": ("d315a3c70113fcbffefb5081afb0a0dc7a5dad7fe22ac438b92721fbaac470af", 7815),
       "prompts/PR-40.json": ("9a762c3f7753fe78d5af694033609f8c821c3d6b07bb4a8680732f2304273111", 8570),
       "prompts/RS-40.json": ("6916dbe138827227ba5bcd5a453be972322be3590566ffc6c48f978896033cf2", 9995)}
FINAL = dict(SIM)
FINAL.update({"global.json": ("ef4abb9cda68a9b75495036981903c76e822d6926421eb754ff0e0067f5dda60", 29598),
              "prompts/PR-35.json": ("c32a2fa5bc20076a98330095def964c4a48adf073d50a1fedd8f1208fcc87702", 8098),
              "prompts/RS-40.json": ("45ba0728ee8c661c2984ce56ff060f789a299d3b4e9ccd06c24dd7a3e531fe5d", 10050)})
SURFACE = ("fecc319bdd4ce7ee6201cb77d7231861", 284)

g0, p0 = load(PARTS)
F0 = files(g0, p0)
raw0 = {k: open(PARTS + "/" + k, "rb").read() for k in F0}
assert F0 == raw0, "writer does not reproduce the current parts byte for byte"
for k, v in BASE.items():
    assert H(F0[k]) == v, ("baseline moved", k, H(F0[k]))
assert g0["protected_identities"]["r1_oracle_sha256"] == "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"

# step 1: routing transform, A1-7 checkpoint
g1, p1 = copy.deepcopy(g0), copy.deepcopy(p0)
apply_routing(g1, p1)
F1 = files(g1, p1)
save(W + "/parts_routing", F1)
B1 = build(W + "/parts_routing", W + "/graph_routing.md")
print("ROUTING build:", B1)
assert (B1["edges"], B1["state_routes"], B1["bytes"], B1["sha256"], B1["surface"]) == (
    229, 55, 574175, "b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7", SURFACE), B1
changed1 = sorted(k for k in F1 if F1[k] != F0[k])
assert changed1 == sorted(SIM), changed1
for k, v in SIM.items():
    assert H(F1[k]) == v, ("V3 first table", k, H(F1[k]))
print("V3 first table: 8 changed files equal the simulation checkpoint; other 48 unchanged")

# step 2: non-routing edits, commit-1 state
g2, p2 = copy.deepcopy(g1), copy.deepcopy(p1)
apply_nonrouting(g2, p2)
assert g2["protected_identities"] == g0["protected_identities"]  # G16 untouched (E2)
assert g2["_other_edges"][1]["condition"] == g2["boundary_transitions"]["NATHAN_MANUAL_MERGE_ASSERTION"][0]["condition"]  # V4
assert g2["_other_edges"][2]["condition"] == g2["boundary_transitions"]["NATHAN_PROCEED"][0]["condition"]  # V4
F2 = files(g2, p2)
save(W + "/parts_final", F2)
B2 = build(W + "/parts_final", W + "/graph_final.md")
print("FINAL build:", B2)
assert (B2["edges"], B2["state_routes"], B2["surface"]) == (229, 55, SURFACE), B2
for k, v in FINAL.items():
    assert H(F2[k]) == v, ("V3 second table", k, H(F2[k]))
changed2 = sorted(k for k in F2 if F2[k] != F0[k])
assert changed2 == sorted(FINAL), changed2
print("V3 second table: global.json, PR-35.json, RS-40.json at commit-1 hashes; DOC-10, PR-10, PR-20, PR-30, PR-40 at sim hashes")

if WRITE:
    for k in changed2:
        open(PARTS + "/" + k, "wb").write(F2[k])
    B3 = build(PARTS, W + "/graph_repo.md")
    print("REPO build:", B3)
    assert B3["sha256"] == B2["sha256"] and B3["surface"] == SURFACE
    print("wrote", len(changed2), "files:", changed2)
