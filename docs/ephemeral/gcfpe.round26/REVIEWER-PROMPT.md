---
artifact_type: PROMPT_ECOSYSTEM_REVIEWER_PROMPT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
template: Glow Operations Hub — "Standard skill reviewer prompt — canonical template — 2026-09-21"
subject: SFR-01 §10 independent validation of the round-26 package
---

# Reviewer prompt — round 26

```text
You are SFR-01, performing independent validation of one skill change. You did not author it.
The package under review is NOT installed and may not be installed until you rule. No skill may be
installed while you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
flowmaster-validate.skill   29 files, 282752 bytes,
                            sha256 2495b2354d93414a0aa8dea3e40569b3fc5004100e22beeb2b56dca11589a805

Installs ALONE. change-flow is not changed and its installed copy stays as it is.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Round 25: you returned SKILL_REPAIR_REQUIRED against 7cf4298c… with two blocking findings.
That package is WITHDRAWN and so is its content. The Product Owner issued the Prompt Corpus Storage
and Fidelity Policy on 2026-09-21, which makes SF10-12 — body pins — defective in principle. Your
two findings are therefore MOOT rather than fixed, and you should confirm the pins are absent
rather than corrected:
  finding 1  the profile's stated extraction convention did not reproduce its own pins. The pins
             are gone; the convention statement is gone with them.
  finding 2  PROMPT_BODY_IDENTITY collided with the identity-header check. The pin check is gone;
             the header check keeps the code, uncollided.
Round 24's package e8f30b9a… IS INSTALLED and carries your SKILL_FIT_CONFIRMED. It is the baseline.

=== 3. BASELINE ===
Recipe: docs/ephemeral/gcfpe.round23/freeze.py, ROOTED AT THE SKILL DIRECTORY.
  installed flowmaster-validate = the baseline   29 files, f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd
  the package under review, extracted            29 files, 54604cf33194858521b714c29bb94b39ef4b7bd913e652aceaf0bb4cba773948
  change-flow, unchanged                         21 files, 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
Reproduce the installed digest first and confirm the baseline is what this prompt says it is. Two
records have been wrong about the install state before; do not take §3 on trust.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch pe35/round26, commit
f3bbc548d2d434fb79cae08336c78cb1f24c6fa0. A pull request may have been opened since.
  docs/ephemeral/gcfpe.round26/REPORT.md      the round under review
  docs/ephemeral/gcfpe.round26/round26.patch  the complete diff from the installed tree, 528 lines,
                                              7 files
  docs/ephemeral/gcfpe.round25/INSTALL-STATE-CORRECTION.md   why round 25 was withdrawn
Read AGENTS.md at the repository root first. It governs. Then read the Prompt Corpus Storage and
Fidelity Policy in the Glow Operations Hub — it is the authority for this change and your review
should test conformance to it, not just correctness.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1  No path in this skill now requires, constructs, or walks a local prompt corpus. Bodies arrive
    as {prompt_id: text} on stdin and there is no path option anywhere.
C2  Four checks were deleted because they policed the mirror rather than the ecosystem:
    PROMPT_BODY_MEMBER_SET, _DUPLICATE, _FILENAME_ID, _UTF8, plus
    CANDIDATE_PROMPT_ROOT_MISMATCH. Nothing about the ecosystem became unobservable as a result;
    membership is carried by the registry and the graph.
C3  PROMPT_BODY_ID_MISMATCH is a net gain: it catches the caller reading the wrong page, which is
    the one error this interface makes likelier than a directory did.
C4  Coverage is reported, not required. prompt_bodies_validated lists ids;
    prompt_body_checks_not_evaluated names set-scoped checks that could not run. A partial run can
    never read as a full pass.
C5  All body hashing is gone, including prompt_body_sha256.
C6  SKILL_TREE_SHA256 makes the validator refuse to certify anything when its own tree does not
    match its declaration, and the declaration line is excluded from the digest so it is stable.
C7  The hash-pin chain does not move; change-flow does not move; the package is SMALLER than the
    tree it replaces.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1  C2 is the claim to break. The author decided four checks were worthless and deleted them.
    For each, construct a real ecosystem defect it used to catch and show whether anything still
    catches it. If any real defect is now invisible, that is a blocking finding.
A2  C6's digest excludes SKILL.md's own declaration line by regex. Attack the exclusion: can two
    materially different trees produce the same digest? Does a second SKILL_TREE_SHA256 line, a
    line with trailing whitespace, or a declaration inside a code fence defeat or confuse it?
A3  C4's honesty depends on a caller reading the new output fields. An operator who keeps reading
    `ok` alone now gets a pass from a run that validated nothing. Decide whether reporting is
    sufficient or whether the validator should refuse to report ok:true when zero bodies were
    supplied and body-level obligations exist.
A4  The author did NOT run a full per-prompt validation against a complete real body — see §7 L1.
    You can. Fetch one writer body from Notion, pipe it in, and confirm the per-prompt obligations
    actually run and pass on real text rather than on the author's synthetic edges.
A5  The fixtures suite lost its 181-case body block and now reports 155. Confirm that is loss of
    mirror-dependent cases only, not loss of real coverage, and that the count is honest.
A6  Grep-recount every revision site. Confirm CHANGE_FLOW_SPECIALIZATION_REVISION is untouched at
    3.2.8 and the candidate contract is byte-identical in both bundled copies.

Questions this round deliberately did NOT settle — answer each explicitly:
Q1  validate_epic_alpha.py and validate_strength_middleware.py each glob a directory of prompt .md
    files and gate on SNAPSHOT_MEMBER_SET — the same defect class, for different prompt sets.
    Neither is reachable from any GCFPE gate; both run only through their own CLI with an explicit
    --prompts. Should they be repaired, deleted, or left dormant?
Q2  With the corpus gate gone, what should the promotion packet cite as body-level evidence? The
    old claim was "0 errors across 55 bodies", which was only ever a point-in-time measurement by a
    session that built a mirror.
Q3  Should SKILL_TREE_SHA256 be adopted by the other installed skills, or is flowmaster-validate a
    special case because it is the instrument everything else is judged by?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1  The author proved the new interface at its edges and proved one writer predicate against real
    Notion text, but ran NO full per-prompt validation against a complete real body — doing so
    would have meant materialising a body on disk or retyping it. This is the largest unverified
    claim in the round and A4 asks you to close it.
L2  validate_flowmaster.py needs the FULL installed skill set present, not this skill alone.
L3  Read the Storage and Fidelity Policy before reviewing. A correction that conforms to it may
    still look like lost coverage if you judge it by repository-software standards, which is
    exactly what the policy forbids.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. PYTHONDONTWRITEBYTECODE=1.
Do NOT build a prompt corpus on disk at any point in this review; if you need a body, read the page
and pipe it.
  a. Extract. Confirm 29 files, 282752 bytes and the sha256 in §1 from the bytes you were given.
     Confirm every entry sits under flowmaster-validate/, no traversal, and the SKILL.md frontmatter
     name is unchanged.
  b. Measure the installed tree's per-skill digest and confirm §3.
  c. Restore the untouched sibling skills and run, FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
           --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       echo '{"IA-10": "<body you read from Notion>"}' | python3 \
           flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow \
           --contract <same> --bodies-stdin
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow --contract <same>
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
  d. Confirm SKILL_TREE_SHA256 holds from the extracted package, then break it: change one byte in
     one script and confirm the validator refuses.
  e. Confirm the diff is exactly the seven files round26.patch names and that applying it to the
     installed skill reproduces the package.
  f. grep the whole skill for prompt_dir, rglob('*.md'), glob('*.md') and any remaining path option
     for bodies. C1 says there are none in any GCFPE path.

The author's measurements, for you to contradict rather than confirm:
  candidate validator     exit 0, ok true, on installed and on this package
  contract fixtures       155 cases, 0 failed
  flowmaster suite        FLOWMASTER_SUITE_PASS
  validator_revision      3.2.11 (installed: 3.2.9)
  SKILL_TREE_SHA256       5bb632ce952b11649e5e868904a5fe7f4d594d5ec1083fa1c000c58cf1cd2fb6
  .pyc written            zero

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not build a local prompt corpus, even a temporary or read-only one — that is
the thing under repair. Do not edit docs/pfcanon/**. Do not change prompt bodies in Notion.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digest in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer Q1, Q2 and Q3
explicitly; a question is not a finding.
State whether this change conforms to the Prompt Corpus Storage and Fidelity Policy, which is the
authority it was made under — separately from whether it is correct.
State which gates you ran and which you could not, plainly.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
