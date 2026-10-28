#!/usr/bin/env python3
"""Before P0: the promotion transaction, P1 to P6, in memory, for MODIFICATION-20261027-gcfpe-backlog-open-items.

  x19_transaction_probe_102726.py <parts> <fetched-after> --set @K=V ... --out R

From this session's newest reads after <fetched-after> of every control page, the 102726.1 catalog and PE (the state
after C4), every phase from activation through sweep is applied in memory as activation_render_102726.py's chain
does (the register entry appears at activation, a moved page leaves its parent at archived, a retitled child shows its
new title), with plan/activation-ops.json as it stands (AM-9 and the opt-ins). At each phase, on each page:
  plan    the landing judgement `plan --phase PH` makes on the read before PH's writes: every earlier phase's listed
          operation LANDED (prior_not_landed)
  check   the judgement `check --phase PH` makes on the read after them: PH's listed operations LANDED (not_landed)
  apply   PH's listed and generated operations refused, and control_check_102726.py's rules for PH on the result
each under two landing rules: `am9`, the renderer's landed() as committed, and `am10`, a candidate for Nathan's
decision, under which an earlier operation's replacement also reads present in the form the page's later listed
operations changed it to (C-FI after C-FI-REV). The plan file is not changed. Negatives for the candidate rule are
measured on synthetic text.

D22: control pages only; counts, ids and booleans. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
sys.path.insert(0, str(E / "plan"))
spec = importlib.util.spec_from_file_location("ar_x19", E / "plan/activation_render_102726.py")
AR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(AR)
C = AR.C
MAP = HERE / "successor-pages-102726.1.json"
FIRST = "activation"


def am10(base_landed):
    """The candidate: the replacement reads present as written or as the later listed operations of page_ops,
    applied in order to it where their anchor resolves inside it, changed it; the anchor count is unchanged."""
    def landed(text, op, page_ops, ctx):
        if base_landed(text, op, page_ops, ctx):
            return True
        if op.get("append") or not op.get("new"):
            return False
        ids = [o["id"] for o in page_ops]
        if op["id"] not in ids:
            return False
        changed = ctx.fill(op["new"])
        for later in page_ops[ids.index(op["id"]) + 1:]:
            if later.get("append") or not later.get("start"):
                continue
            t, rows = AR.apply(changed, [later], ctx)
            if rows and rows[0]["applied"]:
                changed = t
        if changed == ctx.fill(op["new"]):
            return False
        op2 = {**op, "new": changed}   # the changed form replaces the written one, so neither is counted twice
        return base_landed(text, op2, [op2 if o["id"] == op["id"] else o for o in page_ops], ctx)
    return landed


def reads(ctx, after):
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    state, as_of = {}, {}
    for key in AR.OPS["pages"]:
        if key == "@REGISTER_ENTRY_PAGE_ID":
            continue
        real = ctx.values.get(key, key) if key in AR.VIRTUAL else key
        if key == "@PE_PAGE_ID":
            real = ctx.map["pe"]["page_id"]
        got = C.latest(real, root, session, 900, after)
        if got is None:
            raise SystemExit(f"probe: no read of {key} after {after}")
        state[key] = {"text": got[3], "title": got[2]}
        as_of[key] = got[1]
    return state, as_of


def run(ctx, state, rule) -> dict:
    AR.landed = rule
    out = []
    for ph in AR.PHASES[AR.PHASES.index(FIRST):]:
        row = {"phase": ph, "plan_prior_not_landed": {}, "check_not_landed": {}, "refused": {}, "control_failing": {}}
        if ph == "activation":
            ent = AR.entry_text(ctx)
            state["@REGISTER_ENTRY_PAGE_ID"] = {"text": AR.as_fetched(ent), "title": AR.OPS["new_pages"]["REGISTER_ENTRY"]["title"]}
            state[C.REGISTER]["text"] = AR.add_child(state[C.REGISTER]["text"], ctx.values["@REGISTER_ENTRY_PAGE_ID"],
                                                     AR.OPS["new_pages"]["REGISTER_ENTRY"]["title"])
        if ph == "archived":
            gone = set(ctx.moves)
            for st in state.values():
                st["text"] = AR.remove_children(st["text"], gone)
        for key, st in state.items():
            page = AR.OPS["pages"][key]
            ops = AR.page_ops(key, ph)
            gen = AR.generated(key, page, st["text"], ph, ctx)
            if ops:   # run_plan renders this page at ph: its prior check on the read before ph's writes
                prior = [o for o in page["ops"] if AR.PHASES.index(o["phase"]) < AR.PHASES.index(ph)]
                nl = [o["id"] for o in prior if not AR.landed(st["text"], o, prior, ctx)]
                if nl:
                    row["plan_prior_not_landed"][page["name"]] = nl
            if ops or gen:
                text, rows = AR.apply(st["text"], ops + gen, ctx, ctx.values.get(key, key))
                st["text"] = text
                ref = [r["id"] for r in rows if not r["applied"]]
                if ref:
                    row["refused"][page["name"]] = ref
            title = page.get("titles", {}).get(ph)
            if title:
                old = st["title"]
                st["title"] = title
                for other in state.values():
                    other["text"] = other["text"].replace(f"\n{old}\n</page>", f"\n{title}\n</page>")
        for key, st in state.items():   # run_check at ph, on the read after ph's writes
            page = AR.OPS["pages"][key]
            ops = AR.page_ops(key, ph)
            upto = [o for o in page["ops"] if AR.PHASES.index(o["phase"]) <= AR.PHASES.index(ph)]
            nl = [o["id"] for o in ops if not AR.landed(st["text"], o, upto, ctx)]
            if nl:
                row["check_not_landed"][page["name"]] = nl
            res = AR.control(key, st["title"], st["text"], ctx, ph)
            if res.get("judged") and not res["ok"]:
                row["control_failing"][page["name"]] = {k: res[k] for k in ("findings", "failed_checks") if k in res}
        row["ok"] = not any(row[k] for k in ("plan_prior_not_landed", "check_not_landed", "refused", "control_failing"))
        out.append(row)
    return {"phases": out, "ok": all(r["ok"] for r in out)}


def negatives(ctx, rule) -> dict:
    a = {"id": "A", "start": "alpha beta.", "end": None, "new": "intro alpha beta. gamma end"}
    b = {"id": "B", "start": "gamma", "end": None, "new": "gamma delta"}
    base = "head\nalpha beta.\ntail\n"
    t_a = base.replace("alpha beta.", a["new"])
    t_ab = t_a.replace("gamma", b["new"])
    return {
        "earlier_op_landed_after_later_op_changed_it": rule(t_ab, a, [a, b], ctx) is True,
        "earlier_op_landed_before_later_op": rule(t_a, a, [a, b], ctx) is True,
        "later_op_landed": rule(t_ab, b, [a, b], ctx) is True,
        "earlier_op_missing_not_landed": rule(base, a, [a, b], ctx) is False,
        "foreign_edit_inside_replacement_not_landed": rule(t_ab.replace("intro", "intra"), a, [a, b], ctx) is False,
        "leftover_anchor_not_landed": rule(t_ab + "alpha beta.\n", a, [a, b], ctx) is False,
        "unrelated_change_not_landed": rule(t_a.replace("gamma", "gamma omega"), a, [a, b], ctx) is False,
    }


def main() -> int:
    argv = sys.argv[1:]
    parts, after = argv[0], argv[1]
    out = Path(argv[argv.index("--out") + 1])
    values = dict(argv[i + 1].split("=", 1) for i, x in enumerate(argv) if x == "--set")
    ctx = AR.Ctx(str(MAP), parts, values, False)
    committed = AR.landed
    rec = {"record_type": "GCFPE_102726_X19_TRANSACTION_PROBE", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "fetched_after": after, "ops_file_sha256": __import__("hashlib").sha256((E / "plan/activation-ops.json").read_bytes()).hexdigest(),
           "renderer_sha256": __import__("hashlib").sha256((E / "plan/activation_render_102726.py").read_bytes()).hexdigest()}
    for name, rule in (("am9", committed), ("am10", am10(committed))):
        state, as_of = reads(ctx, after)
        rec.setdefault("as_of", as_of)
        rec[name] = run(ctx, state, rule)
    import argparse
    for name, m in (("selftest_real_map", MAP), ("selftest_standin_map", E / "plan/successor-map-standin.json")):
        AR.landed = am10(committed)
        r = AR.selftest(argparse.Namespace(successor_map=str(m), parts=parts))
        rec[f"am10_{name}"] = {"ok": r["ok"], "passed": r["cases_passed"], "cases": r["cases_total"],
                               "failing": [k for k, v in r["cases"].items() if not v]}
    AR.landed = committed
    rec["am10_negatives"] = negatives(ctx, am10(committed))
    rec["am9_on_the_same_negatives"] = negatives(ctx, committed)
    rec["ok_am10"] = (rec["am10"]["ok"] and all(rec["am10_negatives"].values())
                      and rec["am10_selftest_real_map"]["ok"] and rec["am10_selftest_standin_map"]["ok"])
    out.write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"am9_ok": rec["am9"]["ok"], "am10_ok": rec["am10"]["ok"],
                      "am9_failing": {r["phase"]: {k: r[k] for k in ("plan_prior_not_landed", "check_not_landed", "refused", "control_failing") if r[k]}
                                      for r in rec["am9"]["phases"] if not r["ok"]},
                      "am10_failing": {r["phase"]: {k: r[k] for k in ("plan_prior_not_landed", "check_not_landed", "refused", "control_failing") if r[k]}
                                       for r in rec["am10"]["phases"] if not r["ok"]},
                      "am10_negatives": rec["am10_negatives"], "ok_am10": rec["ok_am10"],
                      "am10_selftests": [rec["am10_selftest_real_map"]["passed"], rec["am10_selftest_standin_map"]["passed"]]},
                     indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
