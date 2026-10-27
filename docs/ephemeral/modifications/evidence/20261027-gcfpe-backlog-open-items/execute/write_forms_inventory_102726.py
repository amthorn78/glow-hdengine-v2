#!/usr/bin/env python3
"""The write-form inventory behind AM-4 and the X9a rehearsal, for EXECUTE of
MODIFICATION-20261027-gcfpe-backlog-open-items.

    write_forms_inventory_102726.py --parts P --fetched-after T [--pin ID=TS ...]

In memory and read-only, it runs `activation_render_102726.py plan --chain --standin-values --from-phase candidate
--phase sweep` on the real successor map and the newest reads after T, and records, for every operation the chain
applies (listed and generated):
  - a replacement joining two lines with a single break where the second is not a table row or a list item;
  - each Notion page link ([..](https://app.notion.com/p/<id>)) and page mention in a replacement, with its form and
    its target's relation to the written page (`self`, `child`: a child-page block on the page, or `other`).
It also tabulates, on the newest read of every page this session has read (the control pages, the catalog, PE and
the 56 members), each stored page mention's form by the same relation, and counts the Markdown links to Notion pages
stored on four control pages. It prints counts, ids and forms only and writes nothing. Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import collections
import contextlib
import importlib.util
import io
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
sys.path.insert(0, str(PLAN))
LINK = re.compile(r"\]\(https://app\.notion\.com/p/([0-9a-f]{32})[^)]*\)")
MENT = re.compile(r'<mention url="https://app\.notion\.com/p/([0-9a-f]{32})[^"]*"( />|>[^<]*</mention>)')
CHILD = re.compile(r'<page url="https://app\.notion\.com/p/([0-9a-f]{32})')
LIST_ITEM = re.compile(r"^\s*(- |\* |\d+\. )")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", required=True)
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--pin", action="append", default=[])
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("ar", PLAN / "activation_render_102726.py")
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    breaks, refs, seen = [], [], {"ops": 0}
    orig = ar.apply

    def spy(text, ops, ctx):
        kids = set(CHILD.findall(text))
        for o in ops:
            seen["ops"] += 1
            new = ctx.fill(o["new"]) or ""
            ls = new.split("\n")
            if any(x and y and not (y.lstrip().startswith("|") or LIST_ITEM.match(y)) for x, y in zip(ls, ls[1:])):
                breaks.append(o["id"])
            for m in LINK.finditer(new):
                refs.append({"id": o["id"], "phase": o.get("phase"), "kind": "markdown_link",
                             "relation": "child" if m.group(1) in kids else "other"})
            for m in MENT.finditer(new):
                refs.append({"id": o["id"], "phase": o.get("phase"), "kind": "mention",
                             "form": "self_closing" if m.group(2) == " />" else "inner_text",
                             "relation": "child" if m.group(1) in kids else "other"})
        return orig(text, ops, ctx)

    ar.apply = spy
    argv = ["ar", "plan", "--successor-map", str(HERE / "successor-pages-102726.1.json"), "--parts", a.parts,
            "--phase", "sweep", "--chain", "--standin-values", "--from-phase", "candidate",
            "--set", "@CONTROLS_PR=770", "--set", "@PUBLICATION_DATE=2026-10-27",
            "--set", "@CATALOG_PAGE_ID=4064590a05eb8113ae7de73041631c00",
            "--fetched-after", a.fetched_after, "--since-minutes", "900"]
    for p in a.pin:
        argv += ["--pin", p]
    sys.argv = argv
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            ar.main()
        except SystemExit:
            pass
    chain = json.loads(buf.getvalue())
    C = ar.C
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    m = json.loads((HERE / "successor-pages-102726.1.json").read_text(encoding="utf-8"))
    ids = [k for k in ar.OPS["pages"] if k not in ar.VIRTUAL] + [C.OLD_CATALOG, "4064590a05eb8113ae7de73041631c00",
                                                                  m["pe"]["page_id"]]
    ids += [r["page_id"] for r in m["members"].values()]
    stored, pages_read = collections.Counter(), 0
    for pid in ids:
        got = C.latest(pid, root, session, 100000, "")
        if not got:
            continue
        pages_read += 1
        kids = set(CHILD.findall(got[3]))
        for mm in MENT.finditer(got[3]):
            rel = "self" if mm.group(1) == pid else ("child" if mm.group(1) in kids else "other")
            stored[f"{rel}:{'self_closing' if mm.group(2) == ' />' else 'inner_text'}"] += 1
    links = {}
    for name, pid in (("Flow Index", C.FLOW_INDEX), ("register", C.REGISTER), ("hub HDE Change Flow", C.CF_HUB),
                      ("Glow Operations Hub", "3ce4590a05eb814f8892f88ff8539308")):
        t = C.latest(pid, root, session, 100000, "")[3]
        kids = set(CHILD.findall(t))
        found = LINK.findall(t)
        links[name] = {"markdown_links": len(found), "to_child_pages": sum(x in kids for x in found)}
    out = {"chain_ok": chain.get("ok"), "chain_totals": chain.get("totals"), "ops_seen": seen["ops"],
           "single_break_joins": breaks,
           "references_written": dict(collections.Counter(
               f"{r['kind']}:{r.get('form', 'link')}:{r['relation']}" for r in refs)),
           "ops_with_markdown_links": sorted({r["id"] for r in refs if r["kind"] == "markdown_link"}),
           "ops_with_mentions": sorted({r["id"] for r in refs if r["kind"] == "mention"}),
           "stored_mentions_by_relation": {"pages_read": pages_read, **dict(sorted(stored.items()))},
           "stored_markdown_links": links,
           "d22": "transient reads of this session's harness records; counts, ids and forms only"}
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
