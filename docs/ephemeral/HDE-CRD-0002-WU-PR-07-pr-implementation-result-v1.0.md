---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result: PR_CANDIDATE_PUBLISHED
phase: PR-30 (initial publication); next phase PR-35 in its own dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
work_unit_title: "Close-pack writer for Epic and CRD identities, close-run evidence home, ADR draft (PR; Distillation; S21)"
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1; landed by #667 as 390bc99)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0), as overlaid by the rescope addendum below
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0.md (RS-20 APPROVE; D-1, D-2)
pf10_addendum_overlay: docs/ephemeral/HDE-CRD-0002-WU-PR-07-PF10-build-notes-addendum-v1.0.md (proposed 2.13)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
effective_baseline: approved base + PF10 addenda 2.11 (read with 2.12's numbering), 2.12, 2.5, 2.3, 2.1, the business-case disposition and the rescope addendum overlay (proposed 2.13)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (sha256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35; the only PF10 file on main at 390bc99; read as provenance)
proceed: the Product Owner's PR-30 invocation in this session for exactly PR_IMPLEMENTATION_PLAN v1.1 ("Implement WU-PR-07 (S21, with rescope items D-1 and D-2) from plan v1.1"), EXECUTION_POSTURE MANUAL_PROMPT_EXECUTION
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08.672Z, fetched and read in full in this session)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF (the dedicated WU-PR-07 PR engineering session)
workspace: /home/user/glow-hdengine-v2 (one worktree)
branch: claude/gallant-cerf-ysdde5 (restarted from main 390bc99 after #667 merged; the remote branch had been deleted at merge and was recreated by a plain push)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668 (open, ready for review; created 2026-10-20T16:50:45Z)
base: main 390bc9960a3e9012f67fe7ea39905b624259c87e
implementation_commit: 1080f7736c396ef191e677312994c571817dfb24 (10 files, +1,795/−15)
result_record_commit: the commit that adds this file, on the same branch (not named inside the file it creates)
created_at: 2026-10-20T16:52:30Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** WU-PR-07 is implemented exactly as plan v1.1's companion diff and published as [amthorn78/glow-hdengine-v2#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668). The implementation commit is `1080f77`. Every check in plan v1.1 §11 passed on that commit before publication (§4).

PR-30 ends here. The PR-35 phase owns everything from here to merge readiness: the Codex code review, its corrections, current-head CI and mergeability. It runs in its own dedicated session. Nothing here claims merge readiness, QA, acceptance or closure.

## 2. Recovery before creating anything

| Checked | Found |
| :- | :- |
| Open pull requests on the repository | none (GitHub listing, state open) |
| WU-PR-07 result records on `main` | none |
| Local checkout | one worktree, clean; local branch tip `7130044`, whose tree equals merged `390bc99` (#667, documents only) |
| Remote branch `claude/gallant-cerf-ysdde5` | present at session start; deleted at #667's merge |
| Earlier code | prototypes only, in scratch clones, never pushed |

The branch was restarted from `main` `390bc99`. A pull request merged under an earlier plan cycle (#665, #667, both documents) is landed history and was not reused.

## 3. Implementation

1. `main` moved past `047a22c` only in `docs/ephemeral/` (plan v1.1 and its diff), so plan §9 step 2 needed no re-measurement.
2. `git apply --check`, then `git apply`, of `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1-prototype.diff` (SHA-256 a106044db8969c42d61cbfcc6ebafd0637867eda6b35de612180763a11696353). Every hunk applied; no hand application was needed.
3. Each of the ten changed files' blobs equals the validated v1.1 prototype's (blob comparison).
4. One commit, `1080f77`: `feat(close-pack): v2 close-pack writer for Epic and CRD identities, close-run family, closeout-job install, ADR draft (HDE-CRD-0002 WU-PR-07 S21)`.

| Path | Lines |
| :- | :- |
| `schemas/close_candidate_source.v2.json` (new) | +500 |
| `tools/qa/generate_epic_close_pack.py` | +496/−6 |
| `tests/qa/test_generate_epic_close_pack.py` | +396 |
| `tools/evidence/update_evidence_index.py` | +168/−2 |
| `tests/evidence/test_evidence_index_missing_state.py` | +138 |
| `docs/adr/hde/close_pack_writer_adr.md` (new) | +71 |
| `tools/qa/qa_harness.py` | +17/−5 |
| `tests/evidence/test_rails_ci_workflow_integration.py` (D-2) | +4 |
| `ci/checks/classify_ci_changes.py` | +3 |
| `.github/workflows/epic-closeout-validation.yml` (D-1) | +2/−2 |

## 4. Checks run on `1080f77` (plan v1.1 §11)

All in detached clones of the commit under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), CPython 3.12.3, git 2.43.0, a scratch venv with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`), `PYTHONPATH` set to the copy and `XDG_STATE_HOME` an empty scratch directory. Vendor, database and GitHub keys and `ENGINE_ENV` were unset. Every copy ended with an empty `git status --short --untracked-files=all` and an empty `git diff`.

| § | Check | Result | Time (UTC) |
| :- | :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` | 459 passed, exit 0 | 15:57:22 to 15:58:35 |
| 1 | the OBS-17 test alone, 50 times | 50 of 50 passed | to 16:00:10 |
| 2 | the 24 test files referencing the updater + `tests/qa/test_generic_qa_harness.py` | 1,632 passed, exit 0 | 16:06:00 to 16:22:32 |
| 3 | `tests/evidence/test_rails_ci_workflow_integration.py` + `tests/evidence/test_http_reader_ci_ownership.py` | 142 passed, exit 0 | to 16:00:40 |
| 4 | `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_mirror_schema.sh`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_final_lf.sh` | all exit 0; `git diff --stat 390bc99 HEAD -- docs/evidence artifacts audit` empty (Index trio byte-unchanged, ID-9) | ~16:01 |
| 5 | `prepush_check.py --base 390bc99 --head HEAD lanes` | `reason=selected_lanes;paths=10;lanes=product,compat,db,rails,evidence,qa,release`; 166 targets | 5.7 s |
| 5 | `prepush_check.py membership` for all ten paths | none is a member (release 1.3.0, 45 members, `release_id` 77204764…) | 6.9 s |
| 6 | T0–T6 rehearsal, run r1 | every command exit 0 (50); C3 `15e07f6`; re-run of T2, T3 and T5 on C3 changes no byte | 16:01:12 to before 16:03:00 |
| 6 | T0–T6 rehearsal, run r2 | every command exit 0 (50); C3 `197a295`; re-run on C3 changes no byte | 16:03:00 to 16:04:26 |
| 6 | r1 vs r2 terminal trees | 19 files differ: 17 path proofs (`mtime_utc` and `produced_at_utc` lines only) and the two Mirror files that embed them; the close report, manifest, Index JSON, sentinel, orientation output and every close-run primary are byte-identical | — |
| 7 | `prepush_check.py --base 390bc99 --head HEAD --full replay` | PASS: `ci.yml` sha256 d02021f3… (pinned); all 16 steps SUCCESS (1, 4, 5 excluded and substituted); changed tests 4,077 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79 with the attestation built and verified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; copy clean; repository unchanged | 16:22:37 to 16:49:25 (step time 1,602 s) |
| 8 | the closeout job's seven checks on r1's C3, a `requirements.txt`-only interpreter (Flask 2.3.3) and the job's environment (closed rails, `GIT_OPTIONAL_LOCKS=0`, `GIT_NO_LAZY_FETCH=1`, otherwise empty) | all seven exit 0: writer `--check`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh`; C3 clean | ~16:05 |
| 9 | the writer's `--check` on r1's C3, `jsonschema`-only interpreter, the job's environment | exit 0, `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json` | — |
| 10 | D-2 negative control: the workflow restored to `390bc99`'s bytes, `-k manual_closeout` | 1 failed, exit 1 (as intended); workflow restored; copy clean | — |

**Option A line (disposition record §3; instruction ID-17):** one full replay run, on `1080f77`, before publication; PASS. Hosted CI has not yet reported on #668. Any hosted failure that the replay would have caught is PR-40's to record.

**OBS-17:** no recurrence in the 50 repeats on the commit; the diagnosis stands as plan v1.0 §12.5 records it.

## 5. H-1 close sequence, restated against the published code

For HDE-CRD-0002's close mutation set, under closed rails, in a local clean clone of the close branch:
- **T1:** author `audit/HDE-CRD-0002_close_candidate_source.json` (`schema_version` `close_candidate_source.v2`), `audit/docdeltas/hde-crd-0002_doc_deltas.md` and `audit/docdeltas/hde-crd-0002_drain_targets.md`; commit C1.
- **T2:** `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --write`; capture argv, exit code and output.
- **T3:** `python tools/evidence/update_evidence_index.py`; capture; commit C2.
- **T4:** on clean C2, capture each of `python tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check`, `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, `python tools/evidence/validate_evidence_paths.py` and `ci/checks/check_final_lf.sh`.
- **T5:** in Python, from the repository root:
  ```python
  from tools.evidence import update_evidence_index as writer
  from tools.qa import qa_harness as qa
  config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)
  results = [qa.CheckResult(check_id, qa.Status.PASS if code == 0 else qa.Status.FAIL_BEHAVIOR,
      status_reason="" if code == 0 else f"exit {code}", command=tuple(argv),
      command_provenance="executed in the same local close run", exit_code=code, output=output)
      for check_id, argv, code, output in captures]   # one per T2 to T4 command
  writer.publish_crd_close_run_family(config, results, captured_at_utc=t4_capture_time)
  ```
  Commit C3, the terminal state.
- **T6:** the T4 set again on clean C3.
- **T7:** the Product Owner dispatches `.github/workflows/epic-closeout-validation.yml` with `git_ref` = C3 and `candidate_source` = `audit/HDE-CRD-0002_close_candidate_source.json`. The job now installs `requirements.txt` (D-1).

The rehearsal driver in §11 runs exactly this sequence, with a stand-in T0.

## 6. In-flight decisions

| Decision | Why it was needed | Tested by |
| :- | :- | :- |
| Restart the branch from `main` `390bc99` | #667, the branch's previous PR, had merged; a merged PR is landed history | §2 recovery; the commit's parent is `390bc99` |
| Push the branch with a plain push, not a lease | The lease push was refused as "stale info" because the remote branch had been deleted at #667's merge (`git ls-remote` showed no such branch); no remote commit was replaced | `git ls-remote` read back `1080f77` |

No code decision was taken beyond the plan: the applied diff is plan v1.1's companion diff, byte for byte.

## 7. PR_REMOTE_ACTION_LEDGER

| # | Action | Outcome |
| :- | :- | :- |
| 1 | Local checks §11 items 1 to 10 on `1080f77` | all pass (§4) |
| 2 | `git push --force-with-lease=…:7130044` | refused ("stale info"); the remote branch had been deleted; nothing written |
| 3 | `git push -u origin claude/gallant-cerf-ysdde5` | new branch at `1080f77` (read back); no CI, since push CI runs on `main` only |
| 4 | Create PR #668, ready for review | open; head `1080f77`; base `390bc99`; 10 files +1,795/−15; `mergeable_state` `unstable` at creation (checks pending) |
| 5 | Commit and push this result record | adds one `docs/ephemeral/` file; the pull-request CI run on `1080f77` is superseded by the run on the new head (`cancel-in-progress` for pull requests) |
| — | Reviews read | none yet (PR-35's) |
| — | CI runs | none completed at writing (PR-35's) |
| Next | PR-35: subscribe to #668; read the Codex review and current-head CI; disposition findings under addendum 2.11 rules 7 and 8 | — |

## 8. Spend against the ceiling (instruction ID-1)

| Item | Sessions | Elapsed |
| :- | -: | :- |
| PR-10 | 1 | 13:14:32Z to 13:42:00Z |
| PR-20 v1.0, RS-10, PR-20 v1.1, PR-30 (this session) | 1 | 13:55:25Z to 2026-10-20T16:52:30Z |
| RS-20 (IA, in the PR-10 session) | counted in either reading as session 3 (plan v1.1 §3) | to 15:50:00Z |
| **Total now** | **3 of 4** | **about 3.7 hours of 3 days**, excluding Product Owner waits |

PR-35 is session 4. No slack remains: a second PR-35 session or any other repeated stage passes the ceiling and returns to the Product Owner before work continues.

## 9. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| AQ-1 (the S21 ADR, `Proposed`) | Product Owner | pending; before #668 merges |
| Codex code review of #668 | PR-35 | not yet read |
| Hosted CI on the current head | PR-35 | not yet reported |
| The rescope review's observation: one unrelated rails-test subprocess timeout in the reviewer's container | PR-35, if it recurs on the hosted run | not observed here (142 passed) |
| OBS-17 | PR-35, if it recurs; otherwise the QA tool and test owner through the IA | not reproduced |
| The closeout job's first hosted run | HDE-CRD-0002's close mutation set (T7) | stated limit |
| Documentation (`AGENTS.md`, `README.md`, `docs/qa_harness_pattern.md`) | WU-DOC-01 | plan v1.1 §18 |
| PF-Canon drainage of the ADR's homes | PF drainage owners, after AQ-1 | unperformed |
| `GCFPE_PROMPT_USES` persistence | its authorized writer (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) | recorded here only; pending, non-gating |

**Nonclaims:**
- The writer and the close-run family are capability only.
- No close pack, candidate source or close-run family of any change is produced.
- No QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
- No canon edit.
- The ADR is `Proposed` until the Product Owner decides it.
- No merge readiness is claimed.

## 10. TypeSafe reading for the receiving session (PR-35)

Action sent (v8.2): "Resolve, in its own dedicated session, the automated code review findings and the CI result on one already published pull request for one work unit, about 1,800 lines across six code files and three test files (a second model in an existing close-pack writer, a close-run evidence entrypoint in an existing evidence updater, a one-line workflow install change), under rules that fix only findings showing a wrong result on a real input and stop to ask one design question when two consecutive review rounds repeat a finding class; retest each correction locally, push coherent corrections, verify current-head CI across seven lanes and mergeability, and return merge-pending without merging; no live provider call occurs; a lineage review follows after the Product Owner merges."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.44 (confidence 0.69); rung probabilities low 0.00, medium 0.01, high 0.54, extra high 0.45, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.98, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.005, Fable 5.1 at extra high 0.005, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.010, Opus 5.5 at high 0.529, Opus 5.5 at extra high 0.441, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.005, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and high. Sent 2026-10-20T16:06:28Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-20T16:06:28Z; HTTP 200 in 0.87 s; 5493 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and high.
- **Records.** Run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review`, before this record was saved. The Notion row was not written (addendum 2.1). Nathan's pick for PR-35 is not stated; his pick for this PR-30 session is not stated.

**Surface advice:** run PR-35 as its own top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, entered from this handoff. It needs:
- GitHub access for reviews, threads and checks, with PR activity subscription where available;
- Notion read access for the prompt;
- CPython 3.12 with CI's install, plus a `requirements.txt`-only and a `jsonschema`-only interpreter if a correction touches the workflow, writer or updater;
- `ruby`, `bash`, `curl` and git, closed rails, and throwaway clones for every write-mode or test run.

Observed times: the writer test file takes 72 s, the updater consumers 17 minutes, a rehearsal run about 90 s, and a full replay about 27 minutes. No live vendor, production or database access is needed.

## 11. Rehearsal driver (scratch tool; plan v1.1 §9 step 5)

Run as `python rehearse.py <repository-with-the-commit-checked-out> <empty-workdir> <label> <venv-python> <jsonschema-only-python>`. It clones the repository into `<workdir>/<label>`, never touches the source repository, and writes a JSON result and the captures beside the clone. SHA-256 f6bb050861e7f22fe594ca2ebc868e5ff7ecee145b70b33fc08df686a9bfe6ee, 151 lines.

```python
"""Scratch rehearsal of Plan v1.1 WU-PR-07 T0-T6 for a synthetic HDE-CRD-0002 candidate.

Usage: rehearse.py <prototype-repo> <workdir> <label> <venv-python> <jsonschema-only-python>
Runs only in a fresh clone under <workdir>/<label>; never touches the prototype repo.
"""
import json, os, re, subprocess, sys, time
from pathlib import Path

proto, work, label, PY, PYJS = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
repo = work / label
RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "PYTHONDONTWRITEBYTECODE": "1"}
ENV = {k: v for k, v in os.environ.items() if k in ("HOME", "PATH", "USER", "LOGNAME", "SHELL", "TERM")}
ENV.update(RAILS); ENV["PYTHONPATH"] = str(repo); ENV["GIT_CONFIG_GLOBAL"] = "/dev/null"
CAPTURED_AT = "2026-10-20T00:00:00Z"   # fixed rehearsal capture time (not a live close)
log = []

def run(argv, *, py=None, capture=False, cwd=None):
    argv = [py, *argv] if py else list(argv)
    t0 = time.monotonic()
    cp = subprocess.run(argv, cwd=cwd or repo, env=ENV, capture_output=True, text=True)
    dt = time.monotonic() - t0
    shown = [a.replace(str(repo), "<repo>").replace(PY, "python").replace(PYJS, "python(jsonschema-only)") for a in argv]
    log.append({"argv": shown, "exit": cp.returncode, "seconds": round(dt, 2)})
    if cp.returncode and not capture:
        print(cp.stdout, cp.stderr); raise SystemExit(f"FAILED: {shown}")
    return cp

def git(*args):
    return run(("git", *args)).stdout.strip()

def status():
    return git("status", "--porcelain=v1", "--untracked-files=all")

def commit(msg):
    git("add", "-A"); git("-c", "user.email=r@example.invalid", "-c", "user.name=rehearsal", "commit", "-q", "-m", msg)
    assert status() == "", status()
    return git("rev-parse", "HEAD")

subprocess.run(("git", "clone", "-q", "--no-hardlinks", str(proto), str(repo)), check=True)
git("checkout", "-q", "--detach", git("rev-parse", "HEAD"))
heads = {"P": git("rev-parse", "HEAD")}

# T0 (precondition stand-in): a real HDE-CRD-0002 QA family published by publish_crd_check_family.
t0 = '''
import subprocess, sys
from tools.evidence import update_evidence_index as writer
from tools.qa import qa_harness as qa
config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)
def observed(check_id, argv):
    cp = subprocess.run(argv, capture_output=True, text=True, check=False)
    return qa.CheckResult(check_id, qa.Status.PASS if cp.returncode == 0 else qa.Status.FAIL_BEHAVIOR,
        status_reason="" if cp.returncode == 0 else f"exit {cp.returncode}", command=tuple(argv),
        command_provenance="executed in a throwaway rehearsal clone", exit_code=cp.returncode, output=cp.stdout + cp.stderr)
writer.publish_crd_check_family(config, (observed("env-pins", ("ci/checks/check_env_pins.sh",)),
    observed("evidence-index-check", (sys.executable, "tools/evidence/update_evidence_index.py", "--check"))),
    captured_at_utc="''' + CAPTURED_AT + '''")
'''
run(("-c", t0), py=PY)
heads["C0"] = commit("rehearsal T0: QA family (stand-in for the recorded QA verdict)")

# T1: author the causal inputs (synthetic candidate; real Specification and Plan of HDE-CRD-0002).
spec = "docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md"
ids = re.findall(r"^\| (S\d\d) \|", (repo / spec).read_text(encoding="utf-8"), re.M)
assert len(ids) == 22, ids
(repo / "audit/docdeltas/hde-crd-0002_doc_deltas.md").write_text("Doc Deltas: None\n", encoding="utf-8")
(repo / "audit/docdeltas/hde-crd-0002_drain_targets.md").write_text("# HDE-CRD-0002 drain targets\n\nDrain targets: None\n", encoding="utf-8")
qa_ev = [{"binding": "qa_manifest", "path": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json"},
         {"binding": "qa_env_pins", "path": "audit/qa/hde-crd-0002/checks/env-pins/primary.log"},
         {"binding": "qa_evidence_index", "path": "audit/qa/hde-crd-0002/checks/evidence-index-check/primary.log"}]
source = {
 "schema_version": "close_candidate_source.v2", "change_id": "HDE-CRD-0002",
 "plan_path": "docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md",
 "evidence_inputs": [{"binding": "specification", "path": spec},
    {"binding": "doc_deltas", "path": "audit/docdeltas/hde-crd-0002_doc_deltas.md"},
    {"binding": "drain_targets", "path": "audit/docdeltas/hde-crd-0002_drain_targets.md"}, *qa_ev],
 "requirements_binding": "specification",
 "acceptance": [{"criterion_id": i, "evidence_bindings": ["qa_manifest"], "result": "MET", "limitation": "Rehearsal stand-in; no QA verdict exists."} for i in ids],
 "deliverables": ["Rehearsal stand-in for the delivered scope of S01 to S22."],
 "deferrals": [], "later_drain_statements": [{"canon_homes": ["Change Process Guide"], "locators": ["3.5.2.1 Close-pack files"],
   "current_posture": "Names the Epic filename prefix only.", "action": "No status change recommended",
   "readiness": "Not yet supportable from repo evidence", "evidence_bindings": ["specification"], "close_expectation": "Drained later by its owner."}],
 "tracked_issues": [], "closure_decision": {"decision": "SATISFIED", "posture": "review_trace_only"},
 "follow_ups": [], "superseded": [],
 "pointers": ["audit/docdeltas/hde-crd-0002_doc_deltas.md", "audit/docdeltas/hde-crd-0002_drain_targets.md",
              "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "audit/qa/hde-crd-0002/close/"],
 "qa_rca": {"summary_lines": ["Rehearsal stand-in: no QA run or RCA exists for this synthetic candidate."]},
 "key_outputs": {"close_report": "audit/HDE-CRD-0002_close_report.md", "close_manifest": "audit/HDE-CRD-0002_MANIFEST.json",
   "doc_deltas": "audit/docdeltas/hde-crd-0002_doc_deltas.md", "drain_targets": "audit/docdeltas/hde-crd-0002_drain_targets.md",
   "qa_step_logs_manifest": "audit/qa/hde-crd-0002/qa_step_logs_manifest.json"},
 "nonclaims": ["no_canon_drainage_or_register_movement", "no_execution_by_writer", "no_hosted_feedback_inputs", "no_unbound_claim"]}
SRC = "audit/HDE-CRD-0002_close_candidate_source.json"
(repo / SRC).write_text(json.dumps(source, indent=2, sort_keys=True) + "\n", encoding="utf-8")
heads["C1"] = commit("rehearsal T1: candidate source and ledgers")

captures = []
def step(check_id, argv, py=None):
    cp = run(argv, py=py, capture=True)
    shown = [a.replace(PY, "python") for a in ([py] if py else [])] + [a for a in argv]
    captures.append({"check_id": check_id, "command": ["python", *argv] if py else list(argv), "exit": cp.returncode, "output": cp.stdout + cp.stderr})
    if cp.returncode: print(cp.stdout, cp.stderr); raise SystemExit(f"step failed: {check_id}")
# T2, T3
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
# T5: the IF-4 entrypoint renders the close-run family from the captures.
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
manifest_before = (repo / "audit/qa/hde-crd-0002/qa_step_logs_manifest.json").read_bytes()
heads["C3"] = commit("rehearsal T5: close-run family (terminal state)")
assert git("diff", "--name-only", heads["C2"], heads["C3"], "--", "audit/qa/hde-crd-0002/qa_step_logs_manifest.json", "audit/qa/hde-crd-0002/checks") == ""
# T6: T4 set again on clean C3, plus the writer check and the read-only set with jsonschema only.
for check_id, argv, py in T4:
    run(argv, py=py)
jsonschema_only = {}
for argv in (("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--check"), ("tools/evidence/update_evidence_index.py", "--check"),
             ("tools/evidence/orientation_demo.py", "--check"), ("tools/evidence/validate_evidence_paths.py",)):
    env_backup = ENV.pop("PYTHONPATH"); cp = run(argv, py=PYJS, capture=True); ENV["PYTHONPATH"] = env_backup
    jsonschema_only[argv[0]] = [cp.returncode, (cp.stdout + cp.stderr).strip().splitlines()[-1:]]
assert jsonschema_only["tools/qa/generate_epic_close_pack.py"][0] == 0, jsonschema_only
assert status() == ""
# Idempotence: T2-T5 again on clean C3 with the same captures changes no byte.
run(("tools/qa/generate_epic_close_pack.py", "--source", SRC, "--write"), py=PY)
run(("tools/evidence/update_evidence_index.py",), py=PY)
run(("-c", t5, str(work / f"{label}_captures.json")), py=PY)
idempotent = status() == ""
tree = git("rev-parse", "HEAD^{tree}")
files = git("ls-files", "audit/HDE-CRD-0002_close_report.md", "audit/HDE-CRD-0002_MANIFEST.json", "audit/qa/hde-crd-0002/close").splitlines()
out = {"label": label, "jsonschema_only": jsonschema_only, "heads": heads, "tree_C3": tree, "idempotent_rerun_on_C3": idempotent, "close_files": files, "steps": log}
(work / f"{label}_result.json").write_text(json.dumps(out, indent=1))
print(json.dumps({k: out[k] for k in ("heads", "tree_C3", "idempotent_rerun_on_C3", "jsonschema_only")}, indent=1)); print(len(files), "close files;", len(log), "commands")
```

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / PR-30 / result 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21; rescope D-1, D-2) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08.672Z); primary skill glow-hde-pr-development 1.4.0 |
| role/stage | dedicated WU-PR-07 PR engineering session / PR-30 |
| capture time | 2026-10-20T16:52:30Z |
| execution identity | https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF |
| inherited usage | plan v1.0 and v1.1 (PR-20) and rescope proposal v1.0 (RS-10), this session; instruction v1.0 (PR-10) and rescope review v1.0 (RS-20), session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `390bc99` (`docs/pfcanon/` unchanged since `043fa91`).

| Topic | Sources |
| :- | :- |
| Phase authority, recovery, publication, result vocabulary | PR-30 — PR Implementation Proceed — 100926.1 (read in full); glow-hde-pr-development 1.4.0 (read in full) |
| Scope and validation | plan v1.1 in full (§§1 to 22); the rescope review v1.0 §6 conditions 1 to 7; the addendum overlay (proposed 2.13) |
| Ceiling, real inputs, finding disposition (for PR-35) | PF10-HDE-Build-Notes v13.6.3 addendum 2.11 rules 1, 3, 4, 7 and 8, read with 2.12's numbering; the Product Owner disposition §2 and §3 |
| Operative documentation | `AGENTS.md`: closed rails and redaction; "PR descriptions"; "Code review guidelines"; "Evidence harness" and "Governed evidence rules" (no write-mode updater run in the checkout) |
