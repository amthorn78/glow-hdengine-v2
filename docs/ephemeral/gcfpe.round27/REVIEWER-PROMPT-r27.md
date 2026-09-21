---
artifact_type: PROMPT_ECOSYSTEM_REVIEWER_PROMPT
artifact_version: "1.0"
created_date: 2026-09-21
author: PE35
round: 27
template: Glow Operations Hub — "Standard skill reviewer prompt — canonical template — 2026-09-21"
subject: SFR-01 §10 independent validation of the round-27 package cb3c6286…
---

# Reviewer prompt — round 27

> **Filename carries the round deliberately.** Four rounds of `REVIEWER-PROMPT.md` led to the
> round-24 text being pasted against the round-26 package. See *Delivered artifacts must be
> identifiable from their filename* in the Operations Hub.

```text
You are SFR-01, performing independent validation of one skill change. You did not author it.
The package under review is NOT installed and may not be installed until you rule. No skill may be
installed while you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
flowmaster-validate.skill   29 files, 284588 bytes,
                            sha256 cb3c628662a19b77b235634c77e2eac0e24e6d304debb8bb15ef573f1c727bfd
                            SKILL_TREE_SHA256 6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93

Installs ALONE. change-flow is not changed.
If the digest in front of you is not cb3c6286…, you have the wrong package or the wrong prompt.
Stop and say so — that has now happened twice in this sequence.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Round 26: you returned SKILL_REPAIR_REQUIRED against 2495b235… with four blocking findings, one
non-blocking, and one correction to the author's report. PE35 confirmed every one of them against
the bytes and did not dispute any. That package is superseded and was never installed.

This round exists to repair exactly those. Your task is to check the repairs and to find what they
broke — not to re-litigate the findings.

Round 24's package e8f30b9a… IS INSTALLED and carries your SKILL_FIT_CONFIRMED. It is the baseline.

=== 3. BASELINE ===
Recipe: docs/ephemeral/gcfpe.round23/freeze.py, ROOTED AT THE SKILL DIRECTORY.
  installed flowmaster-validate = the baseline   29 files, f170a01cf170124183c8ebcbfd25cafa155410a2e2fce443c38af5d35c8dfacd
  the package under review, extracted            29 files, 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
  change-flow, unchanged                         21 files, 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
Reproduce the installed digest FIRST. Two records have been wrong about the install state; take
nothing in §3 on trust.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch pe35/round27, commit
3c973394075ce035a4761117d7194a2554b4b0cd.
  docs/ephemeral/gcfpe.round27/REPORT-r27.md   the round under review
  docs/ephemeral/gcfpe.round27/round27.patch   the diff from the INSTALLED tree, 666 lines, 9 files
  docs/ephemeral/gcfpe.round26/SECTION-10-REVIEW.md   your own findings this repairs
Read AGENTS.md first. Then the Prompt Corpus Storage and Fidelity Policy in the Operations Hub —
it is the authority for this work, and conformance to it is a separate question from correctness.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1  F1 fixed: ARTIFACT_AVAILABILITY_BODY_SET and the require_complete parameter are deleted, and
    no remaining code path in the skill requires a complete body set.
C2  F2 fixed: None reports ALL_BODY_LEVEL_CHECKS; {} and partial sets report the specific
    set-scoped checks. A run that validated nothing can no longer report that nothing was skipped.
C3  F3 fixed: no operating instruction for --prompt-dir survives. The only mentions are dated prose
    recording its removal, preserved under AUTH-001.
C4  F4 fixed: validate_flowmaster and validate_gcfpe_current both refuse a tampered tree.
C5  Exactly one SKILL_TREE_SHA256 declaration is permitted.
C6  Q1 answered: the two dormant --prompts snapshot validators are retired.
C7  The hash-pin chain does not move; change-flow does not move; CHANGE_FLOW_SPECIALIZATION_REVISION
    stays 3.2.8.
C8  The documented procedure was executed end-to-end against a real Notion body BEFORE packaging —
    the test round 26 skipped — and the body was deleted in the same command.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1  C1 is the claim that failed last time in exactly this shape: a requirement removed in one place
    and left standing in another. Do not check the two places the author names. Search the WHOLE
    skill for any remaining assertion over a complete set — set comparisons against EXPECTED_MEMBERS,
    stage_categories, SUBSTANTIVE, or any roster — and decide whether each is a legitimate contract
    check or another corpus requirement wearing a different name.
A2  C6 retired two code paths by making them return an error. That is a stub, not a removal. Decide
    whether a retired path should fail loudly, be deleted outright, or drop the flag entirely — and
    whether an error return from --prompts is honest or merely quiet-looking.
A3  C4 puts the same self-identity call in three gates by local import. Attack the coupling: what
    happens if validate_gcfpe_20260914.py is absent, renamed, or itself tampered with? Does a
    tampered tree that breaks the import fail open?
A4  C2's ALL_BODY_LEVEL_CHECKS is a single opaque token. Decide whether it tells an operator enough,
    or whether it should enumerate what was not run.
A5  C8 rests on one prompt, IA-10, chosen by the author. Choose a different one — ideally a CF
    Specification author, whose obligations SF10-10 deliberately changed — read it from Notion, and
    confirm the per-prompt path behaves on a body the author did not pick.
A6  Recount every revision site by grep, and confirm the contract is byte-identical in both copies.

Questions this round deliberately did NOT settle:
Q1  With the corpus gate gone, what should the promotion packet cite as body-level evidence?
    Carried from round 26 unanswered.
Q2  Should SKILL_TREE_SHA256 be adopted by the other installed skills, or is flowmaster-validate
    special because it is the instrument everything else is judged by? Carried from round 26.
Q3  The fixture suite reports 155 cases and no longer carries body-level cases at all. Is a fixture
    suite that cannot exercise real bodies still adequate, or does the body path need fixtures of
    its own built from synthetic bodies?

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1  One real body was used for the end-to-end test — IA-10 — and one only. A5 asks you to pick
    another. The author did not test the three-body QA-closure path against real pages at all.
L2  validate_flowmaster.py needs the FULL installed skill set present.
L3  No prompt corpus exists on disk and none may be created during this review, including a
    temporary one. If you need a body, read the page and pipe it.

=== 8. WHAT TO EXECUTE ===
Scratch copy. Never write to the synced skills directory. PYTHONDONTWRITEBYTECODE=1.
  a. Extract. Confirm 29 files, 284588 bytes, the sha256 in §1, no traversal, frontmatter name
     unchanged.
  b. Measure the installed tree's per-skill digest and confirm §3.
  c. Run, FROM THE EXTRACTED CONTENTS, with the sibling skills restored:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract <C>
       echo '{"<ID>": "<body you read from Notion>"}' | python3 \
         flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract <C> --bodies-stdin
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow --contract <C>
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
  d. Break the self-identity: change one byte in one script and confirm ALL THREE gates refuse.
  e. Add a second SKILL_TREE_SHA256 line and confirm MULTIPLE_DECLARATIONS.
  f. Confirm the diff is exactly the nine files round27.patch names and that applying it to the
     installed skill reproduces the package.
  g. grep the whole skill for prompt_dir, rglob('*.md'), glob('*.md'), require_complete, and any
     path option for bodies.

The author's measurements, to contradict rather than confirm:
  candidate validator    exit 0, ok true, on installed and on this package
  contract fixtures      155 cases, 0 failed
  flowmaster suite       FLOWMASTER_SUITE_PASS on a clean tree, FAIL on a tampered one
  validator_revision     3.2.12 (installed: 3.2.9)
  no bodies offered      prompt_body_checks_not_evaluated: ['ALL_BODY_LEVEL_CHECKS']
  one real body          ok true, validated ['IA-10'], not_evaluated ['QA_PASS_CLASS_MAP_AND_INTAKES']
  .pyc written           zero

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge, do not enable
auto-merge. Do not build a local prompt corpus, even temporarily. Do not edit docs/pfcanon/**. Do
not change prompt bodies in Notion.

=== 10. THE DELIVERABLE ===
One verdict: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED, bound explicitly to the digest in §1 and
void for any other bytes. For each finding give the artifact, the exact defect, the evidence, and
the smallest correction. Answer Q1, Q2 and Q3 explicitly.
Give the disposition of each of your four round-26 findings — fixed, partially fixed, or not fixed.
State whether this conforms to the Prompt Corpus Storage and Fidelity Policy, separately from
whether it is correct.
State which gates you ran and which you could not.
Write a successor record; do not correct a dated record in place (AUTH-001). Name it
SECTION-10-REVIEW-r27.md.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
