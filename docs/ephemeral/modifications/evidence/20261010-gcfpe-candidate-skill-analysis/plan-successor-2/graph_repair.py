#!/usr/bin/env python3
"""Candidate graph-part repairs for MODIFICATION-20261010-gcfpe-candidate-skill-analysis (PLAN successor 2).

  graph_repair.py apply <parts-dir>                 F09 and F05 on a copy of the candidate parts; idempotent:
                                                    a second apply changes nothing and says so
  graph_repair.py check <parts-dir> <base-parts>    after the shipped reindex: the repaired parts carry exactly
                                                    the planned values, the only index change is the new edge's
                                                    appended index, and nothing else differs from the base
  graph_repair.py built <graph.md> <base-graph.md>  the shipped build of the repaired parts against the build of
                                                    the base: one more edge, RS-20's derived state routes gain
                                                    exactly the three rows in place, every other route unchanged
  graph_repair.py selftest <base-parts> <scratch> <graph_parts.py>
                                                    check() passes on a clean repair and fails on each injected
                                                    regression; uses the shipped reindex

After apply, run the shipped `graph_parts.py reindex` and then `build`; the index lists are the builder's own
bookkeeping (glow-graph-contract), never set here. Writes only the parts directory it is given.
"""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
from pathlib import Path

_SRC = {"path": "candidate/prompts/d/RS-20.md",
        "section": "Rescope authorship, independent review and return; Required inputs"}
_ABSENT = "future Proceed, PR, execution session/vehicle and PR_RETURN_PHASE fields absent"
PR20_EDGE = {
    "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
    "automatic": False,
    "from": "RS-20",
    "from_kind": "prompt",
    "immediate": True,
    "route_branches": [
        {"applicable_states": ["APPROVE"], "branch_id": "rescope_pr20_preproceed",
         "condition": "recorded origin is the actual PR-20 planning author, before Proceed; the exact approved delta "
                      "returns to that planning context with exactly one qualifying addendum; " + _ABSENT,
         "next_prompt_handoff_count": 1, "public_result": True, "route_kind": "NATIVE_RESULT", "route_steps": [],
         "source_evidence": _SRC, "state": "APPROVE", "terminal_for_invocation": False},
        {"applicable_states": ["REJECT"], "branch_id": "reject_pr20_preproceed",
         "condition": "recorded origin is the actual PR-20 planning author, before Proceed; unchanged authority; "
                      "no addendum; " + _ABSENT,
         "next_prompt_handoff_count": 1, "public_result": True, "route_kind": "NATIVE_RESULT", "route_steps": [],
         "source_evidence": _SRC, "state": "REJECT", "terminal_for_invocation": False},
        {"applicable_states": ["IN_SCOPE_REPAIR"], "branch_id": "in_scope_pr20_preproceed",
         "condition": "recorded origin is the actual PR-20 planning author, before Proceed; the existing scope "
                      "authorizes the repair; no addendum; " + _ABSENT,
         "next_prompt_handoff_count": 1, "public_result": True, "route_kind": "NATIVE_RESULT", "route_steps": [],
         "source_evidence": _SRC, "state": "IN_SCOPE_REPAIR", "terminal_for_invocation": False},
    ],
    "state_predicates": ["APPROVE", "IN_SCOPE_REPAIR", "REJECT"],
    "to": "PR-20",
    "to_kind": "prompt",
    "transport": "COMPLETE_NEXT_PROMPT_HANDOFF",
}
# Each new branch heads its group in the semantic row order (approvals first, terminal rows last).
ORDER_BEFORE = {"rescope_pr20_preproceed": "rescope_pr30_prepublication",
                "reject_pr20_preproceed": "reject_pr30",
                "in_scope_pr20_preproceed": "in_scope_pr30"}
FORMAT_HOME = ("PF06-Canon-Change-Process-Guide §0.1A and PF27-Canon-Plan-Templates, Canon precedence for template "
               "use, read from docs/pfcanon on main")
FORMAT_EXPECTATIONS = {
    "heading": "exactly one H2 carrying the next continuous addendum number, resolved by the producer from current "
               "controlled PF10 at creation, and a descriptive title",
    "number_carrier": "the H2 heading; no standalone pf10_addendum_number metadata field, which stays forbidden",
    "subordinate_headings": "H3 or lower only",
    "subject_matter": "page-ready, self-contained declarative statement of the approved decision and its approval "
                      "status, durable requirements, exceptions, scope, exclusions and nonclaims, evidence, dependencies, "
                      "conflicts, consequences and unresolved obligations, keeping completed work, future work, "
                      "recommendations and unproven facts distinct",
    "excluded_content": "role-addressed handling, publication, routing and record-maintenance instructions, which stay "
                        "in the decision and handoff",
}
F05_VALUES = {"producer_allocates_pf10_number": True, "format_home": FORMAT_HOME,
              "format_expectations": FORMAT_EXPECTATIONS}
PRESERVED = {"producer_edits_pf10": False, "producer_claims_canonical_adoption": False,
             "exactly_one_per_qualifying_approval": True, "paste_ready": True,
             "exact_producer_set": ["CF-C-30", "CF-E-30", "ESC-40", "IA-30", "QA-70", "RS-20"],
             "never_for": ["INITIAL_APPROVAL", "REJECTION", "DENIAL", "REVISION_REQUIRED", "PENDING", "UNCHANGED",
                           "EDITORIAL", "IN_SCOPE_REPAIR"]}


def load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def dump(p: Path, obj) -> None:
    p.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def apply(parts: Path) -> dict:
    changed = []
    rs = parts / "prompts" / "RS-20.json"
    r = load(rs)
    if not any(e.get("to") == "PR-20" for e in r["edges"]):
        # Appended, never sorted in: the shipped builder places an edge beyond its part's index list after the
        # largest index, and `reindex` then records that position, so no existing edge moves.
        r["edges"].append(copy.deepcopy(PR20_EDGE))
        changed.append("RS-20.edges")
    order = r["state_route_order"]
    for new, before in ORDER_BEFORE.items():
        if new not in order:
            order.insert(order.index(before), new)
            changed.append(f"RS-20.state_route_order:{new}")
    if changed:
        dump(rs, r)
    gp = parts / "global.json"
    g = load(gp)
    c = g["pf10_addendum_contract"]
    for k, v in F05_VALUES.items():
        if c.get(k) != v:
            c[k] = v
            changed.append(f"global.pf10_addendum_contract.{k}")
    if any(x.startswith("global.") for x in changed):
        dump(gp, g)
    return {"mode": "apply", "changed": changed, "already_applied": not changed}


def _assembled(parts: Path):
    """Edges in index order when the bookkeeping is complete (exactly one index per edge, exactly 0..N-1)."""
    g = load(parts / "global.json")
    pairs = list(zip(g.get("_other_edge_indices") or [], g.get("_other_edges", [])))
    complete = len(g.get("_other_edge_indices") or []) == len(g.get("_other_edges", []))
    for q in sorted((parts / "prompts").glob("*.json")):
        o = load(q)
        complete &= len(o.get("edge_indices") or []) == len(o["edges"])
        pairs.extend(zip(o.get("edge_indices") or [], o["edges"]))
    if not complete or sorted(i for i, _ in pairs) != list(range(len(pairs))):
        return None, len(pairs)
    return [e for _, e in sorted(pairs, key=lambda t: t[0])], len(pairs)


def _strip_indices(obj):
    o = copy.deepcopy(obj)
    o.pop("edge_indices", None)
    o.pop("_other_edge_indices", None)
    return o


def check(parts: Path, base: Path) -> dict:
    problems = []
    r = load(parts / "prompts" / "RS-20.json")
    edges = [e for e in r["edges"] if e.get("to") == "PR-20"]
    if len(edges) != 1:
        problems.append(f"PR20_EDGE_COUNT_{len(edges)}")
    else:
        e = edges[0]
        want = {b["branch_id"]: b for b in PR20_EDGE["route_branches"]}
        got = {b.get("branch_id"): b for b in e.get("route_branches", [])}
        if set(got) != set(want):
            problems.append("PR20_BRANCH_SET")
        for bid, b in got.items():
            w = want.get(bid)
            if w is None:
                continue
            for k in ("state", "applicable_states", "next_prompt_handoff_count", "terminal_for_invocation",
                      "public_result", "route_kind", "route_steps"):
                if b.get(k) != w[k]:
                    problems.append(f"PR20_BRANCH_FIELD:{bid}.{k}")
        for k in ("to_kind", "transport", "automatic", "immediate", "actual_branch_cardinality", "state_predicates"):
            if e.get(k) != PR20_EDGE[k]:
                problems.append(f"PR20_EDGE_FIELD:{k}")
    order = r["state_route_order"]
    for new, before in ORDER_BEFORE.items():
        if order.count(new) != 1 or order.index(new) + 1 != order.index(before):
            problems.append(f"ROUTE_ORDER:{new}")
    # index proof: the shipped reindex ran (every edge has exactly one index, 0..N-1), and every existing edge
    # keeps its relative order. Where the new edge lands is the builder's own rule (after the largest
    # global.json index); reindex then renumbers later edges, which is bookkeeping, not a move.
    order_new, n_new = _assembled(parts)
    order_base, n_base = _assembled(base)
    if order_new is None or n_new != n_base + 1:
        problems.append("EDGE_INDICES_NOT_REINDEXED")
    elif [e for e in order_new if not (e["from"] == "RS-20" and e["to"] == "PR-20")] != order_base:
        problems.append("EXISTING_EDGE_ORDER_CHANGED")
    c = load(parts / "global.json")["pf10_addendum_contract"]
    for k, v in {**F05_VALUES, **PRESERVED}.items():
        if c.get(k) != v:
            problems.append(f"PF10_CONTRACT:{k}")
    # scope proof: nothing else moved except edge index bookkeeping
    moved = []
    for p in sorted((base / "prompts").glob("*.json")):
        if p.name == "RS-20.json":
            continue
        if _strip_indices(load(p)) != _strip_indices(load(parts / "prompts" / p.name)):
            moved.append(p.name)
    gb, gr = _strip_indices(load(base / "global.json")), _strip_indices(load(parts / "global.json"))
    gb["pf10_addendum_contract"] = {k: v for k, v in gb["pf10_addendum_contract"].items() if k not in F05_VALUES}
    gr["pf10_addendum_contract"] = {k: v for k, v in gr["pf10_addendum_contract"].items() if k not in F05_VALUES}
    if gb != gr:
        moved.append("global.json(other than the F05 values)")
    rb, rr = _strip_indices(load(base / "prompts" / "RS-20.json")), _strip_indices(r)
    rr = copy.deepcopy(rr)
    rr["edges"] = [e for e in rr["edges"] if e.get("to") != "PR-20"]
    rr["state_route_order"] = [x for x in rr["state_route_order"] if x not in ORDER_BEFORE]
    if rb != rr:
        moved.append("RS-20.json(other than the PR-20 edge and its three route-order rows)")
    if moved:
        problems.append("OUT_OF_SCOPE_CHANGE:" + ",".join(moved))
    if set(base.joinpath("prompts").glob("*.json")) and \
            {p.name for p in (base / "prompts").glob("*.json")} != {p.name for p in (parts / "prompts").glob("*.json")}:
        problems.append("PART_SET_CHANGED")
    return {"mode": "check", "problems": problems, "ok": not problems}


def _graph(p: Path):
    lines = p.read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(lines) if l.strip() == "```json")
    e = len(lines) - 1
    while lines[e].strip() != "```":
        e -= 1
    return json.loads("\n".join(lines[s + 1:e]))


def built(graph: Path, base_graph: Path) -> dict:
    problems = []
    g, b = _graph(graph), _graph(base_graph)
    if len(g["edges"]) != len(b["edges"]) + 1:
        problems.append(f"EDGE_COUNT_{len(b['edges'])}_TO_{len(g['edges'])}")
    if [e for e in g["edges"] if not (e["from"] == "RS-20" and e["to"] == "PR-20")] != b["edges"]:
        problems.append("OTHER_EDGES_CHANGED_OR_MOVED")
    rows, base_rows = g["state_routes"]["RS-20"], b["state_routes"]["RS-20"]
    new_rows = [x for x in rows if x["branch_id"] in ORDER_BEFORE]
    if [x for x in rows if x["branch_id"] not in ORDER_BEFORE] != base_rows:
        problems.append("RS20_EXISTING_ROUTES_CHANGED")
    if sorted(x["branch_id"] for x in new_rows) != sorted(ORDER_BEFORE) or any(
            x["destinations"] != ["PR-20"] or x["terminal_for_invocation"] or x["next_prompt_handoff_count"] != 1
            for x in new_rows):
        problems.append("RS20_NEW_ROUTES")
    ids = [x["branch_id"] for x in rows]
    for new, before in ORDER_BEFORE.items():
        if new in ids and before in ids and ids.index(new) + 1 != ids.index(before):
            problems.append(f"RS20_ROUTE_ORDER:{new}")
    if {k: v for k, v in g["state_routes"].items() if k != "RS-20"} != \
            {k: v for k, v in b["state_routes"].items() if k != "RS-20"}:
        problems.append("OTHER_STATE_ROUTES_CHANGED")
    c = g["pf10_addendum_contract"]
    for k, v in {**F05_VALUES, **PRESERVED}.items():
        if c.get(k) != v:
            problems.append(f"BUILT_PF10_CONTRACT:{k}")
    rest = {k: v for k, v in g.items() if k not in ("edges", "state_routes", "pf10_addendum_contract")}
    base_rest = {k: v for k, v in b.items() if k not in ("edges", "state_routes", "pf10_addendum_contract")}
    if rest != base_rest:
        problems.append("OTHER_GRAPH_KEYS_CHANGED:" + ",".join(sorted(k for k in set(rest) | set(base_rest)
                                                                     if rest.get(k) != base_rest.get(k))))
    return {"mode": "built", "edges": len(g["edges"]), "rs20_routes": len(rows), "problems": problems,
            "ok": not problems}


def selftest(base: Path, scratch: Path, graph_parts_py: Path) -> dict:
    def fresh(name: str) -> Path:
        d = scratch / name
        shutil.rmtree(d, ignore_errors=True)
        shutil.copytree(base, d)
        return d

    def repaired(name: str) -> Path:
        d = fresh(name)
        apply(d)
        subprocess.run([sys.executable, str(graph_parts_py), "reindex", str(d)], check=True, capture_output=True)
        return d

    rows = []
    clean = repaired("clean")
    c = check(clean, base)
    rows.append({"case": "clean_repair", "check_ok": c["ok"], "problems": c["problems"], "want": True})
    rows.append({"case": "second_apply_is_noop", "check_ok": apply(clean)["already_applied"], "want": True})
    c = check(fresh("unrepaired"), base)
    rows.append({"case": "unrepaired_base", "check_ok": c["ok"], "problems": c["problems"], "want": False})
    unindexed = fresh("not_reindexed")
    apply(unindexed)
    c = check(unindexed, base)
    rows.append({"case": "not_reindexed", "check_ok": c["ok"], "problems": c["problems"], "want": False})
    injections = {
        "branch_removed": lambda d: _edit_rs(d, lambda e: e["route_branches"].pop()),
        "branch_terminal": lambda d: _edit_rs(d, lambda e: e["route_branches"][0].__setitem__("terminal_for_invocation", True)),
        "two_handoffs": lambda d: _edit_rs(d, lambda e: e["route_branches"][1].__setitem__("next_prompt_handoff_count", 2)),
        "route_order_row_missing": lambda d: _edit_order(d, "reject_pr20_preproceed"),
        "allocates_false": lambda d: _edit_global(d, "producer_allocates_pf10_number", False),
        "format_home_stale": lambda d: _edit_global(d, "format_home", "Glow Operations Hub, Notion. Canonical, and "
                                                                       "not hard-linked to PF10."),
        "format_expectations_missing": lambda d: _edit_global(d, "format_expectations", None),
        "edits_pf10_true": lambda d: _edit_global(d, "producer_edits_pf10", True),
        "claims_adoption_true": lambda d: _edit_global(d, "producer_claims_canonical_adoption", True),
        "producer_set_changed": lambda d: _edit_global(d, "exact_producer_set",
                                                       ["CF-C-30", "CF-E-30", "ESC-40", "IA-30", "QA-70"]),
        "never_for_changed": lambda d: _edit_global(d, "never_for", ["DENIAL"]),
        "forbidden_number_field_dropped": lambda d: _edit_global(d, "forbidden_fields", []),
        "other_part_moved": lambda d: _edit_part(d, "PR-20.json"),
    }
    for name, inject in injections.items():
        d = repaired(name)
        inject(d)
        c = check(d, base)
        rows.append({"case": name, "check_ok": c["ok"], "problems": c["problems"], "want": False})
    for row in rows:
        row["as_expected"] = row["check_ok"] == row["want"]
    return {"mode": "selftest", "rows": rows, "ok": all(r["as_expected"] for r in rows)}


def _edit_rs(d: Path, fn) -> None:
    p = d / "prompts" / "RS-20.json"
    r = load(p)
    fn([e for e in r["edges"] if e["to"] == "PR-20"][0])
    dump(p, r)


def _edit_order(d: Path, branch: str) -> None:
    p = d / "prompts" / "RS-20.json"
    r = load(p)
    r["state_route_order"].remove(branch)
    dump(p, r)


def _edit_global(d: Path, key: str, value) -> None:
    p = d / "global.json"
    g = load(p)
    g["pf10_addendum_contract"][key] = value
    dump(p, g)


def _edit_part(d: Path, name: str) -> None:
    p = d / "prompts" / name
    o = load(p)
    o["state_route_order"] = list(reversed(o["state_route_order"]))
    dump(p, o)


def main() -> int:
    mode = sys.argv[1]
    if mode == "apply":
        res = apply(Path(sys.argv[2]))
        res["ok"] = True
    elif mode == "check":
        res = check(Path(sys.argv[2]), Path(sys.argv[3]))
    elif mode == "built":
        res = built(Path(sys.argv[2]), Path(sys.argv[3]))
    else:
        res = selftest(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
