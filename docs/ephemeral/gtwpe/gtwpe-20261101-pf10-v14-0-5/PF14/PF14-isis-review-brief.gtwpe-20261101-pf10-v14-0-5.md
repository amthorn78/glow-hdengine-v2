---
artifact_type: REVIEW_BRIEF
artifact_id: HDE-GTWPE-T05-ISIS-REVIEW-BRIEF
artifact_version: "1.0"
subject: Two items found while draining HDE Build Notes v14.0.5 into the HDE Mechanics Guide (GTWPE task T-05) that need a decision before canon can state them correctly
requested_by: Nathan / Product Owner, 2026-11-02 ("give me a brief on those items for Isis, I want them reviewed")
addressed_to: Isis, Lead Developer
decision_owner: Product Owner. Isis reviews and recommends, and drafts any canon change (HDE Governance §9.7.3)
author: GTWPE T-05 document session (https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z)
repository_head_read: origin/main 84d6d1cad95c67788336d174dc4b8922d9bb0cb2; checks run at branch head 3af9664, whose code is identical to main outside docs/ephemeral/
source_read: docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md, addenda 2.15 and 2.16 in full
created_at: 2026-11-02T03:01:00Z
---

# T-05 open items: architecture capture root and GATE:CORE-DET stage 04 (review brief)

## 1. Review requested

| # | Item | Question | What breaks if nothing changes | Author's suggestion |
| :- | :- | :- | :- | :- |
| Q-1 | HDE Mechanics Guide §37.17 "Architecture capture" | Which path should "Snapshot root" name? | PF14 names no usable snapshot root. The line is unreadable and cannot be repaired without a decision | B: name the current governed snapshot and keep `_arch/` as history |
| Q-2 | HDE Build Notes 2.16 and GATE:CORE-DET evidence | (a) Correct 2.16's fact about the a3 marker? (b) Is release-sanity stage 04 GATE:CORE-DET evidence? | 2.16's false fact carries into every drain. A passing, CI-run, real-compat-path determinism proof stays outside the gate's evidence while canon calls part of its output frozen | A: correct the fact and add stage 04 to the closed-rails evidence |

The two items are independent. Q-2 matters more: it is about which evidence proves a required-now gate.

## 2. Authority and output

- **Ownership.** Both decisions are the Product Owner's. Agents may draft; the Product Owner is the final maintainer (HDE Governance §9.7.3). 2.16 is a Product Owner decision, so only the Product Owner can correct or extend it.
- **Requested output.** One review record under `docs/ephemeral/`, with a decision or recommendation for each question. Where a decision changes canon, include a draft HDE Build Notes addendum in the addendum form (Change Process Guide §0.1A, the paragraph on agent-authored HDE Build Notes addenda; §1.0.5 for canon changes).
- **Downstream.** Two unpublished GTWPE drafts would follow the decision: HDE Governance v2.8.10 (task T-01) and HDE Mechanics Guide v3.5.10 (task T-05). Both are on branch `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826. Neither is published.
- **Not requested.** No code, test or evidence change. No deletion of the generator, the marker or any capture; 2.16 R-2 keeps them. No edit to `docs/pfcanon/`.

## 3. Q-1 — the §37.17 snapshot root

**What it is.** HDE Mechanics Guide §37.17 "Architecture capture" has one list item under "Snapshot root". Its raw bytes are `audit/gates/arch/*arch/\\*\\/\\`, which render as `audit/gates/arch/*arch/\*\/\`. It names no usable path. The T-05 drain repaired lost placeholders in six other places in PF14, but not this one: no source establishes the intended text.

**Facts on `main`.**

- `scripts/architecture_capture.sh` writes snapshots to `_arch/${EPIC_ID}_${STAMP}/` (line 6): `routes.txt`, `imports.adapters.txt`, `imports.core.txt`, `imports.server.txt`, `emit.dumps.txt`, `tree.txt`, `status.txt`, and optionally `byte_parity.txt`. `scripts/card_close.sh` calls it (line 147).
- 147 files are tracked under `_arch/`, in 21 snapshot directories named from `epic003_20251017_210542` to `HDE-EPIC005_20251025T123345Z`. Nothing newer exists.
- The damaged bytes fit that pattern if a converter turned underscores into emphasis asterisks and dropped the `<...>` placeholders: `_arch/<EPIC_ID>_<STAMP>/<file>` becomes `*arch/\\*\\/\\`. No tracked path, code or canon names the prefix `audit/gates/arch/`.
- `tests/arch/test_arch_capture_exists.py` checked only that a frozen `_arch/HDE-EPIC005_*` snapshot exists. It was retired on 2026-10-13 and replaced by `tests/evidence/test_architecture_snapshot.py` (`tests/retired_tests.md` line 14).
- The current governed architecture snapshot is `artifacts/architecture/architecture_snapshot.keys_only.json`, with its path proof. `tools/evidence/generate_architecture_snapshot.py` writes it. HDE Schemas & Artifacts lists it as `epic038.pr04.architecture_snapshot` (line 3354), and HDE Build Checklist Distillation calls it "the governed snapshot" (line 859). The current 15-stage release-sanity chain has no architecture stage. Architecture "is protected independently in product CI" (`tools/evidence/run_sanity_pipeline.py` line 96), by `tests/evidence/test_architecture_snapshot.py`.

**Options.**

| Option | §37.17 "Snapshot root" names | Cost |
| :- | :- | :- |
| A | `_arch/<EPIC_ID>_<STAMP>/<file>`, written by `scripts/architecture_capture.sh`, without the `audit/gates/arch/` prefix | Restores the pattern the bytes suggest, but names a legacy family whose existence test is retired and whose newest snapshot is stamped 2025-10-25 |
| B | The current governed snapshot `artifacts/architecture/architecture_snapshot.keys_only.json`, owned by HDE Schemas & Artifacts. `_arch/<EPIC_ID>_<STAMP>/` is named as the legacy capture, kept as history | Changes what §37.17 points to, so it is a decision, not a repair |
| C | `audit/gates/arch/_arch/<EPIC_ID>_<STAMP>/<file>`, the literal byte reconstruction | Names a path that does not exist |

**Author's suggestion (not binding): B.** §37.17 sits among PF14's evidence-home sections, and the governed snapshot is the one current architecture evidence. B keeps the legacy family as history, which is what the test retirement already treats it as.

**Canon effect.** A wording change in HDE Mechanics Guide §37.17 only, made as a later PF14 redline. No Build Notes addendum is needed unless the decision changes evidence policy.

## 4. Q-2 — the a3 marker and release-sanity stage 04

**What 2.16 says.**

- R-1: GATE:CORE-DET evidence is the real compat path, in two parts. Closed rails: five named CI owner tests. Open rails: each run of the 2.15 live compat test.
- R-2: retires listed entries, including upper-case `artifacts/cards/A3/IDENTITY_OK.txt`, and keeps "the lower-case a3 marker" as it is, "as history".
- "The facts that prompted it": the lower-case copy "is a frozen marker last changed by HDE-EPIC024 (2026-01-22)".

**What is true on `main`.**

- **The marker is not frozen.**
  - `artifacts/cards/a3/IDENTITY_OK.txt` last changed on 2026-07-13, in HDE-EPIC038 PR-02 (`ceefe4f5`). The HDE-EPIC024 commit of 2026-01-22 (`16f4215c`) is the change before that (GitHub commit history for the path).
  - Its content reads: `IDENTITY_OK` / "HDE-EPIC038 PR-02 deterministic predicate evidence only; no acceptance token satisfaction claimed."
- **A current generator writes it.** It is one of six outputs of `tools/evidence/generate_determinism_gate_proofs.py`, release-sanity stage 04 "Reader-to-CLI, AB-to-BA, two-run, and preimage checks".
  - HDE-EPIC040 PR-04 (#467, `cd6f9e6c`) rewrote the generator onto the real compat path. Two complete fixture charts (`fixtures/charts/alice.json`, `fixtures/charts/bob.json`) are resolved through the CLI file path and scored by `engine.compat.compute.evaluate_pair`, then emitted by the single Reader emitter. `hdctl showcompat --dump-reader` runs as a subprocess for the CLI side.
  - The other five outputs are `audit/gates/parity/reader_cli/ab.json`, `ba.json` and `summary.json`, `audit/gates/determinism/abba.bytes` and `audit/gates/determinism/tworun_identity.sha256`.
  - It writes nothing unless every predicate passes.
- **It runs today.**
  - `tools/evidence/run_sanity_pipeline.py` calls it in stage 04 (`validate_current_reader_cli_determinism`).
  - The identity closure lists it (`tools/evidence/regenerate_identity_closure.py` lines 231–233), and the release attestation builder runs that closure in CI's release lane.
  - Its CI owner test is `tests/evidence/test_determinism_gate_proofs.py` (`ci/checks/classify_ci_changes.py` line 670).
- **It passes.** These are this session's local checks under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=test`), on code identical to `main` `84d6d1c`:
  - `generate_determinism_gate_proofs.py --check` exits 0 ("determinism gate proofs check ok");
  - its owner test passes (15 passed);
  - all six predicates are true: `reader_cli_byte_identity`, `abba_byte_identity`, `two_run_byte_identity`, `preimage_hash_match`, `canonical_reserialization` and `canonical_gate_check`.
  - The first attempt failed only on `canonical_gate_check`, because Flask was not installed; after installing the repository's requirements, the check passed.
  - These are local results, not CI's result and not QA.
- **It fits the gate's own definition.** HDE Governance §12.1 gives GATE:CORE-DET's evidence as "Preimage recompute logs; AB/BA and two-run byte-compare goldens". Stage 04 produces exactly those, from the real compat path.
- **Neither 2.16 nor any draft names it.** R-1's closed-rails list is the five owner tests:
  - `tests/core/test_engine_core_abba.py`;
  - `tests/core/test_engine_core_determinism.py`;
  - `tests/compat/test_evaluate_pair_eligibility.py`;
  - `tests/compat/test_compat_public_ab_ba_identity.py`;
  - `tests/cli/test_showcompat_parity_and_identity.py`.

  Stage 04 is not in that list. The T-01 draft of HDE Governance §12.2 (v2.8.10) follows R-1 and omits it as well.

**Questions.**

- 2a. Should 2.16's statement that the marker is "frozen" and "last changed by HDE-EPIC024" be corrected?
- 2b. Is stage 04 (the generator and its six outputs) GATE:CORE-DET evidence under closed rails, alongside the five owner tests?

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | Correct the fact, and add stage 04 to R-1's closed-rails GATE:CORE-DET evidence. The a3 marker counts only as one output of that family, not as standalone proof | The one release-lane AB/BA, two-run and preimage proof on the real compat path is named as gate evidence. HDE Governance §12.2, B.2, D.1 and D.3 and HDE Mechanics Guide §37.7 drain the change. No code change |
| B | Correct the fact only. Stage 04 stays release-sanity evidence, not GATE:CORE-DET evidence | Smallest change; canon stops saying something false. The gate's closed-rails evidence stays the five owner tests |
| C | No change | 2.16's false fact remains canon until someone corrects it |

**Author's suggestion (not binding): A.** 2.16's own test is "GATE:CORE-DET evidence is the real compat path", and stage 04 runs that path. It also meets HDE Governance §12.1's stated evidence form, and CI already runs it. Under B or C, a passing proof of the gate stays unnamed while a draft calls part of its output history.

**Canon effect.**

- Under A or B: a new HDE Build Notes addendum correcting 2.16's fact, and under A also extending R-1. HDE Build Notes addenda are not rewritten in place.
- Drainage, under A: HDE Governance §12.2, Appendix B.2, D.1 and D.3; HDE Mechanics Guide §37.7. Under B: only the drafts' wording about the marker. The T-01 and T-05 GTWPE drafts can be revised once the addendum exists.

## 5. Not in this brief

| Item | Why not here | Owner |
| :- | :- | :- |
| HDE Architecture line 1056 writes the narrative pack path as `/narratives/<pack_sha>/<OBJECT_KEY>`; HDE Narratives Guide line 845 and HDE Schemas & Artifacts line 1992 write `<PACK_MEMBER>` | A naming difference in another document. PF14 now uses the Narratives Guide's form. It can be added as Q-3 if wanted | Product Owner |
| Other rendered escapes in PF14 left as they are | Their meaning survives; no decision is needed (T-05 preparation proof log §10) | None |

## 6. Facts checked for this brief

- `main` at `84d6d1c`. Branch head `3af9664` differs from it only under `docs/ephemeral/` (`git diff --name-only origin/main HEAD -- . ':!docs/ephemeral'` is empty).
- Read on `main`:
  - `scripts/architecture_capture.sh`, `scripts/card_close.sh` and `tests/retired_tests.md`;
  - `git ls-files _arch`;
  - `tests/evidence/test_architecture_snapshot.py`;
  - `tools/evidence/generate_determinism_gate_proofs.py`, `tools/evidence/run_sanity_pipeline.py`, `tools/evidence/regenerate_identity_closure.py` and `ci/checks/classify_ci_changes.py`;
  - `artifacts/cards/a3/IDENTITY_OK.txt`.
- GitHub commit history for `artifacts/cards/a3/IDENTITY_OK.txt` and for the generator. The local clone is shallow and cannot show it.
- Run locally under closed rails, read-only:
  - `generate_determinism_gate_proofs.py --check` (exit 0);
  - `tests/evidence/test_determinism_gate_proofs.py` (15 passed);
  - `run_canonical_json_gate.py --check-only` (exit 0).
  - The working tree stayed clean.
- No live, production or vendor behavior was observed.

## Canon relied on

Read on `main` at `84d6d1c`:

- PF04-Canon-HDE-Governance v2.8.8: §9.7.3; §12.1 "GATE:CORE-DET — Determinism and identity"; §12.2; Appendix B.2, D.1 and D.3.
- PF06-Canon-Change-Process-Guide v2.5.5: §0.1A, the paragraph on agent-authored HDE Build Notes addenda; §1.0.5.
- PF10-HDE-Build-Notes v14.0.5: addendum 2.15 R-1; addendum 2.16 in full.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7: the entry `epic038.pr04.architecture_snapshot` (line 3354); line 1992.
- PF14-Canon-HDE-Mechanics-Guide v3.5.9: §37.7; §37.17.
- PF09.6-Canon-HDE-Build-Checklist-Distillation v1.1.9: line 859.
- PF02-Canon-HDE-Architecture v2.4.7: line 1056. PF17-Canon-HDE-Narratives-Guide v1.5.4: line 845.

In-flight documents, on branch `claude/gtwpe-triage-authoring-j94ewf`:

- `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, rows T-01 and T-05;
- `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md` §12.2 (T-01 draft);
- `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/`: the T-05 redlines r3, the v3.5.10 draft and their proof logs.
