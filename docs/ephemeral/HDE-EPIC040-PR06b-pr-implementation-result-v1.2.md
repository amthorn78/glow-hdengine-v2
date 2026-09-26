# HDE-EPIC040-PR06b — PR Implementation Result v1.2 (PR-35)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR06b-PR-IMPLEMENTATION-RESULT` v1.2, the PR-35 phase record at the final PR-35 push. It supersedes only v1.1's outcome, *Final head* condition, readiness table and continuation. v1.1 (`docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-result-v1.1.md`, SHA-256 `d68c31321317f931da9054a22a45a25f648904ef825edb7a29281b7bc05b0cc1`) is unchanged as issued and remains the record of: the CR-01 disposition and its evidence (§§4–5), PR-35 local validation (§7), CI on `85e702b3` (§8), observation O-P06b-15, and provenance. v1.0 remains the implementation record |
| `WORK_UNIT_ID` | HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08, alternative A) with a release re-cut to `1.3.0` |
| Change | `EPIC / HDE-EPIC040`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`); PR06b rescope decision v1.0 |
| Producer | the dedicated PR-35 session for HDE-EPIC040-PR06b (`session_disposition: NEW_DEDICATED`; `role_session_ref: NOT_YET_ASSIGNED`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06b / PR-35`; `context_conflict: NONE`; runtime `https://claude.ai/code/session_01XyLNkn9Ab1sB7kCUCJvodt`); `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `MERGE_PENDING` — Ready to merge, on the condition under *Final head* (§1) |
| Prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 (`https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`; page as of 2026-09-24T15:48:24.405Z; Notion read only). Primary skill: `glow-hde-pr-development` 1.3.1 |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/focused-heisenberg-91y3cn` |
| Pull request | [#513](https://github.com/amthorn78/glow-hdengine-v2/pull/513), the one work vehicle |
| Base | merge-base `d031f94a9cd0ef89f0fc50b37e86abe3cd90a643`; `origin/main` is `d031f94`, re-read before the push |
| Commits | PR-30: `acae4c637e2ce8c9e987953bcbe284f7e03719c9` (implementation) and `85e702b3259f4a549adc69d2f68fa36ddaefda57` (PR-30 records). PR-35: `e34541b0abe072e2b6f4774cde10874b3da8f789` (records v1.1, tree `b3a9682d…`); `f9a655236ee7d445b913854d7e85685be7e78888` (the Product Owner-directed PF10 file operation, tree `9ecee5a2…`, §2); and the commit adding this file (records v1.2). A commit cannot embed its own SHA, so the v1.2 records commit's SHA and the remote head after its push are recorded in the PR #513 body and the PR-35 return |
| Recorded by | the dedicated PR-35 session, 2026-09-26 (UTC) |

## 1. Outcome

**`MERGE_PENDING` — Ready to merge,** on the condition under *Final head*. This record is historical pre-merge evidence. It does not claim the PR is merged. It is not a QA verdict, acceptance, release activation, PF09 movement, OPS01 attestation, C040-08 drainage, deployment or closure. Nathan / Product Owner merges manually as a separate action. Nothing here enables, schedules or requests a merge.

- **Since v1.1.**
  - The v1.1 records commit `e34541b` was pushed as a fast-forward and read back.
  - The CR-01 thread was answered (`discussion_r4111998120`) and resolved; it is the PR's only thread, and `is_resolved` reads `true`.
  - Codex's Code Review of `e34541b` completed with no new review, thread or comment (§4).
  - CI run `36255782232` on `e34541b` concluded `success` (§4).
  - Then Nathan directed: "include this PF10 update in your PR, and remove the old version". Commit `f9a65523` adds `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md` byte-for-byte and removes `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` (§2).
- **Candidate code unchanged.** PR-35 changed no code, test, evidence or roster byte. Every commit after `acae4c6` touches only `docs/ephemeral/` or `docs/pfcanon/`.
- **CR-01 disposition unchanged and better supported.** PF10 v13.3.6 §2.24, the PR06a lineage review, records `generate_open_rails_abba_proof.py` as an accepted coherence dependent of the re-cut (§3).
- **Final head.** This record's commit adds only `docs/ephemeral/` records above `f9a65523`, and `f9a65523` changes only `docs/pfcanon/`. After the push, the following are read and recorded in the PR #513 body and the PR-35 return:
  - the pushed head's exact-head CI (the same four lanes on the same code tree; `docs/pfcanon/**` and `docs/ephemeral/**` select no lane);
  - Codex's review of that head;
  - the thread state and mergeability.

  The return states `MERGE_PENDING` only if CI is green, no new review finding or unresolved thread exists, and the PR stays open and mergeable. Otherwise this result no longer stands and a later version replaces it.

## 2. Product Owner-directed PF10 file operation (not a PR06b delivery)

| Item | Value |
| --- | --- |
| Direction | Nathan / Product Owner, in this PR-35 session, 2026-09-26, with the file attached: "include this PF10 update in your PR, and remove the old version" |
| Authority | `AGENTS.md`, "Explicit PO-directed PF-Canon exception". It authorizes exactly the requested file operation and its commit, and no other PF-Canon edit. The PR06b overlay itself authorizes no PF-Canon edit (its *Exclusions*: §2.25 in v13.3.6, §2.24 in v13.3.5), and this operation does not rely on it. It rides on PR #513 by the Product Owner's direct instruction, and is not a PR06b delivery, a loci extension, an in-flight decision or a rescope |
| Source | the upload `25ce8d70-PF10-HDE-Build-Notes-v13.3.6.md` (the leading `25ce8d70-` is the upload prefix): 281,008 bytes, 2,639 lines, SHA-256 `cc20d134c54bcf0be3b192b063354ddd12688e51d82092f21a06160180de12e6`; UTF-8, LF only, one final LF, no BOM; front matter `**Version: v13.3.6**`, effective date Sep 26, 2026 |
| Target | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md`, byte-identical to the source (`cmp` equal, same SHA-256), mode 644 |
| Removed | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.5.md` (274,422 bytes, `7010511c…`). "The old version" is read as the version this update replaces. Git records the pair as a rename (`R097`) |
| Not touched | `v13.3`, `v13.3.1`, `v13.3.2`, `v13.3.3` and `v13.3.4`, stale base versions already noted as N-01 and O-P06b-07. Whether "the old version" also covers them is Nathan's to say (§8), so they stay until he does |
| Commit | `f9a655236ee7d445b913854d7e85685be7e78888` (tree `9ecee5a274f68791673e38984a12e7a808ebebb2`), 2026-09-26T16:35:54Z; `docs/pfcanon/` only |
| References | `git grep` finds no tracked file outside `docs/ephemeral/` and `docs/pfcanon/` that names the v13.3.5 filename (historical audit records name only older versions). Records issued before this commit cite v13.3.5 and stay as issued: they record what was read at the time, and v13.3.5 remains in git history |
| CI and review effect | `docs/pfcanon/**` is in `ci.yml`'s `paths-ignore` and among the classifier's documentation prefixes, and `AGENTS.md` puts it outside automated-review scope. The PR's cumulative diff still selects product, compat, evidence and release, on unchanged code |

## 3. PF10 v13.3.6, the version this PR makes current on `main`

- **Currency.** `main` carries v13.3.5 until this PR merges and v13.3.6 afterwards. Under front-matter rule 6 only the latest base version counts, so the post-merge reviewer resolves v13.3.6.
- **Read.**
  - Read directly: the headings, the Addendum Index (2.1 to 2.25), and §§2.24 and 2.25 in full (L2487–L2639).
  - Read in full by a read-only worker: all 2,639 lines (281,008 bytes), in chunks of about 250 lines, modifying nothing. What it found:
    - The file never names `FROZEN_OPEN_ABBA_SHA256`, `audit/gates/determinism/open_rails_abba.json`, HDE-EPIC038 or "frozen primary".
    - §2.25 has no coherence-dependent wording and does not list the ABBA proof tool among its loci; result v1.1 §5.1 treats that loci question. PF10 records the tool only as an accepted coherence dependent (§2.22 L2316; §2.24 L2541). It says nothing about the constant, whose history comes from `git log -G` and the PR06 / PR06a result records.
    - PF10's "CR-01" (L2284, L2323, L2497) is PR06's packaged-wheel finding (O-12), not this work unit's Codex CR-01. Finding IDs are per work unit.
    - L2316 cites "plan v1.1 §6.2" and L2541 cites "plan v2.1 §6.2" for the same PR06 precedent (O-P06b-16 (c)).
    - Nothing in the file changes the CR-01 disposition.
  - Located with `grep`: the lines below.
- **Numbering in v13.3.6.**
  - §2.24 is "HDE-EPIC040-PR06a — PR Work-Unit Lineage Review v1.0" (L2487): `decision: ACCEPT`, ACCEPTED_FINAL.
  - §2.25 (L2568, an H2 heading) is the PR06b overlay: objective, three deliveries, owned loci, the rescope clause (L2599), exclusions, completion and work-unit effects. Plan v1.0 and this PR implement it.
  - Records issued before `f9a65523` cite the overlay as §2.24 of v13.3.5.
- **Bearing on CR-01.**
  - §2.24 §4 (L2540–L2541) says: "Paths outside the listed loci: … tools/evidence/generate\_a7\_transport\_proofs.py and generate\_open\_rails\_abba\_proof.py, plus the tests/config/\*, tests/scripts/\* and tests/transport/\* rewrites, are coherence dependents of the re-cut and the route, as with PR06 under plan v2.1 §6.2."
  - PF10 therefore now records the acceptance of the ABBA proof tool as a coherence dependent for both PR06 (§2.22, L2316) and PR06a (§2.24, L2541).
  - The IA accepted that under PR06a's out-of-loci clause (§2.23, L2422). §2.25 L2599 is the corresponding clause for PR06b.
  - CR-01's disposition (result v1.1 §§4–5) stands.
- **Other bearing.** §2.24 L2551 says "PR06b's re-cut must run the engine-core owner". PR-30 did so: plan D-08, result v1.0 §7.1 (C4).
- **Citation map.** Result v1.1 cites v13.3.5 line numbers. The same passages in v13.3.6, located by `grep`:

  | v13.3.5 | v13.3.6 |
  | --- | --- |
  | L1372 | L1373 |
  | L1713 | L1714 |
  | L2080 | L2081 |
  | L2213 | L2214 |
  | L2262 | L2263 |
  | L2308 | L2309 |
  | L2315 | L2316 |
  | L2421 | L2422 |
  | L2517 | L2599 |

## 4. Reviews, threads and CI after v1.1

| Item | State | Evidence |
| --- | --- | --- |
| CR-01 thread `PRRT_kwDOP103ks6mSA83` | answered in `discussion_r4111998120` (16:32:02Z) and resolved; `is_resolved: true`; the only thread on the PR. GitHub records the reply as review `5326574071` (`COMMENTED`) | GitHub API read-back |
| Codex Code Review of `e34541b` | `Completed` at 2026-09-26T16:33:59Z, trigger "New commits"; no new review object, thread or comment. The PR issue carries one `+1` reaction, and its `updated_at` is 16:33:59Z; the read tool does not expose who reacted | Codex Review Summary comment `5847734093`; issue read |
| Codex Security Review | the `acae4c6` run, no finding. PR-35 landed no code correction, so it was not re-requested | comment `5847734093` |
| CI `36255782232` on `e34541b` | **`success`**, job `108442179664`, 16:31:52Z–16:39:49Z. `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=72;lanes=product,compat,evidence,release`. Changed tests `667 passed`; product `20 passed`; compat `102 passed, 3 skipped, 2 xfailed`; db, rails and qa skipped; evidence `111 passed`; release `64 passed` plus the attestation build and `--verify`; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. `RELEASE_LANE:RELEASE_NOT_ADMITTED` never appeared as output | GitHub API; run-log archive |
| CI on the final head | read after the push (*Final head*) | PR #513 body |

## 5. In-flight decisions

`NONE`. The PF10 file operation is the Product Owner's direction (§2), and CR-01 is a review disposition (v1.1 §4).

## 6. Merge-readiness predicates

| Predicate | State | Evidence |
| --- | --- | --- |
| Approved implementation scope complete | true | result v1.0 §1; result v1.1 §9 (CC-6 and CC-8 on `85e702b3`; CC-7: the Security Review is clean, and CR-01 is dispositioned out of scope with its thread resolved) |
| Required local checks pass on the candidate | true | result v1.0 §7 (`acae4c6`); result v1.1 §7 (`85e702b3`, Python 3.12.3). Nothing after `acae4c6` changes code, tests or evidence |
| Intended commits pushed; PR reflects the exact remote head | established after the push | *Final head* |
| Code and security findings resolved; no required thread unresolved | true at `e34541b` (§4); the final head's review is read after the push | §4; *Final head* |
| Required CI passes on the current candidate | true on `85e702b3` and on `e34541b`; the final head is read after the push | result v1.1 §8; §4; *Final head* |
| No unresolved material rescope, dependency or repository-state conflict | true. The PF10 operation is Product Owner-directed and outside the work unit's scope; the base is unchanged | §2 |
| Result, ledger, checkpoint and handoff saved and read back | true locally before the push; remote read-back after it | this file; `docs/ephemeral/HDE-EPIC040-PR06b-pr-remote-action-ledger-v1.2.md`; `docs/ephemeral/HDE-EPIC040-PR06b-pr35-checkpoint-v1.1.md`; `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.1.md` |

## 7. Limitations

- The final head's CI and Codex review, and the remote read-back of this commit, happen after this record is committed. They are recorded in the PR #513 body and the PR-35 return.
- PF10 v13.3.6 was read directly for its headings, its Addendum Index, §§2.24 and 2.25 in full, and every line this record cites. The rest of the file was read by a read-only worker (§3).
- Result v1.1 §10's limitations stand.

## 8. Observations and open items

| ID | Item | Owner |
| --- | --- | --- |
| O-P06b-16 (update) | (a) The §2.11 prompt-use record is also truncated mid-word in v13.3.6: L1373 ends "Repository provenance persistence remains p". (b) No longer applies: the PR06b section in v13.3.6 is §2.25 with an H2 heading, as PF10-FORM-001 requires. (c) New: §2.22 L2316 cites "plan v1.1 §6.2" and §2.24 L2541 cites "plan v2.1 §6.2" for the same PR06 coherence-dependent precedent | Nathan / PF10 drain owner |
| Open item (Nathan) | "Remove the old version" was applied to v13.3.5 only. `docs/pfcanon/` still holds v13.3, v13.3.1, v13.3.2, v13.3.3 and v13.3.4, which are stale base versions. Removing them needs Nathan's word | Nathan |
| carried | O-P06b-01 to O-P06b-15 and the inherited items (result v1.1 §11) | their recorded owners |

## 9. Register, provenance and continuation

- **`CANON_CONFLICT_REGISTER`.** C040-01 to C040-08 are unchanged. PR-35 opened, reopened, relabeled or decided no entry.
- **Provenance.** `GCFPE-USE-HDE-EPIC040-PR-35-20260926-PR06b-01` (this phase), with the entries result v1.1 §14 carries. PF10 read: v13.3.5 (`7010511c…`, result v1.1) and v13.3.6 (`cc20d134…`, this record). Recorded as provenance, not as a gate.
- **Continuation.** `MERGE_PENDING` on the *Final head* condition. Nathan merges manually. This session stays subscribed to PR #513 and does not poll.
  - When the subscription delivers the merge, the return is `MERGE_OBSERVED` with the PR-40 handoff.
  - Otherwise `docs/ephemeral/HDE-EPIC040-PR06b-conditional-PR40-handoff-v1.1.md` applies. It is usable only after Nathan's manual merge and only where no `MERGE_OBSERVED` result was returned. Handoff v1.0 is void.
- **What merging does.** Merging makes the following current on `main`:
  - the corrected Reader v1 schema: its error branch admits exactly the 17 governed envelopes the v1 routes emit, requires `schema`, and drops `retry_after_ms`;
  - the real g06 error golden and the regenerated release-pack outputs;
  - the 45-member `1.3.0` release (`release_id 52be4558…`) with its converged evidence;
  - by Product Owner direction, PF10 v13.3.6 as the current PF10, with v13.3.5 removed. This is not a PR06b delivery.

  Reader v1 and v2 response bytes do not change. It establishes none of: QA verdict, acceptance, PF09 movement, OPS01's final external attestation, C040-08 drainage into PF01 §2.3 / PF04 §8.1.2, C040-07 drainage, deployment, activation, Epic closure. PR07 must follow PR06b, and OPS01 verifies the `1.3.0` release.
