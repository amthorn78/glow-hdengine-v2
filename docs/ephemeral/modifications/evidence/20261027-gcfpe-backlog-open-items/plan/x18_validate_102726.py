#!/usr/bin/env python3
"""X18 (EXECUTE production validation): the activated GCFPE-20261027.1 / 102726.1 state checked with the INSTALLED
skills, for MODIFICATION-20261027-gcfpe-backlog-open-items. Adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/x18_validate.py (repair R2).

  x18_validate_102726.py run <installed-skills-dir> <fetched-after> --successor-map M [--registry R]
                             [--landing-report L] [--stand-in-ok]
        The installed 102726.1 profile with all 56 member bodies, its fixtures with and without the bodies, the
        flowmaster suite targeted and untargeted, and registry_assemble_102726.py assertions --landed --inject on the
        selected registry R (default docs/prompt_ecosystem_management/project-prompt-contract-registry.md) with the
        installed governance audit, all on fresh reads this session took after <fetched-after>. With L (EXECUTE's
        body_check.py check report), each read's revision is compared with the landing check's.
  x18_validate_102726.py selftest
        each check this file adds fails on its injected defect.

C-15 (repair R2): every body is normalize_fetch.normalize(read) before the profile or its fixtures see it (and the
registry assertions normalize inside registry_assemble_102726.py's body form); the run refuses to pipe a payload that is
not in that form. C-21: the untargeted suite passes when its only findings are the three pre-existing
human-design-reading-flowmaster findings. D22: bodies are read transiently from this session's fetch records and piped
on stdin; no body text or digest is written; the receipt carries flags, counts, ids, revisions and error codes only.
Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import x12_qualify_102726 as X12  # noqa: E402  (payload_of, payload_normalized, read_bodies, suite_ok_c21, fxsum)

REPO = HERE.parents[5]
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
REGISTRY = REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
TARGETS = [a for n in ("flowmaster-primary", "tw-flowmaster", "change-flow", "session-branch-flowmaster",
                       "session-relay-flowmaster", "flowmaster-validate") for a in ("--target", n)]


def run_json(args, cwd, stdin=None, hide=None):
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=stdin, capture_output=True, text=True, env=ENV)
    try:
        return r.returncode, json.loads(r.stdout)
    except ValueError:
        tail = (r.stdout + r.stderr)[-300:]
        return r.returncode, {"_unparsed": tail.replace(str(hide), "<installed>") if hide else tail}


def run(argv: list) -> int:
    I, fetched_after = Path(argv[0]).resolve(), argv[1]
    map_path = argv[argv.index("--successor-map") + 1]
    registry = Path(argv[argv.index("--registry") + 1]) if "--registry" in argv else REGISTRY
    landing = (json.loads(Path(argv[argv.index("--landing-report") + 1]).read_text(encoding="utf-8"))
               if "--landing-report" in argv else None)
    bodies, as_of, missing, stand_in = X12.read_bodies(fetched_after, map_path, "--stand-in-ok" in argv)
    if missing:
        print(json.dumps({"record_type": "GCFPE_102726_X18_PRODUCTION_VALIDATION", "ok": False, "error": "NO_FETCH_FOUND",
                          "missing": missing}))
        return 2
    payload = X12.payload_of(bodies)
    del bodies
    if not X12.payload_normalized(payload):
        raise SystemExit("x18: refusing to pipe a payload that is not in the normalized form (C-15)")
    text = json.dumps(payload)
    del payload
    fv, cf = I / "flowmaster-validate", I / "change-flow"
    cc = cf / X12.CF_CONTRACT
    c1, prof = run_json([sys.executable, "scripts/validate_gcfpe_20261027.py", cf, "--contract", cc, "--bodies-stdin"], fv, text, I)
    c2, fxb = run_json([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", cf, "--contract", cc, "--bodies-stdin"], fv, text, I)
    del text
    c3, fx = run_json([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", cf, "--contract", cc], fv, None, I)
    c4, suite = run_json([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", I, *TARGETS], fv, None, I)
    c5, suite_all = run_json([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", I], fv, None, I)
    reg_args = [sys.executable, HERE / "registry_assemble_102726.py", "assertions", "--registry", registry,
                "--audit-root", I / "amthor-workspace-governance-audit", "--successor-map", map_path,
                "--fetched-after", fetched_after, "--since-minutes", "900", "--landed", "--inject"]
    c6, reg = run_json(reg_args, HERE, None, I)
    landing_as_of = {p["prompt"]: p.get("as_of") for p in (landing or {}).get("pages", [])} if landing else {}
    rows = reg.get("rows", [])
    s_ok, s_change, s_pre = X12.suite_ok_c21(suite_all)
    cov = suite.get("change_contract_coverage", {})
    receipt = {
        "record_type": "GCFPE_102726_X18_PRODUCTION_VALIDATION", "step": "X18", "stand_in": stand_in,
        "skills": "the installed directory itself, read only",
        "reads": {"fetched_after": fetched_after, "members": len(as_of), "as_of_min": min(as_of.values()),
                  "as_of_max": max(as_of.values()), "text_form": "normalize_fetch.normalize (C-15)",
                  "as_of_equals_landing_check": sorted(p for p in as_of if landing_as_of.get(p) == as_of[p]) if landing else None,
                  "as_of_differs_from_landing_check": {p: [landing_as_of.get(p), as_of[p]] for p in as_of
                                                       if landing_as_of.get(p) != as_of[p]} if landing else None,
                  "d22": "member bodies read transiently from this session's fetch records, normalized in memory and "
                         "piped on stdin; no body text or digest written"},
        "profile_102726_with_bodies": {"exit": c1, "ok": prof.get("ok"), "errors": prof.get("errors"), "profile": prof.get("profile"),
                                       "prompt_bodies_validated": len(prof.get("prompt_bodies_validated") or []),
                                       "prompt_body_checks_not_evaluated": prof.get("prompt_body_checks_not_evaluated"),
                                       "contract_status": prof.get("contract_status")},
        "fixtures_102726_with_bodies": X12.fxsum(c2, fxb),
        "fixtures_102726_without_bodies": X12.fxsum(c3, fx),
        "flowmaster_suite_targeted": {"exit": c4, "verdict": suite.get("verdict"), "suite_ok": suite.get("suite_ok"),
                                      "self_identity": suite.get("self_identity"), "name_line_forms": suite.get("name_line_forms"),
                                      "current_profile": cov.get("gcfpe_current_direct_handoff", {}).get("profile"),
                                      "current_ok": cov.get("gcfpe_current_direct_handoff", {}).get("ok")},
        "flowmaster_suite_untargeted": {"exit": c5, "verdict": suite_all.get("verdict"), "ok_c21": s_ok,
                                        "findings_from_this_change": s_change, "findings_preexisting": s_pre},
        "registry_assertions": {"exit": c6, "ok": reg.get("ok"), "text_form": reg.get("text_form"), "rows": len(rows),
                                "rows_passing": sum(1 for r in rows if r.get("ok")),
                                "assertions_evaluated": sum(r.get("assertions", 0) for r in rows),
                                "findings_after": sum(r.get("findings_after", 0) for r in rows),
                                "operations_not_landed": sum(len(r.get("operations_not_landed", [])) for r in rows),
                                "injected_fired": sum(r.get("injected_fired", 0) for r in rows),
                                "injected_missed": sum(len(r.get("injected_missed", [])) for r in rows),
                                "errors": [r.get("prompt") for r in rows if r.get("error")],
                                "failing_rows": [r.get("prompt") for r in rows if not r.get("ok")]},
    }
    receipt["ok"] = (c1 == 0 and prof.get("ok") is True and receipt["profile_102726_with_bodies"]["prompt_bodies_validated"] == X12.MEMBERS
                     and prof.get("prompt_body_checks_not_evaluated") == [] and fxb.get("fixture_suite_ok") is True
                     and fx.get("fixture_suite_ok") is True and suite.get("suite_ok") is True
                     and (suite.get("name_line_forms") or {}).get("ok") is True and s_ok
                     and reg.get("ok") is True and len(rows) == X12.MEMBERS
                     and receipt["registry_assertions"]["operations_not_landed"] == 0 and len(as_of) == X12.MEMBERS
                     and not stand_in)
    print(json.dumps(receipt, indent=1, sort_keys=True))
    return 0 if receipt["ok"] else 1


def selftest(argv: list) -> int:
    rows = {}
    fetch = {"CL-C-10": "You are Isis, continuing <code>QA\\_REPORT\\_ID</code>"}
    p = X12.payload_of(fetch)
    rows["payload_normalized"] = p["CL-C-10"] == "You are Isis, continuing `QA_REPORT_ID`"
    rows["injected_raw_payload_refused"] = not X12.payload_normalized(fetch) and X12.payload_normalized(p)
    rows["targets_six"] = len(TARGETS) == 12
    import registry_assemble_102726 as RA
    line = "<code>QA\\_RCA\\_ID</code> <b>x</b>"
    rows["registry_assertion_text_normalizes"] = RA.assertion_text(line) == "`QA_RCA_ID` **x**"
    rows["injected_raw_registry_text_differs"] = RA.assertion_text(line) != line
    ok = all(rows.values())
    print(json.dumps({"mode": "selftest", "rows": rows, "ok": ok}, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("run", "selftest"):
        sys.exit(__doc__)
    sys.exit((run if sys.argv[1] == "run" else selftest)(sys.argv[2:]))
