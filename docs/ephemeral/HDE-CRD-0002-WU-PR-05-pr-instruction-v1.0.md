---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-05-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-05
work_unit_title: "Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation; S19)"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + IA-30 review v1.1 (approved)
applicable_pf10_overlays: PF10 addendum 2.3 (the reviewer chain without the Codex security review; Rule 3 names the S19 review as an unchanged security deliverable that adds no review tooling); addendum 2.7 AD-4 (the four non-public-route gaps are decided once, in S19) and AD-5 (refresh order and restart rules); addendum 2.6 (22-path label roster; step 3b and its restart point); addendum 2.5 (LR-O1 to LR-O3); addendum 2.9 (the WU-PR-04 acceptance, the refresh base 2f18a5eb… and its "Carried into the WU-PR-05 instruction" list, applied in §5.8 and §15); addendum 2.8 (the WU-PR-03 acceptance and its carried items). Addenda 2.2 and 2.4 have no item for this unit beyond the ruby fact (§5.7). Addendum 2.1 governs §19 only
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa3)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b2)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276db) — §6 S19 (threat checklist) and Appendix B (the review input) bind this unit; §5 re-measures them at the current baseline
predecessor_unit_acceptance: WU-PR-01 docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-work-unit-lineage-review-v2.0.md (ACCEPT; addendum 2.4); WU-PR-02 docs/ephemeral/HDE-CRD-0002-WU-PR-02-pr-work-unit-lineage-review-v2.0.md (ACCEPT; addendum 2.5); WU-PR-03 docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-work-unit-lineage-review-v1.0.md (ACCEPT across #643 and #646; blob 7c9a00bd0de2; addendum 2.8); WU-PR-04 docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-work-unit-lineage-review-v1.0.md (ACCEPT on #651; blob d1bf66cf77fd; landed by #652 as dd9ac32; addendum 2.9)
decision_record_read: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md (blob e35ec2cc4858; §3 AD-4, §7 obligations) with its binding text, addendum 2.7
override_contract_read: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-result-v1.0.md (blob 80a40a279291; §6, contract F-2; §9, the refresh that set the current release_id)
structure_precedent: docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-instruction-v1.0.md (blob 51371eeae9d9)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md (v13.6, effective 2026.10.18; blob f6f80d8779e8; 167,152 bytes; sha256 4ecdd9caf9dc172ecb07ab0c577b400ca7a96cc18cef4421448b99dd94fe28aa; Product Owner commit 86e002c, #653). Read for this unit: the complete v13.5.9→v13.6 diff (the version line, one index line and addendum 2.9 appended; nothing else changed), with 2.9 read in full; 2.7 and 2.3 read in full in this invocation; 2.6, 2.5's retained decisions and 2.8 read in full at PR-10 for WU-PR-04 earlier on 2026-10-18 in this session, and byte-unchanged since; 2.1, 2.2 and 2.4 read for applicability
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md §2.3, §2.5, §2.6, §2.7, §2.8, §2.9; §2.1 for §19
pf10_note: the handoff for this invocation named PF10 v13.5.9; the Product Owner's #653 replaced it with v13.6 on main before this instruction was written, so v13.6 is the current controlled PF10 and every reference here is to it
pf10_addendum_created: none (PR-10 is not a qualifying approval prompt)
issuer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a; page state as of 2026-10-12T02:29:33.739Z, re-fetched and unchanged in this invocation; read in full)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-18T16:05:00Z
repository_baseline: origin/main 86e002c3fdb0b1632555c9072bcc3361e81589af (#653). Every non-`docs/` byte equals 5892538 (#651): the two later commits change only docs/ephemeral/ and docs/pfcanon/. Every repository fact in §5 was measured at 86e002c in detached scratch worktrees
receiver: dedicated HDE-CRD-0002 WU-PR-05 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba; page state as of 2026-10-12T02:29:47.327Z, re-fetched and unchanged)
canon_conflict_register: CR-1 to CR-8 carried, all decided; no new entry (§16)
---

# HDE-CRD-0002 WU-PR-05 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-05 of HDE-CRD-0002. The whole-change IA issues it from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit, and perform the review the plan carries, from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

It does not:
- perform the security review, classify any finding or author the detailed plan. Those are the PR session's (ID-2);
- authorize implementation, a commit, a pull request, a merge, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation, and only Nathan merges;
- decide a canon, product or scope question. ID-5 and ID-7 route such items to their owners;
- change canon or create a PF10 addendum.

## 2. Identity and lineage

| Item | Identity |
| :- | :- |
| Change | CRD HDE-CRD-0002 |
| Work unit | WU-PR-05 (Plan v1.1 §7 heading "WU-PR-05 — Code security review of the HDE-EPIC040 PR04 to PR06a code (PR; Distillation)") |
| Requirement | S19 (source 6(b), RA-09) |
| Approved base | Specification v1.1 → Plan v1.1 + review v1.1 (refs above). Review v1.0 and v1.1 carry no note for this unit |
| Overlays | PF10 addenda 2.3, 2.5, 2.6, 2.7 (AD-4, AD-5), 2.8 and 2.9, as named in the header |
| Upstream units | WU-PR-01 to WU-PR-04, all accepted |
| Phase | Distillation |
| Live QA class (Specification table; Plan §6) | "inherits the class of each fixed surface": a confirmed finding fixed here takes the class of the surface its fix changes |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (review v1.1, INITIAL_APPROVE).
- **Unit type.** PR unit.
- **Dependency state: ready.**
  - Plan v1.1 §7: "Fifth; after WU-PR-03 and WU-PR-04 so that fixes are judged against the surfaces' final shape and precede the version bump."
  - WU-PR-03 is accepted (lineage review v1.0; addendum 2.8). WU-PR-04 is accepted (lineage review v1.0 on #651, landed as `dd9ac32`; addendum 2.9). Their surface changes are on `main`.
  - No `HDE-CRD-0002-WU-PR-05-*` file exists on `main`.
  - No QA Guide, QA Plan or Ops receipt is a prerequisite (Plan §9 item 4).
- **Order.** WU-PR-01 → WU-PR-02 → WU-PR-03 → WU-PR-04 → **WU-PR-05** → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7). WU-PR-06 and WU-PR-07 may be prepared in parallel but merge after this unit.
- **Downstream dependents** (contracts in §8):
  - WU-PR-08 cuts `1.4.0` after this unit, from this unit's `release_id` (unchanged unless a fix changes a member);
  - WU-PR-06 reads the classifier rules, including any registration this unit adds;
  - WU-DOC-01 owns the repository documents a fix makes stale;
  - the QA Plan designs the live steps for each fix by its class, and QA-10 reads the S19 record (Plan §9 items 2 and 3);
  - the Product Owner receives every routed finding that needs a canon, product or scope decision.

## 4. Required behavior

**Acceptance intent and constraint**, verbatim from the approved Specification:

| ID | Scope | Acceptance intent |
| :- | :- | :- |
| S19 | "One code security review of what #467, #492, #501 and #508 merged, read on `main`" | "The review is recorded; each confirmed finding is fixed within this CRD or routed to an owner with a reason" |

- **Constraint "Security review."** "S19 findings may enlarge the work; findings in code a later PR already changed are judged against `main`."
- **Exclusions** that bind this unit: "No Reader contract or payload change, and no new public route"; "No canon change beyond S21's ADR-covered close-pack change"; "As implementation work: no deployment, no production configuration change, and no live vendor call made by an implementation work unit"; "No change to the code-review tooling (item 6)".
- **Live QA row.** "Inherits the class of the surface its fix changes | S19 | A confirmed finding fixed within this CRD takes the class above of the surface the fix changes; the Implementation Plan names those fixes."

**Plan v1.1 §7 WU-PR-05 block**, verbatim:
- **Purpose.** "Record one code security review of what #467, #492, #501 and #508 merged, read on `main`, and fix or route each confirmed finding."
- **Bounded scope.** "S19; Audit Appendix B (48 paths) and §6 S19 (threat checklist); fixes inherit their surface's Live QA class."
- **Inputs.** "The 48 files at the reviewed head; PR06b's later changes to four of them (Audit §6 S19); the existing tests as proof of behavior."
- **Deliverables.** "`docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` (scope and head reviewed; checklist; findings table: id, file and line, description, severity, confirmed or not, disposition fixed-here or routed with owner and reason); fixes with regression tests at the paths the findings name (fixed at PR-20 time); `catalog/manifest.json` refreshed at `1.3.0` with convergence only if a fix changes a member."
- **Risks and recovery.** "R-5 (enlargement); a finding that needs architectural change goes to RS-10 or routes to its owner."
- **Nonclaims.** "The review is implementation-side assurance, not QA, not acceptance."

**Audit §6 S19 "Required behavior"**, verbatim: "One recorded review of the 48 current files (plus the tests they rely on for proof), against a stated threat checklist (input bounds and body limits, path and file handling, environment gating and rails, secret and keys-only logging, error disclosure, injection into audit or log lines, concurrency and atomic publication for the evidence writers, dependency and subprocess use), with each finding classified confirmed / not confirmed and each confirmed finding either fixed in this CRD or routed with an owner and reason." Its "Feasibility": "manual review with repository tooling only (no new scanner dependency; Exclusions bullet 6 forbids changing the review tooling, and adding a static analyzer is not needed to meet the acceptance intent)."

**PF10 addendum 2.3 Rule 3**, verbatim in part: every other security obligation is unchanged, including "security deliverables of a work unit, such as the recorded code security review that HDE-CRD-0002 requirement S19 assigns to WU-PR-05, a recorded review that adds no review tooling."

**PF10 addendum 2.7 AD-4**, verbatim in part: "Production exposure of non-public routes is decided once, in the HDE-CRD-0002 security review, not in WU-PR-03." "A correct fix is one factory-level design applied uniformly to every non-public route." "Any gap S19 cannot reach returns to the Product Owner as a separate change candidate."

### 4.1 Threat checklist mapped to canon

The checklist is Audit §6 S19's eight items. Each per-file line (ID-3) applies the items that fit the file. Where canon is silent on an item, the review states the observed behavior and judges the risk; silence is not a finding by itself.

| # | Checklist item | Governing canon on `main` (read for this instruction) |
| :- | :- | :- |
| T1 | Input bounds and body limits | HDE-CLI-API-Vendor-Ref §5.5 "Validation and environment gating" (reject invalid or empty ids before resolution; exact compat namespace); §5.11.3 (sampler body validated by the writer JSON helpers; typed errors); §7.1.11a (the authorization reference's bounds); §7.1.10 "Configured-base boundary" (absolute HTTPS, host, no userinfo, query or fragment) |
| T2 | Path and file handling | HDE Schemas & Artifacts §6.2.1 (the attestation builder refuses a symlinked output root, an output inside the repository, a non-directory or non-empty destination, or an overwrite); HDE Mechanics Guide §27.1 (manifest entries use safe repository-relative POSIX paths, no parent traversal, no unsafe symlink source) and §27.3 (the builder refuses an output inside the repository and leaves the checkout byte-stable); Glow QA Guide §9.2.4, the `EVIDENCE_PATHS_VALIDATED_OK` QA definition (Index and Mirror records reference only safe, in-repository paths); HDE Users Guide §6.1 ("a and b must point to safe, complete mapped chart files under fixtures/charts"; the dev `GET /reader` query parameters, read by `_safe_load_chart`) |
| T3 | Environment gating and rails | HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK`, including "Dev/admin APP_ENV gating" (exactly `{"dev","test","local"}`; missing, empty or other values fail closed without default) and the same rule in §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)"; §3.1 "SAFE rails default ON", "Public traffic (Reader/Aux)", "Admin ops windows (vendor override)"; HDE Architecture §1.3 "Separation of surfaces", §3.2 "A7 proof surface" ("Non-prod entries must be unreachable in production"), §3.3 "Gating & posture" ("Harness is dev-only; never mounted in production") and "Current repository discrepancy", §3.5 "Adopted routes" and "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "Gate" ("must not be mounted in production builds or non-dev deploys"), §5.5, §5.6 transport table, §5.11.2 ("exactly one of `dev`, `test`, or `local`"), §7.1.1 to §7.1.11; HDE Mechanics Guide §22 and §34; Glow Infrastructure §2.4 "Production — Railway" (production `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`) |
| T4 | Secret and keys-only logging | HDE Governance §7.1 "Keys-only logging" and §8.2 "No PII or secrets in logs"; HDE-CLI-API-Vendor-Ref §5.4 "Hygiene and logs" and §7.1.11f exclusions; `AGENTS.md` redaction rule |
| T5 | Error disclosure | HDE-CLI-API-Vendor-Ref §8.1 ("HTTP error envelopes must not echo payloads, secrets, stack traces, or vendor bodies") and §5.2 by reference; HDE Governance §8.1.2 "Typed errors" and §6.3.2 (diagnostics keys-only; no stack traces); HDE Architecture §1.3 "No leakage across boundaries" |
| T6 | Injection into audit or log lines | HDE Governance §7.1.4 "Determinism and formatting" and §8.2.3 "Structured log shape tests"; HDE-CLI-API-Vendor-Ref §7.1.11f (CR/LF and delimiter sanitization) and §3.3 CRLF guards on stdout |
| T7 | Concurrency and atomic publication for the evidence writers | `AGENTS.md` "Evidence harness" (the updater is the sole Index/Mirror writer, one convergent transaction) and "never hand-edit governed artifacts"; HDE Schemas & Artifacts §8.3 "Field order and write discipline (merge-blocking)" and §8.6.1; §6.2.1 and HDE Mechanics Guide §27.3 (attestation). Canon names no general atomic-replace rule for evidence writers; the review states each writer's actual behavior. Runtime concurrency fact: the production command runs `gunicorn` with `--workers 2 --threads 4` (`Procfile`) |
| T8 | Dependency and subprocess use | HDE Mechanics Guide §27.3 (no raw subprocess output retained in attestation content); HDE Schemas & Artifacts §8.11 SBOM (optional); Specification Exclusions bullet 6 and Plan acceptance (3) (no new tooling or dependency) |

### 4.2 Binding IA decisions (canon-conforming readings; HDE Governance §9.1.2)

**ID-1. Review scope and the coverage statement (LR4-O4; OBS-W5-1).**
- **The paths.** Every path Audit Appendix B names: 49 paths measured at `86e002c` (§5.1). Appendix B's prose says 48, but it names 49: three sidecars are written as suffixes ("and its `.path_proof.txt`", "and `.sha256`"). The record gives each of the 49 a per-file line, which satisfies acceptance (1) (OBS-W5-1).
- **The bytes.** Each path is read at its current bytes on the reviewed head (ID-2), including what later commits changed in it: PR06b, the four CI commits of 2026-09-27, and HDE-CRD-0002 WU-PR-01 to WU-PR-04 (§5.2). This is the Specification's "findings in code a later PR already changed are judged against `main`."
- **Context reads.** Tests, callers and callees outside the 49 are read as proof or context: for example `engine/bodygraph/vendor_client.py`, `engine/bodygraph/vendor_audit.py`, `engine/presenter/emitter.py`, `adapter/env_guard.py`, `adapter/logging_filter.py`, `run_flask.py`, `run_flask_dev.sh`, `requirements*.txt` and the `tests/` files. They get no per-file line and no finding of their own.
- **What counts as an S19 finding.** A defect located in, or reached through, code of the 49 paths. Its fix may change files outside the 49 where the correct fix lies there; the plan names each path (Plan: "at the paths the findings name").
- **The override code (LR4-O4), stated precisely.**
  - `engine/bodygraph/resolver.py` and `engine/cli/main.py` are among the 49. Their per-file lines therefore cover the WU-PR-04 override code they contain on `main`: the CLI pre-scan, parser and usage errors; steps 4 to 7 in `_resolve_vendor`; the event calls; the read-only write refusals.
  - `engine/bodygraph/vendor_audit.py` is not among the 49. It was added by #651, an HDE-CRD-0002 unit, not by #467, #492, #501 or #508. It has no per-file line. It is read as context for the resolver's calls. A defect located only in it is an out-of-scope observation (ID-8), not an S19 finding. Its review was WU-PR-04's chain: the Codex code review on #651 and the PR-40 lineage review v1.0.

**ID-2. When the review runs, its head and its record.**
- **PR-20 performs the review.** The dedicated PR-20 session performs the whole review read-only, on the then-current `main`, and writes it into its plan: the 49 per-file lines, the checklist, the findings table with proposed dispositions, the named-input table (ID-6, ID-7) and the out-of-scope observations (ID-8). Basis: Plan v1.1 fixes the fix paths "at PR-20 time", and the Product Owner's Proceed must authorize an exact fix set.
- **Reviewed head.** The plan names the `main` commit it reviewed and the blob ID of each of the 49 paths there. The expected head is the merge of this instruction's pull request, whose code equals `86e002c` and `5892538` (§5).
- **PR-30 writes the record.** PR-30 writes `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` from the plan's review:
  - scope and reviewed head, with the 49 blob IDs;
  - the method and its limits (manual review with repository tooling; no scanner);
  - the checklist (§4.1);
  - the 49 per-file lines;
  - the findings table with the Plan's columns: id, file and line, description, severity, confirmed or not, disposition. A fixed-here disposition names the fix commit and its regression test; a routed one names the owner and the reason;
  - the named-input table and the out-of-scope observations;
  - the PF27 route-policy statement (ID-7);
  - the nonclaims (§12).
- **Head confirmation.** Before writing, PR-30 compares the 49 blob IDs at its base with the reviewed head's. Any changed path has its changed hunks reviewed and recorded. A new confirmed finding there whose fix the plan does not cover is routed, or, if it must be fixed in this CRD, goes to RS-10 with `PR_RETURN_PHASE` (§14).
- **Corrections.** The record is one complete Markdown file. Corrections before the merge amend it in the pull request, and the PR-35 result lists each one. Nothing changes it after the merge; a later correction is a new version.
- **Who reviews the record.** The Codex code review excludes Markdown and `docs/ephemeral/` (`AGENTS.md` "Code review guidelines" and "Code review scope"). The record's independent check is this IA's PR-40 lineage review.

**ID-3. The per-file line.** Each line names: the path; its attribution (§5.1); whether it is a release member; the checklist items that apply; what was read (functions, line ranges, tests relied on); and the result ("no finding", or the finding IDs). A file where an item does not apply says so in one phrase. A sidecar (`.sha256`, `.path_proof.txt`) is reviewed for what it binds and how it is produced.

**ID-4. Classification and severity.**
- **Confirmed** means all of these hold:
  - the defect exists on `main` at the reviewed head;
  - it is shown by the code read together with a reproduction under closed rails (a test, a probe or a traced call path) wherever one can be run;
  - it violates a stated requirement (canon, the Specification, `AGENTS.md`) or gives a realistic exposure path under a checklist item.
- **Not confirmed** lines record what was checked and why the item does not hold. A speculative concern is never recorded as confirmed.
- **Severity.** PR-20 defines one scale (for example high, medium, low, informational) with a one-line criterion per level, records it in the plan and applies it to every finding.
- **Non-security defects** met during the review are recorded as observations with an owner. They are not findings, and they are not fixed here unless they are part of a confirmed finding's fix.

**ID-5. Disposition rule.**
- **Fixed here** only when every condition holds:
  - (a) the fix needs no canon change, no Specification change and no product decision;
  - (b) it changes no public Reader or Aux contract, payload, route, flag or transport (Exclusions bullet 1);
  - (c) it adds no review tooling and no dependency: no package in `requirements*.txt` or `pyproject.toml`, and no scanner or review step in any workflow. A fix to `.github/workflows/ci.yml` or `ci/checks/classify_ci_changes.py`, both among the 49, is allowed when the finding lies there, and runs every lane;
  - (d) every frozen family keeps its bytes (§6);
  - (e) a regression test fails without the fix and passes with it, and the negative control is recorded;
  - (f) the plan names the fix's Live QA class from the Specification's table, by the surface it changes.
- **Routed** with owner and reason when any of (a) to (d) fails, or when the finding lies in a frozen family whose regeneration belongs to its owner. A fix that would impose a policy neither canon nor the Specification states, changing what an operator or client may do, needs a product decision and fails (a); OBS-W4-1 is the example. Engineering hardening that sets no such policy, such as a bound, a sanitization, or an exact comparison canon already requires, needs no product decision. A routed finding names the owner (the Product Owner for canon, product or scope questions; WU-DOC-01, WU-PR-06, WU-PR-08 or the QA Plan where the item is theirs) and the evidence.
- **Rescope.** If PR-20 concludes that a confirmed finding needs a fix in this CRD that crosses a boundary in §14, the PR-20 author raises RS-10 rather than routing the finding or absorbing the fix.
- **Order.** Fixes land in this unit, before WU-PR-08's version bump (Plan R-5).

**ID-6. AD-4's four gaps and their companions (named inputs).** Each gets its own line in the named-input table: canon basis, the evidence in §5.3, classification under ID-4, and disposition under ID-5.
1. **Production mount of the dev-harness routes and the `POST /reader` stub.** `GET`/`HEAD /reader`, `POST /internal/dev/sampler`, the three `GET /dev/*/conjunction` routes and the unprefixed `POST /reader` 405 stub are mounted by `adapter.factory:create_app()`, the production application (`Procfile`). Each refuses at request time under `APP_ENV=prod` (§5.3). Canon: HDE Architecture §3.2 "A7 proof surface", §3.3 "Gating & posture" and its "Current repository discrepancy"; HDE-CLI-API-Vendor-Ref §5.4 "Gate".
2. **The three canon-retired `/ops` routes, mounted and ungated in production.** `/ops/db/unavailable`, `/ops/probe/env` and `/ops/writer/diagnostic`. `/ops/probe/env` answers 200 with the process id, its start time, the `SAFE_MODE`, `ALLOW_NETWORK` and `APP_ENV` values and whether a probe token is present. `/ops/writer/diagnostic` refuses an unauthenticated `POST` (401) and checks its bearer against the `HDE_TEST_TOKEN_ADMIN` and `HDE_TEST_TOKEN_NONE` environment values (`adapter/http_reader.py` lines 191–213). Canon: HDE Architecture §3.5 "Current repository discrepancy" (`RETIRED/NONCANONICAL`); HDE Users Guide §1.1.
3. **`_dev_admin_gate` normalizes.** It trims and case-folds `APP_ENV` (`adapter/http_reader.py` lines 826–832), so `DEV`, ` dev`, `Dev` and `TEST ` pass it (§5.3). Canon: HDE Governance "Dev/admin APP_ENV gating" ("exactly"); HDE-CLI-API-Vendor-Ref §5.11.2 ("exactly one of `dev`, `test`, or `local`").
4. **The after-request hook of `adapter/http_reader.py::create_app` (LR3-O2's wording).** The hook runs on every response, but its two branches never match, because `getattr(resp, "request", None)` is `None` for a Flask response (lines 1223–1232). The `/internal/` ETag strip and the `/ops/writer/diagnostic` Content-Length rule therefore never apply in that factory. It is the dev-runner factory, also used by the A7 proof generator; the production factory has its own hook, which reads `flask.request` and does strip `/internal/` ETags (`adapter/factory.py`). Addendum 2.7 and the decision record say the hook "never fires"; the precise statement is this one.

With them:
- **OBS-P3-3.** `adapter/wsgi.py`'s 405 handler emits no `Allow`. `adapter/wsgi.py` is not the production factory; `scripts/scratch.py` and tests import it. It is an S02-adjacent note: classify it under ID-4 as an observation or a finding.
- **OBS-P3-14.** If `python-dotenv` were installed, `Flask.run` in the canonical runner would read a local `.env` or `.flaskenv`, which could supply `APP_ENV`. It is not in `requirements*.txt` or CI's install; no such file is tracked (§5.5). Addendum 2.7 AD-3 binds the runner's run-call arguments.
- **OBS-P3-17.** The root helpers `run_flask.py` and `run_flask_dev.sh` (documented by `FLASK_AUTO_RUN_GUIDE.md`) run the production factory, which mounts the dev routes, with the interactive debugger and reloader on. HDE Architecture §3.8.1 records that they do not satisfy the dedicated-harness contract. They are not among the 49. The part reached through `adapter/factory.py` is gap 1. The helpers' own settings are an out-of-scope observation (ID-8). A change to them fails classification today (§5.5).

**Constraints on a fix of gap 1 or gap 2, should the review confirm and fix it:**
- **One design.** One factory-level design, applied uniformly to every non-public route in gaps 1 and 2 (AD-4).
- **Canon postures kept.** Routes canon adopts keep their posture: `/internal/version` (ops identity), `/ops/rails/refusal` (the canonical closed-rails refusal probe), the compat namespace (canon requires its production-excluding 404 guard) and the production Reader and Aux routes. `/internal/healthz` and `/internal/readyz` are served only by `adapter/wsgi.py`.
- **Dev use kept.** Dev, test and local use stays intact: the canonical runner `python -m adapter.http_reader`, `scripts/dev_start_reader.sh`, `VERIFY.sh` and the tests (Specification constraint "Dev route"). HDE Architecture §3.8.1 requires the dev harness to "expose the canonically required dev/internal HTTP surfaces for QA", the compat surface included.
- **Canon reading for §3.8.1.** The same section describes the dev server as one "that exposes the same Reader and internal/dev sampler routes as the production adapter". Read with §3.3 ("Harness is dev-only; never mounted in production"), which records the production mount as a discrepancy, and with HDE-CLI-API-Vendor-Ref §5.4 ("must not be mounted in production builds"), the IA reads §3.8.1 as a duty of the dev server. It does not require the production adapter to mount the dev routes. A fix that stops mounting them in production makes that phrase a doc-delta candidate. If PR-20 reads it otherwise, that is a canon question under §14.
- **Exposure, not removal.** Not mounting a route in production is exposure, which AD-4 assigns here. Deleting a canon-retired route's code is not: its removal stays with its canon owner (addendum 2.7 AD-1 "S15 reading"; HDE Architecture §3.5 "No repository removal … is claimed").
- **Proofs stay truthful.** The governed env-gate proof (`artifacts/proofs/endpoints_env_gate_proof.log`: `APP_ENV=prod`, `/reader_success_unreachable=true`) stays truthful and is produced only by its owner. The A7 generator builds `adapter.http_reader.create_app()` once and switches `APP_ENV` per request (`tools/evidence/generate_a7_transport_proofs.py` lines 24 and 107–130), so the plan states what that proof observes under the chosen design.
- **Catalog accounting.** The Endpoint Catalog and the route-enumeration test (`tests/http/test_endpoint_catalog.py::test_every_served_pair_has_one_catalog_row_or_a_reasoned_exclusion`) keep accounting for every served pair (addendum 2.7 AD-1 and AD-6). Any catalog-validator change runs step 3b (§5.8).
- **Live QA class.** Functional-feature: the production application that serves Reader v1 and v2, as for S02 and S10.

**Constraint on a fix of gap 3:** an exact comparison, as AD-2 made for `/reader`. Each gated route gets a refusal matrix covering unset, empty, ` dev`, `dev `, `Dev`, `DEV`, `prod`, `production`, `live` and an arbitrary value, and the three exact values are served.

**ID-7. Vendor-path inputs (OBS-W4-1, OBS-W4-3) and the route-policy statement.**
- **OBS-W4-1.** `hdctl showcompat --source vendor`, including conjunction mode, reaches vendor HTTP under open rails through `_acquire_dry_run` with no production override or audit (§5.4). HDE-CLI-API-Vendor-Ref §7.1.11a scopes the flag to `bg:resolve`, and canon does not decide whether production showcompat or conjunction acquisition must meet a production gate (WU-PR-04 instruction §15). Classify it under ID-4. A fix that gates those commands would create policy canon does not state, so a confirmed OBS-W4-1 is routed to the Product Owner, as owner of HDE-CLI-API-Vendor-Ref, with that reason. It is not fixed here.
- **OBS-W4-3.** `classify_bg_resolve_route_policy` (`engine/bodygraph/vendor_client.py` lines 124–153, outside the 49) maps every non-`v2` base to the legacy `bodygraphs` route. It is reached through `resolver.py::_classify_env_route_policy` (lines 676–694, inside the 49). HDE-CLI-API-Vendor-Ref §7.1.10 requires `PROVIDER_ROUTE_UNSUPPORTED` "before credential projection or any external I/O" for an unversioned, unsupported, nonterminal or ambiguous base, and defines the configured-base boundary. §7.2.0 of the same document records "broad non-v2 legacy selection" as a gap against that contract.
  - Classify it under ID-4. A fix here must implement §7.1.10 exactly and pass ID-5.
  - Such a fix makes three passages stale, which are doc-delta candidates and not edited here: HDE-CLI-API-Vendor-Ref §1 "CLI commands" status line, HDE Users Guide §11.3 and `AGENTS.md` "EPIC036 docs posture". It also contradicts the frozen EPIC036 route-policy captures, whose `--check` already fails on `main` (§5.6).
  - If the fix cannot keep every frozen family byte-unchanged, route the finding to the Product Owner with that reason.
- **PF27 statement.** The plan and the record state the `bg:resolve --source vendor` route-policy posture, as Plan Templates "`bg:resolve --source vendor` route-policy posture" requires: v2 chart-backed for configured `v2` bases, and explicit legacy fallback for every other base, unless a fix changes it, in which case the changed posture is stated.

**ID-8. Out-of-scope observations.** Defects met in files outside the 49 that no S19 finding reaches are recorded in the record's out-of-scope section, with an owner and no fix here:
- **LR4-O1.** `vendor_audit.append_event` creates the sink's parent with `Path.mkdir(mode=0o700, parents=True)`; intermediate directories get the default mode. The sink directory (`0700`) and file (`0600`) stay owner-only. Owner: this IA, which routes it at the WU-PR-05 PR-40 review (to the Product Owner as a later change candidate unless a planned unit takes it).
- **OBS-P3-17**, the root helpers' debugger and reloader settings: the Product Owner.
- anything else of this kind the review meets.

**ID-9. Release identity and the refresh.**
- **If no fix changes a member,** no refresh happens and `release_id` stays `2f18a5eb…`.
- **If a fix changes a member,** this unit performs one same-version refresh at `1.3.0` / `2026-08-24T18:04:49Z` through the cutter and converges the evidence, exactly as §5.8 states.
- **A fix to a non-member evidence owner** (for example `tools/evidence/generate_a7_transport_proofs.py`) regenerates its outputs through that owner and publishes them through the updater, in the §5.8 order from step 3b.

**ID-10. Tests and the test environment.**
- **Regression tests.** Each fix has a regression test at the path the plan names, with a negative control (ID-5 (e)). New test modules must be reached by a lane or by full validation without a `ci.yml` change (the WU-PR-01 coverage guard, `test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target`).
- **Hazards.**
  - **OBS-P4-7:** `tests/adapter/test_jsonschema.py` leaks `ENGINE_ENV` and `ENGINE_SERVICE_TOKEN` into `os.environ` for the rest of the pytest process. A new test that sets `APP_ENV` and reaches the vendor gate removes the ambient `ENGINE_ENV` with `monkeypatch`.
  - **OBS-P4-5:** the attestation's isolated child environment has no `APP_ENV`. A new open-rails vendor-path test that a rails job or a sanity-run test executes sets `APP_ENV` itself.
  - **OBS-P4-2:** six route-policy tests depend on an ambient `APP_ENV`; run sweeps with the closed-rails profile, which sets it.
  - **The EPIC030 generator (OBS-W5-3, §5.6):** `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` parses no arguments. Any invocation, including `--help`, rewrites three tracked EPIC030 logs. Never run it in the repository tree.
- **No skips.** No test is skipped, deselected, marked expected-failure or quarantined.

**ID-11. Classification consequences.** A fix's lanes follow the classifier (§5.5).
- **Unclassified paths.** A change to `run_flask.py` or `run_flask_dev.sh` fails classification (`CI_CHANGE_SURFACE_UNCLASSIFIED`). Such a change belongs to an out-of-scope observation, not to this unit.
- **New paths.** A new path under an unregistered prefix needs the smallest registration that classifies it, with an owner test. A change to `ci/checks/classify_ci_changes.py` is a full-validation path: all seven lanes run. Every registry pin in `tests/evidence/test_rails_ci_workflow_integration.py` stays true.
- **A record-only pull request** selects no lane and starts no CI run, because `docs/ephemeral/**` is in the workflow's skip list (S05). Acceptance (4) is then met by no applicable lane, and PR-35 records the absent run as that fact, not as a failure.

## 5. Current repository and reference baseline (measured at `86e002c`)

### 5.1 The 49 review paths

Union of the non-`docs/`, non-`tests/`, non-`audit/`, non-`artifacts/`, non-`goldens/`, non-`narratives/`, non-`fixtures/` paths of `cd6f9e6` (#467, 2026-09-22), `4d7ab9d` (#492, 2026-09-25), `f7484d0` (#501, 2026-09-26) and `d79cfc1` (#508, 2026-09-26). All 49 exist on `main`; none was deleted. 17 are release members, the 17 that Audit §7.3 lists. "Later changes" are commits after `d79cfc1` that touched the path. "Lanes" are `_lanes_for_path` at `86e002c`.

| # | Path | Merged by | Member | Later changes | Lanes | Blob at `86e002c` |
| :- | :- | :- | :- | :- | :- | :- |
| 1 | `.github/workflows/ci.yml` | #467 | no | 398276b, 735af8a, WU-PR-01 #627 | all seven | `3836bad11c39` |
| 2 | `adapter/factory.py` | #508 | no | WU-PR-03 #643 | compat, product, release | `618a624dc4d4` |
| 3 | `adapter/http_reader.py` | #467, #508 | yes | WU-PR-03 #643, #646 | compat, db, product, release | `a26feb9b48f4` |
| 4 | `adapter/schemas/error_v1.schema.json` | #501 | yes | — | compat, product, release | `720aa6738466` |
| 5 | `adapter/wsgi.py` | #508 | no | — | compat, product, release | `52fd4aedf1a9` |
| 6 | `catalog/manifest.json` | #467, #501, #508 | no (the identity source) | PR06b #513, WU-PR-03 #643, #646, WU-PR-04 #651 | release | `80364154c776` |
| 7 | `ci/checks/classify_ci_changes.py` | all four | no | e1bff8d, 398276b, 2876fa0, 735af8a, WU-PR-01 #627, WU-PR-03 #643, WU-PR-04 #651 | all seven | `3be620cbac91` |
| 8 | `ci/checks/run_rails_job_definitions.py` | #467 | no | — | rails, release | `ce25809df3e7` |
| 9 | `ci/jobs/rails_open_conformance.yml` | #467 | no | — | rails, release | `b1d3f056b3e4` |
| 10 | `engine/bodygraph/ingest.py` | #467 | no | — | db, product, release | `68fb7b4a7d0a` |
| 11 | `engine/bodygraph/mapped_cache.py` | #467 | yes | — | db, product, release | `8741137ba14a` |
| 12 | `engine/bodygraph/projection.py` | #467 | yes | — | product, release | `e28c47d8ee02` |
| 13 | `engine/bodygraph/resolver.py` | #467 | yes | WU-PR-04 #651 | product, release | `c3550c066094` |
| 14 | `engine/bodygraph/v2_adapter.py` | #467 | yes | — | product, release | `447243305d5e` |
| 15 | `engine/cli/main.py` | #467 | yes | WU-PR-03 #643, WU-PR-04 #651 | compat, product, release | `7761834a6100` |
| 16 | `engine/compat/compute.py` | #467 | yes | — | compat, product, release | `77e311800838` |
| 17 | `engine/compat/error_tokens.py` | #467 | yes | — | compat, product, release | `32f013d484e6` |
| 18 | `engine/config/__init__.py` | #467 | no | — | product, release | `aef7a0206c09` |
| 19 | `engine/config/registry_loader.py` | #508 | yes | PR06b #513 | product, release | `d7e9496d96d0` |
| 20 | `engine/emit_public.py` | #467 | no | WU-PR-03 #643 | product, release | `4fdcd8d94517` |
| 21 | `engine/http/compat_handler.py` | #467 | yes | — | compat, product, release | `42d0e7f9bfc6` |
| 22 | `engine/runtime/public.py` | #467, #508 | yes | — | product, release | `df33eab7d8f4` |
| 23 | `errors/token_map/token_map.json` | #467, #501 | yes | — | compat, product, release | `7a5b2df0125f` |
| 24 | `errors/token_map/token_map.json.path_proof.txt` | #467, #501 | no | — | evidence | `30822f401b73` |
| 25 | `presenter/reader_v1/emitter.py` | #508 | yes | — | compat, product, release | `4a9f1bacbd72` |
| 26 | `schemas/reader.v1.schema.json` | #501, #508 | yes | PR06b #513 | compat, product, release | `a91843f13c20` |
| 27 | `schemas/reader.v1.schema.json.sha256` | #501, #508 | no | PR06b #513 | compat, product, release | `e8ef6ca434c2` |
| 28 | `schemas/reader.v2.schema.json` | #508 | yes | — | compat, product, release | `7803e9a63009` |
| 29 | `schemas/reader.v2.schema.json.sha256` | #508 | no | — | compat, product, release | `0a39e26325c2` |
| 30 | `scripts/cut_release_manifest.py` | #501 | no | — | product, release | `f87ef35c396d` |
| 31 | `scripts/make_reader_v1_goldens.py` | #508 | no | PR06b #513 | product, release | `9bb05d6dc503` |
| 32 | `scripts/make_release_pack.sh` | #508 | no | — | product, release | `6ea1acf4ffc1` |
| 33 | `tools/bodygraph/check_magic10_gate_readiness.py` | #492 | yes | — | db, product, release | `50fbc78f77e0` |
| 34 | `tools/cli/generate_cli_conformance_artifacts.py` | #467 | no | — | evidence, release | `54db49d57b0a` |
| 35 | `tools/cli/generate_showcompat_artifacts.py` | #467 | no | — | evidence, release | `9ef2f0b818e9` |
| 36 | `tools/config/artifacts.py` | #492, #501 | no | — | evidence, release | `c8b702fefaee` |
| 37 | `tools/config/generate_config_artifacts.py` | #492, #501 | no | — | evidence, release | `402c60206398` |
| 38 | `tools/errors/generate_error_artifacts.py` | #501 | no | — | compat, release | `ea1e1110578e` |
| 39 | `tools/evidence/build_release_attestation.py` | #467 | no | WU-PR-02 #634 | evidence, release | `edcdd517aa87` |
| 40 | `tools/evidence/generate_a7_transport_proofs.py` | #467, #508 | no | WU-PR-03 #643, #646 | evidence, release | `b5f71b9c704d` |
| 41 | `tools/evidence/generate_conjunction_writer_evidence.py` | #508 | no | — | evidence | `ad8d812ed29d` |
| 42 | `tools/evidence/generate_determinism_gate_proofs.py` | #467 | no | — | evidence, release | `31df358af63a` |
| 43 | `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` | #467 | no | — | evidence | `c2d199883a9e` |
| 44 | `tools/evidence/generate_hde_epic037_v2_to_compat.py` | #467 | no | — | evidence | `b76746a132fa` |
| 45 | `tools/evidence/generate_open_rails_abba_proof.py` | #467, #501, #508 | no | PR06b #513, WU-PR-03 #643, #646, WU-PR-04 #651 | evidence, release | `d5097d28e679` |
| 46 | `tools/evidence/regenerate_identity_closure.py` | #467 | no | WU-PR-02 #634 | evidence, release | `c1a06abee562` |
| 47 | `tools/evidence/run_canonical_json_gate.py` | #467, #501 | no | — | evidence, release | `652029563561` |
| 48 | `tools/evidence/run_sanity_pipeline.py` | #467 | no | — | evidence, release | `853566a0e4f7` |
| 49 | `tools/evidence/run_sanity_pipeline_gate.py` | #467 | no | — | evidence, release | `62fbf8f87b1f` |

### 5.2 Change history since the four merges (OBS-W5-2)

Audit §6 S19 says that after the four merges "only PR06b (`8999bd0`, #513) changed any of them" and names four files. Measured at `86e002c`:
- PR06b changed six of the 49: the four named plus `catalog/manifest.json` and `schemas/reader.v1.schema.json.sha256`.
- Four commits of 2026-09-27 changed `.github/workflows/ci.yml` and `ci/checks/classify_ci_changes.py` before the Audit's baseline `982071b`: `e1bff8d`, `398276b`, `2876fa0` and `735af8a`.
- HDE-CRD-0002 units changed 12 of the 49 since: rows 1, 2, 3, 6, 7, 13, 15, 20, 39, 40, 45 and 46 of §5.1.

Because the review reads current bytes (ID-1), none of this changes its scope. The record carries the corrected attribution.

### 5.3 The production application and non-public route exposure (AD-4 evidence)

- **Production entry.** `Procfile`: `gunicorn 'adapter.factory:create_app()' --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30`.
- **Served set.** `adapter.factory.create_app()` under `APP_ENV=prod` serves 15 rules and 50 `(method, path)` pairs, including Flask's `/static` rule. The three factories together serve 56 pairs, which is 53 without `/static`, the count addendum 2.7 AD-1 uses. The Endpoint Catalog holds 18 records; `success_endpoints` is `GET /reader` only.
- **Probe on the production factory** (Flask test client; `APP_ENV=prod`; closed rails; no network, database or vendor):

  | Request | Status | Body or note |
  | :- | :- | :- |
  | `GET /reader?v=1`, `HEAD /reader?v=1` | 403, `no-store` | `ERR_READER_FORBIDDEN` (HEAD bodiless) |
  | `POST /reader` | 405, `Allow: GET, HEAD` | `ERR_NOT_FOUND` |
  | `POST /internal/dev/sampler` | 403 | `ERR_WRITER_FORBIDDEN` |
  | `GET /dev/sampler/conjunction`, `/dev/reader/conjunction`, `/dev/writer/conjunction` | 403 | `ERR_WRITER_FORBIDDEN` |
  | `GET /ops/probe/env` | 200, `no-store` | `pid`, `started_at_utc`, `rails_state` (`SAFE_MODE`, `ALLOW_NETWORK`, `APP_ENV` values), `probe_token_present` |
  | `GET /ops/db/unavailable` | 503 | `ERR_WRITER_RAILS_CLOSED` with `details.adapter_code` |
  | `GET /ops/rails/refusal` | 503 | `ERR_WRITER_RAILS_CLOSED` |
  | `POST /ops/writer/diagnostic` (no bearer) | 401 | `ERR_WRITER_UNAUTHORIZED` |
  | `GET /internal/version` | 200 | identity fields |

- **Gate comparison.** With `APP_ENV` set to `DEV`, ` dev`, `Dev`, `test`, `local` or `TEST `, `POST /internal/dev/sampler` passed the gate (the next check answered 415); `GET /reader` passed only for exactly `dev`.
- **Hooks.**
  - `adapter/http_reader.py::create_app`'s hook: lines 1223–1232.
  - The production factory's hook: `adapter/factory.py` `_strip_etag_on_internal`.
  - The dev runner `__main__` binds `127.0.0.1` with debug, debugger and reloader off (addendum 2.7 AD-3).
- **`adapter/wsgi.py`.**
  - It is not named by the `Procfile`. It mounts the same blueprints plus `/internal/healthz` and `/internal/readyz`.
  - Its 405 handler sets no `Allow` (OBS-P3-3).
  - Its header helper reads `APP_ENV`, else `ENGINE_ENV`, else `dev`, only to decide the HSTS header.
- **Governed proofs.** `artifacts/proofs/endpoints_env_gate_proof.log` reads `APP_ENV=prod`, `/reader_success_unreachable=true`, `cache_control=no-store`, `etag_absent=true`. Its owner is `tools/evidence/generate_a7_transport_proofs.py`, which imports `adapter.http_reader.create_app` (line 24).

### 5.4 Vendor path loci (OBS-W4-1, OBS-W4-3)

- **`engine/bodygraph/resolver.py`:** `resolve_bodygraph` line 151; `_resolve_vendor` line 217, with the WU-PR-04 gate and event calls through line 381; `_resolve_vendor_route` line 383; `_resolve_vendor_v2_chart` line 490; `_vendor_config_env` line 660; `_classify_env_route_policy` lines 676–694; `_acquire_dry_run` line 905; `resolve_compat_chart` line 1073.
- **`engine/cli/main.py`:** showcompat vendor acquisition at lines 752–753 and 798 (`source_policy="vendor"`).
- **Public HTTP call sites all pass `source_policy="local"`:** `adapter/http_reader.py` lines 528–529 and 637–638; `engine/http/compat_handler.py` lines 105 and 164–165.
- **`engine/bodygraph/vendor_client.py::classify_bg_resolve_route_policy`:** lines 124–153.

### 5.5 Classification and environment facts

- **Lanes.** `docs/ephemeral/**` selects no lane and is in `.github/workflows/ci.yml`'s skip list for both `pull_request` and `push`. Full-validation paths: `.gitignore`, `ci/checks/classify_ci_changes.py`, `pyproject.toml`, `pytest.ini`, `requirements-dev.txt`, `requirements.txt`, `tests/evidence/test_rails_ci_workflow_integration.py`.
- **Paths outside the 49.**
  - `engine/bodygraph/vendor_client.py`: product, rails and release.
  - `engine/bodygraph/vendor_audit.py`: product and release.
  - `tests/http/test_endpoint_catalog.py`: product, compat and release.
  - `run_flask.py` and `run_flask_dev.sh`: `CI_CHANGE_SURFACE_UNCLASSIFIED`.
- **`python-dotenv`.** Absent from the CI-equivalent environment (CPython 3.12.3 with CI's install) and from `requirements*.txt`. No `.env` or `.flaskenv` is tracked.
- **`ruby`.** `tests/evidence/test_hdapi_v2_contract_inventory.py` needs `ruby` on `PATH` (addendum 2.2). It is present on the hosted runner with its version unprinted (O-6), and at `/usr/local/bin/ruby` in the cloud container used here.

### 5.6 Checks run at the baseline (closed rails; detached worktrees of `86e002c`)

Environment: CPython 3.12.3 with CI's install, closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`), with `DATABASE_URL`, `GEO_API_KEY`, `HD_API_KEY`, `HDAPI_BASE_URL`, `HD_API_BASE_URL`, `HDAPI_KEY`, `HD_GEOCODE_KEY`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH` and `ENGINE_ENV` unset, and `XDG_STATE_HOME` pointed at an empty scratch directory.

| Check | Result |
| :- | :- |
| Admission | `2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76`, 45 members, `1.3.0` |
| `release_id_recompute.py --check-manifest-only`; `update_evidence_index.py --check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `check_lf_endings.py`; `ci/checks/check_final_lf.sh`; `refresh_step_logs_manifest.py --check`; `run_canonical_json_gate.py --check-only` | 10 × exit 0 |
| `--check` of `generate_a7_transport_proofs.py`, `generate_v2_mapped_cache_evidence.py`, `generate_bodygraph_policy_proofs.py`, `generate_error_artifacts.py`, `generate_conjunction_writer_evidence.py`, `generate_determinism_gate_proofs.py`, `generate_open_rails_abba_proof.py` | 7 × exit 0 |
| Frozen families: `--check` of `generate_showcompat_artifacts.py`, `generate_cli_conformance_artifacts.py`, `generate_rails_gate_evidence.py`, `generate_env_matrix_snapshot.py`; `ci/checks/check_cli_help.sh` | 5 × exit 0 |
| `generate_config_artifacts.py --check`; `--compare-goldens .` with `--report` outside the tree; `cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission --check` | 3 × exit 0 |
| Sanity pipeline (`run_sanity_pipeline.py --log-path` outside the tree) | `summary:PASS`, `first_failed_stage:NONE` (58 s) |
| Attestation build into an external empty directory with `--require-clean`, then `--verify` | exit 0 and exit 0; `release_admission` `PR06R_B_FINAL_PASS`, `validation_result` `PASS`, `source_commit_exact` true (167 s) |
| **Pre-existing failures (not caused by HDE-CRD-0002):** `generate_hde_epic037_v2_to_compat.py --check` (one of the 49) | exit 1, `STALE_HDE_EPIC037_PR04_V2_TO_COMPAT` naming four `artifacts/vendor/hdapi_v2/` files. Same result at `982071b` and at `d79cfc1` (OBS-W5-4) |
| `generate_hde_epic037_bg_resolve.py --check`, `generate_hde_epic036_bg_resolve_route_policy.py --check` | exit 1 each (OBS-P4-3; pre-existing) |
| Full `tests/` sweep | SWEEP_RESULT_PENDING |

Every worktree ended with an empty `git status --short --untracked-files=all`, after restoring one scratch worktree from the EPIC030 run below.

**OBS-W5-3 (hazard, measured).** `generate_epic030_pr05_category_framework_evidence.py --help` ran the generator in write mode, because it parses no arguments. It rewrote `audit/qa/hde-epic030/pr-05/{category_canonical_compare.log,category_framework_binding.log,per_channel_mechanics.json}` in the scratch worktree: a new `produced_at_utc`, and a category order that begins `harmony, heat` where the tracked file begins `heat, harmony`. The scratch worktree was restored. The tool is among the 49, so the review reads it under T7 and T8.

### 5.7 Prompt and environment facts for the PR session

- The PR-20 and PR-10 pages are unchanged since the page states named in the header.
- The installed TypeSafe skill carries request v8.2 (`request-v8.2.json`, sha256 `62486fcc…`).
- Run times measured here: a full `tests/` sweep about 28 minutes in this lineage; the sanity pipeline 58 s; an attestation build 167 s.

### 5.8 Release identity and the refresh (only if a fix changes a member)

- **Manifest.** `catalog/manifest.json`: `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`, 45 members, `release_id 2f18a5ebbf1908ae1425ec546677d6618746f27c2e1ddc9e5087a81b0aaceb76` (sha256 of the file at `86e002c`; equal to WU-PR-04 result v1.0 §9 and addendum 2.9's refresh base). `FROZEN_OPEN_ABBA_SHA256` is `9949ddf5fe7e5d329a6d9a49bea916a9ff369ba6dd058de18b7cf7df9556098f`.
- **Members among the 49:** the 17 marked in §5.1. A fix to any of them forces the refresh. Admission's roster stays at 45.
- **The refresh.** A same-version cut at `1.3.0` / `2026-08-24T18:04:49Z` through the cutter with `--roster-from-admission`, then convergence in the order WU-PR-04 result v1.0 §9 executed: Plan v1.1 §10 with step 3b after admission.
  - A member change after the cut restarts at step 2; an evidence-primary change restarts at step 3b (addenda 2.6 and 2.7 AD-5).
  - Steps 3b to 10 must be byte-stable on a second pass.
  - Step 3b runs the A7 owner: it is required whenever the catalog validator or the A7 generator changes, and harmless otherwise.
- **Labels** (addenda 2.5 and 2.6):
  - **LR-O3 (a).** The updater refuses `CURRENT_RELEASE_LABEL_MANIFEST_INVALID` between the member edits and the cut. Do not run it there.
  - **LR-O3 (b).** Roster captures take the new label at the first updater run after their owner regenerates them.
  - **LR-O3 (c).** A roster capture left byte-stable keeps its earlier label. That is a finding to the IA, never a roster edit. The roster holds 22 paths; the engine-core purity report stays unlabelled.
  - **LR-O1.** The label is not proof that an owner ran.
- **Footprint now.** 620 Mirror rows; 27 carry `2f18a5eb…`. Outside `docs/`, `.audit_src/` and `handoff/`, 10 tracked files contain `2f18a5eb`.
- **Expected changed set.** Modelled on WU-PR-04's 54 paths: the manifest, `FROZEN_OPEN_ABBA_SHA256`, the release-binding primaries and their path proofs, the Index and the Mirror, plus whatever the fix itself regenerates.
- **Stale-binding sweep (step 11).** Search for `2f18a5eb` and `9949ddf5` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256` and `manifest_post.sha256`.

## 6. Bounded files and components

Plan v1.1 §7 WU-PR-05 "Deliverables" approves the loci: the record, "fixes with regression tests at the paths the findings name (fixed at PR-20 time)", and the manifest only if a member changes. This instruction bounds them as follows:

| Path | Bound |
| :- | :- |
| `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` | the record (ID-2) |
| Each path a confirmed, fixed-here finding names | only the fix the plan states for that finding (ID-5). When the review confirms gap 1 or 2, the expected loci are `adapter/factory.py` and possibly `adapter/http_reader.py` (member); for gap 3, `adapter/http_reader.py` (member) |
| `tests/**` at the paths the plan names | the regression tests and negative controls of ID-10; the environment setup of existing tests only where a fix forces it, without removing or weakening an assertion |
| Evidence owners a fix touches (for example `tools/evidence/generate_a7_transport_proofs.py`) and the families they regenerate; the Index and Mirror through the updater | only as the fix and §5.8 require |
| `ci/checks/classify_ci_changes.py`; `tests/evidence/test_rails_ci_workflow_integration.py` | the smallest registration a new path needs (ID-11), or the fix of a finding located in the classifier (ID-5 (c)) |
| `catalog/manifest.json` | the refresh, by the cutter only, only if a member changes |
| `docs/server/reader_v1.md`, `docs/CLI_commands.md` | one sentence each, only if a fix changes the behavior they state |
| `docs/ephemeral/` PR result records | evidence obligations (§10) |

Expected unchanged, so that a needed change is a finding under §14:
- `requirements*.txt`, `pyproject.toml`, `pytest.ini`; `.github/workflows/ci.yml` except a fix of a finding located in it (ID-5 (c));
- `engine/bodygraph/vendor_audit.py` (ID-8);
- `run_flask.py`, `run_flask_dev.sh`, `FLASK_AUTO_RUN_GUIDE.md` (ID-8);
- `engine/config/registry_loader.py`'s admission constants (WU-PR-08);
- `tools/evidence/update_evidence_index.py` (WU-PR-07);
- every frozen family: `artifacts/vendor/**`, `artifacts/cli/**`, `artifacts/architecture/**`, `audit/ops/**`, `audit/qa/hde-epic0*/**` and the EPIC022 release evidence.

## 7. Exclusions

- **Surfaces and contracts.** No Reader or Aux contract, payload, route, flag or transport change; no new public route (Specification Exclusions bullet 1). Not mounting a non-public route in production is not a public change.
- **Review tooling.** No scanner or analyzer is run, installed or added, and no dependency is added (Exclusions bullet 6; acceptance (3)). The review uses the repository's own tests and tools, `git`, `grep` and the Python standard library.
- **Live and production.** No live vendor, production or database call; closed rails throughout, except monkeypatched open-rails unit tests with fake clients. No real credentials. No production configuration change. No deployment.
- **Release.** No version bump and no admission-constant change (WU-PR-08 owns `1.4.0`).
- **Canon.** No canon edit; no PF10 addendum; no new `schemas/` file; no new evidence family or acceptance token.
- **Policy not in canon.** No production gate on `hdctl showcompat` or conjunction acquisition (ID-7). No deletion of a canon-retired route's code (ID-6).
- **Documents.** No `AGENTS.md`, `README.md`, `CHANGELOG.md` or `.env.example` edit (WU-DOC-01 and WU-PR-08).
- **Tests.** No skipped, disabled, expected-failure or quarantined test. No write-mode run of a frozen-family generator, the EPIC030 generator or the EPIC036/EPIC037 generators in the repository tree.

## 8. Interface contracts with other units

| Contract | Consumer | Content |
| :- | :- | :- |
| F-1 Release base | WU-PR-08 | `release_id` after this unit: `2f18a5eb…` unchanged, or the refreshed value if a fix changed a member. The result record names it |
| F-2 The S19 record | QA-10 readiness (Plan §9 item 2); the QA Plan (Plan §9 item 3) | the record path; each fix with its Live QA class and the surface it changes; each routed finding with its owner |
| F-3 Route exposure | QA Plan; WU-PR-08 (S17 statements); WU-DOC-01 | if gap 1 or 2 is fixed: which routes the production application serves, how the dev, test and local runners still serve the dev routes, and how the env-gate proof reads |
| F-4 Routed findings | Product Owner and the named owners | finding ID, evidence, owner, reason, and the decision needed |
| F-5 Classifier registrations | WU-PR-06 | any registration this unit adds |

## 9. Disposition rules PR-20 must apply and record

1. **The review.** Perform it as ID-1 to ID-8 state. Record the reviewed head, the 49 blob IDs, the per-file lines, the findings, the named-input table and the out-of-scope observations in the plan.
2. **Choices left to PR-20,** each recorded with its reason:
   - the severity scale (ID-4);
   - each disposition (ID-5);
   - each fix's design and its regression test;
   - for gaps 1 and 2, if fixed, the factory-level design and how it keeps dev, test and local use and the proofs truthful (ID-6).
3. **Prototype.** Prototype each fix in a throwaway copy. Run the full `tests/` sweep and the §5.6 checks there, and record every affected test, tool or governed output.
4. **Refresh.** If a member changes, follow §5.8 exactly. Record every step, both passes' results, the byte-stability digest and the stale-binding sweep.
5. **Stale documents.** Name each document or canon passage a fix makes stale but this unit may not change, with its owner.
6. **Route-policy statement.** State the PF27 posture (ID-7).
7. **No fix, or record only.** If no finding is fixed here, the plan says so. Its implementation is then the record alone, and §10's lane reading for a record-only pull request applies.

## 10. Acceptance, tests and evidence

**Plan v1.1 §7 WU-PR-05 acceptance, verbatim**, with the binding readings in brackets:
1. "The record covers all 48 paths with a per-file review line, even when no finding." [Every path Appendix B names: 49 measured (ID-1; OBS-W5-1). Each line has the content ID-3 lists.]
2. "Every confirmed finding has a merged fix with a regression test, or a routing line with owner and reason." [The fix's regression test fails without it, shown by a negative control. A routing line names the owner, the reason and the evidence (ID-5).]
3. "No new review tooling or dependency is added (Exclusions bullet 6)." [No scanner run or added; no package added to `requirements*.txt` or `pyproject.toml`; no scanner or review step added to any workflow.]
4. "Lanes green; if a member changed, admission and convergence as WU-PR-03 (7)." [CI on the exact head with every selected lane green and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. A record-only pull request starts no run (ID-11), recorded as that fact. If a member changed, WU-PR-03 (7) reads: "Admission at the PR head reports `1.3.0`, 45 members and the refreshed `release_id`; every convergence step byte-stable on a second run; `release_id_recompute.py --check-manifest-only` exits 0; all lanes green."]

**Evidence obligations**, verbatim from the Plan: "The review record is the deliverable; the PR result record names it." The result record also names:
- each check actually run, with counts;
- the reviewed head and the head confirmation (ID-2);
- each fix, its test and its negative control;
- each routed finding and its owner;
- the `release_id` after the unit, and every regenerated family if a refresh ran;
- the stale-document list (§9.5);
- the nonclaims (§12).

**Validation PR-20 plans** (minimum). Every item below ran at the baseline in its read-only form (§5.3, §5.6). Two kinds did not: the negative controls, which need a fix to exist, and the write steps of the convergence, which run only after a member change:
- the full `tests/` sweep in a detached worktree with `ruby`, `bash` and `curl` on `PATH`, under the closed-rails profile, with `XDG_STATE_HOME` pointed at an empty scratch directory;
- the 25 read-only checks and the sanity pipeline of §5.6, after the fixes;
- if a member changed: the convergence checks of Plan v1.1 §10 steps 4 to 10, and the attestation build and verify into an external empty directory with `--require-clean`;
- a negative control for each fix;
- for gaps 1 to 3, if fixed: the probe of §5.3 repeated, showing the new behavior on the production factory and unchanged dev, test and local behavior on the canonical runner.

Do not list as passing validations the three pre-existing failures of §5.6 (EPIC036 and the two EPIC037 tools). Never run the EPIC030 generator in the repository tree (OBS-W5-3).

Each run that can write tracked files runs in a detached worktree and ends with `git diff --exit-code` and an empty untracked status.

| Requirement | Acceptance item | Proof | Stage |
| :- | :- | :- | :- |
| S19 review recorded | (1) | the record's 49 per-file lines; ID-2 head and blobs | PR-20 (review); PR-30 (record); PR-40 |
| S19 findings dispositioned | (2) | fixes with regression tests and negative controls; routing lines | PR-30; CI |
| Exclusion 6 | (3) | the diff | PR-30; PR-35 |
| Lanes and release identity | (4) | CI on the exact head; admission and convergence if a member changed | PR-30; PR-35 |
| Fixed surfaces live | — | the QA Plan's steps by class (F-2) | QA, not this unit |

## 11. Migration and security constraints

- **Migration:** none (no data or schema change).
- **Rollback:** Nathan's revert of the squash commit, followed by a same-version manifest refresh if the unit changed a member (Plan §7 common paragraph).
- **Security:**
  - Fixes only narrow exposure: no rail opens, no write path opens, and no surface gains vendor or database access.
  - No secret, token, key value, birth input, location or user identifier appears in a test, a record, a log or a commit. Probes of `/ops/probe/env` and similar routes run under closed rails, and their captured bodies are recorded with the rails values as observed.
  - A finding's record states the exposure in keys-only terms; it carries no exploit payload beyond what reproduces the defect under closed rails.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session):
  - reads this instruction and its lineage, the 49 files and their context (ID-1), and canon on `main`;
  - performs the review (ID-2) and writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/`: the review, the fixes with their tests, the requirement-to-change/test map, ordered steps including any refresh, risks and recovery;
  - returns `AWAITING_PO_PROCEED` only for a complete plan within this scope.
- **PR-30** (after Nathan's Proceed for that exact plan):
  - recovers existing work first;
  - confirms the head (ID-2);
  - implements only the planned fixes;
  - writes the record;
  - converges evidence by owners only;
  - tests locally under §10;
  - commits coherently;
  - publishes `PR_CANDIDATE_PUBLISHED`;
  - hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session):
  - retrieves and resolves the Codex code review findings on the code (PF10 addendum 2.3: the Codex security review is not part of the chain; the Codex code review excludes Markdown and `docs/ephemeral/`);
  - retests, and pushes coherent corrections. Any member change re-runs the refresh from step 2; an evidence-primary change from step 3b;
  - verifies current-head CI (every selected lane, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and mergeability, or records that a record-only head starts no run;
  - returns `MERGE_PENDING` without merging.
- **PR description:** the `.github/pull_request_template.md` headings with the `AGENTS.md` content rules. A record-only pull request states "Merging preserves the record and approves nothing (D21-C)".
- **Merge:** Nathan merges manually. No agent merges, enables auto-merge, enqueues or schedules a merge.
- **PR-40:** after the merge is observed or asserted, this IA reviews the landed lineage, including the record against ID-1 to ID-8, and on ACCEPT selects the next unit (WU-PR-06).
- **Attributable lineage:** the PR result records, the S19 record, the PR reference and the squash commit.
- **Nonclaims** every record keeps:
  - the review is implementation-side assurance, not QA and not acceptance (Plan);
  - no live run of any fixed surface;
  - no QA verdict, acceptance, Ops, deployment, PF09 movement or closure;
  - no conformance claim beyond the fixes made;
  - no canon edit; routed items are not decided by this unit.

## 13. Recovery

- **Interruption:** resume in the same dedicated phase session from its last saved artifact. Inspect existing worktrees, branches, PRs and `docs/ephemeral/` before creating anything.
- **A failed or interrupted refresh** restarts at step 2 for a member change and at step 3b for an evidence-primary change.
- **An ordinary defect in this instruction** returns to this IA through PR-10. A corrected instruction is a new version, never an edit of v1.0.
- **Abort** is only Nathan's manual PR-50 instruction.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent; a protected architecture, security, data-model or external-contract boundary; several units' scope; an accepted dependency; or budget, schedule or risk needing Product Owner direction.
- **Before Proceed:** the PR-20 author owns any rescope proposal (RS-10 optional support; RS-30 for revisions), and this IA reviews it through RS-20. The decision returns to the PR-20 planning context.
- **After Proceed:** PR-30 or PR-35 records `PR_RETURN_PHASE`.
- **Specification issue:** `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- **Expected triggers:**
  - a confirmed finding whose needed fix fails ID-5 (a) to (d) and that the PR-20 author believes must still be fixed in this CRD;
  - a change needed in an "expected unchanged" path of §6;
  - a frozen-family output that a fix cannot leave byte-identical;
  - a reading of ID-1 to ID-11 that PR-20 believes conflicts with canon;
  - a new finding at PR-30's head confirmation that must be fixed in this CRD (ID-2).

  Routing a finding with owner and reason is an S19 outcome, not a rescope.

## 15. Unresolved items, carried observations and owners

| Item | Owner | State |
| :- | :- | :- |
| The review itself, its findings and dispositions | PR-20 session (review); PR-30 (record) | In the plan |
| The PR-20 choices of §9.2 | PR-20 session | In the plan |
| AD-4's four gaps; OBS-P3-3, OBS-P3-14, OBS-P3-17; LR3-O2's wording | this unit (ID-6) | Carried here, as addenda 2.7, 2.8 and 2.9 direct |
| OBS-W4-1, OBS-W4-3 | this unit (ID-7); Product Owner for any canon or policy decision | Carried here |
| LR4-O4 | this instruction (ID-1) | Settled |
| LR4-O1 | IA, as an out-of-scope observation (ID-8) | Carried |
| OBS-P4-5, OBS-P4-7 (and OBS-P4-2) | this unit as test-environment hazards (ID-10); the leak's fix stays with a later owner through the IA | Carried |
| OBS-17: intermittent hosted failure of `tests/qa/test_generate_epic_close_pack.py` | QA tool and test owner, through the IA; Product Owner to route | If the qa lane runs, a failure of that test is recorded as OBS-17, never "fixed" here |
| O-6: hosted `ruby` version unprinted | IA | PR-35 records it if a job log shows it |
| LR-O1, LR-O3 | this unit, only if a refresh runs (§5.8) | Conditional |
| LR-O2 (run every updater consumer on an updater change) | IA | Not triggered: the updater does not change. A refresh rewrites the Index and Mirror, and the full sweep runs every consumer |
| **OBS-W5-1** (new). Audit Appendix B says "48 paths" and names 49 | IA (recorded; ID-1 reads it) | Recorded |
| **OBS-W5-2** (new). Audit §6 S19's "only PR06b … changed any of them" omits two PR06b files and four CI commits (§5.2) | IA (recorded; no scope effect) | Recorded |
| **OBS-W5-3** (new). The EPIC030 generator writes on any invocation, and its output differs from the tracked files (§5.6) | this unit's review (T7, T8); Product Owner for the frozen family | Recorded; a hazard here |
| **OBS-W5-4** (new). `generate_hde_epic037_v2_to_compat.py --check` fails on `main`, as it did at `982071b` and `d79cfc1` | this unit's review (the file is among the 49); Product Owner for refreshing or retiring the EPIC037 captures, as for OBS-P4-3 | Pre-existing; recorded |
| OBS-W4-2, OBS-W4-4; OBS-P4-3, OBS-P4-4 | Product Owner | Carried, unchanged |
| OBS-P4-1 (classifier gap for the override tests) | WU-PR-06 or a later classifier unit | Carried |
| WU-PR-08: the loopback bind statements and OBS-P4-5 | the WU-PR-08 instruction | Not this unit |
| WU-DOC-01: the start command and bind, OBS-P3-12, LR3-O4, and the repository documents of WU-PR-04 plan v1.0 §17 (`README.md`, `AGENTS.md`, runbooks such as `docs/RUN.md` lines 65–66) | the WU-DOC-01 instruction | Not this unit |
| LR3-O1, LR3-O5 | Product Owner; IA | Not this unit |
| AQ-1 | Product Owner | WU-PR-07 only |
| Doc-delta candidates a fix creates | Product Owner (canon); WU-DOC-01 (repository docs) | Named in the plan and the record (§9.5) |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict:
- AD-4's gaps are gaps between canon and the repository, which canon itself records ("Current repository discrepancy" in HDE Architecture §3.3 and §3.5). They are not conflicts between canon passages.
- HDE Architecture §3.8.1's description of a dev server "that exposes the same Reader and internal/dev sampler routes as the production adapter" is read with §3.3 and HDE-CLI-API-Vendor-Ref §5.4 as a duty of the dev server (ID-6, "Canon reading for §3.8.1"). The more specific production-mount rules govern exposure, so no decision between the passages is needed.
- For OBS-W4-3, HDE-CLI-API-Vendor-Ref owns vendor route selection: §7.1.10 is its normative contract, and its own §7.2.0 records "broad non-v2 legacy selection" as a gap. HDE Mechanics Guide §1.1 ("Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback only as a legacy route-family posture"), HDE Users Guide §11.3 and `AGENTS.md` describe the current posture. Under the technical ownership PR-10 states (HDE-CLI-API-Vendor-Ref owns CLI/API/vendor), §7.1.10 governs. A fix would make the other passages stale doc-delta candidates; no decision between them is needed.
- For OBS-W4-1, canon is silent (ID-7). Silence is routed to the owner; it is not a conflict.

Coverage read for this instruction (in this invocation unless stated):
- the eight checklist items' canon of §4.1. Each section was read in full, except three that were read in full earlier on 2026-10-18 in this session and are byte-unchanged since: HDE Governance §3.1 and HDE Mechanics Guide §22 (PR-10 for WU-PR-04), and HDE Mechanics Guide §34 (the WU-PR-03 lineage review). HDE Schemas & Artifacts §8.6.1 was read through its "Discipline" rules, not its exact-source binding list;
- HDE Architecture §3.8.1 in full; HDE Users Guide §1.1 "Checked-in retired/noncanonical route drift" table and §6.1;
- HDE-CLI-API-Vendor-Ref §5.4, §5.5, §5.6 transport table, §5.11 (all subsections), §7.1.10, §7.1.11 preamble, §7.2.0, §8.1 and §8.2 opening, and the §1 "CLI commands" status line;
- HDE Governance §2.0.10 (`ENV_RAILS_POLICY_OK` and "Dev/admin APP_ENV gating"), §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)", §6.3.2, §7.1, §8 (§8.1 to §8.3);
- HDE Architecture §1.3, §3.2 to §3.5;
- Glow Infrastructure §2.4;
- HDE Mechanics Guide §1.1 (route-family bullets), §27.1 and §27.3 passages;
- HDE Schemas & Artifacts §6.2.1, §8.3 "Field order and write discipline", §8.6.1, §8.11;
- Plan Templates "Contract and Compatibility Posture (MUST)", including the route-policy posture bullet;
- HDE Users Guide §11.3;
- whole-canon searches for body limits, path traversal and symlinks, subprocess and dependency pinning, log injection and sanitization, atomic writes, error disclosure, dev/admin gating and the non-v2 route-policy statements.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Unit | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S19 "One code security review … read on `main`" | one review of the four merges' code at its current bytes | ID-1 (49 paths, current bytes, context reads); ID-2 (PR-20 reviews; PR-30 records) | WU-PR-05 | (1) | PR-20; PR-30; PR-40 |
| S19 "each confirmed finding is fixed within this CRD or routed to an owner with a reason" | no confirmed finding left without an owner | ID-4 (criteria), ID-5 (disposition rule), ID-6 and ID-7 (named inputs) | WU-PR-05 | (2) | PR-30; CI |
| Constraint "findings in code a later PR already changed are judged against `main`" | current bytes govern | ID-1; §5.2 | WU-PR-05 | (1) | PR-20 |
| Exclusion 6 / Plan acceptance (3) / addendum 2.3 Rule 3 | a recorded manual review; no new tooling | §7 "Review tooling"; ID-5 (c) | WU-PR-05 | (3) | PR-30; PR-35 |
| Live QA row "inherits the class" | each fix carries its class to the QA Plan | ID-5 (f); F-2 | WU-PR-05 / QA | — | PR-20; QA |
| Plan "manifest refreshed … only if a fix changes a member" | refresh is conditional | ID-9; §5.8 | WU-PR-05 | (4) | PR-30; PR-35 |
| Addendum 2.7 AD-4 | the four gaps decided once, here, with one factory-level design | ID-6 with its fix constraints | WU-PR-05 | (2) | PR-20; PR-30 |
| Addendum 2.9 carried list | every carried item placed | §15 rows; ID-1 (LR4-O4), ID-7, ID-8, ID-10 | WU-PR-05 | — | PR-10 (here) |

Checks against the full PR-20 contract:
- Its sole substantive input is `PR_INSTRUCTION_ID`.
- This instruction carries everything PR-20 needs:
  - the Specification, Audit, Plan and review lineage;
  - the PF10 path and overlays;
  - the baseline, loci, exclusions, interfaces and dependencies;
  - acceptance, evidence, migration and security;
  - recovery, rescope, merge ownership and the return owner.
- PR-20's step 2 forbids mutating the repository while planning. The review it performs is read-only, its prototypes run in throwaway copies, and its only writes are its own artifacts.
- Numeric domains: the path count is 49, with the Appendix's "48" read under ID-1. Severity is an ordinal scale PR-20 defines, with no numeric score required. No boolean field is introduced.
- No decisive comparison fails. Every fact in §5 was measured at `86e002c` by this IA, and every check §10 lists ran at the baseline, with the three pre-existing failures named (lesson LR4-O3).

## 18. Return owner and next step

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in a new dedicated top-level WU-PR-05 PR engineering session that Nathan creates. It returns `AWAITING_PO_PROCEED`.
- **Return to the IA:**
  - PR-40 lineage review after Nathan's merge;
  - rescope review through RS-20;
  - same-owner correction of this instruction through PR-10.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-05)

Action sent (v8.2): "Write, in a new dedicated session, the first detailed PR implementation plan for one work unit of an approved change, in which the planner itself performs a one-time recorded code security review of 49 source and configuration files that four earlier pull requests merged, read on current main against an eight-item threat checklist mapped to canon, with a per-file review line for each file and a findings table, and classifies about ten named inputs (four exposure gaps on non-public HTTP routes, two vendor-path observations and related notes). It then plans, for each confirmed finding, a fix with a regression test or a routing line with an owner, possibly including one factory-level change to how non-public routes are mounted in production, and, only if a fix changes a release member, a same-version release re-cut with a fixed twelve-step governed-evidence convergence; a ready instruction lists the files, inputs and rules, prototypes run in a throwaway copy, no live provider call occurs, and a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 3.20 (confidence 0.67); rung probabilities low 0.00, medium 0.00, high 0.14, extra high 0.51, max 0.35, ultracode 0.00. Model probabilities Fable 5.1 0.34, Opus 5.5 0.66, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 0.55). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.048, Fable 5.1 at extra high 0.173, Fable 5.1 at max 0.119, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.000, Opus 5.5 at high 0.092, Opus 5.5 at extra high 0.337, Opus 5.5 at max 0.231, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between max and extra high. Sent 2026-10-18T15:33:43Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-18T15:33:43Z; HTTP 200 in 0.58 s; 5550 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between max and extra high.
- **Which request.** The installed TypeSafe scoring skill's request v8.2 (`request-v8.2.json`, sha256 `62486fcc4357e5917c3e9ba3e1ba9e2709364f0338dde70d4a88b116022b22ec`) and `score_v8.py`, run once, before this record was saved.
- **Records.** The Notion row was not written, as PR-10 directs. Nathan's pick for PR-20 is not stated. Nathan's pick for this PR-10 session is not stated; its reading is WU-PR-04 lineage review v1.0 §11.

**Surface advice:** run PR-20 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Environment.**
  - The review's probes, the prototypes and the sweep need Python 3.12 with CI's install (package-index access for `pip install -r requirements-dev.txt`).
  - They also need `ruby` on `PATH` for the contract-inventory test (present at `/usr/local/bin/ruby` in the cloud container used for this instruction), plus `bash` and `curl`.
  - Run under closed rails with the vendor, database and GitHub keys unset; the container sets several of them.
  - Use a clone with history back to `cd6f9e6` (a shallow clone lacks the four merge commits; `git fetch --deepen=400 origin main` reached them here).
- **Run times observed.** A full `tests/` sweep about 28 minutes; the sanity pipeline about one minute; an attestation build about three minutes.
- **Access.** No live vendor, production or database access is needed. HTTP probes use the Flask test client.
- **Order.** This instruction's pull request should be merged first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-05 / PR-10 / instruction 1 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-05 (S19) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (page state as of 2026-10-12T02:29:33.739Z) |
| role/stage | continuing whole-change IA / PR-10 |
| capture time | 2026-10-18T16:05:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | WU-PR-04 lineage review v1.0 §12 (PR-40) and the earlier uses it names |
| repository persistence | recorded here only (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `86e002c`.

| Topic | Sources and sections |
| :- | :- |
| Instruction authority, content and readiness | PR-10 — Create PR Work-Unit Instructions — 100926.1 (read in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1 ("Execute", "Required result"; the receiver contract); HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 (PR Instructions are the IA's; Proceed per detailed PR plan; PR merges remain Product Owner actions) and §9.1.2 (canon precedence over in-flight documents; ID-1 to ID-11 rest on it) |
| Overlays and carried items | PF10-HDE-Build-Notes v13.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.6.md`): addendum 2.9 (in full: "Approval and source record", the findings table with LR4-O1 to LR4-O4, "Epic, task, and status effects" with the list carried into this instruction, "Deferred obligations", "Scope boundaries and nonclaims"); 2.7 (in full: AD-4 and its "Why they are decided there", AD-5, AD-1's "S15 reading", AD-6, "Unresolved obligations and owners"); 2.3 (in full: Rules 1–5, the passages read under the rule); 2.6 (step 3b, the 22-path roster); 2.5 (LR-O1 to LR-O3, OBS-17, O-6); 2.8 (the carried items); 2.2 (the `ruby` requirement); 2.1 (§19); 2.4 read for applicability |
| S19 threat checklist (§4.1) | HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.4 "Route and gate (must)" and "Hygiene and logs (dev)", §5.5 "Validation and environment gating", §5.6 transport table, §5.11.1 to §5.11.6, §7.1.10 "Normative route selection" and "Configured-base boundary", §7.1.11 preamble and §7.1.11a and §7.1.11f, §7.2.0, §8.1 ("No other fields"), §3.3 CRLF guards, §1 "CLI commands" status line. HDE Governance §2.0.10 `ENV_RAILS_POLICY_OK` ("Dev/admin APP_ENV gating"), §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)", §3.1, §6.3.2, §7.1.1 to §7.1.5, §8.1.2 "Typed errors", §8.2.1 to §8.2.4, §8.3. HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §1.3 "Separation of surfaces" and "No leakage across boundaries", §3.2 "A7 proof surface", §3.3 "Gating & posture" and "Current repository discrepancy", §3.4, §3.5 "Adopted routes" and "Current repository discrepancy", §3.8.1 in full (the dev server and dev-harness bullets; its "Current repository discrepancy" on the root helpers, OBS-P3-17). Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §2.4 "Production — Railway". HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §1.1 (route-family bullets), §22, §27.1, §27.3, §34. HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §6.2.1, §8.3 "Field order and write discipline (merge-blocking)", §8.6.1, §8.11. HDE Users Guide (`docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md`) §1.1 "Checked-in retired/noncanonical route drift (unsupported)", §6.1, §11.3. Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §9.2.4, the `EVIDENCE_PATHS_VALIDATED_OK` QA definition. HDE Governance §3.1, HDE Mechanics Guide §22 and §34 were read in full earlier on 2026-10-18 in this session; `docs/pfcanon/PF04-…`, `PF14-…`, `PF02-…` and `PF05-…` are unchanged since 2026-10-09 |
| Plans and route-policy statements | Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "Contract and Compatibility Posture (MUST)": "`bg:resolve --source vendor` route-policy posture" |
| Release refresh (conditional) | Implementation Plan v1.1 §10; Audit §5.1 and §7.3; WU-PR-04 result v1.0 §9; `AGENTS.md` "Release identity" and "HDE-EPIC040 admission addition"; WU-PR-02 lineage review v1.0 §7 (LR-O1 to LR-O3) |
| In-flight documents | Specification v1.1: row S19, constraints "Security review", "Dev route", "Release members", Exclusions, the Live QA class table, routed decision RD-1; Plan v1.1 §3, §4, §6, §7 (common paragraph; WU-PR-05 block; WU-PR-03 acceptance (7)), §9 items 2 to 4, §10, §11 (R-5), §12, §14; review v1.1 (no note for this unit); Audit §3, §6 S19, §7.3, §7.6 R-5, Appendix B; corrective decisions record §3 and §7; WU-PR-03 lineage review v1.0 §7–§8 and the OBS-P3 tables of WU-PR-03 result v1.0 §9 and plan v2.0 §18; WU-PR-04 instruction v1.0 (structure; §5.3, §14, §15), plan v1.0 §17 (OBS-P4-1 to OBS-P4-7, F-13), result v1.0 §6 and §9, lineage review v1.0 §5, §7, §8 |
| Operative documentation | `AGENTS.md` (canon-first rule; closed rails and redaction; "Code review guidelines" and "Code review scope" (Markdown and `docs/ephemeral/` outside the Codex code review); sole Index/Mirror writer; no hand edits; pytest readiness; PR descriptions; "EPIC036 docs posture" (OBS-W4-3); "Truncation/retrieval-failure guardrail" (exit codes captured from the producer)) |
