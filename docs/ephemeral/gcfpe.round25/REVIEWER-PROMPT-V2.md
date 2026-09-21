---
artifact_type: PROMPT_ECOSYSTEM_REVIEWER_PROMPT
artifact_version: "2.0"
created_date: 2026-09-21
author: PE35
template: Glow Operations Hub — "Standard skill reviewer prompt — canonical template — 2026-09-21"
supersedes: REVIEWER-PROMPT.md v1.0, which assumed nothing was installed — see §0
subject: SFR-01 §10 independent validation of the round-25 package, against the tree as it actually stands
---

# Reviewer prompt — round 25, v2

## §0 — why v1 is superseded

`REVIEWER-PROMPT.md` v1.0 is a dated record and is not edited (`AUTH-001`). It told the reviewer
that the baseline was the pre-round-24 tree `5dcb95a9…` and that round 24's package was "never
installed". **Both statements were true when written and are false now.** Round 24's package
`e8f30b9a…` was installed on 2026-09-21 in place of round 25's, under an identical filename. A
reviewer working from v1 would find that `round25.patch` does not apply to the installed tree and
would have to reconstruct the situation themselves. This version states it.

Paste the block below into a fresh `SFR-01` session with `flowmaster-validate.skill`
(`7cf4298c…`) attached.

```text
You are SFR-01, performing independent validation of one skill change. You did not author it.
The package under review is NOT installed and may not be installed until you rule. No skill may be
installed while you are reviewing; if the tree moves under you, the review is void — say so and
stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
flowmaster-validate.skill   29 files, 284004 bytes,
                            sha256 7cf4298c43d515c33c8d9fc4b4dc5892e421d39c740b495f8ae42356f3cd231a

Installs ALONE. change-flow is not changed and its installed copy stays as it is.
Your verdict binds to the WHOLE package digest above, not to a delta. The delta in §4 is an aid for
checking scope; it does not redefine what you are ruling on.

=== 2. THE PRIOR VERDICT, AND THE STATE YOU WILL ACTUALLY FIND ===
Prior verdict: SKILL_FIT_CONFIRMED with one finding, 2026-09-21, issued by you against
  flowmaster-validate.skill  e8f30b9a798ce12b0616d54ee6fb99af296bab9f1986cfa6158088a8c3bff872

READ THIS CAREFULLY, because an earlier version of this prompt said the opposite. That package was
declared withdrawn and superseded — and then it, rather than the round-25 package, was INSTALLED.
So the tree you will measure is `e8f30b9a…`: reviewed and confirmed by you, but one round behind.
The package in front of you supersedes it.

Findings carried forward:
  Round-24 finding  the absence fixture's comment claimed PROMPT_HANDOFF_RECEIVER fires in that
                    fixture's own checker and that the case isolates the arity branch. Both false.
                    FIXED IN THIS PACKAGE and therefore STILL PRESENT IN THE INSTALLED TREE.
                    Check the fix; the finding itself is settled.
  F1, F2            fixed and closed in earlier rounds; not reopened.

Your prior confirmation is VOID for these bytes. It is not void as a record, and C6 asks you to
confirm that what you already confirmed survives here unaltered.

=== 3. BASELINES — THERE ARE TWO, AND BOTH MATTER ===
Recipe for every digest below: docs/ephemeral/gcfpe.round23/freeze.py, ROOTED AT THE SKILL
DIRECTORY, never at the synced tree.

  installed now, = round 24's package    29 files, f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd
  pre-round-24, the historical baseline  29 files, 5dcb95a992263cc2255c9e324ec3ea28fe2768f97ac7d0bf3f6204c0b50c6220
  the package under review, extracted    29 files, 90e9d405061c3975884056d067ec595e533c6c35dcc9702bd67bcd4cd58410dc
  change-flow, unchanged throughout      21 files, 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2

Reproduce the INSTALLED digest first, from the synced tree, and confirm for yourself that it equals
`f170a01c…` and therefore that round 24's package is what is running. If it does not, the situation
has changed again since this prompt was written — stop and say so before reviewing anything.

SUPERSEDED, so you do not chase them: every whole-tree digest in rounds 23 and 24 (3e84e5cc…,
ca9bdd1e…, 2fa5b848…, c607cedc…) and the never-reproducible round-21 baseline 2f5d14a6…. Also
freeze.py's docstring still says the count is "one fewer than the tree's file count" — true when
rooted at the synced tree, stale under skill rooting. You reported that; it is a repository-only
fix and is deliberately not in this package.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch pe35/round25-review. NOT MERGED when written; a pull
request may have been opened since, so check the branch.
  docs/ephemeral/gcfpe.round25/REPORT.md                    the round under review
  docs/ephemeral/gcfpe.round25/round25.patch                diff from the PRE-ROUND-24 tree
                                                            (5dcb95a9…), 451 lines — it does NOT
                                                            apply to the installed tree
  docs/ephemeral/gcfpe.round25/round25-from-installed.patch diff from the INSTALLED tree
                                                            (f170a01c…), 398 lines, 5 files — this
                                                            is the one that applies to what is
                                                            running, and applying it reproduces
                                                            90e9d405…
  docs/ephemeral/gcfpe.round25/REVIEWER-PROMPT.md           v1 of this prompt, superseded, kept
  docs/ephemeral/gcfpe.round24/SECTION-10-REVIEW.md         your own prior review — on main
  docs/prompt_ecosystem_management/project-prompt-contract-registry.md  where the body pins came from
Read AGENTS.md at the repository root first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1  Before this change a corrupted prompt body passed the entire end-to-end gate silently. The
    validator computed prompt_body_sha256, reported it, and compared it with nothing. This is still
    true of the INSTALLED tree, so you can measure it there rather than only on a mutated copy.
C2  All 55 body identities were ALREADY recorded in the approved registry's evidence_contract, and
    all 55 reproduce against a corpus fetched from Notion. Nothing was invented.
C3  The pins belong in the validation profile, not the candidate contract, because they are
    validation expectations rather than contract terms — which is why the candidate contract's own
    sha256 already lives there. Consequence: the hash-pin chain does not move, and change-flow does
    not move.
C4  Exactly one trailing newline is stripped before hashing and nothing else is normalised, because
    the pin is a property of the Notion page and not of the file holding it.
C5  Absent pins are an error and the profile parameter is required, so the check cannot be silently
    skipped.
C6  Everything you confirmed in round 24 survives here unaltered except the one comment your
    finding named.
C7  validator_revision 3.2.9 → 3.2.10 and FLOWMASTER_VALIDATE_REVISION 3.2.11 → 3.2.12, because
    both are bound to your published verdict on e8f30b9a… — extending F1's rule from "an identity
    an installed build claims" to "an identity a published verdict describes". Note that e8f30b9a…
    is now BOTH, which makes the increment unambiguous rather than merely prudent.
C8  The delta from the installed tree is exactly the five files in round25-from-installed.patch, and
    applying that patch to the installed tree reproduces the package.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1  C4 is the weakest point and the likeliest source of a future defect. The normalisation is a
    judgement about which differences are legitimate. Construct a corpus difference you believe
    should be caught and check that it is. Does stripping one trailing newline hide anything? Does
    not stripping it make the check unusable?
A2  C2 rests on the registry's recorded extraction of 2026-09-18/19, not on a fetch made today.
    Fetch at least two bodies from Notion yourself and confirm their pins still reproduce. If one
    does not, that is drift in the corpus, not necessarily a defect in this package — say which.
A3  The author chose the profile over the contract (C3) partly because it is cheaper — one skill
    moves instead of two. Cheapness is a bad reason for an architectural choice. Decide whether the
    profile is genuinely the right home or whether cost drove it.
A4  C1 is the author's justification for the whole change and was established by removing their own
    check. You can do better: the installed tree HAS no such check, so corrupt one body, run the
    end-to-end gate against the INSTALLED validator, and see for yourself whether it passes.
A5  Recount every revision site by grep. Confirm CHANGE_FLOW_SPECIALIZATION_REVISION is untouched at
    3.2.8 and the candidate contract is byte-identical in both bundled copies.
A6  The profile grew from 2473 to 10672 bytes. Confirm it still round-trips under
    indent=2/sort_keys=True/ensure_ascii=False plus a trailing newline, and that nothing in it
    changed beyond validator_revision and the new prompt_bodies block.
A7  Specific to this round: the author's own report and v1 of this prompt both asserted an install
    state that was not measured. Treat every claim here about what is installed as suspect until you
    have measured it, including §3's claim that the installed tree is round 24's package.

Questions this round deliberately did NOT settle — answer each explicitly:
Q1  Should PROMPT_BODY_IDENTITY be fatal, or should a mismatch be reported as drift and routed to a
    re-pinning step? The author chose fatal. An authorised body edit in Notion will then fail every
    gate until the profile is re-pinned — correct forcing function, or trap?
Q2  The pins record an extraction dated 2026-09-18/19. Should the profile pin a date and require a
    fresh fetch instead, or is a dated pin the right artifact?
Q3  New. Nothing in this ecosystem detects that the WRONG package was installed: the hash-pin chain,
    the body pins, the fixture suites and §10 itself all pass against a superseded version. A
    canonical rule now requires a post-install digest comparison, which is a procedure rather than a
    control. Is a procedural rule sufficient, or should the validator refuse to run when the skill
    it is running from does not match a declared self-identity?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1  You can verify a corpus you build against this package, which you could not last round — that is
    the point of SF10-12. Build it from Notion and the gate will tell you whether you built it
    correctly. If a body does not reproduce, report which and stop; do not adjust it to fit.
L2  validate_flowmaster.py needs the FULL installed skill set present, not this skill alone.
L3  The author's corpus was rebuilt by extracting bodies from transcripts, not retyped. Stated so
    you do not assume otherwise; it is not offered as your evidence.
L4  The author has twice stated an install state without measuring it. Nothing in §2 or §3 about
    what is installed should be believed until you have reproduced the digest yourself.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. PYTHONDONTWRITEBYTECODE=1.
  a. Extract. Confirm 29 files, 284004 bytes and the sha256 in §1 from the bytes you were given.
     Confirm every entry sits under flowmaster-validate/, no traversal, no entry outside it, and
     `name: flowmaster-validate` in SKILL.md frontmatter.
  b. Measure the installed tree's per-skill digest and confirm §3's claim about it, either way.
  c. Restore the untouched sibling skills and run the gates FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
           --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
           --prompt-dir <bodies>
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow \
           --contract <same> [--prompt-dir <bodies>]
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
     Read each tool's own top-level flag by name.
  d. Apply round25-from-installed.patch to a copy of the installed skill and confirm it reproduces
     the package, and that the difference is exactly those five files.
  e. Reproduce the four falsifications in REPORT.md, and A4 above against the installed validator.
  f. Recompute the candidate contract sha256 and byte count from the file; confirm the validator
     pins and the profile pin agree with it.
  g. Grep-recount validator_revision (claim: 3.2.10 at four sites), FLOWMASTER_VALIDATE_REVISION
     (3.2.12) and CHANGE_FLOW_SPECIALIZATION_REVISION (3.2.8).
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  end-to-end, 55 bodies       exit 0 — 0 errors, on the pre-round-24 tree and on this package
  contract fixtures           155 cases, 0 failed
  body fixtures               181 cases, 0 failed (pre-round-24 tree: 179)
  validator_revision emitted  3.2.10
  flowmaster suite            FLOWMASTER_SUITE_PASS
  .pyc written                zero

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat your round-24 confirmation as carrying to these bytes. Do not edit
docs/pfcanon/**. Do not change prompt bodies in Notion — if a body does not reproduce against its
pin, report it; do not make it fit.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digest in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer Q1, Q2 and Q3
explicitly; a question is not a finding.
State plainly what you measured the installed tree to be, since two records have now been wrong
about it.
State which gates you actually ran and which you could not, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Give the disposition of your round-24 finding — fixed, declined or deferred — and any defect found
while checking it.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
