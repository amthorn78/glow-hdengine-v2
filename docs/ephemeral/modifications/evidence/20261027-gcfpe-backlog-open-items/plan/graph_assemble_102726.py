#!/usr/bin/env python3
"""Candidate and production graph-part assembly for GCFPE-20261027.1 / 102726.1 / 56
(MODIFICATION-20261027-gcfpe-backlog-open-items, PART-13 and PART-24; adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/graph_assemble.py per W7 tooling).

  graph_assemble_102726.py apply <parts-dir> <successor-map> [--graph-edits F] [--members-tsv F] [--stand-in-ok]
        on a copy of main's docs/graph/parts: every normalized graph edit in plan/graph-edits.json (each refused
        unless the value at its pointer equals its recorded old value; the whole application is refused, with
        nothing written, if any edit is refused, so a second application is refused), then the head rules: uniform
        UNSELECTED_CANDIDATE lifecycle (C-11), successor node heads from the map (C-1; never typed), CL-05's URL from
        the map, and global.json `proofs` measured from the parts. Run the installed `graph_parts.py reindex` next.
  graph_assemble_102726.py flip <src-parts-dir> <dst-parts-dir>
        the production parts: a copy whose only changes are selection_status and every node.lifecycle
        (SELECTED_PRODUCTION) and global.json's `_prologue` (the selected header, GE-W7-12).
  graph_assemble_102726.py check <parts-dir> <main-parts-dir> <successor-map> [--flipped] [--stand-in-ok] [...]
        after reindex: the parts equal main's parts with exactly the planned edits and rules applied (and, with
        --flipped, the flip); edge_indices are exempt from the comparison but must be exactly 0..N-1, each once.
  graph_assemble_102726.py routes <graph.md>
        Q3's script over a build: 56 nodes, 240 edges, 56 state_routes, no QA-120 edge to CL-C-10 or CL-E-10, no
        DOC-20 edge to PR-40, IA-40 REDLINE_INCOMPLETE routes to IA-30 only, CL-C-10 and CL-E-10 DO_NOT_CLOSE reach
        CL-05, and the measured proofs.
  graph_assemble_102726.py selftest <main-parts-dir> <successor-map> <scratch> <graph_parts.py> [--stand-in-ok]
        check() passes on a clean apply and flip and fails on each injected regression.

Every receipt says whether a stand-in map was used. Writes only the directories it is given. Run with
PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("successor_map_102726", HERE / "successor_map_102726.py")
SM = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(SM)

NEW_REL, NEW_VER, OLD_REL, OLD_VER = "GCFPE-20261027.1", "102726.1", "GCFPE-20261009.1", "100926.1"
CANDIDATE, PRODUCTION = "UNSELECTED_CANDIDATE", "SELECTED_PRODUCTION"
OBSERVED_PF10_PRODUCERS = ["CF-C-30", "CF-E-30", "ESC-40", "IA-30", "QA-70", "RS-20"]
URL_RE = re.compile(r"^https://app\.notion\.com/p/[0-9a-f]{32}\?pvs=204$")
MARKER = "@MAP_URL:CL-05"
DEFAULT_EDITS = HERE / "graph-edits.json"
DEFAULT_TSV = HERE / "members-100926.1.tsv"


def _load(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _dump(obj) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def read_parts(root: Path) -> dict:
    out = {"global.json": _load(root / "global.json")}
    for f in sorted((root / "prompts").glob("*.json")):
        out["prompts/" + f.name] = _load(f)
    return out


def write_parts(root: Path, parts: dict) -> list[str]:
    changed = []
    for rel, obj in parts.items():
        p = root / rel
        text = _dump(obj)
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8")
            changed.append(rel)
    return changed


def _opts(args) -> dict:
    o = {"edits": str(DEFAULT_EDITS), "tsv": str(DEFAULT_TSV), "stand_in_ok": "--stand-in-ok" in args,
         "flipped": "--flipped" in args}
    for flag, key in (("--graph-edits", "edits"), ("--members-tsv", "tsv")):
        if flag in args:
            o[key] = args[args.index(flag) + 1]
    return o


def _get(obj, ptr):
    for k in ptr:
        obj = obj[k]
    return obj


def measured_proofs(parts: dict, base_ids: set) -> dict:
    """The graph's `proofs`, measured from the parts. Baseline ids are main's 55 part ids (CL-05's predecessor is
    null, so predecessor titles cannot supply them; W7 tooling)."""
    g = parts["global.json"]
    prompts = [v for k, v in parts.items() if k.startswith("prompts/")]
    nodes = {p["id"]: p["node"] for p in prompts}
    edges = g.get("_other_edges", []) + [e for p in prompts for e in p["edges"]]
    boundary = set(g["boundary_nodes"])
    unresolved = sorted({e["to"] for e in edges if e["to"] not in nodes and e["to"] not in boundary})
    producers = list(OBSERVED_PF10_PRODUCERS)
    return {
        "PR-35_same_r1_row_as_PR-30": nodes["PR-35"]["r1_mapping"] == nodes["PR-30"]["r1_mapping"],
        "all_candidate_urls_are_observed_direct_notion_urls": all(URL_RE.match(n["candidate_url"]) for n in nodes.values()),
        "all_edge_endpoints_resolved": not unresolved,
        "baseline_ids_retained": base_ids <= set(nodes) and len(base_ids) == g["baseline"]["member_count"],
        "boundary_nodes_counted_as_members": bool(boundary & set(nodes)),
        "candidate_node_count": len(nodes),
        "candidate_url_placeholder_count": sum(1 for n in nodes.values() if not URL_RE.match(n["candidate_url"])),
        "observed_pf10_producers": producers,
        "pf10_producer_set_exact": producers == sorted(g["pf10_addendum_contract"]["exact_producer_set"]),
        "prompt_inbound_edges_to_PR-50": sum(1 for e in edges if e["to"] == "PR-50" and e["from_kind"] == "prompt"),
        "sole_added_node": sorted(set(nodes) - base_ids),
        "unique_node_ids": len(prompts) == len(nodes),
        "unresolved_edges": unresolved,
    }


class Refused(Exception):
    pass


def plan(base: dict, ge: dict, smap: dict) -> dict:
    """main's parts -> the planned candidate parts (pure; raises Refused)."""
    out = copy.deepcopy(base)
    g = out["global.json"]
    if g["candidate"]["release"] == NEW_REL or "prompts/CL-05.json" in out:
        raise Refused(["ALREADY_APPLIED"])
    base_ids = {v["id"] for k, v in base.items() if k.startswith("prompts/")}
    if len(base_ids) != 55:
        raise Refused([f"BASE_NOT_55:{len(base_ids)}"])
    refused = []
    edits = [e for e in ge["edits"] if e["op"] != "remove"]
    edits += sorted((e for e in ge["edits"] if e["op"] == "remove"), key=lambda e: (e["file"], e["pointer"]),
                    reverse=True)
    for e in edits:
        if e["op"] == "new_file":
            if e["file"] in out:
                refused.append(f"{e['id']}:FILE_EXISTS")
                continue
            out[e["file"]] = copy.deepcopy(e["new"])
            continue
        doc = out.get(e["file"])
        if doc is None:
            refused.append(f"{e['id']}:NO_FILE")
            continue
        for gptr, gval in e.get("guard", []):
            try:
                if _get(doc, gptr) != gval:
                    refused.append(f"{e['id']}:GUARD")
            except (KeyError, IndexError, TypeError):
                refused.append(f"{e['id']}:GUARD")
        try:
            parent = _get(doc, e["pointer"][:-1]) if e["pointer"] else None
            cur = _get(doc, e["pointer"])
        except (KeyError, IndexError, TypeError):
            refused.append(f"{e['id']}:NO_POINTER")
            continue
        if e["op"] == "append":
            if not isinstance(cur, list) or len(cur) != e["old_length"]:
                refused.append(f"{e['id']}:OLD_LENGTH")
                continue
            cur.append(copy.deepcopy(e["new"]))
        elif cur != e["old"]:
            refused.append(f"{e['id']}:OLD_VALUE")
            continue
        elif e["op"] == "replace":
            parent[e["pointer"][-1]] = copy.deepcopy(e["new"])
        elif e["op"] == "remove":
            del parent[e["pointer"][-1]]
            if len(e["pointer"]) == 2 and e["pointer"][0] == "edges":
                del doc["edge_indices"][e["pointer"][1]]
        else:
            refused.append(f"{e['id']}:OP")
    if refused:
        raise Refused(refused)
    # GE-W7-07 (C-11): uniform candidate lifecycle.
    for k, v in out.items():
        if k.startswith("prompts/"):
            v["node"]["lifecycle"] = CANDIDATE
    # GE-W7-08 (C-1): node heads from the map.
    members = smap["members"]
    if {k[len("prompts/"):-5] for k in out if k.startswith("prompts/")} != set(members):
        raise Refused(["MAP_MEMBER_SET_NOT_PART_SET"])
    for pid, row in members.items():
        node = out[f"prompts/{pid}.json"]["node"]
        if row["disposition"] == "SUCCESSOR":
            b = base[f"prompts/{pid}.json"]["node"]
            b_id = b["candidate_url"][len("https://app.notion.com/p/"):][:32]
            if row["predecessor_page_id"] != b_id or b["candidate_version"] != OLD_VER:
                raise Refused([f"MAP_PREDECESSOR_NOT_MAIN:{pid}"])
            node["predecessor"] = {"notion_page_id": b_id, "release": OLD_REL, "title": b["title"],
                                   "url": SM.url(b_id), "version": OLD_VER}
            node["title"] = row["title"]
            node["candidate_url"] = SM.url(row["page_id"])
            node["candidate_version"] = NEW_VER
        elif row["disposition"] == "KEPT":
            if node["candidate_url"] != SM.url(row["page_id"]):
                raise Refused([f"MAP_KEPT_PAGE_NOT_MAIN:{pid}"])
        elif row["disposition"] == "ADDED":
            if node["candidate_url"] != MARKER or node["title"] != row["title"]:
                raise Refused([f"MAP_ADDED:{pid}"])
            node["candidate_url"] = SM.url(row["page_id"])
    # GE-W7-11: measured proofs, which must show what the plan expects.
    proofs = measured_proofs(out, base_ids)
    exp = next(r for r in ge["rules"] if r["id"] == "GE-W7-11")["expected"]
    bad = [k for k, v in exp.items() if proofs.get(k) != v]
    if bad:
        raise Refused([f"PROOFS:{k}" for k in bad])
    g["proofs"] = proofs
    return out


def flip_parts(parts: dict, ge: dict) -> dict:
    out = copy.deepcopy(parts)
    out["global.json"]["selection_status"] = PRODUCTION
    out["global.json"]["_prologue"] = next(r for r in ge["rules"] if r["id"] == "GE-W7-12")["selected_prologue"]
    for k, v in out.items():
        if k.startswith("prompts/"):
            v["node"]["lifecycle"] = PRODUCTION
    return out


def _map(path: str, o: dict) -> dict:
    return SM.load(path, o["tsv"], o["stand_in_ok"])


def apply(parts_dir: str, map_path: str, *args: str) -> int:
    o = _opts(args)
    root = Path(parts_dir)
    smap = _map(map_path, o)
    ge = _load(Path(o["edits"]))
    try:
        new = plan(read_parts(root), ge, smap)
    except Refused as exc:
        print(json.dumps({"apply_ok": False, "refused": exc.args[0], "written": [],
                          "stand_in_used": smap.get("stand_in") is True}))
        return 1
    changed = write_parts(root, new)
    print(json.dumps({"apply_ok": True, "written": len(changed), "edits_applied": len(ge["edits"]),
                      "stand_in_used": smap.get("stand_in") is True, "next": "graph_parts.py reindex"}))
    return 0


def flip(src: str, dst: str, *args: str) -> int:
    o = _opts(args)
    s, d = Path(src), Path(dst)
    if d.exists():
        sys.exit(f"flip: {d} exists")
    shutil.copytree(s, d)
    parts = read_parts(d)
    write_parts(d, flip_parts(parts, _load(Path(o["edits"]))))
    print(json.dumps({"flip_ok": True, "flipped": str(d), "parts": len(parts)}))
    return 0


def _no_idx(rel: str, obj):
    obj = copy.deepcopy(obj)
    obj.pop("_other_edge_indices" if rel == "global.json" else "edge_indices", None)
    return obj


def check_errors(parts_dir: str, base_dir: str, smap: dict, ge: dict, flipped: bool) -> list[str]:
    actual, base = read_parts(Path(parts_dir)), read_parts(Path(base_dir))
    try:
        exp = plan(base, ge, smap)
    except Refused as exc:
        return [f"BASE_NOT_PLANNABLE:{exc.args[0]}"]
    if flipped:
        exp = flip_parts(exp, ge)
    if sorted(actual) != sorted(exp):
        return [f"PART_SET_CHANGED:{sorted(set(actual) ^ set(exp))}"]
    errs = []
    for rel in sorted(exp):
        if _no_idx(rel, actual[rel]) != _no_idx(rel, exp[rel]):
            a, x = _no_idx(rel, actual[rel]), _no_idx(rel, exp[rel])
            keys = sorted(k for k in set(a) | set(x) if a.get(k) != x.get(k))
            errs.append(f"UNPLANNED:{rel}:{keys}")
    g = actual["global.json"]
    seen = list(g.get("_other_edge_indices") or [])
    total = len(g.get("_other_edges", []))
    for rel, p in actual.items():
        if rel.startswith("prompts/"):
            if len(p.get("edge_indices") or []) != len(p["edges"]):
                errs.append(f"EDGE_INDEX_COUNT:{p['id']}")
            seen += p.get("edge_indices") or []
            total += len(p["edges"])
    if sorted(seen) != list(range(total)):
        errs.append("EDGE_INDICES_NOT_REINDEXED")
    base_ids = {v["id"] for k, v in base.items() if k.startswith("prompts/")}
    if g.get("proofs") != measured_proofs(actual, base_ids):
        errs.append("PROOFS_NOT_MEASURED")
    want = PRODUCTION if flipped else CANDIDATE
    if g.get("selection_status") != want:
        errs.append("SELECTION_STATUS")
    for rel, p in actual.items():
        if rel.startswith("prompts/") and p["node"].get("lifecycle") != want:
            errs.append(f"LIFECYCLE:{p['id']}")
    return errs


def check(parts_dir: str, base_dir: str, map_path: str, *args: str) -> int:
    o = _opts(args)
    smap = _map(map_path, o)
    errs = check_errors(parts_dir, base_dir, smap, _load(Path(o["edits"])), o["flipped"])
    print(json.dumps({"check_ok": not errs, "flipped": o["flipped"], "errors": errs,
                      "stand_in_used": smap.get("stand_in") is True}))
    return 0 if not errs else 1


def graph_obj(path: str):
    raw = Path(path).read_text(encoding="utf-8")
    lines = raw.split("\n")
    s = next(i for i, l in enumerate(lines) if l.strip() == "```json")
    e = max(i for i, l in enumerate(lines) if l.strip() == "```")
    block = ("\n".join(lines[s + 1:e]) + "\n").encode("utf-8")
    return json.loads(block), block


def route_flags(g: dict) -> dict:
    E = g["edges"]

    def branches(frm, state=None):
        return [(e["to"], b) for e in E if e["from"] == frm for b in e["route_branches"]
                if state is None or b.get("state") == state or state in (b.get("applicable_states") or [])]
    ia40 = sorted({to for to, _ in branches("IA-40", "REDLINE_INCOMPLETE")})
    return {
        "nodes_56": len(g["nodes"]) == 56,
        "edges_240": len(E) == 240,
        "state_routes_56": len(g["state_routes"]) == 56,
        "no_qa120_edge_to_cl_c10_or_cl_e10": not any(e["from"] == "QA-120" and e["to"] in ("CL-C-10", "CL-E-10")
                                                    for e in E),
        "qa120_pass_to_cl05": sorted(to for to, b in branches("QA-120", "PASS")) == ["CL-05", "CL-05"],
        "no_doc20_edge_to_pr40": not any(e["from"] == "DOC-20" and e["to"] == "PR-40" for e in E),
        "ia40_redline_incomplete_routes_to_ia30_only": ia40 == ["IA-30"],
        "cl_c10_do_not_close_reaches_cl05": "CL-05" in {to for to, _ in branches("CL-C-10", "DO_NOT_CLOSE")},
        "cl_e10_do_not_close_reaches_cl05": "CL-05" in {to for to, _ in branches("CL-E-10", "DO_NOT_CLOSE")},
        "cl05_exits_cl_c10_cl_e10_and_terminal": sorted({e["to"] for e in E if e["from"] == "CL-05"})
        == ["CL-C-10", "CL-E-10", "NATHAN_TERMINAL_RETURN"],
        "proofs_sole_added_node_cl05": g["proofs"]["sole_added_node"] == ["CL-05"],
        "proofs_candidate_node_count_56": g["proofs"]["candidate_node_count"] == 56,
        "proofs_unresolved_edges_empty": g["proofs"]["unresolved_edges"] == [],
        "candidate_head": (g["candidate"]["release"], g["candidate"]["version_family"], g["candidate"]["member_count"])
        == (NEW_REL, NEW_VER, 56),
        "baseline_head": (g["baseline"]["release"], g["baseline"]["version_family"], g["baseline"]["member_count"])
        == (OLD_REL, OLD_VER, 55),
        "r1_pins": (g["protected_identities"]["r1_rows"], g["protected_identities"]["r1_core_rows"],
                    g["protected_identities"]["r1_material_rows"], g["protected_identities"]["r1_oracle_sha256"])
        == (47, 26, 21, "f1b221e91cd3c22ce9923d555671bce0e7af25335b69dabab60e097f3fa8d46d"),
    }


def routes(graph_md: str) -> int:
    g, block = graph_obj(graph_md)
    flags = route_flags(g)
    ok = all(flags.values())
    print(json.dumps({"routes_ok": ok, "flags": flags, "nodes": len(g["nodes"]), "edges": len(g["edges"]),
                      "state_routes": len(g["state_routes"]), "bytes": len(block),
                      "sha256": hashlib.sha256(block).hexdigest(), "selection_status": g["selection_status"]}))
    return 0 if ok else 1


def selftest(base_dir: str, map_path: str, scratch: str, graph_parts: str, *args: str) -> int:
    o = _opts(args)
    smap = _map(map_path, o)
    ge = _load(Path(o["edits"]))
    work = Path(scratch) / "selftest"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    quiet = {"stdout": subprocess.DEVNULL}

    def fresh(name: str) -> Path:
        d = work / name
        shutil.copytree(base_dir, d)
        write_parts(d, plan(read_parts(d), ge, smap))
        subprocess.run([sys.executable, graph_parts, "reindex", str(d)], check=True, capture_output=True)
        return d

    def errs(d: Path, flipped=False) -> list[str]:
        return check_errors(str(d), base_dir, smap, ge, flipped)

    rows = {}
    clean = fresh("clean")
    rows["clean_apply_passes"] = errs(clean) == []
    try:
        plan(read_parts(clean), ge, smap)
        rows["second_apply_refused"] = False
    except Refused as exc:
        rows["second_apply_refused"] = exc.args[0] == ["ALREADY_APPLIED"]
    # an edit whose old value does not match the base is refused, and nothing is written
    stale = work / "stale-base"
    shutil.copytree(base_dir, stale)
    p = stale / "prompts" / "QA-80.json"
    obj = _load(p)
    obj["edges"][1]["route_branches"][0]["condition"] += " (drift)"
    p.write_text(_dump(obj), encoding="utf-8")
    before = {f.name: f.read_bytes() for f in (stale / "prompts").glob("*.json")}
    try:
        plan(read_parts(stale), ge, smap)
        rows["old_value_mismatch_refused"] = False
    except Refused as exc:
        rows["old_value_mismatch_refused"] = exc.args[0] == ["GE-W4-07:OLD_VALUE"]
    rows["refused_apply_writes_nothing"] = before == {f.name: f.read_bytes() for f in (stale / "prompts").glob("*.json")}
    flip(str(clean), str(work / "flipped"), "--graph-edits", o["edits"])
    rows["clean_flip_passes"] = errs(work / "flipped", True) == []
    rows["unflipped_fails_flipped_check"] = bool(errs(clean, True))
    rows["flipped_fails_candidate_check"] = bool(errs(work / "flipped"))
    rows["flipped_prologue_is_selected"] = ("selection_status: SELECTED_PRODUCTION"
                                            in _load(work / "flipped" / "global.json")["_prologue"])

    def injected(name: str, rel: str, fn) -> bool:
        d = fresh(name)
        obj = _load(d / rel)
        fn(obj)
        (d / rel).write_text(_dump(obj), encoding="utf-8")
        return bool(errs(d))

    def unapply(obj):  # a missing graph edit: QA-120's CRD pass still goes to CL-C-10
        obj["edges"][0]["to"] = "CL-C-10"

    rows["rejects_extra_edited_field"] = injected("i1", "prompts/PR-10.json",
                                                  lambda o_: o_["node"].__setitem__("native_function", "x"))
    rows["rejects_missing_graph_edit"] = injected("i2", "prompts/QA-120.json", unapply)
    rows["rejects_node_with_old_title"] = injected("i3", "prompts/PR-10.json", lambda o_: o_["node"].__setitem__(
        "title", o_["node"]["predecessor"]["title"]))
    rows["rejects_predecessor_not_from_map"] = injected("i4", "prompts/PR-10.json", lambda o_: o_["node"][
        "predecessor"].__setitem__("notion_page_id", "0" * 32))
    rows["rejects_selected_lifecycle_in_candidate"] = injected("i5", "prompts/PR-10.json", lambda o_: o_[
        "node"].__setitem__("lifecycle", PRODUCTION))
    rows["rejects_global_change"] = injected("i6", "global.json", lambda o_: o_["handoff_contract"].__setitem__(
        "first_line", "X"))
    rows["rejects_stale_proofs"] = injected("i7", "global.json", lambda o_: o_["proofs"].__setitem__(
        "sole_added_node", []))
    rows["rejects_kept_member_given_successor_head"] = injected("i8", "prompts/GCFPE-MGMT-10.json", lambda o_: o_[
        "node"].__setitem__("candidate_version", NEW_VER))
    rows["rejects_cl05_marker_left"] = injected("i9", "prompts/CL-05.json", lambda o_: o_["node"].__setitem__(
        "candidate_url", MARKER))
    d = fresh("i10")
    (d / "prompts" / "CL-05.json").unlink()
    rows["rejects_missing_cl05"] = bool(errs(d))
    shutil.copytree(base_dir, work / "i11-unreindexed")
    write_parts(work / "i11-unreindexed", plan(read_parts(work / "i11-unreindexed"), ge, smap))
    rows["rejects_unreindexed_parts"] = "EDGE_INDICES_NOT_REINDEXED" in errs(work / "i11-unreindexed")
    # Q3's route script fires on each injected route regression in a build of the clean parts.
    subprocess.run([sys.executable, graph_parts, "build", str(clean), str(work / "clean.md")], check=True, **quiet)
    g0, _ = graph_obj(str(work / "clean.md"))
    rows["routes_clean_build_passes"] = all(route_flags(g0).values())

    def route_inj(fn, flag) -> bool:
        h = copy.deepcopy(g0)
        fn(h)
        return route_flags(h)[flag] is False

    rows["routes_rejects_qa120_to_cl_c10"] = route_inj(lambda h: next(
        e for e in h["edges"] if e["from"] == "QA-120" and e["to"] == "CL-05").__setitem__("to", "CL-C-10"),
        "no_qa120_edge_to_cl_c10_or_cl_e10")
    rows["routes_rejects_doc20_to_pr40"] = route_inj(lambda h: h["edges"].append(
        {"from": "DOC-20", "to": "PR-40", "route_branches": []}), "no_doc20_edge_to_pr40")
    rows["routes_rejects_ia40_terminal_redline"] = route_inj(lambda h: next(
        e for e in h["edges"] if e["from"] == "IA-40" and e["to"] == "IA-30").__setitem__(
        "to", "ACTUAL_OWNER_TERMINAL_RETURN"), "ia40_redline_incomplete_routes_to_ia30_only")
    rows["routes_rejects_239_edges"] = route_inj(lambda h: h["edges"].pop(), "edges_240")
    ok = all(rows.values())
    shutil.rmtree(work)
    print(json.dumps({"mode": "selftest", "rows": rows, "selftest_ok": ok,
                      "stand_in_used": smap.get("stand_in") is True}))
    return 0 if ok else 1


COMMANDS = {"apply": apply, "flip": flip, "check": check, "routes": routes, "selftest": selftest}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]](*sys.argv[2:]))
