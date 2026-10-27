#!/usr/bin/env python3
"""AM-8's check, each way, for MODIFICATION-20261027-gcfpe-backlog-open-items.

  am8_runner_check_102726.py <built-skills-root> <fetched-after> [--receipt R]

AM-8 moved the built runner's QA-120 source-case anchors to the body PART-07 and PART-13 wrote, with the CRD class
cell taken in either table rendering. On the 56 bodies this session read after <fetched-after> (the successor map's
pages), the built flowmaster-validate's run_gcfpe_20261027_fixtures.py --bodies-stdin is run five times:

  pass_pipe         the bodies as read (QA-120's class map in the pipe rendering): every case passes, the nine
                    QA-closure source cases among them
  pass_html         QA-120's class map re-rendered as an HTML table (the rendering the 100926.1 precedent read): every
                    case passes
  stop_rca          QA-120 without the RCA intake sentence's anchor: the runner stops on reject-source-missing-rca
  stop_cell         QA-120 with the CRD class cell in neither rendering: it stops on reject-source-absent-crd-class-branch
  stop_dup          QA-120 whose CRD pipe row does not begin its line: it stops on
                    reject-source-duplicate-crd-class-branch

A stop is a non-zero exit whose last error line names the case: the runner refuses rather than reporting a pass it
did not test. D22: bodies are read transiently from this session's fetch records, normalized in memory (C-15), varied
in memory and piped on stdin; the receipt carries flags, counts, case names and error lines only.
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
E = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(E / "plan"))
spec = importlib.util.spec_from_file_location("x12q", E / "plan/x12_qualify_102726.py")
Q = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Q)

MAP = E / "execute/successor-pages-102726.1.json"
RUNNER = "scripts/run_gcfpe_20261027_fixtures.py"
RCA = "`QA_RCA` with their IDs"
CRD_PIPE = "| `PASS` | `CRD` |"
TABLE_HEAD = re.compile(r"(?m)^\| Result \| Verified change class \| Required receiver \|\n\| --- \| --- \| --- \|\n((?:\|.*\|\n)+)")


def as_html(body: str) -> str:
    """QA-120's pipe class map as an HTML table, one tag per line (the form the 100926.1 runner's anchors read)."""
    found = list(TABLE_HEAD.finditer(body))
    if len(found) != 1:
        raise SystemExit("am8: QA-120's class map not found once in the pipe rendering")
    m = found[0]
    rows = [["Result", "Verified change class", "Required receiver"]]
    rows += [[c.strip() for c in line.strip()[1:-1].split(" | ")] for line in m.group(1).splitlines()]
    out = ['<table header-row="true">']
    for row in rows:
        out += ["<tr>"] + [f"<td>{cell}</td>" for cell in row] + ["</tr>"]
    out.append("</table>")
    return body[:m.start()] + "\n".join(out) + "\n" + body[m.end():]


def run(fv: Path, cf: Path, bodies: dict) -> dict:
    r = subprocess.run([sys.executable, RUNNER, str(cf), "--contract", str(cf / Q.CF_CONTRACT), "--bodies-stdin"],
                       cwd=fv, input=json.dumps(bodies), capture_output=True, text=True, env=Q.ENV)
    out = {"exit": r.returncode}
    try:
        d = json.loads(r.stdout)
    except ValueError:
        lines = [l for l in r.stderr.strip().splitlines() if l.strip()]
        out["error"] = (lines[-1] if lines else "")[:200]
        return out
    out.update({k: d.get(k) for k in ("fixture_suite_ok", "case_count", "qa_closure_source_case_count")})
    out["failed_cases"] = [c.get("name") for c in d.get("cases", []) if not c.get("passed")]
    out["source_cases_passed"] = sum(bool(c.get("passed")) for c in d.get("cases", [])
                                     if c["name"].startswith(("reject-source-", "accept-live-source")))
    return out


def main(argv: list) -> int:
    X, fetched_after = Path(argv[0]).resolve(), argv[1]
    receipt = Path(argv[argv.index("--receipt") + 1]) if "--receipt" in argv else None
    bodies, as_of, missing, stand_in = Q.read_bodies(fetched_after, str(MAP), False)
    if missing or stand_in:
        raise SystemExit(f"am8: missing {missing}, stand_in {stand_in}")
    base = Q.payload_of(bodies)
    del bodies
    if not Q.payload_normalized(base):
        raise SystemExit("am8: the payload is not in the normalized form (C-15)")
    qa = base["QA-120"]
    if qa.count(RCA) != 1 or qa.count(CRD_PIPE) != 1 or "<td>`CRD`</td>" in qa:
        raise SystemExit("am8: QA-120 is not in the form this check expects (one RCA anchor, one pipe CRD row)")

    def varied(text: str) -> dict:
        b = dict(base)
        b["QA-120"] = text
        return b

    fv, cf = X / "flowmaster-validate", X / "change-flow"
    runs = {
        "pass_pipe": run(fv, cf, base),
        "pass_html": run(fv, cf, varied(as_html(qa))),
        "stop_rca": run(fv, cf, varied(qa.replace(RCA, "`QA_RCA`"))),
        "stop_cell": run(fv, cf, varied(qa.replace(CRD_PIPE, "| `PASS` | `CRD-X` |"))),
        "stop_dup": run(fv, cf, varied(qa.replace("\n" + CRD_PIPE, "\n " + CRD_PIPE))),
    }
    del base, qa
    want_stop = {"stop_rca": "reject-source-missing-rca", "stop_cell": "reject-source-absent-crd-class-branch",
                 "stop_dup": "reject-source-duplicate-crd-class-branch"}
    rows = {}
    for k in ("pass_pipe", "pass_html"):
        r = runs[k]
        rows[k] = (r["exit"] == 0 and r.get("fixture_suite_ok") is True and r.get("failed_cases") == []
                   and r.get("qa_closure_source_case_count") == 9 and r.get("source_cases_passed") == 9)
    for k, case in want_stop.items():
        r = runs[k]
        rows[k] = r["exit"] != 0 and r.get("error", "").endswith(f"Mutation anchor absent: {case}")
    rec = {"record_type": "GCFPE_102726_AM8_RUNNER_CHECK", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "built_root": X.name, "fetched_after": fetched_after, "members": len(as_of),
           "runs": runs, "rows": rows, "ok": all(rows.values()),
           "d22": "member bodies read transiently from this session's fetch records, normalized and varied in memory, "
                  "piped on stdin; flags, counts, case names and error lines only"}
    text = json.dumps(rec, indent=1, sort_keys=True)
    if receipt:
        receipt.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
