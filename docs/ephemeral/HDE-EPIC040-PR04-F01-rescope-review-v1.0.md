---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR04-F01-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: RESCOPE_REVIEW_COMPLETE
decision: REVISION_REQUIRED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR04
finding_ref: HDE-EPIC040-PR04-F01
reviewed_artifact: HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0
reviewer: Isis-50 — continuing independent Lead Developer reviewer for HDE-EPIC040
session_disposition: RETAIN_EXISTING
role_session_ref: the continuing Isis-50 reviewer session that decided Implementation Plan Review v2.1 on 2026-09-09T13:36:43Z
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR04 / RS-20 (GCF-17.RESCOPE)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
authoring_context: APPROVED_BASE_WITH_OVERLAYS
decision_time_utc: 2026-09-22T06:48:06Z
addendum_created: NONE
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md
---

# HDE-EPIC040-PR04-F01 — Bounded Work-Unit Rescope Review v1.0

## 1. Decision

**`REVISION_REQUIRED`.**

The finding is real, its classification is correct, and its recommended candidate is the right one. The proposal's **enumerated bounded delta is provably incomplete**: §6.2 names six files, and the delta cannot achieve its own stated purpose without a seventh, `tools/evidence/run_sanity_pipeline_gate.py`. Because §6.2, §6.3 and risk R-01 deliberately state the overlay as an **exhaustive** file list in order to bound its precedent, an enumeration that is not exhaustive is a defect in the artifact, not an implementation detail inside it.

This decision creates **no** `PF10_BUILD_NOTES_ADDENDUM`. Under the RS-20 contract only `APPROVE` does.

**What is settled by this review and must not be relitigated at RS-30.** The classification is decided: `HDE-EPIC040-PR04-F01` is a **bounded implementation rescope** (§3). The suspended boundary is confirmed by execution, not inference (§2). Candidate **D** is the correct disposition (§5). The revision is confined to the redlines in §6.

**What this decision does not supply.** No implementation authority, no Product Owner Proceed, no merge permission, no PF09 movement, no QA verdict, no acceptance, no closure, no PF10 edit, no PF10 number, no canonical adoption.

## 2. Independent verification of the proven boundary

The proposal's conclusion was not accepted. Every load-bearing claim was re-derived from the repository at the current head, and the causal collision was **reproduced by execution** rather than inferred from two separate observations.

### 2.1 Repository baseline, re-verified by this reviewer

`main` has advanced since the proposal was authored. The proposal's baseline remains valid.

| Fact | Proposal (authoring time) | This review (decision time) |
| --- | --- | --- |
| `main` head | `3e943ada3987720cf69c491c2cb7eb4bc9e1ae45` | **`a07340965c1dabbe0205135e321ecd6e76687d68`**, tree `9ab2c9a9c3ed1dfb9aba127ee19c87fce8d98702`, committed 2026-09-22T07:35:39+01:00 |
| Working tree | clean | clean, before and after every observation below |
| Non-documentation drift from `6ecacafb…` | empty | **still empty** — `git diff 6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612..HEAD -- . ':(exclude)docs/'` produces no output |
| Post-PR03 commits touching `ci/` or `.github/` | `3c0b1fa`, `c683255`, both ancestors of `6ecacafb` | **confirmed exactly these two**; `fe65a3b` and `28612bc` touch `AGENTS.md` only |
| PR04 vehicle state | none | **none** — no branch, commit, pull request, Proceed, implementation, review, CI run or merge exists |

The three commits added to `main` since the proposal (`590ae71`, `76689ac`, `a073409`) touch only `docs/ephemeral/` and `docs/prompt_ecosystem_management/`. The executable baseline is unchanged and the finding is unaffected.

**Storage state correction.** The proposal's §11 U-01 and the Flow Index both record pull request #453 as open. **#453 has merged**, and **#457 has merged** (`a073409`) — the proposal itself is now on `main` at the cited path. This review reads it from `main`.

### 2.2 Artifact identity

Every supplied SHA-256 was independently recomputed at `a073409`.

| Artifact | Repository path | SHA-256 | Result |
| --- | --- | --- | --- |
| Reviewed proposal | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` | `51eae27c2013722a3aebf22ca073587ad4d83c105176df87e970c37bc9f46bf6` | **matches**; 268 lines / 32,091 bytes; read complete |
| Immutable base Plan v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` | `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` | **matches** |
| Specification v1.1 | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` | **matches — U-03 resolved**, recomputed by this reviewer |
| Implementation Audit v2.0 | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` | `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` | recorded |
| Plan Review v2.1 | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` | `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` | recorded |
| PR04 instruction v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md` | `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf` | **matches**; 359 lines / 57,324 bytes |
| PR04 implementation plan v1.0 | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md` | `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65` | **matches**; 653 lines / 122,661 bytes |

**Current controlled PF10**, resolved read-only from `docs/pfcanon/` and completely read by this reviewer: `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`, recomputed SHA-256 `1421e4d6124a07006ec88eaae5c065934dd38614552c73b965e21c7ef0a1a93f` — **matches**; 1,649 lines / 181,316 bytes. It is the unique PF10 Markdown in `docs/pfcanon/`. No Google Doc, `.doc`, `.docx`, export, archive result or search hit was opened, compared or cited. Recorded as provenance of what was read; it gates nothing downstream.

Applicable active overlays were read at their repository paths as listed in the proposal §2. Two are load-bearing and were read in full: **PF10 §2.12** (`docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md`), which places the executing-mechanics admission boundary in `engine/config/registry_loader.py`; and **PF10 §2.13** (`docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md`). PF10 §2.8 (PF10-FORM-001) was read as the form rule governing any addendum this stage could emit. PF10 §2.14 exists in the body and is not applicable.

### 2.3 The collision, reproduced by execution

The proposal offers two separate observations (E-01, E-02) and infers a collision between them. This reviewer **reproduced the collision directly**, in an isolated `git worktree` under the session scratchpad, by applying a minimal PR04-shaped change to `engine/runtime/public.py` — a file inside PR04's own approved loci — and running the selected gates against it. The repository working tree was clean before and after; the worktree was removed and `git worktree prune` run; `git status --porcelain` is empty and `HEAD` is unchanged at `a073409`.

| ID | Observation | Result |
| --- | --- | --- |
| **V-01** | `load_active_mechanics_bundle()` under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` | `SchemaValidationError` **`INCOMPLETE_RELEASE_ROSTER`** — E-01 reproduced |
| **V-02** | `catalog/manifest.json` `files` length vs. `ADMITTED_RELEASE_ROSTER` | **15 vs. 44**, and the 15 are a **strict subset** of the 44 (verified set-wise, not by count alone) — E-03 reproduced and strengthened |
| **V-03** | `generate_open_rails_abba_proof.py --check-current` at baseline under the job-declared rails `SAFE_MODE=0 ALLOW_NETWORK=1` | **exit 0**, `{"result":"pass","status":"OK","top_level_pass":true}` — E-02 reproduced |
| **V-04** | Release-sanity stage 04 and stage 05 validators at baseline | both **OK** — the release lane is green today |
| **V-05** | **Simulation A.** `engine/runtime/public.py::_compute_harmony_band` routed through the admission owner instead of `ts_v0`; then `generate_open_rails_abba_proof.py --check-current` | **exit 1**, `SchemaValidationError: release manifest does not yet contain the complete adopted roster` at `registry_loader.py:1224` via `:1461` |
| **V-06** | Same simulation; release-sanity **stage 04** validator | **FAIL** — same `INCOMPLETE_RELEASE_ROSTER` refusal |
| **V-07** | **Simulation B.** `adapter/http_reader.py::reader_v1_post` implements the instruction §6.5 success path at the existing declared route; release-sanity **stage 05** validator | **FAIL — `AssertionError: writer`**, i.e. `require(post.status_code==405, …, 'writer')` at `generate_a7_transport_proofs.py:75` |
| **V-08** | Same simulation; `tests/http/test_reader_a7_transport.py` and `tests/transport/test_a7_transport_proofs.py` | **8 failed, 13 passed** |

V-05 through V-08 convert the finding from an inference to a demonstration: **a change confined to PR04's own approved loci, implementing exactly PR04's approved behavior, turns all three selected gates red.** The proposal's §4.2 conclusion is correct and is now stronger than the proposal states it.

### 2.4 Gate selection and canon corroboration

| Claim | Verification | Result |
| --- | --- | --- |
| Rails lane chain | `.github/workflows/ci.yml:164–173` "Run rails policy and secret-safety lane" → `run_rails_job_definitions.py … ci/jobs/rails_open_conformance.yml` → that file's **line 18**, `generate_open_rails_abba_proof.py --check-current` | confirmed (the proposal's `164–172` is `164–173`; immaterial) |
| Release lane chain | `ci.yml:228` / `:259` → `build_release_attestation.py --require-clean` → `run_sanity_pipeline_gate.py` (`:669`) → `run_sanity_pipeline.py` stages `04`/`05` (`:68`, `:69`; validators at `:123` and `:146`) → `AttestationBuildError("final_sanity_pass_missing")` at `:766` | confirmed, **with the correction in §4** |
| Release lane selected for every PR04 product path | `classify_ci_changes.py:1451–1452` — any `_PRODUCT_PREFIXES` path yields `{"product","release"}`; the tuple at `:226` includes `adapter/`, `engine/`, `presenter/`, `schemas/`, `scripts/` | confirmed |
| A7 pins `POST /reader` → 405 | `generate_a7_transport_proofs.py:75`; `adapter/http_reader.py:459–462` returns `_error("method_not_allowed", 405)` | confirmed |
| Legacy band path still live | `engine/runtime/public.py` `_compute_harmony_band` derives the band via `ts_v0.extract_ts` / `compute_features` / `band_v0` | confirmed |
| Failure receipt already exists in canon, codes open | `schemas/hde_release_attestation_failure.v1.json` — `code` and `stage` are `"pattern": "^[a-z0-9_]+$"`, **not enums**; `build_release_attestation.py::_write_failure` (`:498–507`) already emits it on every `AttestationBuildError` | confirmed — **§6.1's narrowing holds** |
| Success attestation pins the wire value | `schemas/hde_release_attestation.v1.json` — `validation_result: const "PASS"`, `release_admission: const "PR06R_B_FINAL_PASS"` | confirmed, **with the precision note in §6, redline R-3** |

**Canon independently corroborates the cause.** PF10 §2.13 — an active overlay, not repository code — records that "the actual repository release remains the original incomplete 15-member manifest with identity `e0d5c980…`" and that "**PR06 alone** owns final actual 44-member materialization, identity recomputation, convergence, and promotion", with "PR04 owns application eligibility, identity and consumer integration; PR05 owns golden comparison/read-only readiness". The interval between PR04's consumer switch and PR06's admission is therefore a property of the approved plan recorded in current canon, not an artifact of implementation.

### 2.5 Closed set of in-scope treatments

Each row of proposal §4.4 was checked against the instruction text rather than accepted:

- *Retain any legacy success path* — instruction §10 and Plan §6.4 ("Remove hash/`ts_v0` scoring"); Plan §5 "obtains the harmony band from the validated result, not `ts_v0`". Prohibited.
- *Expand or activate the manifest* — instruction §9 and PR04 plan §4.3 exclude "release promotion, manifest expansion or activation"; PR04 plan §6.6 lists `catalog/manifest.json` as explicitly unchanged; PF10 §2.13 assigns it to PR06. Prohibited.
- *Bypass, relocate or weaken admission* — PF10 §2.12; instruction §7.3. Prohibited.
- *Feed a synthetic or test-only release into a governed gate or the attestation* — instruction §6.4 verbatim: "local fixture candidates stay test-only". Prohibited, and a `PR06R_B_FINAL_PASS` so produced is a fabricated passing result.
- *Convert the gates to frozen-byte comparison while still emitting PASS* — instruction §6.6 verbatim: "do not weaken a refusal to preserve an old fixture". Prohibited.
- *Skip, disable or quarantine* — `AGENTS.md`, and PR04 plan §4.2 condition 4 verbatim. Prohibited.

The set is closed and every member is genuinely prohibited or false. Confirmed.

## 3. Classification — decided

**`HDE-EPIC040-PR04-F01` is a bounded implementation rescope.** This is decided and is not reopened by the revision.

**Not an `IN_SCOPE_REPAIR`.** Instruction §7.1 and Plan §6.4 enumerate PR04's owned loci; **none of the affected gate, sanity-pipeline, attestation or workflow files appears in either**. The PR04 implementation plan reaches the same conclusion from the other direction: its §6.6 lists `.github/workflows/ci.yml`, `ci/jobs/*.yml`, `tools/evidence/run_sanity_pipeline.py` and `tools/evidence/build_release_attestation.py` as "outside PR04's approved loci; they change only under the RS-20 disposition of F01". Neither the immutable base nor any active overlay authorizes the repair, so the existing owner cannot make it under unchanged authority.

**Not a `SPECIFICATION_CHANGE_REQUIRED`.** No product behavior, intent, exclusion or acceptance criterion moves. Specification v1.1 and Plan v2.1 §§5.7, 5.8, 6.4 are satisfied exactly as written; §8's requirement-to-unit mapping is unchanged in substance. What is missing is only a truthful way for three CI gates to express a state that the approved dependency order itself creates — a state PF10 §2.13 already records as canon. Product intent is untouched, so this is not Nathan's decision to take.

**Not a defect in PR01–PR03.** V-03 and V-04 show the gates green at the accepted PR03 state because its consumers still use `ts_v0`. PR03 passed lawfully. No accepted-final work is reopened, rerun, revised or reaccepted.

## 4. Why the submitted delta is not approvable as written

The finding is a rescope; the **remedy as enumerated is incomplete**.

### 4.1 The omitted file, proven

Proposal §6.2 item 2 requires `build_release_attestation.py` to withhold the success value and emit its failure receipt with a distinct code, and item 1 requires sanity stages 04 and 05 to record an explicit `RELEASE_NOT_ADMITTED` outcome that "is never `PASS`". Both are blocked by a file the proposal does not name:

1. `build_release_attestation.py:669` invokes **`tools/evidence/run_sanity_pipeline_gate.py`**, not `run_sanity_pipeline.py` directly.
2. `run_sanity_pipeline_gate.py::_expected_log()` constructs a byte-exact expected log containing `check <name>:OK` for **all fifteen** stages plus `first_failed_stage:NONE` and `summary:PASS`; `_valid_log()` returns true only on `data == _expected_log()` — **byte equality**. Any other log makes `main()` return non-zero.
3. `run_sanity_pipeline.py::_render_log` (`:220`) collapses every stage status to exactly two tokens: `"OK" if status == "OK" else "FAIL"`. **There is no third token today.**
4. `build_release_attestation.py:757–766` independently requires the log to end with `"check 15 Final-LF validation:OK\nfirst_failed_stage:NONE\nsummary:PASS\n"`.

So a truthful third state must be expressible in `run_sanity_pipeline.py` **and** accepted by `run_sanity_pipeline_gate.py` before it can reach the attestation's failure receipt at all. The gate wrapper is a second, independent byte-exact `PASS` pin sitting between the stages and the attestation. **The six-file delta cannot achieve its own §6.2 purpose.**

### 4.2 Why this is `REVISION_REQUIRED` and not `APPROVE`

This reviewer could have approved a seven-file delta. It did not, for one reason: **it has proven that six is insufficient, and it has not proven that seven is sufficient.**

Establishing sufficiency requires a reproducible trace of every `PASS` pin in the rails and release chains, which neither the proposal nor this review performed. The proposal was authored by the retained whole-change IA with deep context and still missed one file in an enumeration it deliberately made exhaustive; a reviewer substituting its own unverified enumeration would repeat that failure with less context and no better method. Approving an overlay whose completeness cannot be vouched for would land the PR04 session against a file list that blocks again at implementation — and force a **second** rescope for the same finding. One bounded RS-30 round trip is the cheaper and more honest outcome.

`APPROVE` requires the overlay to be "complete, executable, smallest safe scope". The submitted overlay is executable in purpose and smallest in intent, but **not complete**. `REVISION_REQUIRED` is the matching value: a potentially valid request lacking precision and impact coverage, repairable by its author.

## 5. Candidate disposition — D remains correct

Candidate **D** is the right disposition and the revision should return with D, corrected. Recorded so RS-30 does not reopen it:

- **D over A.** Identical engineering; A additionally adds a work unit to an immutable approved decomposition. Strictly larger for the same result.
- **D over B.** B changes the whole-change dependency order fixed by PF10 §2.13, and PR06's own admission work depends on PR04/PR05 outputs, so the re-sequence is not obviously coherent. Largest and least safe.
- **D over C.** C leaves ordinary CI red across PR04 **and PR05** (§7), destroying the signal for every candidate in that window, and defers rather than resolves. C also requires Nathan's express waiver, which no one has requested and which this review does not request.

**A cost the proposal overstates, in D's favour.** §6.3 records D's cost as "widens PR04's loci to six CI/evidence files", and R-01 flags the precedent. The *CI surface* cost is nil: PR04's candidate **already** runs full validation and **all seven lanes**, because PR04 plan §6.5 changes `ci/checks/classify_ci_changes.py`, which is a member of `_FULL_VALIDATION_PATHS`. Executing the classifier confirms `classify_paths(("ci/checks/classify_ci_changes.py",))` returns every lane `True` with `reason='selected_lanes'`, and `.github/workflows/ci.yml` independently maps to all seven. **Adding the workflow and job files to PR04's loci selects no additional lane and enlarges no CI surface.** The real cost of D is precedent and ownership, addressed by redlines R-6 and R-7.

## 6. Exact redlines for RS-30

Returned to the RS-10 proposal author — the retained whole-change HDE-EPIC040 Implementation Architect session — for a successor `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1`. **R-1 and R-2 are blocking; R-3 through R-7 are required corrections that do not, by themselves, change the disposition.**

| ID | Section | Required change |
| --- | --- | --- |
| **R-1** *(blocking)* | §4.4, §6.2, §6.3 candidate D, §10 | Add **`tools/evidence/run_sanity_pipeline_gate.py`** to the enumerated file set, with the evidence in §4.1 of this review: `build_release_attestation.py:669` invokes the gate wrapper; `run_sanity_pipeline_gate.py::_expected_log()` / `_valid_log()` require byte equality with an all-`:OK`, `summary:PASS` log; `run_sanity_pipeline.py::_render_log` (`:220`) emits only `OK`/`FAIL`. Correct §4.4's closing sentence and the §6.3 cost cell to the corrected count. |
| **R-2** *(blocking)* | §6.2, new subsection | State the **method** by which the enumerated set was derived and its stopping condition — an explicit, reproducible trace of every `PASS` pin reachable from the rails lane and from the release lane through `build_release_attestation.py` — so that completeness is a testable claim rather than an inspection result. An exhaustive enumeration is what R-01 relies on to bound the precedent; it must be derived exhaustively. |
| **R-3** | §6.1, third bullet and §10 E-13 | `schemas/hde_release_attestation.v1.json` pins `pipeline_stop` as `{"type": "null"}`, **not** `const null`. `validation_result` and `release_admission` are `const` as stated. Correct for accuracy; the §6.1 narrowing is unaffected and is confirmed. |
| **R-4** | §7 "Dependencies", §11 R-03 | Replace the assertion that PR05 "inherits the same interim gate condition" with its proof, supplied in §7 of this review. |
| **R-5** | §6.3 candidate D cost cell | Record that widening PR04's loci to the named CI/evidence files **selects no additional CI lane**, because PR04's candidate already runs full validation and all seven lanes via its planned change to `ci/checks/classify_ci_changes.py` (§5 of this review). This materially lowers D's stated cost and should be visible to the reader. |
| **R-6** | §5, second bullet | Qualify "every truthful treatment lies outside the work unit's approved loci": PR04's plan §6.2 and §6.5 **already** change several paths outside instruction §7.1 as "necessary dependents", including `ci/checks/classify_ci_changes.py`, `tools/evidence/run_canonical_json_gate.py` and `tools/cli/generate_showcompat_artifacts.py`, without a rescope. State the distinguishing criterion the overlay rests on — these change **gate semantics and acceptance**, whereas the plan's dependents change **coherence registration and frozen-byte validation** — because R-01's precedent argument depends on that line being drawn explicitly. |
| **R-7** | §6.2 item 2, §7 "Downstream" | State explicitly that PR04's bounded touch on `tools/evidence/build_release_attestation.py` **transfers no attestation ownership from PR06**. Plan §4.2 maps "Complete release / external attestation" to `scripts/cut_release_manifest.py`, `scripts/release_id_recompute.py` and `build_release_attestation.py`, and Plan §6.6 gives PR06 the "owning attestation validator only where current contract gaps are evidenced". The overlay must bound PR04's touch to the non-admitted outcome and its failure receipt. |

**Conditions that the revised §6.2 must carry forward unchanged** — this reviewer confirms them as correct and they are not open for revision:

- The explicit outcome is **never** `PASS`, never `top_level_pass: true`, and never a frozen-byte substitute presented as a live result. Frozen captures stay frozen with their existing nonclaims.
- The ordinary-CI acceptance keys on **that one explicit outcome only**, and on the observed non-admitted state of the active release — never on a generic failure, a lane name or a time window. This is R-02's mitigation and it is binding.
- Because the acceptance is conditioned on a runtime-observable fact rather than a hardcoded window, it is **self-extinguishing by construction**: once PR06 admits the complete 44-member roster the branch is never taken, and its continued presence is truthful and inert. No later removal is owed, no unit is allocated scope for one, and no cleanup pull request is required. Removal is optional hygiene only.
- No change to the `hde.release_attestation.v1` success schema or to the `PR06R_B_FINAL_PASS` wire value is authorized. §6.1 establishes that none is expected. If implementation nonetheless requires one, that portion is a **separate PF12 canon decision** routed to the governed PF12 maintainer as a new finding, and is not pre-authorized by any RS-20 disposition.

## 7. PR05 — stated explicitly, as required

**Yes. An overlay approved on the corrected delta must cover PR05, and PR05 requires no separate overlay and receives no new loci.**

This is proven, not assumed:

1. PR05's owned loci (Plan §6.5) are `tests/fixtures/magic10/v1/goldens.json`, `tools/config/artifacts.py`, `tools/config/generate_config_artifacts.py`, `tools/bodygraph/check_magic10_gate_readiness.py`, and existing config/core/bodygraph/application test homes.
2. Executing the classifier over exactly those paths yields the lane union **`{evidence, product, release}`**. The **release lane is selected**.
3. The release lane is precisely where sanity stages 04 and 05 run (`ci.yml:228`/`:259` → attestation → gate wrapper → pipeline). PR05 therefore hits the identical refusal, via the release lane. It does **not** select the rails lane, so PR05 inherits through one chain rather than two.
4. PR05 owns **none** of the affected files and, like PR04, cannot make any truthful treatment under its own authority.
5. PR05 runs before PR06 under the dependency order fixed by PF10 §2.13.

Because the approved condition keys on the **non-admitted state of the active release** and not on PR04's candidate, it covers every candidate in the interval — PR05 included — and extinguishes for all of them simultaneously when PR06 lands. The revised proposal must carry this reasoning at §7 and §11 R-03 (redline R-4).

## 8. Effects

| Dimension | Effect of this `REVISION_REQUIRED` decision |
| --- | --- |
| Requirements | None. No requirement or acceptance criterion is changed, added or removed. The obligations the finding touches remain `K040-REQ-012` / `AC040-08` and the CI clause of PR04's completion condition (PR04 plan §4.2 condition 4); both stay exactly as approved and undecided. |
| Dependencies | None changed. The order `PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01` fixed by PF10 §2.13 is untouched. PR05's inherited condition is stated at §7 and remains undisposed until a qualifying `APPROVE`. PR06 owns convergence under any disposition. |
| Tests | None. PR04 plan §8 stands unchanged, including all six `R040-IA30-02` proof classes, the eligibility matrix, the Reader POST suite and the CLI/compat carriers. |
| Ops | None. No Ops task, environment, deployment, vendor or database operation is created, required or performed. |
| Documentation | This review, its checkpoint and its handoff only, all under `docs/ephemeral/`. **No PF10 addendum is created.** No PF-Canon edit is proposed or made; `docs/pfcanon/` was read only. |
| Downstream | None on PR07, OPS01, independent QA, release promotion, PF09 movement or Epic closure. |
| Evidence integrity | No governed evidence was written, refreshed or hand-edited. The two simulations ran in an isolated scratch worktree, which was removed; the repository tree is clean at `a073409` and no governed artifact, frozen capture, path proof, Index or Mirror row was touched. |
| Preserved work | PR04 plan §§5–8 in full, §9 checkpoints C1–C3 executable as written, and §§10–12 are preserved and valid. Only §9 item 15 and §4.2 condition 4 remain dependent on a disposition, which this decision does not supply. The proposal v1.0 itself is preserved intact on `main`; v1.1 supersedes it without deletion. |

## 9. Evidence against each excluded decision

| Excluded decision | Evidence against it |
| --- | --- |
| `APPROVE` | The enumerated overlay is incomplete (§4.1, proven) and its completeness was not established by a reproducible method (§4.2). `APPROVE` requires a complete overlay. |
| `REJECT` | The boundary is real, reproduced by execution (V-05 to V-08), necessary (PR04 cannot complete without a disposition), safe in the candidate-D form (never `PASS`, condition-keyed, self-extinguishing), and squarely within this IA's bounded authority. Rejecting would leave PR04 with no lawful path and force candidate C, a Product Owner waiver nobody has requested. |
| `IN_SCOPE_REPAIR` | Neither the immutable base nor any active overlay authorizes the repair. None of the affected files appears in instruction §7.1 or Plan §6.4, and PR04 plan §6.6 independently records four of them as outside PR04's approved loci (§3). |
| `SPECIFICATION_CHANGE_REQUIRED` | No product intent, behavior, exclusion or acceptance boundary moves (§3). The interval the finding describes is recorded in current canon at PF10 §2.13 as a consequence of the approved order. Returning this to Nathan would misroute an implementation matter as a product decision. |

## 10. Carried `CANON_CONFLICT_REGISTER`

Carried unchanged from Plan v2.1 §11.1, PR04 instruction §13 and proposal §12. **No entry is reopened, relabeled, omitted, newly decided or resolved by this review, and `HDE-EPIC040-PR04-F01` is not a register entry.**

| ID | Classification / status | Decision lineage | Carried effect | Remaining owner / state |
| --- | --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED` exactly as proposed | Thoth-17, 2026-09-08T13:23:24Z, against Specification v1.0 represented by approved v1.1 | Preserve explicit `Done` exclusions and current PF09.3 agreement | Source correction resolved; no drainage pending |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use the current controlled PF12 Markdown; historical identity mismatch is history only | Resolved; PF12 version currency is ordinary maintenance (§11 U-04) |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | Use current PF14 v3.5.7; C040-05 controls its contradictory core-test text | Historical mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED` | Same Thoth decision | QA identity history preserved; PR04 performs engineering checks, not independent QA | Historical mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED`, alternative A exactly | Isis-49, 2026-09-09T03:57:16Z, against Plan v1.0 | The four-argument Gate core supersedes precomputed-score passages; no second calculator | Permanent PF14 §6.7 correction pending with its governed maintainer; non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED`, alternative A exactly | Isis-50, 2026-09-09T11:48:08Z, Review v2.0 against Plan v2.0 and ADR v1.0 | 36-row taxonomy and 16-case conformance as delivered through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage pending with governed maintainers; non-gating |

Reviewer fields for this review are supplied in §1 and the front matter. Review fields for a successor proposal v1.1 remain explicitly **not yet reviewed**.

## 11. Unresolved facts

| ID | Status | Detail and owner |
| --- | --- | --- |
| **U-01** | **Resolved and corrected** | The proposal's baseline `3e943ad…` has advanced to `a073409…`; pull requests **#453 and #457 have both merged** (the proposal itself is now on `main`). The Flow Index still records #453 as open — stale, corrected by this review's Notion record. Nothing in F01 changes (§2.1). |
| **U-02** | Carried, not raised | PR04 plan §14.2 decision D-03 (valid self-pair exit-0 carrier) is a potential second boundary, deliberately not bundled into F01. This review does not raise, bundle or decide it. Owner: the PR04 session, through a separate RS-10 if the Product Owner rejects D-03. |
| **U-03** | **Resolved** | The Specification v1.1 SHA-256 was independently recomputed by this reviewer as `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` and **matches** the supplied value (§2.2). The proposal's §11 U-03 can be closed at v1.1. |
| **U-04** | Carried, non-gating | The repository-resolved current PF12 is v2.9.5 against the register's recorded v2.9.6. Unchanged by this review and not load-bearing for F01 or §6.1, both of which cite the repository's actual schema files. Owner: the governed PF12 maintainer. |
| **U-05** | **New, non-gating** | PF10's §1.1 Addendum Index lists entries through `2.13`, while the body carries `## 2.14 Specification format authority`. The index is one entry behind the body. Recorded as an observation for the PF10 drain owner; RS-20 neither edits PF10 nor allocates numbering, and no addendum is created by this decision in any case. |
| **U-06** | **New, non-gating** | Repository provenance persistence remains `PENDING`: `docs/changes` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`, with no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination. Usage metadata is preserved in §12 and in the handoff instead. Nothing is invented and no authorized work is blocked. Owner: the authorized repository writer, once a real procedure is installed. |

## 12. Return owner and stage

- **Decision:** `REVISION_REQUIRED`. **No addendum is created.**
- **Receiver:** `RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1`, https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204
- **Return owner:** the **same proposal author session** — the retained whole-change HDE-EPIC040 Implementation Architect that produced `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.0`. Artifact type and this IA decision owner are preserved. No new session, role or approval owner is created.
- **Expected successor:** `HDE-EPIC040-PR04-F01-RESCOPE-PROPOSAL v1.1`, `RESCOPE_PROPOSAL_PENDING_REVIEW`, carrying redlines R-1 through R-7 and returning to this same Isis-50 reviewer session for a second RS-20 decision.
- **`PR_RETURN_PHASE`:** none applies and none is asserted. The finding arose at **PR-20 planning**, before any Proceed, workspace, worktree, branch, commit, open pull request or CI run. Those vehicle facts are truthfully **not yet produced**, not missing prerequisites. The three execution values (`PR-30_PREPUBLICATION`, `PR-30_POSTPUBLICATION`, `PR-35`) are not in play, and **RS-40 is ineligible and is not invoked**.
- **Eventual native return point, on a later qualifying `APPROVE`:** `PR-20 — Create Detailed PR Implementation Plan — 091426.1` in the dedicated PR-development session `PR04-HDE-EPIC040-1`, which then issues PR04 plan v1.1 as a complete successor in state `AWAITING_PO_PROCEED` for Nathan's separate exact `PR-30` invocation. The Flow Index clause "prepublication resumes PR-30 directly" presupposes an existing original Proceed; **none exists here**, so the return is to PR-20 and not to PR-30.
- **Preserved authority.** The dedicated session `PR04-HDE-EPIC040-1` is retained and is not replaced. The PR04 instruction v1.0, plan v1.0 `DRAFT`, the immutable Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1, every active PF10 overlay, and accepted-final PR01, PR02 and PR03 all remain exactly as they are. No accepted-final PR is rerun.
- **Nothing here authorizes** implementation, a product branch or pull request, a Proceed, a merge, auto-merge, PF10 editing, PF10 number allocation, canonical adoption, PF09 movement, a QA verdict, acceptance, deployment or closure. Merge is a Product Owner action; `PR-50` is Nathan-only and no route here reaches it.

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES` — this entry, preserving the earlier ones by exact reference:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` (recomputed)
- `work_unit_id` / `finding_ref`: `HDE-EPIC040-PR04` / `HDE-EPIC040-PR04-F01`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `RS-20 — Review Bounded Work-Unit Rescope — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204`
- `prompt_retrieved_revision`: page fetched, `page_last_edited_at` `2026-09-21T22:57:36.541Z`
- `role_stage`: continuing independent Lead Developer reviewer Isis-50 / RS-20 decision owner
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `session_disposition`: `RETAIN_EXISTING`
- `capture_time`: `2026-09-22T06:48:06Z`
- `runtime_identity`: not asserted beyond the Product Owner-assigned role and session reference
- `result`: this `HDE-EPIC040-PR04-F01-RESCOPE-REVIEW v1.0`, `REVISION_REQUIRED`, no addendum
- `result_refs`: repository path in the front matter; branch, commit and pull-request identities populated only after they exist

Preserved earlier entries, by exact reference: `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01` (proposal §13), `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01` (PR04 plan §16) and `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (PR04 instruction §15).

Repository provenance persistence remains `PENDING / NON_GATING` — see §11 U-06.
