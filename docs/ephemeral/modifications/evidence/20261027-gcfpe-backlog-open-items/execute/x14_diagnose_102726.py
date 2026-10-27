#!/usr/bin/env python3
"""X14 (Q7) and its failure diagnosis, for MODIFICATION-20261027-gcfpe-backlog-open-items.

  x14_diagnose_102726.py <x13-dir> <fetched-after> <candidate-contract> <scratch> <out>

<x13-dir> holds X13's two skills roots, root-plain and root-quoted (D28). For each root, the plan's X14 command,
plan/x12_qualify_102726.py run <root> <fetched-after> --successor-map execute/successor-pages-102726.1.json, with
--candidate-contract naming X12's candidate contract (X12 wrote it to scratch; the tool's default path under
execute/contracts/ holds only the filled release values). Then, read-only:

  revisions   each member's X14 revision against the X7 landing check (execute/landing-check-102726.1.json)
  anchors     how often each QA-closure mutation anchor of the shipped runner occurs in each QA-120 read this session
              holds: the 100926.1 page, the successor before its X6 write and the successor now (counts only)
  experiment  a scratch copy of root-plain's flowmaster-validate with the three stale anchors substituted, run with
              the same bodies: a measurement for the return, never a package (the copy is deleted afterwards)

D22: bodies are read transiently from this session's fetch records, normalized in memory (C-15) and piped on stdin;
the receipt carries flags, counts, ids, the runner's own anchor strings and error codes only.
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
E = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(E / "plan"))
import body_check as B  # noqa: E402
import normalize_fetch as nf  # noqa: E402

spec = importlib.util.spec_from_file_location("x12q", E / "plan/x12_qualify_102726.py")
Q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Q)

MAP = E / "execute/successor-pages-102726.1.json"
RUNNER = "scripts/run_gcfpe_20261027_fixtures.py"
QA120_PAGES = {"100926.1 page": "3f44590a05eb81a4a3fbc0fae65d153e", "successor": "4064590a05eb810ea503f98b34fa85aa"}
# the shipped runner's QA-120 anchors (run_gcfpe_20261027_fixtures.py, carried from the 100926.1 runner), and the
# text each would anchor on in the body the plan wrote, in its fetch form
ANCHORS = {
    "reject-source-missing-rca": "`QA_RCA_ID`",
    "reject-source-absent-crd-class-branch": "<td>`CRD`</td>",
    "reject-source-duplicate-crd-class-branch": "<td>`CRD`</td>",
}
PLAN_TEXT = {
    "QA_PASS_INTAKE_MARKERS[2] (validator)": "by repository path, the separate `QA_REPORT` and `QA_RCA` with their IDs",
    "the pipe-rendered CRD row": "| `PASS` | `CRD` |",
    "the other source anchors: `CL-E-10 — `": "`CL-E-10 — ",
    "the other source anchors: Do not infer a class": "Do not infer a class",
}
SUBS = [
    ('("reject-source-missing-rca", "QA-120", "`QA_RCA_ID`", "`OMITTED_RCA`", "QA_PASS_BODY_INTAKE")',
     '("reject-source-missing-rca", "QA-120", "`QA_RCA` with their IDs", "`OMITTED_RCA` with their IDs", '
     '"QA_PASS_BODY_INTAKE")'),
    ('("reject-source-absent-crd-class-branch", "QA-120", "<td>`CRD`</td>", "", "QA_PASS_BODY_CLASS_MAP")',
     '("reject-source-absent-crd-class-branch", "QA-120", "| `PASS` | `CRD` |", "| `PASS` |  |", '
     '"QA_PASS_BODY_CLASS_MAP")'),
    ('        anchor = producer_lines.index("<td>`CRD`</td>")\n'
     '        start, end = anchor - 2, producer_lines.index("</tr>", anchor)\n'
     '        if producer_lines[start] != "<tr>" or producer_lines[anchor - 1] != "<td>`PASS`</td>":\n'
     '            raise ValueError("Mutation anchor absent: reject-source-duplicate-crd-class-branch")\n'
     '        crd_row = "\\n".join(producer_lines[start:end + 1])',
     '        hits = [l for l in producer_lines if l.startswith("| `PASS` | `CRD` |")]\n'
     '        if len(hits) != 1:\n'
     '            raise ValueError("Mutation anchor absent: reject-source-duplicate-crd-class-branch")\n'
     '        crd_row = hits[0]'),
]


def qualify(root: Path, fetched_after: str, cand: str) -> tuple[int, dict]:
    r = subprocess.run([sys.executable, str(E / "plan/x12_qualify_102726.py"), "run", str(root), fetched_after,
                        "--successor-map", str(MAP), "--candidate-contract", cand],
                       capture_output=True, text=True, env=Q.ENV)
    return r.returncode, json.loads(r.stdout)


def fixtures_with_bodies(fv: Path, cf: Path, text: str) -> dict:
    r = subprocess.run([sys.executable, RUNNER, str(cf), "--contract", str(cf / Q.CF_CONTRACT), "--bodies-stdin"],
                       cwd=fv, input=text, capture_output=True, text=True, env=Q.ENV)
    out = {"exit": r.returncode}
    try:
        d = json.loads(r.stdout)
    except ValueError:
        last = [l for l in r.stderr.strip().splitlines() if l.strip()][-1:] or [""]
        out["error"] = last[0][:200]
        return out
    out.update({k: d.get(k) for k in ("fixture_suite_ok", "case_count", "qa_closure_source_case_count",
                                      "artifact_timing_case_count", "section_13_passed", "section_13_variants_passed")})
    out["failed_cases"] = [c.get("name") for c in d.get("cases", []) if not c.get("passed")]
    out["qa_closure_source_cases"] = {c["name"]: c["passed"] for c in d.get("cases", [])
                                      if c["name"].startswith("reject-source-") or c["name"].startswith("accept-live-source")}
    return out


def main(argv: list) -> int:
    x13, fetched_after, cand, scratch, out = Path(argv[0]), argv[1], argv[2], Path(argv[3]), Path(argv[4])
    rec = {"record_type": "GCFPE_102726_X14_BODIES", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X14", "fetched_after": fetched_after,
           "candidate_contract": {"path": "<scratch>/q/x12/contracts/" + Path(cand).name,
                                  "sha256": hashlib.sha256(Path(cand).read_bytes()).hexdigest()}}
    runs = {}
    for name in ("root-plain", "root-quoted"):
        code, r = qualify(x13 / name, fetched_after, cand)
        runs[name] = {"exit": code, **r}
    rec["runs"] = runs
    rec["roots_identical"] = runs["root-plain"] == runs["root-quoted"]

    bodies, as_of, missing, stand_in = Q.read_bodies(fetched_after, str(MAP), False)
    lc = json.load(open(E / "execute/landing-check-102726.1.json", encoding="utf-8"))["check"]["pages"]
    lc_asof = {v.get("prompt"): v.get("as_of") for v in (lc.values() if isinstance(lc, dict) else lc)}
    rec["revisions"] = {"members": len(as_of), "missing": missing, "stand_in": stand_in,
                        "moved_since_landing_check": {p: [lc_asof.get(p), as_of[p]] for p in sorted(as_of)
                                                      if lc_asof.get(p) != as_of[p]}}

    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    reads = []
    for label, pid in QA120_PAGES.items():
        for cap, rev, body in B.all_fetches(pid, root, session, 100000):
            n = nf.normalize(body)
            reads.append({"page": label, "page_id": pid, "revision": rev, "captured": cap,
                          "runner_anchors": {k: n.count(v) for k, v in ANCHORS.items()},
                          "plan_text": {k: n.count(v) for k, v in PLAN_TEXT.items()}})
            del n, body
    rec["qa120_anchor_counts"] = reads

    payload = Q.payload_of(bodies)
    del bodies
    text = json.dumps(payload)
    del payload
    work = scratch / "x14-anchor-experiment"
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    fv = work / "flowmaster-validate"
    shutil.copytree(x13 / "root-plain/flowmaster-validate", fv, ignore=shutil.ignore_patterns("__pycache__"))
    cf = x13 / "root-plain/change-flow"
    shipped = fixtures_with_bodies(x13 / "root-plain/flowmaster-validate", cf, text)
    p = fv / RUNNER
    src = p.read_text(encoding="utf-8")
    for old, new in SUBS:
        if src.count(old) != 1:
            raise SystemExit("x14: experiment substitution base moved")
        src = src.replace(old, new)
    p.write_text(src, encoding="utf-8")
    patched = fixtures_with_bodies(fv, cf, text)
    del text
    shutil.rmtree(work, ignore_errors=True)
    rec["experiment"] = {"note": "scratch copy only, deleted after the run; not a package and not a fix",
                         "substitutions": [{"old": o, "new": n} for o, n in SUBS],
                         "shipped_runner": shipped, "anchors_substituted": patched}
    rec["ok"] = all(r.get("ok") is True for r in runs.values())
    rec["d22"] = ("member bodies read transiently from this session's fetch records, normalized in memory and piped "
                  "on stdin; counts, ids, the runner's own anchor strings and error codes only")
    out.write_text(json.dumps(rec, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": rec["ok"], "roots_identical": rec["roots_identical"],
                      "shipped_runner": shipped.get("error") or shipped.get("fixture_suite_ok"),
                      "anchors_substituted": patched.get("fixture_suite_ok"), "case_count": patched.get("case_count"),
                      "moved": rec["revisions"]["moved_since_landing_check"]}))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
