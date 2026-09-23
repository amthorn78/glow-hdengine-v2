"""§9 item 9, contract and graph regressions on the FINAL E2 contract and graph (in memory):
§8b.10's 53 (R-AB ... R-LIN) and §6.5's R1-R17, plus the header-vector check R-HDR-2.
Pass = findings(mutated) - findings(clean) == expected set, and nothing clean disappears.
usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_contract.py <edited-skills-root>"""
import copy, json, os, shutil, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
K = Path(sys.argv[1])
sys.path.insert(0, str(K / "flowmaster-validate/scripts"))
import validate_gcfpe_20260914 as V  # noqa: E402
C0 = json.loads((K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
G0 = json.loads((K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json").read_bytes())


def run(c, g):
    return set(V.validate_contract(c)), set(V.validate_graph_contract(c, g))


CC, GC = run(C0, G0)
print("CLEAN validate_contract:", sorted(CC), "validate_graph_contract:", sorted(GC), "routing_surface:", V.routing_surface(C0))
assert CC == set() and GC == set()
RES = []
GRAPH_SCORED = {"R-DE-8", "R-HC-6", "R-HC-7", "R3c"}


def edge(c, frm, to):
    r = [e for e in c["route_edges"] if e["from"] == frm and e["to"] == to]
    assert len(r) == 1, (frm, to, len(r)); return r[0]


def case(rid, mut, exp_c, exp_g=None, both=False, gmut=None):
    c, g = copy.deepcopy(C0), copy.deepcopy(G0)
    if mut: mut(c)
    if gmut: gmut(g)
    if both:
        g["edges"] = c["route_edges"]; g["state_routes"] = c["state_routes"]
    C, G = run(c, g)
    dc, dg = sorted(C - CC), sorted(G - GC)
    # §8b.10: contract regressions are scored on validate_contract; a graph set is scored only where the
    # spec states one (the regression targets validate_graph_contract). Other graph deltas are reported.
    graph_scored = rid in GRAPH_SCORED
    ok = dc == sorted(exp_c) and (not graph_scored or dg == sorted(exp_g or [])) and not (CC - C) and not (GC - G)
    RES.append((rid, ok)); print(("OK   " if ok else "BAD  ") + rid, "| contract +", dc, "| graph +", dg, "(scored)" if graph_scored else "(reported)")


RS = "ROUTING_SURFACE_CHANGED"
pd = lambda c: c["pr_development_contract"]
pm = lambda c: c["post_merge_three_event_contract"]
rc = lambda c: c["receiver_compatibility"]
tc = lambda c: c["transition_contract"]
# ---------- §8b.10 (53) ----------
case("R-AB-1", lambda c: pd(c)["added_boundaries"].__setitem__("session", 0), ["PR35_ADDED_BOUNDARY"])
case("R-AB-2", lambda c: pd(c)["added_boundaries"].__setitem__("cross_session_route", 0), ["PR35_ADDED_BOUNDARY"])
case("R-AB-3", lambda c: pd(c)["added_boundaries"].__setitem__("proceed", 1), ["PR35_ADDED_BOUNDARY"])
case("R-PC", lambda c: pd(c)["shared_exactly_one"].insert(2, "dedicated PR-development session"), ["PR_PHASE_CONTINUITY"])
case("R-V-1", lambda c: pd(c).__setitem__("pr35_result_vocabulary", [x for x in V.EXPECTED_PR35_RESULTS if x != "MERGE_OBSERVED"]), ["PR35_RESULT_VOCABULARY"])
case("R-V-2", lambda c: c["member_registry"]["PR-35"]["result_states"].remove("MERGE_OBSERVED"), ["PR35_STATE_ROUTES", "STATE_REGISTRY_MISMATCH:PR-35"],
     ["GRAPH_NODE_CONTRACT:PR-35"])
case("R-DE-1", lambda c: c["route_edges"].append({"from": "PR-35", "to": "PR-40", "automatic": False}), ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-2", lambda c: edge(c, "PR-35", "PR-40").__setitem__("automatic", True), ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-3", lambda c: edge(c, "RS-40", "PR-40").__setitem__("automatic", True), ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-4", lambda c: edge(c, "PR-35", "PR-40")["route_branches"][0].__setitem__("condition", "PR-35 returns its result"), ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-5", lambda c: (edge(c, "PR-35", "PR-40").__setitem__("state_predicates", ["MERGE_PENDING"]),
                          edge(c, "PR-35", "PR-40")["route_branches"][0].update({"state": "MERGE_PENDING", "applicable_states": ["MERGE_PENDING"]})),
     ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-6", lambda c: c["route_edges"].remove(edge(c, "RS-40", "PR-40")), ["DIRECT_PR35_PR40_EDGE", RS, "STATE_EDGE_MISMATCH:RS-40:merge_observed"], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-7", lambda c: c["route_edges"].append({"from": "PR-30", "to": "PR-40", "automatic": False}), ["DIRECT_PR30_PR40_EDGE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-DE-8", lambda c: c["route_edges"].append(copy.deepcopy(edge(c, "PR-35", "PR-40"))), ["DIRECT_PR35_PR40_EDGE", RS], ["GRAPH_DIRECT_PR40_EDGE"], both=True)
case("R-MB-1", lambda c: c["route_edges"].remove(edge(c, "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40")), ["PR40_MANUAL_MERGE_BOUNDARY", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-MB-2", lambda c: edge(c, "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40").__setitem__("automatic", True), ["PR40_MANUAL_MERGE_BOUNDARY", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-MB-3", lambda c: edge(c, "DOC-20", "PR-40")["route_branches"][0].__setitem__("condition", "actual merged state review is required"), ["PR40_MANUAL_MERGE_BOUNDARY", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-MB-4", lambda c: c["route_edges"].append({"from": "QA-10", "from_kind": "prompt", "to": "PR-40", "automatic": False, "route_branches": [{"condition": "x"}]}),
     ["PR40_MANUAL_MERGE_BOUNDARY", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R-PM-1", lambda c: pm(c).__setitem__("direct_PR35_to_PR40_automatic_edge", True), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-PM-2", lambda c: pm(c)["event_2"].__setitem__("fact", "product_owner_manual_merge_assertion"), ["POST_MERGE_THREE_EVENTS"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-PM-3", lambda c: pm(c).__setitem__("agent_merge_authorized", True), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-PM-4", lambda c: pm(c)["event_2"].__setitem__("time", "observed by the subscribed PR-35 session, else asserted at the later PR-40 invocation"), ["POST_MERGE_THREE_EVENTS"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-PM-5", lambda c: pm(c)["observed_merge_edges"].pop(1), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-PM-6", lambda c: pm(c)["observed_merge_edges"][0].__setitem__("automatic", True), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R-RG-1", lambda c: c["route_graph"].__setitem__("ordinary_pr_work_unit", ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]), ["ROUTE_GRAPH_SHORTHAND"])
case("R-RG-2", lambda c: c["route_graph"].pop("pr40_reject_replan"), ["ROUTE_GRAPH_SHORTHAND"])
case("R-RG-3", lambda c: c["route_graph"].__setitem__("pr35_no_subscription_fallback", c["route_graph"].pop("pr35_merge_pending_fallback")), ["ROUTE_GRAPH_SHORTHAND"])
case("R-SEM-1", lambda c: (c["route_graph_semantics"].pop("pr30_to_pr35_phase_continuation"),
                           c["route_graph_semantics"].__setitem__("same_session_phase_continuation", "PR-30 to PR-35 is one lawful same-session phase continuation inside GCF-17, not a new work unit or cross-session route.")), ["ROUTE_GRAPH_SEMANTICS"])
case("R-SEM-2", lambda c: c["route_graph_semantics"].__setitem__("pr40_entry", "Requires Nathan's later manual-merge assertion and PR-40's independent read-only verification."), ["ROUTE_GRAPH_SEMANTICS"])
case("R-SEM-3", lambda c: c["route_graph_semantics"].pop("pr40_reject_replan"), ["ROUTE_GRAPH_SEMANTICS"])
case("R-ROLE", lambda c: c["member_registry"]["PR-35"].__setitem__("receiving_role", "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request."),
     ["PR35_TOP_LEVEL_ROLE"], ["GRAPH_NODE_CONTRACT:PR-35"])


def to30(c):
    [e.__setitem__("to", "PR-30") for e in c["route_edges"] if e["from"] == "PR-40" and e["route_branches"][0]["branch_id"] == "reject_replan"]
    [r.__setitem__("destinations", ["PR-30"]) for r in c["state_routes"]["PR-40"] if r.get("branch_id") == "reject_replan"]


case("R-RP-1", to30, ["PR40_REJECT_REPLAN_ROUTE", RS], ["GRAPH_EDGE_CONTRACT_MISMATCH", "GRAPH_STATE_ROUTE_CONTRACT_MISMATCH"])
case("R-RP-2", lambda c: c["rescope_contract"].__setitem__("new_proceed_required", True), ["RESCOPE_CONTRACT"])
case("R-RC-1", lambda c: rc(c).__setitem__("PR-35", {"context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION", "same_session_workspace_worktree_branch_open_pr_original_proceed": True}), ["RECEIVER_CONTRACT:PR-35"])
case("R-RC-2", lambda c: rc(c)["PR-40"].__setitem__("nathan_manual_merge_assertion_required", True), ["RECEIVER_CONTRACT:PR-40"])
case("R-RC-3", lambda c: rc(c)["PR-30"]["accepted_contexts"].append("PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"), ["RECEIVER_CONTRACT:PR-30"])
case("R-RC-4", lambda c: rc(c).pop("PR-20"), ["RECEIVER_CONTRACT:PR-20"])
case("R-RC-5", lambda c: rc(c)["RS-40"].__setitem__("accepted_approval", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"), ["RECEIVER_CONTRACT:RS-40"])
case("R-RC-6", lambda c: rc(c)["PR-40"].__setitem__("entry_fact", "OBSERVED_MERGE_EVENT_OR_NATHAN_ASSERTION_WHERE_NO_SUBSCRIPTION"), ["RECEIVER_CONTRACT:PR-40"])
case("R-HC-1", lambda c: tc(c).__setitem__("status_completed_work_decisions_constraints_unresolved_authority", True), ["HANDOFF_CONTRACT"])
case("R-HC-2", lambda c: tc(c).__setitem__("actual_pasteable_complete_prompt", False), ["HANDOFF_CONTRACT"])
case("R-HC-3", lambda c: tc(c)["prohibited_references"].remove("branch"), ["HANDOFF_PROHIBITED_REFERENCES"], ["GRAPH_HANDOFF_PROHIBITED_REFERENCES"])
case("R-HC-4", lambda c: tc(c).pop("no_branch_or_commit"), ["HANDOFF_CONTRACT"])
case("R-HC-5", lambda c: tc(c).__setitem__("every_required_repository_and_pr_reference", True), ["HANDOFF_CONTRACT"])
case("R-HC-6", None, [], ["GRAPH_HANDOFF_PROHIBITED_REFERENCES"], gmut=lambda g: g["handoff_contract"]["prohibited"].append("phase history"))
case("R-HC-7", lambda c: tc(c)["prohibited_references"].remove("menu"), ["HANDOFF_PROHIBITED_REFERENCES"], ["GRAPH_HANDOFF_PROHIBITED_REFERENCES"])
case("R-R1-1", lambda c: c["protected_identities"].__setitem__("r1_oracle_changed", False), ["PROTECTED_IDENTITIES"])
case("R-R1-2", lambda c: c["graph_proofs"].__setitem__("protected_r1_46_rows_unchanged", True), ["GRAPH_PROOFS"])
case("R-R1-3", lambda c: c["protected_identities"].__setitem__("pr35_adds_r1_row", True), ["PROTECTED_IDENTITIES"])
case("R-ID", lambda c: c.__setitem__("contract_revision", "4.0.6"), ["CONTRACT_IDENTITY"])
case("R-PS", lambda c: pd(c).__setitem__("primary_skill_revision", "1.2.5"), ["PR_DEVELOPMENT_CONTRACT"])
case("R-OWN", lambda c: pd(c)["pr30_ownership"].__setitem__(5, "complete same-session PR-35 handoff"), ["PR_DEVELOPMENT_CONTRACT"])
case("R-LIN", lambda c: c["rescope_contract"]["preserved_lineage"].__setitem__(1, "PR_DEVELOPMENT_SESSION"), ["RESCOPE_CONTRACT"])
n8b = len(RES)
# ---------- §6.5 R1-R17 (those not identical to an 8b row are run separately; all are run) ----------
case("R1", lambda c: c.__setitem__("contract_revision", "4.0.6"), ["CONTRACT_IDENTITY"])
case("R2a", lambda c: tc(c).__setitem__("status_completed_work_decisions_constraints_unresolved_authority", True), ["HANDOFF_CONTRACT"])
case("R2b", lambda c: tc(c).__setitem__("epic_change_and_work_unit", True), ["HANDOFF_CONTRACT"])
case("R2c", lambda c: tc(c).__setitem__("actual_pasteable_complete_prompt", False), ["HANDOFF_CONTRACT"])
case("R2d", lambda c: tc(c).pop("no_branch_or_commit"), ["HANDOFF_CONTRACT"])
case("R2e", lambda c: tc(c).__setitem__("every_required_repository_and_pr_reference", True), ["HANDOFF_CONTRACT"])
case("R3a", lambda c: tc(c)["prohibited_references"].remove("branch"), ["HANDOFF_PROHIBITED_REFERENCES"], ["GRAPH_HANDOFF_PROHIBITED_REFERENCES"])
case("R3b", lambda c: tc(c)["prohibited_references"].append("next action"), ["HANDOFF_PROHIBITED_REFERENCES"])
case("R3c", None, [], ["GRAPH_HANDOFF_PROHIBITED_REFERENCES"], gmut=lambda g: g["handoff_contract"]["prohibited"].append("next action"))
case("R4", lambda c: pm(c).__setitem__("direct_PR35_to_PR40_automatic_edge", True), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R5a", lambda c: pm(c)["event_2"].__setitem__("fact", "product_owner_manual_merge_assertion"), ["POST_MERGE_THREE_EVENTS"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R5b", lambda c: pm(c)["event_2"].__setitem__("time", "later PR-40 invocation"), ["POST_MERGE_THREE_EVENTS"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])
case("R5c", lambda c: pm(c)["observed_merge_edges"].__delitem__(1), ["POST_MERGE_CONTRACT"], ["GRAPH_POST_MERGE_CONTRACT_MISMATCH"])  # §8b.7 rule 7 placement
case("R6a", lambda c: c["route_graph"].__setitem__("ordinary_pr_work_unit", ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]), ["ROUTE_GRAPH_SHORTHAND"])
case("R6b", lambda c: c["route_graph"].pop("pr40_reject_replan"), ["ROUTE_GRAPH_SHORTHAND"])
case("R6c", lambda c: c["route_graph"].pop("pr35_merge_pending_fallback"), ["ROUTE_GRAPH_SHORTHAND"])
case("R7a", lambda c: pd(c)["added_boundaries"].__setitem__("session", 0), ["PR35_ADDED_BOUNDARY"])
case("R7b", lambda c: pd(c)["added_boundaries"].__setitem__("proceed", 1), ["PR35_ADDED_BOUNDARY"])
case("R7c", lambda c: pd(c)["added_boundaries"].__setitem__("cross_session_route", 0), ["PR35_ADDED_BOUNDARY"])
case("R8", lambda c: pd(c)["shared_exactly_one"].insert(2, "dedicated PR-development session"), ["PR_PHASE_CONTINUITY"])
case("R9", lambda c: pd(c)["pr35_result_vocabulary"].remove("MERGE_OBSERVED"), ["PR35_RESULT_VOCABULARY"])
case("R10a", lambda c: pd(c).__setitem__("primary_skill_revision", "1.2.5"), ["PR_DEVELOPMENT_CONTRACT"])
case("R10b", lambda c: pd(c)["pr30_ownership"].__setitem__(5, "complete same-session PR-35 handoff"), ["PR_DEVELOPMENT_CONTRACT"])
case("R11a", lambda c: c["protected_identities"].__setitem__("r1_oracle_changed", False), ["PROTECTED_IDENTITIES"])
case("R11b", lambda c: c["protected_identities"].__setitem__("r1_oracle_sha256", "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"), ["PROTECTED_IDENTITIES"])
case("R12", lambda c: c["graph_proofs"].__setitem__("protected_r1_46_rows_unchanged", True), ["GRAPH_PROOFS"])
case("R13a", lambda c: rc(c)["PR-30"].__setitem__("accepted_inputs", ["PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"]), ["RECEIVER_CONTRACT:PR-30"])
case("R13b", lambda c: rc(c)["PR-35"].__setitem__("same_session_workspace_worktree_branch_open_pr_original_proceed", True), ["RECEIVER_CONTRACT:PR-35"])
case("R13c", lambda c: rc(c)["PR-40"].__setitem__("nathan_manual_merge_assertion_required", True), ["RECEIVER_CONTRACT:PR-40"])
case("R13d", lambda c: rc(c).pop("PR-20"), ["RECEIVER_CONTRACT:PR-20"])
case("R13e", lambda c: rc(c)["RS-40"].__setitem__("accepted_approval", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"), ["RECEIVER_CONTRACT:RS-40"])
case("R14", lambda c: c["route_edges"][0]["route_branches"][0].__setitem__("condition", c["route_edges"][0]["route_branches"][0]["condition"] + " x"), [RS], ["GRAPH_EDGE_CONTRACT_MISMATCH"])
case("R15", lambda c: c["preservation"].__setitem__("versioned_sibling_successors", False), ["PRESERVATION_CONTRACT"])
case("R16", lambda c: c["route_graph_semantics"].__setitem__("same_session_phase_continuation", c["route_graph_semantics"].pop("pr30_to_pr35_phase_continuation")), ["ROUTE_GRAPH_SEMANTICS"])
case("R17", lambda c: c["rescope_contract"]["preserved_lineage"].__setitem__(1, "PR_DEVELOPMENT_SESSION"), ["RESCOPE_CONTRACT"])
n6 = len(RES) - n8b
# ---------- R-HDR-2: 12 decorated release-header forms (4 keys x plain, bold, bullet) ----------
clean_header = ["PR-35 title", "Prompt ID: PR-35", "Notion URL: https://app.notion.com/p/" + "0" * 32 + "?pvs=204", "## Native purpose"]
forms = []
for key, val in (("Prompt Version:", "091426.1"), ("Prompt version:", "091426.1"), ("Set:", "Glow HDE Complete Prompt Flow 091426.1"), ("Ecosystem release:", "GCFPE-20260914.1")):
    forms += [f"{key} {val}", f"**{key}** {val}", f"- {key} {val}"]
hits = [V.prompt_body_release_header(clean_header[:2] + [f] + clean_header[2:]) for f in forms]
ok = all(hits) and len(forms) == 12 and not V.prompt_body_release_header(clean_header)
RES.append(("R-HDR-2", ok)); print(("OK   " if ok else "BAD  ") + "R-HDR-2", sum(hits), "of", len(forms), "forms caught; clean header silent:", not V.prompt_body_release_header(clean_header))
# ---------- change-flow validator (fail-fast) for R1 and R9 ----------
W = Path("/tmp/claude-0/e2/reg/cfR"); ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/e2/tmp"}
for rid, mut, want in (("R1-cf", lambda c: c.__setitem__("contract_revision", "4.0.6"), "FAIL: corrected-source contract revision"),
                       ("R9-cf", lambda c: pd(c)["pr35_result_vocabulary"].remove("MERGE_OBSERVED"), "FAIL: PR-35 results")):
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(K / "change-flow", W / "change-flow")
    c = copy.deepcopy(C0); mut(c)
    (W / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").write_text(json.dumps(c, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    r = subprocess.run([sys.executable, str(W / "change-flow/scripts/validate_gcfpe_20260914.py")], capture_output=True, text=True, env=ENV)
    out = (r.stdout + r.stderr).strip()
    ok = r.returncode == 1 and out == want
    RES.append((rid, ok)); print(("OK   " if ok else "BAD  ") + rid, out[:200])
shutil.rmtree(W, ignore_errors=True)
print(f"CONTRACT_REGRESSIONS 8b.10: {sum(ok for _, ok in RES[:n8b])} of {n8b} exact; 6.5: {sum(ok for _, ok in RES[n8b:n8b + n6])} of {n6} exact; "
      f"other: {sum(ok for _, ok in RES[n8b + n6:])} of {len(RES) - n8b - n6}")
