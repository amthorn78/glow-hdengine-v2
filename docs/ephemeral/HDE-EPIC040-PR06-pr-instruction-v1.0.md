---
artifact_type: PR_INSTRUCTION
artifact_id: HDE-EPIC040-PR06-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR06
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-09-25T08:13:25Z
next_stage: PR-20
---

# HDE-EPIC040-PR06 — PR Work-Unit Instruction v1.0

## 1. Identity and state

| Field | Value |
| --- | --- |
| Artifact | `PR_INSTRUCTION` `HDE-EPIC040-PR06-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY` |
| Change / unit | `EPIC` / `HDE-EPIC040` Separation Pass 3 / `HDE-EPIC040-PR06` — Complete release admission and evidence convergence |
| `AUTHORING_CONTEXT` | `APPROVED_BASE_WITH_OVERLAYS` |
| Author | Retained whole-change HDE-EPIC040 Implementation Architect; `session_disposition: RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06 / PR-10`; `context_conflict: NONE` |
| Posture / time | `MANUAL_PROMPT_EXECUTION` / `2026-09-25T08:13:25Z` |
| Path | `docs/ephemeral/HDE-EPIC040-PR06-pr-instruction-v1.0.md` |

This is one work unit's instruction. It is not a detailed plan, not a Proceed, and not authority to merge, run QA or Ops, deploy, activate a release, edit PF10, or close anything.

## 2. Approved lineage (all under `docs/ephemeral/` on `main`)

| Role | Artifact | Identity |
| --- | --- | --- |
| `SPECIFICATION_REF` | `HDE-EPIC040-specification-v1.1-approved.md` | v1.1, Thoth-17 `APPROVE`; SHA-256 `43e1b182…e9df` |
| `IMPLEMENTATION_AUDIT_REF` | `HDE-EPIC040-implementation-audit-v2.0.md` | v2.0 `AUDIT_COMPLETE` |
| `IMPLEMENTATION_PLAN_REF` | `HDE-EPIC040-implementation-plan-v2.1.md` | immutable approved base; SHA-256 `10732f93…1be`. The header reads `PLAN_PENDING_REVISED`; that is its authoring state. Approval comes from the review in the next row |
| `PLAN_REVIEW_REF` | `HDE-EPIC040-implementation-plan-review-v2.1.md` | Isis-50 `APPROVE` 2026-09-09T13:36:43Z |
| Approved overlay | `HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` + `HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` | RS-20 `RESCOPE_REVIEW` `APPROVE` (this is not a remediation review). Published as PF10 §2.15 |
| Accepted predecessors | PR01 v1.1, PR02 v1.0, PR03 v1.0, PR04 v1.0, PR05 v1.0 lineage reviews (`HDE-EPIC040-PR0N-pr-work-unit-lineage-review-v1.x.md`) | All `ACCEPTED_FINAL`. The PR05 review has SHA-256 `7265e9cf…b023`; it names PR06 next and carries O-17/CR-06 to it |

**Current PF10.** Resolved from `docs/pfcanon/` as `PF10-HDE-Build-Notes-v13.3.1.md` (2,239 lines, SHA-256 `66305b8f…9c14`, effective 2026-09-25). It is a strict superset of v13.3: same addenda 2.1–2.19, plus 2.20 recording PR05's acceptance.

**Observation O-P06-01, non-gating, owned by Nathan.** `PF10-HDE-Build-Notes-v13.3.md` is still present beside v13.3.1. The commit that added v13.3.1 did not remove it, whereas the v13.2.9 → v13.3 update removed its predecessor. PF10 §3 allows one active unlettered base version, so v13.3.1 is taken as current. PR-20 must re-resolve PF10 when it runs.

**Applicable overlays:**
- §§2.2–2.5: C040 decisions. There is one four-argument core only, and the 36-row taxonomy governs.
- §§2.6–2.11, 2.13, 2.19, 2.20: accepted predecessor behaviour, consumed unchanged.
- **§2.12:** the admission execution-provenance owner in `engine/config/registry_loader.py` stays the admission boundary. PR06 exercises it for real and must not weaken it.
- **§2.15 (F01):** PR06 is the unit whose complete admission ends the `RELEASE_NOT_ADMITTED` interval (§5.4).
- §§2.16–2.18: the F03/F05/F07 deferrals to PR07 (§8).

## 3. Baseline and verified state

- `main` is at `f41714919053a3ed1533a5e3e3ae48252ca3208f` (tree `51e6d48a…`). Since PR05 landed (`4d7ab9d`), every change is under `docs/`. PR-20 re-verifies this.
- **Manifest vs roster, verified:** `catalog/manifest.json` is version `1.0.0`, `built_at_utc 2025-12-26T00:00:00Z`, and has **15** members, none extra. `ADMITTED_RELEASE_ROSTER` has **44**, so **29 are missing**. All 44 roster paths exist on disk.

  The 29 missing are: `adapter/schemas/error_v1.schema.json`, `catalog/magic10_mechanics_v1.json`, `engine/bodygraph/{gates,mapped_cache,projection,resolver,v2_adapter}.py`, `engine/categories/registry.py`, `engine/cli/main.py`, `engine/compat/{compute,error_tokens}.py`, `engine/config/registry_loader.py`, `engine/core/core.py`, `engine/http/compat_handler.py`, `engine/magic10/{calculators,composite,signals}.py`, `engine/narratives/router.py`, `engine/runtime/public.py`, `engine/stable/sercanon.py`, `errors/token_map/token_map.json`, `presenter/reader_v1/emitter.py`, `schemas/{channels_v1,gates_v1,magic10_compat_result_v1,magic10_mechanics_v1,magic10_result_v1}.schema.json`, `schemas/reader.v1.schema.json`, `tools/bodygraph/check_magic10_gate_readiness.py`.

- **Roster authority.** The effective **44-member `ADMITTED_RELEASE_ROSTER`** (PR02/PR03, PF10 §§2.9–2.13) is the exact target. It supersedes Plan §5.10's 15 + 31 description where the two differ; for example, the roster also includes `engine/categories/registry.py`, `engine/stable/sercanon.py` and `schemas/gates_v1.schema.json`. A disagreement between the roster and any other list is a finding (§9), not something to edit to fit.
- **Cutter gap, verified.** `scripts/cut_release_manifest.py` validates and refreshes the **existing** rows. It has no promoted-membership construction. Plan §6.6 names extending it as owned work.
- **Admission today:** `load_active_mechanics_bundle()` refuses with `INCOMPLETE_RELEASE_ROSTER`. After PR06 it must admit the real repository root.
- **CI lanes:** `catalog/manifest.json` → `{release}`; `scripts/cut_release_manifest.py` and `registry_loader.py` → `{product, release}`; the sanity log → `{evidence, release}`.

**Sources** (unique controlled Markdown in `docs/pfcanon/`):
- PF12 v2.9.5: manifest, canonical JSON, attestation `hde.release_attestation.v1` including `PR06R_B_FINAL_PASS`, and evidence owners.
- PF01 v1.3.7 §9.6 "Pack closure and release identity", and §9.5 goldens.
- PF02 v2.4.5, PF05 v2.5.2, PF14 v3.5.7 §6.7 with C040-05, PF09.3 v1.1.5, PF03.
- PF10 v13.3.1.
- There is no fallback source.

## 4. Objective and completion (Plan §§5.10, 6.6)

**Objective.** Close the actual complete promoted release and its same-root, deterministic generated evidence.

**Completion.** The real candidate passes full release admission and current tests and CI, with coherent evidence. The final external clean-candidate attestation is **not final until PR07's documentation lands**; that belongs to OPS01. There is no activation and no deployment.

**Excluded:** PR07 (DOC-10 and F03/F05/F07), OPS01, independent QA, Ops, deployment, live DB or vendor work, PF10 edits, PF09 movement, Epic closure.

## 5. Required behaviour

### 5.1 Manifest materialization
- Preserve every legitimate existing member. Add or refresh each missing roster member exactly once, so the manifest is the complete 44 in ASCII order. There must be no self-listing and no non-input extras.
- Version **`1.1.0`** and `built_at_utc` **`2026-08-24T18:04:49Z`** are Canon-fixed source values (Plan §5.10), not this run's clock.
- Validate each member's format, then its hash and size, over the exact validated bytes. Reject unknown keys, duplicates, ordering errors, unsafe paths (absolute, escaping, backslash, empty), invalid hash/size/date/version, and missing members.
- Extend `scripts/cut_release_manifest.py` for exact promoted-membership construction (Plan §6.6). Cut only after **all** intended source bytes are final. A later source change requires a re-cut.
- `release_id` = sha256 of the canonical manifest bytes. Validate with `scripts/release_id_recompute.py --check-manifest-only`.

### 5.2 Admission and generated configuration
- Validate active admission from the actual candidate root through the unchanged §2.12 owner (`registry_loader.py`; integrate only). Active config source hashes cover the four exact inputs only, never release or evidence outputs.
- Then, from the **same capture**, generate `config.magic10`, band edges, the registry report and the FE/BE bundles through their owners: `tools/config/generate_config_artifacts.py`, `tools/config/generate_bundles.py` and `tools/generate_registry_report.py`.
- The registry report binds only registry catalog inputs; it never binds release identity (`AGENTS.md`).

### 5.3 Generation order (Plan §6.6)
1. Source, config and schema bytes.
2. Complete manifest and release.
3. All applicable primary generated artifacts.
4. Owning index and skeleton assembly (`tools/evidence/update_evidence_index.py`, the sole Index/Mirror writer).
5. Read-only schema, hash, path, orientation, sentinel and mirror checks.

Do not postpone already-changed PR01–PR05 companions. Nothing is hand-edited. Historical EPIC022 release evidence is not refreshed to fake equality.

### 5.4 F01 interval ends
- With the real roster admitted, the F01 non-admitted branch must stop being taken on the real root. Governed gates return to requiring PASS; the F01 code stays and becomes inert (PF10 §2.15). There is no removal obligation.
- **Sanity-log transition `NOT_ADMITTED → PASS`**: run the owner's canonical `run_sanity_pipeline.py` run, then a full updater run (PR04 observation O-07).
- The attestation builder must now pass all fifteen stages and may emit `PR06R_B_FINAL_PASS` **only** from a genuinely admitted real candidate, into an external empty directory. That in-CI build is not the final OPS01 attestation. There is no change to `hde.release_attestation.v1` or its wire value; any change there is a separate PF12 decision.
- Frozen capture-time families are regenerated **only** where their owner can now truthfully do so from admitted sources. Otherwise they stay frozen, with nonclaims, and are recorded.

### 5.5 Comparator against the actual candidate (Plan §6.5 completion; PR05)
- Run PR05's `generate_config_artifacts.py --compare-goldens` against the actual complete candidate, expecting all eight goldens equal. A mismatch is a finding; never rewrite expected values.
- **O-17/CR-06, inherited from PR05:** golden runners execute the running installation's application modules. Admission binds executing code to candidate bytes only for its covered modules. Decide the bounded treatment, inside the admission owner's existing scope, so that a manifest-consistent candidate with a non-runnable application member cannot report `ok: true`. If the treatment requires widening the §2.12 covered-module set beyond what the approved overlays allow, apply §9.

## 6. Owned loci (Plan §6.6)

- `scripts/cut_release_manifest.py` and `scripts/release_id_recompute.py`.
- Admission integration in `engine/config/registry_loader.py`.
- `tools/config/artifacts.py` and `tools/config/generate_config_artifacts.py`, `tools/config/generate_bundles.py`, `tools/generate_registry_report.py`.
- `tools/evidence/update_evidence_index.py`.
- The owning attestation validator, **only where a contract gap is evidenced**.
- `catalog/manifest.json` via its cutter.
- Existing manifest, config and evidence tests.

Governed artifacts are regenerated by their owners. No new release ledger and no duplicate Index. Registering a new path in `ci/checks/classify_ci_changes.py` is a coherence dependent if one is needed.

## 7. Acceptance, tests, evidence (Plan §§6.6, 7.2–7.4, 8)

- **Requirements:**
  - `K040-REQ-006`: single immutable manifest-bound active configuration; no partial release.
  - `K040-REQ-009`: distinct config, source, pair, manifest and repo identities, with exact closure.
  - `K040-REQ-010`: actual-candidate comparison.
  - `K040-REQ-012`: convergence of primaries and companions.
  - Portions of `-001`, `-004`, `-008` and `-011`.
- **Acceptance criteria:** `AC040-05`, `-06`, `-08`, `-09` for their PR06 portions. OPS01's external proof is not claimed.
- **Positive:**
  - The actual complete admitted candidate.
  - All eight goldens equal against it.
  - Coherent regenerated evidence.
  - Admission refuses at the real root before PR06 and succeeds after.
- **Adverse:**
  - Each promoted member omitted in turn.
  - Unsafe, duplicate, path, format, hash or size errors.
  - A mixed-root source capture.
  - An invalid config despite a valid-looking snapshot.
  - Tampered primary, companion or Index linkage.
  - A dirty or in-repo attestation destination.
  - The fixed canonical-JSON gate roster is not silently extended.
- **Evidence:** existing owners only; primaries before companions. The PR's CI and test record is the evidence where no family is declared. Local and CI proof is not QA, acceptance or OPS01.

## 8. Inherited state

- **F03 / F05 / F07 go to PR07** (PF10 §§2.16–2.18).
  - F07 was gated on PR06's admission; after PR06 it becomes fixable by PR07.
  - **Interaction:** `schemas/reader.v1.schema.json`, `adapter/http_reader.py` and `presenter/reader_v1/emitter.py` become manifest members. Any PR07 fix to F03/F05 will therefore require a re-cut and a new `release_id`. Do not pre-empt PR07's fix here.
- **Carried to PR06:**
  - O-07: sanity transition (§5.4).
  - O-09, O-20, O-21: capture generators and the canonical harness. Regenerate where admitted sources now allow; the choice of capture source/identity may need a Product Owner decision (§9).
  - O-17/CR-06 (§5.5).
  - O-18: narrative pack mount becomes live after admission. Settle it within scope or record it with its owner.
  - O-12: roster not shipped in wheels. Packaging owner/PO; no distribution change unless decided.
- **Carried unchanged:**
  - L-10-type limitation: no current-head security review for PR04 or PR05. Product Owner.
  - O-16 / O-01 token-naming tension: PF01/PF05 maintainers.

## 9. Rescope and owners

"Material" follows PR-10 (091426.1): a change to the Epic-level commitment, meaning outcome, acceptance criteria, a protected boundary, several units' scope, an accepted dependency, or budget/schedule/risk needing PO direction. A planned approach found incomplete is not by itself material.

- **Material findings:** preserve the work, assign a `FINDING_REF` bound to `HDE-EPIC040-PR06`, and route through RS-10 → RS-20 (RS-30 only on `REVISION_REQUIRED`). An `APPROVE` emits exactly one PF10 addendum.
- **Capture-source/identity choices (O-09/O-20/O-21):** these are Product Owner decisions, raised when needed.
- **PF12 or PF01 changes:** these are Canon decisions for their maintainers, never made here.
- **Never:** rewrite the Plan, mint a Proceed, rerun accepted units, merge, or invoke PR-50 (Nathan only).

## 10. Sessions, merge, review, CI

- **Sessions:** PR-20 runs in the dedicated PR06 session. PR-30 and PR-35 each run in their own dedicated session. PR-30 hands off to PR-35 by naming the result path and the PR; there is no second Proceed.
- **Merge:** Nathan's alone.
- **Reviews and CI:** PR-session code review, security review of corrected code, and CI. There is no inherited exception. PR descriptions follow `.github/pull_request_template.md` and `AGENTS.md`.
- **Lineage review:** PR-40 runs after `MERGE_OBSERVED`, or after Nathan's assertion where no such result exists. The reviewer is this same IA, in its read-only role.

## 11. Migration, security, recovery

- **Migration:** no DB or deployment migration; there is no release activation.
- **Security:** synthetic fixtures only in tests; no secrets or birth/Gate payloads in evidence; attestation output only to an external empty directory.
- **Recovery:**
  - Validate temporary outputs before replacing primaries.
  - On convergence failure, claim nothing and hand-edit nothing.
  - Re-run the owners on unchanged inputs. If the source changed, re-cut.
  - Roll back the compatible set together (code, config, schema, generated artifacts, manifest).

## 12. `CANON_CONFLICT_REGISTER`

C040-01…C040-06 are carried unchanged (PR05 instruction §13). Nothing is reopened or newly decided, and PR06 opens no entry by default.

| Entry | PR06 note |
| --- | --- |
| C040-02 | Current controlled PF12 is repository v2.9.5 |
| C040-05 | One core |
| C040-06 | PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |

The O-01 tension remains with the PF01/PF05 maintainers.

## 13. Current truth and provenance

- **State:** `INSTRUCTION_READY`. The PR06 plan is `NOT PRODUCED`. The Proceed is `NOT REQUESTED`. Implementation, PR, CI and merge are `NOT EXECUTED`. QA, Ops, activation and closure are `NOT EXECUTED`.
- **`GCFPE_PROMPT_USES`:** `GCFPE-USE-HDE-EPIC040-PR-10-20260925-PR06-01`
  - Prompt: PR-10 — Create PR Work-Unit Instructions — 091426.1, `https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204` (current body as read 2026-09-24T15:44Z; this invocation did not re-diff it).
  - Release: GCFPE-20260914.1 / 091426.1 / 55.
  - Role: retained IA / PR06 instruction.
  - Captured: 2026-09-25T08:13:25Z.
  - Repository persistence: `PENDING / NON_GATING`.

## 14. Semantic readiness

Compared against:
- Plan §§5.10, 6.6, 7.1–7.4 and 8.
- F01 / PF10 §2.15.
- The PR05 acceptance, including O-17.
- Verified repository facts: 15 vs 44, 29 missing, the cutter gap, lanes.
- The current PR-20 contract.

No decisive comparison failed. The roster-vs-Plan list difference is resolved by the governed roster (§3) and is not a conflict. The obligations outside PR-20's inputs are preserved in §§7, 10 and 11. `INSTRUCTION_READY`: PR-20 can plan PR06 from this instruction plus current repository and Canon evidence. No material boundary was found.
