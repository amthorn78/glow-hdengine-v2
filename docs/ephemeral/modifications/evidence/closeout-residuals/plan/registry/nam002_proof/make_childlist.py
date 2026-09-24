#!/usr/bin/env python3
"""PLAN prototype input for nam002_live.py (P-63): a SYNTHETIC child list built from the new registry's own parent
IDs and titles (circular by construction, as the first prototype was). No Notion fetch; no prompt body.

Hubs: each lane's notion_parent_id with its notion_parent_title; children: each row's notion_page_id and
expected_title under its expected_parent_id. Asserts the result equals the ANALYZE parent map (guards.PARENT_MAP).
  python3 make_childlist.py <registry.new.md> <out.json>
"""
import json, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "wga_scripts"))
from audit_workspace_governance import load_data  # noqa: E402
import guards as G  # noqa: E402


def childlist(reg):
    hubs = {}
    for lane in reg["lanes"]:
        t = hubs.setdefault(lane["notion_parent_id"], lane["notion_parent_title"])
        assert t == lane["notion_parent_title"], lane
    kids = {h: [] for h in hubs}
    for r in reg["prompts"]:
        assert r["expected_parent_id"] in hubs, r["prompt_key"]
        if "expected_parent_title" in r:
            assert r["expected_parent_title"] == hubs[r["expected_parent_id"]], r["prompt_key"]
        kids[r["expected_parent_id"]].append({"id": r["notion_page_id"], "title": r["expected_title"]})
    return {"captured_at": "SYNTHETIC (PLAN prototype; hubs and titles from the registry's own parent fields)",
            "hubs": [{"id": h, "title": t, "fetched": "SYNTHETIC", "children": kids[h]} for h, t in hubs.items()]}


if __name__ == "__main__":
    reg = load_data(sys.argv[1])
    cl = childlist(reg)
    assert {h["id"]: h["title"] for h in cl["hubs"]} == {n: nt for _, _, n, nt, _, _ in G.PARENT_MAP}
    json.dump(cl, open(sys.argv[2], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(json.dumps({"hubs": len(cl["hubs"]), "children": sum(len(h["children"]) for h in cl["hubs"])}))
