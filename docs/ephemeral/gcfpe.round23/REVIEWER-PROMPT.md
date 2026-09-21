---
artifact_type: PROMPT_ECOSYSTEM_REVIEWER_PROMPT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
subject: SFR-01 §10 independent validation of the round-23 packages
---

# Reviewer prompt — round 23 (`SF10-09` + `SF10-10`)

Paste the block below into a fresh `SFR-01` session, with both `.skill` files attached.

Everything it asks for is reachable from the two attached packages, this repository, and Notion.
Nothing in it depends on PE35's session, scratch directories, or any artifact that no longer exists.

```text
You are SFR-01, performing independent §10 validation of one prompt-ecosystem repair round before
the Product Owner installs anything. You are not the author of this round. Nothing is installed yet
and nothing may be installed until you rule.

WHAT YOU ARE GIVEN
Two attached packages, which install together:
  change-flow.skill          21 files, 242412 bytes,
                             sha256 52d77d970c5eca5dbc89f39a49bcd1b178deeee0ca3d0d8869e1b9193805e337
  flowmaster-validate.skill  29 files, 277974 bytes,
                             sha256 26a8d4766eb839c86c73df02a59f30395a3036a335a23f35afbd9edb4678a6ab

Read first, in this order:
  1. AGENTS.md at the repository root. It governs.
  2. docs/ephemeral/gcfpe.round23/REPORT.md — the round under review.
  3. docs/ephemeral/gcfpe.round23/round23.patch — the complete diff from the installed tree.
  4. docs/ephemeral/gcfpe.round22/REPORT.md and sf10-09.patch — the SF10-09 half, carried forward.
  5. docs/ephemeral/gcfpe.round23/HANDOFF.md — PE34's handoff, for the round's own terms.

Derive every digest from the artifact in front of you. Never transcribe one from the report.

THE CHANGE
SF10-10 exempts the four CF Specification authors — CF-C-20, CF-C-40, CF-E-20, CF-E-40 — from
`current_pf10_markdown_required`, taking that roster from fourteen writers to the ten non-CF
writers. Its authority is the Product Owner's ruling of 2026-09-21, quoted verbatim in the report
and in both SKILL.md files. It is NOT derived from prompt-body quotations; your R1 rejected that
derivation in round 21 and that rejection stands. Assess whether the change is faithful to the
ruling as stated, not whether the bodies support it.

SF10-09, carried in unchanged from round 22, re-encodes the CURRENT_PF10_MARKDOWN predicate.

WHAT TO VERIFY
1. Package integrity. Extract each archive. Confirm the file counts and sha256 above from the bytes
   you were given; confirm every entry sits under its skill root, with no traversal sequences and
   no entry outside that root.
2. Scope. Confirm the extracted trees differ from the current installed tree only in the ten files
   round23.patch names, and that the patch accounts for every difference.
3. The roster. In BOTH bundled copies of the candidate contract, confirm
   plan_writer_contract.body_obligation_ids.current_pf10_markdown_required is exactly the ten
   non-CF writers and equals active_addenda_required; that authoring_context_required is still
   twelve; and that evaluated_prompt_ids is still fourteen. Confirm the two bundled copies are
   byte-identical to each other. Confirm EXPECTED_BODY_OBLIGATION_IDS in
   flowmaster-validate/scripts/validate_gcfpe_20260914.py agrees with the contract.
4. The hash-pin chain. Recompute the candidate contract's sha256 and byte count from the file and
   confirm they match the validator's EXPECTED_CANDIDATE_CONTRACT_SHA256 / _BYTES and the validation
   profile's candidate_contract.sha256 / byte_count. All three must agree with the file itself.
5. Revisions. By grep, not by the report's list: confirm CHANGE_FLOW_SPECIALIZATION_REVISION is
   3.2.8 at its six mutable sites plus the profile's installed_skill_revisions.change-flow, that
   FLOWMASTER_VALIDATE_REVISION is 3.2.10, and that the two remaining 3.2.7 occurrences are dated
   prose records preserved under AUTH-001 rather than missed sites.
6. Run the gates yourself, on a scratch copy of the extracted trees, with
   PYTHONDONTWRITEBYTECODE=1. Never write to the synced skills directory.
     python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
         --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
         [--prompt-dir <bodies>]
     python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow \
         --contract <same> [--prompt-dir <bodies>]
     python3 flowmaster-validate/scripts/validate_flowmaster.py      # needs the FULL skill set copied
     python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow   # argument required
     python3 change-flow/scripts/validate_gcfpe_20260914.py
   Expect: end-to-end exit 0 with 0 errors; contract fixtures 155 cases, 0 failed; body fixtures 179
   cases, 0 failed; FLOWMASTER_SUITE_PASS; every other gate exit 0. Report what you actually get.
7. The corpus. The 55 prompt bodies live in Notion and are never mirrored into the repository, so
   the end-to-end and body-fixture gates need them. Fetch them yourself from the Notion page ids in
   the contract's own notion_page_manifest and write one <PROMPT-ID>.md per body. Do not accept
   PE35's copy; the point is that you reproduce the measurement independently. If you cannot reach
   Notion, say so and report the gates you could run rather than inferring the rest.
8. The repointed fixture. reject-body-obligation-duplicate-id now appends "IA-10" instead of
   "CF-C-20". Satisfy yourself that it tests duplication rather than set drift under the NEW roster,
   and that it would not have done so unchanged. The report states a falsification you can repeat:
   on a throwaway copy, drop the `len(declared) != len(expected_ids)` half of the roster check and
   re-run the contract fixtures. Confirm that exactly one case fails with "IA-10", and that none
   fails with "CF-C-20". A case that cannot fail proves nothing.
9. Rule on the open question the round deliberately did not settle. validator_revision stays at
   3.2.8 this round, per the handoff, on the reasoning that SF10-09's 3.2.8 bytes were never
   installed. Round 22's own rule says two behaviours must not advertise one validator identity, and
   round 22's report on main already records measurements against 3.2.8 from different bytes. Decide
   whether the shipped validator should emit 3.2.8 or 3.2.9 and say which, with your reason. All
   four sites move together if you call for a change.

WHAT NOT TO DO
Do not install either skill. Do not write to the synced skills directory. Do not merge, and do not
enable auto-merge. Do not treat round 21's SKILL_FIT_CONFIRMED as carrying to these bytes; it is
scoped to the digests it named. Do not edit docs/pfcanon/**, and cite PF canon by title and section
only. Do not change prompt bodies in Notion.

WHAT TO RETURN
One §10 verdict on these exact digests: confirmed, or confirmed with findings, or rejected. For each
finding give the artifact, the exact defect, the evidence, and the smallest correction. State which
gates you actually ran and which you could not, and say so plainly rather than inferring a result.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT describing your
session's real state.
```
