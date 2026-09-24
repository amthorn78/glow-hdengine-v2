#!/usr/bin/env python3
"""EXECUTE landing tool for MODIFICATION-20260923-closeout-residuals (the parent's evidence/e6/land.py, for these rules).

  land.py plan    <PID> <PAGE_ID> --candidate-url URL [--no-ops | --journal DIR] [--registry R] [--guards G] [--skills K]
  land.py check   <PID> <PAGE_ID> [--registry R] [--guards G] [--skills K]
  land.py reverse <PID> <PAGE_ID> --journal DIR

--no-ops (P-59): the rehearsal. Prints counts, refusals and the precheck, never the operations.
--journal DIR (P-58): also writes the operations to DIR/<PID>.ops.json (the rollback journal: session scratchpad only,
      read only to reverse this landing, deleted when the landing unit passes its gate or has been reversed; D22).
reverse: reads DIR/<PID>.ops.json and the newest fetch of the page, confirms each landed new_str occurs exactly once,
      and prints the reversing operations (new_str -> old_str, in reverse order) for one `update_content` call.

plan: the newest fetch of the page (dryrun.latest_body: this session's harness files written in the last 30 minutes;
      D22) -> closeout_rules.apply -> the minimal search-and-replace operations for Notion `update_content`, printed to
      stdout for the landing call in hand and written nowhere. Refuses: a body already landed (every non-empty new text
      of its rules and LOCAL edits already present), any rule or LOCAL count off its expected value, any `{{` left in
      the edited body (P-48), and operations that do not reproduce the edit. It also prints the precheck: `check` run on
      the text the operations produce, as Notion will store it.
check: the readback. The newest fetch of the page after the landing -> the row's registry assertions (0 findings), every
      new guard on the row (forbidden: silent, and fires on its injected regression; required: matches, and fails when
      removed), flowmaster-validate's body validator, and the placement counts. No body text is printed.
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
    """True when every non-empty new text this body receives is already in it (nothing left to land)."""
    flat = C.collapse(body)
    news = []
    for rid, anchor, action, new, exp in R.RULES:
        if pid in exp and exp[pid] > 0:
            t = R._pick(new, pid)
            if t and t.strip():
                news.append(t)
    news += [e["new_text"] for e in R.LOCAL.get(pid, []) if e["new_text"].strip()]
    return bool(news) and all(C.collapse(n).strip() in flat for n in news)


def nothing_to_land(rep):
    """Every rule and LOCAL edit reads 0 and every CHECK passes: a deletion-only body already landed, or an untouched
    body (P-59)."""
    rules = [v for k, v in rep.items() if not k.startswith("CHECK ")]
    checks_ok = all(v["ok"] for k, v in rep.items() if k.startswith("CHECK "))
    return all(v["hits"] == 0 for v in rules) and checks_ok


def checks(pid, text, a):
    """The readback checks on `text` as stored; the dryrun's registry, guard and validator checks, without the rules."""
    import os
    import subprocess
    stored = C.collapse(text)
    has_news = any(pid in exp and exp[pid] > 0 for _, _, _, _, exp in R.RULES) or bool(R.LOCAL.get(pid))
    if a.mode == "check" and has_news and not landed(pid, text):
        post, rep = R.apply(pid, text)
        if not nothing_to_land(rep):
            return {"status": "STALE_READBACK_OR_NOT_LANDED", "pass": False,
                    "note": "the page does not show this landing's new text: re-fetch and run check again; reverse only on a "
                            "failure of a readback that shows the landing (P-59)"}
    out = {"placement": {k: stored.count(C.collapse(v)) for k, v in
                         {"W-4": C.W4, "ONCE": C.ONCE, "OWN": R.OWN, "RECV": R.RECV}.items()},
           "unfilled_tokens": stored.count("{{")}
    if pid == "GCFPE-MGMT-10-PROPOSED":
        gates = {cid: len(re.findall(pat, stored)) for cid, pat, rows in R.CHECKS if pid in rows}
        out["gates"] = gates
        out["pass"] = all(n == 0 for n in gates.values()) and out["unfilled_tokens"] == 0
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
                   and p.returncode == 0 and out["unfilled_tokens"] == 0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["plan", "check", "reverse"])
    ap.add_argument("pid")
    ap.add_argument("page")
    ap.add_argument("--candidate-url")
    ap.add_argument("--registry", default=str(C.REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"))
    ap.add_argument("--guards", default=str(HERE.parent / "registry/row_assertions.json"))
    ap.add_argument("--skills", default=str(D.INSTALLED))
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--no-ops", action="store_true")
    ap.add_argument("--journal")
    a = ap.parse_args()
    D.SINCE = a.since_minutes * 60
    ts, body = D.latest_body(a.page)
    if a.mode == "check":
        print(json.dumps({"pid": a.pid, "fetched": ts, **checks(a.pid, body, a)}, indent=1, ensure_ascii=False))
        return
    if a.mode == "reverse":
        if not a.journal:
            raise SystemExit(json.dumps({"refused": "REVERSE_NEEDS_JOURNAL"}))
        ops = json.loads((Path(a.journal) / f"{a.pid}.ops.json").read_text(encoding="utf-8"))["ops"]
        rev = [{"old_str": o["new_str"], "new_str": o["old_str"]} for o in reversed(ops)]
        t = body
        for o in rev:
            if t.count(o["old_str"]) != 1:
                print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "REVERSE_NOT_UNIQUE"}))
                raise SystemExit(7)
            t = t.replace(o["old_str"], o["new_str"])
        print(json.dumps({"pid": a.pid, "fetched": ts, "ops": rev}, ensure_ascii=False))
        return
    if a.candidate_url:
        fill(a.candidate_url)
    if landed(a.pid, body):
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "ALREADY_LANDED: run check, not plan"}))
        raise SystemExit(3)
    post, rep = R.apply(a.pid, body)
    if nothing_to_land(rep):
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "NOTHING_TO_LAND: already landed or untouched; run check"}))
        raise SystemExit(3)
    bad = {k: v for k, v in rep.items() if not v["ok"]}
    if bad:
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "COUNT_MISMATCH", "rules": bad}, indent=1))
        raise SystemExit(4)
    if post.count("{{") > body.count("{{"):  # P-59: only a token the edit introduces
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "UNFILLED_TOKEN (P-48)"}))
        raise SystemExit(5)
    ops = D.ops_for(body, post)
    if ops is None or D.simulate(body, ops) != post:
        print(json.dumps({"pid": a.pid, "fetched": ts, "refused": "OPS_DO_NOT_REPRODUCE"}))
        raise SystemExit(6)
    a.mode = "precheck"
    pre = checks(a.pid, D.simulate(body, ops), a)
    if a.journal:
        jd = Path(a.journal)
        jd.mkdir(parents=True, exist_ok=True)
        jf = jd / f"{a.pid}.ops.json"
        jf.write_text(json.dumps({"pid": a.pid, "page": a.page, "fetched": ts, "ops": ops}, ensure_ascii=False), encoding="utf-8")
        jf.chmod(0o600)
    if a.no_ops:
        print(json.dumps({"pid": a.pid, "fetched": ts, "source_file": D.SOURCE, "ops_count": len(ops),
                          "rules": rep, "precheck": pre}, indent=1, ensure_ascii=False))
        return
    print(json.dumps({"pid": a.pid, "fetched": ts, "ops": ops, "rules": rep, "precheck": pre}, ensure_ascii=False))


if __name__ == "__main__":
    main()
