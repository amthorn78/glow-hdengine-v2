#!/usr/bin/env python3
"""X12 (EXECUTE qualification): the shipped 102726.1 validators from the built packages over every member body, for
MODIFICATION-20261027-gcfpe-backlog-open-items. Adapted from
docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/x12_qualify.py (repair R2).

  x12_qualify_102726.py run <built-skills-root> <fetched-after> --successor-map M [--candidate-contract C]
                            [--stand-in-ok]
        <built-skills-root> holds the four built packages beside the other installed skills (read only). Every member
        of the 56 is read from this session's fetch records (body_check.py's D22 reader; the successor pages come
        from the map M), and the bodies go on stdin to flowmaster-validate's validate_gcfpe_20261027.py and
        run_gcfpe_20261027_fixtures.py (with and without bodies); validate_flowmaster.py runs over the root; the
        candidate and production 102726.1 contracts must be release-semantically equal outside their lifecycle keys.
  x12_qualify_102726.py selftest [<built-skills-root>]
        each check this file adds fails on its injected defect (with a built root, also the built validator's
        QA-120 PASS intake check on a normalized and a raw synthetic body).

C-15 (repair R2): every body is normalize_fetch.normalize(read) (the Markdown form) before any validator sees it, and
the run refuses to pipe a payload that is not in that form (normalize(v) == v for every body). C-21: the suite gate
passes when its only findings are the three pre-existing human-design-reading-flowmaster FMV-SKILL-STRUCTURE-001
findings, named. D22: bodies travel on a pipe only and are never written; the receipt carries flags, counts, ids and
error codes only. Run with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import normalize_fetch as nf  # noqa: E402

E = HERE.parent
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
CF_CONTRACT = "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json"
DEFAULT_CANDIDATE = E / "execute/contracts/gcfpe-20261027.1-102726.1-candidate-contract.json"
MEMBERS = 56
# C-21: the findings the unchanged installed suite already reports; nothing else may appear
PREEXISTING_SUITE_FINDINGS = {
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: HUMAN_DESIGN_READING_SPECIALIZATION_REVISION: 1.0.1"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster",
     "missing specialization contract: AUTHOR_SKILL_TARGET_SURFACE_UNAVAILABLE"),
    ("FMV-SKILL-STRUCTURE-001", "human-design-reading-flowmaster", "missing specialization contract: Original-session QA"),
}


def payload_of(bodies: dict) -> dict:
    """C-15: the --bodies-stdin payload, every body in its normalized form."""
    return {k: nf.normalize(v) for k, v in bodies.items()}


def payload_normalized(payload: dict) -> bool:
    """The gate before any pipe: a payload a validator may see is already normalized (normalize is idempotent)."""
    return all(nf.normalize(v) == v for v in payload.values())


def suite_findings(suite: dict) -> list:
    """(rule_id, skill, evidence) of every finding validate_flowmaster.py reports (the skill is the subject's
    directory, as a3_package_dryrun_102726.py reads it)."""
    out = []
    for f in suite.get("findings") or []:
        skill = f.get("skill") or Path(str(f.get("subject") or "")).parent.name
        out.append((f.get("rule_id"), skill, f.get("evidence")))
    return sorted(set(out))


def suite_ok_c21(suite: dict) -> tuple[bool, list, list]:
    """C-21: the suite's findings are exactly the three named pre-existing ones (or none)."""
    found = suite_findings(suite)
    from_change = [list(f) for f in found if f not in PREEXISTING_SUITE_FINDINGS]
    preexisting = [list(f) for f in found if f in PREEXISTING_SUITE_FINDINGS]
    return (not from_change and (suite.get("suite_ok") is True or len(preexisting) == len(found))), from_change, preexisting


def read_bodies(fetched_after: str, map_path: str, stand_in_ok: bool) -> tuple[dict, dict, list, bool]:
    import body_check as B
    B.use_map(map_path)
    if B.STATE["stand_in"] and not stand_in_ok:
        raise SystemExit("x12: a stand-in successor map is refused without --stand-in-ok")
    root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
    bodies, as_of, missing = {}, {}, []
    for prompt, meta in B.EDITS["pages"].items():
        if prompt == "PE":
            continue
        got = B.latest_fetch(meta["page_id"], root, session, 900, fetched_after)
        if got is None:
            missing.append(prompt)
            continue
        bodies[prompt], as_of[prompt] = got[2], got[1]
    return bodies, as_of, sorted(missing), B.STATE["stand_in"]


def run_json(args, cwd, stdin=None):
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=stdin, capture_output=True, text=True, env=ENV)
    try:
        return r.returncode, json.loads(r.stdout)
    except ValueError:
        return r.returncode, {"_unparsed": (r.stdout + r.stderr)[-300:]}


def fxsum(c, d):
    return {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "profile_errors": d.get("profile_errors"),
            "section_13_fixture_count": d.get("section_13_fixture_count"), "section_13_passed": d.get("section_13_passed"),
            "section_13_variant_count": d.get("section_13_variant_count"),
            "section_13_variants_passed": d.get("section_13_variants_passed"), "case_count": d.get("case_count"),
            "failed_cases": [x.get("name") for x in d.get("cases", []) if not x.get("passed")]}


def run(argv: list) -> int:
    X, fetched_after = Path(argv[0]).resolve(), argv[1]
    map_path = argv[argv.index("--successor-map") + 1]
    cand_path = Path(argv[argv.index("--candidate-contract") + 1]) if "--candidate-contract" in argv else DEFAULT_CANDIDATE
    bodies, as_of, missing, stand_in = read_bodies(fetched_after, map_path, "--stand-in-ok" in argv)
    if missing:
        print(json.dumps({"record_type": "GCFPE_102726_X12_QUALIFICATION", "ok": False, "error": "NO_FETCH_FOUND",
                          "missing": missing}))
        return 2
    payload = payload_of(bodies)
    del bodies
    if not payload_normalized(payload):
        raise SystemExit("x12: refusing to pipe a payload that is not in the normalized form (C-15)")
    text = json.dumps(payload)
    del payload
    fv, cf = X / "flowmaster-validate", X / "change-flow"
    cc = cf / CF_CONTRACT
    c1, prof = run_json([sys.executable, "scripts/validate_gcfpe_20261027.py", cf, "--contract", cc, "--bodies-stdin"], fv, text)
    c3, fxb = run_json([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", cf, "--contract", cc, "--bodies-stdin"], fv, text)
    del text
    c4, fx = run_json([sys.executable, "scripts/run_gcfpe_20261027_fixtures.py", cf, "--contract", cc], fv)
    c2, suite = run_json([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", X], fv)
    spec = importlib.util.spec_from_file_location("v102726", fv / "scripts/validate_gcfpe_20261027.py")
    v = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(fv / "scripts"))
    spec.loader.exec_module(v)

    def strip(c):
        c = copy.deepcopy(c)
        for k in v.CONTRACT_LIFECYCLE_KEYS:
            c.pop(k, None)
        fg = (c.get("source_snapshot") or {}).get("frozen_candidate_graph")
        if isinstance(fg, dict):
            fg.pop("sha256", None)
        return v.release_semantic_view(c)
    diff = []
    if cand_path.exists():
        sc = strip(json.loads(cand_path.read_text(encoding="utf-8")))
        sp = strip(json.loads(cc.read_text(encoding="utf-8")))

        def walk(a, b, p):
            if isinstance(a, dict) and isinstance(b, dict):
                for k in sorted(set(a) | set(b)):
                    walk(a.get(k, "<absent>"), b.get(k, "<absent>"), p + [str(k)])
            elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
                for i, (x, y) in enumerate(zip(a, b)):
                    walk(x, y, p + [str(i)])
            elif a != b:
                diff.append(".".join(p))
        walk(sc, sp, [])
    s_ok, s_change, s_pre = suite_ok_c21(suite)
    rec = {
        "record_type": "GCFPE_102726_X12_QUALIFICATION", "step": "X12", "stand_in": stand_in,
        "reads": {"fetched_after": fetched_after, "members": len(as_of), "as_of_min": min(as_of.values()),
                  "as_of_max": max(as_of.values()), "text_form": "normalize_fetch.normalize (C-15)",
                  "d22": "member bodies read transiently from this session's fetch records, normalized in memory and "
                         "piped on stdin; no body text or digest written"},
        "profile_102726_with_bodies": {"exit": c1, "ok": prof.get("ok"), "errors": prof.get("errors"),
                                       "profile": prof.get("profile"),
                                       "prompt_bodies_validated": len(prof.get("prompt_bodies_validated") or []),
                                       "prompt_body_checks_not_evaluated": prof.get("prompt_body_checks_not_evaluated"),
                                       "contract_status": prof.get("contract_status"),
                                       "frozen_graph_edge_count": prof.get("frozen_graph_edge_count")},
        "fixtures_102726_with_bodies": fxsum(c3, fxb), "fixtures_102726_without_bodies": fxsum(c4, fx),
        "flowmaster_suite": {"exit": c2, "verdict": suite.get("verdict"), "suite_ok": suite.get("suite_ok"),
                             "ok_c21": s_ok, "findings_from_this_change": s_change, "findings_preexisting": s_pre,
                             "self_identity": suite.get("self_identity")},
        "release_semantic_equality": {"candidate_contract_present": cand_path.exists(),
                                      "candidate_vs_production_outside_lifecycle_and_graph_digest": cand_path.exists() and not diff,
                                      "differing_paths": diff[:20]},
    }
    rec["ok"] = (c1 == 0 and prof.get("ok") is True and rec["profile_102726_with_bodies"]["prompt_bodies_validated"] == MEMBERS
                 and prof.get("prompt_body_checks_not_evaluated") == [] and fxb.get("fixture_suite_ok") is True
                 and fx.get("fixture_suite_ok") is True and s_ok and cand_path.exists() and not diff
                 and len(as_of) == MEMBERS)
    print(json.dumps(rec, indent=1, sort_keys=True))
    return 0 if rec["ok"] else 1


def selftest(argv: list) -> int:
    rows = {}
    fetch = {"QA-120": "the change ID and <code>QA\\_REPORT</code> with <b>its</b> ID", "X": "plain"}
    p = payload_of(fetch)
    rows["payload_normalized"] = p["QA-120"] == "the change ID and `QA_REPORT` with **its** ID" and p["X"] == "plain"
    rows["payload_gate_passes_normalized"] = payload_normalized(p)
    rows["injected_raw_payload_refused"] = not payload_normalized(fetch)
    clean = {"suite_ok": False, "findings": [{"rule_id": r, "skill": s, "evidence": e} for r, s, e in PREEXISTING_SUITE_FINDINGS]}
    rows["c21_preexisting_only_passes"] = suite_ok_c21(clean)[0]
    rows["c21_suite_clean_passes"] = suite_ok_c21({"suite_ok": True, "findings": []})[0]
    extra = copy.deepcopy(clean)
    extra["findings"].append({"rule_id": "FMV-GCF-EDGE-003", "skill": "change-flow", "evidence": "x"})
    rows["injected_change_finding_fails_c21"] = not suite_ok_c21(extra)[0]
    if argv:
        fv = Path(argv[0]).resolve() / "flowmaster-validate"
        sys.path.insert(0, str(fv / "scripts"))
        spec = importlib.util.spec_from_file_location("v102726_selftest", fv / "scripts/validate_gcfpe_20261027.py")
        v = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(v)
        intake = ("For either PASS branch, the handoff names CL-05's Close Implementer and the inputs CL-05's intake reads: "
                  "the change ID and, by repository path, the separate <code>QA\\_REPORT</code> and <code>QA\\_RCA</code> "
                  "with their IDs; the artifacts hold the PF10 and addendum lineage, the Product Owner publication state and "
                  "the rescope, remediation and unresolved-finding lineage. Read CL-05's complete intake before emitting "
                  "its one handoff.\n")
        rows["built_intake_passes_normalized"] = "QA_PASS_BODY_INTAKE" not in v.validate_qa_closure_bodies(
            payload_of({"QA-120": intake}), {"member_registry": {}})
        rows["built_intake_injected_raw_fails"] = "QA_PASS_BODY_INTAKE" in v.validate_qa_closure_bodies(
            {"QA-120": intake}, {"member_registry": {}})
    ok = all(rows.values())
    print(json.dumps({"mode": "selftest", "rows": rows, "ok": ok}, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in ("run", "selftest"):
        sys.exit(__doc__)
    sys.exit((run if sys.argv[1] == "run" else selftest)(sys.argv[2:]))
