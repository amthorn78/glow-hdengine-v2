#!/usr/bin/env python3
"""AM-4's write-form rehearsal, for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items (Nathan's decision
after X9: before C-FI, rehearse both write forms on a real page).

    am4_rehearsal_102726.py render --parts P
    am4_rehearsal_102726.py insert --parts P --page ID --fetched-after T
    am4_rehearsal_102726.py check  --parts P --page ID --fetched-after T --stage created|inserted

`render` prints, on stdout only, the private draft's title and the register entry's rendered text
(activation_render_102726.entry_text on the real successor map; the markers that exist only after promotion take
activation_render's named stand-in values, as the read-only chain does). The draft is not a transaction page and is
deleted after the rehearsal, so no stand-in value reaches a page the Modification keeps.

`insert`, on the newest fetch of the draft after T, requires the draft to equal the plan's model of the created
page (as_fetched(entry_text)), then prints the one P1c-style multi-line insert as an update_content payload: the
entry's `validation\\_status: VALIDATED` line replaced by P1c-PE-5's replacement as AM-4 builds it (two frontmatter
lines, each its own paragraph, in the escaped fetch form), resolved by activation_render's apply.

`check` compares the newest fetch of the draft after T with the plan's model: for `created`, as_fetched(entry_text);
for `inserted`, that model with the insert applied in memory. It prints counts, booleans and line indexes only, and
exits 0 only when the read equals the model exactly. Nothing is written by this helper. Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PLAN = HERE.parent / "plan"
sys.path.insert(0, str(PLAN))
TITLE = "AM-4 write-form rehearsal — draft, to be deleted"
ANCHOR = "validation\\_status: VALIDATED"


def load():
    spec = importlib.util.spec_from_file_location("ar", PLAN / "activation_render_102726.py")
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    return ar


def model(ar, ctx) -> tuple:
    created = ar.as_fetched(ar.entry_text(ctx))
    p1c5 = next(o for o in ar.OPS["pages"]["@PE_PAGE_ID"]["ops"] if o["id"] == "P1c-PE-5")
    op = {"id": "R-P1c", "start": ANCHOR, "end": None, "new": p1c5["new"]}
    inserted, rows = ar.apply(created, [op], ctx)
    return created, inserted, op, rows[0]


def diff_report(real: str, want: str) -> dict:
    a, b = real.split("\n"), want.split("\n")
    diff = [i for i in range(min(len(a), len(b))) if a[i] != b[i]]
    return {"real_lines": len(a), "model_lines": len(b), "real_equals_model": real == want,
            "differing_line_indexes": diff[:5], "line_count_difference": len(a) - len(b)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=("render", "insert", "check"))
    ap.add_argument("--parts", required=True)
    ap.add_argument("--page")
    ap.add_argument("--fetched-after", default="")
    ap.add_argument("--since-minutes", type=int, default=600)
    ap.add_argument("--stage", choices=("created", "inserted"))
    a = ap.parse_args()
    ar = load()
    ctx = ar.Ctx(str(HERE / "successor-pages-102726.1.json"), a.parts, {}, True, read_only=True)
    created, inserted, op, row = model(ar, ctx)
    if a.mode == "render":
        spec = ar.OPS["new_pages"]["REGISTER_ENTRY"]
        used = sorted({m for x in spec["frontmatter"] + spec["body"] for m in ar.MARKER.findall(x)} & set(ctx.standin_used))
        print(json.dumps({"title": TITLE, "content": ar.entry_text(ctx), "stand_in_values": used},
                         ensure_ascii=False, indent=1))
        return 0
    got = ar.C.latest(a.page, os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"],
                      a.since_minutes, a.fetched_after)
    if got is None:
        print(json.dumps({"ok": False, "error": "NO_FETCH_FOUND"}))
        return 1
    real = got[3]
    if a.mode == "insert":
        if real != created:
            print(json.dumps({"ok": False, "error": "DRAFT_NOT_AT_CREATED_MODEL", **diff_report(real, created)}))
            return 1
        _, rows = ar.apply(real, [op], ctx)
        r = rows[0]
        if not r["applied"]:
            print(json.dumps({"ok": False, "error": r["refusal"]}))
            return 1
        print(json.dumps({"ok": True, "page_id": a.page, "op": op["id"], "form": r["form"],
                          "content_updates": [{"old_str": r["old_str"], "new_str": r["new_str"]}]},
                         ensure_ascii=False, indent=1))
        return 0
    want = created if a.stage == "created" else inserted
    out = {"page": a.page, "stage": a.stage, "as_of": got[1], "title": got[2], **diff_report(real, want)}
    fm = [x for x in ar.C.frontmatter_lines(real) if x and x != "---"]
    out["frontmatter_lines"] = len(fm)
    out["frontmatter_joined_by_br"] = sum("<br />" in x for x in fm)
    if a.stage == "inserted":
        lines = [ar.C.unescape(x) for x in op["new"].split("\n\n")]
        out["inserted_lines_read_as_frontmatter_lines"] = all(x in fm for x in lines)
        out["landed"] = ar.landed(real, op, [op], ctx)
    out["ok"] = out["real_equals_model"] and out["frontmatter_joined_by_br"] == 0 and \
        (a.stage == "created" or (out["inserted_lines_read_as_frontmatter_lines"] and out["landed"]))
    out["d22"] = "transient read of this session's harness records; counts, booleans and line indexes only"
    print(json.dumps(out, indent=1))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
