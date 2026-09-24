#!/usr/bin/env python3
"""PLAN dry run of MODIFICATION-20260923-closeout-residuals on one live body, in memory. Nothing is landed.

  dryrun.py <PID> <PAGE_ID> [--registry R] [--guards G] [--skills K]

The body is the newest Notion fetch of PAGE_ID in this session's harness files written in the last --since-minutes
(default 30; the parent's E6 extractor, evidence/e6/land.py, limited so an earlier task's file is never opened): the
transient files D22 allows. They are never written, kept, copied, hashed or deleted here.
The output carries no body text: counts, rule ids, guard ids, and guard patterns (which are registry text).

Checks, all on the body as Notion will store it (blank-line runs collapsed):
- every shared rule and LOCAL edit hits its expected count; every LOCAL-only check reads 0 afterwards;
- the edit reduces to unique search-and-replace operations that reproduce the edited body;
- the row's registry assertions (R, the repaired registry draft) give 0 findings after, and the new forbidden guards
  fire on the unedited body where this Modification edits their class;
- every new guard on the row fires on its injected regression (forbidden) or on removal of its match (required);
- flowmaster-validate's body validator (skills root K) passes the edited body.
"""
import argparse
import difflib
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import canon as C  # noqa: E402
import closeout_rules as R  # noqa: E402

INSTALLED = Path("/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502")
ROOT = "/root/.claude/projects/-home-user-glow-hdengine-v2"


SOURCE = None
TITLE = None  # the page title of the fetch latest_body last returned (ctrl.py children)
SINCE = 30 * 60  # seconds: only files written in the last 30 minutes are opened (D22 condition 2: a harness file
                 # from an earlier task is never read again). Set by --since-minutes.


SESSION = os.environ.get("CLAUDE_CODE_SESSION_ID") or None  # P-101: only the running session's harness files (its
                 # transcript, tool results, subagents and workflows) are read, so a fetch made by another session is
                 # never taken for the one just made. None (or --session any) reads every session under ROOT.


def candidates():
    import time
    cutoff = time.time() - SINCE
    base = ROOT + "/" + SESSION if SESSION else ROOT + "/*"
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(base + "/workflows/**/*.jsonl", recursive=True) + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    return sorted((f for f in set(files) if os.path.getmtime(f) >= cutoff), key=os.path.getmtime)


def texts(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "text" and isinstance(v, str):
                yield v
            else:
                yield from texts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from texts(v)


def latest_body(page):
    import time
    from datetime import datetime, timezone
    # P3 fix: a live session transcript keeps a fresh mtime while holding fetches from earlier tasks, so the file-level
    # mtime filter alone lets an earlier task's fetch be selected. Each transcript entry is also filtered by its own
    # timestamp; a tool-results file (no entry timestamp) keeps the file-level mtime test.
    cutoff_iso = datetime.fromtimestamp(time.time() - SINCE, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    page = page.replace("-", "")
    best = None
    for f in candidates():
        try:
            raw = open(f, encoding="utf-8").read()
        except Exception:
            continue
        if page not in raw.replace("-", "") and page not in raw:
            continue
        for line in (raw.splitlines() if f.endswith(".jsonl") else [raw]):
            try:
                obj = json.loads(line)
            except Exception:
                continue
            entry_ts = obj.get("timestamp") if isinstance(obj, dict) else None
            if f.endswith(".jsonl") and not (isinstance(entry_ts, str) and entry_ts >= cutoff_iso):
                continue
            for t in texts(obj):
                if 'Here is the result of \\"fetch\\"' not in t and 'Here is the result of "fetch"' not in t:
                    continue
                try:
                    inner = json.loads(t)["text"]
                except Exception:
                    inner = t
                head = re.match(r'Here is the result of "fetch" for the Page with URL https://[^/\s]+/p/([0-9a-f-]{32,36})', inner)
                if not head or head.group(1).replace("-", "") != page:
                    continue
                m = re.search(r"<content>\n?(.*)</content>", inner, re.S)
                if m:
                    ts = re.search(r"as of (\S+):", inner)
                    tm = re.search(r"<properties>\n?(\{.*?\})\n?</properties>", inner, re.S)
                    try:
                        title = json.loads(tm.group(1)).get("title") if tm else None
                    except Exception:
                        title = None
                    # P-88: the newest capture wins. A tool-results file has no entry timestamp, so its capture time
                    # is the file's mtime; a page's "as of" need not advance when it is edited.
                    captured = entry_ts if f.endswith(".jsonl") else datetime.fromtimestamp(
                        os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                    cand = ((captured or "", ts.group(1) if ts else ""), m.group(1), f, title)
                    if best is None or cand[0] >= best[0]:
                        best = cand
    if best is None:
        raise SystemExit(json.dumps({"page": page, "error": "NO_FETCH_FOUND", "harness_root": ROOT}))
    global SOURCE, TITLE
    SOURCE, TITLE = best[2], best[3]
    return best[0][1], best[1]


def occ(text, s):
    """Occurrences of s in text, overlapping ones included (P-103): "occurs exactly once" must hold however a search
    is anchored, so two overlapping matches count as two."""
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


def ops_for(old, new):
    """The minimal search-and-replace operations that turn `old` into `new` (Notion update_content). Each old_str
    occurs exactly once in `old`. P-103: each old_str is also grown, within the unchanged lines that follow its change,
    until it no longer occurs in `new`, so the same operation applied again to a page that already carries it matches
    nothing and Notion refuses it (a stale fetch cannot land an insertion twice). Where the lines that follow cannot
    make it absent (an insertion at the very end), the minimal old_str is kept, and reapply_unsafe() names it."""
    a, b = old.splitlines(keepends=True), new.splitlines(keepends=True)
    codes = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    out = []
    for k, (tag, i1, i2, j1, j2) in enumerate(codes):
        if tag == "equal":
            continue
        o2 = i2
        while True:
            s = "".join(a[i1:i2])
            if s.strip() and occ(old, s) == 1:
                break
            if i1 > 0 and (not out or i1 > out[-1][1]):
                i1 -= 1; j1 -= 1
            elif i2 < len(a):
                i2 += 1; j2 += 1
            else:
                return None
        if out and i1 < out[-1][1]:
            p = out.pop(); i1, j1 = p[0], p[2]
        # P-103: grow forward within the unchanged block after this change (never into the next change), then
        # backward, merging with earlier operations, until old_str no longer occurs in `new`; if no growth short of
        # the whole text does it, keep the minimal operation
        room = (codes[k + 1][2] - codes[k + 1][1]) if k + 1 < len(codes) and codes[k + 1][0] == "equal" else 0
        g1, g2, h1, h2, popped = i1, i2, j1, j2, []
        while occ(new, "".join(a[g1:g2])) > 0:
            if g2 < o2 + room:
                g2 += 1; h2 += 1
            elif g1 > 0:
                g1 -= 1; h1 -= 1
                if out and g1 < out[-1][1]:
                    p = out.pop(); popped.append(p); g1, h1 = p[0], p[2]
            else:
                break
        if occ(new, "".join(a[g1:g2])) == 0 and (g1, g2) != (0, len(a)):
            i1, i2, j1, j2 = g1, g2, h1, h2
        else:
            out.extend(reversed(popped))
        out.append([i1, i2, j1, j2])
    return [{"old_str": "".join(a[i1:i2]), "new_str": "".join(b[j1:j2])} for i1, i2, j1, j2 in out]


def reapply_unsafe(body, ops):
    """Indexes of the operations whose old_str still occurs in the text all of them produce (P-103): applied a second
    time, on a stale read of a landed page, such an operation would land again."""
    landed = simulate(body, ops)
    if landed is None:
        return None
    return [i for i, op in enumerate(ops) if occ(landed, op["old_str"]) > 0]


def simulate(body, ops):
    t = body
    for op in ops:
        if occ(t, op["old_str"]) != 1:
            return None
        t = t.replace(op["old_str"], op["new_str"])
    return t


def load_guards(path):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    out = []
    for g in raw:
        if g.get("kind") not in ("forbidden_regex", "required_regex") or not g.get("pattern"):
            continue
        rows = g.get("rows") or []
        allrows = any(str(r).startswith("ALL55") for r in rows)
        reg = str(g.get("regression") or "")
        inj = re.sub(r"^inject(?:ed)? into [A-Z0-9-]+(?:, [A-Z0-9-]+)*: ", "", reg)
        inj = None if (not reg or reg.lower().startswith(("delete", "remove", "put the placeholder"))) else inj
        out.append({"id": g.get("rule_id", "").split(" ")[0], "kind": g["kind"], "pattern": g["pattern"],
                    "rows": "ALL" if allrows else set(rows), "inject": inj})
    return out


def registry_row(reg_path, pid):
    sys.path.insert(0, str(INSTALLED / "amthor-workspace-governance-audit/scripts"))
    import audit_workspace_governance as A  # noqa: E402
    reg = A.load_data(reg_path)
    row = next((r for r in reg["prompts"] if r.get("prompt_key") == pid), None)
    return A, row


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pid")
    ap.add_argument("page")
    ap.add_argument("--registry", default=str(C.REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"))
    ap.add_argument("--guards", default=str(HERE.parent / "registry/row_assertions.json"))
    ap.add_argument("--skills", default=str(INSTALLED), help="at PLAN the final trial tree; at EXECUTE the patched tree ($PKG, built at X1.1)")
    ap.add_argument("--since-minutes", type=int, default=30)
    ap.add_argument("--candidate-url", help="fills {{CANDIDATE_CRD_LIST_URL}} (R-ITEM18); a dry run may use a well-formed stand-in")
    a = ap.parse_args()
    global SINCE
    SINCE = a.since_minutes * 60
    if a.candidate_url:
        for i, (rid, anc, act, new, exp) in enumerate(R.RULES):
            if isinstance(new, str) and "{{CANDIDATE_CRD_LIST_URL}}" in new:
                R.RULES[i] = (rid, anc, act, new.replace("{{CANDIDATE_CRD_LIST_URL}}", a.candidate_url), exp)
    ts, body = latest_body(a.page)
    post, rep = R.apply(a.pid, body)
    out = {"pid": a.pid, "fetched": ts, "source_file": SOURCE, "chars_before": len(body), "chars_after": len(post),
           "rules": rep, "rule_mismatches": {k: v for k, v in rep.items() if not v["ok"]}}
    ops = ops_for(body, post)
    out["ops"] = {"count": len(ops) if ops is not None else None,
                  "reproduces_edit": ops is not None and simulate(body, ops) == post,
                  "max_old_str_lines": max((o["old_str"].count("\n") + 1 for o in ops), default=0) if ops else None}
    stored = C.collapse(post)
    out["placement"] = {k: stored.count(C.collapse(v)) for k, v in
                        {"W-4": C.W4, "ONCE": C.ONCE, "OWN": R.OWN, "RECV": R.RECV}.items()}
    if a.pid == "GCFPE-MGMT-10-PROPOSED":
        out["registry"] = "NOT_A_REGISTRY_ROW"
        out["pass"] = not out["rule_mismatches"] and out["ops"]["reproduces_edit"]
        print(json.dumps(out, indent=1, ensure_ascii=False))
        return
    A, row = registry_row(a.registry, a.pid)
    if row is None:
        out["registry"] = "ROW_NOT_FOUND"
    else:
        pre_f = sorted({(f["rule_id"], f["observed"]["summary"][:160]) for f in A._evaluate_assertions(row, C.collapse(body), "pre")})
        post_f = sorted({(f["rule_id"], f["observed"]["summary"][:160]) for f in A._evaluate_assertions(row, stored, "post")})
        out["registry"] = {"findings_before": len(pre_f), "findings_after": post_f}
    guards = []
    if Path(a.guards).exists():
        for g in load_guards(a.guards):
            if g["rows"] != "ALL" and a.pid not in g["rows"]:
                continue
            fl = re.MULTILINE
            r = {"id": g["id"], "kind": g["kind"][:9]}
            if g["kind"] == "forbidden_regex":
                r["fires_before"] = bool(re.search(g["pattern"], C.collapse(body), fl))
                r["silent_after"] = not re.search(g["pattern"], stored, fl)
                if g["inject"]:
                    r["fires_on_injection"] = bool(re.search(g["pattern"], stored + "\n" + g["inject"] + "\n", fl))
            else:
                r["matches_after"] = bool(re.search(g["pattern"], stored, fl))
                removed = re.sub(g["pattern"], "", stored, flags=fl)
                r["fires_on_removal"] = not re.search(g["pattern"], removed, fl)
            guards.append(r)
    out["guards"] = guards
    out["guard_failures"] = [g for g in guards if g.get("silent_after") is False or g.get("fires_on_injection") is False
                             or g.get("matches_after") is False or g.get("fires_on_removal") is False]
    contract = Path(a.skills) / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
    p = subprocess.run([sys.executable, str(Path(a.skills) / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"),
                        str(Path(a.skills) / "change-flow"), "--contract", str(contract), "--bodies-stdin"],
                       input=json.dumps({a.pid: stored}), capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    try:
        v = json.loads(p.stdout)
    except Exception:
        v = {"raw": p.stdout[-400:], "stderr": p.stderr[-400:]}
    out["validator"] = {"exit": p.returncode, "ok": v.get("ok"), "errors": v.get("errors"),
                        "validated": v.get("prompt_bodies_validated")}
    out["pass"] = (not out["rule_mismatches"] and out["ops"]["reproduces_edit"] and isinstance(out["registry"], dict)
                   and not out["registry"]["findings_after"] and not out["guard_failures"] and p.returncode == 0)
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
