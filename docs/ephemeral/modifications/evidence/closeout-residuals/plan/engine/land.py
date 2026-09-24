#!/usr/bin/env python3
"""EXECUTE landing tool for MODIFICATION-20260923-closeout-residuals (the parent's evidence/e6/land.py, for these rules).

  land.py plan  <PID> <PAGE_ID> [--candidate-url URL] [--no-ops] [--registry R] [--guards G] [--skills K] [--harness-root H]
  land.py check <PID> <PAGE_ID> [--candidate-url URL] [--registry R] [--guards G] [--skills K] [--harness-root H]

--candidate-url is required, in both modes, for a body whose rules carry {{CANDIDATE_CRD_LIST_URL}} (CL-40): the
      token is filled before anything is compared, so a landed page carrying the real URL reads as landed (P-75).
plan: the newest fetch of the page (dryrun.latest_body: this session's harness files written in the last 30 minutes;
      D22) -> the edits still missing from it (edit_states, P-88) -> the minimal search-and-replace operations for
      Notion `update_content`, printed to stdout for the landing call in hand and written nowhere. Each edit is
      NOT_LANDED (its anchor matches its expected count and, for an insertion, its new text does not already follow),
      LANDED (a replacement whose anchor is gone and whose new text is present, a deletion whose anchor is gone, or an
      insertion whose every match is already followed by its new text), or MIXED. On an unlanded page every edit is
      NOT_LANDED and `repair` is []; on a partly landed page only the NOT_LANDED edits are planned and `repair` lists
      the LANDED ones. Refuses: a body already landed (ALREADY_LANDED), a body with nothing to land (NOTHING_TO_LAND),
      any MIXED edit or failing LOCAL-only check (COUNT_MISMATCH), a `{{` the edit introduces (P-48, P-59), operations
      that do not reproduce the edit, and (P-76) a failing precheck (PRECHECK_FAILED) or landed check
      (LANDED_CHECK_FAILED). The precheck is `check`'s criteria on the text the operations produce; the landed check
      is `check` itself, the STALE test included, on that text, i.e. what the readback after the landing will run.
      --no-ops (the rehearsal) prints counts and both checks, never the operations.
check: the readback. The newest fetch of the page after the landing -> the row's registry assertions (0 findings), every
      new guard on the row (forbidden: silent, and fires on its injected regression; required: matches, and fails when
      removed), flowmaster-validate's body validator, no insertion doubled (P-88), and the placement counts. A page
      that does not yet show the landing's new text reports STALE_READBACK_OR_NOT_LANDED. Prints the harness file it
      read (source_file, D22 condition 5); exits 1 unless `pass` is true. No body text is printed.
There is no rollback journal and no reverse mode (P-58 as revised in repair round 4, D22): nothing keeps a copy of a
body. A failed readback is repaired forward by `plan` on a fresh fetch, which plans only the edits still missing
(P-88); a page it refuses stops the landing unit and returns to Nathan (spec §9 X5.4).
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon as C  # noqa: E402
import closeout_rules as R  # noqa: E402
import dryrun as D  # noqa: E402

TOKEN = "{{CANDIDATE_CRD_LIST_URL}}"
URL_RE = re.compile(r"https://app\.notion\.com/p/[0-9a-f]{32}")


def fill(url):
    """Replace the page-URL token in every rule's new text (R-ITEM18)."""
    if not URL_RE.fullmatch(url):
        raise SystemExit(json.dumps({"refused": "URL_FORM", "want": URL_RE.pattern}))
    for i, (rid, anchor, action, new, exp) in enumerate(R.RULES):
        if isinstance(new, str) and TOKEN in new:
            R.RULES[i] = (rid, anchor, action, new.replace(TOKEN, url), exp)


def landed(pid, body):
    """True when every edit this body receives reads LANDED (edit_states, P-88): nothing is left to land."""
    _, rep, states = edit_states(pid, body)
    live = [k for k in states if rep[k]["expected"] > 0]
    return bool(live) and all(states[k] == "LANDED" for k in live)


def nothing_to_land(rep):
    """Every rule and LOCAL edit reads 0 and every CHECK passes: a deletion-only body already landed, or an untouched
    body (P-59)."""
    rules = [v for k, v in rep.items() if not k.startswith("CHECK ")]
    checks_ok = all(v["ok"] for k, v in rep.items() if k.startswith("CHECK "))
    return all(v["hits"] == 0 for v in rules) and checks_ok


def _state(t, pat, action, nt, n):
    """One edit on text t: ("NOT_LANDED" | "LANDED" | "MIXED", hits). An edit is placed at a match when its new text
    already stands there: after the match (insert_after), before it (insert_before), or, for a replacement, around it
    (the match lies inside an occurrence of the new text). A replacement that shortens its match to a prefix of it
    (R-ITEM38, LCL-30-2) is therefore never read as placed on the text it has not yet changed (pass 5)."""
    ms = list(re.finditer(pat, t))
    if action == "delete":
        return ("NOT_LANDED" if len(ms) == n else "LANDED" if not ms else "MIXED"), len(ms)

    def placed(m):
        if not nt:
            return False
        if action == "insert_after":
            return t[m.end():].startswith(nt)
        if action == "insert_before":
            return t[:m.start()].endswith(nt)
        if len(m.group(0)) > len(nt):
            return False
        return any(t[s:s + len(nt)] == nt for s in range(max(0, m.end() - len(nt)), m.start() + 1))
    done = sum(1 for m in ms if placed(m))
    if len(ms) == n and done == 0:
        return "NOT_LANDED", len(ms)
    if len(ms) == n and done == n:
        return "LANDED", len(ms)
    if action == "replace" and not ms and (not nt.strip() or C.collapse(nt).strip() in C.collapse(t)):
        return "LANDED", 0
    return "MIXED", len(ms)


def edit_states(pid, body):
    """closeout_rules.apply, edit by edit and in the same order, applying only the edits not yet on the page (P-88).
    Returns the edited text, the report and each edit's state. On an unlanded page it equals closeout_rules.apply."""
    t, rep, states = body, {}, {}
    todo = [(rid, R._pick(anchor, pid), action, R._pick(new, pid), exp[pid])
            for rid, anchor, action, new, exp in R.RULES if pid in exp]
    todo += [(e["id"], R.local_pattern(e), e["action"], e["new_text"], 1) for e in R.LOCAL.get(pid, [])]
    for rid, pat, action, nt, n in todo:
        if n == 0:
            hits = len(re.findall(pat, t))
            states[rid], rep[rid] = ("NOT_LANDED" if hits == 0 else "MIXED"), {"hits": hits, "expected": 0, "ok": hits == 0}
            continue
        st, hits = _state(t, pat, action, nt, n)
        states[rid] = st
        rep[rid] = {"hits": hits, "expected": n, "ok": st != "MIXED", "state": st}
        if st == "NOT_LANDED":
            t, _ = R._edit(t, pat, action, nt)
    for cid, pat, rows in R.CHECKS:
        if pid in rows:
            k = len(re.findall(pat, t))
            rep["CHECK " + cid] = {"hits": k, "expected": 0, "ok": k == 0}
    return t, rep, states


def doubled(pid, stored):
    """Insertions that occur twice in a row: what re-applying an insertion to a page that already has it produces."""
    ins = [(rid, R._pick(new, pid)) for rid, anchor, action, new, exp in R.RULES
           if action.startswith("insert") and exp.get(pid, 0) > 0]
    ins += [(e["id"], e["new_text"]) for e in R.LOCAL.get(pid, []) if e["action"].startswith("insert")]
    return sorted(rid for rid, nt in ins if nt.strip() and C.collapse(nt + nt) in stored)


def checks(pid, text, a, mode):
    """The readback checks on `text` as stored; the dryrun's registry, guard and validator checks, without the rules.
    mode "check" (the readback, and plan's landed check) also reports a page that does not show the landing."""
    import os
    import subprocess
    stored = C.collapse(text)
    has_news = any(pid in exp and exp[pid] > 0 for _, _, _, _, exp in R.RULES) or bool(R.LOCAL.get(pid))
    if mode == "check" and has_news and not landed(pid, text):
        post, rep = R.apply(pid, text)
        if not nothing_to_land(rep):
            _, _, states = edit_states(pid, text)
            return {"status": "STALE_READBACK_OR_NOT_LANDED", "pass": False,
                    "not_landed": sorted(k for k, s in states.items() if s != "LANDED"),
                    "note": "the page does not show every edit of this landing: re-fetch after the write's task has "
                            "succeeded and check again; if it still does not, run plan on the fresh fetch (P-88)"}
    out = {"placement": {k: stored.count(C.collapse(v)) for k, v in
                         {"W-4": C.W4, "ONCE": C.ONCE, "OWN": R.OWN, "RECV": R.RECV}.items()},
           "unfilled_tokens": stored.count("{{"), "doubled_insertions": doubled(pid, stored)}
    if pid == "GCFPE-MGMT-10-PROPOSED":
        gates = {cid: len(re.findall(pat, stored)) for cid, pat, rows in R.CHECKS if pid in rows}
        out["gates"] = gates
        out["pass"] = all(n == 0 for n in gates.values()) and out["unfilled_tokens"] == 0 and not out["doubled_insertions"]
        return out
    A, row = D.registry_row(a.registry, pid)
    out["registry_findings"] = sorted({(f["rule_id"], f["observed"]["summary"][:160])
                                       for f in A._evaluate_assertions(row, stored, "readback")}) if row else "ROW_NOT_FOUND"
    guards = []
    for g in (D.load_guards(a.guards) if Path(a.guards).exists() else []):
        if g["rows"] != "ALL" and pid not in g["rows"]:
            continue
        r = {"id": g["id"], "kind": g["kind"][:9]}
        if g["kind"] == "forbidden_regex":
            r["silent"] = not re.search(g["pattern"], stored, re.M)
            if g["inject"]:
                r["fires_on_injection"] = bool(re.search(g["pattern"], stored + "\n" + g["inject"] + "\n", re.M))
        else:
            r["matches"] = bool(re.search(g["pattern"], stored, re.M))
            r["fires_on_removal"] = not re.search(g["pattern"], re.sub(g["pattern"], "", stored, flags=re.M), re.M)
        guards.append(r)
    out["guard_failures"] = [g for g in guards if False in g.values()]
    contract = Path(a.skills) / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
    p = subprocess.run([sys.executable, str(Path(a.skills) / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"),
                        str(Path(a.skills) / "change-flow"), "--contract", str(contract), "--bodies-stdin"],
                       input=json.dumps({pid: stored}), capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    try:
        v = json.loads(p.stdout)
    except Exception:
        v = {}
    out["validator"] = {"exit": p.returncode, "ok": v.get("ok"), "errors": v.get("errors")}
    out["pass"] = (row is not None and not out["registry_findings"] and not out["guard_failures"]
                   and p.returncode == 0 and out["unfilled_tokens"] == 0 and not out["doubled_insertions"])
    return out


TOKEN_PIDS = sorted({p for rid, anchor, action, new, exp in R.RULES
                     for p, n in exp.items() if n > 0 and TOKEN in (R._pick(new, p) or "")})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["plan", "check"])
    ap.add_argument("pid")
    ap.add_argument("page")
    ap.add_argument("--candidate-url")
    ap.add_argument("--registry", default=str(C.REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"))
    ap.add_argument("--guards", default=str(HERE.parent / "registry/row_assertions.json"))
    ap.add_argument("--skills", default=str(D.INSTALLED))
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--harness-root", default=D.ROOT)
    ap.add_argument("--no-ops", action="store_true")
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    D.ROOT = a.harness_root
    if a.pid in TOKEN_PIDS and not a.candidate_url:
        print(json.dumps({"pid": a.pid, "refused": "CANDIDATE_URL_REQUIRED (P-75)"}))
        raise SystemExit(2)
    if a.candidate_url:
        fill(a.candidate_url)
    ts, body = D.latest_body(a.page)
    if a.mode == "check":
        res = checks(a.pid, body, a, "check")
        print(json.dumps({"pid": a.pid, "fetched": ts, "source_file": D.SOURCE, **res}, indent=1, ensure_ascii=False))
        raise SystemExit(0 if res.get("pass") else 1)
    post0, rep0 = R.apply(a.pid, body)
    if nothing_to_land(rep0):
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "NOTHING_TO_LAND: already landed or untouched; run check"}))
        raise SystemExit(3)
    post, rep, states = edit_states(a.pid, body)
    bad = {k: v for k, v in rep.items() if not v["ok"]}
    if bad:
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "COUNT_MISMATCH", "rules": bad}, indent=1))
        raise SystemExit(4)
    repair = sorted(k for k, s in states.items() if s == "LANDED")
    if not any(s == "NOT_LANDED" for k, s in states.items() if rep[k]["expected"] > 0):
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "ALREADY_LANDED: every edit reads landed; run check, not plan"}))
        raise SystemExit(3)
    if not repair and post != post0:
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "ENGINE_DISAGREES: edit_states differs from apply"}))
        raise SystemExit(9)
    if post.count("{{") > body.count("{{"):  # P-59: only a token the edit introduces
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "UNFILLED_TOKEN (P-48)"}))
        raise SystemExit(5)
    ops = D.ops_for(body, post)
    if ops is None or D.simulate(body, ops) != post:
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "OPS_DO_NOT_REPRODUCE"}))
        raise SystemExit(6)
    landed_text = D.simulate(body, ops)
    pre = checks(a.pid, landed_text, a, "precheck")
    after = checks(a.pid, landed_text, a, "check")
    summary = {"pid": a.pid, "fetched": ts, "source_file": D.SOURCE, "ops_count": len(ops), "repair": repair, "rules": rep,
               "precheck": pre, "landed_check": after}
    if not pre.get("pass") or not after.get("pass"):
        print(json.dumps({**summary, "refused": "PRECHECK_FAILED" if not pre.get("pass") else "LANDED_CHECK_FAILED"},
                         indent=1, ensure_ascii=False))
        raise SystemExit(8)
    if a.no_ops:
        print(json.dumps(summary, indent=1, ensure_ascii=False))
        return
    print(json.dumps({"pid": a.pid, "fetched": ts, "source_file": D.SOURCE, "repair": repair, "ops": ops, "rules": rep,
                      "precheck": pre, "landed_check": after}, ensure_ascii=False))


if __name__ == "__main__":
    main()
