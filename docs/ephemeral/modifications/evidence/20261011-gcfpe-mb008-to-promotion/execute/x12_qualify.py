#!/usr/bin/env python3
"""X12: shipped validators from the extracted packages over every member body (D22: transient reads piped on
stdin, never written). Prints two receipts as one JSON object {"validators": ..., "fixtures": ...}; flags,
counts, ids and error codes only."""
import json, os, subprocess, sys, copy, importlib.util, hashlib
from pathlib import Path
REPO = Path("/home/user/glow-hdengine-v2")
E = REPO / "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion"
X = Path(sys.argv[1])            # root holding the 13 skills, the six extracted
FETCHED_AFTER = sys.argv[2]
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
sys.dont_write_bytecode = True
sys.path.insert(0, str(E / "plan"))
import body_check as B
SUCC = "3f74590a05eb81b69bd8c27106f7a59d"
B.EDITS["pages"]["GCFPE-MGMT-10"] = {"page_id": SUCC, "expected_last_edited": "2026-10-12T02:24:58.597Z"}
root, session = os.path.expanduser("~/.claude/projects"), os.environ["CLAUDE_CODE_SESSION_ID"]
bodies, as_of = {}, {}
for prompt, meta in B.EDITS["pages"].items():
    if prompt == "PE":
        continue
    got = B.latest_fetch(meta["page_id"], root, session, 900, FETCHED_AFTER)
    if got is None:
        print(json.dumps({"error": f"NO_FETCH_FOUND:{prompt}"})); sys.exit(2)
    bodies[prompt] = got[2]; as_of[prompt] = got[1]
payload = json.dumps(bodies)
fv, cf = X / "flowmaster-validate", X / "change-flow"
cc = cf / "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"
def run(args, cwd, stdin=None):
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=stdin, capture_output=True, text=True, env=ENV)
    try: return r.returncode, json.loads(r.stdout)
    except ValueError: return r.returncode, {"_unparsed": (r.stdout + r.stderr)[-300:]}
c1, prof = run([sys.executable, "scripts/validate_gcfpe_20261009.py", cf, "--contract", cc, "--bodies-stdin"], fv, payload)
c2, suite = run([sys.executable, "scripts/validate_flowmaster.py", "--skills-root", X], fv)
c3, fx_bodies = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc, "--bodies-stdin"], fv, payload)
c4, fx = run([sys.executable, "scripts/run_gcfpe_20261009_fixtures.py", cf, "--contract", cc], fv)
del payload, bodies
spec = importlib.util.spec_from_file_location("v100926", fv / "scripts/validate_gcfpe_20261009.py")
v = importlib.util.module_from_spec(spec); sys.path.insert(0, str(fv / "scripts")); spec.loader.exec_module(v)
cand = json.loads((E / "execute/contracts/gcfpe-20261009.1-100926.1-candidate-contract.json").read_text(encoding="utf-8"))
prod = json.loads(cc.read_text(encoding="utf-8"))
def strip(c):
    c = copy.deepcopy(c)
    for k in v.CONTRACT_LIFECYCLE_KEYS: c.pop(k, None)
    fg = (c.get("source_snapshot") or {}).get("frozen_candidate_graph")
    if isinstance(fg, dict): fg.pop("sha256", None)
    return v.release_semantic_view(c)
sc, sp = strip(cand), strip(prod)
diff = []
def walk(a, b, p):
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)): walk(a.get(k, "<absent>"), b.get(k, "<absent>"), p + [str(k)])
    elif isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)): walk(x, y, p + [str(i)])
    elif a != b: diff.append(".".join(p))
walk(sc, sp, [])
cov = suite.get("change_contract_coverage", {})
validators = {
    "record_type": "MB008_X12_QUALIFICATION_VALIDATORS", "step": "X12",
    "reads": {"fetched_after": FETCHED_AFTER, "members": len(as_of), "as_of_min": min(as_of.values()), "as_of_max": max(as_of.values()),
              "d22": "55 member bodies read transiently from this session's fetch records and piped on stdin; no body text or digest written"},
    "profile_100926_with_bodies": {"exit": c1, "ok": prof.get("ok"), "errors": prof.get("errors"), "profile": prof.get("profile"),
        "prompt_bodies_validated": len(prof.get("prompt_bodies_validated") or []), "prompt_body_count": prof.get("prompt_body_count"),
        "prompt_body_checks_not_evaluated": prof.get("prompt_body_checks_not_evaluated"), "contract_status": prof.get("contract_status"),
        "frozen_graph_edge_count": prof.get("frozen_graph_edge_count")},
    "flowmaster_suite": {"exit": c2, "verdict": suite.get("verdict"), "suite_ok": suite.get("suite_ok"), "finding_counts": suite.get("finding_counts"),
        "self_identity": suite.get("self_identity"), "current_profile": cov.get("gcfpe_current_direct_handoff", {}).get("profile")},
    "release_semantic_equality": {"candidate_vs_production_outside_lifecycle_and_graph_digest": not diff, "differing_paths": diff[:20],
        "method": "release_semantic_view after removing CONTRACT_LIFECYCLE_KEYS and source_snapshot.frozen_candidate_graph.sha256"},
}
validators["ok"] = (c1 == 0 and prof.get("ok") is True and validators["profile_100926_with_bodies"]["prompt_bodies_validated"] == 55
                    and prof.get("prompt_body_checks_not_evaluated") == [] and suite.get("suite_ok") is True and not diff)
def fxsum(c, d):
    return {"exit": c, "fixture_suite_ok": d.get("fixture_suite_ok"), "profile_errors": d.get("profile_errors"),
            "section_13_fixture_count": d.get("section_13_fixture_count"), "section_13_passed": d.get("section_13_passed"),
            "section_13_variant_count": d.get("section_13_variant_count"), "section_13_variants_passed": d.get("section_13_variants_passed"),
            "case_count": d.get("case_count"), "qa_closure_source_case_count": d.get("qa_closure_source_case_count"),
            "artifact_timing_case_count": d.get("artifact_timing_case_count"),
            "artifact_timing_actual_source_mutation_count": d.get("artifact_timing_actual_source_mutation_count"),
            "failed_cases": [x.get("name") for x in d.get("cases", []) if not x.get("passed")]}
fixtures = {"record_type": "MB008_X12_QUALIFICATION_FIXTURES", "step": "X12", "with_bodies": fxsum(c3, fx_bodies), "without_bodies": fxsum(c4, fx)}
fixtures["ok"] = fx_bodies.get("fixture_suite_ok") is True and fx.get("fixture_suite_ok") is True
print(json.dumps({"validators": validators, "fixtures": fixtures}, indent=1))
