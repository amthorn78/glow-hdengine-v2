---
artifact_type: REVIEW_RECORD
artifact_id: HDE-GTWPE-T05-ISIS-REVIEW
artifact_version: "1.0"
subject: Isis review of the T-05 brief's two items (the HDE Mechanics Guide §37.17 snapshot root, and the a3 marker and release-sanity stage 04 as GATE:CORE-DET evidence), with a draft HDE Build Notes addendum 2.1
responds_to: HDE-GTWPE-T05-ISIS-REVIEW-BRIEF v1.0, docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-isis-review-brief.gtwpe-20261101-pf10-v14-0-5.md, branch claude/gtwpe-triage-authoring-j94ewf, commit f28c9e3
requested_by: Nathan / Product Owner, 2026-11-02 ("Follow this, BUT i want the new addendum numbered 2.1. It will go in the next post drained PF10 document.")
reviewer: Isis, Lead Developer (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)
decision_owner: Product Owner
repository_head_read: origin/main 84d6d1cad95c67788336d174dc4b8922d9bb0cb2
gtwpe_branch_head_read: 97938c448584533199d9d01638b1ea1ff986af59. The brief, the HDE Governance v2.8.10 draft and the HDE Mechanics Guide v3.5.10 draft are unchanged from f28c9e3. Later commits touch only PF07, the LEDGER and a T-01 follow-up redline for Appendix D.4
created_at: 2026-11-02T03:17:00Z
---

# T-05 open items: Isis review

## 1. Result

| # | Question | Recommendation | Changes canon | Where the decision is recorded |
| :- | :- | :- | :- | :- |
| Q-2b | Is release-sanity stage 04 GATE:CORE-DET evidence under closed rails? | **Yes. Option A**, with one precision: only a passing result counts (§4.3) | Yes | Draft addendum 2.1, R-1 |
| Q-2a | Correct the earlier addendum's fact about the a3 marker? | **Yes.** The fact was wrong, and so was the conclusion drawn from it. The marker is a current, checked output, not history | Yes | Draft addendum 2.1, R-2 |
| Q-1 | Which path should HDE Mechanics Guide §37.17 "Snapshot root" name? | **Option B**, with a currency condition. The governed snapshot fails its own check today (FND-007), and the brief does not say so | Yes, an evidence rule as well as wording | Draft addendum 2.1, R-3 |

The draft addendum is numbered **2.1** and written to stand alone in the next PF10 base version, after HDE Build Notes v14.0.5 has drained (§6). It needs no code, test or evidence change.

## 2. Correction: the a3 marker error was mine

I wrote the draft of the earlier addendum (HDE Build Notes v14.0.5 addendum 2.16, from `docs/ephemeral/HDE-EPIC041-PF10-core-det-evidence-addendum-draft-v1.0.md`, #823). It says that `artifacts/cards/a3/IDENTITY_OK.txt` "is a frozen marker last changed by HDE-EPIC024 (2026-01-22)". That is false.

- **What is true.** The lower-case marker last changed on 2026-07-13, in HDE-EPIC038 PR-02 (`ceefe4f5`). `tools/evidence/generate_determinism_gate_proofs.py` writes it as one of its six outputs. Release-sanity stage 04 and the identity closure check it.
- **How the error happened.** I took the history of the upper-case path `artifacts/cards/A3/IDENTITY_OK.txt` (last changed in `16f4215c`, 2026-01-22, HDE-EPIC024) and attributed it to the lower-case copy. I also never traced what writes the lower-case copy. If I had, I would have found stage 04.
- **What it caused.** R-1 of that addendum names five owner tests and omits stage 04. Stage 04 is the one release-lane determinism proof on the real compat path. The wrong date is the visible symptom; the omission from R-1 is the substantive error.

The brief's Q-2 facts are correct. I re-verified them (§3).

## 3. The brief's facts, verified

All checks below ran on `main` `84d6d1ca` under closed rails: `env -i`, `LC_ALL=C`, `TZ=UTC`, `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=test`. The working tree stayed clean. This clone has full history.

| Brief claim | Result | Note |
| :- | :- | :- |
| §37.17 raw bytes are `audit/gates/arch/*arch/\\*\\/\\` | Confirmed | Published HDE Mechanics Guide line 7488; T-05 draft line 7504 |
| `scripts/architecture_capture.sh` line 6 writes `_arch/${EPIC_ID}_${STAMP}`; `scripts/card_close.sh` line 147 calls it | Confirmed | |
| "147 files … in 21 snapshot directories" | **Corrected** | 147 files is right. They sit in 20 epic-stamped snapshot directories, plus `_arch/missing/not_20251025T122821Z/` (8 files) and `_arch/README.md`. This does not change the options |
| `tests/arch/test_arch_capture_exists.py` was retired on 2026-10-13 | Confirmed | `tests/retired_tests.md` line 14 |
| The governed snapshot is `artifacts/architecture/architecture_snapshot.keys_only.json` | Confirmed | HDE Schemas & Artifacts `epic038.pr04.architecture_snapshot` (line 3354); HDE Build Checklist Distillation line 859 |
| "Architecture is protected independently in product CI" by `tests/evidence/test_architecture_snapshot.py` | **Partly true** | The test checks the current analysis: verdict `pass`, `unknown_count` 0, and no write to the stored file. It does not compare the stored file with a fresh analysis |
| — (not in the brief) | **New** | `python tools/evidence/generate_architecture_snapshot.py --check` exits 1 with `STALE:artifacts/architecture/architecture_snapshot.keys_only.json`. Its test passes (5 passed). This is FND-007, recorded as CRD candidate item 12(a) in `docs/ephemeral/HDE-EPIC041-CL-40-cycle-gap-scan-v1.0.md` (line 88). It is still open |
| History of `artifacts/cards/a3/IDENTITY_OK.txt`, and its content | Confirmed | `ceefe4f5` 2026-07-13, then `16f4215c` 2026-01-22 |
| Six generator outputs; two fixture charts; real compat path | Confirmed | Generator lines 30–33 |
| Stage 04 calls the generator; identity closure lists it; owner-test mapping | Confirmed | `run_sanity_pipeline.py` lines 101–104 and 184; `regenerate_identity_closure.py` lines 229–233; `classify_ci_changes.py` lines 670–671 |
| The release attestation builder runs the closure in CI's release lane | Confirmed, and wider | `build_release_attestation.py` lines 740–764 run the closure in write mode, then with `--check`, then `run_sanity_pipeline_gate.py`, which runs all 15 stages. The CI classifier puts `engine/compat/compute.py`, `engine/core/compute_core.py`, `engine/magic10/composite.py`, `engine/cli/main.py`, `engine/reader_v1/emitter.py` and the generator in the release lane. A change to the compat path therefore runs stage 04 in CI |
| `--check` exits 0; owner test 15 passed | Confirmed | Rerun for this review |
| — (not in the brief) | **New** | Stage 04 also runs the fixture-backed open-rails AB/BA proof (`generate_open_rails_abba_proof.build_fixture_proof`). It is one of three release-admission-gated stages (`run_sanity_pipeline.py` line 112). While the release is not admitted it reports `NOT_ADMITTED` (exit 3), not PASS. At `84d6d1ca` the release is admitted, and the stage-04 validator ran in memory and passed |
| Authority citation "HDE Governance §9.7.3" | Minor | §9.7.3 covers Product Owner-owned planning artifacts. The addendum form is set by Change Process Guide §0.1A, and HDE Build Notes publication is the Product Owner's. The brief's conclusion stands |

Two statements in the drafts change under the recommendations:

- **T-01, HDE Governance v2.8.10 §12.2** (draft line 4321) keeps "the lower-case marker `artifacts/cards/a3/IDENTITY_OK.txt` … as history". It does not repeat the false date.
- **T-05, HDE Mechanics Guide v3.5.10 §37.7** says the marker "is not GATE:CORE-DET evidence, and no record may cite it as current two-run identity proof". That follows from the earlier addendum's R-1, so it is a faithful drain, but it conflicts with Option A. The same section lists `artifacts/cli/ab.json`, `ba.json` and `summary.json` as the AB↔BA goldens. Those are a different family (`tools/cli/generate_cli_conformance_artifacts.py`); the stage-04 outputs are under `audit/gates/parity/reader_cli/` and `audit/gates/determinism/`.

## 4. Q-2: the a3 marker and release-sanity stage 04

### 4.1 What stage 04 is

Release-sanity stage 04, "Reader-to-CLI, AB-to-BA, two-run, and preimage checks", is the release lane's determinism proof.

1. It resolves two complete fixture charts (`fixtures/charts/alice.json` and `bob.json`) through the CLI file path.
2. It scores them with `engine.compat.compute.evaluate_pair` and emits through the single Reader emitter.
3. It runs `hdctl showcompat --dump-reader` as a subprocess for the CLI side.
4. It requires six predicates to be true: Reader↔CLI bytes, AB↔BA bytes, two-run bytes, preimage hash, canonical re-serialization and the canonical gate check.

`--check` then requires each of the six stored outputs to equal the fresh build byte for byte. The a3 marker is one of those six outputs.

### 4.2 What breaks if nothing changes

- The gate's own definition names its evidence as "Preimage recompute logs; AB/BA and two-run byte-compare goldens" (HDE Governance §12.1). Stage 04 produces exactly that, on the real compat path, and CI runs it on every compat-path change. Without a change, canon leaves this proof out of the gate's evidence.
- Canon also calls one of its outputs history (the T-01 draft), or says no record may cite it (the T-05 draft).
- A reviewer who follows canon would treat a current, passing, CI-run determinism proof as non-evidence.

### 4.3 2b: recommend Option A, with one precision

Stage 04 counts as GATE:CORE-DET closed-rails evidence for a commit only when it passes on that commit. That means either:

- stage 04 reports PASS; or
- `generate_determinism_gate_proofs.py --check` exits 0.

`NOT_ADMITTED` is not a pass. The stored outputs are evidence only for a commit where `--check` exits 0. The a3 marker counts only as one of the six outputs and proves nothing on its own.

`tests/evidence/test_determinism_gate_proofs.py` joins the owner tests, so a change that weakens the generator needs its owner's review, like any other gate test.

**Why A.**

- It meets the earlier addendum's own test, "GATE:CORE-DET evidence is the real compat path".
- It meets the gate's stated evidence form.
- It costs nothing: CI already runs it, and no code changes.

**Limit.** Stage 04 proves determinism on two fixture charts. It is not a correctness proof for compat scores, and it does not replace the five owner tests or the live compat test.

**Option B** fixes the false sentence but leaves the proof unnamed.

**Option C** leaves canon false.

### 4.4 2a: recommend correcting the fact and the status

Correct the date and the commit. Also correct the conclusion: the lower-case marker is not history but a current output that is checked on every release-lane run.

The upper-case path `artifacts/cards/A3/IDENTITY_OK.txt` and `scripts/make_compat_determinism_artifacts.py` stay retired.

HDE Build Notes addenda are not rewritten in place. After the drain, the earlier addendum's content lives in HDE Governance and HDE Mechanics Guide, so 2.1 states the corrected fact against those homes.

## 5. Q-1: the §37.17 snapshot root

### 5.1 What §37.17 is

§37.17 is HDE Mechanics Guide's pointer to where architecture evidence lives. A QA, close or audit reader uses it to find the snapshot to cite.

### 5.2 What breaks

- **Today**, §37.17 names nothing usable.
- **Under plain Option B**, it would name a stored snapshot that fails its own currency check (`--check` exits 1, `STALE`). No CI check catches that. A reader following canon would cite a stale file as current architecture evidence.

### 5.3 Recommend Option B, with a currency condition

§37.17 names:

- the governed snapshot `artifacts/architecture/architecture_snapshot.keys_only.json` and its path proof, whose binding HDE Schemas & Artifacts owns;
- its producer, `tools/evidence/generate_architecture_snapshot.py`.

It also states three conditions:

- The stored snapshot is current for a commit only when `--check` exits 0 on that commit. No record may cite it as current architecture proof otherwise.
- Product CI's `tests/evidence/test_architecture_snapshot.py` checks the current analysis, not the stored file.
- `_arch/<EPIC_ID>_<STAMP>/<file>`, written by `scripts/architecture_capture.sh`, is legacy capture kept as history.

**Why.** B is right for the brief's reasons. The currency condition stops canon from vouching for a file that fails its own check.

**The other options.** Option A names a family whose existence test is retired and whose newest snapshot is from 2025-10-25. Option C names a path that does not exist.

**The decision goes in 2.1.** The currency condition is an evidence rule, so it belongs in HDE Build Notes. That gives the §37.17 repair a source, which T-05 lacked ("no source establishes the intended text"). If the Product Owner chooses plain B, R-3 drops its "Currency" bullet. If the Product Owner chooses A, R-3 names `_arch/<EPIC_ID>_<STAMP>/<file>` instead.

**Not fixed here.** Refreshing the stale snapshot is a development change: FND-007, CL-40 CRD candidate item 12(a). HDE Build Checklist Distillation line 859 still says the snapshot is "revalidated through release-sanity stage 10". In the current chain, stage 10 is "Configured-v2 mapped-cache behavior". Item 12(a) records this already.

## 6. Placement and the GTWPE drafts

Nathan placed the addendum: number 2.1, in the next PF10 base version after v14.0.5 drains. Two consequences follow.

**The drafts proceed as written.** The T-01 and T-05 drafts drain v14.0.5 as published, and that drain is faithful. Once 2.1 is published, it governs the overlapping text in HDE Governance §12.2, Appendix B.2, D.1 and D.3 and HDE Mechanics Guide §37.7 and §37.17 until a later drain. The authority for that is HDE Build Notes, "PF10 authority" and "Individual-addendum supersession".

**2.1 stands alone.** The current-version rule forbids reading an older base version once a newer one exists. So 2.1 states its rules against the permanent homes, and names the earlier addendum only as the origin of the corrected fact, by date and title, without a version number. This follows HDE Build Notes' titles-only rule.

**The form follows Change Process Guide §0.1A.**

- One H2 numbered 2.1, with only H3 subordinate headings.
- Declarative language.
- No role-addressed publication, routing or record-maintenance instructions.

**Why no ADR.** Change Process Guide §1.0.5 requires an ADR for a CRD that changes canon. This is a Product Owner decision outside a CRD, as the earlier addendum was.

**Two fields need the Product Owner's decision before publication.** The draft marks them `<…>`: the decision date and the decision quote. Everything else is final text.

## 7. Draft HDE Build Notes addendum 2.1

The text between the two rules below is the addendum, ready to paste into the next PF10 base version.

---

## 2.1 GATE:CORE-DET closed-rails evidence includes release-sanity stage 04, the lower-case a3 marker is a current checked output, and HDE Mechanics Guide §37.17 names the governed architecture snapshot

Timestamp: 110226 03:17 (UTC). Details:

* What this records. The Product Owner's decision of \<decision date\> on two items found while draining into HDE Mechanics Guide. No code, test or evidence changes.  
* What this decides.  
  * Release-sanity stage 04 is GATE:CORE-DET closed-rails evidence (R-1).  
  * The lower-case a3 marker's history is corrected, and so is its status (R-2).  
  * HDE Mechanics Guide §37.17 names the governed architecture snapshot, with a currency condition (R-3).

### Decision and approval status

* Decision. The Product Owner \<decision quote\>, adopting the recommendations of review record HDE-GTWPE-T05-ISIS-REVIEW v1.0: option A for stage 04 and the a3 marker, and option B with the currency condition for §37.17.  
* Status. Proposed. The rules take effect as canon when this addendum is published in HDE Build Notes.  
* Relation to other canon.  
  * The GATE:CORE-DET pass conditions in HDE Governance §12.1 are unchanged.  
  * Also unchanged are the five compat-path owner tests, the live compat test as open-rails evidence, and the retired entries. The retired entries include `artifacts/cards/A3/IDENTITY_OK.txt` and `scripts/make_compat_determinism_artifacts.py`.  
  * This addendum supersedes only the following:  
    * in HDE Governance §12.2, Appendix B.2, D.1 and D.3, the closed-rails GATE:CORE-DET evidence lists, to the extent R-1 extends them;  
    * in those sections and in HDE Mechanics Guide §37.7, any statement that the lower-case marker `artifacts/cards/a3/IDENTITY_OK.txt` is kept only as history, is not GATE:CORE-DET evidence, or may not be cited as two-run identity proof;  
    * the "Snapshot root" entry of HDE Mechanics Guide §37.17.  
  * Every other entry in those sections still governs.

### The facts that prompted it

All read on main at `84d6d1ca`.

* The lower-case a3 marker is current, not frozen.  
  * `artifacts/cards/a3/IDENTITY_OK.txt` last changed on 2026-07-13, in HDE-EPIC038 PR-02 (`ceefe4f5`). The change before that was HDE-EPIC024 (`16f4215c`, 2026-01-22).  
  * The earlier HDE Build Notes addendum of 2026-11-01, "GATE:CORE-DET evidence is the real compat path" (FND-005), called it "a frozen marker last changed by HDE-EPIC024 (2026-01-22)". That was the upper-case path's history, applied to the lower-case copy.  
  * The marker is one of six outputs of `tools/evidence/generate_determinism_gate_proofs.py`. The other five are `audit/gates/parity/reader_cli/ab.json`, `ba.json` and `summary.json`, `audit/gates/determinism/abba.bytes` and `audit/gates/determinism/tworun_identity.sha256`.  
* Release-sanity stage 04 runs the real compat path.  
  * Stage 04 is "Reader-to-CLI, AB-to-BA, two-run, and preimage checks".  
  * It resolves `fixtures/charts/alice.json` and `fixtures/charts/bob.json` through the CLI file path, scores them with `engine.compat.compute.evaluate_pair`, and emits through the single Reader emitter. It runs `hdctl showcompat --dump-reader` as a subprocess for the CLI side.  
  * It requires six predicates: Reader↔CLI bytes, AB↔BA bytes, two-run bytes, preimage hash, canonical re-serialization and the canonical gate check.  
  * `generate_determinism_gate_proofs.py --check` also requires each stored output to equal the fresh build byte for byte.  
  * Stage 04 is release-admission-gated. While the active release is not admitted, it reports `NOT_ADMITTED`, not PASS.  
* CI runs it.  
  * The identity closure lists the generator with `--check`.  
  * CI's release lane builds the release attestation. That runs the closure and then the full release-sanity pipeline.  
  * The CI classifier sends changes to `engine/compat/compute.py`, `engine/core/compute_core.py`, `engine/magic10/composite.py`, `engine/cli/main.py`, `engine/reader_v1/emitter.py` and the generator to the release lane.  
  * The generator's CI owner test is `tests/evidence/test_determinism_gate_proofs.py`.  
* It passes. These checks ran under closed rails, read-only:  
  * `--check` exits 0;  
  * the owner test gives 15 passed;  
  * the release is admitted, and the stage-04 validator passes.  
* It was not named. GATE:CORE-DET's closed-rails evidence named five owner tests and omitted stage 04, although stage 04 produces the gate's stated evidence form: "Preimage recompute logs; AB/BA and two-run byte-compare goldens" (HDE Governance §12.1).  
* HDE Mechanics Guide §37.17 named no usable snapshot root.  
  * Its one entry read `audit/gates/arch/*arch/\*\/\`. No path, code or canon uses the prefix `audit/gates/arch/`.  
  * The governed snapshot is `artifacts/architecture/architecture_snapshot.keys_only.json`. HDE Schemas & Artifacts owns its binding, `epic038.pr04.architecture_snapshot`.  
  * `python tools/evidence/generate_architecture_snapshot.py --check` exits 1 with `STALE:artifacts/architecture/architecture_snapshot.keys_only.json` (FND-007).  
  * Product CI's `tests/evidence/test_architecture_snapshot.py` passes (5 passed). It checks the current analysis, not the stored file.  
  * `_arch/` holds 147 files of legacy capture written by `scripts/architecture_capture.sh`. The newest is stamped 2025-10-25. Their existence test was retired on 2026-10-13.

### R-1 — Release-sanity stage 04 is GATE:CORE-DET closed-rails evidence

GATE:CORE-DET closed-rails evidence is the five compat-path owner tests named in HDE Governance §12.2, plus the following:

* Release-sanity stage 04, "Reader-to-CLI, AB-to-BA, two-run, and preimage checks", for a commit on which it passes. A pass means either:  
  * stage 04 reports PASS; or  
  * `python tools/evidence/generate_determinism_gate_proofs.py --check` exits 0.  
  `NOT_ADMITTED` is not a pass.  
* The generator's six stored outputs, for a commit on which `--check` exits 0:  
  * `audit/gates/parity/reader_cli/ab.json`, `ba.json` and `summary.json`;  
  * `audit/gates/determinism/abba.bytes`;  
  * `audit/gates/determinism/tworun_identity.sha256`;  
  * `artifacts/cards/a3/IDENTITY_OK.txt`.  
  The marker counts only as one of these six outputs. Alone, it is not proof.  
* The owner test `tests/evidence/test_determinism_gate_proofs.py`, run as CI selects it. A change that removes or weakens it needs its owner's review, like any other gate test.

Stage 04 proves AB↔BA, two-run and preimage identity on two fixture charts. It does not prove compat score correctness. It does not replace the owner tests, or the live compat test as open-rails evidence.

### R-2 — The lower-case a3 marker: corrected fact and status

* Corrected fact. `artifacts/cards/a3/IDENTITY_OK.txt` last changed on 2026-07-13, in HDE-EPIC038 PR-02. The statement that it is a frozen marker last changed by HDE-EPIC024 is withdrawn.  
* Status. It is a current output of `tools/evidence/generate_determinism_gate_proofs.py`, and the identity closure checks it. It is GATE:CORE-DET evidence only as R-1 states.  
* Unchanged. `artifacts/cards/A3/IDENTITY_OK.txt` and `scripts/make_compat_determinism_artifacts.py` remain retired, and no record may cite them as current proof.

### R-3 — HDE Mechanics Guide §37.17 snapshot root

* Snapshot root. The governed architecture snapshot is `artifacts/architecture/architecture_snapshot.keys_only.json`, with its sibling `artifacts/architecture/architecture_snapshot.keys_only.json.path_proof.txt`.  
  * Its producer is `tools/evidence/generate_architecture_snapshot.py`.  
  * HDE Schemas & Artifacts owns its binding, and HDE Architecture owns architecture meaning.  
* Currency.  
  * The stored snapshot is current for a commit only when `python tools/evidence/generate_architecture_snapshot.py --check` exits 0 on that commit.  
  * No record may cite it as current architecture proof for a commit on which that check does not exit 0.  
  * `tests/evidence/test_architecture_snapshot.py` checks the current analysis, not the stored snapshot.  
* Legacy capture. `_arch/<EPIC_ID>_<STAMP>/<file>`, written by `scripts/architecture_capture.sh`, is kept as history. It is not current architecture evidence.  
* The damaged entry is replaced by this text, not reconstructed. No `audit/gates/arch/` path exists.

### Scope, exclusions and nonclaims

* Scope: GATE:CORE-DET closed-rails evidence; the lower-case a3 marker's history and status; the §37.17 snapshot root and its currency condition.  
* Excluded:  
  * the gate's pass conditions;  
  * any code, test or artifact change;  
  * refreshing the stale architecture snapshot (FND-007, a CRD candidate);  
  * whether the compat scores are right;  
  * conjunction;  
  * the narrative pack path naming difference between HDE Architecture and HDE Narratives Guide.  
* Nonclaims. This record makes no QA verdict, acceptance, Ops result, deployment or PF09 movement, and drains no canon. The checks it cites were run for the review record, not as QA.

### Dependencies and unresolved obligations

* Drainage into permanent canon has not been done. The targets are:  
  * HDE Governance §12.2, Appendix B.2, Appendix D.1 and Appendix D.3;  
  * HDE Mechanics Guide §37.7 and §37.17.  
* FND-007 is open. Until `generate_architecture_snapshot.py --check` exits 0 on a cited commit, R-3 bars citing the stored snapshot as current architecture proof for that commit.

### Evidence

* Review record: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-isis-review.gtwpe-20261101-pf10-v14-0-5.md`, which responds to the T-05 review brief beside it.  
* Marker history: `git log` for `artifacts/cards/a3/IDENTITY_OK.txt` (`ceefe4f5`, `16f4215c`) and `artifacts/cards/A3/IDENTITY_OK.txt` (`16f4215c`, `c4a73ae0`).  
* Stage 04 wiring:  
  * `tools/evidence/run_sanity_pipeline.py` (stage names; `validate_current_reader_cli_determinism`; admission-gated stages);  
  * `tools/evidence/regenerate_identity_closure.py` (step `reader_cli_determinism`);  
  * `tools/evidence/build_release_attestation.py` (closure, closure `--check`, release sanity);  
  * `.github/workflows/ci.yml` (`release_lane`);  
  * `ci/checks/classify_ci_changes.py` (lane and owner-test mapping).  
* Checks on main at `84d6d1ca` under closed rails, read-only:  
  * determinism `--check` exit 0;  
  * `tests/evidence/test_determinism_gate_proofs.py` 15 passed;  
  * release admitted, and the stage-04 validator passed;  
  * architecture `--check` exit 1 `STALE`;  
  * `tests/evidence/test_architecture_snapshot.py` 5 passed.  
* FND-007: CL-40 cycle gap scan v1.0, item 12(a).

---

## 8. Canon and sources relied on

Read on `main` `84d6d1ca`:

- **Canon:**
  - PF04-Canon-HDE-Governance v2.8.8: §3.4; §9.7.3; §12.1; §12.2; Appendix B.2, D.1 and D.3.
  - PF06-Canon-Change-Process-Guide v2.5.5: §0.1A, the paragraph on agent-authored HDE Build Notes addenda; §1.0.5.
  - PF10-HDE-Build-Notes v14.0.5: front matter rules 1–9; template; addendum 2.16 in full.
  - PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7: line 3354.
  - PF14-Canon-HDE-Mechanics-Guide v3.5.9: §37.7; §37.17.
  - PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.9: lines 857–861.
- **Code and tests:**
  - `tools/evidence/generate_determinism_gate_proofs.py`, `run_sanity_pipeline.py`, `regenerate_identity_closure.py`, `build_release_attestation.py`, `generate_open_rails_abba_proof.py` and `generate_architecture_snapshot.py`;
  - `ci/checks/classify_ci_changes.py` and `.github/workflows/ci.yml`;
  - `tests/evidence/test_architecture_snapshot.py` and `tests/retired_tests.md`;
  - `scripts/architecture_capture.sh` and `scripts/card_close.sh`;
  - `git ls-files _arch`.
- **Records:** `docs/ephemeral/HDE-EPIC041-CL-40-cycle-gap-scan-v1.0.md`.

On branch `claude/gtwpe-triage-authoring-j94ewf` at `97938c44`:

- the brief;
- `PF04/PF04-Canon-HDE-Governance-v2.8.10.md` §12.2, B.2, D.1 and D.3;
- `PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md` §37.7 and §37.17;
- `LEDGER.md`.

No live, production or vendor behavior was observed. Nothing under `docs/pfcanon/` was edited.
