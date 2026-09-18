---
artifact: GCFPE cross-cutting repair report
subject: Retirement of the PF10 addendum drainage lifecycle (D6) and removal of the addendum-role token (D4)
release: GCFPE-20260914.1 / 091426.1 / 55 (UNSELECTED_CANDIDATE)
authority: Product Owner rulings D1–D6, recorded in docs/prompt_ecosystem_management/gcfpe.decision-record.md
version: 1.0
date: 2026-09-18
verdict: DRAINAGE_RETIRED_AND_VERIFIED
---

# What was removed

The **PF10 addendum drainage lifecycle**: a prompt emitted a PF10 addendum; the
addendum sat in a non-canonical "pending manual drain" state; Nathan manually drained
it into PF10; downstream work was **gated** on that drain being verified. Prompts
carried drain statuses, drain anchors, drain owners, pre-drain and post-drain
reference roles, four-value drain-verification enums, and rules about what may not be
inferred from a failed drain lookup.

All of it is gone. There is no drain step, no drain gate, no drain status, no drain
verification, no drain inference — and no replacement state machine, enum, status
token, anchor or gate was introduced anywhere.

# What was deliberately kept

**PF10 addenda themselves.** A qualifying approval still emits exactly one PF10
addendum overlay against an immutable approved base. Only the drainage of it is gone.

**Legitimate canon drainage** — the canon-conflict register's disposition of a
conflict into permanent PF authority. 18 passage families / 74 occurrences carry
*permanent drainage target and owner*, *permanent Canon drainage*, *drainage owner*
inside a conflict/ADR register, or *drain PF Canon* in a negative-authority list.
These are a different concept that happens to share the word, and they are untouched.
A lexical sweep for "drain" would have deleted all of them.

# Measured surface

| | Families | Occurrences |
|---|---|---|
| Rewritten — retired lifecycle present | **142** | **280** |
| Preserved — legitimate canon drainage | 18 | 74 |
| Carried by the CL-20 rename rather than the sweep | 11 | 13 |
| **Total drain-word occurrences across 55 prompts** | **171** | **367** |

This supersedes the earlier 93-passage / 218-occurrence figure, which was produced by
a heuristic and understated the surface by 49 families / 62 occurrences. See the
decision record for what the heuristic got wrong.

# How each passage was repaired

Three moves, no fourth:

1. **Delete** the drainage clause from an otherwise valid surviving instruction.
2. **Replace an obsolete drainage gate** with the qualifying approval itself, or with
   reading current PF10 where current PF10 is what the step actually needs.
3. **Replace a drainage enum or status** with a recorded provenance fact, in these
   words, used verbatim wherever move 3 applied:
   > Record the PF10 version actually read as provenance; it is evidence of what was
   > read, never a gate on later work.

Sixteen passages were whole-line or whole-block deletions: the `status`,
`canonicality`, `drain_owner` and `drain_verification_anchor` fields of the addendum
contract, and the four-value drain-verification enums. Where deleting an enum left a
lead-in sentence introducing nothing, the lead-in was folded into prose; where it left
a bullet with no list, the bullet was folded in or removed. A structural audit
confirmed the sweep introduced **no** new blank lines, dangling lead-ins or orphaned
bullets in any prompt.

# CL-20 rename

`CL-20` was the retired machine: its native function was *Prepare Post-Closure
Drainage and Closure Memo* and it produced a `POST_CLOSURE_DRAINAGE_STATUS`. Its
surviving job is real — the closure memo to Thoth and Master Scrum, the board-update
instruction, the inventory of already-produced addenda, and the tracking of delivery
and board actions.

Renamed, under Product Owner authorization, to
**`CL-20 — Prepare Closure Memo and Post-Closure Record`**, producing `CLOSURE_MEMO`
and `POST_CLOSURE_RECORD`. The four tracked manual actions become three: PF10 drainage
drops out; delivery to Thoth, delivery to Master Scrum and the board update remain.

All 13 title references across CL-20, CL-30, CL-40, CL-C-10 and CL-E-10 were updated
in the same pass, along with the Notion page title, the registry `expected_title`,
`function` and output artifact, and the CL-20 graph part.

# D4 — the addendum-role token

`PF10 addendum role` is removed from all **55** prompt bodies, from all 55 graph
nodes, and `role_vocabulary` from the graph's addendum contract. Nothing read it: it
appeared only as a leaf attribute in zero edges, conditions, predicates or routes, and
the registry's `outputs[].artifact` already carries the same fact in a checkable form.
Four of the six declared producers used three different values for the same concept.

# Graph contract

The `NATHAN_MANUAL_PF10_DRAIN` boundary node and its 10 outbound transitions are
removed. The six producer prompts now route their qualifying approval directly to the
receiver the approval names, carrying `transport: MANUAL_PRODUCT_OWNER_INVOCATION`
where the receiver is separately invoked — the manual event is the paste, not a gate
the graph models.

RS-40's `MANUAL_DRAIN_REQUIRED`, `MANUAL_DRAIN_MISMATCH` and `DRAIN_VERIFIED` intake
states are gone. Its mismatch case survives as a terminal return under the existing
`PRODUCT_OWNER_DECISION_REQUIRED` state rather than minting a replacement token. The
long-standing `RS-40.drain_verified` orphan route — reported by the builder on every
run since the parts design landed — disappears with the machine that declared it.

`pf10_addendum_contract.forbidden_fields` deliberately keeps its three drainage
entries. They are an active schema guard against reintroducing the fields, not a
restatement of the retired process.

Proof token from the updated parts:

    55 nodes · 227 edges · 55 state_routes
    embedded JSON 570793 bytes
    sha256 cb9286cd796970b91467485ee178569d8f3ef1bb450f6854bf1a26a37f450f51

Edges fall from 236 to 227: sixteen drainage edges removed, seven direct edges added
where no edge to that receiver already existed.

# Verification

Every prompt was read back from Notion after the sweep and compared against the
intended result derived independently from the pre-repair body. Checks applied to
every prompt:

- **applied exactly as intended** — the live page is byte-identical to the derived
  result;
- **machinery gone** — zero retired-lifecycle markers survive anywhere;
- **legitimate canon drainage intact** — every preserved occurrence still present;
- **job intact** — no prompt-ID reference, routing target, immutability rule,
  canon-conflict duty, negative-authority item or terminal/handoff rule lost;
- **no substitute state machine** — zero new `UPPER_SNAKE_CASE` tokens introduced;
- **D4 applied** — no prompt carries the addendum-role token;
- **structure sound** — no blank lines, dangling lead-ins or orphaned bullets
  introduced.

The registry's `evidence_contract` byte count and SHA-256 are refreshed for all 55
prompts. The extraction convention was proved first: all 55 pre-repair bodies hash
exactly to the evidence the registry already recorded, so the refreshed values are in
the same convention a future verifier will reproduce.

# Prompts touched

54 of 55 prompts carried drainage language; all 55 carried the addendum-role token.
`IA-60` carried the token only and was edited for D4 alone.

# What this repair did not do

Two of the authored rewrites initially moved PF10 addendum storage from
`Glow / Ephemeral Planning Files` in Drive to `docs/ephemeral/` in the repository.
That is a **storage-architecture** change, not a drainage change, and it was reverted
before the sweep ran. The ecosystem currently holds both conventions in different
prompts. That inconsistency is a separate, already-inventoried defect class and is
left for its own pass, so that this diff stays reviewable as one rule.
