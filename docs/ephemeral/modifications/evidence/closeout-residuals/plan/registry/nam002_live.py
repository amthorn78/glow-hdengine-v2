#!/usr/bin/env python3
"""PART-10 (ITEM-22) gate: NAM-002 over a snapshot of the LIVE 091426.1 hub child lists. No prompt body is read.

EXECUTE writes the child-list file from six Notion fetches of the hub pages (control pages, not prompt bodies):

  {"captured_at": "<UTC>", "hubs": [{"id": "<32-hex hub id>", "title": "<hub title>", "fetched": "<as-of stamp>",
    "children": [{"id": "<32-hex child page id>", "title": "<child title>"}, ...]}, ...]}

build_snapshot() turns it into the governance audit's snapshot shape, one source per registry row:
  {"source_id": <row notion_page_id>, "kind": "notion_page", "complete": true, "in_scope": true,
   "title": <observed child title>, "parent": <hub id under which the page is listed>}
No source carries a "path", so the audit reads no text and evaluates no assertion (D22); NAM-002 compares
"parent" with the row's expected_parent_id as a plain string (audit_workspace_governance.py:604), NAM-001
compares "title" with expected_title. A row whose page is under no hub gets no source (the audit then raises
INV-001 for it); a page listed under two hubs stops the run.

  PYTHONDONTWRITEBYTECODE=1 python3 nam002_live.py <registry.md> <childlist.json> [--inject ROW=PARENT]
        [--audit-root <amthor-workspace-governance-audit dir>] [--snapshot-out <file>]
Exit 0 when the run meets its expectation: without --inject, 0 NAM-002 and 0 prompt errors; with --inject,
exactly one NAM-002, on ROW. Exit 1 otherwise, 2 on unusable input.
"""
import argparse, importlib.util, json, os, re, sys

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


def build_snapshot(childlist, registry):
    where = {}
    for hub in childlist["hubs"]:
        h = undash(hub["id"])
        if not HEX.match(h):
            raise SystemExit(f"bad hub id {hub['id']!r}")
        for c in hub["children"]:
            cid = undash(c["id"])
            if cid in where and where[cid][0] != h:
                raise SystemExit(f"page {cid} listed under two hubs: {where[cid][0]} and {h}")
            where[cid] = (h, c.get("title"))
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


MANIFEST = {"AUDIT_RUN_ID": "PART-10-NAM002", "MODE": "TARGETED", "WORKSPACE_SKILL_REGISTRY_ID": "WSR-20260914.1-OBSERVATIONAL",
            "PROJECT_PROFILE_ID": "glow-hde", "PROJECT_PROMPT_REGISTRY_ID": "GCFPE-PCR-20260914.1",
            "NOTION_SCOPE": ["six 091426.1 hub pages (child lists only)"], "SKILL_SCOPE": [], "TARGETS": ["PART-10"],
            "PF_SOURCES": [], "OUTPUT_DESTINATION": "scratch"}
WSR = {"schema_version": "workspace-skill-registry/1.0", "registry_id": "WSR-20260914.1-OBSERVATIONAL", "status": "DRAFT", "skills": []}


def run(registry_path, childlist, inject=None, audit_root=None, snapshot_out=None):
    A = audit_module(audit_root)
    reg = A.load_data(registry_path)
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
    prompt_f = [f for f in res["findings"] if f.get("subject", {}).get("kind") == "prompt"]
    nam2 = sorted(f["subject"]["id"] for f in prompt_f if f["rule_id"] == "NAM-002")
    summary = {"sources": len(snap["sources"]), "rows": len(reg["prompts"]), "unplaced_rows": unplaced,
               "NAM-002": len(nam2), "NAM-002_rows": nam2,
               "NAM-001": sorted(f["subject"]["id"] for f in prompt_f if f["rule_id"] == "NAM-001"),
               "other_errors": sum(1 for f in prompt_f if f["rule_id"] not in ("NAM-001", "NAM-002")
                                   and f["severity"] in ("ERROR", "BLOCKER")),
               "other_prompt_findings": sorted({(f["rule_id"], f["subject"]["id"]) for f in prompt_f
                                                if f["rule_id"] not in ("NAM-001", "NAM-002")}),
               "non_prompt_findings": sorted({f["rule_id"] for f in res["findings"] if f.get("subject", {}).get("kind") != "prompt"})}
    return {"summary": summary, "verdict": res["verdict"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("registry")
    ap.add_argument("childlist")
    ap.add_argument("--inject")
    ap.add_argument("--audit-root")
    ap.add_argument("--snapshot-out")
    a = ap.parse_args()
    try:
        cl = json.load(open(a.childlist, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"error": str(e)}))
        return 2
    inj = tuple(a.inject.split("=", 1)) if a.inject else None
    r = run(a.registry, cl, inj, a.audit_root, a.snapshot_out)
    s = r["summary"]
    ok = (s["NAM-002_rows"] == [inj[0]]) if inj else (s["NAM-002"] == 0 and s["other_errors"] == 0 and not s["unplaced_rows"])
    print(json.dumps({**r, "expectation_met": ok}, indent=1, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
