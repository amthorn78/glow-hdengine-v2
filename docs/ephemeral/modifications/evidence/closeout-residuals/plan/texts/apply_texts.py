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
Each anchor must occur exactly once when applied. Refuses, writing nothing, when a token has no value, when a filled
text still carries '{{', or when an anchor count is not 1 (the files edited before a refusal are left as they are:
run it on a clean tree and `git checkout -- <file>` to retry). Prints one JSON line per edit and the gate results.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True


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
    added_quote_lines, files = [], set()
    for e in edits:
        p = repo / e["file"]
        text = p.read_text(encoding="utf-8")
        n = text.count(e["anchor"])
        if n != 1:
            print(json.dumps({"id": e["id"], "anchor_count": n, "applied": False}))
            raise SystemExit(1)
        nt = texts[e["id"]]
        if e["action"] == "insert_after":
            new = text.replace(e["anchor"], e["anchor"] + nt)
        elif e["action"] == "insert_before":
            new = text.replace(e["anchor"], nt + e["anchor"])
        elif e["action"] == "replace":
            new = text.replace(e["anchor"], nt)
        else:
            raise SystemExit(f"unknown action {e['action']}")
        added_quote_lines += [ln for ln in nt.split("\n") if ln.startswith("> ")]
        p.write_text(new, encoding="utf-8")
        files.add(e["file"])
        print(json.dumps({"id": e["id"], "file": e["file"], "action": e["action"], "anchor_count": n, "applied": True}))
    out = {"edits_applied": [e["id"] for e in edits], "files": sorted(files),
           "added_lines_starting_quote": len(added_quote_lines)}
    for fn in sorted(files):
        t = (repo / fn).read_bytes()
        out[fn] = {"sha256": hashlib.sha256(t).hexdigest(), "bytes": len(t),
                   "count_^## D25": len(re.findall(r"(?m)^## D25", t.decode("utf-8")))}
    print(json.dumps(out))


if __name__ == "__main__":
    main()
