#!/usr/bin/env python3
"""X18 diagnosis: activation_render_102726.py's landed() under run_check, for MODIFICATION-20261027-gcfpe-backlog-open-items.

  x18_landed_probe_102726.py <parts> <before-T> <after-T> --set @K=V ... --out R

  model     the Flow Index's read before C-FI-REV (the newest after <before-T>, at its pin), with C-FI-REV applied in
            memory by the renderer's own apply(), against the read after the write (newest after <after-T>), both after
            control_check_102726.fold: equal or not, and the differing line count
  rule      every phase from review through sweep rendered in memory from the reads after <after-T> (the chain's own
            state, C-FI-REV already landed), and at each phase each listed operation judged by landed() exactly as
            run_check calls it (page_ops = every operation of the page up to that phase) and as plan's prior check
            calls it (page_ops = the earlier phases' operations): the operations the rule reports not landed on a
            text that holds them

Read-only; control pages only; counts, ids and booleans. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID
names the session.
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
E = HERE.parent
sys.path.insert(0, str(E / "plan"))
spec = importlib.util.spec_from_file_location("ar", E / "plan/activation_render_102726.py")
AR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AR)
C = AR.C
FI = "3db4590a05eb81de9736ea69bac61016"
MAP = HERE / "successor-pages-102726.1.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("parts"); ap.add_argument("before"); ap.add_argument("after")
    ap.add_argument("--set", action="append", default=[]); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    values = dict(x.split("=", 1) for x in a.set)
    ctx = AR.Ctx(str(MAP), a.parts, values, False)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    rec = {"record_type": "GCFPE_102726_X18_LANDED_PROBE", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items"}
    # model: the page before, C-FI-REV applied, against the page after
    import body_check as B
    reads = B.all_fetches(FI, root, session, 100000)
    before = [r for r in reads if r[1] == "2026-10-27T15:35:09.250Z"]
    after = [r for r in reads if r[0] >= a.after]
    if not before or not after:
        raise SystemExit("probe: no read of the Flow Index at its pin, or none after the write")
    op = next(o for o in AR.OPS["pages"][FI]["ops"] if o["id"] == "C-FI-REV")
    model, rows = AR.apply(before[-1][2], [op], ctx, FI)
    m, r = C.fold(model), C.fold(after[-1][2])
    ml, rl = m.split("\n"), r.split("\n")
    rec["model"] = {"before_revision": before[-1][1], "after_revision": after[-1][1], "applied": [x["applied"] for x in rows],
                    "after_equals_model": m == r, "lines_model": len(ml), "lines_after": len(rl),
                    "lines_differing": sum(1 for x, y in zip(ml, rl) if x != y) + abs(len(ml) - len(rl))}
    # rule: run_check's and plan's landed() calls, phase by phase, on the chain's own rendered state
    rec["rule"] = []
    start = AR.PHASES.index("review")
    state = {}
    for key in AR.OPS["pages"]:
        if key in AR.VIRTUAL:
            real = ctx.values.get(key, key)
            if key == "@REGISTER_ENTRY_PAGE_ID":
                continue
        else:
            real = key
        got = C.latest(real, root, session, 900, a.after)
        if got:
            state[key] = got[3]
    for ph in AR.PHASES[start:]:
        if ph == "activation" and "@REGISTER_ENTRY_PAGE_ID" not in state:
            state["@REGISTER_ENTRY_PAGE_ID"] = AR.as_fetched(AR.entry_text(ctx))
        if ph == "archived":
            gone = set(ctx.moves)
            state = {k: AR.remove_children(t, gone) for k, t in state.items()}
        for key, text in list(state.items()):
            page = AR.OPS["pages"][key]
            ops = AR.page_ops(key, ph)
            gen = AR.generated(key, page, text, ph, ctx)
            if ph != "review" and (ops or gen):
                text, _ = AR.apply(text, ops + gen, ctx, ctx.values.get(key, key))
                state[key] = text
            upto = [o for o in page["ops"] if AR.PHASES.index(o["phase"]) <= AR.PHASES.index(ph)]
            for o in ops:
                if not AR.landed(text, o, upto, ctx):
                    prior = [p for p in page["ops"] if AR.PHASES.index(p["phase"]) < AR.PHASES.index(ph)]
                    rec["rule"].append({"phase": ph, "page": page["name"], "op": o["id"],
                                        "run_check_landed": False, "start_on_page": AR.occ(C.fold(text), o["start"]),
                                        "start_in_replacements": sum(AR.occ(C.fold(ctx.fill(x["new"]) or ""), o["start"]) for x in upto),
                                        "new_on_page": AR.occ(C.fold(text), C.fold(ctx.fill(o["new"]) or "")) >= 1})
    rec["rule_false_not_landed"] = sorted({(x["phase"], x["op"]) for x in rec["rule"] if x["new_on_page"]})
    rec["ok_model"] = rec["model"]["after_equals_model"]
    Path(a.out).write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False, default=list) + "\n", encoding="utf-8")
    print(json.dumps({"after_equals_model": rec["model"]["after_equals_model"], "lines_differing": rec["model"]["lines_differing"],
                      "rule_false_not_landed": rec["rule_false_not_landed"]}, indent=1, default=list))
    return 0


if __name__ == "__main__":
    sys.exit(main())
