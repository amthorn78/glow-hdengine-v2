---
artifact_type: GCFPE_WORKFLOW_SKILL_FIT_REVIEW
artifact_version: "2.0"
created_date: 2026-09-19
release: GCFPE-20260914.1 / 091426.1 / 55
review_run: 8
reviewer: PE33 coordinating; two isolated independent reviewers
verdict: SKILL_REPAIR_REQUIRED
findings: 2
frozen_snapshot_sha256: 5f430e55ca3f5c3ffd27dc56a6337bfe22b51c2f7bd10f1daf67a241b71221b9
frozen_snapshot_files: 319
gate: post-flight remains blocked until this returns SKILL_FIT_CONFIRMED
supersedes: none — gcfpe.workflow-skill-fit-review.md is the round-7 record and is not edited
---

# GCFPE Workflow Skill-Fit Review — run 8

Run against a frozen installed snapshot on 2026-09-19. The round-7 record at
`gcfpe.workflow-skill-fit-review.md` is a dated artifact and is not modified.

## Verdict

`SKILL_REPAIR_REQUIRED`. Two findings. **PR #418 remains unmerged.** The selected release
`GCFPE-20260913.1 / 091326.2 / 54` was not touched.

## Snapshot control

Round 16 was confirmed **installed** before the review, correcting the handover record,
which said it was packaged and awaiting installation. Confirmed by recomputation rather
than by reading the pinned constant: all four bundled candidate contracts yield
`dcfcf6c3d3189cb43f3067369e9288b7` / 144 rows, and the guard block is byte-identical
across both installed validator copies (3098 bytes, sha256 `738be21e832fb56b…`).

The tree was hashed before and after: **319 files, `5f430e55ca3f5c3f…`**. No pre-existing
file changed. Three `__pycache__/*.pyc` files were created by running the bundled
validators. This closes `SF-07`, the round-7 defect in which the snapshot moved mid-review.

Per §7, the guard was attacked by two parties that could not see each other's work, and
the ten §10 questions were answered by a third reviewer barred from assessing the guard.
Every evidence quote was machine-verified against source before acceptance.

## Finding 1 — the D8/D15 guard (v5) is defeated

v5 selects a branch only when `terminal_for_invocation` is truthy or
`next_prompt_handoff_count == 0` — **72 of 280** state-route branches. The remaining
**208 are never hashed**, so how completely a selected branch is hashed is irrelevant.

Seven injections were reported independently and **reproduced by the coordinator** against
the real guard function. In every case the digest stayed `dcfcf6c3d3189cb43f3067369e9288b7`
at 144 rows and the vocabulary regex was silent:

| Attack | Evasion |
|---|---|
| A-02 | `next_prompt_handoff_count: "0"` — a string is not equal to `0` |
| A-03 | both selector fields absent; terminality in `ends_invocation` |
| A-04 | both selector fields `null` |
| A-05 | gate on the **edge object**, which is hashed only through `from` |
| A-06 | branch list under a key other than `route_branches` |
| A-13 | mirrored across both surfaces so all structural checks stay satisfied |
| A-14 | terminal branch re-homed onto a prompt-destined edge; rows were a set keyed without `to` |

The coordinator reached the same root cause independently, by rewording the existing
non-terminal `recovery_pr30` branch into a reconciliation gate: control and attack produced
identical validator error lists.

**Survived attack and recorded as verified:** per-surface `E`/`S` tagging does prevent a
deletion on one surface being cancelled by an addition on the other; whole-object hashing
does cover every field of branches the selector admits. Row count alone carries no
information — both held it at exactly 144.

**Not verified:** one reported attack (`route_graph` / `terminal_contract`) was not
reproduced by the coordinator and is recorded as unconfirmed.

## Finding 2 — `SF10-01`, blocking §11 independently

`flowmaster-validate`'s prompt-identity header check builds `f"Candidate Notion URL: {url}"`
from `member['notion_url']`. All **55 of 55** contract URLs carry `?pvs=204`; no prompt body
does, and bodies render the binding as a `<mention-page>` element. Confirmed by direct fetch
of the live PR-40 body: the installed check returns `False` on it.

The suite is green only because that path runs when a prompt directory is supplied, and the
corpus reports `NOT_REQUESTED` with `prompt_bodies_validated: false`. §11 must validate all
55 bodies, so it would fail on every one. A check that fails on every member of a set is
information about the check.

## Verified clean

All eleven round-7 findings are closed in the installed tree, each re-verified against
source rather than carried forward, four by executing the tools. Nine of the ten §10
questions answer affirmatively; question 4 has no subject under **D16** and was not
re-litigated.

**Subagent Notion access is confirmed working**, retiring the standing blocker behind
`prompt_bodies_validated: false`. §11 can validate all 55 bodies against source.
