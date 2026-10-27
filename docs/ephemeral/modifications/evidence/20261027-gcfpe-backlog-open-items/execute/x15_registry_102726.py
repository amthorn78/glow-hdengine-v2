#!/usr/bin/env python3
"""X15 (Q8, the registry) for EXECUTE of MODIFICATION-20261027-gcfpe-backlog-open-items.

  x15_registry_102726.py <installed-skills-root> <scratch> --parts <candidate-parts> --fetched-after T [--receipt R]

PLAN X15 on the real inputs, in the gate order of plan/a3_registry_dryrun_102726.py (A3's PLAN form of Q8):

  base        the selected GCFPE-PCR-20261009.1 registry read from `main` with `git show` (W7-D9)
  inputs      the installed amthor-workspace-governance-audit and glow-graph-contract, copied to <scratch>; X11's
              candidate parts; the real successor map; page revisions from X7's landing-check report
              (execute/landing-check-102726.1.json check.pages[*].as_of), written to <scratch> as {"revisions": ...},
              one form load_revisions reads; a build from the report's own form must be byte-identical; the catalog
              record execute/notion-controls-102726.1.json (C-22)
  gates       build --stage candidate to execute/candidate-registry.md, and a byte-identical rebuild; check --stage
              candidate; assertions --synthetic --inject; assertions on the bodies as read after T, --landed
              --inject (C-15's text form); build --stage selected with a stand-in @PROMOTION_APPROVAL_DATE (to
              <scratch>; the real one is X26's) and check --stage selected; compare; selftest

Writes execute/candidate-registry.md, <scratch> and, with --receipt, that file. D22: the body form reads this
session's fetch records transiently and reports counts, ids and booleans only. Run with PYTHONDONTWRITEBYTECODE=1;
CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
E = HERE.parent
REPO = E.parents[4]
TOOL = E / "plan/registry_assemble_102726.py"
REG = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
MAP = HERE / "successor-pages-102726.1.json"
CATREC = HERE / "notion-controls-102726.1.json"
LANDING = HERE / "landing-check-102726.1.json"
CAND = HERE / "candidate-registry.md"
APPROVAL_STAND_IN = "2026-10-27"
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
       "CLAUDE_CODE_SESSION_ID": os.environ.get("CLAUDE_CODE_SESSION_ID", ""), "HOME": os.environ.get("HOME", "/root")}


def run(args) -> tuple[int, dict | None, str]:
    p = subprocess.run([sys.executable, str(TOOL), *map(str, args)], capture_output=True, text=True, env=ENV)
    try:
        return p.returncode, json.loads(p.stdout), p.stderr[-400:]
    except json.JSONDecodeError:
        return p.returncode, None, (p.stdout + p.stderr)[-400:]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("installed"); ap.add_argument("scratch")
    ap.add_argument("--parts", required=True); ap.add_argument("--fetched-after", required=True)
    ap.add_argument("--receipt")
    a = ap.parse_args()
    SK, W = Path(a.installed), Path(a.scratch).resolve() / "x15-registry"
    if "/skills/synced/" in str(W):
        raise SystemExit("refusing to write under the synced install directory")
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    for k in ("amthor-workspace-governance-audit", "glow-graph-contract"):
        shutil.copytree(SK / k, W / k, ignore=shutil.ignore_patterns("__pycache__"))
    AR, GC = W / "amthor-workspace-governance-audit", W / "glow-graph-contract"
    main_rev = subprocess.run(["git", "-C", str(REPO), "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
    base = W / "base-registry-main.md"
    base.write_bytes(subprocess.run(["git", "-C", str(REPO), "show", f"origin/main:{REG}"], capture_output=True).stdout)
    # X7's revisions in the {"revisions": {prompt: as_of}} form load_revisions reads; the build is byte-identical to
    # one from the body_check.py report form (checked below), and the tool's selftest mutates only this form
    report = json.loads(LANDING.read_text(encoding="utf-8"))["check"]
    revs, revs_report = W / "landing-check-revisions.json", W / "landing-check-report.json"
    revs.write_text(json.dumps({"source": "execute/landing-check-102726.1.json check.pages[*].as_of (X7)",
                                "revisions": {p["prompt"]: p["as_of"] for p in report["pages"] if "as_of" in p}},
                               indent=1) + "\n", encoding="utf-8")
    revs_report.write_text(json.dumps(report, indent=1) + "\n", encoding="utf-8")
    common = ["--base-registry", base, "--audit-root", AR, "--graph-contract", GC, "--parts", a.parts, "--map", MAP,
              "--revisions", revs, "--catalog-record", CATREC]
    ck = ["--audit-root", AR, "--graph-contract", GC, "--parts", a.parts]
    rec = {"record_type": "GCFPE_102726_X15_REGISTRY", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
           "step": "X15", "stand_in_used": False,
           "stand_ins": [f"@PROMOTION_APPROVAL_DATE {APPROVAL_STAND_IN} in the selected-stage build only (to scratch); "
                         "the real value is X26's"],
           "base": {"source": f"git show origin/main:{REG}", "origin_main": main_rev, "sha256": sha(base),
                    "bytes": base.stat().st_size},
           "inputs": {"audit_root": "installed amthor-workspace-governance-audit (copied)",
                      "graph_contract": "installed glow-graph-contract (copied)", "parts_sha_count": None,
                      "revisions": "execute/landing-check-102726.1.json check.pages[*].as_of (X7), "
                                   f"{sum(1 for p in report['pages'] if 'as_of' in p)} pages",
                      "catalog_record": "execute/notion-controls-102726.1.json @CATALOG_PAGE_ID "
                                        + json.loads(CATREC.read_text(encoding="utf-8"))["values"]["@CATALOG_PAGE_ID"],
                      "fetched_after": a.fetched_after}}
    parts = sorted(Path(a.parts).rglob("*"))
    rec["inputs"]["parts_sha_count"] = len([p for p in parts if p.is_file()])
    cand2, sel = W / "candidate-registry-again.md", W / "selected-registry-standin.md"
    rc, b, err = run(["build", "--stage", "candidate", "--out", CAND, *common])
    rec["build_candidate"] = {"exit": rc, "ok": (b or {}).get("ok"), "error": None if rc == 0 else err,
                              **{k: (b or {}).get(k) for k in ("rows", "bytes", "read_back_equal", "successor_rows", "kept_rows",
                                                               "added_rows", "hand_edits", "plan_assertions_added", "stand_in_used")}}
    if rc == 0:
        rec["build_candidate"]["sha256"] = sha(CAND)
    rc2, _, _ = run(["build", "--stage", "candidate", "--out", cand2, *common])
    rec["rebuild_byte_identical"] = rc == 0 and rc2 == 0 and CAND.read_bytes() == cand2.read_bytes()
    cand3 = W / "candidate-registry-report-form.md"
    form = [x if x != revs else revs_report for x in common]
    rc3, _, _ = run(["build", "--stage", "candidate", "--out", cand3, *form])
    rec["report_form_build_byte_identical"] = rc == 0 and rc3 == 0 and CAND.read_bytes() == cand3.read_bytes()
    rc, c, err = run(["check", "--stage", "candidate", "--registry", CAND, *ck])
    rec["check_candidate"] = {"exit": rc, **(c or {"error": err})}
    rc, s, err = run(["assertions", "--registry", CAND, "--audit-root", AR, "--synthetic", "--inject"])
    rec["assertions_synthetic_inject"] = {"exit": rc, **({k: v for k, v in (s or {}).items() if k != "per_row"} if s else {"error": err}),
                                          "required_reported_total": sum(r["required_reported"] for r in (s or {}).get("per_row", [])),
                                          "forbidden_injected_reported_total": sum(r["forbidden_injected_reported"] for r in (s or {}).get("per_row", []))}
    rc, bd, err = run(["assertions", "--registry", CAND, "--audit-root", AR, "--successor-map", MAP, "--landed", "--inject",
                       "--fetched-after", a.fetched_after])
    rows = (bd or {}).get("rows", [])
    rec["assertions_body_landed_inject"] = {
        "exit": rc, "error": None if bd else err,
        **{k: (bd or {}).get(k) for k in ("form", "text_form", "stand_in", "rows_total", "rows_ok", "findings_total",
                                           "rows_with_findings", "ok")},
        "rows_not_fetched": [r["prompt"] for r in rows if r.get("error")],
        "operations_not_landed": {r["prompt"]: r["operations_not_landed"] for r in rows if r.get("operations_not_landed")},
        "injected_fired_total": sum(r.get("injected_fired", 0) for r in rows),
        "injected_missed": {r["prompt"]: r["injected_missed"] for r in rows if r.get("injected_missed")},
        "rows_failing": [r["prompt"] for r in rows if not r.get("ok")],
        "as_of_min": min((r["as_of"] for r in rows if r.get("as_of")), default=None),
        "as_of_max": max((r["as_of"] for r in rows if r.get("as_of")), default=None)}
    rc, b, err = run(["build", "--stage", "selected", "--out", sel, *common, "--set", f"@PROMOTION_APPROVAL_DATE={APPROVAL_STAND_IN}"])
    rec["build_selected_standin"] = {"exit": rc, "ok": (b or {}).get("ok"), "error": None if rc == 0 else err}
    rc, c, err = run(["check", "--stage", "selected", "--registry", sel, *ck])
    rec["check_selected_standin"] = {"exit": rc, **{k: (c or {}).get(k) for k in ("ok", "validator_errors", "deriver_drift", "rows",
                                                                                   "rows_active", "header_values_ok")}}
    rc, m, err = run(["compare", CAND, sel, "--audit-root", AR])
    rec["compare"] = {"exit": rc, **(m or {"error": err})}
    rc, t, err = run(["selftest", "--scratch", W / "selftest", *common])
    rec["selftest"] = {"exit": rc, **(t or {"error": err})}
    rec["ok"] = all([rec["build_candidate"]["ok"] is True, rec["rebuild_byte_identical"], rec["report_form_build_byte_identical"],
                     rec["check_candidate"].get("ok") is True, rec["assertions_synthetic_inject"].get("ok") is True,
                     rec["assertions_body_landed_inject"].get("ok") is True,
                     rec["assertions_body_landed_inject"].get("rows_total") == 56,
                     rec["build_selected_standin"]["ok"] is True, rec["check_selected_standin"].get("ok") is True,
                     rec["compare"].get("ok") is True, rec["selftest"].get("selftest_ok") is True])
    cand2.unlink(missing_ok=True)
    cand3.unlink(missing_ok=True)
    if a.receipt:
        Path(a.receipt).write_text(json.dumps(rec, indent=1, ensure_ascii=False, default=str) + "\n", encoding="utf-8")
    print(json.dumps({k: (v.get("ok") if isinstance(v, dict) and "ok" in v else v) for k, v in rec.items()
                      if k in ("build_candidate", "rebuild_byte_identical", "check_candidate", "assertions_synthetic_inject",
                               "report_form_build_byte_identical", "assertions_body_landed_inject",
                               "build_selected_standin", "check_selected_standin",
                               "compare", "ok")} | {"selftest": rec["selftest"].get("selftest_ok")}, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
