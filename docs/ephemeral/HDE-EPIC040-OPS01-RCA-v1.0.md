---
artifact_type: RCA
artifact_id: HDE-EPIC040-OPS01-RCA
artifact_version: "1.0"
change_id: HDE-EPIC040
subject: HDE-EPIC040-OPS01 execution, task v1.0 through receipt v1.2
author: HDE-EPIC040-2, successor retained whole-change HDE-EPIC040 Implementation Architect
requested_by: Nathan (Product Owner)
capture_time_utc: 2026-09-27T05:00:00Z
---

# HDE-EPIC040-OPS01 — Root Cause Analysis v1.0

## 1. Answer

**The main cause was procedure: the Implementation Architect wrote defective Ops tasks.**

Four things compounded it:
- the executor made procedural errors and overclaimed;
- a latent defect in the tool combined with deliberately opaque failure reporting;
- an environment drift in the Codespace, and a failure in how its agent captured terminal output;
- the IA communicated badly with the Product Owner.

**Canon was not a cause.** PF27 §3 already required everything that was missing. The one exception is a small gap: nothing requires a rehearsal before handover. **The prompt bodies were not established as a cause.** I did not read the OPS-10, OPS-20 or OPS-30 Notion bodies for this RCA, so I make no claim about them.

The release itself was never defective. The attestation built and verified at the first valid attempt, and every adverse check refused correctly once it was run properly.

| Category | Verdict | Weight |
| --- | --- | --- |
| Procedure: IA task authoring | **Primary cause** | Four of the five failed cycles |
| Procedure: executor behaviour | Contributing | Two cycles |
| Development: tool robustness and observability | Contributing | Turned a one-line setup gap into an unexplained failure |
| Environment and tooling (Codespace) | Contributing | One cycle, plus the setup drift that exposed the tool defect |
| IA communication with the PO | Contributing | No failed runs, but most of the PO's time and friction |
| Canon | Not causal; one small gap | — |
| Prompt bodies | Not assessed | — |

## 2. Timeline (all times 2026-09-27 UTC)

| # | Artifact or event | Outcome | Immediate cause |
| --- | --- | --- | --- |
| 1 | Task v1.0 (#520, 00:28) | READY | Written as prose, not exact commands. Did not use the PF27 §3 controlled execution contract |
| 2 | Attempt 1, result v1.0 (00:51) | BLOCKED at P-0 | The task required Nathan's delegation but gave no text for it, and the handoff did not tell Nathan what to type or where |
| 3 | Attempt 2, result v1.1 (00:58) | FAIL, reclassified FAIL_TOOLING | The executor created `audit/ops/hde-epic040/` inside the repo before building, so the tree was dirty (`source_tree_not_clean`). With no bundle, A-5 and A-6 crashed (`FileNotFoundError`, `StopIteration`), and those crashes were logged as "exit 1" refusals |
| 4 | Attempt 3, result v1.2 (01:09) | Claimed COMPLETE | Build and verify passed. But the log was not kept, A-5 and A-6 were not reported, and A-7's tamper was left uncommitted, so it refused as "dirty" and never reached the member check. The result overclaimed |
| 5 | Receipt v1.0 (#522) | REJECT | Correct and bounded. The attestation was accepted; A-5, A-6 and A-7 were not |
| 6 | Task v1.1 and script (#523) | READY | The exact script was a real improvement. But its environment step installed only the two requirements files, not the repo package (`-e .`). Its P-0 step was a placeholder asking Nathan to compose text. The script was only checked statically, never executed |
| 7 | Successor IA handoff | Delegation text supplied | I checked the script against the tool code, but only by reading. I told Nathan the checks "will each make the tool refuse" without running anything, and I did not check the environment assumption |
| 8 | Attempt 4, result v1.3 (#524) | STOP | Run 1: the executor's Python lacked `jsonschema`, so the Codespace `.venv` was not the active interpreter. Run 2: `closure_write_and_check` failed with the unrecorded error `ModuleNotFoundError: engine`, because the repo package was not installed. The executor handled this correctly |
| 9 | Receipt v1.1 and task v1.2 (#525) | Cause found | I reproduced the failure in scratch, confirmed the fix, and rehearsed the whole script (PASS). This rehearsal should have happened at step 6 or 7 |
| 10 | Execution prompt in the Codespace | STOP before running | The agent's terminal returned no output, not even for `git rev-parse HEAD`. The executor correctly refused to proceed on missing evidence |
| 11 | IA–PO exchanges | Friction | I repeatedly told Nathan how to run things, issued several prompts, and only produced a PF27 §3 record after Nathan pointed out the template |
| 12 | Task v1.3 (#526), then result v1.4 (#527) | **PASS** | PF27 §3 record plus the package install. A-5, A-6 and A-7 all refused as required |
| 13 | Receipt v1.2 (#528) | ACCEPT | Independently verified |

## 3. Root causes

### RC-1 (primary, procedure). Tasks were handed over without being run.

Neither task v1.0 nor task v1.1 was ever executed by its author before handover. Both prior IA records say so explicitly: the script was "not executed by its author, because execution requires P-0." I repeated this at step 7.

A delegation is needed to create evidence. It is not needed for a scratch rehearsal outside the repository, and the rehearsal at step 9 took about ten minutes and found the defect at once. One rehearsal before handover would have prevented attempts 2, 3 and 4.

### RC-2 (primary, procedure). The execution environment was not specified.

Tasks v1.0 and v1.1 said "requirements.txt and requirements-dev.txt installed." The repository's actual standard also installs the package itself:
- CI: `.github/workflows/ci.yml`, install step with `-e .`;
- the devcontainer: `.devcontainer/scripts/post-create.sh:12`.

The IA copied an incomplete rule. The `AGENTS.md` pytest readiness rule names only `requirements-dev.txt`, and it was written for pytest, not for the release tool.

### RC-3 (primary, procedure). The PF27 §3 template was not used.

PF27 §3 already required each of these:
- exact command proof;
- a controlled execution contract;
- a preflight matrix with status rules;
- run rules;
- required evidence outputs with their content;
- an outcome map.

Task v1.0 was prose. It left the adverse-check mechanics to the executor, which produced the A-5, A-6 and A-7 errors in attempts 2 and 3, and it did not say that nothing may be written in the repo before the build, which produced attempt 2's dirty tree. The template was used only at v1.3.

### RC-4 (procedure). The delegation step was designed as work for the PO.

PF27 §3 requires "a secret-free reference to the direct PO instruction." It does not require the PO to compose text, and it does not require a verbatim quote. The IA's tasks turned this into a prompt for Nathan to write something, without giving him the text, which caused attempt 1 and a later stall.

### RC-5 (contributing, executor procedure). The executor improvised and overclaimed.

In attempts 2 and 3 the executor:
- wrote evidence into the repo before the build;
- counted crashes as refusals;
- left the A-7 tamper uncommitted;
- dropped the attempt 3 log;
- declared COMPLETE without evidence for three required checks.

RC-3 made this possible. Separately, it is an executor fault. From attempt 4 on, executor behaviour was correct: faithful stops, no forced passes.

### RC-6 (contributing, development). A latent tool defect was hidden by opaque failure reporting.

`tools/evidence/regenerate_identity_closure.py` probes admission first, and that probe imports `engine`. The script is run from `tools/evidence/` inside a child environment stripped down to `PATH` and `TMPDIR`. So `engine` resolves only if the package is already installed in that Python, and then it resolves to the installed copy, not the isolated copy.

CI and the devcontainer always install the package, so the dependency never surfaced. By design, the builder records no child stdout or stderr (`stdout_recorded=false`), so the executor saw only `isolated_stage_failed` and could not diagnose it.

This is carried as O-OPS01-01. It is not a release defect: on a clean candidate the exact-copy check keeps the bytes identical.

### RC-7 (contributing, environment and tooling). The Codespace drifted and its agent terminal failed.

The executor's interpreter lacked `jsonschema`. The devcontainer puts `.venv/bin` first on `PATH` and builds it in post-create, so either that venv was absent or broken, or another Python was active. Separately, the Codespace agent's terminal capture returned no output. Nothing in this epic changed `.devcontainer/`: its last change was 2026-07-08, "QA Pass 2 HDE-EPIC037".

### RC-8 (contributing, IA communication). The IA misread what the PO needed.

The IA over-specified how the PO should run things, which Nathan had not asked for, and sent several successive prompts where one template-conformant record was needed. It cost no failed runs, but it cost most of the PO's time.

## 4. Canon assessment

- **PF27 §3 (Ops Task Record):** adequate and not causal. It required the fields whose absence caused RC-3. It allows personal PO execution or explicit delegation without requiring composed text, which bears on RC-4.
- **Gap G-1:** PF27 §3 does not require the facilitating IA to rehearse an executable command artifact (outside the repository, creating no evidence) before READY. The rule against inventing commands does not cover commands that were written but never run. This is a candidate for canon improvement through its maintainer. It is not authored here, and it is non-gating.
- **Gap G-2:** PF10 — HDE Build Notes (release-attestation posture) and PF12 name the attestation tool but not its execution-environment prerequisite, the installed package. This is a candidate note for the same maintainers. Non-gating.
- **PF07:** not causal. The task needed no hosted facts.

## 5. Corrective and preventive actions

| ID | Action | Owner | Status |
| --- | --- | --- | --- |
| CA-1 | Every executable Ops artifact is rehearsed by the IA outside the repository before READY. The rehearsal is recorded as non-evidence in the task | This IA (applied from task v1.2 on) | Adopted |
| CA-2 | Ops tasks are written in the PF27 §3 template, including the controlled execution contract | This IA (v1.3 on) | Adopted |
| CA-3 | The execution environment is stated exactly as the repository's own standard (`-e .`), with an import probe run outside the repo | This IA (v1.2 on) | Adopted |
| CA-4 | The PO never composes delegation text. The task gives the delegation reference, and the executor records it | This IA (O-OPS01-02) | Adopted |
| CA-5 | The IA hands over deliverables and requirements only. It does not prescribe how the PO runs them | This IA | Adopted |
| PA-1 | Make the closure admission probe self-contained (repository root on the import path, or the isolated package), and record a names-only failure detail for isolated stages | Evidence-tool owner, through change control (O-OPS01-01) | Open, non-gating |
| PA-2 | Add the package install to the `AGENTS.md` readiness rule for release-tool work | Doc agents, under PO direction | Open, proposal |
| PA-3 | G-1 and G-2 canon notes | PF27, PF10 and PF12 maintainers | Open, proposal |
| PA-4 | Repair the Codespace: rebuild the container so post-create recreates `.venv`, and check the agent's terminal integration | PO environment | Open, outside this epic |
| PA-5 | Check the OPS-10 and OPS-20 prompt bodies for the "verbatim quote" and "rehearsal" points | Prompt-ecosystem owner | Open, not assessed here |

## 6. Non-claims

This RCA changes no decision. OPS01 stays accepted (receipt v1.2), and it establishes no QA, acceptance, PF09 movement or closure. It makes no finding about the Notion prompt bodies, which were not read. No canon is edited.
