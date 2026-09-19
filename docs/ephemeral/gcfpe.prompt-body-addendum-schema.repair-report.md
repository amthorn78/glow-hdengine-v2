# GCFPE Prompt-Body Repair — Addendum Schema and Support-Skill Scope

artifact_type: `RUN_EVIDENCE_REPORT`
release: `GCFPE-20260914.1 / 091426.1 / 55`
date: `2026-09-19`
session: PE32
status: `COMPLETE`

## Scope

Three defect classes across the 55 candidate prompt bodies, plus the registry
guard that would have caught the first of them.

A fourth candidate class was withdrawn before any edit was applied. Its rule
had been written as "the only writable repository paths are `docs/ephemeral/`,
`docs/graph/` and `docs/prompt_ecosystem_management/`". That is the PE
session's own write boundary, not the governance of runtime evidence
destinations. Its only hits were OPS-10 and OPS-20 correctly directing
evidence to `artifacts/ops/`, which PF02 §1001 names as the governed proof
surface and PF04 §3807-3814 enumerates by filename. Applying it would have
deleted a Canon-mandated destination. No prompt body was edited under it.

## Applied edits — 30 across 21 prompt bodies

| class | authority | prompts |
|---|---|---|
| `artifact_version` inside the PF10 addendum field list | candidate direct-handoff contract, `pf10_addendum_contract.forbidden_fields` | 9 |
| support-skill capability list offering QA | same contract, `support_skill_policy` | 18 |
| CL-40 citing three RS prompts by non-manifest names | selected catalog manifest titles | 3 names |

`support_skill_policy` reads: "A support skill may supply only a specifically
required environment, Railway, vendor, database, deployment or Ops capability,
and receives no PR-workflow authority; QA execution remains with the authorized
QA lane and its operator."

## Verification

- Every edit re-checked against the live page after application: all absent
  conditions hold, all present conditions hold, 0 remaining support-skill QA
  hits, 0 remaining `artifact_version` occurrences across the 21.
- The two edits that removed a line from inside a fenced YAML block (ESC-40,
  IA-30) had their blocks re-fetched and quoted back in full; fences closed,
  keys well-formed, no residue.
- Each body extracted twice independently; all 21 pairs byte-for-byte identical.
- Reverse-applying the 30 edits to the extracted bodies reproduces the
  registry's pre-edit SHA-256 for 21 of 21.

## Registry guard

`audit_assertions.forbidden_regex` gained one entry on all 55 rows:

    addendum_id[\s\S]{0,400}?artifact_version

Anchored on function, not on the token, per the contract's own
`forbidden_fields_scope` direction to "interpret this list by function, never
by the word". Five fixtures in `amthor-workspace-governance-audit`. Verified by
mutation: neutering the pattern fails the two regression cases; widening it to
a bare `artifact_version` fails the unrelated-mention case; the correct pattern
passes all five. The guard is silent on all 21 repaired bodies.

## Extraction convention — open item for the Product Owner

The registry states: "the exact slice between the fetch result's `<content>`
and `</content>` markers, with no trailing newline added".

The markers occupy their own lines, so a literal reading retains the newline
after `<content>` and the one before `</content>`, and yields bodies two bytes
larger than the registry's actual basis on every prompt. The convention in
force drops both boundary newlines. Established two ways:

- reverse-applied edits reproduce the recorded digests for 21 of 21 under
  "strip both", and 0 of 21 under as-extracted, leading-only or trailing-only;
- three untouched prompts extracted under all four variants reproduce their
  recorded digests only under "strip both" — CF-C-10 `41dce73a…` / 7203 B,
  MGR-10 `5c8aebc6…` / 7276 B, PR-40 `042255564c…` / 54043 B, the last
  extracted programmatically from a persisted payload rather than transcribed.

The wording is left unchanged pending a Product Owner decision. It defines the
ecosystem's tamper-evidence and is ambiguous enough to have produced a silent
two-byte error that no amount of agreement between extractions would surface.
