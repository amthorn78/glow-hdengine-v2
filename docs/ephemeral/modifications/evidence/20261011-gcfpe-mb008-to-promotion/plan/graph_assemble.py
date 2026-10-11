#!/usr/bin/env python3
"""Candidate graph-part assembly for MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN, PART-05 and PART-08).

  graph_assemble.py apply <parts-dir> <mgmt10-url>
        GCFPE-MGMT-10's successor part (DN-C option A: the D20 three-mode body), global.json's member rule, and
        global.json's `proofs`, measured from the parts (the parent left them empty; F06), on a copy of the
        parent's candidate parts. <mgmt10-url> is the successor page's direct Notion URL, which
        exists only once EXECUTE duplicates the testing page; the PLAN dry run passes the testing page's URL as a
        stand-in. Idempotent: a second apply changes nothing and says so.
  graph_assemble.py flip <src-parts-dir> <dst-parts-dir>
        the production parts for PART-08: a copy whose only change is the lifecycle literals the selected parts
        carry (global selection_status and each node's lifecycle, to SELECTED_PRODUCTION). Nothing else moves.
  graph_assemble.py check <parts-dir> <base-parts-dir> [--flipped]
        after the shipped reindex: the parts carry exactly the planned values, and nothing else differs from the
        base except edge_indices lists (two edges leave the assembled order) and, with --flipped, the lifecycle
        literals
  graph_assemble.py selftest <base-parts-dir> <scratch> <graph_parts.py>
        check() passes on a clean apply and flip and fails on each injected regression; uses the shipped reindex

The MGMT-10 values are derived from the testing body's *Native purpose*, *Entry contract* and *Result routing*
sections and from the prepared stage 3 specification (GCFPE-MGMT-REDESIGN-ANALYSIS-v1.0.md §9A). That
specification predates D26, which added PRODUCT_OWNER_ACTION_PENDING to the body; the part follows the body.
After apply, run the shipped `graph_parts.py reindex` and then `build`. Writes only the directory it is given.
"""
from __future__ import annotations

import copy
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

MGMT = "GCFPE-MGMT-10"
SRC = {"path": "candidate/prompts/b/GCFPE-MGMT-10.md", "section": "Result routing"}
PREDECESSOR = {
    "notion_page_id": "3db4590a05eb81d1bb64ebcb3ca8eb54",
    "release": "GCFPE-20260914.1",
    "title": "GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1",
    "url": "https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54",
    "version": "091426.1",
}
STATES = ["PRODUCT_OWNER_ACTION_PENDING", "ECOSYSTEM_CHANGE_COMPLETE", "IMPLEMENTATION_BLOCKED",
          "PROMOTION_CHECKPOINT_REQUIRED"]
CONDITIONS = {
    "PRODUCT_OWNER_ACTION_PENDING": (
        "product_owner_action_pending",
        "the session waits on Nathan: an ANALYZE or PLAN section returned for approval, or an EXECUTE step that is "
        "Nathan's, such as a merge or an install; name the action, where it is recorded and how the session will "
        "verify it; the Modification continues only in its own next mode after Nathan's recorded approval; no "
        "handoff to any prompt"),
    "ECOSYSTEM_CHANGE_COMPLETE": (
        "maintenance_complete_terminal",
        "the Modification is applied and verified; return the read-back Modification record to Nathan"),
    "IMPLEMENTATION_BLOCKED": (
        "implementation_blocked",
        "a real blocker; return its exact statement, evidence, owner and recovery point to Nathan"),
    "PROMOTION_CHECKPOINT_REQUIRED": (
        "promotion_checkpoint_required",
        "a control-layer action is outstanding; return it to Nathan without treating general change authority as "
        "promotion approval"),
}
MEMBER_RULE = ("54 successor runtime members + the GCFPE-MGMT-10 successor (D20 three-mode body); no additions or "
               "removals")


# Observed in the producer bodies, not measurable from branch text (QA-70's and ESC-40's approving branches do
# not name the addendum): carried from the selected 091426.1 proofs (docs/graph/parts/global.json). The six bodies
# are unchanged as producers by this Modification; validators and the body guards check the bodies themselves.
OBSERVED_PF10_PRODUCERS = ["CF-C-30", "CF-E-30", "ESC-40", "IA-30", "QA-70", "RS-20"]
URL_RE = re.compile(r"^https://app\.notion\.com/p/[0-9a-f]{32}\?pvs=204$")


def measured_proofs(root: Path) -> dict:
    """The graph's `proofs`, measured from the parts: the claims flowmaster-validate checks, restated for a
    release that adds no member to its baseline."""
    glob_ = _load(root / "global.json")
    parts = [_load(f) for f in sorted((root / "prompts").glob("*.json"))]
    nodes = {p["id"]: p["node"] for p in parts}
    edges = glob_.get("_other_edges", []) + [e for p in parts for e in p["edges"]]
    boundary = set(glob_["boundary_nodes"])
    baseline_ids = {n["predecessor"]["title"].split(" \u2014 ")[0] for n in nodes.values()}
    producers = list(OBSERVED_PF10_PRODUCERS)
    unresolved = sorted({e["to"] for e in edges if e["to"] not in nodes and e["to"] not in boundary})
    return {
        "PR-35_same_r1_row_as_PR-30": nodes["PR-35"]["r1_mapping"] == nodes["PR-30"]["r1_mapping"],
        "all_candidate_urls_are_observed_direct_notion_urls": all(URL_RE.match(n["candidate_url"]) for n in nodes.values()),
        "all_edge_endpoints_resolved": not unresolved,
        "baseline_ids_retained": baseline_ids <= set(nodes) and len(baseline_ids) == glob_["baseline"]["member_count"],
        "boundary_nodes_counted_as_members": bool(boundary & set(nodes)),
        "candidate_node_count": len(nodes),
        "candidate_url_placeholder_count": sum(1 for n in nodes.values() if not URL_RE.match(n["candidate_url"])),
        "observed_pf10_producers": producers,
        "pf10_producer_set_exact": producers == sorted(glob_["pf10_addendum_contract"]["exact_producer_set"]),
        "prompt_inbound_edges_to_PR-50": sum(1 for e in edges if e["to"] == "PR-50" and e["from_kind"] == "prompt"),
        "sole_added_node": sorted(set(nodes) - baseline_ids),
        "unique_node_ids": len(parts) == len(nodes),
        "unresolved_edges": unresolved,
    }


def node_values(url: str) -> dict:
    return {
        "candidate_url": url,
        "candidate_version": "100926.1",
        "title": "GCFPE-MGMT-10 — Manage an Ecosystem Change — 100926.1",
        "native_function": ("Manage one ecosystem Modification from request to applied result through three explicit "
                            "modes, ANALYZE, PLAN and EXECUTE, stopping at merge and install, which are Nathan's."),
        "output_artifacts": ["GCFPE_MODIFICATION_RECORD"],
        "result_states": list(STATES),
        "predecessor": dict(PREDECESSOR),
    }


def edge() -> dict:
    return {
        "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
        "automatic": False,
        "from": MGMT,
        "from_kind": "prompt",
        "immediate": True,
        "route_branches": [
            {"applicable_states": [s], "branch_id": CONDITIONS[s][0], "condition": CONDITIONS[s][1],
             "next_prompt_handoff_count": 0, "public_result": True, "route_kind": "NATIVE_RESULT",
             "route_steps": [], "source_evidence": dict(SRC), "state": s, "terminal_for_invocation": True}
            for s in STATES],
        "state_predicates": sorted(STATES),
        "to": "NATHAN_TERMINAL_RETURN",
        "to_kind": "boundary",
        "transport": "TERMINAL_RETURN_NO_HANDOFF",
    }


def _load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _write(p: Path, obj) -> None:
    p.write_text(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


def planned_part(part: dict, url: str) -> dict:
    out = copy.deepcopy(part)
    out["node"].update(node_values(url))
    out["edges"] = [edge()]
    out["state_route_order"] = [CONDITIONS[s][0] for s in STATES]
    out["state_routes_extra"] = []
    return out


def apply(parts_dir: str, url: str) -> int:
    root = Path(parts_dir)
    pp, gp = root / "prompts" / f"{MGMT}.json", root / "global.json"
    part, glob_ = _load(pp), _load(gp)
    new_part = planned_part(part, url)
    new_part["edge_indices"] = part["edge_indices"][:1]  # reindex owns the values; one edge remains
    changed = []
    if {k: v for k, v in new_part.items() if k != "edge_indices"} != {k: v for k, v in part.items() if k != "edge_indices"}:
        _write(pp, new_part)
        changed.append(str(pp.relative_to(root)))
    if glob_["candidate"]["member_rule"] != MEMBER_RULE:
        glob_["candidate"]["member_rule"] = MEMBER_RULE
        _write(gp, glob_)
        changed.append("global.json")
    proofs = measured_proofs(root)
    if glob_.get("proofs") != proofs:
        glob_ = _load(gp)
        glob_["proofs"] = proofs
        _write(gp, glob_)
        changed.append("global.json:proofs")
    print(json.dumps({"applied": changed, "unchanged": not changed}))
    return 0


def flip(src: str, dst: str) -> int:
    s, d = Path(src), Path(dst)
    if d.exists():
        sys.exit(f"flip: {d} exists")
    shutil.copytree(s, d)
    g = _load(d / "global.json")
    g["selection_status"] = "SELECTED_PRODUCTION"
    _write(d / "global.json", g)
    for f in sorted((d / "prompts").glob("*.json")):
        p = _load(f)
        p["node"]["lifecycle"] = "SELECTED_PRODUCTION"
        _write(f, p)
    print(json.dumps({"flipped": str(d), "parts": 1 + len(list((d / 'prompts').glob('*.json')))}))
    return 0


def _strip(obj, flipped: bool, is_global: bool):
    obj = copy.deepcopy(obj)
    if is_global:
        obj.pop("_other_edge_indices", None)
        if flipped:
            obj.pop("selection_status", None)
    else:
        obj.pop("edge_indices", None)
        if flipped:
            obj["node"].pop("lifecycle", None)
    return obj


def check_errors(parts_dir: str, base_dir: str, flipped: bool = False) -> list[str]:
    root, base = Path(parts_dir), Path(base_dir)
    errors = []
    names = sorted(f.name for f in (root / "prompts").glob("*.json"))
    if names != sorted(f.name for f in (base / "prompts").glob("*.json")):
        return ["PART_SET_CHANGED"]
    g, bg = _load(root / "global.json"), _load(base / "global.json")
    if g["candidate"]["member_rule"] != MEMBER_RULE:
        errors.append("MEMBER_RULE")
    if flipped and g.get("selection_status") != "SELECTED_PRODUCTION":
        errors.append("FLIP_GLOBAL")
    exp_g = _strip(bg, flipped, True)
    exp_g["candidate"]["member_rule"] = MEMBER_RULE
    exp_g["proofs"] = g.get("proofs")
    if _strip(g, flipped, True) != exp_g:
        errors.append("GLOBAL_UNPLANNED_CHANGE")
    if g.get("proofs") != measured_proofs(root):
        errors.append("PROOFS_NOT_MEASURED")
    for name in names:
        p, bp = _load(root / "prompts" / name), _load(base / "prompts" / name)
        if flipped and p["node"].get("lifecycle") != "SELECTED_PRODUCTION":
            errors.append(f"FLIP_NODE:{p['id']}")
        if len(p.get("edge_indices", [])) != len(p.get("edges", [])):
            errors.append(f"EDGE_INDEX_COUNT:{p['id']}")
        if p["id"] == MGMT:
            url = p["node"].get("candidate_url", "")
            if not (url.startswith("https://app.notion.com/p/") and url.endswith("?pvs=204")):
                errors.append("MGMT10_URL_FORM")
            if _strip(p, flipped, False) != _strip(planned_part(bp, url), flipped, False):
                errors.append("MGMT10_NOT_PLANNED")
        elif _strip(p, flipped, False) != _strip(bp, flipped, False):
            errors.append(f"UNPLANNED_CHANGE:{p['id']}")
    return errors


def check(parts_dir: str, base_dir: str, *flags: str) -> int:
    errs = check_errors(parts_dir, base_dir, "--flipped" in flags)
    print(json.dumps({"ok": not errs, "errors": errs}))
    return 0 if not errs else 1


def selftest(base_dir: str, scratch: str, graph_parts: str) -> int:
    url = "https://app.notion.com/p/3e34590a05eb811b93d2da9b4ef8106d?pvs=204"
    work = Path(scratch) / "selftest"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    def fresh(name: str) -> Path:
        d = work / name
        shutil.copytree(base_dir, d)
        apply(str(d), url)
        subprocess.run([sys.executable, graph_parts, "reindex", str(d)], check=True, capture_output=True)
        return d

    rows = {}
    clean = fresh("clean")
    rows["clean_apply_passes"] = check_errors(str(clean), base_dir) == []
    before = {f.name: f.read_bytes() for f in (clean / "prompts").glob("*.json")}
    apply(str(clean), url)
    rows["second_apply_changes_nothing"] = before == {f.name: f.read_bytes() for f in (clean / "prompts").glob("*.json")}
    flip(str(clean), str(work / "flipped"))
    rows["clean_flip_passes"] = check_errors(str(work / "flipped"), base_dir, True) == []
    rows["unflipped_fails_flipped_check"] = bool(check_errors(str(clean), base_dir, True))

    def injected(name: str, mutate) -> bool:
        d = fresh(name)
        mutate(d)
        return bool(check_errors(str(d), base_dir))

    def mut_json(rel: str, fn):
        def go(d: Path):
            p = d / rel
            obj = _load(p)
            fn(obj)
            _write(p, obj)
        return go

    rows["rejects_other_part_change"] = injected("inj1", mut_json("prompts/PR-10.json",
                                               lambda o: o["node"].__setitem__("title", o["node"]["title"] + " x")))
    rows["rejects_kept_pr10_edge"] = injected("inj2", mut_json(f"prompts/{MGMT}.json",
                                            lambda o: o["edges"].append(copy.deepcopy(o["edges"][0]))))
    rows["rejects_missing_state"] = injected("inj3", mut_json(f"prompts/{MGMT}.json",
                                           lambda o: o["node"]["result_states"].remove("PRODUCT_OWNER_ACTION_PENDING")))
    rows["rejects_global_change"] = injected("inj4", mut_json("global.json",
                                           lambda o: o["handoff_contract"].__setitem__("first_line", "X")))
    rows["rejects_old_member_rule"] = injected("inj5", mut_json("global.json",
                                             lambda o: o["candidate"].__setitem__("member_rule", "old")))
    rows["rejects_bad_url"] = injected("inj6", mut_json(f"prompts/{MGMT}.json",
                                     lambda o: o["node"].__setitem__("candidate_url", "PLACEHOLDER")))
    rows["rejects_stale_proofs"] = injected("inj7", mut_json("global.json",
                                          lambda o: o["proofs"].__setitem__("sole_added_node", ["PR-35"])))
    rows["proofs_describe_no_added_member"] = (_load(clean / "global.json")["proofs"]["sole_added_node"] == []
                                               and _load(clean / "global.json")["proofs"]["pf10_producer_set_exact"])
    ok = all(rows.values())
    print(json.dumps({"mode": "selftest", "rows": rows, "ok": ok}))
    return 0 if ok else 1


COMMANDS = {"apply": apply, "flip": flip, "check": check, "selftest": selftest}

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]](*sys.argv[2:]))
