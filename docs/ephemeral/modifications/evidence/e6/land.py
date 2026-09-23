#!/usr/bin/env python3
"""E6 step 4 and step 5 (spec v2 §11): land the reviewed body edits in Notion, one page at a time, and check the
readback. Bodies live only in this process's memory. They are read from the session's Notion fetch results, the
transient harness files that D22 allows, which are never written, kept or deleted by this script. Nothing is hashed or
byte-compared (prompt-corpus-policy.md).

  plan  <PID> <PAGE_ID>   the latest fetch of the page -> body_rules.apply -> minimal search-and-replace operations
                          for Notion `update_content`. Stdout: {"pid", "ops": [{"old_str", "new_str"}], "applied",
                          "not_found", "notes", "placed_once", "precheck"}. precheck runs the step-5 checks on the
                          text the operations produce, before anything is landed.
  check <PID> <PAGE_ID>   the latest fetch of the page (the readback) -> the step-5 checks. Stdout carries no body
                          text: validator verdict, registry-assertion findings (matched guard phrases of at most 12
                          words only), placement counts.

Step-5 checks, the E3 form: the installed validate_gcfpe_20260914.py with --bodies-stdin on the body; the page's
registry assertions from the repository registry (0 findings); every canonical text the body should carry placed
exactly once (body_rules.placement_counts).
usage: PYTHONDONTWRITEBYTECODE=1 python3 land.py plan|check <PID> <PAGE_ID>
"""
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
REPO = HERE.parents[4]
sys.path.insert(0, str(HERE.parent / "e3"))
import body_rules as R  # noqa: E402

SKILLS = Path("/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502")
REG = REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
sys.path.insert(0, str(SKILLS / "amthor-workspace-governance-audit/scripts"))
import audit_workspace_governance as A  # noqa: E402

ROOT = "/root/.claude/projects/-home-user-glow-hdengine-v2"


def candidates():
    files = glob.glob(ROOT + "/*.jsonl") + glob.glob(ROOT + "/*/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(ROOT + "/*/workflows/**/*.jsonl", recursive=True) + glob.glob(ROOT + "/*/tool-results/*")
    return sorted(files, key=os.path.getmtime)


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
    """The body of the most recent fetch of `page` found in the session's harness files, with its fetch time."""
    page = page.replace("-", "")
    best = None
    for f in candidates():
        try:
            raw = open(f, encoding="utf-8").read()
        except Exception:
            continue
        for line in (raw.splitlines() if f.endswith(".jsonl") else [raw]):
            try:
                obj = json.loads(line)
            except Exception:
                continue
            for t in texts(obj):
                if 'Here is the result of \\"fetch\\"' not in t and 'Here is the result of "fetch"' not in t:
                    continue
                try:
                    inner = json.loads(t)["text"]
                except Exception:
                    inner = t
                if page not in inner[:800].replace("-", ""):
                    continue
                m = re.search(r"<content>\n?(.*)</content>", inner, re.S)
                if m:
                    ts = re.search(r"as of (\S+):", inner)
                    best = (ts.group(1) if ts else "", m.group(1))
    if best is None:
        raise SystemExit(f"no fetch of {page} found")
    return best


def ops_for(old, new):
    """Minimal search-and-replace operations turning `old` into `new`; each old_str unique in `old`."""
    a, b = old.splitlines(keepends=True), new.splitlines(keepends=True)  # line ends travel with their lines
    groups = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            groups.append([i1, i2, j1, j2])
    out = []
    for g in groups:
        i1, i2, j1, j2 = g
        while True:  # widen with equal context until the old text is non-empty and unique
            s = "".join(a[i1:i2])
            if s.strip() and old.count(s) == 1:
                break
            if i1 > 0 and (not out or i1 > out[-1][1]):
                i1 -= 1; j1 -= 1
            elif i2 < len(a):
                i2 += 1; j2 += 1
            else:
                raise SystemExit("cannot make a unique operation")
        if out and i1 < out[-1][1]:  # overlaps the previous operation: merge
            p = out.pop(); i1, j1 = p[0], p[2]
        out.append([i1, i2, j1, j2])
    ops = [{"old_str": "".join(a[i1:i2]), "new_str": "".join(b[j1:j2])} for i1, i2, j1, j2 in out]
    for op in ops:
        assert old.count(op["old_str"]) == 1
    return ops


def simulate(body, ops):
    """The text Notion will hold after the operations, applied in order as update_content applies them."""
    t = body
    for op in ops:
        assert t.count(op["old_str"]) == 1, "an operation is not unique at its turn"
        t = t.replace(op["old_str"], op["new_str"])
    return t


def checks(pid, text):
    nph, _ = R.nph_from_registry(str(REG))
    contract = SKILLS / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
    p = subprocess.run([sys.executable, str(SKILLS / "flowmaster-validate/scripts/validate_gcfpe_20260914.py"),
                        str(SKILLS / "change-flow"), "--contract", str(contract), "--bodies-stdin"],
                       input=json.dumps({pid: text}), capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    v = json.loads(p.stdout)
    reg = A.load_data(REG)
    row = next(r for r in reg["prompts"] if r["prompt_key"] == pid)
    found = sorted({(f["rule_id"], f["observed"]["summary"]) for f in A._evaluate_assertions(row, text, "e6")})
    # Notion stores paragraphs as blocks, so a blank line between paragraphs reads back as one line break. Placement
    # is counted with runs of blank lines collapsed in both the body and the canonical texts; nothing else changes.
    collapse = lambda x: re.sub(r"\n{2,}", "\n", x)  # noqa: E731
    saved = dict(R.T)
    try:
        R.T.update({k: collapse(v) for k, v in saved.items() if isinstance(v, str)})
        placed = R.placement_counts(pid, collapse(text), nph)
    finally:
        R.T.clear(); R.T.update(saved)
    return {"validator_exit": p.returncode, "validator_ok": v.get("ok"), "validated": v.get("prompt_bodies_validated"),
            "not_evaluated": v.get("prompt_body_checks_not_evaluated"), "validator_errors": v.get("errors"),
            "registry_findings": found, "placed_once": placed,
            "pass": p.returncode == 0 and v.get("ok") is True and not found and all(n == 1 for n in placed.values())}


if __name__ == "__main__":
    mode, pid, page = sys.argv[1:4]
    ts, body = latest_body(page)
    if mode == "plan":
        # Never plan twice: a page that already carries C-TOP (every main-ecosystem body gets it) has been landed.
        # GCFPE-MGMT-10 gets no C-TOP; it is landed once its release header lines are gone.
        flat = re.sub(r"\n{2,}", "\n", body)
        landed = (re.sub(r"\n{2,}", "\n", R.T["C-TOP"]) in flat) if pid != "GCFPE-MGMT-10" else \
            not re.search(r"(?m)^[ \t>*_|`#-]*(?:Prompt [Vv]ersion|Ecosystem release|Set)\b", flat[:2000])
        if landed:
            print(json.dumps({"pid": pid, "fetched": ts, "refused": "ALREADY_LANDED: run check, not plan"}))
            raise SystemExit(3)
        edited, rep = R.apply({pid: body}, str(REG))
        r = rep[pid]
        ops = ops_for(body, edited[pid])
        # precheck runs on the text the operations produce, not on the rules output: no body is compared
        print(json.dumps({"pid": pid, "fetched": ts, "ops": ops, "applied": r.get("applied"),
                          "not_found": r.get("not_found"), "notes": r.get("notes"),
                          # as Notion will store it: a blank line between paragraphs reads back as one line break
                          "precheck": checks(pid, re.sub(r"\n{2,}", "\n", simulate(body, ops)))}, ensure_ascii=False))
    else:
        print(json.dumps({"pid": pid, "fetched": ts, **checks(pid, body)}, ensure_ascii=False))
