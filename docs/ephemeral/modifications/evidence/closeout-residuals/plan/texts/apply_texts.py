#!/usr/bin/env python3
"""Apply the EV/texts/edits.json entries of one commit label, in order, to a repository working tree (P-102).

  PYTHONDONTWRITEBYTECODE=1 python3 apply_texts.py <repo> <edits.json> <label> [--run EX/run.json]
      [--installed-freeze EX/installed_freeze.txt]

<label> is the entry's "commit" field: X2.2 (X2.1's texts), X3.5 (X3.4's), X5.2 or close (X7.6). The §9-order proof
(skills/results/run_proof_x.py) ran the PLAN copy of this script for X2.2 and X3.5; this committed copy adds the fills
and the token refusal. Tokens are filled before anything is written (P-48, P-96):
  {{CANDIDATE_CRD_LIST_URL}}  EX/run.json "url" (X5.2)
  {{INSTALL_DATE}}            EX/run.json "install_date" (X7.6; recorded at X7.4 from Nathan's confirmation)
  {{FREEZE_DIGESTS}}          the seven lines '<skill> <files> <digest>' X7.4 wrote to EX/installed_freeze.txt, as
                              Markdown bullets '- `<skill>` `<files> <digest>`' in that order (P-68)
Idempotent (P-104): each edit is first stated on its file. APPLIED: its filled text already stands at its anchor
once, with its anchor once (texts inserted at one anchor stack, so a landed text need not stand directly against
it); for replace, the anchor is gone and the new text is there. It is skipped. NOT_APPLIED: the anchor occurs exactly once and the new text does not occur, so it is applied.
Anything else (the text twice, the anchor missing or repeated) is MIXED, and the run is refused before any write. So
a label re-run in a new session, over a tree where some or all of it already landed, writes each text once. Refuses,
writing nothing, when a token has no value, when a filled text still carries '{{', or when any edit is MIXED.
Afterwards each inserted text occurs exactly once in its file, and each replaced anchor not at all. Prints one JSON
line per edit and the gate results.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True


def occ(text, s):
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


def fills(a):
    out = {}
    if a.run:
        run = json.loads(Path(a.run).read_text(encoding="utf-8"))
        if run.get("url"):
            out["{{CANDIDATE_CRD_LIST_URL}}"] = run["url"]
        if run.get("install_date"):
            out["{{INSTALL_DATE}}"] = run["install_date"]
    if a.installed_freeze:
        lines = [ln.split() for ln in Path(a.installed_freeze).read_text(encoding="utf-8").splitlines() if ln.strip()]
        out["{{FREEZE_DIGESTS}}"] = "\n".join(f"- `{s}` `{n} {d}`" for s, n, d in lines)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("edits")
    ap.add_argument("label")
    ap.add_argument("--run")
    ap.add_argument("--installed-freeze")
    a = ap.parse_args()
    repo = Path(a.repo)
    edits = [e for e in json.load(open(a.edits, encoding="utf-8")) if str(e["commit"]) == a.label]
    f = fills(a)
    texts = {}
    for e in edits:
        t = e["new_text"]
        for tok, val in f.items():
            t = t.replace(tok, val)
        if "{{" in t:
            print(json.dumps({"id": e["id"], "refused": "UNFILLED_TOKEN",
                              "tokens": sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", t)))}))
            raise SystemExit(1)
        texts[e["id"]] = t
    def state(text, e):
        a_, nt = e["anchor"], texts[e["id"]]
        joined = {"insert_after": a_ + nt, "insert_before": nt + a_}.get(e["action"])
        if e["action"] == "replace":
            if occ(text, a_) == 0 and occ(text, nt) >= 1:
                return "APPLIED"
            return "NOT_APPLIED" if occ(text, a_) == 1 else "MIXED"
        if joined is None:
            raise SystemExit(f"unknown action {e['action']}")
        # texts inserted at the same anchor stack (P29-D23C and P29-D23G both before `## D24`), so a landed insertion
        # need not stand directly against its anchor: it is applied when its text is there once and the anchor once
        if occ(text, a_) == 1 and occ(text, nt) == 1:
            return "APPLIED"
        return "NOT_APPLIED" if occ(text, a_) == 1 and occ(text, nt) == 0 else "MIXED"

    # state every edit first, in order, on the text as the earlier edits of this label leave it; write nothing
    # unless none is MIXED
    work, plan = {}, []
    for e in edits:
        f = e["file"]
        text = work.get(f, (repo / f).read_text(encoding="utf-8"))
        st = state(text, e)
        if st == "MIXED":
            print(json.dumps({"id": e["id"], "state": "MIXED", "anchor_count": occ(text, e["anchor"]),
                              "text_count": occ(text, texts[e["id"]])}))
            raise SystemExit(1)
        if st == "NOT_APPLIED":
            nt = texts[e["id"]]
            text = text.replace(e["anchor"], {"insert_after": e["anchor"] + nt, "insert_before": nt + e["anchor"],
                                              "replace": nt}[e["action"]], 1)
        work[f] = text
        plan.append((e, st))
    added_quote_lines, files = [], set()
    for e, st in plan:
        nt = texts[e["id"]]
        if st == "NOT_APPLIED":
            added_quote_lines += [ln for ln in nt.split("\n") if ln.startswith("> ")]
        files.add(e["file"])
        print(json.dumps({"id": e["id"], "file": e["file"], "action": e["action"], "state": st,
                          "applied": st == "NOT_APPLIED"}))
    for f, text in work.items():
        if text != (repo / f).read_text(encoding="utf-8"):
            (repo / f).write_text(text, encoding="utf-8")
    for e, st in plan:
        text = work[e["file"]]
        once = occ(text, e["anchor"]) == 0 if e["action"] == "replace" else occ(text, texts[e["id"]]) == 1
        if not once:
            print(json.dumps({"id": e["id"], "refused": "NOT_ONCE_AFTER"}))
            raise SystemExit(1)
    out = {"edits_applied": [e["id"] for e in edits], "files": sorted(files),
           "added_lines_starting_quote": len(added_quote_lines)}
    for fn in sorted(files):
        t = (repo / fn).read_bytes()
        out[fn] = {"sha256": hashlib.sha256(t).hexdigest(), "bytes": len(t),
                   "count_^## D25": len(re.findall(r"(?m)^## D25", t.decode("utf-8")))}
    print(json.dumps(out))


if __name__ == "__main__":
    main()
