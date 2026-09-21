---
artifact_type: PROMPT_ECOSYSTEM_REVIEWER_PROMPT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
template: Glow Operations Hub — "Standard skill reviewer prompt — canonical template — 2026-09-21"
subject: SFR-01 §10 independent validation of the round-25 package
---

# Reviewer prompt — round 25 (`SF10-12` + the round-24 comment correction)

```text
You are SFR-01, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
flowmaster-validate.skill   29 files, 284004 bytes,
                            sha256 7cf4298c43d515c33c8d9fc4b4dc5892e421d39c740b495f8ae42356f3cd231a

This package installs ALONE. change-flow is not changed and its installed copy stays as it is.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Prior verdict: SKILL_FIT_CONFIRMED with one finding, 2026-09-21, issued by you against
  flowmaster-validate.skill  e8f30b9a798ce12b0616d54ee6fb99af296bab9f1986cfa6158088a8c3bff872
That package was NEVER INSTALLED and is now WITHDRAWN. This one supersedes it against the same
baseline and carries everything it carried, plus SF10-12, plus the fix for your finding. Your prior
verdict is therefore VOID for these bytes — but it is not void as a record, and §5 C6 asks you to
confirm that what you already confirmed is still present and unaltered.

Findings carried forward:
  Round-24 finding  the absence fixture's comment claimed PROMPT_HANDOFF_RECEIVER fires here and
                    that the case isolates the arity branch. FIXED IN THIS ROUND — check the fix,
                    not the finding.
  F1, F2            fixed and closed in earlier rounds; not reopened.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline — the installed flowmaster-validate, unchanged since before round 24:
  29 files, digest 5dcb95a992263cc2255c9e324ec3ea28fe2768f97ac7d0bf3f6204c0b50c6220
Repaired tree:
  29 files, digest 90e9d405061c3975884056d067ec595e533c6c35dcc9702bd67bcd4cd58410dc
Unchanged change-flow: 21 files, 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
Recipe: docs/ephemeral/gcfpe.round23/freeze.py, ROOTED AT THE SKILL DIRECTORY.
Reproduce the baseline first. If it does not reproduce, stop and say so before reviewing anything.

SUPERSEDED, so you do not chase them: every whole-tree digest in rounds 23 and 24 (3e84e5cc…,
ca9bdd1e…, 2fa5b848…, c607cedc…) and the never-reproducible round-21 baseline 2f5d14a6…. Also
note freeze.py's docstring still says the count is "one fewer than the tree's file count" — true
when rooted at the synced tree, stale under skill rooting. You reported that last round; it is a
repository-only fix and is deliberately not in this package.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch pe35/followup, commit
8b5135f260776100417a9d464471e7cc707d1ff4. NOT MERGED at the time of writing; a pull request may
have been opened since, so check the branch.
  docs/ephemeral/gcfpe.round25/REPORT.md       the round under review
  docs/ephemeral/gcfpe.round25/round25.patch   the complete diff from the INSTALLED tree, 451 lines
  docs/ephemeral/gcfpe.round24/SECTION-10-REVIEW.md   your own prior review — on main
  docs/ephemeral/gcfpe.round24/REPORT.md       the round this supersedes — on main
  docs/prompt_ecosystem_management/project-prompt-contract-registry.md  where the pins came from
Read AGENTS.md at the repository root first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1  Before this round a corrupted prompt body passed the entire end-to-end gate silently. The
    validator computed prompt_body_sha256, reported it, and compared it with nothing.
C2  All 55 body identities were ALREADY recorded in the approved registry's evidence_contract, and
    all 55 reproduce against a corpus fetched from Notion. Nothing needed to be invented.
C3  The pins belong in the validation profile, not the candidate contract, because they are
    validation expectations rather than contract terms — which is why the candidate contract's own
    sha256 already lives there. Consequence: the hash-pin chain does not move and change-flow does
    not move.
C4  Exactly one trailing newline is stripped before hashing and nothing else is normalised, because
    the pin is a property of the Notion page, not of the file holding it.
C5  Absent pins are an error and the profile parameter is required, so the check cannot be silently
    skipped.
C6  Everything you confirmed in round 24 is still present and unaltered except the one comment your
    finding named.
C7  validator_revision 3.2.9 → 3.2.10 and FLOWMASTER_VALIDATE_REVISION 3.2.11 → 3.2.12 because both
    are bound to your published verdict on e8f30b9a…, extending F1's rule from "installed identity"
    to "identity a published verdict describes".

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1  C4 is the weakest point and the likeliest source of a future defect. The normalisation is a
    judgement about which differences are legitimate. Attack it: does stripping one trailing
    newline hide anything that should fail? Does NOT stripping it make the check unusable in
    practice? Construct a corpus difference you think should be caught and check that it is.
A2  C2 rests on the registry's recorded extraction of 2026-09-18/19, not on a fetch made today.
    Fetch at least two bodies from Notion yourself and confirm their pins still reproduce. If one
    does not, that is drift in the corpus, not necessarily a defect in this package — say which.
A3  The author chose the profile over the contract (C3) partly because it is cheaper — one skill
    moves instead of two. Cheapness is a bad reason for an architectural choice. Decide whether the
    profile is genuinely the right home or whether cost drove it.
A4  C1 is the author's justification for the whole change, established by removing their own check
    and observing 0 errors. Reproduce that: delete the identity comparison on a throwaway copy,
    corrupt one body, and confirm the gate really does pass.
A5  Recount the revision sites by grep. Confirm CHANGE_FLOW_SPECIALIZATION_REVISION is untouched at
    3.2.8 and that the candidate contract is byte-identical in both bundled copies.
A6  The profile grew from 2473 to 10672 bytes. Confirm it still round-trips under
    indent=2/sort_keys=True/ensure_ascii=False plus a trailing newline, and that nothing else in it
    changed beyond validator_revision and the new prompt_bodies block.

Questions this round deliberately did NOT settle:
Q1  Should PROMPT_BODY_IDENTITY be fatal, or should a mismatch be reported as drift and routed to a
    re-pinning step? The author chose fatal. An authorised body edit in Notion will now fail every
    gate until the profile is re-pinned, which is either the correct forcing function or a trap.
Q2  The pins record an extraction dated 2026-09-18/19. Should the profile instead pin a date and
    require a fresh fetch, or is a dated pin the right artifact?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1  You can now verify a corpus you build, which you could not last round — that is the point of
    SF10-12. Build it from Notion and the gate will tell you whether you built it correctly. If a
    body does not reproduce, report which and stop rather than adjusting it to fit.
L2  validate_flowmaster.py needs the FULL installed skill set present, not this skill alone.
L3  The author's corpus was rebuilt by extracting bodies from transcripts, not retyped. Stated so
    you do not assume otherwise; it is not offered as your evidence.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. PYTHONDONTWRITEBYTECODE=1.
  a. Extract. Confirm 29 files, 284004 bytes and the sha256 in §1 from the bytes you were given.
     Confirm every entry sits under flowmaster-validate/, no traversal, no entry outside it, and
     `name: flowmaster-validate` in SKILL.md frontmatter.
  b. Restore the untouched sibling skills and run the gates FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
           --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
           --prompt-dir <bodies>
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow \
           --contract <same> [--prompt-dir <bodies>]
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
     Read each tool's own top-level flag by name.
  c. Confirm the extracted tree differs from the installed flowmaster-validate only in the five
     files round25.patch names, and that applying the patch to the installed skill reproduces the
     package.
  d. Reproduce all four falsifications in REPORT.md, A4 above included.
  e. Recompute the candidate contract sha256 and byte count from the file; confirm the validator
     pins and the profile pin agree with it.
  f. Grep-recount validator_revision (claim: 3.2.10 at four sites),
     FLOWMASTER_VALIDATE_REVISION (3.2.12) and CHANGE_FLOW_SPECIALIZATION_REVISION (3.2.8).
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  end-to-end, 55 bodies       exit 0 — 0 errors, on both the installed and repaired trees
  contract fixtures           155 cases, 0 failed
  body fixtures               181 cases, 0 failed (installed tree: 179)
  validator_revision emitted  3.2.10 (installed tree: 3.2.8)
  flowmaster suite            FLOWMASTER_SUITE_PASS
  .pyc written                zero

=== 9. WHAT NOT TO DO ===
Do not install any skill, and in particular do not install the withdrawn e8f30b9a…. Do not write to
the synced skills directory. Do not merge and do not enable auto-merge. Do not treat your round-24
confirmation as carrying to these bytes. Do not edit docs/pfcanon/**. Do not change prompt bodies
in Notion — if a body does not reproduce against its pin, report it; do not make it fit.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digest in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer Q1 and Q2
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Give the disposition of your round-24 finding — fixed, declined or deferred — and any defect found
while checking it.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
