#!/usr/bin/env python3
"""X18: production validation on the activated state, with the INSTALLED skills (PLAN §7).

The installed gates, the 100926.1 profile with all 55 member bodies, its fixtures with and without the bodies,
and `registry_assemble.py assertions --landed --inject` with the installed governance audit, all on fresh reads
taken by this session after <fetched-after>. D22: the bodies are read transiently from this session's fetch
records and piped on stdin; no body text or digest is written. Prints one JSON receipt: flags, counts, ids,
revisions and error codes only.

Usage: x18_validate.py <installed-skills-dir> <fetched-after ISO>
"""
import json, os, subprocess, sys
from pathlib import Path
REPO = Path("/home/user/glow-hdengine-v2")
E = REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion"
I = Path(sys.argv[1]).resolve()
FETCHED_AFTER = sys.argv[2]
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
sys.dont_write_bytecode = True
sys.path.insert(0, str(E / "plan"))
import body_check as B
SUCC = "3f74590a05eb81b69bd8c27106f7a59d"
SUCC_PIN = "2026-10-12T02:24:58.597Z"
B.EDITS["pages"]["GCFPE-MGMT-10"] = {"page_id": SUCC, "expected_last_edited": SUCC_PIN}
TARGETS = [a for n in ("flowmaster-primary", "tw-flowmaster", "change-flow", "session-branch-flowmaster", "session-relay-flowmaster", "flowmaster-validate") for a in ("--target", n)]
root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
x6 = {p["prompt"]: p["as_of"] for p in json.loads((E / "execute/x6-check.json").read_text(encoding="utf-8"))["pages"]}

bodies, as_of, captured, missing = {}, {}, {}, []
for prompt, meta in B.EDITS["pages"].items():
    if prompt == "PE":
        continue
    got = B.latest_fetch(meta["page_id"], root, session, 900, FETCHED_AFTER)
    if got is None:
        missing.append(prompt)
        continue
    captured[prompt], as_of[prompt], bodies[prompt] = got
if missing:
    print(json.dumps({"record_type": "MB008_X18_PRODUCTION_VALIDATION", "ok": False, "error": "NO_FETCH_FOUND", "missing": sorted(missing)}))
    sys.exit(2)
payload = json.dumps(bodies)
del bodies

fv, cf = I / "flowmaster-validate", I / "change-flow"
cc = cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"


def run(args, cwd, stdin=None):
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=stdin, capture_output=True, text=True, env=ENV)
    try:
        return r.returncode, json.loads(r.stdout)
    except ValueError:
        return r.returncode, {"_unparsed": (r.stdout + r.stderr)[-300:].replace(str(I), "<installed>")}


c1, prof = run([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract", cc, "--bodies-stdin"], fv, payload)
c2, fxb = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc, "--bodies-stdin"], fv, payload)
del payload
c3, fx = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc], fv)
c4, suite = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", I, *TARGETS], fv)
c5, suite_all = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", I], fv)
c6, reg = run([sys.executable, E / "plan/registry_assemble.py", "assertions", "--registry", E / "execute/candidate-registry.md",
               "--audit-root", I / "amthor-workspace-governance-audit", "--fetched-after", FETCHED_AFTER, "--since-minutes", "900",
               "--page", f"GCFPE-MGMT-10={SUCC}@{SUCC_PIN}", "--shared", f"MGMT10_URL=https://app.notion.com/p/{SUCC}",
               "--landed", "--inject"], E)


def fxsum(c, d):
    return {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "profile_errors": d.get("profile_errors"),
            "section_13_fixture_count": d.get("section_13_fixture_count"), "section_13_passed": d.get("section_13_passed"),
            "section_13_variant_count": d.get("section_13_variant_count"), "section_13_variants_passed": d.get("section_13_variants_passed"),
            "case_count": d.get("case_count"), "qa_closure_source_case_count": d.get("qa_closure_source_case_count"),
            "artifact_timing_case_count": d.get("artifact_timing_case_count"),
            "failed_cases": [x.get("name") for x in d.get("cases", []) if not x.get("passed")]}


cov = suite.get("change_contract_coverage", {})
rows = reg.get("rows", [])
receipt = {
    "record_type": "MB008_X18_PRODUCTION_VALIDATION", "step": "X18",
    "skills": "the installed directory itself, read only (flowmaster-validate 3.4.1 and the five other 100926.1 packages as installed)",
    "reads": {"fetched_after": FETCHED_AFTER, "members": len(as_of), "captured_min": min(captured.values()), "captured_max": max(captured.values()),
              "as_of_equals_x6": sorted(p for p in as_of if as_of[p] == x6.get(p)), "as_of_differs_from_x6": {p: [x6.get(p), as_of[p]] for p in as_of if as_of[p] != x6.get(p)},
              "d22": "55 member bodies read transiently from this session's fetch records and piped on stdin; no body text or digest written"},
    "profile_100926_with_bodies": {"exit": c1, "ok": prof.get("ok"), "errors": prof.get("errors"), "profile": prof.get("profile"),
        "prompt_bodies_validated": len(prof.get("prompt_bodies_validated") or []), "prompt_body_count": prof.get("prompt_body_count"),
        "prompt_body_checks_not_evaluated": prof.get("prompt_body_checks_not_evaluated"), "contract_status": prof.get("contract_status")},
    "fixtures_100926_with_bodies": fxsum(c2, fxb),
    "fixtures_100926_without_bodies": fxsum(c3, fx),
    "flowmaster_suite_targeted": {"exit": c4, "verdict": suite.get("verdict"), "suite_ok": suite.get("suite_ok"), "finding_counts": suite.get("finding_counts"),
        "self_identity": suite.get("self_identity"), "name_line_forms": suite.get("name_line_forms"),
        "skills": {n: s.get("status") for n, s in suite.get("skills", {}).items()},
        "current_profile": cov.get("gcfpe_current_direct_handoff", {}).get("profile"), "current_ok": cov.get("gcfpe_current_direct_handoff", {}).get("ok"),
        "current_fixtures_ok": cov.get("gcfpe_current_fixtures", {}).get("fixture_suite_ok"), "rows_exact": cov.get("rows_exact")},
    "flowmaster_suite_untargeted": {"exit": c5, "verdict": suite_all.get("verdict"),
        "skills_not_pass": sorted(n for n, s in suite_all.get("skills", {}).items() if s.get("status") != "PASS"), "listed_risk": "LR-1"},
    "registry_assertions": {"exit": c6, "ok": reg.get("ok"), "rows": len(rows), "rows_passing": sum(1 for r in rows if r.get("ok")),
        "assertions_evaluated": sum(r.get("assertions", 0) for r in rows), "findings_after": sum(r.get("findings_after", 0) for r in rows),
        "operations_not_landed": sum(len(r.get("operations_not_landed", [])) for r in rows),
        "injected_fired": sum(r.get("injected_fired", 0) for r in rows), "injected_missed": sum(len(r.get("injected_missed", [])) for r in rows),
        "errors": [r for r in rows if r.get("error")], "failing_rows": [r.get("prompt") for r in rows if not r.get("ok")]},
}
receipt["ok"] = (c1 == 0 and prof.get("ok") is True and receipt["profile_100926_with_bodies"]["prompt_bodies_validated"] == 55
                 and prof.get("prompt_body_checks_not_evaluated") == [] and fxb.get("fixture_suite_ok") is True and fx.get("fixture_suite_ok") is True
                 and suite.get("suite_ok") is True and (suite.get("name_line_forms") or {}).get("ok") is True
                 and set(receipt["flowmaster_suite_untargeted"]["skills_not_pass"]) <= {"human-design-reading-flowmaster"}
                 and reg.get("ok") is True and len(rows) == 55 and receipt["registry_assertions"]["operations_not_landed"] == 0
                 and len(as_of) == 55)
print(json.dumps(receipt, indent=1, sort_keys=True))
