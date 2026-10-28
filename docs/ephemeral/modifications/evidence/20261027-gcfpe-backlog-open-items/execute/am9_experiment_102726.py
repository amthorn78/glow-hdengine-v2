#!/usr/bin/env python3
"""The proposed AM-9, measured as an experiment, for MODIFICATION-20261027-gcfpe-backlog-open-items. Not a fix.

  am9_experiment_102726.py <parts> <before-T> <after-T> --set @K=V ... --out R

activation_render_102726.py's landed() counts a start anchor's expected occurrences over every replacement the page
carries up to the phase (run_check: page_ops = all ops through the phase; plan: the earlier phases'). An operation whose
anchor lies inside an earlier operation's replacement (C-FI-REV inside C-FI; P1d-FI-CAND-H and the five P1e-*-CAND
inside C-FI and C-HUB-*) is then expected twice where the page holds it once, and reads not landed. The proposed rule
counts the anchor only inside the replacements still on the page whole, and in the operation's own. Here, in memory
only (the plan file is not changed), with the real module's landed() replaced:
  selftest       activation_render_102726.py selftest on the real map and the PLAN stand-in map
  review check   check --phase review on the reads after <after-T>
  probe          execute/x18_landed_probe_102726.py's phase-by-phase judgement, review through sweep
  negatives      a chained operation is landed; the old rule's false negative; a missing replacement, a leftover
                 anchor and an unapplied operation are each not landed
D22: control pages only; counts, ids and booleans. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
sys.path.insert(0, str(E / "plan"))
MAP = HERE / "successor-pages-102726.1.json"
STANDIN = E / "plan/successor-map-standin.json"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def proposed(AR):
    C, occ, esc = AR.C, AR.occ, AR.esc

    def landed(text, op, page_ops, ctx):
        text = C.fold(text)
        new = C.fold(ctx.fill(op["new"]) or "")
        if op.get("append"):
            return occ(text, new) + occ(text, esc(new)) >= 1
        news = [C.fold(ctx.fill(o["new"]) or "") for o in page_ops]
        news = [x for x in news if x and x != new and (occ(text, x) + (occ(text, esc(x)) if esc(x) != x else 0)) >= 1]
        news = list(dict.fromkeys(news)) + ([new] if new else [])
        s, wl = op["start"], op.get("whole_line", False)
        n_text = occ(text, s, wl) + (occ(text, esc(s), wl) if esc(s) != s else 0)
        n_want = sum(occ(x, s, wl) + (occ(x, esc(s), wl) if esc(s) != s else 0) for x in news)
        if n_text != n_want:
            return False
        return new == "" or occ(text, new) + (occ(text, esc(new)) if esc(new) != new else 0) >= 1
    return landed


def run_main(mod, argv) -> dict:
    buf = io.StringIO()
    old = sys.argv
    sys.argv = ["x", *map(str, argv)]
    try:
        with contextlib.redirect_stdout(buf):
            try:
                mod.main()
            except SystemExit:
                pass
    finally:
        sys.argv = old
    return json.loads(buf.getvalue())


def main() -> int:
    argv = sys.argv[1:]
    parts, before, after = argv[0], argv[1], argv[2]
    out = Path(argv[argv.index("--out") + 1])
    sets = [argv[i + 1] for i, x in enumerate(argv) if x == "--set"]
    AR = load("ar_am9", E / "plan/activation_render_102726.py")
    orig = AR.landed
    AR.landed = proposed(AR)
    rec = {"record_type": "GCFPE_102726_AM9_EXPERIMENT", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "note": "an experiment for Nathan's decision; the plan's activation_render_102726.py is unchanged"}
    for name, m in (("selftest_real_map", MAP), ("selftest_standin_map", STANDIN)):
        r = run_main(AR, ["selftest", "--successor-map", m, "--parts", parts])
        cases = r.get("cases") or r.get("rows") or {}
        rec[name] = {"ok": r.get("ok"), "passed": sum(1 for v in cases.values() if v), "cases": len(cases),
                     "failing": [k for k, v in cases.items() if not v]}
    vals = [y for s in sets for y in ("--set", s)]
    r = run_main(AR, ["check", "--successor-map", MAP, "--parts", parts, "--phase", "review", "--fetched-after", after, *vals])
    rec["review_check"] = {"ok": r.get("ok"), "pages": [{k: p.get(k) for k in ("page", "as_of", "landed", "not_landed", "ok")}
                                                         for p in r.get("pages", [])]}
    PR = load("probe_am9", HERE / "x18_landed_probe_102726.py")
    PR.AR.landed = proposed(PR.AR)
    tmp = out.with_suffix(".probe.tmp")
    run_main(PR, [parts, before, after, *vals, "--out", tmp])
    pr = json.loads(tmp.read_text(encoding="utf-8"))
    tmp.unlink()
    rec["probe"] = {"after_equals_model": pr["model"]["after_equals_model"], "rule_false_not_landed": pr["rule_false_not_landed"]}
    new = AR.landed
    ctx = AR.Ctx(str(MAP), parts, {}, True, read_only=True)
    A = {"id": "A", "start": "alpha beta.", "end": None, "new": "intro alpha beta. gamma"}
    B = {"id": "B", "start": "alpha beta.", "end": None, "new": "alpha beta.\n- delta"}
    base = "head\nalpha beta.\ntail\n"
    t_a = base.replace("alpha beta.", A["new"])
    t_ab = t_a.replace("alpha beta.", B["new"])
    rec["negatives"] = {
        "chained_op_landed": new(t_ab, B, [A, B], ctx) is True,
        "old_rule_false_negative_on_chained_op": orig(t_ab, B, [A, B], ctx) is False,
        "earlier_op_still_landed": new(t_a, A, [A], ctx) is True,
        "missing_replacement_not_landed": new(t_a, B, [A, B], ctx) is False,
        "leftover_anchor_not_landed": new(t_ab + "alpha beta.\n", B, [A, B], ctx) is False,
        "unapplied_op_not_landed": new(base, A, [A], ctx) is False}
    rec["ok"] = (rec["selftest_real_map"]["ok"] is True and rec["selftest_standin_map"]["ok"] is True
                 and rec["review_check"]["ok"] is True and rec["probe"]["after_equals_model"] is True
                 and not rec["probe"]["rule_false_not_landed"] and all(rec["negatives"].values()))
    out.write_text(json.dumps(rec, indent=1, sort_keys=True, default=list) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], "review_check": rec["review_check"]["ok"], "probe": rec["probe"],
                      "selftests": [rec["selftest_real_map"]["passed"], rec["selftest_standin_map"]["passed"]]}, default=list))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
