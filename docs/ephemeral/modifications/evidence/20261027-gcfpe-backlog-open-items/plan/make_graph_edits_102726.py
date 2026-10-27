#!/usr/bin/env python3
"""Normalize every design worker's graph_edits into plan/graph-edits.json (MODIFICATION-20261027-gcfpe-backlog-open-items).

    make_graph_edits_102726.py <repo-root> [--check]

Reads plan/work/W1.json, W4.json, W5.json and W7.json (W2, W3a, W3b, W6 and W8 carry no graph edit; checked) and
main's docs/graph/parts, and writes plan/graph-edits.json: one entry per edit with the part file, a JSON pointer
(a list of keys and indices) into that file, the base value at the pointer (`old`) and the planned value (`new`).
Every `new` is copied from the worker file, never retyped here; every `old` is read from main's parts and must
equal the worker's stated old wherever the worker gave a concrete value. The coordinator's decisions are applied:

  C-11  every candidate node, CL-05 included, is UNSELECTED_CANDIDATE until the flip (GE-W7-07, GE-W7-09); W5's
        CL-05 object carried SELECTED_PRODUCTION, which is replaced.
  C-9   GCF-24.CLOSE is a material row (r1 26 core / 21 material) and CL-05's stage category is CLOSE_MUTATION_SET:
        W5's values, checked here.
  C-1   successor node heads (title, URL, version, predecessor) come from the successor map at apply time, by
        rule GE-W7-08; CL-05's URL is the marker "@MAP_URL:CL-05", filled from the map. GCFPE-MGMT-10 is KEPT.

--check rebuilds in memory and exits 1 unless the file on disk is byte-identical. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

REL = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/plan"


def _get(obj, ptr):
    for k in ptr:
        obj = obj[k]
    return obj


def main(repo: str, *flags: str) -> int:
    root = Path(repo)
    work = root / REL / "work"
    parts = root / "docs/graph/parts"
    W = {n: json.loads((work / f"{n}.json").read_text(encoding="utf-8")) for n in
         ("W1", "W2", "W3a", "W3b", "W4", "W5", "W6", "W7", "W8")}
    for n in ("W2", "W3a", "W3b", "W6", "W8"):
        assert W[n]["graph_edits"] == [], f"{n} has graph edits"
    base = {"global.json": json.loads((parts / "global.json").read_text(encoding="utf-8"))}
    for f in sorted((parts / "prompts").glob("*.json")):
        base["prompts/" + f.name] = json.loads(f.read_text(encoding="utf-8"))
    edits, no_ops = [], []

    def add(eid, src, part, file, ptr, op, new=None, stated_old=None, why=None, guard=None):
        doc = base[file]
        if op == "append":
            old = None
            length = len(_get(doc, ptr))
        else:
            old = copy.deepcopy(_get(doc, ptr))
            length = None
            if stated_old is not None:
                assert old == stated_old, (eid, "stated old differs from main's parts")
        if guard:
            for gptr, gval in guard:
                assert _get(doc, gptr) == gval, (eid, gptr, _get(doc, gptr))
        e = {"id": eid, "source": src, "part": part, "file": file, "pointer": list(ptr), "op": op, "old": old,
             "new": copy.deepcopy(new)}
        if length is not None:
            e["old_length"] = length
        if guard:
            e["guard"] = [[list(p), v] for p, v in guard]
        if why:
            e["why"] = why
        edits.append(e)

    # --- W1 (PART-08): DOC-20 loses its PR-40 edge. ---
    g1 = W["W1"]["graph_edits"]
    add("GE-W1-01", "W1.json graph_edits[0]", "PART-08", "prompts/DOC-20.json", ["edges", 3], "remove",
        stated_old=g1[0]["old_value"], why=g1[0]["why"])
    add("GE-W1-02", "W1.json graph_edits[1]", "PART-08", "prompts/DOC-20.json", ["state_route_order"], "replace",
        new=g1[1]["new_value"], stated_old=g1[1]["old_value"], why=g1[1]["why"])
    add("GE-W1-03", "W1.json graph_edits[2]", "PART-08", "prompts/DOC-20.json",
        ["edges", 1, "route_branches", 0, "condition"], "replace", new=g1[2]["new_value"],
        stated_old=g1[2]["old_value"], why=g1[2]["why"],
        guard=[(["edges", 1, "route_branches", 0, "branch_id"], "documentation_terminal")])
    no_ops.append({"source": "W1.json graph_edits[3]", "file": "prompts/DOC-20.json", "pointer": ["edge_indices"],
                   "disposition": "DERIVED by graph_parts.py reindex"})

    # --- W4 (PART-09, PART-10). ---
    g4 = W["W4"]["graph_edits"]
    add("GE-W4-01", "W4.json graph_edits[0]", "PART-09", "prompts/IA-40.json", ["edges", 0, "route_branches", 0],
        "remove", why=g4[0]["why"],
        guard=[(["edges", 0, "to"], "ACTUAL_OWNER_TERMINAL_RETURN"),
               (["edges", 0, "route_branches", 0, "branch_id"], "redline_incomplete"),
               (["edges", 0, "route_branches", 0, "state"], "REDLINE_INCOMPLETE"),
               (["edges", 0, "route_branches", 0, "route_kind"], "TERMINAL_EXCEPTION")])
    add("GE-W4-02", "W4.json graph_edits[1]", "PART-09", "prompts/IA-40.json", ["edges", 0, "state_predicates"],
        "replace", new=g4[1]["new"], stated_old=g4[1]["old"])
    add("GE-W4-03", "W4.json graph_edits[2]", "PART-09", "prompts/IA-40.json", ["edges", 1, "route_branches"],
        "append", new=g4[2]["new"], why=g4[2]["why"],
        guard=[(["edges", 1, "to"], "IA-30"), (["edges", 1, "route_branches", -1, "branch_id"], "plan_delta_pending")])
    add("GE-W4-04", "W4.json graph_edits[3]", "PART-09", "prompts/IA-40.json", ["edges", 1, "state_predicates"],
        "replace", new=g4[3]["new"], stated_old=g4[3]["old"])
    no_ops.append({"source": "W4.json graph_edits[4]", "file": "prompts/IA-40.json", "pointer": ["state_route_order"],
                   "disposition": "UNCHANGED (already lists redline_incomplete)"})
    no_ops.append({"source": "W4.json graph_edits[5]", "file": "prompts/IA-30.json", "disposition": "UNCHANGED"})
    for eid, i, file, ptr, bid, to in (
            ("GE-W4-05", 6, "prompts/QA-70.json", ["edges", 3, "route_branches", 0, "condition"], "initial_approve", "QA-90"),
            ("GE-W4-06", 7, "prompts/QA-70.json", ["edges", 2, "route_branches", 0, "condition"], "initial_deny", "QA-80"),
            ("GE-W4-07", 8, "prompts/QA-80.json", ["edges", 1, "route_branches", 0, "condition"], "plan_pending_revised", "QA-70"),
            ("GE-W4-08", 9, "prompts/QA-80.json", ["edges", 0, "route_branches", 0, "condition"], "wrong_route_terminal",
             "NATHAN_TERMINAL_RETURN"),
            ("GE-W4-09", 10, "prompts/QA-80.json", ["edges", 1, "route_branches", 1, "condition"], "existing_delta_review",
             "QA-70")):
        add(eid, f"W4.json graph_edits[{i}]", g4[i]["part"], file, ptr, "replace", new=g4[i]["new"],
            stated_old=g4[i]["old"],
            guard=[(ptr[:2] + ["to"], to), (ptr[:4] + ["branch_id"], bid)])
    add("GE-W4-10", "W4.json graph_edits[11]", "PART-10", "global.json",
        ["artifact_availability_contract", "qa_artifact_births", "QA_PLAN_REVIEW", "after"], "replace",
        new=g4[11]["new"], stated_old=g4[11]["old"], why=g4[11]["why"])
    for i in (12, 13, 14):
        no_ops.append({"source": f"W4.json graph_edits[{i}]", "part": g4[i]["part"], "disposition": "NO GRAPH CHANGE"})

    # --- W5 (PART-13): CL-05 and the close stage. ---
    g5 = W["W5"]["graph_edits"]
    cl05 = copy.deepcopy(g5[0]["object"])
    assert cl05["edge_indices"] == ["<derived by graph_parts.py reindex; never typed>"]
    assert cl05["node"]["lifecycle"] == "SELECTED_PRODUCTION"
    cl05["edge_indices"] = []                                      # reindex derives them
    cl05["node"]["lifecycle"] = "UNSELECTED_CANDIDATE"             # C-11, GE-W7-09
    cl05["node"]["candidate_url"] = "@MAP_URL:CL-05"               # C-1, GE-W7-09: filled from the map
    assert cl05["node"]["r1_mapping"] == "GCF-24.CLOSE" and cl05["node"]["predecessor"] is None
    assert len(cl05["edges"]) == 4
    edits.append({"id": "GE-W5-01", "source": "W5.json graph_edits[0]", "part": "PART-13",
                  "file": "prompts/CL-05.json", "pointer": [], "op": "new_file", "old": None, "new": cl05,
                  "why": "W5's object; C-11 lifecycle UNSELECTED_CANDIDATE and the map URL marker (GE-W7-09); "
                         "edge_indices [] for reindex"})
    for eid, i, ptr, guard in (
            ("GE-W5-02", 1, ["edges", 0, "to"], [(["edges", 0, "route_branches", 0, "branch_id"], "pass_crd")]),
            ("GE-W5-03", 2, ["edges", 0, "route_branches", 0, "condition"],
             [(["edges", 0, "route_branches", 0, "branch_id"], "pass_crd")]),
            ("GE-W5-04", 3, ["edges", 1, "to"], [(["edges", 1, "route_branches", 0, "branch_id"], "pass_epic")]),
            ("GE-W5-05", 4, ["edges", 1, "route_branches", 0, "condition"],
             [(["edges", 1, "route_branches", 0, "branch_id"], "pass_epic")])):
        add(eid, f"W5.json graph_edits[{i}]", "PART-13", "prompts/QA-120.json", ptr, "replace", new=g5[i]["new"],
            stated_old=g5[i]["old"], guard=guard)
    no_ops.append({"source": "W5.json graph_edits[5]", "file": "prompts/QA-120.json",
                   "pointer": ["node", "predecessor_union_destinations"], "disposition": "UNCHANGED (GE-W7-10, W7-D6)"})
    for (eid0, f, i0, ptr_cond, ei) in (("GE-W5-06", "CL-C-10", 6, ["edges", 1, "route_branches", 0, "condition"], 4),
                                        ("GE-W5-09", "CL-E-10", 10, ["edges", 2, "route_branches", 0, "condition"], 5)):
        file = f"prompts/{f}.json"
        n = int(eid0[-2:])
        add(eid0, f"W5.json graph_edits[{i0}]", "PART-13", file, ptr_cond, "replace", new=g5[i0]["new"],
            stated_old=g5[i0]["old"], why=g5[i0].get("authority"),
            guard=[(ptr_cond[:2] + ["to"], "ESC-30"), (ptr_cond[:4] + ["branch_id"], "do_not_close_new_remedy")])
        assert g5[i0 + 1]["json_path"] == f"edges[+] (append as edges[{ei}])"
        assert len(base[file]["edges"]) == ei
        add(f"GE-W5-{n + 1:02d}", f"W5.json graph_edits[{i0 + 1}]", "PART-13", file, ["edges"], "append",
            new=g5[i0 + 1]["new"])
        add(f"GE-W5-{n + 2:02d}", f"W5.json graph_edits[{i0 + 2}]", "PART-13", file, ["state_route_order"], "replace",
            new=g5[i0 + 2]["new"], stated_old=g5[i0 + 2]["old"])
        no_ops.append({"source": f"W5.json graph_edits[{i0 + 3}]", "file": file, "pointer": ["edge_indices"],
                       "disposition": "DERIVED by graph_parts.py reindex"})
    gidx = {e["json_path"]: (i, e) for i, e in enumerate(g5) if e["file"] == "docs/graph/parts/global.json"}
    for eid, key, ptr in (("GE-W5-12", "qa_closure_contract", ["qa_closure_contract"]),
                          ("GE-W5-13", "candidate.member_count", ["candidate", "member_count"]),
                          ("GE-W5-14", "candidate.member_rule", ["candidate", "member_rule"]),
                          ("GE-W5-15", "protected_identities.r1_rows", ["protected_identities", "r1_rows"]),
                          ("GE-W5-16", "protected_identities.r1_material_rows",
                           ["protected_identities", "r1_material_rows"]),
                          ("GE-W5-17", "protected_identities.r1_oracle_sha256",
                           ["protected_identities", "r1_oracle_sha256"]),
                          ("GE-W5-18", "artifact_availability_contract.stage_categories",
                           ["artifact_availability_contract", "stage_categories"])):
        i, e = gidx[key]
        add(eid, f"W5.json graph_edits[{i}]", "PART-13", "global.json", ptr, "replace", new=e["new"],
            stated_old=e["old"], why=e.get("authority") or e.get("note"))
    # C-9: 26 core / 21 material; CLOSE_MUTATION_SET.
    assert gidx["protected_identities.r1_core_rows"][1]["new"] == 26
    assert gidx["protected_identities.r1_material_rows"][1]["new"] == 21
    assert gidx["artifact_availability_contract.stage_categories"][1]["new"]["CL-05"] == "CLOSE_MUTATION_SET"
    for key in ("protected_identities.r1_core_rows", "protected_identities.flowmaster_primary_core_sha256",
                "proofs.baseline_ids_retained"):
        i, e = gidx[key]
        assert e["old"] == e["new"]
        no_ops.append({"source": f"W5.json graph_edits[{i}]", "file": "global.json", "pointer": key.split("."),
                       "disposition": "UNCHANGED"})
    proofs_expected = {k.split(".")[1]: gidx[k][1]["new"] for k in ("proofs.candidate_node_count",
                                                                     "proofs.sole_added_node")}

    # --- W7 (PART-24): head values. ---
    g7 = {e["id"]: e for e in W["W7"]["graph_edits"]}
    for eid, ptr in (("GE-W7-01", ["candidate", "release"]), ("GE-W7-02", ["candidate", "version_family"]),
                     ("GE-W7-03", ["baseline"]), ("GE-W7-04", ["contract_id"]), ("GE-W7-05", ["selection_status"]),
                     ("GE-W7-06", ["_prologue"])):
        add(eid, f"W7.json graph_edits {eid}", "PART-24", "global.json", ptr, "replace", new=g7[eid]["new"],
            stated_old=g7[eid]["old"], why=g7[eid].get("why"))
    for eid in ("GE-W7-10", "GE-W7-13"):
        no_ops.append({"source": f"W7.json graph_edits {eid}", "json_path": g7[eid]["json_path"],
                       "disposition": "UNCHANGED"})
    prod_prologue = g7["GE-W7-12"]["new"].split("; ", 2)[2]
    assert prod_prologue.startswith("# GCFPE-20261027.1 Candidate Graph Contract\n")
    p7 = dict(g7["GE-W7-11"]["old"])
    proofs_expected.update({"baseline_ids_retained": True, "unresolved_edges": [], "prompt_inbound_edges_to_PR-50": 0,
                            "all_edge_endpoints_resolved": True, "candidate_url_placeholder_count": 0,
                            "unique_node_ids": True, "pf10_producer_set_exact": True,
                            "observed_pf10_producers": p7["observed_pf10_producers"]})
    rules = [
        {"id": "GE-W7-07", "source": "W7.json graph_edits GE-W7-07; C-11", "stage": "candidate",
         "rule": "node.lifecycle = UNSELECTED_CANDIDATE on all 56 parts", "value": "UNSELECTED_CANDIDATE"},
        {"id": "GE-W7-08", "source": "W7.json graph_edits GE-W7-08; C-1; W7-D8", "stage": "candidate",
         "rule": "for every member whose map disposition is SUCCESSOR: node.title = map title; node.candidate_url = "
                 "https://app.notion.com/p/<map page_id>?pvs=204; node.candidate_version = 102726.1; node.predecessor = "
                 "{notion_page_id: <100926.1 id>, release: GCFPE-20261009.1, title: <100926.1 title>, url: "
                 "https://app.notion.com/p/<100926.1 id>?pvs=204, version: 100926.1}, where the 100926.1 id and title "
                 "are main's node values and must equal the map's predecessor_page_id; KEPT members keep every node "
                 "value; CL-05's @MAP_URL marker takes the map's CL-05 page"},
        {"id": "GE-W7-11", "source": "W7.json graph_edits GE-W7-11; W5.json proofs edits", "stage": "candidate",
         "rule": "global.json proofs measured from the parts (baseline ids from main's 55 parts); never typed",
         "expected": proofs_expected},
        {"id": "GE-W7-12", "source": "W7.json graph_edits GE-W7-12", "stage": "production (flip)",
         "rule": "selection_status and every node.lifecycle SELECTED_PRODUCTION; _prologue the selected header",
         "selected_prologue": prod_prologue},
    ]
    doc = {
        "record_type": "BACKLOG_OPEN_ITEMS_GRAPH_EDITS",
        "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
        "release": "GCFPE-20261027.1", "version_family": "102726.1",
        "base": {"parts": "docs/graph/parts (main)", "token": {"nodes": 55, "edges": 235, "state_routes": 55,
                                                                "bytes": 593569,
                                                                "sha256": "43f84f29b9921c21f63ffbe21dd36a14bd846a89ae697ba3cf38746c2f887eb1"}},
        "decisions_applied": ["C-1: successor heads from the map; GCFPE-MGMT-10 KEPT",
                              "C-9: GCF-24.CLOSE material (26 core, 21 material); stage category CLOSE_MUTATION_SET",
                              "C-11: uniform UNSELECTED_CANDIDATE lifecycle until the flip (CL-05 included)"],
        "generated_by": REL + "/make_graph_edits_102726.py",
        "pointer_rule": "pointers resolve against main's parts; apply does replace and append first, then removals in "
                        "descending index order, so no pointer shifts before it is used",
        "edits": edits,
        "rules": rules,
        "no_ops": no_ops,
        "expected_build": {"nodes": 56, "edges": 240, "state_routes": 56,
                           "edge_arithmetic": "235 - 1 (DOC-20 -> PR-40) + 4 (CL-05) + 1 (CL-C-10 -> CL-05) + 1 "
                                              "(CL-E-10 -> CL-05) = 240"},
    }
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    out = root / REL / "graph-edits.json"
    if "--check" in flags:
        same = out.exists() and out.read_text(encoding="utf-8") == text
        print(json.dumps({"graph_edits_file_current": same, "edits": len(edits)}))
        return 0 if same else 1
    out.write_text(text, encoding="utf-8")
    print(json.dumps({"written": str(out), "edits": len(edits), "rules": len(rules), "no_ops": len(no_ops)}))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:]))
