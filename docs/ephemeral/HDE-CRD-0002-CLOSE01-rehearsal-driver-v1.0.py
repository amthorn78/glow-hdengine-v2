"""PR-40 scratch rehearsal of Plan v1.1 WU-PR-07 T0-T7-precheck against the landed v2 contract.

Adapted from the PR-30 driver (result v1.0 §11) for the contract as merged (PO-35-10 to PO-35-21):
the source now binds the change's QA plan (QA-50 form) and QA report (QA-120 form), maps each MET
criterion to the primary of a PASS check whose plan mapping names it, allocates deliverables, and
carries an ADR block. Runs only in a fresh clone under <workdir>/<label>.

Usage: rehearse_v2.py <repo> <commit> <workdir> <label> <venv-python> <jsonschema-only-python> <requirements-only-python>
"""
import json, os, re, subprocess, sys, time
from pathlib import Path

src, commit_ref, work, label, PY, PYJS, PYREQ, MERGE_REF, BUILDER = sys.argv[1], sys.argv[2], Path(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9]
PROTO = sys.argv[10] if len(sys.argv) > 10 else None
repo = work / label
RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "PYTHONDONTWRITEBYTECODE": "1"}
BASE = {k: v for k, v in os.environ.items() if k in ("HOME", "PATH", "USER", "LOGNAME", "SHELL", "TERM")}
ENV = dict(BASE, **RAILS, PYTHONPATH=str(repo), GIT_CONFIG_GLOBAL="/dev/null")
JOB_ENV = dict(BASE, **RAILS, GIT_OPTIONAL_LOCKS="0", GIT_NO_LAZY_FETCH="1", GIT_CONFIG_GLOBAL="/dev/null")
CAPTURED_AT = "2026-10-26T00:00:00Z"   # fixed rehearsal capture time (not a live close)
CRD = "HDE-CRD-0002"
log = []

def run(argv, *, py=None, capture=False, env=None):
    argv = [py, *argv] if py else list(argv)
    t0 = time.monotonic()
    cp = subprocess.run(argv, cwd=repo, env=env or ENV, capture_output=True, text=True)
    shown = [a.replace(str(repo), "<repo>").replace(PYJS, "python(jsonschema-only)").replace(PYREQ, "python(requirements-only)").replace(PY, "python") for a in argv]
    log.append({"argv": shown[:4], "exit": cp.returncode, "seconds": round(time.monotonic() - t0, 2)})
    if cp.returncode and not capture:
        print(cp.stdout[-3000:], cp.stderr[-3000:]); raise SystemExit(f"FAILED: {shown[:4]}")
    return cp

def git(*args):
    return run(("git", *args)).stdout.strip()

def status():
    return git("status", "--porcelain=v1", "--untracked-files=all")

def commit(msg):
    git("add", "-A"); git("-c", "user.email=r@example.invalid", "-c", "user.name=rehearsal", "commit", "-q", "-m", msg)
    assert status() == "", status()
    return git("rev-parse", "HEAD")

subprocess.run(("git", "clone", "-q", "--no-hardlinks", src, str(repo)), check=True)
git("checkout", "-q", "--detach", commit_ref)
# Stand-in for the Product Owner's merge of the CL-C-10 v1.0 record (PR #747): docs/ephemeral only.
git("-c", "user.email=r@example.invalid", "-c", "user.name=rehearsal", "merge", "-q", "--no-ff", "-m", "rehearsal: CL-C-10 v1.0 record (stand-in for #747)", MERGE_REF)
assert git("diff", "--name-only", commit_ref, "HEAD").splitlines() == ["docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md"]
heads = {"P": git("rev-parse", "HEAD")}
assert (repo / "audit/qa/hde-crd-0002/qa_step_logs_manifest.json").exists()
assert not (repo / "audit/qa/hde-crd-0002/close").exists()
if PROTO:
    run(("python3", PROTO, str(repo)))
    heads["PROTO"] = commit("rehearsal: scratch prototype remedy (never pushed)")
# T1: the real causal inputs and the RF-12 lines.
run(("python3", BUILDER, str(repo)))
SRC = "audit/HDE-CRD-0002_close_candidate_source.json"
heads["C1"] = commit("rehearsal T1: candidate source, ledgers, RF-12")
lanes = run((PY, "tools/ci/prepush_check.py", "lanes", "build-notes"), capture=True)
paths = git("diff", "--name-only", heads["P"], heads["C1"]).splitlines()
memb = run((PY, "tools/ci/prepush_check.py", *[a for p in paths for a in ("--path", p)], "membership"), capture=True)
(work / f"{label}_prepush_C1.txt").write_text(lanes.stdout + lanes.stderr + "\n----\n" + memb.stdout + memb.stderr)
captures = []
def step(check_id, argv, py=None):
    cp = run(argv, py=py, capture=True)
    captures.append({"check_id": check_id, "command": ["python", *argv] if py else list(argv), "exit": cp.returncode, "output": cp.stdout + cp.stderr})
    if cp.returncode:
        print(cp.stdout[-3000:], cp.stderr[-3000:]); raise SystemExit(f"step failed: {check_id}")
step("close-pack-write", ("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--write"), py=PY)
step("evidence-index-write", ("tools/evidence/update_evidence_index.py",), py=PY)
heads["C2"] = commit("rehearsal T2-T3: close pack and evidence graph")
T4 = [("close-pack-check", ("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check"), PY),
      ("evidence-index-check", ("tools/evidence/update_evidence_index.py", "--check"), PY),
      ("orientation-check", ("tools/evidence/orientation_demo.py", "--check"), PY),
      ("mirror-schema", ("ci/checks/check_mirror_schema.sh",), None),
      ("evidence-index-hash", ("ci/checks/check_evidence_index_hash.sh",), None),
      ("evidence-paths", ("tools/evidence/validate_evidence_paths.py",), PY),
      ("final-lf", ("ci/checks/check_final_lf.sh",), None)]
for check_id, argv, py in T4:
    step(check_id, argv, py)
assert status() == ""
(work / f"{label}_captures.json").write_text(json.dumps(captures, indent=1))
t5 = '''
import json, sys
from tools.evidence import update_evidence_index as writer
from tools.qa import qa_harness as qa
config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)
results = [qa.CheckResult(c["check_id"], qa.Status.PASS if c["exit"] == 0 else qa.Status.FAIL_BEHAVIOR,
    status_reason="" if c["exit"] == 0 else "exit %d" % c["exit"], command=tuple(c["command"]),
    command_provenance="executed in the same local close run (rehearsal)", exit_code=c["exit"], output=c["output"])
    for c in json.load(open(sys.argv[1]))]
print(len(writer.publish_crd_close_run_family(config, results, captured_at_utc="''' + CAPTURED_AT + '''")))
'''
run(("-c", t5, str(work / f"{label}_captures.json")), py=PY)
heads["C3"] = commit("rehearsal T5: close-run family (terminal state)")
qa_untouched = git("diff", "--name-only", heads["C2"], heads["C3"], "--", "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "audit/qa/hde-crd-0002/checks") == ""
assert qa_untouched
# T6: the T4 set again on clean C3.
for check_id, argv, py in T4:
    run(argv, py=py)
assert status() == ""
# The hosted closeout job's seven checks under the job's own install (D-1): requirements.txt only, job env, no PYTHONPATH.
job = {}
for argv, py in (((("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check")), PYREQ),
                 (("tools/evidence/update_evidence_index.py", "--check"), PYREQ),
                 (("tools/evidence/orientation_demo.py", "--check"), PYREQ),
                 (("ci/checks/check_evidence_index_hash.sh",), None),
                 (("tools/evidence/validate_evidence_paths.py",), PYREQ),
                 (("ci/checks/check_mirror_schema.sh",), None),
                 (("ci/checks/check_final_lf.sh",), None)):
    env = dict(JOB_ENV)
    if py is None:  # shell checks call `python`; put the requirements-only interpreter first on PATH
        env["PATH"] = str(Path(PYREQ).parent) + os.pathsep + env["PATH"]
    cp = run(argv, py=py, capture=True, env=env)
    job[argv[0]] = [cp.returncode, (cp.stdout + cp.stderr).strip().splitlines()[-1:]]
# The writer's --check with jsonschema only (ID-10's retained writer constraint).
cp = run(("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check"), py=PYJS, capture=True, env=JOB_ENV)
jsonschema_only = [cp.returncode, (cp.stdout + cp.stderr).strip().splitlines()[-1:]]
clean_after_job = status() == ""
# Idempotence: T2-T5 again on clean C3 with the same captures changes no byte.
run(("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--write"), py=PY)
run(("tools/evidence/update_evidence_index.py",), py=PY)
run(("-c", t5, str(work / f"{label}_captures.json")), py=PY)
idempotent = status() == ""
lanes3 = run((PY, "tools/ci/prepush_check.py", "lanes"), capture=True)
(work / f"{label}_prepush_C3.txt").write_text(lanes3.stdout + lanes3.stderr)
files = git("ls-files", "audit/HDE-CRD-0002_close_report.md", "audit/HDE-CRD-0002_MANIFEST.json", "audit/qa/hde-crd-0002/close").splitlines()
report = (repo / "audit/HDE-CRD-0002_close_report.md").read_text(encoding="utf-8")
out = {"label": label, "heads": heads, "tree_C3": git("rev-parse", "HEAD^{tree}"), "qa_manifest_and_checks_untouched_C2_C3": qa_untouched,
       "job_seven_checks_requirements_only": job, "writer_check_jsonschema_only": jsonschema_only, "clean_after_job_checks": clean_after_job,
       "idempotent_rerun_on_C3": idempotent, "close_files": files,
       "report_headings": [l[3:] for l in report.splitlines() if l.startswith("## ")],
       "report_decision_lines": [l for l in report.splitlines() if l.startswith("- Closure decision") or l.startswith("- Decision posture")],
       "commands": len(log), "nonzero": [s for s in log if s["exit"]], "steps": log}
(work / f"{label}_result.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("heads", "tree_C3", "qa_manifest_and_checks_untouched_C2_C3", "job_seven_checks_requirements_only", "writer_check_jsonschema_only", "clean_after_job_checks", "idempotent_rerun_on_C3", "report_decision_lines", "commands")}, indent=1))
print(len(files), "close files")
