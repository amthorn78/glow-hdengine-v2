#!/usr/bin/env python3
"""PART-10 (ITEM-22) gate: NAM-002, lane parents and parent titles over a snapshot of the LIVE 091426.1 hub child
lists. No prompt body is read.

EXECUTE writes the child-list file from six Notion fetches of the hub pages (control pages, not prompt bodies):

  {"captured_at": "<UTC>", "hubs": [{"id": "<32-hex hub id>", "title": "<hub title>", "fetched": "<as-of stamp>",
    "children": [{"id": "<32-hex child page id>", "title": "<child title>"}, ...]}, ...]}

Every hub must carry its fetched page title (a non-empty string); a hub without one is unusable input (exit 2).

Check 1, NAM-002 (the governance audit's own rule). build_snapshot() turns the child lists into the governance
audit's snapshot shape, one source per registry row:
  {"source_id": <row notion_page_id>, "kind": "notion_page", "complete": true, "in_scope": true,
   "title": <observed child title>, "parent": <hub id under which the page is listed>}
No source carries a "path", so the audit reads no text and evaluates no assertion (D22); NAM-002 compares
"parent" with the row's expected_parent_id as a plain string (audit_workspace_governance.py:604), NAM-001
compares "title" with expected_title. A row whose page is under no hub gets no source (the audit then raises
INV-001 for it); a page listed under two hubs stops the run.

Check 2, lane parents (P-63). For each of the registry's lanes, the hub that holds the lane's rows is observed from
the same child lists (the hub under which each row's notion_page_id is listed). The lane's notion_parent_id must be
exactly that hub: one finding per lane whose rows sit under no fetched hub, under more than one hub, or under a
hub other than its notion_parent_id (and one per lane with no row at all).

Check 3, parent titles (P-63). Every lane notion_parent_title and every row expected_parent_title must equal the
fetched title of the hub it refers to: for a lane, the hub observed holding its rows; for a row, the hub observed
holding its page (when there is none, the hub its notion_parent_id / expected_parent_id names, if it was fetched).
Findings are one per hub (all of that hub's differing references listed in it), so one wrong hub title is exactly
one finding; references whose hub cannot be resolved form one more finding (hub null). A row without
expected_parent_title (PR-35) has no reference. The summary also counts references compared and mismatched.

  PYTHONDONTWRITEBYTECODE=1 python3 nam002_live.py <registry.md> <childlist.json>
        [--inject ROW=PARENT | --inject-title HUB=TITLE]
        [--audit-root <amthor-workspace-governance-audit dir>] [--snapshot-out <file>]

Must-fail cases (each checks only its own finding; the two flags are exclusive):
  --inject ROW=PARENT       the snapshot's observed parent of ROW becomes PARENT: exactly one NAM-002, on ROW.
  --inject-title HUB=TITLE  the fetched title of hub HUB becomes TITLE (in memory; the file is not changed):
                            exactly one parent-title finding, on HUB. HUB must be a fetched hub id and TITLE must
                            differ from its fetched title, or the input is unusable (exit 2).
Exit 0 when the run meets its expectation: without an injection, 0 NAM-002, 0 other prompt errors, no unplaced
row, 0 lane-parent findings and 0 parent-title findings; with --inject, exactly one NAM-002, on ROW; with
--inject-title, exactly one parent-title finding, on HUB. Exit 1 otherwise, 2 on unusable input.
"""
import argparse, copy, importlib.util, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
HEX = re.compile(r"^[0-9a-f]{32}$")


def audit_module(root=None):
    path = os.path.join(root, "scripts", "audit_workspace_governance.py") if root else os.path.join(HERE, "wga_scripts", "audit_workspace_governance.py")
    spec = importlib.util.spec_from_file_location("audit_workspace_governance", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def undash(x):
    return str(x).replace("-", "").lower()


def locate(childlist):
    """{hub id: fetched hub title} and {child page id: (hub id, child title)}; a page under two hubs stops the run."""
    hubs, where = {}, {}
    for hub in childlist["hubs"]:
        h = undash(hub["id"])
        if not HEX.match(h):
            raise SystemExit(f"bad hub id {hub['id']!r}")
        hubs[h] = hub.get("title")
        for c in hub["children"]:
            cid = undash(c["id"])
            if cid in where and where[cid][0] != h:
                raise SystemExit(f"page {cid} listed under two hubs: {where[cid][0]} and {h}")
            where[cid] = (h, c.get("title"))
    return hubs, where


def build_snapshot(childlist, registry):
    _, where = locate(childlist)
    sources, unplaced = [], []
    for r in registry["prompts"]:
        pid = r["notion_page_id"]
        if pid not in where:
            unplaced.append(r["prompt_key"])
            continue
        parent, title = where[pid]
        sources.append({"source_id": pid, "kind": "notion_page", "complete": True, "in_scope": True,
                        "title": title, "parent": parent})
    return {"schema_version": "amthor-workspace-governance-snapshot/1.0", "run_id": "PART-10-NAM002",
            "source_count": len(sources), "sources": sources,
            "captured_at": childlist.get("captured_at")}, unplaced


def parent_checks(childlist, registry):
    """Checks 2 and 3 (P-63), from the same child lists; no Notion call, no body."""
    hubs, where = locate(childlist)
    rows_by_lane = {}
    for r in registry["prompts"]:
        rows_by_lane.setdefault(r.get("lane"), []).append(r)
    lane_findings, lane_hub = [], {}
    for lane in registry["lanes"]:
        name, declared = lane["lane"], undash(lane.get("notion_parent_id"))
        rows = rows_by_lane.get(name, [])
        observed = sorted({where[undash(r["notion_page_id"])][0] for r in rows if undash(r["notion_page_id"]) in where})
        unplaced = sorted(r["prompt_key"] for r in rows if undash(r["notion_page_id"]) not in where)
        if len(observed) == 1:
            lane_hub[name] = observed[0]
        if observed != [declared] or not rows:
            lane_findings.append({"check": "LANE_PARENT", "lane": name, "notion_parent_id": declared,
                                  "observed_hubs": observed, "rows": len(rows), "unplaced_rows": unplaced})
    refs = []  # (hub or None, field, registry value)
    for lane in registry["lanes"]:
        if "notion_parent_title" not in lane:
            continue
        h = lane_hub.get(lane["lane"])
        if h is None and undash(lane.get("notion_parent_id")) in hubs:
            h = undash(lane.get("notion_parent_id"))
        refs.append((h, f"lanes[{lane['lane']}].notion_parent_title", lane["notion_parent_title"]))
    for r in registry["prompts"]:
        if "expected_parent_title" not in r:
            continue
        pid = undash(r["notion_page_id"])
        h = where[pid][0] if pid in where else (undash(r.get("expected_parent_id")) if undash(r.get("expected_parent_id")) in hubs else None)
        refs.append((h, f"{r['prompt_key']}.expected_parent_title", r["expected_parent_title"]))
    by_hub = {}
    for h, field, value in refs:
        if h is None or value != hubs.get(h):
            by_hub.setdefault(h, []).append({"field": field, "value": value})
    title_findings = [{"check": "PARENT_TITLE", "hub": h, "fetched_title": hubs.get(h) if h else None,
                       "references": len([1 for x, _, _ in refs if x == h]), "mismatches": m}
                      for h, m in sorted(by_hub.items(), key=lambda kv: (kv[0] is None, kv[0] or ""))]
    return {"lane_findings": lane_findings, "title_findings": title_findings,
            "title_references": {"compared": len(refs), "mismatched": sum(len(m) for m in by_hub.values())}}


MANIFEST = {"AUDIT_RUN_ID": "PART-10-NAM002", "MODE": "TARGETED", "WORKSPACE_SKILL_REGISTRY_ID": "WSR-20260914.1-OBSERVATIONAL",
            "PROJECT_PROFILE_ID": "glow-hde", "PROJECT_PROMPT_REGISTRY_ID": "GCFPE-PCR-20260914.1",
            "NOTION_SCOPE": ["six 091426.1 hub pages (child lists only)"], "SKILL_SCOPE": [], "TARGETS": ["PART-10"],
            "PF_SOURCES": [], "OUTPUT_DESTINATION": "scratch"}
WSR = {"schema_version": "workspace-skill-registry/1.0", "registry_id": "WSR-20260914.1-OBSERVATIONAL", "status": "DRAFT", "skills": []}


def usable(childlist):
    """None when the child list has the documented shape (hub ids, non-empty hub titles, child lists); else why not."""
    if not isinstance(childlist, dict) or not isinstance(childlist.get("hubs"), list) or not childlist["hubs"]:
        return "childlist has no hubs"
    for hub in childlist["hubs"]:
        if not isinstance(hub, dict) or not HEX.match(undash(hub.get("id", ""))):
            return f"bad hub id {hub.get('id') if isinstance(hub, dict) else hub!r}"
        if not isinstance(hub.get("title"), str) or not hub["title"]:
            return f"hub {hub['id']} has no fetched title"
        if not isinstance(hub.get("children"), list):
            return f"hub {hub['id']} has no children list"
    return None


def run(registry_path, childlist, inject=None, audit_root=None, snapshot_out=None, inject_title=None):
    A = audit_module(audit_root)
    reg = A.load_data(registry_path)
    if inject_title:
        hub, title = undash(inject_title[0]), inject_title[1]
        childlist = copy.deepcopy(childlist)
        target = [h for h in childlist["hubs"] if undash(h["id"]) == hub]
        if len(target) != 1:
            raise ValueError(f"--inject-title: {hub} is not a fetched hub")
        if target[0].get("title") == title:
            raise ValueError("--inject-title: the injected title equals the fetched one")
        target[0]["title"] = title
    snap, unplaced = build_snapshot(childlist, reg)
    if inject:
        row, parent = inject
        page = next(r["notion_page_id"] for r in reg["prompts"] if r["prompt_key"] == row)
        src = next(s for s in snap["sources"] if s["source_id"] == page)
        assert src["parent"] != parent, "the injected parent equals the observed one"
        src["parent"] = parent
    if snapshot_out:
        json.dump(snap, open(snapshot_out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    res = A.audit_governance(MANIFEST, WSR, snap, reg)
    pc = parent_checks(childlist, reg)
    prompt_f = [f for f in res["findings"] if f.get("subject", {}).get("kind") == "prompt"]
    nam2 = sorted(f["subject"]["id"] for f in prompt_f if f["rule_id"] == "NAM-002")
    summary = {"sources": len(snap["sources"]), "rows": len(reg["prompts"]), "unplaced_rows": unplaced,
               "NAM-002": len(nam2), "NAM-002_rows": nam2,
               "NAM-001": sorted(f["subject"]["id"] for f in prompt_f if f["rule_id"] == "NAM-001"),
               "other_errors": sum(1 for f in prompt_f if f["rule_id"] not in ("NAM-001", "NAM-002")
                                   and f["severity"] in ("ERROR", "BLOCKER")),
               "other_prompt_findings": sorted({(f["rule_id"], f["subject"]["id"]) for f in prompt_f
                                                if f["rule_id"] not in ("NAM-001", "NAM-002")}),
               "non_prompt_findings": sorted({f["rule_id"] for f in res["findings"] if f.get("subject", {}).get("kind") != "prompt"}),
               "lanes": len(reg["lanes"]),
               "lane_parent_findings": len(pc["lane_findings"]),
               "lane_parent_lanes": [f["lane"] for f in pc["lane_findings"]],
               "title_findings": len(pc["title_findings"]),
               "title_hubs": [f["hub"] for f in pc["title_findings"]],
               "title_references": pc["title_references"]}
    return {"summary": summary, "verdict": res["verdict"], "lane_findings": pc["lane_findings"],
            "title_findings": pc["title_findings"]}


def expectation_met(s, inject=None, inject_title=None):
    if inject:
        return s["NAM-002_rows"] == [inject[0]]
    if inject_title:
        return s["title_hubs"] == [undash(inject_title[0])]
    return (s["NAM-002"] == 0 and s["other_errors"] == 0 and not s["unplaced_rows"]
            and s["lane_parent_findings"] == 0 and s["title_findings"] == 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("registry")
    ap.add_argument("childlist")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--inject")
    g.add_argument("--inject-title")
    ap.add_argument("--audit-root")
    ap.add_argument("--snapshot-out")
    a = ap.parse_args()
    try:
        cl = json.load(open(a.childlist, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"error": str(e)}))
        return 2
    why = usable(cl)
    if why:
        print(json.dumps({"error": why}))
        return 2
    inj = tuple(a.inject.split("=", 1)) if a.inject else None
    injt = tuple(a.inject_title.split("=", 1)) if a.inject_title else None
    if injt and len(injt) != 2:
        print(json.dumps({"error": "--inject-title needs HUB=TITLE"}))
        return 2
    try:
        r = run(a.registry, cl, inj, a.audit_root, a.snapshot_out, injt)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        return 2
    ok = expectation_met(r["summary"], inj, injt)
    print(json.dumps({**r, "expectation_met": ok}, indent=1, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
