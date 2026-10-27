#!/usr/bin/env python3
"""X9's catalog probe, for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items (the X9 failure record).

    x9_catalog_probe_102726.py --fetched-after T [--catalog ID] [--since-minutes N]

On the newest fetch of the 102726.1 catalog after T (body_check.py's D22 reader: this session's harness records,
subagents included) it compares the real page with the form plan/activation_render_102726.py models for it
(`as_fetched(catalog_text(...))`), and runs, in memory and on both, the candidate control check and the activation
phase's catalog operations followed by the activation control check. It also reports the 100926.1 catalog's
frontmatter form. It prints counts, booleans and check names only; it writes nothing and sends nothing. Run with
PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set, and the candidate parts in scratch as --parts.
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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--catalog", default="4064590a05eb8113ae7de73041631c00")
    ap.add_argument("--parts", required=True)
    ap.add_argument("--since-minutes", type=int, default=900)
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("ar", PLAN / "activation_render_102726.py")
    ar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ar)
    C = ar.C
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    vals = {"@CATALOG_PAGE_ID": a.catalog, "@CONTROLS_PR": "770", "@PUBLICATION_DATE": "2026-10-27"}
    ctx = ar.Ctx(str(HERE / "successor-pages-102726.1.json"), a.parts, vals, True, read_only=True)
    got = C.latest(a.catalog, root, session, a.since_minutes, a.fetched_after)
    if got is None:
        print(json.dumps({"ok": False, "error": "NO_FETCH_FOUND"}))
        return 1
    real, title = got[3], got[2]
    model = ar.as_fetched(ar.catalog_text(ctx))
    out = {"catalog": a.catalog, "as_of": got[1], "real_lines": len(real.split("\n")),
           "model_lines": len(model.split("\n")), "real_equals_model": real == model}
    fm_r, fm_m = C.frontmatter_lines(real), C.frontmatter_lines(model)
    joined = [l for l in fm_r if "<br />" in l]
    segs = [s.strip() for s in joined[0].split("<br />")] if joined else []
    out.update({"frontmatter_lines_real": len(fm_r), "frontmatter_lines_model": len(fm_m),
                "real_frontmatter_paragraphs_joined_by_br": len(joined), "real_br_segments": len(segs),
                "segments_equal_model_lines": [l for l in fm_m if l and l != "---"] == segs})

    def after_fm(t: str) -> str:
        ls = t.split("\n")
        j = [i for i, l in enumerate(ls) if l == "---"][1]
        return "\n".join(ls[j + 1:])

    out["body_after_frontmatter_equal"] = after_fm(real) == after_fm(model)
    page = ar.OPS["pages"]["@CATALOG_PAGE_ID"]
    for label, text in (("real", real), ("model", model)):
        out[f"control_candidate_{label}"] = ar.control("@CATALOG_PAGE_ID", title, text, ctx, "candidate")
        ops = ar.page_ops("@CATALOG_PAGE_ID", "activation")
        gen = ar.generated("@CATALOG_PAGE_ID", page, text, "activation", ctx)
        new, rows = ar.apply(text, ops + gen, ctx)
        out[f"activation_ops_{label}"] = {"listed": len(ops), "generated": len(gen),
                                          "applied": sum(r["applied"] for r in rows),
                                          "refused": [[r["id"], r["refusal"]] for r in rows if not r["applied"]]}
        t2 = page.get("titles", {}).get("activation", title)
        out[f"control_activation_{label}"] = ar.control("@CATALOG_PAGE_ID", t2, new, ctx, "activation")
    old = C.latest(C.OLD_CATALOG, root, session, 100000, "")
    if old:
        fo = C.frontmatter_lines(old[3])
        out["old_catalog"] = {"id": C.OLD_CATALOG, "as_of": old[1], "frontmatter_lines": len(fo),
                              "joined_by_br": sum("<br />" in l for l in fo)}
    out["ok"] = (out["real_equals_model"] and out["control_candidate_real"]["ok"]
                 and out["control_activation_real"]["ok"])
    out["d22"] = "transient read of this session's harness records; counts, booleans and check names only"
    print(json.dumps(out, indent=1))
    return 0 if out["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
