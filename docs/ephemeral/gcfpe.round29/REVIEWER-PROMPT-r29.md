You are SFR-01, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

This is a RE-REVIEW of your own SKILL_REPAIR_REQUIRED verdict on round 28.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
change-flow.skill           21 files   242827 bytes   sha256 ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860
flowmaster-validate.skill   29 files   286739 bytes   sha256 423458d9f0a61f89d301a4ee8e1f7819aad554b8c5cd149dc17b50478a481f69

The two packages install TOGETHER and must be reviewed together.

**change-flow.skill is byte-identical to the one you reviewed in round 28.** Same 242827 bytes,
same ed7041c0… Both corrections are in flowmaster-validate. Your round-28 findings on change-flow
— none — therefore apply to identical bytes, but that is for you to confirm, not to assume.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Prior verdict: SKILL_REPAIR_REQUIRED, round 28, issued by you against
  change-flow.skill          ed7041c0… (21 files, 242827 bytes)
  flowmaster-validate.skill  b5f5d3a3… (29 files, 285630 bytes)

flowmaster-validate's digest has changed; nothing you concluded about it carries.
change-flow's has not; you may reuse your own round-28 measurements on it if you choose to, and
say so explicitly if you do.

Disposition of every round-28 finding:
  F1  prompt_body_governance_state evaded by indentation and Markdown decoration   — FIXED
  F2  validation profile asserts UNSELECTED_CANDIDATE about the contract it pins    — FIXED
No finding declined. No finding deferred. One defect found while fixing them: the round-28
fixture suite tested only undecorated input, which is why F1 survived it; that is repaired as
part of F1 rather than logged separately.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline is the currently installed tree, which is still the round-27 release:
  change-flow            21 files, digest 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
  flowmaster-validate    29 files, digest 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
Repaired trees:
  change-flow            21 files, digest 80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8   (= round 28)
  flowmaster-validate    29 files, digest 5da1c46b913a3494a17e72760384e524f37b6d76d94085495c444111b49ecb85
flowmaster-validate declares SKILL_TREE_SHA256: 740844f0ba0fd7bd655f0cf703ac75e9063c102e849bfbf951154cba0053ae76
(different recipe from the freeze digest — it excludes its own declaration line; both correct,
not meant to match). change-flow carries no such declaration and is not meant to.
Recipe: docs/prompt_ecosystem_management/freeze.py, ROOTED AT THE SKILL DIRECTORY.
Reproduce the baseline first. If it does not reproduce, stop and say so.

Superseded, do not chase: round-28 flowmaster-validate b5f5d3a3… / 13353ffe… / 8ed6d8b0…

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch docs/20260921-prompt-body-policy. **NOT MERGED.**
This prompt was delivered at branch head 08091481 or the commit immediately after it — the lag is
structural, because the commit that adds this file cannot contain its own hash. **Read the branch
HEAD, not a pinned commit.** Round 28 pinned a commit and you were handed a copy two commits
stale, whose §6 and §7 stated the opposite of the policy. Any commit after this one only corrects
this prompt; none of them change the packages, whose digests are fixed in §1.
  docs/ephemeral/gcfpe.round29/REPORT-r29.md                     this round's report
  docs/ephemeral/gcfpe.round28/SECTION-10-REVIEW-r28.md          your own prior verdict
  docs/prompt_ecosystem_management/prompt-body-content-policy.md the governing policy
  docs/prompt_ecosystem_management/prompt-corpus-policy.md       storage vs reading — read this
  docs/prompt_ecosystem_management/freeze.py                     the digest recipe
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
C1. F1 is fixed by stripping leading whitespace and Markdown lead-in (block quote, bullet, bold,
    italic) before matching, and by testing the authority line as a substring of the stripped line
    rather than by list equality. All nine vectors you named are caught.
C2. The fix does not create false positives. Ordinary prose that discusses lifecycle or selection
    still passes — including lines that instruct the reader to resolve lifecycle from the register,
    which several real bodies contain.
C3. F2 is fixed by renaming to selection_status_during_staging in both the profile and
    load_profile's required subset, matching the file's three existing _during_staging siblings.
    The assertion moved rather than disappearing: reverting to the bare name fails
    PROFILE_CONTRACT_PIN.
C4. The round-28 fixture suite tested only undecorated input. Seven decorated vectors and one
    prose control are added: 164 cases, up from 156.
C5. change-flow is byte-identical to round 28. Contracts, graph and revisions are untouched by
    this round.
C6. A1's residual is UNCHANGED and is not claimed to be closed. See §7 L1.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. **The strip regex is the whole of F1's fix, and I wrote it from your vector list.** It is
    `^[\s>*\-+]*(?:\*\*|__|\*|_)?\s*`. Find what it still misses. Candidates I did not test:
    HTML entities, a leading `#` heading marker, `1.` ordered-list prefixes, non-breaking space,
    zero-width characters, `~~strikethrough~~`, nested emphasis, a line where the key itself is
    split by emphasis such as `**Lifecycle**: X`. That last one I believe evades and I have not
    fixed it — decide whether it matters.
A2. **The false-positive control is one fixture case that I chose.** A real body that legitimately
    begins a line with a stripped-to `Selection status:` prefix would now fail the gate. Look for
    one in the corpus. Reading is unrestricted.
A3. **F2 may be the wrong shape of fix.** Renaming makes the sentence true, but the profile still
    cannot express the contract's actual selection state, and `load_profile` still cannot see the
    contract. I did not restructure. Decide whether renaming is sufficient or merely quiet.
A4. **I did not re-audit change-flow** beyond confirming byte-identity, on the grounds that you
    already reviewed those exact bytes. That is an assumption about your prior work, not a
    measurement of mine.
A5. **The fixture count arithmetic:** 156 + 7 decorated + 1 prose control = 164. Confirm no case
    was silently removed.

Questions carried from round 28, unchanged and still open as questions: Q1 the graph's
CANDIDATE-GRAPH contract_id and FROZEN_FOR_CANDIDATE_AUTHORING status; Q2 the lane hubs' "Candidate
prompt"/"Candidate binding" column headers; Q3 candidate_url / candidate_version node keys. You
answered "leave all three, with reasoning" and I have left all three.

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. **A1's residual is exactly where you left it: 13 of 55 bodies directly confirmed.** The sweep
    with the corrected tool — the thing you identified as closing it — HAS NOT BEEN RUN. I am not
    claiming it was. The 42 unread bodies still rest on an argument whose blind spot was F1.
L2. The 55 prompt bodies live in Notion, not the repository. **Reading them is not restricted;
    copying, persisting or hashing them is.** Read whatever you need; keep none of it. Page ids are
    in docs/prompt_ecosystem_management/project-prompt-contract-registry.md under notion_page_id.
L3. The dated source_bindings capture in docs/graph/parts/global.json still reads
    UNSELECTED_CANDIDATE, deliberately, under AUTH-001. Unchanged from round 28.
L4. The §8b TypeError on passing the graph contract where the direct-handoff contract is expected
    is pre-existing and unrepaired. You confirmed it is not introduced by this work.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1 — including any ad-hoc importlib call, which is how round 28's review
contaminated its own scratch tree.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, no traversal, `name:` unchanged.
  b. Extract side by side, restore the whole synced directory around them (§3g — a two-skill copy
     produces phantom SKILL_MISSING), and run the gates FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
     Read each tool's own top-level flag by name.
  c. Diff both extracted trees against the round-28 packages, not only against the installed tree.
     change-flow must differ in nothing. flowmaster-validate must differ in exactly three files:
     the validator, the fixture runner, and the validation profile — plus SKILL.md's digest line.
  d. Re-falsify F1 directly: import prompt_body_governance_state and run every vector from your
     round-28 table, plus the ones in §6 A1. Then run your own inventions.
  e. Re-falsify F2: set candidate_contract.selection_status_during_staging back to the bare name
     and confirm PROFILE_CONTRACT_PIN fires.
  f. Confirm no hash pin moved: contract 2b78f877… / 606657, graph 90021eb7… / 569835, revisions
     3.2.9 / 3.2.15 / 3.2.13, and both bundled contract copies byte-identical.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  validate_gcfpe_20260914.py        ok: true, errors: [], SELECTED_PRODUCTION
  run_gcfpe_20260914_fixtures.py    fixture_suite_ok: true, 164 cases
  validate_flowmaster.py            suite_ok: true, FLOWMASTER_SUITE_PASS, self_identity OK
  validate_gcfpe_current.py         ok: true, errors: []
  change-flow/…                     PASS

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat your round-28 conclusions about flowmaster-validate as carrying to
these bytes. Do not edit any prompt body in Notion — read only. Do not write to docs/pfcanon/.
Do not build a local copy of the prompt corpus, persist prompt bodies, or hash them; that policy
restricts STORAGE, not reading — read whatever the review needs and keep none of it.

=== 10. THE DELIVERABLE ===
One verdict: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it explicitly to the digests in §1
and state that it is void for any other bytes. For each finding give the artifact, the exact
defect, the evidence, and the smallest correction. Answer every §6 item explicitly; a question is
not a finding. State which gates you actually ran and which you could not.
Write a successor record; do not correct an earlier dated record in place (AUTH-001). Include the
disposition of both prior findings and any defect found while checking the fixes.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
