You are SFR-01, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

This is a RE-REVIEW. You returned SKILL_REPAIR_REQUIRED on round 28 and again on round 29.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
change-flow.skill           21 files   242827 bytes   sha256 ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860
flowmaster-validate.skill   29 files   288056 bytes   sha256 0e00084e397ede0848c68f9368469d6be50f55bb044826088b40fc8485982e09

The two packages install TOGETHER and must be reviewed together.
change-flow.skill is byte-identical to rounds 28 and 29 (verified by cmp). Every change is in
flowmaster-validate. You may reuse your own prior measurements on change-flow; say so if you do.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Prior verdict: SKILL_REPAIR_REQUIRED, round 29, against flowmaster-validate 423458d9…
flowmaster-validate's digest has changed; nothing you concluded about it carries.

Disposition of every round-29 finding:
  R29-F1  changed validation behaviour shipped under an unchanged revision identity  — FIXED
  R29-F2  `**Lifecycle**: X` and neighbours evade the prefix strip (non-blocking)    — FIXED
No finding declined, none deferred. One defect found while fixing them and repaired in the same
change: the fixture suite again tested only the shapes its author had already thought of, which is
why R29-F2 survived a round that was specifically about evasion.

Round-28 findings F1 and F2 you verified fixed in round 29; that work is unchanged here except
where R29-F2 extends F1's matcher.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline is the currently installed tree, still the round-27 release:
  change-flow            21 files, digest 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
  flowmaster-validate    29 files, digest 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
Repaired trees:
  change-flow            21 files, digest 80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8   (= rounds 28, 29)
  flowmaster-validate    29 files, digest b9ca212ac1275f16af12d34ad15d3df6e95fc71a95f2ce1ab56ee7245a3317af
flowmaster-validate declares SKILL_TREE_SHA256: eb9634d60a65610c131e5d406d7ed6c69038864c555ad89e4c92b5bfde5dd6a8
(different recipe from the freeze digest, by design; both correct, not meant to match).
Recipe: docs/prompt_ecosystem_management/freeze.py, ROOTED AT THE SKILL DIRECTORY.
Reproduce the baseline first. If it does not reproduce, stop and say so.

Superseded, do not chase: round 28 b5f5d3a3… / 13353ffe… / 8ed6d8b0…; round 29 423458d9… /
5da1c46b… / 740844f0…

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch docs/20260922-gcfpe-round30. **NOT MERGED.**
Read the branch HEAD, not a pinned commit. Round 28's lesson stands: a pinned commit produced a
stale copy whose §6 and §7 stated the opposite of the policy.
Note for this round: rounds 28 and 29 were on docs/20260921-prompt-body-policy, which merged as
**#445 and was deleted**. That evidence is now on main. Your round-29 record is on main too.
  docs/ephemeral/gcfpe.round30/REPORT-r30.md                     this round's report
  docs/ephemeral/gcfpe.round29/SECTION-10-REVIEW-r29.md          your prior verdict (on main, or PR #446)
  docs/ephemeral/gcfpe.round28/SECTION-10-REVIEW-r28.md          your round-28 verdict (on main)
  docs/prompt_ecosystem_management/prompt-body-content-policy.md the governing policy
  docs/prompt_ecosystem_management/prompt-corpus-policy.md       storage vs reading
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. R29-F1 is fixed: validator_revision 3.2.14 at four sites, FLOWMASTER_VALIDATE_REVISION 3.2.16,
    and a round-29/30 narrative paragraph in SKILL.md. Rounds 28, 29 and 30 are now mutually
    distinguishable on all three advertised values.
C2. R29-F2 is fixed by removing emphasis and code marks from the whole line before stripping the
    list/quote/heading lead-in. 21 of 21 vectors caught, including every one you named.
C3. The fix creates no new false positives. 7 of 7 controls pass, including `## Selection and
    authority` and prose that discusses lifecycle and selection.
C4. 8 fixture cases added for the newly closed shapes, 3 lines added to the prose control:
    164 → 172. No case removed.
C5. change-flow is byte-identical to rounds 28 and 29. Contracts, graph and
    CHANGE_FLOW_SPECIALIZATION_REVISION are untouched.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. **The emphasis strip is now global to the line, not a prefix.** That is a bigger hammer than
    round 29's and the false-positive surface grew with it. `governance_line_normalised` removes
    every `*`, `_`, backtick and `~` in the line before matching. Hunt the corpus for a line that
    now fires and should not — a body that quotes the forbidden field name while forbidding it, a
    template block, a table of field names. You found the last false-positive answer by looking;
    look again, because my controls are again ones I chose.
A2. **I did not fix everything R29-F2 named.** You said your correction closed 8 of 12 survivors.
    I believe this closes more, but I did not enumerate your remaining four. Name what still
    evades and decide whether it matters.
A3. **The revision bump is mechanical and I have now got it wrong twice.** Confirm 3.2.14 appears
    at exactly four executable sites and nowhere stale, that FLOWMASTER_VALIDATE_REVISION is 3.2.16
    in exactly one place, and that CHANGE_FLOW_SPECIALIZATION_REVISION is still 3.2.9 everywhere.
A4. **The SKILL.md narrative is self-assessment.** It describes the defect as round 24's F1
    repeated. Decide whether that framing is accurate or self-serving, and whether the paragraph
    would actually warn the next author.
A5. **Fixture arithmetic:** 164 + 8 reject + 0 accept = 172. Confirm by comparing case NAME sets,
    not counts — that is how you caught it last time.

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. AF-004 stands: 42 of 55 bodies have never been scanned for a decorated governance line.
    Deferred by the Product Owner on 2026-09-21 to the next GCFPE-MGMT-10 run. Round 30 widens
    what such a scan would catch. Not claimed closed.
L2. The 55 prompt bodies live in Notion. **Reading them is not restricted; persisting, copying or
    hashing them is.** Page ids are in project-prompt-contract-registry.md under notion_page_id.
L3. The dated source_bindings capture in docs/graph/parts/global.json still reads
    UNSELECTED_CANDIDATE, deliberately, under AUTH-001.
L4. The §8b TypeError on passing the graph contract where the direct-handoff contract is expected
    is pre-existing and unrepaired.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1, including any ad-hoc importlib call.
  a. Extract each archive. Confirm counts, byte sizes and sha256 in §1 from the bytes you were
     given. No traversal, `name:` unchanged.
  b. Extract side by side, restore the whole synced directory around them, and run the five gates
     FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
  c. Three-way diff: change-flow against round 29 must show zero differences.
     flowmaster-validate must differ in the validator, the fixture runner, the profile and
     SKILL.md, and nothing else.
  d. Re-falsify the matcher: every vector from rounds 28 and 29, every one in §6 A1 and A2, and
     your own inventions. Then run the false-positive controls, and go find a real one.
  e. **Prove the identity collision is gone.** Extract rounds 28, 29 and 30 side by side and
     confirm all three differ in FLOWMASTER_VALIDATE_REVISION, validator_revision and
     SKILL_TREE_SHA256. Confirm no two packages in this repair advertise the same identity.
  f. Confirm no hash pin moved: contract 2b78f877… / 606657, graph 90021eb7… / 569835, and both
     bundled contract copies byte-identical.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  validate_gcfpe_20260914.py        ok: true, errors: []
  run_gcfpe_20260914_fixtures.py    fixture_suite_ok: true, 172 cases
  validate_flowmaster.py            suite_ok: true, FLOWMASTER_SUITE_PASS, self_identity OK
  validate_gcfpe_current.py         ok: true, errors: []
  change-flow/…                     PASS

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat your round-29 conclusions about flowmaster-validate as carrying.
Do not edit any prompt body in Notion — read only. Do not write to docs/pfcanon/. Do not build a
local copy of the prompt corpus, persist prompt bodies, or hash them; that policy restricts
STORAGE, not reading.

=== 10. THE DELIVERABLE ===
One verdict: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it explicitly to the digests in §1
and state that it is void for any other bytes. For each finding give the artifact, the exact
defect, the evidence, and the smallest correction. Answer every §6 item explicitly. State which
gates you ran and which you could not.
Write a successor record; do not correct an earlier dated record in place (AUTH-001). Include the
disposition of both prior findings and any defect found while checking the fixes.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
