You are SFR-01, performing independent validation of one skill change. You did not author it.
Nothing is installed and nothing may be installed until you rule. No skill may be installed while
you are reviewing; if the tree moves under you, the review is void — say so and stop.

=== 1. WHAT THIS VERDICT IS SCOPED TO ===
change-flow.skill           21 files   242827 bytes   sha256 ed7041c0ee2179afcc0b684954f0605fd5ab495fea203a4dfafd7eb3f97c7860
flowmaster-validate.skill   29 files   285630 bytes   sha256 b5f5d3a338a2cd7dafe8436b73af6713dec0633403ed03a24e026d4f2439fd36

The two packages install TOGETHER and must be reviewed together. They share both bundled
contracts byte-for-byte, and each fixes a gate in the other's promotion path: reviewing or
installing one alone leaves the ecosystem in the contradictory state this round exists to repair.

=== 2. THE PRIOR VERDICT, AND WHAT DOES NOT CARRY ===
Prior verdict: SKILL_FIT_CONFIRMED, round 27, 2026-09-21, issued against
  change-flow            21 files, freeze digest 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
  flowmaster-validate    29 files, freeze digest 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
  SKILL_TREE_SHA256      6f682315a9437c1275688d568ee8b79baeccdd52f9c896b89fdd617a46863a93

Both digests have changed. **Nothing from that verdict carries.** Every file that moved is listed
in §3, and the independent post-flight of 2026-09-21 (PASS WITH WARNINGS) was scoped to the
release as it then stood; its three warnings are dispositioned in §5, C6.

Findings carried forward: NONE.

=== 3. BASELINE, SO IDENTITY REPRODUCES BEFORE ANYTHING ELSE ===
Baseline is the currently installed tree.
  change-flow            21 files, digest 14981ba71e6fe400b4ae0d42410ce9bd9144e5b02bf73bfa53f2a823193240c2
  flowmaster-validate    29 files, digest 9c0ca6fe1811e444193daccf67c29a65d9f623fcf4d1e255095ae932a646a833
Repaired trees (extract the packages, then measure):
  change-flow            21 files, digest 80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8
  flowmaster-validate    29 files, digest 13353ffed880aa0337b90f91aba4302b450708cacae91b042edee78583c8d289
Recipe: docs/prompt_ecosystem_management/freeze.py, ROOTED AT THE SKILL DIRECTORY, never at the
synced tree. Reproduce the baseline first. If it does not reproduce, stop and say so.

flowmaster-validate declares SKILL_TREE_SHA256: 8ed6d8b00240d04a72e1caa69a0f1c4be473913d1035d36534d1a030bbaf5f23.
That is a DIFFERENT recipe from the freeze digest — it excludes its own declaration line. Both
values are correct and they are not meant to match. change-flow carries no such declaration and
is not meant to.

Superseded, do not chase: contract 1c3c7969… / 610549 bytes and graph 1d0b7258… / 569902 bytes.
Both were correct through round 27 and appear in every earlier record.

=== 4. WHERE THE REPOSITORY EVIDENCE IS ===
Repository amthorn78/glow-hdengine-v2. Branch docs/20260921-prompt-body-policy, commit b83bd1070b2437184c17b5ac254a7cfcd52380dc.
**NOT MERGED.** Do not look on main; the graph parts and the policy are only on that branch.
  docs/prompt_ecosystem_management/prompt-body-content-policy.md   the governing policy
  docs/ephemeral/gcfpe.round28/REPORT-r28.md                       this round's report
  docs/prompt_ecosystem_management/freeze.py                       the digest recipe
  docs/graph/parts/                                                the graph source, 56 files changed
  docs/ephemeral/gcfpe.promotion-20260921/PROMOTION-RECORD-20260921.md   why the release is selected
Read AGENTS.md first. It governs.

=== 5. WHAT THE CHANGE CLAIMS, AS CLAIMS ===
The authority is the Product Owner, 2026-09-21, verbatim: *"yes fix it. and create a policy that
such things should not be appended to prompts in the future. prompt bodies may not be changed."*
Clarified in the same conversation: *"I mean of course they may be changed but not with useless
unapproved things like that."*

C1. A prompt body's only consumer for its selection line was the check that verified the line.
    SELECTION_HEADER_KEYS appears in exactly one function; that function derived the expected
    value from the contract's own status and confirmed the body repeated it.
C2. There was no mode in which the line was absent. In production mode the validator required it
    to read REGISTER_CONTROLLED **and** required a second line asserting the register's authority.
    Promotion grew the metadata rather than removing it.
C3. 091326.2 — the release that actually ran — carries no such line on any of its 54 bodies.
C4. Three coupled defects made a promoted release unreachable, each requiring the release to still
    be a candidate: change-flow's selection_status gate; change-flow's candidate_page_binding
    requirement, which promotion removes and flowmaster-validate rejects in production; and
    validate_graph_contract pinning the graph to UNSELECTED_CANDIDATE with no production branch.
C5. All 55 prompt bodies were cleaned: the selection line removed, Candidate Notion URL: renamed
    to Notion URL:, and NO selection-authority line added. Two header dialects existed in the
    corpus — `Lifecycle:` and `Selection status:` — and both are now rejected.
C6. The round-27 post-flight's three warnings are unaffected by this change and remain open as
    warnings: the §3g scratch-copy scope, the 721-vs-831 assertion count, and fixture_suite_ok
    not being qualified by families that evaluated nothing.

=== 6. WHAT TO ATTACK, IN PRIORITY ORDER ===
A1. **The claim that all 55 bodies are clean is the weakest thing here.** I did not read 55
    bodies — the corpus policy forbids it. My proof is indirect: 55 exact-match replaces each
    succeeded, and the OLD validator enforced len(status_lines) == 1, so exactly one line existed
    per body and exactly one was removed. Test that reasoning. If you can falsify it on even one
    prompt, the claim fails. Read any prompts you need directly from Notion.
A2. **prompt_body_governance_state is a check I wrote to test my own change.** It is a substring
    scan over SELECTION_HEADER_KEYS plus one literal. Ask what it misses: a lifecycle line with
    leading whitespace, a different key, the same fact stated in prose.
A3. **I removed a production mode rather than fixing it.** Verify nothing else depended on
    production_mode inside prompt_identity_header_valid, and that the remaining production_mode
    branches in validate_contract are untouched and still correct.
A4. **The graph now mirrors the contract instead of pinning a literal.** That makes the graph
    unable to disagree — but also unable to catch a contract whose selection_status is wrong.
    I added GRAPH_SELECTION_STATUS to bound the value. Decide whether that is sufficient.
A5. **PR-35's node lifecycle was UNSELECTED_CANDIDATE_NEW_MEMBER and is now SELECTED_PRODUCTION.**
    I claim the "new member" fact survives in sole_added_member and the graph's member_rule.
    Confirm it, or find where that fact is now absent.
A6. **The fixture suite went from 155 to 156 cases.** I replaced 8 header cases with 8 of my own
    design. Read them: they are the checks the author built to test the author's work.

Questions this round deliberately did NOT settle, marked as questions, not findings:
Q1. The graph contract keeps contract_id GCFPE-20260914.1-CANDIDATE-GRAPH and status
    FROZEN_FOR_CANDIDATE_AUTHORING. Both are release-phase names on a selected release. I left
    them because changing an id cascades further than this round's scope. Should they move?
Q2. The five lane hubs' topology tables still head their columns "Candidate prompt" and
    "Candidate binding". Control pages, not prompt bodies, so the policy does not reach them.
Q3. member_registry node keys candidate_url and candidate_version keep candidate naming.

=== 7. KNOWN LIMITS, VOLUNTEERED ===
L1. The 55 prompt bodies live in Notion and are NOT in the repository, by standing Product Owner
    policy. You cannot diff them. Read any page you need directly; the page ids are in
    docs/prompt_ecosystem_management/project-prompt-contract-registry.md under notion_page_id.
L2. I did not run the body-level gate against all 55 live bodies. Doing so would be a corpus read
    the policy prohibits. If you want body-level evidence, read the prompts you judge necessary
    and pipe them with --bodies-stdin.
L3. The dated source_bindings capture in docs/graph/parts/global.json still reads
    UNSELECTED_CANDIDATE. That is deliberate: it is a dated repair-snapshot observation marked
    EVIDENCE_ONLY, and AUTH-001 forbids rewriting one.

=== 8. WHAT TO EXECUTE ===
Work from a scratch copy. Never write to the synced skills directory. Run everything with
PYTHONDONTWRITEBYTECODE=1.
  a. Extract each archive. Confirm the file counts, byte sizes and sha256 in §1 from the bytes you
     were given. Confirm every entry sits under its skill root, with no traversal sequences and no
     entry outside it. Confirm `name:` in each SKILL.md frontmatter is unchanged (change-flow,
     flowmaster-validate).
  b. Extract into a clean tree. Each archive contains its own top-level skill directory, so
     extract them side by side, not into a directory of the same name. Then restore the untouched
     sibling skills — §3g means the WHOLE synced directory; a two-skill copy makes the gates
     report phantom SKILL_MISSING errors because validate_gcfpe_20260914.py resolves siblings
     from change_skill_dir.parent. Run the gates FROM THE EXTRACTED CONTENTS:
       python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py change-flow --contract change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
       python3 flowmaster-validate/scripts/validate_flowmaster.py
       python3 flowmaster-validate/scripts/validate_gcfpe_current.py change-flow
       python3 change-flow/scripts/validate_gcfpe_20260914.py
     The contract argument is the DIRECT-HANDOFF contract. Passing the graph contract instead
     raises TypeError: 'NoneType' object is not iterable at validate_contract — a crash, not a
     message. Read each tool's own top-level flag by name. A green section count beside a false
     suite flag means the suite failed.
  c. Confirm the extracted trees differ from the installed tree only in the files the report
     names, and that the report accounts for every difference.
  d. Confirm the promotion transition is complete and coherent in the direct-handoff contract:
     status and selection_status SELECTED_PRODUCTION; contract_id ends -DIRECT-HANDOFF-SELECTED;
     selection_claim and publication_evidence both true; selected_member_count 55; all 55
     member_registry and notion_page_manifest entries SELECTED_PRODUCTION; all 55 member
     lifecycles SELECTED_PRODUCTION; NO member retains candidate_page_binding; the five prompt
     references and alpha_resumption_contract.successor_trigger.prompt all SELECTED_PRODUCTION.
     Count zero occurrences of UNSELECTED_CANDIDATE in that file.
  e. Recompute every hash pin from its artifact and confirm each consumer agrees:
     contract 606657 bytes; graph 569835 bytes; the graph pin inside the contract at
     source_snapshot.frozen_candidate_graph.sha256; EXPECTED_FROZEN_GRAPH_SHA256 and
     EXPECTED_CANDIDATE_CONTRACT_SHA256 and their byte constants; change-flow's
     EXPECTED_GRAPH_SHA; and the validation profile's candidate_contract and frozen_graph blocks.
     Confirm both bundled copies of each contract are byte-identical.
  f. Rebuild the graph from docs/graph/parts/ with the glow-graph-contract skill's graph_parts.py
     and confirm it reproduces 55 nodes, 227 edges, 55 state_routes and sha256 90021eb7…
     independently of my number. Recount every revision site by grep: CHANGE_FLOW_SPECIALIZATION_
     REVISION 3.2.9, FLOWMASTER_VALIDATE_REVISION 3.2.15, validator_revision 3.2.13.
Derive every digest from the artifact in front of you. Never transcribe one from the report.

The author's measurements, for you to contradict rather than confirm:
  validate_gcfpe_20260914.py        ok: true, errors: [], contract_status SELECTED_PRODUCTION
  run_gcfpe_20260914_fixtures.py    fixture_suite_ok: true, 156 cases, §13 33/33 and 28/28 variants
  validate_flowmaster.py            suite_ok: true, FLOWMASTER_SUITE_PASS, self_identity OK
  validate_gcfpe_current.py         ok: true, errors: []
  change-flow/…/validate_gcfpe_20260914.py   PASS

=== 9. WHAT NOT TO DO ===
Do not install any skill. Do not write to the synced skills directory. Do not merge and do not
enable auto-merge. Do not treat the round-27 confirmation as carrying to these bytes. Do not edit
any prompt body in Notion — read only. Do not write to docs/pfcanon/. Do not build a local copy of
the prompt corpus, hash prompt bodies, or compare them byte-for-byte; the Prompt Corpus Storage
and Fidelity Policy prohibits it, and if a procedure you are given conflicts with it, report that
and stop rather than working around it.

=== 10. THE DELIVERABLE ===
One verdict, using exactly this vocabulary: SKILL_FIT_CONFIRMED or SKILL_REPAIR_REQUIRED. Bind it
explicitly to the digests in §1 and state that it is void for any other bytes. For each finding give
the artifact, the exact defect, the evidence, and the smallest correction. Answer every §6 question
explicitly; a question is not a finding.
State which gates you actually ran and which you could not, plainly, rather than inferring a result.
Write a successor record; do not correct an earlier dated record in place (AUTH-001).
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
