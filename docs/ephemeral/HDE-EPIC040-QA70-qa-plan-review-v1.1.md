---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-EPIC040-QA70-QA-PLAN-REVIEW
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.0.md (APPROVE; rejected by the Product Owner 2026-09-27; history only)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
decision: DENY
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
reviewer: Isis — continuing Lead Developer and QA Plan reviewer
session_disposition: RETAIN_EXISTING
role_session_ref: continuing HDE-EPIC040 Isis session (execution identity https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq, the same identity recorded in QA-10 readiness and the QA-20 Guide)
invocation_binding: EPIC / HDE-EPIC040 / QA-70 / QA_PLAN v1.0 (restart)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
restart_authority: Product Owner, 2026-09-27 ("restart QA-70"); Alpha state record docs/ephemeral/HDE-EPIC040-alpha-state-stopped-failed-at-qa-v1.0.md
prompt: QA-70 — Review Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb8143bf26d1459fbbcad7; page as of 2026-09-24T15:55:17Z; read in full this session)
reviewed_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; read in full, 837 lines)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0; read in full)
author: Kronos (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md (see Canon relied on for the parts read)
observed_revision: 3be23de (origin/main)
decision_time_utc: 2026-09-27
PF10_ADDENDUM_OUTPUT: NONE (initial-mode DENY produces no addendum)
---

# HDE-EPIC040 — QA Plan Review v1.1 (QA-70, restart)

## 1. Decision

**`DENY`.** QA Plan v1.0 is not approvable. Six blockers remain after faithful syntax normalization. Each changes rails posture, verdict meaning or evidence trust, and each contradicts PF-Canon that I have read in full (§2). The Plan returns to the same Kronos author through QA-80 with the redlines in §5.

What is sound and must be kept: the open-rails vendor step (check 11) posture and scope, the evidence root and step-log contract, the rerun and Moon Loop bounds, the PF09 accountability table, the nonclaims, and coverage of both Product Owner dispositions.

This review replaces v1.0, which approved the same Plan without reading the rails canon (RCA v1.1). No PF10 addendum is produced. This is not task selection, execution, QA PASS, merge or closure.

## Canon relied on

Every PF source below was read from `docs/pfcanon/` on `main` at `3be23de`, in the sections listed, in full.

**Glow QA Guide** (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md`):

| Section | Governs in this review |
| --- | --- |
| §2.2.6 Rails posture in CI | Closed rails default |
| §2.3 Rails & environment posture | Two rail states; `captured_env`; recording closed-rails runs where open rails are required |
| §3.1–§3.3, incl. §3.3 Environment constraints — pre-App, no-user QA mode | No app users or user-bound BodyGraphs; blocked-by-environment deferral; DB-backed paths not valid live acceptance; local/offline labels; vendor-backed birth-only posture |
| §3.4.1–§3.4.14 (all of §3.4) | One command per artifact; tooling discipline; evidence grammar; §3.4.8 rails for manual Live QA, execution-critical helper readiness, closed-rails ownership by CI and pre-merge QA; §3.4.10 plan lint and approval materiality |
| §3.5.5 PO Live QA sessions (vendor-first rails) | Check classes 1/2/3; Codespaces not a surrogate prod; production-affecting open-rails minimum |
| §3.5.6 Vendor vs non-vendor steps | Mandatory class labels and PO subset |
| §3.5.7 Evidence expectations for vendor-focused PO steps | Vendor evidence set; failure classification |
| §11.3 Canon-first QA preparation | No PO questions canon answers; PF07-derived/PF07-gap; closed vs open-rails prod checks |
| §14.1–§14.6 Codespaces QA environments | Venue materiality; §14.4.2 Codespaces is not prod; §14.5.1 HD Engine profile rails (closed `SAFE_MODE=1 ALLOW_NETWORK=0`; open only for an approved step; `APP_ENV=dev` for dev-gated local checks) |

**Plan Templates** (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md`): "Unknowns, discovery, deferral, and open rails"; "Canon precedence for template use"; §A.1 Live QA Plan in full, including "Open-Rails Live QA Requirement", "Environment and rails posture", "Rails posture (explicit)", "Step-log header schema expectations" (`PARKED` definition), Step-0B, Check Blocks and "Vendor-dependent steps (rails-scoped)"; "Review guardrails" in full, including "Hard blockers", "Live QA Plan approval materiality discipline", the redline bundle rules and "Review stability and no-moving-target discipline"; §2 "QA Rails — Open/Close (Final PR)".

**Glow Infrastructure** (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md`): §0 production rails and CI-lane boundary (L61); §2.1–§2.2 environments; §2.4 Env Deployment Inventory (Production, Development, QA Codespaces bindings); §2.6; §2.7 Terminal CLI access, including the CLI-local vendor smoke target; §2.8.

**HDE CLI/API Vendor Ref** (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`): §7.3.9 (open-rails QA step required for affected CLI/vendor surfaces); §7.4 adapter data-source policy.

**HDE Build Notes** (`docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md`): the index; addendum 2.28 read in full; the whole document searched for `rails`, `live qa`, `SAFE_MODE` and `ALLOW_NETWORK` (38 hits, each read in context). No addendum sets or overrides a QA rails or Live QA environment rule for HDE-EPIC040. Addendum 2.29 governs canon location. PF10 was not read in full.

**In-flight change documents** (`docs/ephemeral/`): QA Plan v1.0 and QA Audit v1.0, in full; Live QA Guide v1.0, in full; QA readiness v1.0 and PO disposition v1.0, in full; Specification v1.1 §6.2–§12, in full; Implementation Plan v2.1, searched for `rails`, `live qa`, `current rows` and `unobserved`; QA-70 review v1.0 front matter and §1; RCA v1.1, in full.

**Per-topic governing section:**

| Topic | Governing section |
| --- | --- |
| Rail states | Glow QA Guide §2.3, §14.5.1; Glow Infrastructure §2.4 |
| Production posture | Glow Infrastructure L61 and §2.4 Production; Glow QA Guide §3.5.5, §11.3, §14.4.2 |
| Vendor step posture | Glow Infrastructure §2.7; Glow QA Guide §3.3; Plan Templates "Vendor-dependent steps" |
| No-user environment | Glow QA Guide §3.3 |
| Closed-rails ownership and labels | Glow QA Guide §3.3, §3.4.8, §3.5.5, §3.5.6 |
| Execution-critical helpers | Glow QA Guide §3.4.8 |
| Deferral and `PARKED` | Plan Templates "Unknowns, discovery, deferral"; "Step-log header schema expectations" |
| Venue | Glow QA Guide §14.1 |
| Open-rails requirement | HDE CLI/API Vendor Ref §7.3.9; Plan Templates "Open-Rails Live QA Requirement" |

## 2. Rail postures canon allows for HDE-EPIC040 Live QA

Canon settles these; the Plan must use only them.

| Posture | Values | Where it applies | Canon |
| --- | --- | --- | --- |
| Closed (default) | `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, pins `LC_ALL=C LANG=C TZ=UTC` | Every check except the vendor step | Glow QA Guide §14.5.1, §2.2.6; Glow Infrastructure §2.4 Development and QA bindings |
| CLI-local vendor | `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=dev`, same pins | `hdctl showcompat --source vendor`, birth-only, for that step only, then back to closed | Glow Infrastructure §2.7; Glow QA Guide §3.3 |
| Production | `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod` | Only the deployed Railway service `glow-hdengine-v2`. Never a local or Codespaces process | Glow Infrastructure L61, §2.4, §2.6; Glow QA Guide §3.5.5, §14.4.2 |

A database read under closed rails is lawful (Development and QA bindings carry `DATABASE_URL` with `ALLOW_NETWORK=0`). But Glow QA Guide §3.3 bars relying on user-bound rows, and it bars counting DB-backed paths as live behavior acceptance in this pre-App environment.

## 3. Findings

All blockers are **Review Drift** under Plan Templates "Review stability". The text was visible and unchanged when v1.0 approved it. The trigger that makes each newly raisable is a prior read failure: v1.0 was issued without reading the governing canon (RCA v1.1 §2.1, C1–C2), and the Product Owner rejected it.

| ID | Class | Defect | Governing canon | Material harm |
| --- | --- | --- | --- | --- |
| FND-001 | Blocker | Checks 10, 13 and 14 start a local server at `APP_ENV=prod` under closed rails (ENV-S, and ENV-D's server). Check 10 is titled "live production Reader route", and S-22 to S-25 claim "dev routes refuse in production posture". No canon environment has this posture. A local or Codespaces process is not prod | Glow QA Guide §3.5.5 ("Codespaces MUST NOT be used as a surrogate 'prod' environment"), §14.4.2 ("MUST NOT be treated as prod"); Glow Infrastructure L61 and §2.4 (the production pair is `SAFE_MODE=0 ALLOW_NETWORK=1` on Railway) | The recorded verdicts would assert production behavior that no production environment produced. Verdict meaning and rails posture are false |
| FND-002 | Blocker | Check 7 command 1 sets `SAFE_MODE=0` with `ALLOW_NETWORK=0` for one command inside a check. This mixed pair is neither canon state, and the Plan changes rails per command. The command also duplicates the existing unit test `test_open_or_unpinned_rails_refuse_before_any_database_access` (`safe_mode_open`, `tests/bodygraph/test_check_magic10_gate_readiness.py` L375–389), which group D runs in the same check | Glow QA Guide §2.3, §14.5.1 (two defined states); Plan Templates "Rails posture (explicit)" (rails change per check); Plan Templates "MUST NOT include a step … solely 'for good measure'" | An undefined rails state enters governed evidence. The step adds no proof |
| FND-003 | Blocker | Checks 12 and 14 require existing current rows and a Product Owner list of user UUIDs (§6 "Readiness selection file"; QA50-F05). Guide §4.3, which I authored, made this mandatory | Glow QA Guide §3.3: no app-level user IDs and no persistent user-bound BodyGraphs exist pre-App. Such requirements "are treated as blocked by environment" and "must be explicitly called out in epic-level QA plans and deferred to a future epic". Glow QA Guide §11.3: no PO inputs for what canon settles | The Plan depends on an input canon says does not exist, and asks the PO for it. Any PASS would rest on rows QA may not rely on |
| FND-004 | Blocker | Check 13 counts a live DB-backed Reader refusal as AC040-09 live behavior, in the FND-001 posture | Glow QA Guide §3.3 ("Engine 'DB/auto' compat paths … are not valid for Live QA behavior acceptance in this environment"; "no canonical DB-backed compat source for live behavior tests") | Evidence would be credited to a claim canon says it cannot support |
| FND-005 | Blocker | No check carries its PF19 class label (1 ops/identity; 2 internal functional/determinism; 3 vendor). The Plan does not state which subset is PO Live QA workload. §7.1 makes the PO the executor for all 15 checks. Checks 3–9 re-run closed-rails suites and validators and map them to AC040-02 to AC040-08 as acceptance, but only check 8 is labelled local/offline | Glow QA Guide §3.5.6 (MUST label each step and the PO subset); §3.5.5 (class 2 "must not be scheduled as PO Live QA tasks"); §3.3 (non-vendor runs "must be labeled accordingly in QA plans"); §3.4.8 (closed-rails testing is CI and pre-merge QA responsibility); §3.4.14 (bind existing workflow records; do not duplicate) | Acceptance meaning for seven criteria is misstated, and the PO's workload is wrong. The next QA-90/QA-100 would repeat the failed run's shape |
| FND-006 | Blocker | The final decisive command of checks 6, 10, 11, 12, 13 and 14 is an "evaluator (embedded `python -c`)". Its code is not in the Plan and would be written at execution time | Glow QA Guide §3.4.8, "Execution-critical helper readiness (normative; preapproval blocker)". Such a helper must be smoke-validated before plan approval, and a plan "MUST NOT embed … large inline programs, newly invented runners" | The decisive PASS/FAIL of six checks would come from unreviewed code composed during the run. Verdictability and evidence trust are lost |
| FND-007 | Caveat | Check 8 passes on rc 0, while three tests in `tests/cli/test_showcompat_parity_and_identity.py` (L108, L128, L150) skip with "showcompat vendor calls require open rails" | Glow QA Guide §2.3 (a closed-rails run where open rails are required must say so explicitly); Plan Templates status predicates (a native skip does not map blindly to a governed outcome) | Skipped tests could be read as passing vendor coverage. Safe default: record each skip and state that it contributes no proof |
| FND-008 | Caveat | Front matter says venue cannot affect results. The QA-100 run in `06b04a9` failed a group G assertion on a Codespaces file mode: `docs/evidence/INDEX.sha256` 420 expected, 438 observed (`audit/qa/hde-epic040/checks/ac040-08-evidence-validators/primary.log` L174–177 on branch `qa/hde-epic040-qa100-checks-1-10`) | Glow QA Guide §14.1 (venue is material when behavior "is reasonably capable of differing in Codespaces because of the … filesystem") | Observed evidence contradicts a stated premise. The affected check needs a venue statement or a proof that venue cannot affect it |
| FND-009 | Caveat | The Plan requires every primary log to be written through `record_check`, but gives a hand operator no stated way to do it. In `06b04a9` the PO-run logs have no `pf27.step_log_header.v2` header and no manifest exists (for example `d0-discovery/primary.log` starts `# T01 d0-discovery`). Check 10 captured one refused connection | Glow QA Guide §3.4.10 ("Live QA Plan approval is an operational-readiness review … clear enough for the assigned operator"); Plan Templates Check Blocks dependency posture | PO-run checks may again produce evidence the reviewer cannot accept |

### Decisions carried to this review

| Item | Decision |
| --- | --- |
| C040-09 (Glow Infrastructure §2.8 vs Glow QA Guide §3.4.9 and Plan Templates) | **APPROVED_AS_CHANGED.** Glow Infrastructure §2.1 is "Names-only … No procedures or policy here", and §2.8 routes the Live QA execution rail to the Glow QA Guide. So Glow QA Guide §3.4.9 (read-only repository observation for attribution, never a PASS predicate) and Plan Templates (invocation of tracked harness entrypoints) govern. The change: this approval covers invoking tracked, tested entrypoints (`tools.qa.qa_harness`, `_refresh_path_proof`) through `python -c`. It does not cover newly written decisive evaluators, which Glow QA Guide §3.4.8 governs (FND-006). Drainage: Glow Infrastructure §2.8 wording, PF07 maintainer, documentation only. Reviewer: Isis, this artifact, 2026-09-27 |
| QA50-S01 (birth tuples in evidence) | Confirmed as proposed. Synthetic QA tuples, recorded verbatim as Glow QA Guide §3.3's substituted birth-input record, satisfy both that section and Plan v2.1 §7.4. Default: the L-51 tuples |
| QA50-S02 (population of "current rows") | Moot under FND-003 |
| Check 11 `open-rails-showcompat-vendor` | Posture, inputs, forbidden inputs, secret handling, evidence set and exercised-versus-inferred statement conform to Glow Infrastructure §2.7, Glow QA Guide §3.3 and §3.5.7, and HDE CLI/API Vendor Ref §7.3.9. It satisfies the Plan Templates open-rails requirement and PO Q-2. Only its evaluator step is affected (FND-006) |
| Glow Infrastructure §2.4 QA binding has no `SAFE_MODE` (RCA D-2) | Not a gap for this Plan: the HD Engine Codespaces profile sets closed rails `SAFE_MODE=1 ALLOW_NETWORK=0` (Glow QA Guide §14.5.1) |

### Upstream defects recorded, not redlined here

| Item | Owner | Treatment |
| --- | --- | --- |
| Guide §4.3 mandates a live readiness run against current rows, and §5 states default rails without citation | Isis (QA-20 author) | Canon governs over the Guide (Glow QA Guide §3.3, §14.5.1). QA-80 follows canon, not Guide §4.3. The Guide is not re-issued by this review |
| Implementation Plan v2.1 has no epic rails statement ("QA Rails — Open/Close (Final PR)", Plan Templates §2 A) | Whole-change IA | Carried finding (RCA v1.1 C6). It does not block this QA Plan, because the posture follows from canon (§2 above) |

## 4. Coverage after correction

With the redlines applied, AC040-07's live part and AC040-09's live success path are not claimable in this environment. They are recorded as blocked by environment and deferred (Glow QA Guide §3.3). The Specification's own boundary already says "unavailable live facts remain unavailable" (AC040-07). QA-120 then reports those parts as not supported for that stated reason, not as failures. Every other criterion keeps a check.

## 5. Redlines for QA-80

One-pass bundle. Every anchor is in the unchanged Plan v1.0, and no two regions overlap. Each redline states the required outcome and its canon. Kronos chooses the wording, commands and evidence design, within the Audit's proven loci. No new locus is supplied here.

| ID | Base region (Plan v1.0) | Required outcome | Finding |
| --- | --- | --- | --- |
| RL-01 | Front matter lines 33–39 (venue fields and "Target environment") | State the target truthfully: a local QA console under the closed or CLI-local vendor posture, plus HumanDesignAPI for the vendor step. Either give the four venue-materiality fields for any check the filesystem can affect (Glow QA Guide §14.1), or show why venue cannot affect it | FND-001, FND-008 |
| RL-02 | §2 scope list, lines 80–84 (D9 to D13) | Re-scope D9 and D12 to canon postures (RL-06, RL-08). Mark D11 and D13 as blocked by environment and deferred under Glow QA Guide §3.3, with the reactivation condition (a future epic defining user-bound QA surfaces once the App user model exists) | FND-001, FND-003, FND-004 |
| RL-03 | §5.2 in full (lines 160–179) | Replace the four ENV classes with the §2 postures of this review. No class may pair `APP_ENV=prod` with a local process. Rails change only between checks. Remove the per-command `SAFE_MODE=0` paragraph (line 177). Keep the unset lists for keys that are not needed | FND-001, FND-002 |
| RL-04 | §6 PO inputs, rows at lines 191 and 194 | Remove the readiness selection file input. Keep `DATABASE_URL` only if RL-08 retains a DB-reading check, citing the Glow Infrastructure §2.4 QA binding | FND-003 |
| RL-05 | §7.1 in full (lines 201–206) | Assign class 2 checks to QA/infra (a named delegated executor) outside PO Live QA time. The PO runs class 3 (the vendor step) and any class 1 pre-flight the Plan assigns to the PO (Glow QA Guide §3.5.5) | FND-005 |
| RL-06 | CHECK 10 block in full (lines 568–624) | Run under the closed posture with `APP_ENV=dev`, or remove. Retitle it without "live production". Keep the Q-1 security probes that the production route answers identically under `dev`. For the dev-route production-gating probes S-22 to S-25, choose either: (a) target the deployed production service under Glow QA Guide §11.3, with a PF07-derived base URL, open rails and PO authorization, stating what deployed identity it proves and does not prove; or (b) drop the live claim and cite the in-process coverage as in-process class | FND-001 |
| RL-07 | CHECK 7 block, command 1 only (line 524) | Remove the command. The group D unit test already proves the refusal | FND-002 |
| RL-08 | CHECK 13 block in full (lines 692–717) | Remove it, or re-posture it to the closed posture (`APP_ENV=dev`, Glow Infrastructure §2.4 QA `DATABASE_URL`). Relabel it as a class 1/2 secret-safety observation with no AC040-09 live-behavior claim (Glow QA Guide §3.3) | FND-001, FND-004 |
| RL-09 | CHECK 12 block (lines 658–690) and CHECK 14 block (lines 719–746) | Record both as `PARKED` before execution, under Glow QA Guide §3.3 as the controlling source. State the affected acceptance claim (AC040-07 live part; AC040-09 live success) and the reactivation condition (Plan Templates `PARKED` definition). No commands, inputs or probes | FND-003 |
| RL-10 | §10 matrix and §11 dependency table (lines 278–318) | Add the Glow QA Guide §3.5.6 class for each check, and mark the PO Live QA subset. Label every class 2 check "local/offline (no vendor)". For each closed-rails criterion, name the existing exact-head CI or PR evidence that supports it alongside the local run (Glow QA Guide §3.4.14). Update dependencies for RL-06, RL-08 and RL-09 | FND-005 |
| RL-11 | §12 common rules (lines 322–331) | Add how a hand operator produces the `pf27.step_log_header.v2` header and manifest entry for each PO-run check, with a step-local preflight proving that mechanism runs. Add that no decisive evaluator is composed at run time: each decisive predicate is either evaluated by a tracked, tested entrypoint, evaluated by Kronos at QA-110 from the captured artifacts, or given in full in the Plan and smoke-validated before approval under Glow QA Guide §3.4.8 | FND-006, FND-009 |
| RL-12 | CHECK 8 predicates (line 550) | Record each skipped test with its reason. State that skips contribute no proof, and that vendor-backed behavior is carried by check 11 | FND-007 |
| RL-13 | §14 check-to-PF09 mapping paragraph (line 806) | Make it consistent with RL-08 and RL-09: parked checks map to no current proof | FND-003 |

Checks 6 and 11 need no block redline beyond RL-11. Their evaluator steps follow the RL-11 rule.

## 6. Unresolved items and owners

| Item | Owner |
| --- | --- |
| QA Plan revision per §5 | Kronos, QA-80 |
| Guide §4.3 and §5 defects | Isis (recorded; canon governs) |
| Epic rails statement missing from Implementation Plan v2.1 | Whole-change IA |
| QA-100 attempts in `06b04a9` (T01–T10) | Kronos at QA-110, after the revised Plan (RCA v1.1 §6) |
| Glow Infrastructure §2.8 wording (C040-09) | PF07 maintainer, documentation only |
| Deferred live readiness and live Reader success | Future epic that introduces the App user model (Glow QA Guide §3.3) |

`CANON_CONFLICT_REGISTER`: C040-01 to C040-08 carried unchanged from QA Audit §11. C040-09 decided above.

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-70-20260927-02
  change: EPIC / HDE-EPIC040 (Specification v1.1)
  prompt: QA-70 — Review Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb8143bf26d1459fbbcad7; release GCFPE-20260914.1
  role_stage: continuing Isis, QA-70 (restart after rejected v1.0)
  capture_time: 2026-09-27
  execution_identity: https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
  result: QA_PLAN_REVIEW v1.1, DENY, routed to QA-80 (same Kronos)
  repository_persistence: PENDING / NON_GATING
- earlier entry: GCFPE-USE-HDE-EPIC040-QA-70-20260927-01 (v1.0, rejected)
```
