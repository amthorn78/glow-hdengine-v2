---
artifact_type: PROMPT_ECOSYSTEM_EVIDENCE_NOTE
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
release: GCFPE-20260914.1 / 091426.1 / 55
subject: Post-flight as specified cannot be run, and its method is the origin of the last three weeks
---

# Post-flight — review before running it

The Product Owner asked for this review on the grounds that post-flight *"was designed for ChatGPT,
has never been run in Claude, and often failed in ChatGPT — its failures are the reason we went
through 3 weeks of iterations."* Measured against the instrument and the record, that account is
correct and the mechanism is identifiable.

## 1. Its evidence contract mandates the artifact the policy forbids

`amthor-workspace-governance-audit/references/report-contracts.md`:

> Store the run manifest, registry identities and hashes, **source manifest**, deterministic check
> results, semantic findings, finding dispositions, and **artifact hashes** in
> `WGA-{RUN_ID}-Evidence.json`. **Preserve raw and structural digests separately.**

Applied to 55 prompt bodies, that is a whole-corpus export with byte-for-byte hashing — named twice
in the **Prompt Corpus Storage and Fidelity Policy**: *"whole-corpus Markdown or JSON exports"* and
*"byte-for-byte comparisons, hashes, or raw-file identity checks for prompt bodies."*

This is not how one auditor chose to run it. **The skill requires it.**

The last run says so in its own words:

> All 67 live Notion candidate bodies match the frozen raw hashes/revisions/parents and **their
> complete local counterparts** under documented presentation normalization.

## 2. That method is the origin of the three weeks

*"Documented presentation normalization"* is the whole defect class:

- **24 of 55** `evidence_contract` entries reproduced only with a trailing newline the page does not
  contain, because the corpus had been assembled by two different methods;
- `ESC-40`'s stored capture carried an **841-byte paragraph the live page never had**, and the
  approved registry was built from that contaminated capture;
- the `body_extraction_convention` key exists solely to adjudicate this, and a session still got it
  wrong reading the same file that defines it;
- `SF10-12` pinned body hashes, was rejected, and was withdrawn by the policy;
- rounds 25, 26 and 27 were consumed by it.

**Every one of those is a byte-fidelity dispute about a copy of a Notion page.** None is a defect in
a prompt. Remove the method and the defect class goes with it.

## 3. The cost-to-signal ratio, measured

The last post-flight produced, to report **one error**:

| artifact | bytes |
|---|---|
| Evidence Manifest v2.0 | **13,619,000** |
| Evidence Manifest v1.0 | 3,926,689 |
| `WGA-…-Evidence.json` | 3,926,358 |
| Correction Delivery Receipt | 152,984 |
| four reports, changesets, receipts | ~85,000 |

**~17.7 MB of evidence, one error, verdict `FAIL`.** The finding itself — *"PR-35 requires an
approved Guide before the ordinary flow creates the Live QA Guide"* — is a producer/receiver
question answerable from the registry and the graph in one query.

## 4. Four of its thirteen checks are stale or unfalsifiable

| §11 check | status |
|---|---|
| 1. all 55 complete prompt bodies | **prohibited** — a corpus read, and the policy names requiring one as a violation in itself |
| 3. producer/consumer **and required/optional input** agreement | producer/consumer is fine; **optional-input agreement is unrecorded anywhere** and was dispositioned today as unfalsifiable |
| 6. PF10 producer count and **manual-drain handshake** | producer count fine; **manual drain was retired by `D6`** |
| 9. Markdown-only PFCanon and **Drive artifact routing** | PFCanon fine; **Drive was retired by `D7`** |

The remaining **nine** checks are all corpus-free and already instrumented:

| check | where it is already answered |
|---|---|
| batch ledgers and dispositions | repository, `docs/ephemeral/` |
| terminal and nonterminal branches | the graph's own invariant, `D15`; zero violations |
| graph closure and handoff identities | the graph, which rebuilds to its proof token exactly |
| PF10 producer count | the contract — exactly the six |
| PR/QA boundary | `PR-20`'s registry row: exactly one input, `PR_INSTRUCTION_ID` |
| PR continuity, abort/merge controls | registry prohibitions on all 55 rows |
| prompt-to-skill agreement | the §10 matrix, refreshed each round |
| Primary/R1 identity | `flowmaster-validate`, run continuously |
| selected-release nonmutation, Alpha stopped | directly checkable |

## 5. The options, stated plainly

**A — Run it as written.** Not available. It would either produce the prohibited corpus artifact or
fail on retired requirements. Both outcomes are defects, not verdicts.

**B — Amend §11, then run a bounded independent post-flight.** Strike the retired halves of checks 6
and 9 and the unfalsifiable half of check 3; re-scope check 1 from *"all 55 complete prompt bodies"*
to targeted Notion reads with stated coverage; cap the evidence at citation rather than
transcription. Keep the independence requirements unchanged — fresh session, not the author, not the
skill reviewer, cannot repair. **Recommended.**

**C — Skip post-flight and promote on the §10 verdict plus the installed gates.** Defensible: nine
of the thirteen checks already run continuously, and §10 is independent and current. What is lost is
a second independent pair of eyes on the repository controls — and independence is precisely what
caught `F1`–`F4` in round 26 after the author had declared the round sound.

## 6. The recommendation

**B.** The value of post-flight was never the exhaustive hashing; it was that someone who did not
author the work looked at it and could say no. That survives the amendment intact. What does not
survive — and should not — is a method that manufactured three weeks of byte-fidelity disputes about
copies of pages that were never in question.

**The amendment is a plan change and therefore the Product Owner's.** Nothing here amends anything.
