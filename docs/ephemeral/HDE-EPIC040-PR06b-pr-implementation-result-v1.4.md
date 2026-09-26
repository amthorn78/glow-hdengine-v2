# HDE-EPIC040-PR06b — PR Implementation Result v1.4 (PR-35)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-RESULT` v1.4, the PR-35 phase record at the final PR-35 push. It supersedes only v1.3's outcome, *Final head* condition, readiness table and continuation. v1.3 (`docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.3.md`, SHA-256 `1a653d08caa983fddf36c7277033c2b337ad2472d85b3297c11b7474dc456c79`) is unchanged as issued and remains the record of the second Product Owner-directed PF10 operation. v1.2 remains the record of the first PF10 operation and the v13.3.6 read. v1.1 remains the record of CR-01, PR-35 local validation and CI on `85e702b3`. v1.0 remains the implementation record |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A) with a release re-cut to `1.3.0` |
| Change | `EPIC / HDE-EPIC040`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`); PR06b rescope decision v1.0 |
| Producer | the dedicated PR-35 session for HDE-EPIC040-PR06b (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06b / PR-35`; `context_conflict: NONE`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`); `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `MERGE_PENDING` — Ready to merge, on the condition under *Final head* (§1) |
| Prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 (`https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`; Notion read only). Primary skill: `glow-hde-pr-development` 1.3.1 |
| Repository / branch / PR | `amthorn78/glow-hdengine-v2` / `claude/focused-heisenberg-91y3cn` / [#513](https://github.com/amthorn78/glow-hdengine-v2/pull/513) |
| Base | merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643`; `origin/main` is still `d031f94` |
| Commits | PR-30: `acae4c637e2ce8c9e987953bcbe284f7e03719c9` (implementation) and `85e702b3…` (records). PR-35: `e34541b0…` (records v1.1); `f9a65523…` (PF10 v13.3.6 added, v13.3.5 removed); `20ca1c35…` (records v1.2); `43aa2d6b…` (PF10 v13.3 to v13.3.4 removed); `7309f2bf597902a000d008d46ff1e5dbdccc7c8c` (records v1.3); and the commit adding this file (records v1.4). A commit cannot embed its own SHA, so the v1.4 records commit's SHA and the remote head after its push are recorded in the PR #513 body and the PR-35 return |
| Recorded by | the dedicated PR-35 session, 2026-09-26 (UTC) |

## 1. Outcome

**`MERGE_PENDING` — Ready to merge,** on the condition under *Final head*. This record is historical pre-merge evidence. It does not claim the PR is merged. It is not a QA verdict, acceptance, release activation, PF09 movement, OPS01 attestation, C040-08 drainage, deployment or closure. Nathan / Product Owner merges manually as a separate action. Nothing here enables, schedules or requests a merge.

- **Since v1.3.**
  - `43aa2d6b` and the v1.3 records commit `7309f2b` were pushed as one fast-forward and read back.
  - CI run `36256453481` on `20ca1c3` concluded `cancelled` at 16:50:04Z, superseded by that push.
  - Codex's Code Review of `7309f2b` completed at 16:53:40Z with one new P1 finding, CR-02 (§2), dispositioned here with the class it belongs to (§3).
  - CI run `36256852430` on `7309f2b` was still running when this push was prepared, and this push supersedes it.
- **Candidate code unchanged.** PR-35 changed no code, test, evidence or roster byte. Every commit after `acae4c6` touches only `docs/ephemeral/` or `docs/pfcanon/`.
- **Final head.** This record's commit adds only `docs/ephemeral/` records above `7309f2b`. After the push, the following are read and recorded in the PR #513 body and the PR-35 return:
  - the pushed head's exact-head CI (the same four lanes on the same code tree);
  - Codex's review of that head;
  - the thread state and mergeability.

  The return states `MERGE_PENDING` only if CI is green, no unresolved thread or new finding outside §3's class exists, and the PR stays open and mergeable. Otherwise this result no longer stands and a later version replaces it.

## 2. CR-02: finding and disposition

| Field | Value |
| --- | --- |
| Reviewer / surface | `chatgpt-codex-connector[bot]`, Code Review `5326634675` (`COMMENTED`, 2026-09-26T16:53:41Z) on `7309f2bf59`; thread `PRRT_kwDOP103ks6mSUll` (`discussion_r4112055897`), P1 |
| Location | `artifacts/evidence_index.jsonl:453`, the Machine Mirror row for `audit/gates/parity/reader_cli/ab.json` |
| Finding | "Preserve the original EPIC038 snapshot bytes". The diff rewrites the `reader_cli/ab.json` payload from release `9f962c…` to `52be45…`, while the Mirror row still identifies it as an HDE-EPIC038 snapshot produced on 2026-07-12, so a September 1.3.0 result reads as the July capture. Proposed fix: retain the original snapshot, and publish the current-release capture under a new evidence identity. It cites `AGENTS.md` L114–L117 |
| Disposition | **Not changed. It is out of scope for PR06b, and it belongs to the same class as CR-01 (§3).** The regeneration is canon-directed and approved scope. The proposed revert fails the owner's check and the updater's check. The labels are pre-existing, and the alternative is an evidence-model change for its owners (O-P06b-17) |

Evidence:

- **A release-bound derivative regenerated by its owner.**
  - `tools/evidence/regenerate_identity_closure.py` has a closure step `reader_cli_determinism`: write with `generate_determinism_gate_proofs.py`, then check with `--check`.
  - `READER_CLI_DETERMINISM_OUTPUTS` (six outputs, `ab.json` among them) and their path proofs are in `ATTESTATION_GENERATED_OUTPUTS` (checked by executing the module).
- **Canon directs the regeneration.**
  - PF10 v13.3.6 §2.15, L1697 (L1696 in v13.3.5), says: "Governed evidence affected by the corrected renders is regenerated by its existing owning writers and is never hand-edited. This includes … the six outputs of the determinism builder: `audit/gates/parity/reader_cli/ab.json`, …".
  - §2.25 item 3 requires evidence to "converge through their owning writers in PR06's generation order".
- **Approved scope.**
  - Plan v1.0 F-11 lists `audit/gates/parity/reader_cli/{ab,ba}.json` among the owner-written bindings of the current `release_id`.
  - §5.4 step 7 has the determinism writer run, then `--check`.
  - §6.3 puts the determinism family in the owner-regenerated set, not the frozen families of §6.4.
  - Instruction v1.0 §5.3 requires convergence through the owning writers in PR06/PR06a's order.
- **Precedent.** `ab.json` was regenerated at every re-cut: PR06 `f7484d0` (release `988ed2a7…`), PR06a `d79cfc1` (`9f962ce3…`) and PR06b `acae4c6` (`52be4558…`). The sole updater rewrote 34 and 37 Mirror rows at the first two cuts.
- **What changed.**
  - `ab.json`, the Reader v1 envelope of the fixture pair, differs from `main` only in `release_id` and `idempotence_hash`.
  - The Mirror row differs only in `sha256`. Its labels are byte-identical on `main`: `artifact_key` `epic038.pr02.reader_cli_ab`, `epic_id` `HDE-EPIC038`, `record_type` `epic038_pr02_predicate_evidence`, `produced_at_utc` `2026-07-12T00:52:16Z`, and `notes`.
- **`AGENTS.md` L114–L117.** As for CR-01 (result v1.1 §5.1), these lines cover HDE-EPIC038's architecture and OPS packets and runtime identity inputs, and this file is neither.
- **Measured on `7309f2b`** (Python 3.12.3, closed rails, vendor and DB keys absent, detached worktree, discarded):

  | Case | Owner `--check` | `update_evidence_index.py --check` | `tests/evidence/test_determinism_gate_proofs.py` |
  | --- | --- | --- | --- |
  | Baseline | exit 0 | exit 0 | `15 passed` |
  | `ab.json` restored to `main`'s bytes | exit 1, `DRIFT:audit/gates/parity/reader_cli/ab.json` | exit 1, `PROOF_SHA:audit/gates/parity/reader_cli/ab.json.path_proof.txt` | `1 failed, 14 passed` (`test_build_and_check_succeed_on_the_admitted_root`) |
  | All six determinism outputs restored to `main`'s bytes | exit 1, `DRIFT` on five outputs | not run | not run |

  In the six-output case `IDENTITY_OK.txt` is byte-identical on `main`, so only five files changed.
- **The alternative is outside this unit.** "A new evidence identity" for current-release captures is an evidence-family and updater-registration change. Plan §6.6 keeps `tools/evidence/update_evidence_index.py` and the identity closure untouched. The change is contrary to PF10 §2.15 L1697 and to the approved convergence, and it is not needed to deliver the approved scope. It is not material, so there is no `RESCOPE_REQUEST`: it is recorded as a candidate for its owners (O-P06b-17).

## 3. Class-level disposition (CR-01, CR-02 and later instances)

- **The class.** The PR's diff changes 24 Machine Mirror rows. All of them are for artifacts that their owners regenerate at the re-cut because the bytes bind the admitted release. Every row keeps its family registration from `main`:

  | Family | Rows | Labels kept from `main` |
  | --- | --- | --- |
  | determinism | 5: `ab.json`, `ba.json`, `summary.json`, `abba.bytes`, `tworun_identity.sha256` | `epic038.pr02.*`, 2026-07-12T00:52:16Z |
  | open-rails proof | 1 | `epic038.pr03.*`, 2026-07-14T00:00:00Z |
  | A7 success proofs | 5 (four `epic038.pr02.a7_*`, one `a7.*`) | family keys; `produced_at_utc` rewritten by the owner to its capture time, 2026-09-26T15:41:44Z |
  | engine-core | 4 | 2025-11-30T03:58:47Z |
  | F07 writer | 2 | 2026-07-05T15:38:47Z |
  | canonical-JSON gate | 4 (two HDE-EPIC039 `epic039.pr01.*`, two `canonical_json.*`) | 2025-12-26T00:00:00Z |
  | catalog logs | 2 (HDE-EPIC040) | 2026-08-18T16:05:54Z |
  | Machine Mirror self-row | 1 | 2026-09-22T14:25:29Z |

  Ten of the 24 rows are labelled HDE-EPIC038. Only `sha256` changed in 19 rows; the five A7 rows also changed `produced_at_utc`. PR06 and PR06a converged the same way.
- **The disposition.** The class is dispositioned as CR-01 and CR-02 are: not changed, and out of scope for PR06b. The regeneration is canon-directed and approved. The labels come from the pre-existing family registrations the sole updater writes. A per-regeneration provenance model is an evidence-model change for its owners (O-P06b-17).
- **Later instances.** A later Codex finding of this class on a later head of this PR is a duplicate of CR-01 and CR-02. It is answered by reference to this section and then resolved, and its thread is listed in the PR #513 body. That needs no new records version. A finding outside this class is new work and does need one.

## 4. Reviews, threads and CI since v1.3

| Item | State | Evidence |
| --- | --- | --- |
| CR-01 thread `PRRT_kwDOP103ks6mSA83` | resolved | GitHub API |
| CR-02 thread `PRRT_kwDOP103ks6mSUll` | open at this commit. The reply and resolution follow the push, so the reply can cite this record | GitHub API |
| Codex Code Review of `7309f2b` | `Completed` at 2026-09-26T16:53:40Z, trigger "New commits"; one finding (CR-02) | Codex Review Summary comment `5847734093`; review `5326634675` |
| Codex Security Review | the `acae4c6` run, no finding. PR-35 landed no code correction, so it was not re-requested | comment `5847734093` |
| CI `36256453481` on `20ca1c3` | `cancelled` at 16:50:04Z, superseded by the v1.3 push. Changed tests, product and compat had already passed | GitHub API |
| CI `36256852430` on `7309f2b` | created at 16:49:46Z and still `in_progress` when this push was prepared, so this push supersedes it. Its final state is recorded in the PR #513 body | GitHub API |
| Earlier heads | `85e702b3`: run `36254322410` `success`. `e34541b`: run `36255782232` `success` | results v1.1 §8, v1.2 §4 |

## 5. In-flight decisions

`NONE`. CR-01 and CR-02 are review dispositions. Both PF10 file operations are the Product Owner's direction.

## 6. Merge-readiness predicates

| Predicate | State | Evidence |
| --- | --- | --- |
| Approved implementation scope complete | true | result v1.0 §1; result v1.1 §9 |
| Required local checks pass on the candidate | true | result v1.0 §7 (`acae4c6`); result v1.1 §7 (`85e702b3`); §2 here (`7309f2b`: the determinism owner's `--check`, the updater's `--check` and `test_determinism_gate_proofs.py` all green). Nothing after `acae4c6` changes code, tests or evidence |
| Intended commits pushed; PR reflects the exact remote head | established after the push | *Final head* |
| Code and security findings resolved; no required thread unresolved | CR-01 resolved. CR-02 is dispositioned, and its reply and resolution follow the push. The final head's review is read after the push | §2, §3; *Final head* |
| Required CI passes on the current candidate | true on `85e702b3` and on `e34541b`; the final head is read after the push | §4; *Final head* |
| No unresolved material rescope, dependency or repository-state conflict | true | §2; results v1.2 §2 and v1.3 §2 |
| Result, ledger, checkpoint and handoff saved and read back | true locally before the push; remote read-back after it | this file; `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.4.md`; `docs/ephemeral/HDE-EPIC040-PR06b-pr35-checkpoint-v1.3.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.3.md` |

## 7. Limitations and observations

- The final head's CI and Codex review, the CR-02 reply and resolution, the remote read-back of this commit, and the final state of run `36256852430` happen after this record is committed. They are recorded in the PR #513 body and the PR-35 return.
- The limitations in results v1.1 §10, v1.2 §7 and v1.3 §6 stand.
- **O-P06b-17 (new).** The Machine Mirror rows of owner-regenerated release-bound derivatives keep their family registration across re-cuts (origin epic and PR in `artifact_key`, `epic_id` and `record_type`; a first-capture `produced_at_utc`, except where an owner rewrites it). Their bytes, meanwhile, bind the current release. A consumer reading only the labels can take a current regeneration for the original capture. This re-cut changes 24 such rows (§3), 10 of them labelled HDE-EPIC038, and PR06 and PR06a did the same. A per-regeneration provenance field or a release-scoped identity would be an evidence-model decision for the sole updater's owner and the evidence-family owners, or the Product Owner. Not decided here; carried with O-P06b-15, O-P06-17 and O-P06a-11.
- The other observations (O-P06b-01 to O-P06b-16) are carried as results v1.1 to v1.3 record them.
- `CANON_CONFLICT_REGISTER`: C040-01 to C040-08 are unchanged. PR-35 opened, reopened, relabeled or decided no entry.

## 8. Provenance and continuation

- **Provenance.** `GCFPE-USE-HDE-EPIC040-PR-35-20260926-PR06b-01` (this phase), with the entries result v1.1 §14 carries. PF10 read: v13.3.5 (result v1.1) and v13.3.6 (result v1.2 §3). Recorded as provenance, not as a gate.
- **Continuation.** `MERGE_PENDING` on the *Final head* condition. Nathan merges manually. This session stays subscribed to PR #513 and does not poll.
  - When the subscription delivers the merge, the return is `MERGE_OBSERVED` with the PR-40 handoff.
  - Otherwise `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.3.md` applies. It is usable only after Nathan's manual merge and only where no `MERGE_OBSERVED` result was returned. Handoffs v1.0 to v1.2 are void.
- **What merging does.** This is unchanged from result v1.3 §7. Merging makes current on `main`:
  - the corrected Reader v1 schema, the real g06 golden and the regenerated release-pack outputs;
  - the 45-member `1.3.0` release (`release_id 52be4558…`) with its converged evidence;
  - by Product Owner direction, PF10 v13.3.6 as the only PF10 file in `docs/pfcanon/`. This is not a PR06b delivery.

  Reader v1 and v2 response bytes do not change. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-08 or C040-07 drainage, deployment, activation, Epic closure.
