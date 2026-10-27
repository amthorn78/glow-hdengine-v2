---
artifact_type: ADR_DECISION_PROPOSAL
artifact_id: HDE-CRD-0002-WU-PR-07-ADR-PROPOSAL
artifact_version: "1.1"
supersedes: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.0.md (preserved unchanged; v1.1 adds CX7-7 and PO-35-4)
decision_question: AQ-1 (Implementation Plan v1.1 §13; Implementation Audit v1.0 §8)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
requirement: S21
adr: docs/adr/hde/close_pack_writer_adr.md (status Proposed; 73 lines, as pushed with this proposal)
decision_owner: Product Owner (Plan v1.1 §13 AQ-1; instruction v1.0 ID-12)
reviewer: the continuing whole-change Implementation Agent for HDE-CRD-0002 (the RS-20 reviewer of this unit, session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j, as provenance)
author: the dedicated WU-PR-07 PR-35 session, https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA, at the Product Owner's direction of 2026-10-20 ("if you need an ADR decision you need to draft the ADR proposal for the IA session")
selected_prompt: none. HDE IA — GCFPE-20261009.1 — 100926.1 lists 21 members (DOC-10 to RS-40), and none reviews an ADR; this proposal is the Product Owner's direct task, not a prompt invocation
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.5.md on the PR branch (addenda 2.11, 2.13, 2.14); main still carries v13.6.3 until #668 merges
created_at: 2026-10-20T23:10:00Z
---

# HDE-CRD-0002 WU-PR-07 — AQ-1 ADR proposal v1.1

## 1. Decision requested

The decision is AQ-1. Does the Product Owner approve the S21 ADR `docs/adr/hde/close_pack_writer_adr.md`, with the text delta in §6?

- **The IA's role:** check this proposal and the ADR against canon and the approved base, then return a recommendation and any redlines.
- **The IA does not approve the ADR.** Approval is the Product Owner's (Plan v1.1 §13; instruction ID-12: "no agent marks the ADR approved").

## 2. What the ADR does

It makes HDE-CRD-0002 and later changes closable on the ordinary path, with a governed close pack.

- **One writer at its registered path.** `tools/qa/generate_epic_close_pack.py` gains a v2 source model (`schemas/close_candidate_source.v2.json`) for Epic and CRD identities. v1 sources keep v1's bytes.
- **The v2 report** carries what Change Process Guide §3.5.2.1 requires: the verbatim heading, acceptance pointers, exact-source acceptance, the binary decision, deferrals, the tracked-issue mapping, follow-ups, superseded artifacts and the verification statement. Every claim is rendered from tracked inputs.
- **Same-run close evidence** gets a post-verdict home, `audit/qa/<crd>/close/<check_id>/primary.log`. Only the canonical updater publishes it, and the approved QA manifest is not reopened.
- **Index rows** for a CRD close pack appear only when both files exist.

Consumers:
- HDE-CRD-0002's close mutation set (T1 to T7 of the plan's close sequence).
- Every later Epic or CRD close that uses the v2 source.

## 3. What breaks without a decision

- **#668 cannot merge** (Plan R-4; instruction ID-12). WU-PR-08 and the units ordered after WU-PR-07 wait with it.
- **S21's acceptance intent fails.** It includes "the accompanying ADR is approved". Change Process Guide §1.0.5 requires an approved ADR for a canon change of this kind.
- **If the ADR is declined:** S21 does not hold, and HDE-CRD-0002 has no ordinary Close Gate. The Product Owner then decides exceptional closure (Plan v1.1 §9 item 5; Change Process Guide §3.5.1). HDE-EPIC040 and HDE-EPIC038 both closed that way.

## 4. Options

| Option | Effect | Cost |
| :- | :- | :- |
| **A. Approve as drafted, with the §6 delta** | The ADR becomes Accepted; #668 can merge once its review and CI are clean; S21 can hold at QA | one ADR edit, pushed with the PR-35 terminal record (one CI run) |
| B. Approve with changes | The unit is revised before merge; through RS-10 where the bounded scope changes (instruction ID-12) | a revision round; within the remaining ceiling only for text changes; a scope change is material and returns to the Product Owner first |
| C. Decline | S21 does not hold; #668 should not merge as is; HDE-CRD-0002 closes by exceptional closure | the WU-PR-07 work is discarded or reverted; the close-report problem (B-1, B-2) stays open for every later change |

Alternatives the ADR weighed (Audit §8 AQ-1):
- (b) a separate close-report writer: two writers for one artifact family, and the same canon change;
- (c) a manifest check added after the verdict: rejected by CC-2;
- a canon change dropping the close-report requirement: the Product Owner chose the writer instead on 2026-10-20.

## 5. What changed since the PR-30 draft

PR-35 fixed seven P1 Codex findings. CX7-2 to CX7-7 were fixed at the Product Owner's direction (PO-35-1 to PO-35-4; result records v1.2, v1.3, v1.5 and v1.6; PF10 addendum 2.14).

| Finding | Writer behavior now |
| :- | :- |
| CX7-1 | Requirement and deferral IDs match only as whole dotted identifiers |
| CX7-2 | A tracked issue closed by ADR status must name an ID in the drain-targets ledger (`TRACKED_ISSUE_UNBOUND`) |
| CX7-3, CX7-4, CX7-6 | Requirement IDs are read only from the change kind's pinned format: a CRD reads `\| S<NN> \|` rows; `HDE-EPIC<NNN>` reads its own `**K<NNN>-REQ-<NNN>.**` paragraphs and `\| AC<NNN>-<NN> — ` rows. Refusals: a document without its change's format (`REQUIREMENTS_TABLE_ABSENT`); a criterion that is not a read ID (`REQUIREMENT_ID_UNBOUND`); `SATISFIED` without an acceptance row for every read ID (`REQUIREMENT_COVERAGE_INCOMPLETE`) |
| CX7-5 | A tracked-issue pointer is `{binding, heading}`: a tracked evidence input that contains that Markdown heading (`BINDING_UNRESOLVED`, `TRACKED_ISSUE_POINTER_UNBOUND`) |
| CX7-7 | The bound QA step-logs manifest is read in the pinned flat format the canonical QA harness writes; any other ledger, including `{}`, is refused (`QA_LEDGER_INVALID`); `SATISFIED` needs every recorded status `PASS` (`DECISION_CONTRADICTION`) |

The ADR's "Stated limits" already reflect these changes:
- the old line "Requirement coverage is the source author's" is removed, as the Product Owner directed;
- the pin line, the pointer line and the QA-ledger line are added.

The ADR's "Decision" section was not revised. It still describes acceptance only as binding "each criterion ID to a tracked requirements document". §6 closes that gap.

## 6. Proposed ADR text delta (for the IA's review; not yet applied)

Decision item 4. Replace:

> an exact-source acceptance section that binds each criterion ID to a tracked requirements document, to tracked evidence and to a result and limitation;

with:

> an exact-source acceptance section that binds each criterion ID to a tracked requirements document, to tracked evidence and to a result and limitation; the criterion IDs are read from that document in the change kind's pinned format, and a `SATISFIED` decision needs an acceptance row for every ID read and a QA step-logs manifest, in the pinned ledger format, whose every recorded status is `PASS`;

Decision item 4. Replace:

> deferrals with a drain target or ADR status; … the tracked-issue mapping;

with:

> deferrals with a drain target or an ADR status whose ID the drain-targets ledger names; … the tracked-issue mapping, each item either a pointer to a heading in a tracked evidence input or an ADR status whose ID the drain-targets ledger names;

Status line, on the Product Owner's decision only:
- Option A: `Status: Accepted. Approved by the Product Owner on <date> (AQ-1; decision record <path>).`
- Option B or C: the text that decision states.

The PR-35 session applies the delta and the status line in one push after the Product Owner decides, and records the decision in its terminal result record. `docs/adr/` is Markdown and outside the Codex review scope (AGENTS.md "Code review guidelines").

## 7. Checks for the IA

1. **Change Process Guide §1.0.5:** the ADR names affected canon and drainage consequences. The table in "Affected canon and drainage consequences" covers four homes:
   - Change Process Guide §3.5.2 and §3.5.2.1;
   - HDE Schemas & Artifacts §1.2;
   - Glow QA Guide close-pack sections;
   - HDE Mechanics Guide §37.2 and §1.6.3.

   Check that no further home needs an entry, now that requirement-ID pins and the TI rules exist. Likely candidates are Plan Templates, if a requirement-ID format becomes a Specification contract, and the HDE CRD Records Specification profile.
2. **PF10 addendum 2.11 rules 4 to 6:** each component rests on real inputs.
   - Each pinned format is taken from a real Specification on `main` (HDE-CRD-0002 v1.1, HDE-EPIC040 v1.1), and each change kind reads only its own.
   - Other formats get one refusal and a stated limit.
   - No external system is emulated.
3. **Addendum 2.14:** no P1 on a real input is left as a stated limit. The three stated limits added in PR-35 are not P1 dispositions:
   - pinned formats only, where another format is refused;
   - the pointer check does not judge whether the section demonstrates closure;
   - the writer reads the QA ledger only and does not open the primaries.

   Check that none reads as declining a P1. CX7-7's fix is pushed with this proposal and awaits Codex's check (thread open).
4. **The approved base:** Specification S21; Plan v1.1 WU-PR-07 block and §13; instruction ID-12 and H-5; rescope review v1.0 §6. Check that the ADR changes no acceptance criterion and no other unit's scope.
5. **Consistency with HDE-EPIC039's posture** (AGENTS.md "HDE-EPIC039 current workflow posture"):
   - one writer;
   - `--source` with exactly one of `--write` or `--check`;
   - manifest committed last;
   - reads in `manifest → report → manifest` order;
   - no hosted feedback.

## 8. Recommendation

**Option A.** The ADR keeps every HDE-EPIC039 safeguard and adds only what canon requires the report to say. The PR-35 fixes make the acceptance section enforce §3.5.2.1's "each current governing requirement" instead of leaving coverage to the author. The §6 delta makes the Decision section say so. Option C would leave every later change on exceptional closure, which the Product Owner rejected on 2026-10-20.

## 9. Return point

- **The IA's recommendation and any redlines** go to the Product Owner, saved under `docs/ephemeral/`.
- **The Product Owner's decision** goes to the WU-PR-07 PR-35 session for #668, which applies §6 and reaches `MERGE_PENDING`.
- **A decision that changes the bounded scope** goes through RS-10 and RS-20 (instruction ID-12).

## 10. TypeSafe reading for the receiving session (IA review of this proposal)

Action sent (v8.2): "Review, in the continuing whole-change implementation session, one proposed architecture decision record (72 lines, drafted with one pull request and revised once by its review corrections) and the decision request that accompanies it, against canon and the approved plan, and prepare the Product Owner's approve, approve-with-changes or decline decision with a recommendation; no code is written and no live provider call occurs; the Product Owner decides, and the pull request session applies the decision before merge."

- **TypeSafe v8.2: Opus 5.5 at extra high.** Effort score 2.86 (confidence 0.66); rung probabilities low 0.00, medium 0.02, high 0.29, extra high 0.51, max 0.18, ultracode 0.00. Model probabilities Fable 5.1 0.08, Opus 5.5 0.87, Sonnet 5.5 0.05, Haiku 5.5 0.00 (confidence 0.83). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.023, Fable 5.1 at extra high 0.041, Fable 5.1 at max 0.014, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.017, Opus 5.5 at high 0.252, Opus 5.5 at extra high 0.444, Opus 5.5 at max 0.157, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.014, Sonnet 5.5 at extra high 0.026, Sonnet 5.5 at max 0.009, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T22:37:45Z. Nathan picks the cell.
- **Detail:** v8.2, session kind `review`, run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`. The printed header line above shows no flags. This session's capture kept only the header line, so the HTTP, token and rule-detail line was not kept. The reading was not re-run (one text, one reading).
- **Records:** the Notion row was not written (addendum 2.1). Nathan has not stated a pick.

**Surface advice:**
- Run in the continuing HDE-CRD-0002 Implementation Agent session, or a session that recovers that role from its artifacts, on `amthorn78/glow-hdengine-v2`.
- Read access to the PR branch is needed for the ADR, the PF10 v13.6.5 file and the PR-35 result records, plus `main` for canon.
- No code execution, provider, database or deployment access is needed.

## Canon relied on

| Topic | Sources |
| :- | :- |
| ADR required for a CRD canon change; affected canon and drainage | Change Process Guide §1.0.5 "Canon changes" |
| Close-pack content the ADR's writer must express | Change Process Guide §3.5.2.1 "Close-pack files"; §3.5.4 "ADR block in the close-pack" (the close report's ADR block, distinct from this ADR) |
| Decision owner and timing | Implementation Plan v1.1 §13 AQ-1, §11 R-4, §9 item 5; Implementation Audit v1.0 §8 AQ-1; WU-PR-07 instruction v1.0 ID-12, H-5 |
| Real inputs, refusals, no emulation; P1 handling | PF10-HDE-Build-Notes v13.6.5 addendum 2.11 rules 4 to 8; addendum 2.14 |
| Rescope items in the same unit | addendum 2.13; rescope review v1.0 §6 |
| No ADR-review prompt in the selected family | HDE IA — GCFPE-20261009.1 — 100926.1 (member table read in full) |
