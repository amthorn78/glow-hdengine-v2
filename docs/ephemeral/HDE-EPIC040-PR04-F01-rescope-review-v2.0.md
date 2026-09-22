---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW
artifact_version: "2.0"
predecessor_version: "1.0"
predecessor_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md
artifact_state: RESCOPE_REVIEW_COMPLETE
decision: APPROVE
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
reviewed_artifact: HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1
reviewed_artifact_path: docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md
reviewed_artifact_sha256: 6bef3daf72eb4b547f43fa9efb49a548f68e97bbb8113c27f7ba13c4dec3756b
reviewer: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: the continuing Isis-50 reviewer session that decided REVISION_REQUIRED on 2026-09-22T06:48:06Z and Implementation Plan Review v2.1 on 2026-09-09T13:36:43Z
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-20 (GCF-17.RESCOPE), second decision
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decision_time_utc: 2026-09-22T07:27:55Z
addendum_created: docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md
---

# HDE-EPIC040-PR04-F01 — Bounded Work-Unit Rescope Review v2.0

## 1. Decision

**`APPROVE`.**

Redlines R-1 through R-7 are each applied exactly once, verified against the repository rather than against the companion report's account. The R-2 derivation method is sound, and its result is **empirically confirmed**: this reviewer applied a PR04-shaped change and executed all three chains, and every failure fell inside either the approved enumeration or loci PR04 already owns.

One addendum is created: `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`.

**The approved set is nine production and CI-configuration files plus four test homes**, not the proposal's eight plus four. This review admits `tools/evidence/run_canonical_json_gate.py` (§4.1), settling item B's first half in the affirmative as the proposal invited.

**Two things this review found that the proposal did not, both recorded rather than folded in:**

1. **A correction (§4.3).** Exclusion X-11's stated reason is false. `tests/runtime/test_identity.py` is *not* "independent of the gate outcome" — it fails under a PR04-shaped change. Its exclusion nevertheless stands, on the correct ground that PR04's plan §6.2 already carries it as a necessary dependent.
2. **A separate boundary, not bundled into F01 (§5).** `adapter/http_reader.py` is both a PR04 owned locus and one of the fifteen committed `catalog/manifest.json` members, so PR04's required §6.5 change breaks `tests/evidence/test_release_manifest_content_binding.py` in the release lane, while PR04 may not refresh the manifest. This is the same class as `HDE-EPIC040-PR02-F03`, whose overlay at PF10 §2.10 is scoped "For HDE-EPIC040-PR02 only". It is **outside F01** by the proposal's own §6.3 definition and is routed as its own finding, not absorbed here.

**What this decision does not supply.** No implementation authority, no Product Owner Proceed, no merge permission, no PF09 movement, no QA verdict, no acceptance, no closure, no PF10 edit, no PF10 number allocation, no claim of canonical adoption.

## 2. Identity and baseline, re-verified

### 2.1 Baseline

`main` has advanced past the head the handoff and the proposal recorded. The finding and the enumeration are unaffected.

| Fact | Proposal v1.1 / handoff | This review |
| --- | --- | --- |
| `main` head | `332fa4c6b2c1ea65a52bee4fd40c227d2d49f4fc` | **`0f47079f24834424c4a4cfaba6a8d44d94286ad2`**, tree `0865ef1814d238910b7da1e935d04124980aba34`, committed 2026-09-22T08:19:44+01:00 |
| Storage PR #463 | open, unmerged | **merged** — v1.1 and its companion are on `main`, read from there |
| Non-documentation drift from `6ecacafb…` | empty | **still empty**; no commit since `332fa4c` touches any non-`docs/` path |
| Executable baseline | accepted PR03 state `9cda1b49…` | unchanged |
| PR04 vehicle state | none | **none** — no branch, commit, pull request, Proceed, implementation, review, CI run or merge |
| Working tree | clean | clean before and after every observation |

### 2.2 Artifact identity

Every SHA-256 recomputed at `0f47079` from `main`.

| Artifact | Path | SHA-256 | Result |
| --- | --- | --- | --- |
| Reviewed proposal v1.1 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.1.md` | `6bef3daf72eb4b547f43fa9efb49a548f68e97bbb8113c27f7ba13c4dec3756b` | **matches**; 368 lines / 53,606 bytes; read complete |
| Companion application report | `docs/ephemeral/HDE-EPIC040-PR04-F01-rs30-redline-application-report-v1.0.md` | `f0cda5a600e32c68da5989cabc025deaccbe673fadadc7c71a6bc371d3f8f7b9` | **matches**; 84 lines / 12,114 bytes; read complete |
| Predecessor proposal v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` | `51eae27c2013722a3aebf22ca073587ad4d83c105176df87e970c37bc9f46bf6` | **matches** — preserved unchanged, not overwritten |
| This reviewer's v1.0 decision | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` | `37fd5d594981c84ec61669c75e2721eb38be698074691f750af17064e2117311` | matches the bytes this session pushed |

**Current controlled PF10**, resolved read-only from `docs/pfcanon/` and completely read: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, recomputed `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f` — **matches**; 1,649 lines / 181,316 bytes; unique PF10 Markdown in that directory. No Google Doc, `.doc`, `.docx`, export, archive result or search hit was opened, compared or cited. Applicable overlays were read at their repository paths; **§2.8** (PF10-FORM-001), **§2.10** (PR02-F03, load-bearing for §5), **§2.12** and **§2.13** were read in full.

## 3. Redline verification — repository, not report

Each item checked against the cited code and the revised text.

| Item | Applied? | What this reviewer verified independently |
| --- | --- | --- |
| **R-1** | **Yes, exactly once** | `run_sanity_pipeline_gate.py` appears as §6.2 row 5 with its own justification, in the §4.3 release chain, in §4.4's corrected closing sentence, in §6.4's cost cell and at §10 E-15/E-16. Chain re-read: `build_release_attestation.py:669` invokes the wrapper; `_expected_log()` / `_valid_log()` require byte equality; `run_sanity_pipeline.py::_render_log` collapses status to `"OK"`/`"FAIL"` and the summary to `"PASS"`/`"FAIL"` — **no third token exists**. |
| **R-2** | **Yes, exactly once** | New §6.3 carries a three-clause definition, a five-step procedure, an explicit stopping condition, eleven exclusions with reasons, and a stated honest limit. Tested in §4 below rather than accepted. |
| **R-3** | **Yes, exactly once** | §6.1 bullet 2 flags the correction explicitly and §10 E-13 is rewritten. Re-read: `pipeline_stop` is `{"type": "null"}`; `validation_result` and `release_admission` are `const`. |
| **R-4** | **Yes, exactly once** | §7's Dependencies row carries the five-step proof and attributes the classifier execution to RS-20; §11 R-03 is marked answered. |
| **R-5** | **Yes, exactly once** | §6.4's cost cell records the nil CI-surface cost and attributes the classifier execution to RS-20 rather than re-claiming it; §10 E-23. |
| **R-6** | **Yes, exactly once** | §5 bullet 1 carries the three-row criterion table — gate semantics and acceptance versus coherence registration and frozen-byte validation — names `run_canonical_json_gate.py` as the boundary case, and cross-references X-8. The criterion is testable as written, which is what the redline asked for. |
| **R-7** | **Yes, exactly once** | §6.2's "Ownership bound on file 6" and §7's Downstream row. Bound to two things: the distinct non-admitted code on the existing failure-receipt path, and the withholding already performed. Consistent with Plan §4.2 and §6.6. |

No item is applied twice, none is silently omitted, and no resolution is fabricated. The companion report's §2 map is accurate in every row this reviewer checked.

## 4. Testing the derivation method

R-2 existed because completeness had to become a testable claim. This reviewer tested it by execution, not by reading: a PR04-shaped change was applied in an isolated `git worktree` under the session scratchpad — `engine/runtime/public.py` banding through the admission owner instead of `ts_v0`, and `adapter/http_reader.py` implementing the instruction §6.5 Reader `POST` success path at its existing declared route — and all three chains were run against it. The worktree was removed and pruned; the repository is clean at `0f47079` and no governed artifact was written.

### 4.1 Results by chain

| Chain | Run | Failures | Disposition |
| --- | --- | --- | --- |
| **Rails** | `run_rails_job_definitions.py` over all three job files; then `pytest tests/evidence/test_rails_ci_workflow_integration.py` | 18 in `tests/evidence/test_open_rails_abba_proof.py`; 1 in `tests/evidence/test_rails_ci_workflow_integration.py` (`test_open_rails_producer_check_mode_has_no_repo_residue`, on `INCOMPLETE_RELEASE_ROSTER`) | Both are **files 10 and 11 of the enumeration**. `tests/bodygraph/test_vendor_client.py` passed, confirming X-3. |
| **Release** | `pytest tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` | 2 failed, 50 passed | `test_identity.py` → **X-11 reason false, disposition right** (§4.3). `test_release_manifest_content_binding.py` → **separate boundary** (§5). `test_release_attestation.py` **fully green** → X-10 confirmed. |
| **Full validation (40 tests)** | the complete `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` roster | 14 failed, 1,207 passed, across five files | `tests/transport/test_a7_transport_proofs.py` is **file 12**. `tests/cli/test_showcompat_sources.py` is named in instruction §7.2. `tests/cli/test_cli_file_inputs.py` and `tests/cli/test_cli_install_help.py` are CLI homes under §7.2. `tests/qa/test_cli_admin_dumps.py` and `tests/qa/test_cli_admin_parity.py` are registered `engine/cli/main.py` owners in PR04 plan §6.5. **Nothing outside the enumeration and outside PR04's authority failed.** |

The proposal's §6.3 disposes of the 40-member roster by category rather than row by row, which was the one place its claim could have been thin. **It is empirically correct**, and that is now on the record rather than inferred.

### 4.2 Item B, first half — X-8 admitted

`tools/evidence/run_canonical_json_gate.py` **is admitted to the enumerated set**, bounded to the overlay's single purpose. The proposal invited this and the evidence supports it:

- X-8 records the file as reached through **sanity stage 03**. That understates its reachability. `generate_open_rails_abba_proof.py::canonical_gate()` (`:440–442`) runs `run_canonical_json_gate.py --check-only` as a subprocess, and `canonical_gate_success` (`:501`) is a predicate of `top_level_pass` (`:521`). The file's result is therefore a **direct input to file 1's gate** — the rails-lane gate at the centre of this finding. `generate_determinism_gate_proofs.py::canonical_gate_result()` invokes it the same way.
- Under the simulation, `run_canonical_json_gate.py --check-only` returns **rc=1**.
- The §6.2.1 principle the author already accepted for file 3 applies identically and more strongly here: leaving it unnamed risks a second rescope for the same finding, which is exactly what the first `REVISION_REQUIRED` existed to prevent.
- Admitting it costs nothing measurable: it selects no additional CI lane (§6.4's R-5 finding), and the purpose clause bounds what may be done to it as tightly as to every other file.

The admission **does not disturb** the file's existing treatment as a PR04 plan §6.2 necessary dependent. The plan's coherence change — dropping removed imports and validating against `_FROZEN_GENERATED_SHA256` — remains the plan's and is unchanged. The overlay adds only the permission to express the non-admitted outcome in this file if implementation finds it must live there. Both treatments are stated in the addendum so the dual role is visible rather than ambiguous.

### 4.3 Item B, second half — X-10 upheld; X-11's reason corrected

**X-10 is upheld, on execution.** `tests/evidence/test_release_attestation.py` passed entirely under the simulation. `test_v1_schema_preserves_the_pf12_wire_contract` (`:388`) pins the `PR06R_B_FINAL_PASS` const, which binding condition 4 forbids changing, so it stays green and confirms the boundary holds. `test_failure_receipt_is_strict_and_secret_safe` (`:302`) constructs its **own** `AttestationBuildError("isolated_stage_failed", …)` at `:303–307` and asserts that code at `:314`, so it pins receipt *shape* and not the production code value. `test_declared_output_roster_is_exact_owned_and_stable` (`:264`) pins roster sizes that this delta does not change. The exclusion is correct.

**X-11 carries a false reason.** The row reads "`tests/runtime/test_identity.py`, `tests/evidence/test_release_manifest_content_binding.py` — Runtime identity and manifest content binding. **Independent of the gate outcome.**" Both fail under the simulation, so neither is independent.

- For `tests/runtime/test_identity.py` the **disposition is right for a different reason**: PR04 plan §6.2 already carries it as a necessary dependent ("`emit_reader_public_envelope` signature — update call sites; identity assertions unchanged"), so stopping condition (ii) excludes it. The addendum records the corrected ground.
- For `tests/evidence/test_release_manifest_content_binding.py` the disposition is also right **for F01**, because the test fails clause (b) of the §6.3 definition — it would fail with a fully admitted release too — but the reason conceals a separate boundary, which §5 records and routes.

Neither correction changes the approved delta. Both are recorded because an exclusion table is only as good as its reasons, and R-01's precedent bound rests on it.

### 4.4 Item A — file 3 upheld, with one omission recorded

Naming `tools/evidence/generate_determinism_gate_proofs.py` (§6.2.1) is **correct**, and the reasoning is sound: the caller-side alternative would duplicate admission logic the builder's own failure already carries, and an unnamed file forces a second rescope. This reviewer verified the file independently:

- It imports `emit_reader_public_envelope` and calls it in `runtime_bytes()` — a live Reader path.
- `cli_bytes()` runs a real CLI subprocess, `python -m engine.cli showcompat --a-file … --b-file … --dump-reader …`, and raises on a non-zero return code or any stderr. The proposal calls this an "`hdctl` subprocess"; it is the same CLI entrypoint invoked as a module rather than through `scripts/hdctl.py`. Immaterial to the finding.
- **Output omission.** The proposal lists five written artifacts. The file declares **six**: `audit/gates/parity/reader_cli/{ab,ba,summary}.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256` **and `artifacts/cards/a3/IDENTITY_OK.txt`**. The sixth is recorded in the addendum's regeneration obligation. This is an incompleteness in the file's *description*, not in the file set.

The contrast drawn with file 1 is correct: the rails lane invokes file 1 directly, so no caller-side alternative exists there.

## 5. A separate boundary, found and routed — not bundled into F01

`adapter/http_reader.py` is simultaneously:

- a PR04 **owned locus** (instruction §7.1, Plan §6.4), which instruction §6.5 **requires** PR04 to change in order to implement the contracted Reader `POST` success path; and
- one of the **fifteen committed members of `catalog/manifest.json`** — verified by reading the manifest's `files` array, where it is the first entry.

`tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` (`:88–94`) asserts that every committed manifest entry's `sha256` and `size` equal the repository bytes. It runs in the **release lane** (`.github/workflows/ci.yml:251`), inside the detached worktree at the candidate head. Under the simulation it **fails on a hash mismatch**. Meanwhile PR04's plan §6.6 lists `catalog/**`, "including `catalog/manifest.json`", as explicitly unchanged, and instruction §9 excludes release promotion, manifest expansion and activation.

**This class is known and has precedent.** PF10 §2.10 — `HDE-EPIC040-PR02-F03`, "Existing Serializer Manifest Binding Refresh" — approved exactly this remedy when PR02 changed `engine/serializer/canon.py`, another manifest member: a single existing-row rebind through the canonical manifest writer, the roster held at fifteen, release identity recomputed from the actual bytes, and the evidence convergence that follows. That overlay is scoped **"For HDE-EPIC040-PR02 only"**, and its item 8 reserves complete member refresh and final identity recomputation to PR06. **It does not extend to PR04.**

**It is not F01 and is not absorbed here.** By the proposal's own §6.3 definition it fails clause (b): the failure is a byte-binding mismatch, independent of admission state, and it would occur with a fully admitted release. F01 is about gates that cannot express a truthful non-admitted outcome. Folding a second, differently-caused boundary into this overlay would break exactly the bound that makes the overlay safe.

**Routing.** This is recorded as **`HDE-EPIC040-PR04-F02` — manifest binding refresh for `adapter/http_reader.py`**, a candidate finding for the PR04 session to raise through `RS-10` in the ordinary way, on the PF10 §2.10 precedent. Nothing here decides it, scopes it, or pre-approves a remedy; this review has no proposal before it on that question. It is treated exactly as the proposal treats U-02 and decision D-03: named, evidenced, and left with its owner. It does **not** gate F01, whose delta is complete on its own terms, and the two can proceed independently.

## 6. Evidence against each excluded decision

| Excluded decision | Evidence against it |
| --- | --- |
| `REVISION_REQUIRED` | The two blocking redlines are applied and verified, the derivation method is sound and its result empirically confirmed on all three chains, and the five non-blocking redlines are applied exactly once. The two defects this review found — X-11's false reason and the manifest boundary — are a corrected ground recorded in the addendum and a separate finding with its own route. Neither improves by another RS-30 cycle, and returning the proposal again would delay a sound delta while the separate boundary would still need its own RS-10. |
| `REJECT` | The boundary is real and was reproduced by execution twice, at two heads, by this reviewer. It is necessary (PR04 cannot complete without a disposition), safe in this form (never `PASS`, condition-keyed, self-extinguishing, exhaustively enumerated), and within this IA's bounded authority. Rejecting would force candidate C, a Product Owner waiver nobody has requested. |
| `IN_SCOPE_REPAIR` | Settled at review v1.0 §3 and unchanged. None of the enumerated files appears in instruction §7.1 or §7.2 or Plan §6.4, and PR04 plan §6.6 independently records four of them as outside PR04's approved loci. The §5 criterion in the proposal now states the distinguishing line explicitly and it holds. |
| `SPECIFICATION_CHANGE_REQUIRED` | Settled at review v1.0 §3 and unchanged. No product intent, behavior, exclusion or acceptance criterion moves; PF10 §2.13 records the interval as a consequence of the approved order. |

## 7. Effects

| Dimension | Effect |
| --- | --- |
| Requirements | None changes in substance. The affected obligations remain `K040-REQ-012` and `AC040-08` and the CI clause of PR04's completion condition (PR04 plan §4.2 condition 4), which the approved delta makes satisfiable rather than altering. |
| Dependencies | The order fixed by PF10 §2.13 is unchanged. **PR05 is covered** by this overlay and needs no separate one and no new loci, on the proof at proposal §7 and review v1.0 §7: PR05's Plan §6.5 loci classify to `{evidence, product, release}`, the release lane is where sanity stages 04 and 05 run, PR05 owns none of the enumerated files, and PR05 precedes PR06. PR05 inherits through the release lane only. PR06 owns convergence. |
| Tests | Plan §8 is unchanged, including all six `R040-IA30-02` proof classes. The four enumerated test homes change only to track the gates' corrected outcome vocabulary. |
| Ops | None. No Ops task, environment, deployment, vendor or database operation is created, required or performed. |
| Documentation | This review, one PF10 addendum overlay, a checkpoint and a handoff, all under `docs/ephemeral/`. No PF-Canon edit; `docs/pfcanon/` was read only. |
| Downstream | None on PR07, OPS01, independent QA, release promotion, PF09 movement or Epic closure. PR04's touch on `build_release_attestation.py` transfers no attestation ownership from PR06. |
| Evidence integrity | No governed evidence was written, refreshed or hand-edited by this review. Both simulations ran in an isolated scratch worktree that was removed; the repository is clean at `0f47079`. The addendum records the regeneration obligations the delta creates, all through existing owning writers. |
| Preserved work | PR04 plan §§5–8, §9 checkpoints C1–C3, and §§10–12 are preserved and valid; §9 item 15 and §4.2 condition 4 are now dispositioned. Proposal v1.0 and review v1.0 are preserved unchanged at their paths. |

## 8. Carried `CANON_CONFLICT_REGISTER`

Carried unchanged from Plan v2.1 §11.1, PR04 instruction §13, proposal v1.0 §12, review v1.0 §10 and proposal v1.1 §12. **No entry is reopened, relabeled, omitted, newly decided or resolved by this review, and neither `HDE-EPIC040-PR04-F01` nor the `HDE-EPIC040-PR04-F02` candidate is a register entry.**

| ID | Classification / status | Decision lineage | Carried effect | Remaining owner / state |
| --- | --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED` exactly as proposed | Thoth-17, 2026-09-08T13:23:24Z, against Specification v1.0 represented by approved v1.1 | Preserve explicit `Done` exclusions and current PF09.3 agreement | Source correction resolved; no drainage pending |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use the current controlled PF12 Markdown; historical identity mismatch is history only | Resolved; PF12 version currency is ordinary maintenance (U-04) |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use current PF14 v3.5.7; C040-05 controls its contradictory core-test text | Historical mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | QA identity history preserved; PR04 performs engineering checks, not independent QA | Historical mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED`, alternative A exactly | Isis-49, 2026-09-09T03:57:16Z, against Plan v1.0 | The four-argument Gate core supersedes precomputed-score passages; no second calculator | Permanent PF14 §6.7 correction pending with its governed maintainer; non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED`, alternative A exactly | Isis-50, 2026-09-09T11:48:08Z, Review v2.0 against Plan v2.0 and ADR v1.0 | 36-row taxonomy and 16-case conformance as delivered through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage pending with governed maintainers; non-gating |

Decision history for this finding is preserved in full: `REVISION_REQUIRED`, Isis-50, 2026-09-22T06:48:06Z, no addendum, against proposal v1.0; and `APPROVE`, Isis-50, 2026-09-22T07:27:55Z, one addendum, against proposal v1.1.

## 9. Unresolved facts

| ID | Status | Detail and owner |
| --- | --- | --- |
| **U-01** | Resolved | The baseline advanced again; `main` is `0f47079` and PR #463 has merged. Recorded at §2.1. |
| **U-02** | Carried, not raised | PR04 plan §14.2 decision D-03 remains a deliberately unbundled potential boundary. Owner: the PR04 session, through a separate RS-10 if the Product Owner rejects D-03. |
| **U-03** | Resolved | Specification v1.1's SHA-256 matches on independent recomputation. Closed. |
| **U-04** | Carried, non-gating | Repository-resolved PF12 v2.9.5 against the register's v2.9.6. Owner: the governed PF12 maintainer. Not load-bearing for F01 or §6.1. |
| **U-05** | Carried, non-gating | PF10's §1.1 Addendum Index lists through `2.13` while the body carries `2.14`. Observation for the PF10 drain owner. RS-20 neither edits PF10 nor allocates numbering; the addendum is page-ready with its number left unallocated. |
| **U-06** | Carried, non-gating | Repository prompt-provenance persistence remains `PENDING`; `docs/changes` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`. Usage metadata is preserved at §10 and in the handoff. Owner: the authorized repository writer. |
| **U-07** | **Resolved** | X-8 is **admitted** to the set (§4.2); X-10 is **upheld** as excluded, on execution (§4.3). Both halves of item B are decided, so nothing is left for implementation to discover. |
| **U-08** | **New, gating nothing in F01** | `tests/evidence/test_release_manifest_content_binding.py` fails because `adapter/http_reader.py` is a manifest member PR04 must change while PR04 may not refresh the manifest (§5). Recorded as candidate finding `HDE-EPIC040-PR04-F02`, on the PF10 §2.10 precedent. Owner: session `PR04-HDE-EPIC040-1`, through `RS-10`. Not decided, scoped or pre-approved here. |
| **U-09** | **New, non-gating** | Proposal §6.2 row 3 lists five outputs for `generate_determinism_gate_proofs.py`; the file declares six, adding `artifacts/cards/a3/IDENTITY_OK.txt` (§4.4). The addendum's regeneration obligation names all six. |

## 10. Return owner and stage

- **Decision:** `APPROVE`. **Exactly one** `PF10_BUILD_NOTES_ADDENDUM` is created: `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`.
- **`PR_RETURN_PHASE`:** none applies and none is asserted. The finding arose at **PR-20 planning**, before any Proceed, workspace, worktree, branch, commit, open pull request or CI run. **RS-40 is ineligible and is not invoked.**
- **Return owner and stage:** `PR-20 — Create Detailed PR Implementation Plan — 091426.1` in the dedicated PR-development session `PR04-HDE-EPIC040-1`, which issues PR04 plan **v1.1** as a complete successor carrying this overlay, in state `AWAITING_PO_PROCEED` for Nathan's separate exact `PR-30` invocation. The Flow Index's "prepublication resumes PR-30 directly" clause presupposes an existing original Proceed; none exists here, so the return is to PR-20.
- **Preserved authority.** Session `PR04-HDE-EPIC040-1` is retained and not replaced. The PR04 instruction v1.0, plan v1.0 `DRAFT`, the immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1, every active PF10 overlay, and accepted-final PR01, PR02 and PR03 remain exactly as they are. No accepted-final PR is rerun.
- **Nothing here authorizes** implementation, a product branch or pull request, a Proceed, a merge, auto-merge, PF10 editing, PF10 number allocation, canonical adoption, PF09 movement, a QA verdict, acceptance, deployment or closure. Merge is a Product Owner action; `PR-50` is Nathan-only and no route here reaches it.

## 11. Prompt-use provenance

`GCFPE_PROMPT_USES` — this entry, preserving the earlier ones by exact reference:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-02`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df`
- `work_unit_id` / `finding_ref`: `HDE-EPIC040-PR04` / `HDE-EPIC040-PR04-F01`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `RS-20 — Review Bounded Work-Unit Rescope — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204`
- `prompt_retrieved_revision`: page fetched, `page_last_edited_at` `2026-09-21T22:57:36.541Z`
- `role_stage`: continuing independent Lead Developer reviewer Isis-50 / RS-20 decision owner, second decision on this finding
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `session_disposition`: `RETAIN_EXISTING`
- `capture_time`: `2026-09-22T07:27:55Z`
- `runtime_identity`: not asserted beyond the Product Owner-assigned role and session reference
- `result`: this `HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v2.0`, `APPROVE`, with exactly one PF10 addendum overlay
- `result_refs`: repository paths in the front matter and §10; branch, commit and pull-request identities populated only after they exist

Preserved earlier entries, by exact reference: `GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01` (proposal v1.1 §13), `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01` (review v1.0 §13), `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01` (proposal v1.0 §13), `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01` (PR04 plan §16) and `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (PR04 instruction §15).

Repository provenance persistence remains `PENDING / NON_GATING` — see §9 U-06.
