---
artifact_type: GCFPE_MODIFICATION_EVIDENCE
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
also_serves: MODIFICATION-20260923-pr40-reject-replans
kind: EXECUTE preflight and critique, read-only
executed: 2026-09-23
workflow_runs:
  - wf_c18f4ad8-bae — four preflight readers. Its critic was interrupted and returned nothing.
  - wf_d3847211-6a7 — three critics of the first amendment draft.
supersedes: the table rendering committed in f0a3437, which escaped '|' inside regexes
---

# EXECUTE preflight and critique — every finding

Before editing anything, EXECUTE checked every step of the approved plan against the installed
skills, the fixtures, the graph parts and the registry.
- **Part 1** holds 121 findings from four readers, each on one surface.
- **Part 2** holds 77 findings from three critics of the first draft of `Amendment 1`.

**How the readers and critics worked:**
- They read no prompt body.
- They wrote nothing to the installed skills, the repository or Notion.
- They ran Python with `PYTHONDONTWRITEBYTECODE=1`, on copies under `/tmp/claude-0/` only.
- An effect marked `WOULD_FAIL` was measured by simulation on those copies, unless its text says it
  was inferred.

**How this file was produced.** It is rendered mechanically from the structured output in the
workflow journals, so no finding was retyped. Every value that may hold a regex, code or a quoted
literal is in a fenced block, unescaped and unabridged. The first rendering, in `f0a3437`, used
table cells, escaped `|`, and so corrupted the regexes in steps 7 and 17 (critic `adversary:6`).

**What answers them.** The plan's response is `Amendment 1` in the Modification's §P, with its
execution specification. The specification's §1 gives the disposition of all 198 findings.

## Part 1 — preflight readers (workflow wf_c18f4ad8-bae)

### fv-main — flowmaster-validate main validator (36 findings)

#### `fv-main:0` — WOULD_FAIL — step 42 (PART-12)

- **Check or surface:** PROMPT_BODY_IDENTITY (prompt_identity_header_valid)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1068-1078 (regex :910, comment :904-908)

- **Asserts**

```text
len(nonblank) >= 7 and nonblank[0] == member.get("title") and any(PROMPT_VERSION_HEADER_RE.match(line) for line in nonblank[:8]) ... and any(line in header_value_lines("Ecosystem release:", "GCFPE-20260914.1") for line in nonblank[:8])
```

- **Required plan step**

```text
Before step 46, in the flowmaster-validate package: rewrite prompt_identity_header_valid so title, one neutral `Notion URL:` and `Prompt ID:` stay required. Lines starting `Prompt [Vv]ersion:`, `Set:` or `Ecosystem release:` (after governance_line_normalised) become a new error code, e.g. PROMPT_BODY_RELEASE_HEADER, mirroring step 43's registry forbidden_regex. Re-derive the `len(nonblank) >= 7` floor, which counted the three deleted lines. Rewrite the :904-908 comment, which cites the registry `Prompt [Vv]ersion` regex that step 43 removes, to cite D23-G.
```

- **Invariant**

```text
D23-G deliberately reverses this, turning a required line into a forbidden one. The identity half (exact title, Prompt ID matching its key, one unlabeled Notion URL) is kept and must stay guarded. Measured: a post-step-42 header with 8 nonblank lines returns False, so every body supplied via --bodies-stdin raises PROMPT_BODY_IDENTITY:<id>. Confirms the already-known defect.
```

#### `fv-main:1` — WOULD_FAIL — step 42 (PART-12)

- **Check or surface:** fixture accept-identity-only-prompt-header plus the 4 URL-label negatives built on clean_header
- **Location:** flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:420-455

- **Asserts**

```text
clean_header = [ pr35["title"], "Prompt Version: 091426.1", "Set: Glow HDE Complete Prompt Flow 091426.1", "Prompt ID: PR-35", "Ecosystem release: GCFPE-20260914.1", f"Notion URL: {pr35['notion_url']}", "## Native purpose", ] ... "name": "accept-identity-only-prompt-header"
```

- **Required plan step**

```text
Rewrite clean_header without the three release lines, keeping enough nonblank lines for the new floor. Add negatives reject-release-header-prompt-version, -set and -ecosystem-release, including decorated forms (bold, bullet, quote), using the same vector list as the governance-state cases. Keep the four URL-label negatives.
```

- **Invariant**

```text
The positive case asserts the retired rule. It fails once the validator is inverted. If the validator is not inverted, it stays green while certifying headers that D23-G forbids, which is a check quietly weakened. The URL-label negatives guard a kept invariant.
```

#### `fv-main:2` — WOULD_FAIL — step 29 (PART-09)

- **Check or surface:** PR35_ADDED_BOUNDARY
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1742-1743

- **Asserts**

```text
if not isinstance(development, dict) or any(value != 0 for value in development.get("added_boundaries", {}).values()): errors.append("PR35_ADDED_BOUNDARY")
```

- **Required plan step**

```text
Replace with exact-map equality: added_boundaries == {approval:0, cross_session_route:0, duplicate_work_vehicle:0, merge_authority:0, proceed:0, product_owner_gate:0, r1_row:0, role:0, session:1, work_unit:0, work_vehicle:0}. Keep fixture reject-new-proceed-boundary (runner:359). Add reject-pr35-shared-session (session back to 0) and reject-cross-session-route=1. Step 29 must also name the graph key correctly: global.json holds pr_continuity_contract.adds.session, not added_boundaries. :1303 compares continuity.adds with development.added_boundaries, and nothing checks the global.json key set, so a transform that writes `added_boundaries` into the graph adds an unchecked key, leaves adds.session at 0, and nothing flags it.
```

- **Invariant**

```text
Reversed for `session` only (D23-D). The other ten keys guard a kept invariant: PR-35 adds no Proceed, approval, role, work unit or R1 row. Do not relax the check to 'ignore session'. Measured with lockstep contract: PR35_ADDED_BOUNDARY fires.
```

#### `fv-main:3` — WOULD_FAIL — step 29 (PART-09)

- **Check or surface:** PR_PHASE_CONTINUITY / EXPECTED_PHASE_CONTINUITY
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:876-880, 1744-1745

- **Asserts**

```text
EXPECTED_PHASE_CONTINUITY = ["WORK_UNIT_ID", "original Product Owner Proceed", "dedicated PR-development session", "workspace/worktree", "branch", "pull request", ...]; if ... development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY: errors.append("PR_PHASE_CONTINUITY")
```

- **Required plan step**

```text
Set EXPECTED_PHASE_CONTINUITY to the nine remaining fields in the same order. Keep the exact ordered-list comparison, and add an explicit absence assertion for 'dedicated PR-development session'. Update contract pr_development_contract.shared_exactly_one in both bundled copies in the same edit.
```

- **Invariant**

```text
Kept for nine fields, including the one pull request that ITEM-16 requires. Reversed for the session field. Measured: fires once the contract is updated in lockstep.
```

#### `fv-main:4` — WOULD_FAIL — step 29 (+15) (PART-09)

- **Check or surface:** GRAPH_PR_CONTINUITY_MISMATCH (graph vs contract parity)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1298-1316

- **Asserts**

```text
continuity.get("adds") != development.get("added_boundaries") or set(continuity.get("shared_exactly_one", [])) != set(development.get("shared_exactly_one", []))
```

- **Required plan step**

```text
Widen step 15 beyond transition_contract. pr_development_contract (shared_exactly_one, added_boundaries) is a contract-only key with no source in the graph parts and no generator, so it must be authored in lockstep with the global.json edit.
```

- **Invariant**

```text
Kept: parity between the graph and the contract. Measured: fires when the graph changes and the contract does not.
```

#### `fv-main:5` — WOULD_FAIL — step 29/30 (PART-09)

- **Check or surface:** fixture PR-SPLIT-POS-01 (pr_split projection)
- **Location:** flowmaster-validate/fixtures/gcfpe-20260914.1-091426.1/scenarios.json:35; run_gcfpe_20260914_fixtures.py:66-70

- **Asserts**

```text
if development.get("phases") == ["PR-30", "PR-35"] and all(value == 0 for value in development.get("added_boundaries", {}).values()): return "PR30_TO_PR35_SAME_SESSION"
```

- **Required plan step**

```text
Rewrite the pr_split projection and PR-SPLIT-POS-01: the input carries new_dedicated_pr35_session:true, and the expected value becomes, e.g., PR30_TO_PR35_NEW_DEDICATED_SESSION, gated on the exact added_boundaries map. Then update EXPECTED_FIXTURE_SHA256 (validate_gcfpe_20260914.py:945) and profile fixtures.sha256 (validation-profile.json:15).
```

- **Invariant**

```text
Reversed (D23-D). Measured: projects VALIDATION_FAILURE against the lockstep contract.
```

#### `fv-main:6` — WOULD_PASS — step 29/30 (PART-09)

- **Check or surface:** stale negatives: PR-SPLIT-NEG-01::new-session-only and independent-requests_new_session
- **Location:** run_gcfpe_20260914_fixtures.py:60, 324; scenarios.json:37

- **Asserts**

```text
if facts.get("requests_additional_proceed") or facts.get("requests_new_session"): return "VALIDATION_FAILURE"
```

- **Required plan step**

```text
Remove or invert the new-session variant and the independent new-session case. Keep the extra-proceed variant and its independent case. If the polarity or id count moves, update the literals it touches: 33 ids (runner:258), 18 POSITIVE/15 NEGATIVE (runner:267), EXPECTED_NEGATIVE_RULES (runner:31-47, 'PR-SPLIT-NEG-01': 'PR35_ADDED_BOUNDARY'), the fixture sha pin and the profile count.
```

- **Invariant**

```text
These stay green while asserting the reversed rule that a new PR-35 session is a failure. They will not flag themselves. The extra-Proceed half guards a kept invariant: D23-F's new Proceed applies only to a PR-40 re-plan, never inside PR-30 to PR-35.
```

#### `fv-main:7` — WOULD_PASS — step 29/30 (13) (PART-09/PART-04)

- **Check or surface:** handoff fixtures HANDOFF-POS-01 and independent-handoff-*
- **Location:** scenarios.json:58, 60; run_gcfpe_20260914_fixtures.py:175, 332

- **Asserts**

```text
if facts.get("origin") == "PR-30" and facts.get("receiver") == "PR-35" and facts.get("same_session") and common: return "PR35_HANDOFF_ACCEPTED"
```

- **Required plan step**

```text
Change the PR-30 to PR-35 acceptance rule to require a new dedicated PR-35 receiving session (same_session false, same WORK_UNIT_ID and PR). Flip the inputs in HANDOFF-POS-01, HANDOFF-NEG-01 and the independent cases. Keep the metadata_only, blank_field, library_id, uses_above and unlinked_filename negatives.
```

- **Invariant**

```text
Same-session acceptance is reversed. The runnable-prompt negatives are kept by C-HANDOFF ('No placeholders, menus ... unlinked filenames') and must stay.
```

#### `fv-main:8` — WOULD_FAIL — step 30 (child if PR-20 role edited) (PART-09 / CHILD)

- **Check or surface:** GRAPH_NODE_CONTRACT:<id> (11 paired node/registry fields)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1221-1237

- **Asserts**

```text
paired_fields = {"candidate_url": "notion_url", "candidate_version": "version", "title": "title", ..., "receiving_role": "receiving_role", "session_class": "session_class", ...}
```

- **Required plan step**

```text
In step 15, update contract member_registry['PR-35'].session_class (DEDICATED_PR_REVIEW_SESSION) and .receiving_role in both copies, byte-for-byte equal to the PR-35.json node. If the child edits PR-20's node receiving_role to accept a successor session, update member_registry['PR-20'] the same way.
```

- **Invariant**

```text
Kept: node and registry parity. Measured: GRAPH_NODE_CONTRACT:PR-35 fires when only the graph changes.
```

#### `fv-main:9` — WOULD_FAIL — step 23, 31, 38, CHILD (PART-07/09/11, CHILD)

- **Check or surface:** ROUTING_SURFACE_CHANGED
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:207-208, 1673-1675

- **Asserts**

```text
EXPECTED_ROUTING_SURFACE = "7380cd14430777675f1e8b2cdfa4a0da"
EXPECTED_ROUTING_SURFACE_ROWS = 282
```

- **Required plan step**

```text
After the final build, add a step that diffs route_edges and state_routes (old vs new contract) and records the diff in §E. A human reads it, then both constants are re-pinned. Rows stay 282 if the NATHAN_MANUAL_MERGE_ASSERTION edge is kept and become 281 if it is removed; the full simulation measured 7e56a9da8507e1a6e4b14dbd60977bae/281, but the exact digest depends on final wording.
```

- **Invariant**

```text
A change detector, re-pinned deliberately. Its own comment (:203-205) says 'Re-pinning is a deliberate act a human performs after reading the diff', so the re-pin cannot be scripted. Measured: fires for each of steps 23, 31, 38 and the child separately, even with the contract in lockstep.
```

#### `fv-main:10` — WOULD_FAIL — step 23, 31, 38, CHILD (15) (PART-07/09/11, CHILD)

- **Check or surface:** GRAPH_EDGE / STATE_ROUTE / BOUNDARY_TRANSITION / BOUNDARY_NODE / POST_MERGE contract mismatch
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1241-1257

- **Asserts**

```text
if graph.get("edges") != contract.get("route_edges"): errors.append("GRAPH_EDGE_CONTRACT_MISMATCH") ... if graph.get("post_merge_three_event_contract") != contract.get("post_merge_three_event_contract"):
```

- **Required plan step**

```text
Widen step 15 so the contract's route_edges, state_routes, boundary_transitions, boundary_nodes, post_merge_three_event_contract and graph_proofs.route_edge_count are copied from the same build whose proof token is recorded. Step 15 currently names only transition_contract (contract:17594-17618).
```

- **Invariant**

```text
Kept: graph and contract parity. Measured: these codes fire whenever the graph changes and the contract does not.
```

#### `fv-main:11` — WOULD_FAIL — step 38 (PART-11)

- **Check or surface:** DIRECT_PR35_PR40_EDGE and GRAPH_DIRECT_PR40_EDGE
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1837-1838 and 1349-1355

- **Asserts**

```text
if any(edge.get("from") == "PR-35" and edge.get("to") == "PR-40" for edge in edges ...): errors.append("DIRECT_PR35_PR40_EDGE") | edge.get("from") in {"PR-30", "PR-35"} and edge.get("to") == "PR-40" -> GRAPH_DIRECT_PR40_EDGE
```

- **Required plan step**

```text
Split both checks. Keep the PR-30 to PR-40 prohibition (:1835-1836, and PR-30 in :1351). Replace the PR-35 half with a positive rule: exactly one PR-35 to PR-40 prompt edge, automatic false (paste), transport COMPLETE_NEXT_PROMPT_HANDOFF, condition naming the observed merge event. Apply the same to RS-40 if it is routed there. Replace fixture reject-pr35-direct-pr40 (runner:361) with mutations that must fail: a PR-35 to PR-40 edge without the merge-event condition, and one with automatic:true.
```

- **Invariant**

```text
The PR-30 half is kept. The PR-35 half is deliberately reversed by D23-E. 'No agent merges' and 'no entry before Nathan merges' are kept, and the new rule must guard both. Measured: both fire.
```

#### `fv-main:12` — WOULD_FAIL — step 38 (39) (PART-11)

- **Check or surface:** PR40_MANUAL_MERGE_BOUNDARY
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1926-1948

- **Asserts**

```text
len(manual_pr40) != 1 or manual_pr40[0].get("from") != "NATHAN_MANUAL_MERGE_ASSERTION" ... or any(edge.get("from") != "DOC-20" ... "after Nathan asserts the manual merge" not in str(branch.get("condition", "")) ...
```

- **Required plan step**

```text
Rewrite the check: allowed prompt inbound edges to PR-40 are DOC-20, keeping its condition text, plus PR-35 (and RS-40) with the merge-event condition. First resolve a conflict inside the plan: step 38 turns the NATHAN_MANUAL_MERGE_ASSERTION boundary into a prompt edge (removing it), while step 39 keeps 'Nathan's assertion where no subscription existed' as a PR-40 input. If the fallback stays, keep exactly one boundary edge and keep the len==1 check. If step 39 rewords the DOC-20 body and DOC-20.json:151/169 follows it, the DOC-20 substring check fires as well.
```

- **Invariant**

```text
'PR-40 runs only after Nathan's merge, never automatically' is kept. 'The only entry is Nathan's pasted assertion' is reversed by D23-E. Measured: fires.
```

#### `fv-main:13` — WOULD_FAIL — step 38 (PART-11)

- **Check or surface:** POST_MERGE_CONTRACT and POST_MERGE_THREE_EVENTS
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1768-1780

- **Asserts**

```text
subset_errors(postmerge, {"agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False}, "POST_MERGE_CONTRACT") ... (postmerge.get("event_2") or {}).get("fact") != "product_owner_manual_merge_assertion"
```

- **Required plan step**

```text
Update the literals together with global.json. direct_PR35_to_PR40_automatic_edge becomes True per D23-E, but the plan must define the edge's own `automatic` field, which stays false in paste mode. event_2.fact takes the new value. Keep event_2.actor == 'Nathan / Product Owner', event_1 == MERGE_PENDING/pre_merge_historical_evidence, event_3 consumer PR-40 independent:true, and agent_merge_authorized False.
```

- **Invariant**

```text
Partly reversed: the trigger and the edge. Kept: Nathan is the merger, MERGE_PENDING is pre-merge evidence, and PR-40 verifies independently. Measured: both codes fire.
```

#### `fv-main:14` — WOULD_FAIL — step 38 (CHILD) (PART-11)

- **Check or surface:** ROUTE_GRAPH_SHORTHAND
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1782-1798

- **Asserts**

```text
"ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]
```

- **Required plan step**

```text
Update contract route_graph and this literal together, keeping exact equality. Decide whether the child adds a `pr40_reject_replan` shorthand (PR-40, PR-20, NATHAN_PROCEED, PR-30). If it does, add that literal too.
```

- **Invariant**

```text
The merge node is reversed. Measured: fires once the contract shorthand is updated.
```

#### `fv-main:15` — WOULD_FAIL — step 38 (PART-11)

- **Check or surface:** PROFILE_GRAPH_PIN edge_count / PROFILE_GRAPH_COUNTS
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1118, 1161-1165; validation-profile.json:20

- **Asserts**

```text
"node_count": 55, "edge_count": 227,
```

- **Required plan step**

```text
If the manual-merge boundary edge is removed, the edge count becomes 226 (measured). Update the literal at :1118, profile frozen_graph.edge_count, and contract graph_proofs.route_edge_count (227, unvalidated but stale).
```

- **Invariant**

```text
Kept: declared counts are measured against the bundled graph.
```

#### `fv-main:16` — WOULD_FAIL — step 12,23,29,30,31,34,38,CHILD,15 (multi)

- **Check or surface:** bundle byte pins: GRAPH_HASH, PROFILE_BUNDLED_GRAPH_HASH, PROFILE_GRAPH_PIN, PROFILE_BUNDLED_CONTRACT_HASH, PROFILE_CONTRACT_PIN, CONTRACT_CHANGE_FLOW_BYTE_MISMATCH
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:941-944, 1099-1151, 2513-2514, 2528-2529; validation-profile.json:2-9, 17-25

- **Asserts**

```text
EXPECTED_FROZEN_GRAPH_SHA256 = "90021eb7..."; EXPECTED_FROZEN_GRAPH_BYTES = 569835; EXPECTED_CANDIDATE_CONTRACT_SHA256 = "2b78f877..."; EXPECTED_CANDIDATE_CONTRACT_BYTES = 606657
```

- **Required plan step**

```text
Add an ordered regeneration step. (1) graph_parts.py build. (2) The bundled graph is the embedded JSON block plus a trailing newline; this is verified byte-identical today, and the proof-token sha equals EXPECTED_FROZEN_GRAPH_SHA256. Write it to flowmaster-validate/references and change-flow/references. (3) Write the proof-token sha into contract source_snapshot.frozen_candidate_graph.sha256 (contract:11543); only change-flow's validator checks it (change-flow/scripts/validate_gcfpe_20260914.py:781). (4) Write contract bytes to both skills. (5) Update the profile sha256/byte_count. (6) Update the script literals at :941-944. (7) Update the fixture pin. (8) Set SKILL_TREE_SHA256 last. Step 15 names only the contract. Also resolve a conflict: glow-graph-contract says existing assembled-graph copies must not be updated ('do not mint a replacement'), yet two skills bundle one and pin its hash.
```

- **Invariant**

```text
Kept: the bundle identity chain. Measured: every code listed fires when the new bundles are written into references without updating the pins.
```

#### `fv-main:17` — WOULD_FAIL — step 15 (PART-04)

- **Check or surface:** HANDOFF_CONTRACT and HANDOFF_PROHIBITED_REFERENCES
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1482-1500

- **Asserts**

```text
"epic_change_and_work_unit": True, "every_required_repository_and_pr_reference": True, "status_completed_work_decisions_constraints_unresolved_authority": True, "next_action_and_expected_output": True, }, "HANDOFF_CONTRACT") ... if prohibited_refs != {"Library ID", "unlinked filename", "above", ...}
```

- **Required plan step**

```text
Step 15 has no tool: no generator exists for the direct-handoff contract (grep of both skills and the repo). transition_contract is contract-only. The graph's handoff_contract `required` and `prohibited` lists never flow into it, and GRAPH_HANDOFF_CONTRACT_MISMATCH (:1259-1269) compares only first_line, fence_language, actual_branch_only, complete_paste_ready_prompt and block counts. So leaving transition_contract unchanged passes the suite while asserting the rule D23-B reverses. Add an authored mapping: status_completed_... false and next_action_and_expected_output false; decide epic_change_and_work_unit; add branch, commit and 'restated artifact content' to prohibited_references. Update :1482-1500 citing D23-B. Keep actual_pasteable_complete_prompt True, so reject-incomplete-handoff (runner:405) keeps guarding. Add a parity check that graph handoff_contract.prohibited is a subset of transition_contract.prohibited_references.
```

- **Invariant**

```text
Three booleans are deliberately reversed. prohibited_references is tightened, not weakened. The paste-ready prompt, exact destination and receiving session are kept. Measured: both codes fire on a truthful update.
```

#### `fv-main:18` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** R1 oracle pins in this validator and its references
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1130, 1379, 1964; validation-profile.json:35; direct-handoff contract protected_identities (both copies); flowmaster-validate/SKILL.md:149 and :246

- **Asserts**

```text
"r1_oracle_sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
```

- **Required plan step**

```text
Step 34's pin list omits validation-profile.json:35, the contract's protected_identities in both skills, and SKILL.md:246 (the plan names only :149). Add them. The graph copy is regenerated from global.json.
```

- **Invariant**

```text
Deliberately re-pinned by Nathan's ruling. Measured: GRAPH_PROTECTED_IDENTITIES, PROTECTED_IDENTITIES and PROFILE_PROTECTED_IDENTITIES fire.
```

#### `fv-main:19` — WOULD_PASS — step 34 (PART-09)

- **Check or surface:** PROTECTED_IDENTITIES r1_oracle_changed / GRAPH_PROOFS protected_r1_46_rows_unchanged
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1955-1956, 1965-1966

- **Asserts**

```text
"protected_primary_core_unchanged": True, "protected_r1_46_rows_unchanged": True, ... "r1_oracle_sha256": "52807e58...", "r1_rows": 46, "flowmaster_primary_core_changed": False, "r1_oracle_changed": False, "pr35_adds_r1_row": False
```

- **Required plan step**

```text
Decide and record under D23-D/F. After the re-pin, the contract's r1_oracle_changed:false and protected_r1_46_rows_unchanged:true are false in fact, and the validator enforces them. Set them truthfully (r1_oracle_changed true, rows_unchanged false or renamed) and update the literals, or redefine them explicitly as relative to the predecessor release. Keep pr35_adds_r1_row False, r1_rows 46 and flowmaster_primary_core_changed False.
```

- **Invariant**

```text
Partly reversed. Left as they are, these checks certify a falsehood. A truthful value fails them. Row count and primary-core identity are kept.
```

#### `fv-main:20` — WOULD_FAIL — step 34 (+CHILD re-pin) (PART-09 / CHILD)

- **Check or surface:** R1_RUNTIME_MAP_IDENTITY and profile r1_runtime_map_sha256
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1131, 2610-2612; validation-profile.json:37

- **Asserts**

```text
if not runtime_map.is_file() or sha256(runtime_map) != "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e": errors.append("R1_RUNTIME_MAP_IDENTITY")
```

- **Required plan step**

```text
Step 34 omits the change-flow runtime map. validate_flowmaster.py:733-757 (FMV-GCF-ROW-001) requires change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json to equal the oracle projection row by row, and that map holds GCF-16 (:442) and GCF-17 (:451). A re-pinned oracle row must therefore be mirrored there, which changes its sha 5574666e. Re-pin it at :1131, :2611, profile:37, validate_flowmaster.py:40, validate_gcfpe_current.py:81/:660, validate_integrated_readiness.py:8/:151, validate_pre_guide_correction.py:9/:67, validate_strength_middleware.py:14 and change-flow SKILL.md. The *-correction.json baseline records in change-flow/references are historical and stay as they are. Without the mirror, FMV-GCF-ROW-001 fires; with it, all of the above fire until re-pinned.
```

- **Invariant**

```text
Kept: the runtime map is an exact projection of the oracle. The pin is re-pinned deliberately. Inferred from code, not simulated.
```

#### `fv-main:21` — WOULD_FAIL — step 34 (verification) (PART-09)

- **Check or surface:** step-34 verification 'grep -rc 52807e58 = 0 across both skills and the graph parts'
- **Location:** change-flow/references/gcfpe-20260913.1-091326.2-direct-handoff-contract.json, gcfpe-20260913.1-direct-handoff-contract.json, gcfpe-current-direct-handoff-contract.json; flowmaster-validate/scripts/validate_gcfpe_current.py:80, 376

- **Asserts**

```text
EXPECTED_R1_SHA256 = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e" ... "r1_oracle_sha256": EXPECTED_R1_SHA256, ... "r1_oracle_changed": False, }, "PROTECTED_IDENTITIES")
```

- **Required plan step**

```text
Scope the grep to live 091426.1 surfaces. The pin occurs in 13 files. The three historical contracts truthfully record 52807e58 and are hash-pinned themselves (e.g. alias bf5140c9 at validate_gcfpe_20260914.py:2564). validate_gcfpe_current.py:80 validates the historical 091326.2 alias, so replacing it, as step 34 says, makes that validator reject its own historical contract. Keep :80. Split :81 into a historical-recorded value (:376) and an installed-file value (:660).
```

- **Invariant**

```text
Historical records are an invariant to keep: never relabel an earlier record. As written, the verification can only be met by falsifying frozen contracts.
```

#### `fv-main:22` — UNCERTAIN — step CHILD (D23-F) (CHILD)

- **Check or surface:** R1 row targeted by the re-pin
- **Location:** flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json:669 (GCF-16); GCF-15 and GCF-14 rows

- **Asserts**

```text
GCF-16 "session": "Same operator invocation and same dedicated PR session; no additional session/object." ... "failure_stop_condition": "STOP_SECOND_APPROVAL_OBJECT_REQUESTED or STOP_PLAN_CHANGED_AFTER_PROCEED; ..."
```

- **Required plan step**

```text
Re-identify the rows before re-pinning. The child and D23-F say GCF-15's stop condition is STOP_SECOND_APPROVAL_OBJECT_REQUESTED. It is not: GCF-15's is 'STOP_PLAN_IDENTITY_MISMATCH or STOP_PO_PROCEED_NOT_INVOKED', and the quoted condition belongs to GCF-16. GCF-14 ('One new work-unit session bound to one planned PR work unit') and GCF-15 ('into the same dedicated PR session') also constrain a second session for an existing WORK_UNIT_ID. Name the exact rows, re-pin them in one oracle revision together with GCF-17, and mirror each into the runtime map.
```

- **Invariant**

```text
The single-approval-object-per-Plan rule is kept. A new Proceed for a new Plan is a new traversal. Only the rows the re-plan actually contradicts should move.
```

#### `fv-main:23` — WOULD_FAIL — step 15/34/38/42 (all flowmaster-validate edits) (multi)

- **Check or surface:** SKILL_SELF_IDENTITY
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2245-2280, 2614; flowmaster-validate/SKILL.md:9

- **Asserts**

```text
SKILL_TREE_SHA256: eb9634d60a65610c131e5d406d7ed6c69038864c555ad89e4c92b5bfde5dd6a8
```

- **Required plan step**

```text
Step 47: after the last flowmaster-validate edit (references, literals, fixtures, SKILL.md pins and wording), recompute skill_tree_digest(flowmaster-validate root), write the single SKILL_TREE_SHA256 line, and do it last.
```

- **Invariant**

```text
Kept: the package certifies its own identity. Measured: SKILL_SELF_IDENTITY:DECLARED_eb9634d60a65_MEASURED_7764936609cb.
```

#### `fv-main:24` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** SKILL_CONTRACT:glow-hde-pr-development ten-field continuity marker
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594 (marker's only occurrence is glow-hde-pr-development/SKILL.md:55)

- **Asserts**

```text
"The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage"
```

- **Required plan step**

```text
Step 35 names only validate_glow_hde_pr_development.py:32-34. Also update this flowmaster-validate literal to the exact new nine-field sentence written at :55, and keep it an exact substring.
```

- **Invariant**

```text
Reversed for the session field. The ordered list of the other fields is kept.
```

#### `fv-main:25` — UNCERTAIN — step 14, 19, 20, 40, 47 (PART-04/05/06/11)

- **Check or surface:** SKILL_CONTRACT:glow-hde-pr-development markers on lines the plan edits
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2590-2596, 1722 (single occurrences: SKILL.md:8, :59, :110, :162)

- **Asserts**

```text
"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5", "REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "This skill never authorizes an agent to merge, enable auto-merge", ... "exactly one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`"
```

- **Required plan step**

```text
Add to the step 14, 19, 20 and 40 edit instructions that these substrings stay intact: :162 (NEXT_PROMPT_HANDOFF block clause, steps 14/19), :59 (PR_REMOTE_ACTION_LEDGER, step 20), :110 (no-merge sentence, step 40). If step 47 bumps the skill revision, update :2592, contract pr_development_contract.primary_skill_revision (checked at :1722) and profile installed_skill_revisions together.
```

- **Invariant**

```text
Kept (no merge, one handoff block, the ledger). Each marker occurs exactly once, on a line the plan rewrites.
```

#### `fv-main:26` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** CHANGE_FLOW_CONTRACT marker 'PR-30 and PR-35 are two phases'
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2580-2586 (only occurrence: change-flow/SKILL.md:301)

- **Asserts**

```text
f"CHANGE_FLOW_SPECIALIZATION_REVISION: {expected_change_revision}", "PR-30 and PR-35 are two phases", ... if marker not in skill_text:
```

- **Required plan step**

```text
C-SESSION's canonical text is '`PR-30` and `PR-35` are two phases'. The backticks break this case-sensitive substring match. Either adapt change-flow:301 without backticks or update the marker. If change-flow's revision moves from 3.2.9, update profile installed_skill_revisions['change-flow'] (validation-profile.json:27).
```

- **Invariant**

```text
Kept: two phases of one work unit. Fails on wording only (inferred from exact-substring semantics).
```

#### `fv-main:27` — WOULD_FAIL — step all contract changes (multi)

- **Check or surface:** fixture mutation cascade (exact-equality mutations)
- **Location:** run_gcfpe_20260914_fixtures.py:346-407, 509-541

- **Asserts**

```text
cases.append({ "name": name, "passed": sorted(errors) == expected, "expected_error": expected_code, "errors": errors, })
```

- **Required plan step**

```text
Step 46 must run the scratch-updated validator and runner, with all literal updates in place, and record case counts. With any residual validate_contract error on the base contract, 46 unrelated mutation cases fail at once. Measured: 48 of 172 failed, including clean-versioned-contract and PR-SPLIT-POS-01. The installed 3.2.16 cannot pass step 46 at all.
```

- **Invariant**

```text
Kept. This is not a new defect. It means a rewritten literal is certified only by the suite that was rewritten with it (AF-001). Every reversed literal therefore needs its own must-fail injected regression, with the old state rejected by the new validator, and the §10 review must cover each literal diff.
```

#### `fv-main:28` — WOULD_PASS — step 38 (PART-11)

- **Check or surface:** fixture HANDOFF-POS-02 (conditional PR-40 handoff)
- **Location:** scenarios.json:59; run_gcfpe_20260914_fixtures.py:177-180

- **Asserts**

```text
facts.get("origin") == "PR-35" and facts.get("receiver") == "PR-40" and common and facts.get("manual_merge_condition") and facts.get("three_events_separate") -> "PR40_CONDITIONAL_HANDOFF_ACCEPTED"
```

- **Required plan step**

```text
Invert to the D23-E trigger (observed merge event, Nathan-performed merge, three_events_separate kept). Add a negative for a PR-40 handoff emitted before any merge event.
```

- **Invariant**

```text
Stays green while asserting the reversed manual-assertion trigger. The separation of the three events is kept.
```

#### `fv-main:29` — WOULD_FAIL — step fixture edits (29/38/42/CHILD) (multi)

- **Check or surface:** fixture identity and document shape
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:945, 1122-1125, 1166-1168; validation-profile.json:11-16; run_gcfpe_20260914_fixtures.py:258, 267

- **Asserts**

```text
EXPECTED_FIXTURE_SHA256 = "a1a730623e5385a6214a6f3e18b8cef56acd0d227028b2236e56d586d822fa14" ... "count": 33 ... if polarities.count("POSITIVE") != 18 or polarities.count("NEGATIVE") != 15:
```

- **Required plan step**

```text
Any scenarios.json edit requires updating :945, profile fixtures.sha256/count, and the 33 / 18-15 literals when ids or polarity change.
```

- **Invariant**

```text
Kept: fixture identity.
```

#### `fv-main:30` — UNCERTAIN — step CHILD (CHILD)

- **Check or surface:** missing coverage for the PR-40 re-plan route
- **Location:** run_gcfpe_20260914_fixtures.py:59-72 (pr_split has no re-plan branch); scenarios.json (no PR-40 REJECT case)

- **Asserts**

```text
if facts.get("requests_additional_proceed") or facts.get("requests_new_session"): return "VALIDATION_FAILURE"
```

- **Required plan step**

```text
Add a positive fixture: PR-40 REJECT for an in-scope defect goes to PR-20 in a new Nathan-seeded session, then a new Proceed on the new Plan, and is accepted. Add negatives: a second Proceed on the same Plan, a second Proceed between PR-30 and PR-35, and PR-40 REJECT routed back to PR-30. Add a contract assertion that the PR-40 REJECT branch targets PR-20 and not PR-30.
```

- **Invariant**

```text
The single approval per Plan is kept. The one-Proceed-per-work-unit rule is reversed for the re-plan case (D23-F). Nothing in the suite currently tests either half of the new rule.
```

#### `fv-main:31` — WOULD_PASS — step 41-44 (PART-12)

- **Check or surface:** PRESERVATION_CONTRACT versioned_sibling_successors
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1970-1977; contract preservation (contract:3095 per §A)

- **Asserts**

```text
"versioned_sibling_successors": True, "predecessor_mutation_during_staging": False,
```

- **Required plan step**

```text
§A lists contract:3095 as a PART-12 surface, but steps 41-44 have no step for it. Add one: set preservation.versioned_sibling_successors to reflect C-VERSION (only changed members get a successor page) in both contract copies, and update the :1972 literal citing D23-G.
```

- **Invariant**

```text
Deliberately reversed by D23-G. Left as it is, the validator enforces the retired rule. A truthful update fails until the literal changes.
```

#### `fv-main:32` — WOULD_PASS — step 15 (29/30/38/CHILD) (multi)

- **Check or surface:** contract-only fields that no check covers (would go stale silently)
- **Location:** direct-handoff contract receiver_compatibility, route_graph_semantics, pr_development_contract.pr30_ownership

- **Asserts**

```text
"PR-35": {"same_session_workspace_worktree_branch_open_pr_original_proceed": true} ... "PR-40": {"nathan_manual_merge_assertion_required": true} ... "same_session_phase_continuation": "PR-30 to PR-35 is one lawful same-session phase continuation..." ... "complete same-session PR-35 handoff"
```

- **Required plan step**

```text
Add these to step 15's authored contract edits: receiver_compatibility.PR-35 and .PR-40; .PR-30 (the child removes the PR-40 return context); a new receiver_compatibility.PR-20 entry that accepts a PR-40 REJECT finding and a new dedicated session for an existing WORK_UNIT_ID; route_graph_semantics.same_session_phase_continuation and .pr40_entry; pr_development_contract.pr30_ownership. Optionally add subset checks, because change-flow reads this contract at runtime.
```

- **Invariant**

```text
These restate the reversed rules. No check reads them, so they would keep contradicting D23-D/E/F without failing anything.
```

#### `fv-main:33` — UNCERTAIN — step 13, 18, 38, 39, CHILD (body runs) (PART-04/05/11, CHILD)

- **Check or surface:** body-level checks: PROMPT_HANDOFF_LITERAL, PROMPT_HANDOFF_RECEIVER, PROMPT_ROUTE_SEMANTICS, PROMPT_PRODUCER, QA closure markers
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2366-2367, 2396-2401, 2411-2417, 2441-2456, 2158-2178

- **Asserts**

```text
if prompt_id not in HANDOFF_LITERAL_EXEMPT and "NEXT_PROMPT_HANDOFF" not in text ... if not names_prompt(text, destination): PROMPT_HANDOFF_RECEIVER ... "PR-40": ("historical pre-merge", "independent", "glow-merged-change-attribution-lock")
```

- **Required plan step**

```text
Bodies were not read (rule). Add these readback assertions. Step 13 anchors on the sentence containing NEXT_PROMPT_HANDOFF: do not remove the literal before step 18's C-PLACE adds it, and make both in one page edit. After step 38, the PR-35 and RS-40 bodies must name PR-40; after the child, PR-40 must name PR-20. PR-40 keeps 'historical pre-merge' and 'independent' through step 39. The step 13 replacement must not drop PF10_BUILD_NOTES_ADDENDUM in the six producers, or `QA_REPORT_ID`, `QA_RCA_ID`, 'without a closure handoff', 'Do not infer a class' in QA-120 and CL-E-10/CL-C-10.
```

- **Invariant**

```text
All kept. These guard handoff presence, receiver binding and the QA class map, and step 13 rewrites the paragraph where several of them may live.
```

#### `fv-main:34` — WOULD_PASS — step 45 (PART-13)

- **Check or surface:** corpus-policy wording copied into code (not checks)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:2288-2291, 2657-2659; run_gcfpe_20260914_fixtures.py:726; flowmaster-validate/SKILL.md:164-165, 173

- **Asserts**

```text
# Bodies arrive on STDIN as {"PROMPT-ID": "<text>"} and there is deliberately no path option: a file would persist, and a persisted corpus is what the policy forbids.
```

- **Required plan step**

```text
Step 45 edits only SKILL.md:55-60 and :231-232. Apply C-D22 to the two code comments, the docstring and runner:726. Also add SKILL.md:164-165 and :173 to steps 35/40: they restate the ten-field list with 'dedicated PR-development session', 'its same-session PR-35 handoff', and 'Nathan's later invocation asserts the manual merge'.
```

- **Invariant**

```text
The no-path-option behaviour is kept. Only the stated reason changes (D22). The SKILL.md lines restate rules that are being reversed.
```

#### `fv-main:35` — UNCERTAIN — step 15/34 (optional) (multi)

- **Check or surface:** CONTRACT_IDENTITY contract_revision / CONTRACT_TOP_LEVEL_KEY_DRIFT
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1388-1400, 339-398

- **Asserts**

```text
"contract_revision": "4.0.6", ... EXPECTED_CONTRACT_TOP_LEVEL_KEYS = frozenset({ "abort_prompt", ... "transition_contract", })
```

- **Required plan step**

```text
Decide whether the changed contract keeps revision 4.0.6. A bump fails CONTRACT_IDENTITY until the literal is updated. Any new top-level key (e.g. a subscription or release-version object) fails the closed key set until a human adds it.
```

- **Invariant**

```text
Kept: contract identity and a closed key set against PF10-gate reintroduction.
```

#### fv-main — Tooling

- **item**

```text
Rebuild the graph to scratch (never into docs/graph): PYTHONDONTWRITEBYTECODE=1 python3 /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/scripts/graph_parts.py build /home/user/glow-hdengine-v2/docs/graph/parts "$SCRATCH/graph.md". Today it prints 'embedded JSON 569835 bytes sha256 90021eb7…', which equals EXPECTED_FROZEN_GRAPH_SHA256 and the bundled file byte-for-byte.
```

- **item**

````text
Derive the bundled graph file: take the lines between the first '```json' fence and the last '```' in graph.md, join them with newlines, and append one trailing newline. That byte string is references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json (verified identical to the current flowmaster-validate and change-flow copies).
````

- **item**

```text
There is no generator for the direct-handoff contract; grep of both skills and the repo finds only validators. Its contract-only keys (transition_contract, pr_development_contract, member_registry, route_graph, route_graph_semantics, receiver_compatibility, protected_identities, graph_proofs, preservation, source_snapshot) must be authored. route_edges, state_routes, boundary_transitions, boundary_nodes and post_merge_three_event_contract are copied from the built graph. Serialization in the simulation: json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) plus a newline. Confirm it reproduces 2b78f877 on an unchanged input before relying on it.
```

- **item**

```text
Validate from a scratch copy, never in the installed tree: cp -a <synced>/flowmaster-validate "$SCRATCH/fv" && cd "$SCRATCH/fv/scripts" && PYTHONDONTWRITEBYTECODE=1 python3 validate_gcfpe_20260914.py <synced>/change-flow --contract "$SCRATCH/fv/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json" [--bodies-stdin]. Baseline: ok=true, errors=[].
```

- **item**

```text
Fixture suite: PYTHONDONTWRITEBYTECODE=1 python3 run_gcfpe_20260914_fixtures.py <synced>/change-flow --contract <same> [--bodies-stdin]. Baseline: fixture_suite_ok=true, 172 cases, section_13 33/33.
```

- **item**

```text
Routing-surface re-pin value (after human diff review): PYTHONDONTWRITEBYTECODE=1 python3 -c "import sys,json; sys.path.insert(0,'$SCRATCH/fv/scripts'); import validate_gcfpe_20260914 as V; print(V.routing_surface(json.load(open('<new contract>'))))"
```

- **item**

```text
Self-identity re-stamp, last step: python3 -c "import sys; sys.path.insert(0,'$SCRATCH/fv/scripts'); import validate_gcfpe_20260914 as V; from pathlib import Path; print(V.skill_tree_digest(Path('$SCRATCH/fv')))" then write the single SKILL_TREE_SHA256 line in SKILL.md:9.
```

- **item**

```text
HAZARD, measured: validate_gcfpe_20260914.py imports validate_gcfpe_artifact_timing at line 17 before it sets sys.dont_write_bytecode at line 20, and run_gcfpe_20260914_fixtures.py does the same at lines 11 and 14. A plain run writes scripts/__pycache__/validate_gcfpe_artifact_timing.cpython-311.pyc into the tree, and that same run already reports SKILL_SELF_IDENTITY:DECLARED_eb9634d60a65_MEASURED_07966b1a6f99. Plan step 1's command has no PYTHONDONTWRITEBYTECODE=1. Run with the variable set or from a scratch copy, or an installed tree becomes permanently self-identity-invalid until the .pyc is removed.
```

- **item**

```text
Simulation used for every 'measured' claim: /tmp/claude-0/pf_scratch/sim.py (applies steps 12, 23, 29, 30, 31, 34, 38, 15 and the child to scratch copies, builds, and runs validate_contract and validate_graph_contract per step group). Outputs are in /tmp/claude-0/pf_scratch/sim/report.json.
```

#### fv-main — Live-window risks

- **item**

```text
The installed flowmaster-validate stays green at contract and graph level for the whole window. It never reads docs/graph/parts; it validates its own frozen bundle, whose parts all agree with each other. Merged graph-part changes and Notion body edits are invisible to it except through --bodies-stdin, so a maintenance run without bodies reports ok:true, with ALL_BODY_LEVEL_CHECKS not evaluated, while the live ecosystem has changed.
```

- **item**

```text
Step 42 lands before the new validator is installed: every body-level run raises PROMPT_BODY_IDENTITY for each edited body, up to all 55 (measured on the header shape). That includes the prompt-validation procedure and any PART-01-style scan. The failure reads like corrupted bodies and invites a 'repair' that re-adds the release headers, the check-driven regression AF-001 warns about. The reverse order also fails: a new validator installed before step 42 rejects all 55 current bodies. No ordering passes both ways, so the header edits and the install need a single cut-over, or a transitional acceptance recorded under D23-G.
```

- **item**

```text
Step 13 before step 18 on the same body: if the C-HANDOFF replacement removes the sentence holding the literal NEXT_PROMPT_HANDOFF, PROMPT_HANDOFF_LITERAL fires until C-PLACE restores it, and the registry audit literal fails too.
```

- **item**

```text
PART-09: new PR-30 and PR-35 bodies say PR-35 runs in its own session, while installed glow-hde-pr-development 1.2.5 (description ':3', ':53', ':55', ':112'), change-flow ':301'/':307'/':365' and the bundled contract (session_class SAME_DEDICATED_PR_DEVELOPMENT_SESSION_AS_PR-30, added_boundaries.session 0, receiver_compatibility.PR-35 same_session…:true) still say one session. A PR-30 session following the skill continues into PR-35 in-session. A fresh PR-35 session following the body may fail the skill's ten-field continuity check, which R1 GCF-17 frames as STOP_SESSION_MISMATCH. That risks stalling any in-flight work unit.
```

- **item**

```text
PART-10/11: PR-35 and RS-40 bodies with C-DISPATCH ('stay subscribed and return control') run under a skill that has no subscription instruction and forbids 'keep polling', and under a contract that forbids any PR-35 to PR-40 edge and requires Nathan's assertion. If the body stops emitting the conditional PR-40 block at MERGE_PENDING and no subscription exists, nothing starts PR-40 after Nathan merges. The body must keep the no-subscription fallback before the skills are installed.
```

- **item**

```text
CHILD: a PR-40 body that routes REJECT to PR-20 in a new session with a new Proceed runs while the installed contract still routes reject_existing_pr_owner to PR-30 under the 'original Proceed', and the installed skills and R1 still say 'never a second Proceed' and GCF-16's STOP_SECOND_APPROVAL_OBJECT_REQUESTED. A new PR-20 session following glow-hde-pr-development's recover-existing-work-before-create rule would find the existing branch and PR and recover it instead of re-planning, and a change-flow run could stop at Nathan's new Proceed. Body-level validation also fails in both orders: an old contract with a new PR-40 body raises PROMPT_HANDOFF_RECEIVER:PR-40:PR-30 if the body no longer names PR-30, and a new contract with an old body raises PROMPT_HANDOFF_RECEIVER:PR-40:PR-20. The PR-40 body should name both identifiers during the cut-over.
```

- **item**

```text
change-flow reads its bundled contract for routing and handoff shape (transition_contract still demands status, completed work, decisions and constraints). Until the new package is installed, a change-flow-orchestrated session enforces the pre-D23 handoff and routing on bodies that say the opposite, including flagging a PR-35 to PR-40 dispatch as a prohibited direct edge.
```

#### fv-main — Notes

- **item**

```text
Answer to 'what does the validator compare?': validate_gcfpe_20260914.py never reads docs/graph/parts. It compares (1) profile pins against the bundled graph and contract bytes (:1134-1168); (2) profile and bundle against the script's own literals (:941-945, :1099-1133); (3) the --contract argument against the bundled contract, byte-equal in candidate mode or by release_semantic_view since the contract is SELECTED_PRODUCTION (:2485-2501; CONTRACT_HASH is skipped in production mode); (4) change-flow's installed contract against flowmaster-validate's bundled contract byte-for-byte (:2502-2516); (5) the bundled graph against the contract field by field (:1172-1383); (6) optionally a --candidate-root graph file against the bundled graph (:2532-2550). A graph-part change therefore requires regenerating: the bundled graph in flowmaster-validate/references and change-flow/references (embedded JSON block plus newline from the parts build); the direct-handoff contract in both skills, lockstep keys plus source_snapshot.frozen_candidate_graph.sha256 at contract:11543; validation-profile.json; the script literals; and SKILL_TREE_SHA256. Order: graph, then contract (the graph does not reference the contract hash, so there is no cycle), then profile, then literals, then fixtures pin, then self-identity. Cross-surface, not mine: change-flow/scripts/validate_gcfpe_20260914.py pins EXPECTED_GRAPH_SHA 90021eb7 (:21, :777, :781) and a topology readback 705f5acf (:25, :779).
```

- **item**

```text
Confirmed by measurement: the three known defects (PROMPT_BODY_IDENTITY after step 42; PR35_ADDED_BOUNDARY and PR_PHASE_CONTINUITY after step 29; POST_MERGE_CONTRACT and POST_MERGE_THREE_EVENTS after step 38). Beyond those, step 38 also fires DIRECT_PR35_PR40_EDGE, GRAPH_DIRECT_PR40_EDGE, PR40_MANUAL_MERGE_BOUNDARY, ROUTE_GRAPH_SHORTHAND, ROUTING_SURFACE_CHANGED and, if the boundary edge is removed, an edge-count change from 227 to 226. Steps 23, 31 and the child each fire ROUTING_SURFACE_CHANGED on their own. Step 15, done truthfully, fires HANDOFF_CONTRACT and HANDOFF_PROHIBITED_REFERENCES. The full end state fires 18 validate_package codes and fails 48 of 172 fixture cases.
```

- **item**

```text
Step 12 on its own raises no graph-to-contract code (measured). GRAPH_HANDOFF_CONTRACT_MISMATCH compares only 5 scalar fields, so the new handoff_contract.required and prohibited lists are unverified against the contract. That is why step 15's 'regenerate from the graph parts' can silently do nothing.
```

- **item**

```text
Plan-internal inconsistencies this validator exposes: (a) step 38 removes the NATHAN_MANUAL_MERGE_ASSERTION boundary while step 39 keeps Nathan's assertion as a PR-40 input where no subscription existed; (b) step 38 routes the MERGE_PENDING branch to PR-40 while MERGE_PENDING is defined as pre-merge evidence (exact marker 'historical pre-merge' at :2444; route_graph_semantics.pr35_merge_pending). If a post-merge state is added instead, EXPECTED_PR35_RESULTS (:853-856), PR35_STATE_ROUTES (:1921), GRAPH_STATE_VOCABULARY_MISMATCH (:1292) and fixture reject-missing-pr35-result all move; (c) C-VERSION says a changed member gets a successor page at a new version, while §P edits 53+ bodies in place at 091426.1. If C-VERSION were applied to this run's own edits, MEMBER_BINDING, GRAPH_NODE_CONTRACT (title, candidate_version) and the identity-header title check would fail for every changed member.
```

- **item**

```text
Kept invariants that unchanged checks still guard: DIRECT_PR30_PR40_EDGE (:1835-1836); pr35_same_r1_row_as_pr30 (:1367, :1953, kept true by step 29); agent_merge_authorized False (:1739, :1770); rescope_contract.new_proceed_required False (:1710), which concerns rescope and must not be reused to encode D23-F's new Proceed; PR_RETURN_PHASE_CONTRACT original_proceed_preserved (:1697); transition_contract.actual_pasteable_complete_prompt True, with fixture reject-incomplete-handoff (runner:405).
```

- **item**

```text
No validator check covers C-ART, C-DEC, C-PLACE, C-LAT, C-SUB or the PART-02 Notion wording, so steps 8-11, 18, 20-22, 3-5 and 37 cannot break this validator. Their only guards are the registry assertions in steps 7, 11, 17, 21 and 25. The artifact-timing body regexes (validate_gcfpe_artifact_timing.py:26-79) were checked against every canonical text: none contains both a 'require/mandatory/prerequisite' word and a QA-artifact term, so none trips PR_FUTURE_QA_INPUT. The child's PR-20 entry must avoid 'when a denial requires correction' (:76).
```

- **item**

```text
Step 1 and step 46 ordering: PART-01 and PART-12 are unordered in §P. If step 42 runs first, step 1's scan is flooded with PROMPT_BODY_IDENTITY, though its PROMPT_BODY_GOVERNANCE_STATE read still works. Step 46 cannot pass with the installed 3.2.16. It must use the scratch-updated validator and must supply bodies, or it reports ALL_BODY_LEVEL_CHECKS as not evaluated, which SKILL.md:234 says is not a pass.
```

- **item**

```text
EXPECTED_MERGE_PENDING_REQUIREMENTS (:881-885) includes 'no unresolved material boundary'. It breaks only if PART-07's terminology is also applied to the contract's merge_pending_requirements. Step 22 and step 23 as written do not do that.
```

- **item**

```text
validate_flowmaster.py FMV-ORACLE-003 pins authority.r1_contract_matrix_sha256 faa7fb7d as immutable, and no script recomputes source_row_sha256. Step 34's 'recompute the row's source_row_sha256' has no defined algorithm and no source row in the pinned matrix to match. Only the whole-file oracle pin can catch the injected regression the step names.
```

- **item**

```text
Nothing was written outside /tmp/claude-0. No git, Notion or prompt-body fetch. The installed skill tree was never executed in place; the check found no __pycache__ there before or after.
```

### fv-rest — rest of flowmaster-validate, and change-flow (30 findings)

#### `fv-rest:0` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** FMV-ORACLE-007 (EXPECTED_ORACLE_SHA256)
- **Location:** flowmaster-validate/scripts/validate_flowmaster.py:37-39, enforced at :478-486

- **Asserts**

```text
EXPECTED_ORACLE_SHA256 = ("52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e") ... if oracle_sha256 != EXPECTED_ORACLE_SHA256: findings.append(finding("FMV-ORACLE-007", ...
```

- **Required plan step**

```text
Step 34's site list must add validate_flowmaster.py:38. exp1 re-pinned only the sites the plan names, and the default suite returned FMV-ORACLE-007, FLOWMASTER_SUITE_FAIL.
```

- **Invariant**

```text
Guards a real invariant that the change keeps: the oracle bytes are pinned. Only the value changes. This is a new pin, not a weakened check.
```

#### `fv-rest:1` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** FMV-GCF-ROW-001 (runtime-map row equality); FMV-GCF-MAP-006 (runtime-map SHA)
- **Location:** flowmaster-validate/scripts/validate_flowmaster.py:732-751 and :40-42/:705-712; change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json (GCF-17 row)

- **Asserts**

```text
expected_projection = {key: oracle[key] for key in ("profile_id", "authority", "coverage", "runtime_rows")} ... "FMV-GCF-ROW-001" ... row={row_id}; declared mapping differs from pinned R1 oracle
```

- **Required plan step**

```text
Add to step 34: 'Apply the identical GCF-17 (and, for the child, GCF-15/16/14/17.LINEAGE) row edit to change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json, then re-pin its SHA-256 (today 5574666e…) at validate_flowmaster.py:41, validate_gcfpe_current.py:81, validate_gcfpe_20260914.py:1131 and :2611, validation-profile.json:37, the r1_runtime_map_sha256 field of the current-alias contract at :806, and the prose at change-flow/SKILL.md:557.' exp1 produced FMV-GCF-ROW-001 row=GCF-17.
```

- **Invariant**

```text
Kept: the runtime map must equal the oracle projection. The check stays exact and only its pinned value moves. change-flow/SKILL.md:557 calls this map 'immutable historical baseline evidence', and editing it reverses that. See the entry on historical bytes.
```

#### `fv-rest:2` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** PROTECTED_IDENTITIES on the selected alias, plus the alias fixture suite (BASELINE_CONTRACT_INVALID)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_current.py:80-83, :372-380; change-flow/references/gcfpe-current-direct-handoff-contract.json:805-808; run_gcfpe_current_fixtures.py:127-135

- **Asserts**

```text
"r1_oracle_sha256": EXPECTED_R1_SHA256, "r1_runtime_map_sha256": EXPECTED_RUNTIME_MAP_SHA256, ... "flowmaster_primary_core_changed": False, "r1_oracle_changed": False, }, "PROTECTED_IDENTITIES")
```

- **Required plan step**

```text
The plan re-pins validate_gcfpe_current.py:80 but not the alias contract it reads. exp1 returned FMV-GCF-CURRENT-001 PROTECTED_IDENTITIES and FMV-GCF-CURRENT-FIXTURE-001. The plan must either re-pin the alias contract's r1_oracle_sha256 and r1_runtime_map_sha256 at :805-806, or retire or re-point the alias first (see the change-flow/SKILL.md:559 entry).
```

- **Invariant**

```text
The r1_oracle_changed:false half guards an invariant the change deliberately reverses. Replace it with an explicit revision record (for example r1_oracle_changed:true plus a D23 pointer). Keeping False next to a new SHA leaves a stale expectation in place and hides the reversal (AF-001).
```

#### `fv-rest:3` — WOULD_PASS — step 34 (PART-09)

- **Check or surface:** Semantic claims that R1 is unchanged: PROTECTED_IDENTITIES, GRAPH_PROOFS, GRAPH_PROTECTED_IDENTITIES
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1953-1956, :1960-1967, :1370-1377; both copies of the bundled 091426.1 contract at :3108-3116

- **Asserts**

```text
"pr35_same_r1_row_as_pr30": True, ... "protected_r1_46_rows_unchanged": True, ... "r1_rows": 46, "flowmaster_primary_core_changed": False, "r1_oracle_changed": False, "pr35_adds_r1_row": False,
```

- **Required plan step**

```text
Proven in exp4: after a blanket SHA replace and re-stamping every byte pin, both the candidate-overlay suite and the change-flow validator return PASS while the contract still asserts r1_oracle_changed:false and protected_r1_46_rows_unchanged:true. The plan needs an explicit step that sets these claims to the truth (oracle changed by D23; row count 46 unchanged; row text changed) and rewrites the expectations to match, with an injected regression that fails.
```

- **Invariant**

```text
Deliberately reversed ('R1 oracle unchanged'). The pinned hash moves while the check's meaning stays the same. The new expectation must still guard a count of 46 rows (26 core, 20 material) and 'no added R1 row'.
```

#### `fv-rest:4` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** Profile protected identities (profile vs constant)
- **Location:** flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:33-38; validate_gcfpe_20260914.py:1126-1133

- **Asserts**

```text
"r1_oracle_sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e", "r1_runtime_map_sha256": "5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e", "r1_rows": 46, }, "PROFILE_PROTECTED_IDENTITIES")
```

- **Required plan step**

```text
Add validation-profile.json:35 and :37 to step 34's site list. The plan names the 'x3' constants in the validator but not the profile JSON they are compared against.
```

- **Invariant**

```text
Kept. Re-pin only.
```

#### `fv-rest:5` — UNCERTAIN — step 34 (PART-09)

- **Check or surface:** Unmentioned documentation pin
- **Location:** flowmaster-validate/SKILL.md:246 (and :248-249)

- **Asserts**

```text
- projection SHA-256 52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e;
```

- **Required plan step**

```text
Add SKILL.md:246 to step 34. No script parses it, but the step-34 grep verification counts it, and it is the skill's own statement of authority.
```

- **Invariant**

```text
Documentation of a kept invariant.
```

#### `fv-rest:6` — UNCERTAIN — step 34 (PART-09)

- **Check or surface:** Oracle authority, and a source_row_sha256 value that cannot be recomputed
- **Location:** flowmaster-validate/scripts/validate_flowmaster.py:33-36, :496-503 (FMV-ORACLE-003), :534-556 (FMV-ORACLE-006 exact 12-field row set); flowmaster-validate/SKILL.md:255-257, :285; oracle authority block (r1_contract_matrix_sha256 faa7fb7d…, r1_frozen_snapshot 5a6d89ed…, r1_verdict R1_CANONICAL_TRUTH_LOCK_PASS)

- **Asserts**

```text
SKILL.md:257 "The bundled projection is maintenance evidence, not a new authority. Any future oracle update requires a separately authorized repair that proves a complete projection against the immutable or successor canonical source."
```

- **Required plan step**

```text
Step 34 says 'recompute the row's source_row_sha256'. I tried 8 common serializations of GCF-17's own fields and none reproduces a2b761a9…, so the value appears to digest the external R1 Contract Matrix row (libfile_9caa…) and no in-skill formula exists. The plan must choose one of two routes: (a) author a successor canonical source row, record its digest and a successor authority block, and move FMV-ORACLE-003 plus R1_CONTRACT_MATRIX_SHA256 at change-flow/SKILL.md:19 and flowmaster-validate/SKILL.md:147/:248; or (b) keep the immutable authority and digest, and record D23 as a projection amendment. Route (b) needs a validator change, because FMV-ORACLE-006 forbids any 13th row field.
```

- **Invariant**

```text
Guards provenance, which the change keeps. Recomputing the digest over the edited projection turns a source digest into a digest of itself, which weakens the check without saying so.
```

#### `fv-rest:7` — WOULD_PASS — step 34 (PART-09)

- **Check or surface:** Oracle profile identity reused for different bytes
- **Location:** validate_flowmaster.py:33 (EXPECTED_ORACLE_PROFILE), :148 (CONTRACT_REQUIRED change-flow), :672; change-flow/SKILL.md:17; flowmaster-validate/SKILL.md:145; oracle required_global_tokens

- **Asserts**

```text
EXPECTED_ORACLE_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1"
```

- **Required plan step**

```text
Decide whether the re-pinned oracle keeps profile_id GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1. flowmaster-validate/SKILL.md:39-53 and :126-135 (F1) forbid corrected bytes from reusing an identity. Renaming the profile moves 5+ pins listed at this entry's location. Keeping it reuses the identity, and the plan should record that it does so knowingly.
```

- **Invariant**

```text
Identity-uniqueness rule that the change keeps. Not addressed by the plan.
```

#### `fv-rest:8` — WOULD_FAIL — step 34 (PART-09)

- **Check or surface:** Historical immutable layers: HISTORICAL_BYTES_CHANGED, HISTORICAL_BYTES, PRESERVED_LAYER
- **Location:** flowmaster-validate/scripts/validate_strength_middleware.py:14; validate_epic_alpha.py:43 (via change-flow/references/epic-alpha-repair-correction.json:9); validate_epic_reengineering.py:48 (via epic-reengineering-correction.json:90); run_strength_middleware_fixtures.py; run_epic_alpha_fixtures.py; change-flow/SKILL.md:557-561

- **Asserts**

```text
'glow-hde-canonical-change-flow-r1-runtime-map.json':'5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e', ... errors.append('HISTORICAL_BYTES:'+x['file'])
```

- **Required plan step**

```text
exp3 kept the historical files unchanged and edited the runtime map. Five validators that pass today then fail: validate_strength_middleware (HISTORICAL_BYTES_CHANGED), validate_epic_alpha (HISTORICAL_BYTES), validate_epic_reengineering (PRESERVED_LAYER), run_strength_middleware_fixtures and run_epic_alpha_fixtures. Step 34's verification ('grep -rc 52807e58 = 0 across both skills') instead forces edits to gcfpe-20260913.1-091326.2-direct-handoff-contract.json:808-811 and gcfpe-20260913.1-direct-handoff-contract.json:773-776, which change-flow/SKILL.md:561 declares 'immutable historical provenance'. Replace that verification with 'zero hits in active pins; historical records unchanged', and choose a route explicitly: preferably a new successor runtime-map file that leaves the historical map bytes intact, rather than rewriting historical correction layers.
```

- **Invariant**

```text
Guards immutability of historical provenance, which the change does not intend to reverse. Rewriting their baseline pins would falsify history, and the default suite runs none of these validators, so nothing would catch it.
```

#### `fv-rest:9` — WOULD_FAIL — step 34, 45, 1-47 (any flowmaster-validate byte change) (PART-09, PART-13, all)

- **Check or surface:** SKILL_SELF_IDENTITY
- **Location:** flowmaster-validate/SKILL.md:9; validate_gcfpe_20260914.py:2245-2280; called from validate_flowmaster.py:1439-1441 and validate_gcfpe_current.py:663-664

- **Asserts**

```text
SKILL_TREE_SHA256: eb9634d60a65610c131e5d406d7ed6c69038864c555ad89e4c92b5bfde5dd6a8 ... return [f"SKILL_SELF_IDENTITY:DECLARED_{declarations[0][:12]}_MEASURED_{measured[:12]}"]
```

- **Required plan step**

```text
Add to step 47, before packaging and freeze: recompute skill_tree_digest(flowmaster-validate) after all edits and re-declare the single SKILL_TREE_SHA256 line. exp1 failed SKILL_SELF_IDENTITY:DECLARED_eb9634d60a65_MEASURED_8fef08a12f9e.
```

- **Invariant**

```text
Kept. The installed-tree identity guard stays. Only the declared value moves.
```

#### `fv-rest:10` — WOULD_FAIL — step 12, 23, 29, 30, 31, 34, 38; CHILD (PART-04, PART-07, PART-09, PART-11; CHILD)

- **Check or surface:** Bundled graph byte pins and edge count (the bundled graph copies are in no plan step)
- **Location:** change-flow/scripts/validate_gcfpe_20260914.py:21, :777, :806, :810-817; flowmaster-validate/scripts/validate_gcfpe_20260914.py:941-942, :1112-1121, :1141-1160, :2537-2548; validation-profile.json frozen_graph; contract source_snapshot.frozen_candidate_graph.sha256

- **Asserts**

```text
EXPECTED_GRAPH_SHA = "90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223" ... require(sha256(graph_bytes) == EXPECTED_GRAPH_SHA, "bundled graph bytes") ... len(graph["edges"]) == 227
```

- **Required plan step**

```text
Add a step: 'Build docs/graph/parts to scratch, take the embedded JSON block plus its final LF, which today is byte-identical to the bundled 569835-byte graph (verified), and write it to references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json in both skills. Then re-pin EXPECTED_GRAPH_SHA (change-flow validator :21), EXPECTED_FROZEN_GRAPH_SHA256/BYTES (:941-942), profile frozen_graph sha256/byte_count/edge_count, contract source_snapshot.frozen_candidate_graph.sha256, graph_proofs.route_edge_count, and the literal 227 at change-flow validator :806 if PART-11 changes the edge count.' exp2 reported GRAPH_HASH, PROFILE_BUNDLED_GRAPH_HASH and 'FAIL: bundled graph bytes'.
```

- **Invariant**

```text
Kept: the bundled graph must equal the build. The pins are re-stamped. The 227 edge count must be measured from the new graph, not hand-edited.
```

#### `fv-rest:11` — WOULD_FAIL — step 15 (PART-04 (also carries PART-09, PART-11 and CHILD))

- **Check or surface:** Contract byte pins and contract_revision
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:943-944, :1097-1111, :1134-1140; validation-profile.json candidate_contract; change-flow/scripts/validate_gcfpe_20260914.py:751

- **Asserts**

```text
EXPECTED_CANDIDATE_CONTRACT_SHA256 = "2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b" EXPECTED_CANDIDATE_CONTRACT_BYTES = 606657 ... require(contract["contract_revision"] == "4.0.6", ...)
```

- **Required plan step**

```text
Extend step 15 to re-pin the contract's sha256 and byte_count in the profile and in EXPECTED_CANDIDATE_CONTRACT_SHA256/BYTES, and to decide on contract_revision. Keeping 4.0.6 reuses an identity for different bytes; bumping it moves change-flow validator :751. exp2 reported PROFILE_BUNDLED_CONTRACT_HASH.
```

- **Invariant**

```text
Kept. Re-pin only.
```

#### `fv-rest:12` — WOULD_FAIL — step 15, 29, 30, 31, 38, CHILD (PART-04, PART-09, PART-11, CHILD)

- **Check or surface:** 'Regenerate from the graph parts' has no generator; graph/contract parity checks
- **Location:** glow-graph-contract/scripts/graph_parts.py (builds only the graph); flowmaster-validate/scripts/validate_gcfpe_20260914.py:1215-1235 (GRAPH_NODE_CONTRACT, session_class/receiving_role paired), :1240-1257 (GRAPH_EDGE_/STATE_ROUTE_/POST_MERGE_CONTRACT_MISMATCH), :1296-1313 (GRAPH_PR_CONTINUITY_MISMATCH); change-flow validator :810-817

- **Asserts**

```text
paired_fields = {... "receiving_role": "receiving_role", "session_class": "session_class", ...} ... if graph.get("edges") != contract.get("route_edges"): errors.append("GRAPH_EDGE_CONTRACT_MISMATCH")
```

- **Required plan step**

```text
No script derives the schema-4.0 direct-handoff contract from the graph parts. transition_contract uses boolean flags that differ from the graph's handoff_contract lists. member_registry, route_edges, state_routes, pr_development_contract (added_boundaries, shared_exactly_one), post_merge_three_event_contract, receiver_compatibility (PR-35 'same_session_…': true; PR-40 'nathan_manual_merge_assertion_required': true) and route_graph exist only in the contract. The plan must name a contract generator to be written and reviewed, or authorize a scripted JSON transform of those exact keys (as it does for the graph parts). Otherwise step 15 is not executable without hand-editing.
```

- **Invariant**

```text
The parity checks guard a kept invariant (contract equals graph). The receiver_compatibility flags are not validated at all, so they would go stale silently.
```

#### `fv-rest:13` — WOULD_FAIL — step 12, 15 (PART-04)

- **Check or surface:** HANDOFF_CONTRACT and HANDOFF_PROHIBITED_REFERENCES on the 091426.1 transition_contract
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1481-1499; contract transition_contract (contract:17594-17618)

- **Asserts**

```text
"every_required_repository_and_pr_reference": True, "status_completed_work_decisions_constraints_unresolved_authority": True, "next_action_and_expected_output": True, }, "HANDOFF_CONTRACT") ... if prohibited_refs != {"Library ID", "unlinked filename", "above", "conversation reconstruction", ...
```

- **Required plan step**

```text
Add a step that replaces those expectations with C-HANDOFF's (restated artifact content prohibited; branch and commit prohibited; PR reference only when continuing a PR), updates the exact prohibited-reference set, and adds a mutation fixture in run_gcfpe_20260914_fixtures.py (for example reject-handoff-restates-decisions or reject-handoff-branch-commit) that must fail.
```

- **Invariant**

```text
Deliberately reversed. The 'status/decisions/constraints' requirement is what C-HANDOFF forbids. The replacement must still guard completeness and paste-readiness. Deleting the flag instead would silently weaken the check.
```

#### `fv-rest:14` — WOULD_FAIL — step 23, 31, 38, CHILD (PART-07, PART-09, PART-11, CHILD)

- **Check or surface:** ROUTING_SURFACE_CHANGED pin
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:207-208, :1673-1675; change-flow/scripts/validate_gcfpe_20260914.py:76-77, :919-921

- **Asserts**

```text
EXPECTED_ROUTING_SURFACE = "7380cd14430777675f1e8b2cdfa4a0da" EXPECTED_ROUTING_SURFACE_ROWS = 282 ... It detects CHANGE, not intent ... Re-pinning is a deliberate act a human performs after reading the diff
```

- **Required plan step**

```text
Add a gate step: produce the before/after routing-surface diff for PART-07 edge conditions, the PART-09 PR-30 to PR-35 edge, the PART-11 PR-35 to PR-40 edge and the CHILD PR-40 to PR-20 re-route. Nathan reads it, and only then are both copies re-pinned (digest and row count). By the pin's own comment, a session must not re-pin it on its own judgement.
```

- **Invariant**

```text
Kept: routing change detection. The pin must be moved by a human after reviewing the diff (AF-001).
```

#### `fv-rest:15` — WOULD_FAIL — step 29, 30 (PART-09)

- **Check or surface:** PR35_ADDED_BOUNDARY: the plan leaves a contradictory cross_session_route=0
- **Location:** docs/graph/parts/global.json:473-485 (adds.cross_session_route 0); PR-35.json node cross_session_route false; validate_gcfpe_20260914.py:1741-1742; run_gcfpe_20260914_fixtures.py:359

- **Asserts**

```text
if not isinstance(development, dict) or any(value != 0 for value in development.get("added_boundaries", {}).values()): errors.append("PR35_ADDED_BOUNDARY")
```

- **Required plan step**

```text
Extends the already-found defect. Steps 29-30 set session=1 and adds_session=true but leave cross_session_route at 0/false, although PR-30 to PR-35 becomes a cross-session route (change-flow/SKILL.md:307 and flowmaster-validate/SKILL.md:164 list 'cross-session route' as prohibited). Set cross_session_route to 1/true as well. Rewrite the check to an exact expected dict ({session:1, cross_session_route:1, every other key 0}) so the fixture reject-new-proceed-boundary still yields exactly ['PR35_ADDED_BOUNDARY'].
```

- **Invariant**

```text
Partially reversed (session and cross-session). The proceed, approval, role, work_unit and merge_authority zeros are kept and must stay pinned. Do not replace the check with 'session may be nonzero'.
```

#### `fv-rest:16` — WOULD_FAIL — step 29-35 (PART-09)

- **Check or surface:** Same-session fixtures and behavior projection
- **Location:** flowmaster-validate/fixtures/gcfpe-20260914.1-091426.1/scenarios.json (PR-SPLIT-POS-01, PR-SPLIT-NEG-01 variant new-session-only, HANDOFF-POS-01, HANDOFF-NEG-01, OBS-POS-01); run_gcfpe_20260914_fixtures.py:60, :66-70, :175, :206, :324-325, :331-333; profile fixtures.sha256 and validate_gcfpe_20260914.py:945 EXPECTED_FIXTURE_SHA256; count 33 at profile and flowmaster-validate/SKILL.md:176

- **Asserts**

```text
if facts.get("requests_additional_proceed") or facts.get("requests_new_session"): return "VALIDATION_FAILURE" ... return "PR30_TO_PR35_SAME_SESSION" ... PR-SPLIT-POS-01 expected PR30_TO_PR35_SAME_SESSION {"same_session_pr35": true}
```

- **Required plan step**

```text
Add a fixture step: invert new-session-only to a positive case (a dedicated PR-35 session is required), rename PR30_TO_PR35_SAME_SESSION, set HANDOFF-POS-01 same_session:false with a session_disposition NEW_DEDICATED fact, keep extra-proceed-only negative, add a negative 'PR-35 continued in the PR-30 session', then re-pin the fixture SHA (profile and EXPECTED_FIXTURE_SHA256) and the count if it changes.
```

- **Invariant**

```text
Deliberately reversed (same session). The 'no additional Proceed' half is kept and must remain negative.
```

#### `fv-rest:17` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** change-flow skill-clause literal 'PR-30 and PR-35 are two phases'
- **Location:** change-flow/scripts/validate_gcfpe_20260914.py:1020-1021; flowmaster-validate/scripts/validate_gcfpe_20260914.py:2580-2587 (CHANGE_FLOW_CONTRACT)

- **Asserts**

```text
for text in ("PR-30 and PR-35 are two phases", ... require(text in skill, f"missing skill clause: {text}")
```

- **Required plan step**

```text
C-SESSION as written ('`PR-30` and `PR-35` are two phases …', with backticks) does not contain the literal. exp5 applied C-SESSION verbatim to change-flow/SKILL.md:301 and got 'FAIL: missing skill clause: PR-30 and PR-35 are two phases' and CHANGE_FLOW_CONTRACT:PR-30 and PR-35 are two phases. Step 35 must update both validators' literal to the C-SESSION text, or place the text without backticks.
```

- **Invariant**

```text
Kept (two phases of one unit). The literal must track the canonical wording.
```

#### `fv-rest:18` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** Ten-field continuity list and 'one dedicated PR-development session' literals, pinned across skills
- **Location:** change-flow/scripts/validate_gcfpe_20260914.py:1022-1023 (change-flow SKILL.md:301, :303); flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594 (glow-hde-pr-development:55); flowmaster-validate/scripts/validate_gcfpe_current.py:650-655 (glow-hde-pr-development:10, :53)

- **Asserts**

```text
"The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; ...", "one dedicated PR-development session",
```

- **Required plan step**

```text
Step 35 names only glow-hde-pr-development's own validator literals. Add the three cross-skill pin sites at this entry's location, updated to the nine-field C-SESSION list. Also add glow-hde-pr-development:10 ('Keep the existing GCFPE actor, one dedicated PR-development session, …') to step 35. If :10 is left, validate_gcfpe_current.py:652 passes only because a stale sentence survives.
```

- **Invariant**

```text
Deliberately reversed ('dedicated PR-development session' leaves the shared list). The new literal must pin the exact nine-field ordered list.
```

#### `fv-rest:19` — UNCERTAIN — step 35, 40 (PART-09, PART-11)

- **Check or surface:** Stale same-session and manual-merge prose outside the plan's line lists (no check reads it)
- **Location:** change-flow/SKILL.md:275, :278, :305, :353, :411, :450-455; flowmaster-validate/SKILL.md:164-165, :173, :294

- **Asserts**

```text
change-flow:455 "GCF-17.LINEAGE — PR-35's `MERGE_PENDING` is historical pre-merge evidence and supplies one conditional complete PR-40 invocation. Only after Nathan later asserts that the identified PR was manually merged may that invocation run."
```

- **Required plan step**

```text
Add these lines to steps 35 and 40, or record them as intentionally untouched. After EXECUTE they contradict C-SESSION and C-DISPATCH. flowmaster-validate/SKILL.md:164 ('PR-35 adds zero roles, sessions, … cross-session routes') and :173 are the validator's own statement of the contract.
```

- **Invariant**

```text
Documentation of reversed invariants.
```

#### `fv-rest:20` — WOULD_FAIL — step 38, 39 (PART-11)

- **Check or surface:** Direct PR-35 to PR-40 edge prohibitions, route shorthand and the manual-merge boundary
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1338-1345 (GRAPH_DIRECT_PR40_EDGE), :1835-1838 (DIRECT_PR35_PR40_EDGE), :1781-1795 (ROUTE_GRAPH_SHORTHAND), :1926-1946 (PR40_MANUAL_MERGE_BOUNDARY); run_gcfpe_20260914_fixtures.py:361, :178-181; scenarios HANDOFF-POS-02

- **Asserts**

```text
if any(edge.get("from") == "PR-35" and edge.get("to") == "PR-40" ...): errors.append("DIRECT_PR35_PR40_EDGE") ... "ordinary_pr_work_unit": [..., "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"] ... manual_pr40[0].get("from") != "NATHAN_MANUAL_MERGE_ASSERTION"
```

- **Required plan step**

```text
These extend the already-found POST_MERGE_CONTRACT defect. Four more checks and one fixture block step 38. Replace them with exact assertions: exactly one PR-35 to PR-40 prompt edge whose condition is 'merge event observed', transport COMPLETE_NEXT_PROMPT_HANDOFF, and whose origin state is not an agent merge; keep DIRECT_PR30_PR40_EDGE; update the DOC-20 recovery-edge phrase 'after Nathan asserts the manual merge'. Change mutation reject-pr35-direct-pr40 to 'reject a second PR-35 to PR-40 edge' or 'reject an agent-merge edge', and rewrite HANDOFF-POS-02 facts (observed_merge_event instead of manual_merge_condition).
```

- **Invariant**

```text
Deliberately reversed (no direct PR-35 to PR-40 edge). Kept and must stay guarded: no agent merge, PR-30 never routes to PR-40, PR-40 verifies independently.
```

#### `fv-rest:21` — UNCERTAIN — step 38, 39 (PART-11)

- **Check or surface:** PR-35 result vocabulary and PR-40 body marker
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1747, :1920-1921, :2444; change-flow/scripts/validate_gcfpe_20260914.py:1006-1011

- **Asserts**

```text
"PR-40": ("historical pre-merge", "independent", "glow-merged-change-attribution-lock"), ... pr35_result_vocabulary == ["MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
```

- **Required plan step**

```text
Step 38 must say which PR-35 state carries the new PR-40 edge. If C-DISPATCH introduces a post-merge state (for example MERGE_OBSERVED), four vocabulary pins break. If the PR-40 body rewrite in step 39 drops 'historical pre-merge', the body check PROMPT_ROUTE_SEMANTICS:PR-40 fails.
```

- **Invariant**

```text
Kept (closed vocabulary) unless the plan adds a state deliberately.
```

#### `fv-rest:22` — WOULD_FAIL — step 41, 42, 43 (PART-12)

- **Check or surface:** Positive and negative header fixtures
- **Location:** flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:420-447 (with validate_gcfpe_20260914.py:910, :1068-1077)

- **Asserts**

```text
clean_header = [pr35["title"], "Prompt Version: 091426.1", "Set: Glow HDE Complete Prompt Flow 091426.1", "Prompt ID: PR-35", "Ecosystem release: GCFPE-20260914.1", f"Notion URL: {pr35['notion_url']}", "## Native purpose",] ... lines.__setitem__(5, ...)
```

- **Required plan step**

```text
This fixture is coupled to the already-found header check. Once the check forbids the three keys, 'accept-identity-only-prompt-header' fails. Removing the three lines leaves 4 lines, so index 5 raises IndexError, surfacing as FMV-GCF-CANDIDATE-FIXTURE-EXECUTION-001, and the len(nonblank) >= 7 guard fails. Rebuild clean_header without the keys (padded to 7 or more nonblank lines), re-index the URL-label mutations, and add negatives: a header carrying 'Prompt Version:', 'Set:' or 'Ecosystem release:' must be rejected.
```

- **Invariant**

```text
Kept: identity-only header. The positive fixture moves to the new shape, and the new forbidden_regex needs its own failing case (D14).
```

#### `fv-rest:23` — WOULD_PASS — step 12-17, 29-40, 42, CHILD (PART-04, PART-09, PART-11, PART-12, CHILD)

- **Check or surface:** change-flow/SKILL.md:559 loads the 091326.2 alias as the 'current specialization overlay', and validate_gcfpe_current.py enforces the alias's stale values
- **Location:** change-flow/SKILL.md:559-561; flowmaster-validate/scripts/validate_gcfpe_current.py:51, :202-217, :260-268, :301-309, :543-552; validate_flowmaster.py:360-364 (OPTIONAL_REFERENCES), :1115-1126

- **Asserts**

```text
"direct_drive_artifact_links": True, "state_decisions_constraints_unresolved": True, ... "returned_reference": "DIRECT_GOOGLE_DRIVE_LINK", ... "ordinary_implementation": ["PR-10", "PR-20", "PR-30", "NATHAN_PRODUCT_OWNER", "PR-40", "QA-10"]
```

- **Required plan step**

```text
The plan does not touch the alias, and the staleness gets worse. After EXECUTE, the overlay that change-flow tells runtime to 'apply' contradicts D23 on five rules: handoff content (C-HANDOFF), artifact reference (Drive rather than repository path), PR-35 session (the alias has no PR-35; continuation_preserves PR_SESSION), merge dispatch (a Nathan boundary between PR-30 and PR-40) and the PR-40 reject route (CHILD). The default suite certifies the contradiction because validate_gcfpe_current.py hard-codes the alias values. Add a step that re-points the overlay to the 091426.1 contract; schema 4.0 makes validate_gcfpe_current.py:619-622 and run_gcfpe_current_fixtures.py:105-109 dispatch to v4. The step must update OPTIONAL_REFERENCES (:360-364) and SKILL.md:559-561. Otherwise record the alias as a known out-of-scope contradiction in D23 and section E.
```

- **Invariant**

```text
The alias checks guard a superseded contract. Re-pointing replaces them with the v4 checks, which is not weakening. Leaving them keeps a validator that enforces the rules D23 reverses.
```

#### `fv-rest:24` — WOULD_FAIL — step 1, 42 (PART-01, PART-12)

- **Check or surface:** Current-alias body validator: pre-existing NameError and 091326.2 header
- **Location:** flowmaster-validate/scripts/validate_gcfpe_current.py:543-552, :602

- **Asserts**

```text
or nonblank[1] != "Prompt Version: 091326.2" or "Ecosystem release: GCFPE-20260913.1" not in text ... text = paths[prompt_id].read_text(encoding="utf-8")
```

- **Required plan step**

```text
Pre-existing, not caused by the plan: any --bodies-stdin call raises NameError: name 'paths' is not defined (reproduced). Step 1 correctly uses validate_gcfpe_20260914.py. EXECUTE must not fall back to validate_gcfpe_current.py for body checks. Record this as an out-of-scope defect for a follow-up Modification.
```

- **Invariant**

```text
Pre-existing defect, outside this plan's scope.
```

#### `fv-rest:25` — UNCERTAIN — step 14, 19 (PART-04, PART-05)

- **Check or surface:** Paste-ready handoff block literals
- **Location:** change-flow/scripts/validate_gcfpe_20260914.py:1024 (change-flow/SKILL.md:295); flowmaster-validate/scripts/validate_gcfpe_20260914.py:2595 (glow-hde-pr-development:162)

- **Asserts**

```text
"exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block", ... "exactly one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`",
```

- **Required plan step**

```text
Steps 14 and 19 rewrite change-flow:295 and glow-hde-pr-development:162. State that the block-shape sentence is kept verbatim and only the field list is replaced. Otherwise update both literals to the C-PLACE wording.
```

- **Invariant**

```text
Kept (one fenced text block, first line NEXT_PROMPT_HANDOFF).
```

#### `fv-rest:26` — WOULD_FAIL — step 35, 40, 47 (PART-09, PART-11, skills)

- **Check or surface:** Skill revision pins across the suite
- **Location:** validate_flowmaster.py:147, :686 (change-flow 3.2.9), :182 (session-relay 3.0.0), :1221 (validator_revision 3.2.14); validate_gcfpe_current.py:634-635, :651 (glow-hde-pr-development 1.2.5); validate_gcfpe_20260914.py:1090, :1722, :2592; run_gcfpe_20260914_fixtures.py:702; change-flow validator :746; validation-profile.json:27-28, :45; contract pr_development_contract.primary_skill_revision

- **Asserts**

```text
"CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9", ... "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0", ... "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5",
```

- **Required plan step**

```text
The plan is silent on revision bumps. The skills' own rules require one on behaviour change: change-flow/SKILL.md:565 (increment so two behaviours do not advertise one identity), session-relay SKILL.md:723, and flowmaster-validate/SKILL.md:44-45 (corrected bytes must not reuse an identity). Add a step that sets the new revision of each of the four skills and moves every pin listed at this entry's location in the same package.
```

- **Invariant**

```text
Kept (identity pinning). Values move.
```

#### `fv-rest:27` — UNCERTAIN — step CHILD (and 34) (CHILD pr40-reject-replans)

- **Check or surface:** R1 row misidentified; R1 transition GCF-17.LINEAGE to GCF-14 undeclared
- **Location:** flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json rows GCF-15, GCF-16, GCF-17.LINEAGE, GCF-14; validate_flowmaster.py:974-981 (FMV-GCF-EDGE-003); fixtures/change-flow/scenarios.json

- **Asserts**

```text
GCF-15 failure_stop_condition: "STOP_PLAN_IDENTITY_MISMATCH or STOP_PO_PROCEED_NOT_INVOKED"; GCF-16: "STOP_SECOND_APPROVAL_OBJECT_REQUESTED or STOP_PLAN_CHANGED_AFTER_PROCEED"; GCF-17.LINEAGE next: ["GCF-19", "GCF-20"]
```

- **Required plan step**

```text
The child's analysis cites GCF-15 as carrying STOP_SECOND_APPROVAL_OBJECT_REQUESTED, but that stop is on GCF-16 and concerns a separate binding object. The rows that block the new route are GCF-17.LINEAGE (no 'next' back to GCF-14; recovery owner) and GCF-14/GCF-15 (session text 'same dedicated PR session'). No validator compares prompt edges with R1 'next', so a graph re-route would pass silently. A fixture of the replan path would raise FMV-GCF-EDGE-003. The child's plan must re-pin the correct rows, add GCF-14 to GCF-17.LINEAGE.next (the count stays 46), and add a positive R1 fixture for GCF-17.LINEAGE to GCF-14. The child is status PLANNING with no approved plan, so none of this is in any executable step yet.
```

- **Invariant**

```text
Deliberately reversed for the replan route only. The single Proceed per plan (GCF-16) is kept.
```

#### `fv-rest:28` — WOULD_PASS — step CHILD (CHILD pr40-reject-replans)

- **Check or surface:** Single-Proceed guards and the PR-40 receiver-name binding
- **Location:** docs/graph/parts/global.json:48; scenarios PR-SPLIT-NEG-01 (extra-proceed-only); run_gcfpe_20260914_fixtures.py:60, :324; validate_gcfpe_20260914.py:1697, :1710; validate_gcfpe_current.py:258, run_gcfpe_current_fixtures reject-second-proceed; body receiver binding validate_gcfpe_20260914.py:2355-2380

- **Asserts**

```text
"condition": "original explicit Proceed for the exact work unit; never a second Proceed" ... "new_proceed_required": False, ... Every prompt-id destination of a non-terminal public branch must be named in the body.
```

- **Required plan step**

```text
These guard the within-plan single Proceed, which the child keeps. Keep them. Reword global.json:48 to 'one Proceed per approved per-PR plan', which moves the routing-surface pin. Add a positive fixture: PR-40 REJECT, then PR-20 in a new session, then a new Proceed is lawful. The PR-40 body must name PR-20, or the body scan raises the receiver-binding error.
```

- **Invariant**

```text
Kept within a cycle. Only the post-reject replan is newly lawful.
```

#### `fv-rest:29` — WOULD_PASS — step 15, 34, 46 (gate)

- **Check or surface:** The default suite does not exercise the 091426.1 contract, graph or fixtures
- **Location:** flowmaster-validate/scripts/validate_flowmaster.py:836-838 (candidate NOT_REQUESTED unless --gcfpe-contract), :806-834; flowmaster-validate/SKILL.md:186-218

- **Asserts**

```text
coverage["gcfpe_20260914_candidate"] = {"status": "NOT_REQUESTED"} ... if gcfpe_contract is not None: from validate_gcfpe_20260914 import validate_package as validate_candidate
```

- **Required plan step**

```text
exp2: after a blanket pin replace, including rewriting the historical contracts, `validate_flowmaster.py` alone returned FLOWMASTER_SUITE_PASS while the 091426.1 contract and graph pins were stale. The same tree with --gcfpe-contract failed. Steps 15, 34 and 46 must state the exact command: `validate_flowmaster.py --strict-warnings --gcfpe-contract <change-flow>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json --gcfpe-candidate-root <scratch>` (with <scratch>/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json holding the embedded JSON extracted from the build), plus `change-flow/scripts/validate_gcfpe_20260914.py`, plus the legacy historical-byte validators. Also 'injected regression (old row text with new pin) fails' proves only the byte pin, not semantic alignment.
```

- **Invariant**

```text
Verification gap, not a check change.
```

#### fv-rest — Tooling

- **item**

```text
Baseline, which passes today (exit 0): PYTHONDONTWRITEBYTECODE=1 python3 <skills>/flowmaster-validate/scripts/validate_flowmaster.py --skills-root <skills>. This validates only the 091326.2 selected alias, the R1 oracle and runtime map, self-identity and the R1 fixtures.
```

- **item**

```text
Candidate overlay, required to exercise 091426.1: python3 flowmaster-validate/scripts/validate_flowmaster.py --strict-warnings --gcfpe-contract <change-flow>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json --gcfpe-candidate-root <root>, where <root>/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json must be byte-identical to the bundled graph.
```

- **item**

```text
change-flow's own fail-fast validator: python3 <skills>/change-flow/scripts/validate_gcfpe_20260914.py (no arguments; it stops at the first failing require).
```

- **item**

```text
Graph rebuild, which writes only to the given output: python3 glow-graph-contract/scripts/graph_parts.py build /home/user/glow-hdengine-v2/docs/graph/parts <scratch>/graph.md. The embedded JSON block plus its final LF is today byte-identical to both bundled graph copies (569835 B, sha256 90021eb7…, verified semantically and by size and digest). The markdown prologue's complete_source_bytes/sha256 values in global.json are stale (580051 / 77e9e1e0…) but are re-stamped on build.
```

- **item**

```text
Body scan: echo "$bodies" | python3 flowmaster-validate/scripts/validate_gcfpe_20260914.py <change-flow> --contract <contract> [--candidate-root <root>] --bodies-stdin. Read prompt_bodies_validated and prompt_body_checks_not_evaluated, not only ok. Never use validate_gcfpe_current.py --bodies-stdin, which raises NameError at :602.
```

- **item**

```text
Section-13 fixtures directly: python3 flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py <change-flow> --contract <contract>.
```

- **item**

```text
Historical-byte validators, all passing today and failing once the runtime map changes (exp3): python3 flowmaster-validate/scripts/validate_strength_middleware.py <change-flow>; validate_epic_alpha.py <change-flow>; validate_epic_reengineering.py --change-flow <change-flow>; run_strength_middleware_fixtures.py <change-flow>; run_epic_alpha_fixtures.py <change-flow>. Also passing today and unaffected: validate_integrated_readiness.py, validate_pre_guide_correction.py, validate_final_scan.py, validate_alpha_feedback.py, run_integrated_readiness_fixtures.py --change-directory, run_final_scan_fixtures.py --change-directory, run_alpha_feedback_fixtures.py.
```

- **item**

```text
Self-identity re-declaration: SKILL_TREE_SHA256 = validate_gcfpe_20260914.skill_tree_digest(<flowmaster-validate root>), which excludes the declaration line. Exactly one declaration line is allowed.
```

- **item**

```text
Install verification: python3 /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/freeze.py <installed tree>, which excludes manifest.json.
```

- **item**

```text
All experiments ran with PYTHONDONTWRITEBYTECODE=1 on copies: /tmp/claude-0/pf/skills (baseline), exp1 (plan-named pins only), exp2 (blanket replace), exp3 (active pins only, historical preserved), exp4 (full hash-chain re-stamp, which passes everything), exp5 (C-SESSION verbatim).
```

#### fv-rest — Live-window risks

- **item**

```text
PART-12 bodies without headers against installed flowmaster-validate 3.2.16: every body read and validated in the window fails PROMPT_BODY_IDENTITY (validate_gcfpe_20260914.py:1068-1077), so all 55 bodies report as defective. A maintenance or audit session could 'repair' them by restoring the header lines, silently reverting the approved change (AF-001). Until the execution PR merges, the registry on main still carries required_regex 'Prompt [Vv]ersion: 091426.1' and 'Ecosystem release', so the governance audit also fails 55 of 55.
```

- **item**

```text
PART-09 session split against installed glow-hde-pr-development 1.2.5 (:10, :53, :82, :164) and change-flow 3.2.9 (:301-307). The change-flow authority order (:345-349) ranks the specialization skill above the stage prompt, so a PR-30 session in the window continues into PR-35 in the same session and emits a 'same dedicated session' handoff. Meanwhile the new PR-35 body and registry input expect session_disposition NEW_DEDICATED. The results are an R1 GCF-17 STOP_SESSION_MISMATCH, or two sessions working the same PR if the operator follows both.
```

- **item**

```text
PART-11 dispatch against the installed skills. The new PR-35 body stays subscribed and emits the PR-40 handoff on the observed merge. The installed glow-hde-pr-development (:110, :164) and change-flow (:331, :353, :455) end PR-35 at MERGE_PENDING with a conditional PR-40 invocation for Nathan. In the window, PR-40 can be dispatched twice for one merge (subscription event plus Nathan's paste), or not at all when the old skill never subscribes. PR-40's fallback ('Nathan's assertion where no subscription existed') covers only the second case.
```

- **item**

```text
PART-04 handoffs against the installed skills. New bodies drop branch, commit and head from handoffs and forbid restating decisions. The installed glow-hde-pr-development:22 requires 'the exact workspace/worktree, branch, open PR and remote-head lineage' in the PR-35 entry handoff, and the installed change-flow:295 tells producers to carry 'current status, decisions, constraints'. A PR-35 session under the old skill may reject a C-HANDOFF-compliant handoff as incomplete (RECOVERY_PENDING), and producers under the old skill emit handoffs that break the new body rule.
```

- **item**

```text
CHILD, if its body edits ride this package: PR-40's REJECT routes to PR-20 in a new session with a new Proceed. The installed change-flow:313/:323 ('requests a second Proceed' / 'creates another Proceed') and glow-hde-pr-development:82 ('create another PR/session/Proceed') forbid this, and the installed bundled contract and graph still route PR-40 reject to PR-30. A PR-20 session under the installed skills refuses the finding. The child has no approved plan (status PLANNING, plan_approved_by empty).
```

- **item**

```text
False assurance in the window: the installed default suite reads no bodies and never validates the 091426.1 contract, so it keeps returning FLOWMASTER_SUITE_PASS while bodies contradict the installed skills and the bundled contract and graph.
```

- **item**

```text
Partial or non-atomic install of the four packages. flowmaster-validate pins change-flow's runtime-map SHA, change-flow and glow-hde-pr-development revisions and literals, the byte-identical contract (CONTRACT_CHANGE_FLOW_BYTE_MISMATCH) and its own SKILL_TREE_SHA256. Any mixed old/new state fails the suite. At runtime, a new change-flow with an old glow-hde-pr-development gives contradictory PR-30/PR-35 session rules. flowmaster-validate/SKILL.md:37 already says 'Both skills ship together and install together'. The Product Owner install step should require one atomic install of all four, verified by freeze.py.
```

- **item**

```text
Authority lag: D23 (step 0), the registry guards and the graph parts land on main only when Nathan merges the execution PR. Body edits go live immediately. In the window, bodies cite D23 and C-* rules that main does not yet hold.
```

- **item**

```text
C-VERSION inconsistency: bodies change in place while every page stays at 091426.1, and the bundled 091426.1 contract (4.0.6) still describes the pre-edit bodies. During and after the window, a version string no longer distinguishes pre-edit from post-edit behaviour. The plan should state that C-VERSION takes effect from the next release, or it contradicts its own rule.
```

#### fv-rest — Notes

- **item**

```text
The known defects are confirmed. Extensions in validate_gcfpe_20260914.py beyond the known list: GRAPH_DIRECT_PR40_EDGE :1338-1345, DIRECT_PR35_PR40_EDGE :1835-1838, ROUTE_GRAPH_SHORTHAND :1781-1795, PR40_MANUAL_MERGE_BOUNDARY :1926-1946, HANDOFF_CONTRACT :1481-1493 (status_completed_work_decisions_constraints_unresolved_authority), HANDOFF_PROHIBITED_REFERENCES :1494-1499, GRAPH_PROOFS protected_r1_46_rows_unchanged :1956, PROTECTED_IDENTITIES r1_oracle_changed False :1966, CHANGE_FLOW_CONTRACT 'PR-30 and PR-35 are two phases' :2581, and the ten-field glow-hde-pr-development literal :2594.
```

- **item**

```text
How R1 rows GCF-15 and GCF-17 are validated: only as whole-file SHA (FMV-ORACLE-007), plus profile_id, matrix SHA (FMV-ORACLE-003), coverage exactly {46, 26, 20} with 46 unique ids (FMV-ORACLE-004/005), and an exact 12-field set per row (FMV-ORACLE-006). The change-flow runtime map must equal the oracle projection row by row (FMV-GCF-ROW-001) and is SHA-pinned (FMV-GCF-MAP-006). graph_findings checks next, producer and consumer closure. R1 fixtures check actor and next-edge transitions; session is checked only for Thoth (GCF-04/05/07). No check recomputes source_row_sha256 or compares prompt-graph edges with R1 'next'. Counts of 46 rows (26 core, 20 material) are pinned at validate_flowmaster.py:506-533 and :777, in the protected_identities of the profile, graph and contract, and at change-flow validator :1015. A text-only re-pin keeps all counts.
```

- **item**

```text
Complete site list for replacing the oracle SHA 52807e58…. Named by the plan: flowmaster-validate/SKILL.md:149; validate_gcfpe_20260914.py:1130/:1379/:1964; validate_gcfpe_current.py:80; docs/graph/parts/global.json:555. Missed: validate_flowmaster.py:38; flowmaster-validate/SKILL.md:246; validation-profile.json:35; both bundled contracts at :3114 and both bundled graphs at :10492 (these follow from regeneration); the current alias at :805. Historical, and 'immutable' per change-flow/SKILL.md:561: gcfpe-20260913.1-091326.2-direct-handoff-contract.json:808 and gcfpe-20260913.1-direct-handoff-contract.json:773.
```

- **item**

```text
The runtime-map SHA family (5574666e…) is absent from the plan. It is pinned at validate_flowmaster.py:41, validate_gcfpe_current.py:81, validate_gcfpe_20260914.py:1131/:2611, validation-profile.json:37, change-flow/SKILL.md:557 and the alias at :806. Historical pins: validate_strength_middleware.py:14, validate_integrated_readiness.py:8, validate_pre_guide_correction.py:9, and six correction-layer JSONs plus two historical contracts.
```

- **item**

```text
exp4 is the key hazard. Once every hash pin is mechanically re-stamped, the candidate-overlay suite and change-flow's validator both PASS on a contract that still claims r1_oracle_changed:false, protected_r1_46_rows_unchanged:true and a same-session PR-35 (receiver_compatibility). A search-and-replace EXECUTE therefore goes green while the semantic claims are false. Every semantic flag needs its own explicit, reviewed step.
```

- **item**

```text
C-SESSION as written includes backticks ('`PR-30` and `PR-35` are two phases'). Verbatim placement breaks two literal checks (exp5).
```

- **item**

```text
A change-flow/SKILL.md:559 pointer answer is included: yes, the plan makes its staleness materially worse (see the dependency entry). A clean fix exists because validate_gcfpe_current.py and run_gcfpe_current_fixtures.py already dispatch schema-4.0 contracts to the v4 validator. Re-pointing also needs validate_flowmaster.py OPTIONAL_REFERENCES (:360-364), because change-flow may link only the runtime map and the current-alias file.
```

- **item**

```text
No generator exists for the direct-handoff contract. graph_parts.py builds only the graph, so step 15 ('Regenerate from the graph parts; never hand-edit') cannot be executed as written. This applies to transition_contract and to every contract-only key that PART-09, PART-11 and the CHILD must change.
```

- **item**

```text
Pre-existing items outside this plan's scope: validate_gcfpe_current.py:602 NameError ('paths') on any --bodies-stdin call; flowmaster-validate/SKILL.md:178 still requires a 'Selection status: REGISTER_CONTROLLED' header, contradicting :99-105; fixtures/gcfpe-20260913.1/scenarios.json is referenced by no script.
```

- **item**

```text
In the CHILD modification record (docs/ephemeral/modifications/MODIFICATION-20260923-pr40-reject-replans.md, §A), the row analysis is wrong on a checkable fact. STOP_SECOND_APPROVAL_OBJECT_REQUESTED belongs to GCF-16, and its approval_contract ('bounded to one Plan; it does not authorize … another Plan') already accommodates a new Proceed for a new plan. The rows that actually block the replan are GCF-17.LINEAGE ('next' has no GCF-14) and the 'same dedicated PR session' text in GCF-14/15.
```

- **item**

```text
Scope honoured: read-only. Writes went only to /tmp/claude-0/pf/. No git, no Notion, no prompt bodies fetched, nothing written under the installed skills tree. The legacy validators and graph build ran only on scratch copies.
```

### pr-relay-graph — PR skill, relay, graph skill and graph parts (34 findings)

#### `pr-relay-graph:0` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** validate_glow_hde_pr_development.py required['PR-30 to PR-35']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:38 (literal only at SKILL.md:53)

- **Asserts**

```text
"PR-30 to PR-35": "same-session `PR-35` handoff",
```

- **Required plan step**

```text
Step 35 lists validator literals ':32-34' but not ':38'. Replace ':38' with a C-SESSION literal such as "exactly one complete `PR-35` handoff to the dedicated PR-35 session". Add "same-session `PR-35` handoff" to the `forbidden` list (validator:91-103). Without that, step 35's own verification ('injected old literal fails') cannot fail, because the validator only checks for presence.
```

- **Invariant**

```text
The change deliberately reverses this check (same session becomes its own session). The new literal must still guard 'exactly one PR-35 handoff from PR-30'. Replacing it without adding the old text to the forbidden list weakens the check.
```

#### `pr-relay-graph:1` — WOULD_FAIL — step 35 (PART-09)

- **Check or surface:** validate_glow_hde_pr_development.py required['exact GCF-17 continuity list'] (plus cross-surface copies)
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:55 (SKILL.md:55); cross-surface: flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594 reads installed SKILL.md; change-flow/scripts/validate_gcfpe_20260914.py:1022

- **Asserts**

```text
"The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage"
```

- **Required plan step**

```text
Add validator ':55' to step 35. Replace it with "The exact ordered nine-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage". Put the same text at flowmaster-validate validate_gcfpe_20260914.py:2594, which the simulation showed failing as SKILL_CONTRACT:glow-hde-pr-development:<ten-field literal>. Also edit SKILL.md:158 ('which the ten-field continuity list requires') and behavior-cases.md:13. Neither is in step 35's list, and no check catches either one.
```

- **Invariant**

```text
Partly kept: the nine remaining fields must stay 'exactly one, in order', so the new literal must list all nine. The session field is removed on purpose.
```

#### `pr-relay-graph:2` — WOULD_PASS — step 35 (PART-09)

- **Check or surface:** validate_glow_hde_pr_development.py required['single session'] and validate_gcfpe_current.py PR skill marker
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:32 (literal at SKILL.md:10 AND :53); cross-surface flowmaster-validate/scripts/validate_gcfpe_current.py:650-655

- **Asserts**

```text
"single session": "one dedicated PR-development session",  |  validate_gcfpe_current.py:652: "## Recover before creating work", "one dedicated PR-development session", "RS-40", "PR-50",
```

- **Required plan step**

```text
Step 35 edits SKILL.md:53 but not :10, so both checks keep passing on the old text at :10 while the skill contradicts itself. The simulation confirmed this: with only :53 rewritten, both the skill's own validator and validate_gcfpe_current pass. Add SKILL.md:10, :22 ('same-session PR-35 handoff'), :27 ('followed in the same session by PR-35') and :158 to step 35. Then replace validator:32 with a two-session literal, for example "run in two dedicated sessions", and add the old literal to the forbidden list. Once :10 changes, validate_gcfpe_current.py:652 fails (simulated: FMV-GCF-CURRENT-001 PR_SKILL_CONTRACT_MISSING), so its marker must change in the same flowmaster-validate package.
```

- **Invariant**

```text
The change deliberately reverses this check. While :10 still carries the old text, the check passes against a stale line and guards nothing.
```

#### `pr-relay-graph:3` — UNCERTAIN — step 35 (PART-09)

- **Check or surface:** validate_glow_hde_pr_development.py required['PR-30 ownership'], ['PR-35 ownership']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:33-34 (SKILL.md:53)

- **Asserts**

```text
"`PR-30` owns recovery, implementation, local testing, coherent commit creation, and deliberate initial publication" / "`PR-35` owns remote review retrieval, corrections, local retesting, coherent corrective publication, CI economy, current-head verification, and genuine merge readiness"
```

- **Required plan step**

```text
Step 35 lists ':32-34' as literals to update. ':33' and ':34' guard phase ownership, which C-SESSION keeps. Step 35 should say these two sentences stay verbatim inside the rewritten :53. Simulation: replacing the whole of :53 with C-SESSION fails both.
```

- **Invariant**

```text
The change keeps this invariant. These literals must not be rewritten; updating them on the session's own judgement would quietly weaken them (AF-001).
```

#### `pr-relay-graph:4` — UNCERTAIN — step 35 (PART-09)

- **Check or surface:** validate_glow_hde_pr_development.py required['PR-35 fit']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:31 (SKILL.md:10)

- **Asserts**

```text
"PR-35 fit": "PR-30 and PR-35 are two phases of the same native PR-execution authority",
```

- **Required plan step**

```text
When SKILL.md:10 is added to step 35, keep this clause verbatim and change only the 'one dedicated PR-development session' part. C-SESSION's 'two phases of one work unit' fits alongside it.
```

- **Invariant**

```text
The change keeps this invariant (one authority across both phases).
```

#### `pr-relay-graph:5` — UNCERTAIN — step 14 (PART-04)

- **Check or surface:** validate_glow_hde_pr_development.py required['postpublication handoff qualification']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:52 (SKILL.md:22)

- **Asserts**

```text
"postpublication handoff qualification": "only when `PR_RETURN_PHASE: PR-35`, the PR-35 handoff",
```

- **Required plan step**

```text
SKILL.md:22 is an intake list, not a handoff field list. Converging it on C-HANDOFF should remove only 'same-session' and move 'workspace/worktree, branch, open PR and remote-head lineage' to entry-recovery checks, as step 13 does for PR-35. The clause 'only when `PR_RETURN_PHASE: PR-35`, the PR-35 handoff' must stay verbatim. Simulation: replacing the whole line fails this check.
```

- **Invariant**

```text
The change keeps this invariant (the RS-40 postpublication qualification).
```

#### `pr-relay-graph:6` — WOULD_FAIL — step 14, 19 (PART-04, PART-05)

- **Check or surface:** validate_glow_hde_pr_development.py required['paste-ready handoff'] and flowmaster-validate SKILL_CONTRACT marker
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:54 (SKILL.md:162); cross-surface flowmaster-validate/scripts/validate_gcfpe_20260914.py:2595

- **Asserts**

```text
"paste-ready handoff": "exactly one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`",
```

- **Required plan step**

```text
In steps 14 and 19, replace only the field-list clause at :162 ("supply every required repository path and repository/PR reference; state current status, completed work, decisions, constraints, unresolved items, and preserved authority; and state the next required action and expected output") with C-HANDOFF, then append C-PLACE. The first sentence must stay verbatim. Simulation: replacing the whole of :162 fails both this check and flowmaster-validate :2595. Step 14 also omits SKILL.md:133, the RS-20 package list that includes 'repository/workspace/worktree/branch state, open PR and remote head'. Add it, keeping the literals at :58 and :61 on that line.
```

- **Invariant**

```text
The change keeps this invariant (one fenced NEXT_PROMPT_HANDOFF block).
```

#### `pr-relay-graph:7` — UNCERTAIN — step 40 (PART-11)

- **Check or surface:** validate_glow_hde_pr_development.py required['manual merge'], ['absolute no-agent merge'], ['remote-head proof'], ['historical merge pending']; flowmaster-validate marker
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:45,46,81,82 (all on SKILL.md:110); cross-surface flowmaster-validate/scripts/validate_gcfpe_20260914.py:2593

- **Asserts**

```text
"Nathan / Product Owner performs the merge manually as a separate action." | "This skill never authorizes an agent to merge, enable auto-merge, schedule a merge" | "verified remote-head identity" | "historical pre-merge evidence"
```

- **Required plan step**

```text
Step 40 must add C-DISPATCH after the existing :110 sentences rather than replace them. Simulation: replacing the whole line fails all four checks and the flowmaster-validate one. The tail of :110 ('or keep polling for that manual action') already agrees with C-DISPATCH's 'do not poll'.
```

- **Invariant**

```text
The change keeps these invariants: manual merge, no agent merge, remote-head proof, pre-merge evidence.
```

#### `pr-relay-graph:8` — WOULD_FAIL — step 40 (also 35 on :164) (PART-11)

- **Check or surface:** validate_glow_hde_pr_development.py required['three-event postmerge'] and ['RS-10 not mandatory']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:83 and :59 (both on SKILL.md:164)

- **Asserts**

```text
"three-event postmerge": "PR-40's duty to independently verify actual merged state and landed lineage", | "RS-10 not mandatory": "RS-10 is optional proposal support, not a mandatory in-flight step",
```

- **Required plan step**

```text
Pasting C-DISPATCH into :164 fails ':83' (simulated). Either keep the old phrase or replace the literal with C-DISPATCH's "`PR-40` still verifies the merged state and landed lineage independently". Remove 'use it only after Nathan has manually merged the identified PR' and "Nathan's later merge assertion" from :164, and 'The conditional prompt separately requires Nathan's later manual-merge assertion' from behavior-cases.md:87 (no check catches that line). Keep the rescope sentence on :164 that carries ':59' verbatim.
```

- **Invariant**

```text
PR-40's independent merge verification is kept, so the replacement must still guard it. What starts PR-40 (event_2) is reversed on purpose.
```

#### `pr-relay-graph:9` — UNCERTAIN — step 37 (PART-10)

- **Check or surface:** validate_glow_hde_pr_development.py required['remote evidence predicate'], ['remote evidence reentry']
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:47-48 (SKILL.md:112)

- **Asserts**

```text
"when an actual external review or required check result is unavailable and no useful local action remains" | "exactly one same-session PR-35 re-entry handoff"
```

- **Required plan step**

```text
Put C-SUB in its own sentence before :112 and keep :112 verbatim. Simulation: replacing the whole line fails both checks. The 'same-session PR-35 re-entry' wording stays correct under C-SESSION, because PR-35 re-enters its own session.
```

- **Invariant**

```text
The change keeps this invariant. C-SUB itself says REMOTE_EVIDENCE_PENDING 'apply as before'.
```

#### `pr-relay-graph:10` — WOULD_PASS — step 20 (PART-06)

- **Check or surface:** validate_glow_hde_pr_development.py required['remote action ledger'], ['publication checkpoint'], ['pre-wait checkpoint'] and the anchor of step 20
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:49-51 (SKILL.md:59); SKILL.md:108

- **Asserts**

```text
"`PR_REMOTE_ACTION_LEDGER`" | "durable repository checkpoint under `docs/ephemeral/` at PR-30 initial publication" | "before any extended wait for remote-only evidence"
```

- **Required plan step**

```text
Step 20 puts C-DEC in `PR_IMPLEMENTATION_RESULT` at ':59', but SKILL.md never names `PR_IMPLEMENTATION_RESULT`; :59 is the remote-action-ledger paragraph. Move the step to SKILL.md:108 ('the complete PR implementation result and handoff artifacts are saved and read back') and name the artifact there. Add a new required literal 'In-flight decisions' to the validator, matching registry step 21. Otherwise C-DEC has no guard in the skill.
```

- **Invariant**

```text
A new invariant (C-DEC) with no guard unless a literal is added. The existing checkpoint literals must stay.
```

#### `pr-relay-graph:11` — WOULD_PASS — step 10 (PART-03)

- **Check or surface:** SKILL.md anchor for C-ART; validate_glow_hde_pr_development.py required['Repository destination']
- **Location:** glow-hde-pr-development/SKILL.md:155-158; validator:53

- **Asserts**

```text
SKILL.md:155 "Save Specifications, Plans, ... and handoff files as efficient machine-readable Markdown under the repository path:" (path follows on :157)
```

- **Required plan step**

```text
Appending C-ART to ':155' puts it between 'under the repository path:' and the path on :157. Put it after :158 or :160 instead. Add the required literal 'never carries the only copy' to the validator, matching registry step 11.
```

- **Invariant**

```text
A new invariant with no guard unless a literal is added.
```

#### `pr-relay-graph:12` — WOULD_PASS — step 24 (PART-07)

- **Check or surface:** validate_glow_hde_pr_development.py literals on the rescope procedure next to the C-LAT anchors
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:56-58,61,74 (SKILL.md:132-133); anchors SKILL.md:65,:128,:135; behavior-cases.md:47-49

- **Asserts**

```text
"create and read back one complete formal bounded `RESCOPE_REQUEST`" | "same-whole-change-IA RS-20" | "return one populated, standalone, copy-paste-ready RS-20 review package" | "`PR-30_PREPUBLICATION`, `PR-30_POSTPUBLICATION`, or `PR-35`"
```

- **Required plan step**

```text
No literal sits on :65, :128 or :135 (simulated: pass). Step 24 must leave the numbered procedure at :130-133 intact, since it carries five literals. Add the required literal 'Decide it during work', matching registry step 25. Converge behavior-cases.md:49 ('requires an approved-boundary change') and keep the validated heading '## Material rescope'.
```

- **Invariant**

```text
The existing rescope invariants are kept. The C-LAT tree is new and needs a guard.
```

#### `pr-relay-graph:13` — WOULD_PASS — step 27 (PART-08)

- **Check or surface:** SKILL.md:79 (no check covers this line)
- **Location:** glow-hde-pr-development/SKILL.md:79

- **Asserts**

```text
"- Bundle related implementation or review corrections into one locally verified push when practical. Never push merely to trigger another remote run."
```

- **Required plan step**

```text
Step 27's replacement text drops the second sentence, 'Never push merely to trigger another remote run.' No check guards it, so a whole-line replacement loses the rule silently. Keep that sentence, or record that it is removed on purpose.
```

- **Invariant**

```text
The change keeps this rule; losing it would be an unguarded weakening.
```

#### `pr-relay-graph:14` — UNCERTAIN — step CHILD (pr40-reject-replans PART-01)

- **Check or surface:** validate_glow_hde_pr_development.py forbidden list, plus the single-Proceed and one-PR text in SKILL.md
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:97,98,100; SKILL.md:10,:17-18,:27,:77,:82,:135,:158

- **Asserts**

```text
forbidden: "normal Plan/instruction path", "receives its own PO Proceed", "PR-35 receives a new Proceed" | SKILL.md:27 "continuation preserves the original Proceed and never requires or creates a second Proceed" | :158 "The work unit keeps exactly one branch and one pull request"
```

- **Required plan step**

```text
The child names only 'the single-Proceed wording in glow-hde-pr-development', with no lines. It needs these edits: SKILL.md:17-18, :27 and :10, saying that after a PR-40 REJECT the re-plan's new Proceed governs a new PR-20, PR-30, PR-35, PR-40 cycle; :77, :82 and :158, saying one branch and one PR per cycle, since Nathan's ruling opens a new PR in a new seeded session; a new required literal; and a behavior-case heading such as '## PR-40 rejection re-plan'. The wording must avoid the forbidden strings. A test phrase, 'the re-planned work unit receives its own PO Proceed', hits forbidden:98, and 're-plans through the normal Plan/instruction path' hits :97.
```

- **Invariant**

```text
The forbidden entries guard single-Proceed for rescope and PR-35, which the child keeps. The child reverses it only for the PR-40 re-plan branch. Narrowing the forbidden list to make room for the child would weaken the check and must be stated explicitly.
```

#### `pr-relay-graph:15` — WOULD_PASS — step 35, 40 (PART-09, PART-11)

- **Check or surface:** behavior-cases.md content (the validator checks headings only)
- **Location:** glow-hde-pr-development/references/behavior-cases.md:7,11,13,17,87; validator case_headings :108-130

- **Asserts**

```text
cases:7 "exactly one complete same-session PR-35 handoff ... The phase split creates no new role, session, Proceed" | cases:11 "in the same dedicated PR-development session" | cases:87 "requires Nathan's later manual-merge assertion"
```

- **Required plan step**

```text
Step 35 names 'behavior-cases.md' with no lines. List :7, :11, :13 and :17 for C-SESSION and :87 for C-DISPATCH. Only headings are validated, so stale case text passes. Consider headings for C-DEC, C-LAT, C-SUB and the re-plan, and add them to case_headings.
```

- **Invariant**

```text
No check guards this; stale acceptance examples would pass silently.
```

#### `pr-relay-graph:16` — UNCERTAIN — step 35, 40, 47 (skills)

- **Check or surface:** revision pins for glow-hde-pr-development and session-relay-flowmaster
- **Location:** glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:26; flowmaster-validate/scripts/validate_gcfpe_20260914.py:1722 and :2592; flowmaster-validate/scripts/validate_gcfpe_current.py:651; flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:26-29; flowmaster-validate/scripts/validate_flowmaster.py:182

- **Asserts**

```text
"GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5" | "primary_skill": "glow-hde-pr-development", "primary_skill_revision": "1.2.5" | "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0"
```

- **Required plan step**

```text
The plan does not say whether either skill's revision is bumped. A bump fails all the listed pins together. The 1.2.5 value also sits inside the hash-pinned direct-handoff contract (pr_development_contract.primary_skill_revision). Decide the bumps and update every pin in the same four-package set. Leaving 1.2.5 on changed content means the revision marker no longer identifies the content.
```

- **Invariant**

```text
Revision identity is kept only if every pin moves together.
```

#### `pr-relay-graph:17` — WOULD_PASS — step 2 (PART-02)

- **Check or surface:** relay manifest SHARED_STATE model (CONTROL_PLANE enum) and update_control_record binding
- **Location:** session-relay-flowmaster/SKILL.md:268, :353, :372; scripts/validate_relay_manifest.py:1094-1095, :1102-1118, fixture :1633-1640; references/manifest-v2-examples.md:51,:118; references/behavioral-test-fixtures.md:20; flowmaster-validate/scripts/validate_flowmaster.py:232

- **Asserts**

```text
SKILL.md:353 "CONTROL_PLANE: NOTION | NONE" | validator:1094 allowed_token(shared_state.get("control_plane"), {"NOTION", "NONE"}) | :1112 "update_control_record requires shared_state.control_plane NOTION"
```

- **Required plan step**

```text
Simulated: rewriting :268 with C-NOTION leaves the relay self-test at PASS (230/230) and validate_flowmaster at PASS. The manifest model is now stale, though: live task and handoff state is declared to live in docs/ephemeral, but CONTROL_PLANE can only be NOTION or NONE, and the only control-record write targets a Notion page. Record an explicit disposition. Either keep the enum, with Notion meaning 'a destination-named maintenance surface', and say so at :353 and :372; or add REPOSITORY, which changes the validator, fixtures, example :51 and validate_flowmaster.py:232 together. Step 2's only verification is a grep.
```

- **Invariant**

```text
Not guarded: no relay check reads the prose at :268.
```

#### `pr-relay-graph:18` — WOULD_PASS — step 14, 19 (PART-04, PART-05)

- **Check or surface:** relay prompt-locator and handoff-content rules that contradict C-HANDOFF
- **Location:** session-relay-flowmaster/SKILL.md:259, :273, :279, :624

- **Asserts**

```text
:259 "Do not insert a static file URL, provider/file/page ID, or version-pinned filename as a locator substitute in prompt text." | :279 "For a Notion prompt use its versionless name and verified directory; approved runtime versions remain input lineage."
```

- **Required plan step**

```text
C-HANDOFF requires the destination prompt's 'full name, version and direct Notion URL'. Step 14's parenthetical covers only versioned files at :259, not the direct Notion URL. Add :279 (currently only in step 19) and :273 to step 14. :273 says to carry 'verified results and material gaps ... in the existing handoff', which restates artifact content that C-HANDOFF forbids. Decide whether :624 (NOTION_REFERENCE is versionless) is out of scope. No check reads these lines.
```

- **Invariant**

```text
Not guarded. The relay would strip URLs and versions that the new bodies require.
```

#### `pr-relay-graph:19` — WOULD_PASS — step 35, 40 (PART-09, PART-11)

- **Check or surface:** relay PR-lane paragraph, and whether an injected-regression guard is possible
- **Location:** session-relay-flowmaster/SKILL.md:283, :285; flowmaster-validate/scripts/validate_flowmaster.py:323-335 (CONTRACT_FORBIDDEN for the relay)

- **Asserts**

```text
:283 "returns PR_CANDIDATE_PUBLISHED with exactly one complete same-session PR-35 handoff ... returns control without polling for that action. PR-35 supplies the actual populated PR-40 handoff conditional on merge."
```

- **Required plan step**

```text
Simulated: rewriting :283 leaves validate_flowmaster at PASS. validate_relay_manifest.py never reads SKILL.md, so the relay has no way to make a re-inserted old sentence fail. If a regression guard is wanted, add CONTRACT_FORBIDDEN entries to the flowmaster-validate package, for example "same-session PR-35 handoff" and "preferred live control plane".
```

- **Invariant**

```text
Not guarded today.
```

#### `pr-relay-graph:20` — WOULD_FAIL — step 12, 23, 29, 30, 31, 34, 38, CHILD (PART-04/07/09/11 + child)

- **Check or surface:** bundled frozen graph = graph_parts.py build output; hash, byte and edge-count pins
- **Location:** flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:2-9,17-25; flowmaster-validate/scripts/validate_gcfpe_20260914.py:941-942,1113-1121,1145-1165,2528-2529; change-flow/scripts/validate_gcfpe_20260914.py:21,777,780-783,805-809; direct-handoff contract :11541-11543 (source_snapshot.frozen_candidate_graph.sha256) and graph_proofs.route_edge_count (both copies)

- **Asserts**

```text
EXPECTED_FROZEN_GRAPH_SHA256 = "90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223" | EXPECTED_FROZEN_GRAPH_BYTES = 569835 | "edge_count": 227 | require(len(graph["edges"]) == 227 and contract["graph_proofs"]["route_edge_count"] == len(graph["edges"]), ...)
```

- **Required plan step**

```text
Verified: the build's embedded JSON block is byte-identical to both bundled references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json files (569835 B, sha256 90021eb7...). Any part edit changes that hash. No plan step replaces the bundled graph. Add a step after the last graph edit, which includes the child's PR-40 edge and the single R1 re-pin: extract the embedded block from the scratch build; copy it byte-identically into both skills; and re-pin, by script, the sha256, bytes and edge_count at every site listed, plus contract source_snapshot and graph_proofs.route_edge_count in both contract copies. Then re-pin the contract's own sha256 and bytes (2b78f877..., 606657) at profile:4 and :8.
```

- **Invariant**

```text
Kept: bundle equals build, and counts are measured (D15). The new pins must come from the build, not be typed by hand.
```

#### `pr-relay-graph:21` — WOULD_FAIL — step 15 (fed by 12, 23, 29-31, 34, 38, CHILD) (PART-04/09/11 + child)

- **Check or surface:** graph-to-contract parity (validate_graph_contract; change-flow parity requires)
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1215-1257, 1298-1316; change-flow/scripts/validate_gcfpe_20260914.py:810-818; direct-handoff contract (both copies)

- **Asserts**

```text
if graph.get("edges") != contract.get("route_edges"): errors.append("GRAPH_EDGE_CONTRACT_MISMATCH") | ... continuity.get("adds") != development.get("added_boundaries") ... | paired_fields ... "receiving_role", "session_class"
```

- **Required plan step**

```text
I simulated every planned graph edit on a scratch copy. The unchanged contract then reports GRAPH_BOUNDARY_TRANSITION_CONTRACT_MISMATCH, GRAPH_DIRECT_PR40_EDGE, GRAPH_EDGE_CONTRACT_MISMATCH, GRAPH_NODE_CONTRACT:PR-35, GRAPH_POST_MERGE_CONTRACT_MISMATCH, GRAPH_PROTECTED_IDENTITIES, GRAPH_PR_CONTINUITY_MISMATCH and GRAPH_STATE_ROUTE_CONTRACT_MISMATCH. Step 15 covers only transition_contract and says 'regenerate from the graph parts', but no such generator exists: graph_parts.py has only split, build and verify, and nothing in docs/prompt_ecosystem_management writes the contract. Add a step that authors and reviews a scripted contract regenerator driven by the built graph. It must cover route_edges, state_routes, boundary_nodes, boundary_transitions, post_merge_three_event_contract, member_registry[PR-35/RS-40].receiving_role/session_class, pr_development_contract.added_boundaries/shared_exactly_one, graph_proofs.route_edge_count and source_snapshot hash, in both copies.
```

- **Invariant**

```text
Kept: the contract mirrors the graph. Regeneration must not hand-edit the contract (D13).
```

#### `pr-relay-graph:22` — WOULD_FAIL — step 38 (PART-11)

- **Check or surface:** GRAPH_DIRECT_PR40_EDGE
- **Location:** flowmaster-validate/scripts/validate_gcfpe_20260914.py:1349-1355

- **Asserts**

```text
if any(isinstance(edge, dict) and edge.get("from") in {"PR-30", "PR-35"} and edge.get("to") == "PR-40" for edge in edges): errors.append("GRAPH_DIRECT_PR40_EDGE")
```

- **Required plan step**

```text
Step 38 adds a prompt edge from PR-35 to PR-40 (simulated: fails). Narrow the set to {"PR-30"} and add a positive check for the new PR-35 to PR-40 edge. That check should pin the condition 'merge event observed', the transport COMPLETE_NEXT_PROMPT_HANDOFF, and an `automatic` value consistent with 'dispatch is a paste'.
```

- **Invariant**

```text
Partly reversed on purpose: PR-35 may now route to PR-40. 'PR-30 never routes directly to PR-40' is kept (SKILL.md:82), so the new check must still forbid it. State the narrowing explicitly (AF-001).
```

#### `pr-relay-graph:23` — WOULD_PASS — step 12, 23, 29, 30, 31, 38 (graph)

- **Check or surface:** graph_parts.py build validation used as the verification in several steps
- **Location:** glow-graph-contract/scripts/graph_parts.py:164-185

- **Asserts**

```text
ids = {n["id"] for n in obj["nodes"]} | set(obj.get("boundary_nodes") or {}); ids |= {e["to"] for e in obj["edges"]} | {e["from"] for e in obj["edges"]}; for e in obj["edges"]: if e["from"] not in ids or e["to"] not in ids: ...
```

- **Required plan step**

```text
The endpoint check always passes, because every edge endpoint is added to `ids` before the test. I built every planned edit plus a zeroed R1 pin: 'validation PASS', 55 nodes, 227 edges, 569301 B, sha256 94813749.... So 'build passes' in steps 12, 23, 29, 30, 31 and 38 shows only that the parts assemble. Each of those steps also needs flowmaster-validate's validate_graph_contract run against the regenerated contract.
```

- **Invariant**

```text
A weak gate. This does not weaken anything, but it should not be counted as evidence.
```

#### `pr-relay-graph:24` — WOULD_FAIL — step CHILD (pr40-reject-replans PART-01)

- **Check or surface:** PR-40 state_route_order, and derived state_routes order
- **Location:** docs/graph/parts/prompts/PR-40.json:260-268 (branch at :164); glow-graph-contract/scripts/graph_parts.py:68-72

- **Asserts**

```text
"state_route_order": ["accept", "reject_existing_pr_owner", "reject_instruction_owner", ...] | rows.sort(key=lambda r: rank.get(r["branch_id"], len(rank)))
```

- **Required plan step**

```text
If the child renames the branch to `reject_replan` without updating state_route_order, the builder moves that row to the end without any warning. The state_routes order then changes, and GRAPH_STATE_ROUTE_CONTRACT_MISMATCH follows unless the contract is regenerated from that build. Rename the entry in state_route_order in the same scripted transform.
```

- **Invariant**

```text
Kept: row order is meaningful ('approvals first, terminals last').
```

#### `pr-relay-graph:25` — UNCERTAIN — step CHILD, 38 (graph)

- **Check or surface:** edge ordering via edge_indices; contract route_edges equality depends on order
- **Location:** docs/graph/parts/prompts/PR-40.json:2-9 (edge to PR-30 = index 172); PR-35.json:2-7; RS-40.json edge_indices [228-232]; global.json:3-17 (_other_edge_indices: 13 indices for 3 edges); graph_parts.py:136-148

- **Asserts**

```text
pairs = list(zip(other_eidx or range(len(other_edges)), other_edges)) ... pairs.append((ei[j] if j < len(ei) else nxt, e))
```

- **Required plan step**

```text
Index counts already disagree with edge counts: 235 indices for 227 edges, and CF-C-10 has 4 indices for 5 edges, ESC-40 3 for 5, QA-70 5 for 4. The transform must say how edges are placed. The child should replace the PR-40 to PR-30 edge in place, keeping index 172. New PR-35/RS-40 to PR-40 edges then append at 235 and above. Removing an _other_edges entry must keep relative order. Regenerate contract route_edges from the built order.
```

- **Invariant**

```text
Order-sensitive parity is kept; nothing checks index alignment.
```

#### `pr-relay-graph:26` — WOULD_FAIL — step CHILD (pr40-reject-replans PART-01)

- **Check or surface:** the Proceed boundary text, which exists in two independent copies in global.json, plus PR-20's edge
- **Location:** docs/graph/parts/global.json:45-57 (_other_edges) and :308-316 (boundary_transitions.NATHAN_PROCEED); docs/graph/parts/prompts/PR-20.json:56; PR-40.json:153-184

- **Asserts**

```text
"branch_id": "original_proceed", "condition": "original explicit Proceed for the exact work unit; never a second Proceed" | PR-20.json:56 "one complete executable approved-scope plan awaits the original Product Owner Proceed"
```

- **Required plan step**

```text
The child's analysis cites only global.json:48. The builder does not reconcile the _other_edges copy with the boundary_transitions copy, so both must be edited identically. PR-20.json:56 also needs a re-plan-aware condition. Both copies must then flow through to the contract (boundary transitions and edges parity).
```

- **Invariant**

```text
Reversed on purpose for the PR-40 re-plan only; 'never a second Proceed' still holds for every continuation.
```

#### `pr-relay-graph:27` — UNCERTAIN — step 38 (PART-11)

- **Check or surface:** the merge-assertion route, in its two global.json copies, the per-prompt edges and DOC-20's restatement
- **Location:** docs/graph/parts/global.json:32-44, :272-275, :299-307, :447-471; prompts/PR-35.json:9-40 (condition :21); prompts/RS-40.json merge_pending edge (:21, to at :38); prompts/DOC-20.json:151

- **Asserts**

```text
"condition": "Nathan has manually merged the identified PR and invokes the conditional PR-40 block" | DOC-20.json:151 "actual merged state or landed-lineage review is required after Nathan asserts the manual merge"
```

- **Required plan step**

```text
Step 38 must decide whether the NATHAN_MANUAL_MERGE_ASSERTION boundary node and its edge remain as the no-subscription fallback that step 39 implies. The builder cannot detect a boundary left with no inbound edge. The final edge count comes from that decision; pin the measured count. Add DOC-20.json:151, which restates the DOC-20 body that step 39 edits. Reconcile `direct_PR35_to_PR40_automatic_edge: true` with the edge-level `automatic` flag, given the ruling that dispatch is a paste or a session launch. closure.py reads only prompts/*.json (closure.py:31-53), so 'PR-35 upstream of PR-40' appears only if the new edge is in PR-35.json with to_kind 'prompt'.
```

- **Invariant**

```text
The trigger is reversed on purpose; PR-40's independent verification is kept.
```

#### `pr-relay-graph:28` — UNCERTAIN — step 29, 30 (PART-09)

- **Check or surface:** field names for the continuity additions, and cross_session_route consistency
- **Location:** docs/graph/parts/global.json:473-485 (adds.session :482, adds.cross_session_route :475); prompts/PR-35.json:164 (adds_session), :170 (cross_session_route); contract pr_development_contract.added_boundaries (contract:2936)

- **Asserts**

```text
"adds": { ... "cross_session_route": 0, ... "session": 0, ... } | PR-35 node "adds_session": false, "cross_session_route": false
```

- **Required plan step**

```text
Step 29 says to set 'added_boundaries.session', but that is the contract's field name; no graph part has it. The graph field is pr_continuity_contract.adds.session at global.json:482. Step 30 sets adds_session but leaves cross_session_route false at PR-35.json:170 and 0 at global.json:475, although the PR-30 to PR-35 handoff now crosses sessions. No check ties these fields together. Name the exact graph fields, decide cross_session_route, and mirror the result into the contract's added_boundaries. That trips the already-known PR35_ADDED_BOUNDARY check at :1742.
```

- **Invariant**

```text
Partly reversed (session). cross_session_route is unguarded either way.
```

#### `pr-relay-graph:29` — UNCERTAIN — step 23 (vs 22) (PART-07)

- **Check or surface:** graph conditions that restate 'material boundary' for bodies edited in step 22
- **Location:** docs/graph/parts/prompts/PR-40.json:197; prompts/DOC-10.json:127; prompts/DOC-20.json:219; (PR-10.json:157 and PR-20.json:157 already in step 23; OPS-30.json:175 out of scope by ruling)

- **Asserts**

```text
PR-40.json:197 "a substantiated material boundary requires a new bounded rescope proposal" | DOC-10.json:127 "repository evidence proves a complete bounded material boundary" | DOC-20.json:219 "evidence proves a bounded material delta"
```

- **Required plan step**

```text
Step 22 changes the routing sentences in the PR-40, DOC-10 and DOC-20 bodies, but step 23 updates only PR-10 and PR-20 in the graph. Either add these three conditions to step 23 or record an explicit no-change disposition (D13: the graph restates the bodies). OPS-30 correctly stays unchanged; it appears only as a state-sharer in PR-40's closure radius.
```

- **Invariant**

```text
Keeps the graph and bodies aligned; no check covers it.
```

#### `pr-relay-graph:30` — WOULD_FAIL — step 34, CHILD (PART-09 + child)

- **Check or surface:** R1 oracle pin inside the graph parts (GRAPH_PROTECTED_IDENTITIES)
- **Location:** docs/graph/parts/global.json:551-557; flowmaster-validate/scripts/validate_gcfpe_20260914.py:1375-1382

- **Asserts**

```text
"r1_oracle_sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
```

- **Required plan step**

```text
Compute the oracle once, after both the GCF-17 row (step 34) and the child's GCF-15 row change. Then update global.json:555, rebuild the graph once, and run the bundled-graph re-pin chain in the bundled-graph entry above. Step 34's acceptance ('grep -rc 52807e58 = 0 across both skills') also covers sites step 34 does not list: flowmaster-validate/scripts/validate_flowmaster.py:38, flowmaster-validate/SKILL.md:246 and the validation profile. It would also require editing the frozen historical contracts (change-flow/references/gcfpe-20260913.1-*.json and gcfpe-current-direct-handoff-contract.json, which is hash-pinned at bf5140c9 in validate_gcfpe_20260914.py:2564). Scope the grep to current artifacts.
```

- **Invariant**

```text
Protected identity is kept, re-pinned once, deliberately. The historical contracts must stay frozen.
```

#### `pr-relay-graph:31` — UNCERTAIN — step 12, 15 (PART-04)

- **Check or surface:** graph handoff_contract compared with pinned transition_contract fields
- **Location:** docs/graph/parts/global.json:341-367; flowmaster-validate/scripts/validate_gcfpe_20260914.py:1259-1269 (only 6 keys compared) and :1481-1500; contract:17594-17618

- **Asserts**

```text
"receiving_role_and_exact_session": True, "epic_change_and_work_unit": True, ... "status_completed_work_decisions_constraints_unresolved_authority": True, "next_action_and_expected_output": True | prohibited_refs != {"Library ID", "unlinked filename", "above", ...}
```

- **Required plan step**

```text
Step 12's new `required` list drops the 'Epic/change and work unit' and 'next action and expected output' items and replaces the status/decisions item; its `prohibited` list gains branch, commit and restated content. Graph parity checks only six keys, so it passes. If step 15 carries these into transition_contract, :1490-1500 fails. Step 15 must list exactly which transition_contract fields change, and flowmaster-validate :1482-1500 must be updated as an explicit reversal.
```

- **Invariant**

```text
The handoff content list is reversed on purpose; the block, fence and first line are kept.
```

#### `pr-relay-graph:32` — WOULD_FAIL — step 45 (and every flowmaster-validate file change: 15, 34, bundle re-pin) (PART-13)

- **Check or surface:** flowmaster-validate self-identity digest
- **Location:** flowmaster-validate/SKILL.md:9; flowmaster-validate/scripts/validate_gcfpe_20260914.py:2246-2280

- **Asserts**

```text
SKILL_TREE_SHA256: eb9634d60a65610c131e5d406d7ed6c69038864c555ad89e4c92b5bfde5dd6a8 | if measured != declarations[0]: return [f"SKILL_SELF_IDENTITY:DECLARED_..._MEASURED_..."]
```

- **Required plan step**

```text
No validator literal sits on SKILL.md:55-60 or :231-232, but any byte change in the flowmaster-validate tree changes skill_tree_digest. Recompute SKILL_TREE_SHA256 as the last edit before packaging. The code comment at validate_gcfpe_20260914.py:2657-2659 repeats the old reason and should be converged too; it is not a check.
```

- **Invariant**

```text
Self-identity is kept; the digest is regenerated, not weakened.
```

#### `pr-relay-graph:33` — WOULD_PASS — step none (stale docs in a surface the plan does not package) (graph)

- **Check or surface:** counts stated in glow-graph-contract SKILL.md
- **Location:** glow-graph-contract/SKILL.md:13, :134

- **Asserts**

```text
:13 "**100%** of its 277 `state_route` rows cite a prompt body" | :134 "verified by `verify`: 55 nodes, 235 edges, 55 state_routes, zero differences."
```

- **Required plan step**

```text
These numbers are already stale: the current build has 227 edges and 280 state_route rows. No check reads them. Any plan-built token will contradict them. Either note that as a known discrepancy or package a fix, which would be a fifth skill.
```

- **Invariant**

```text
Documentation only.
```

#### pr-relay-graph — Tooling

- **item**

```text
Current proof token (read-only build into scratch): PYTHONDONTWRITEBYTECODE=1 python3 /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/scripts/graph_parts.py build /home/user/glow-hdengine-v2/docs/graph/parts /tmp/claude-0/preflight/graph.md -> 'build: 55 nodes, 227 edges, 55 state_routes / embedded JSON 569835 bytes sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223 / validation PASS'. Token: edges 227 · embedded JSON 569835 B · sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223 (280 state_route rows).
```

- **item**

```text
Verify: PYTHONDONTWRITEBYTECODE=1 python3 .../glow-graph-contract/scripts/graph_parts.py verify /home/user/glow-hdengine-v2/docs/graph/parts /tmp/claude-0/preflight/graph.md -> 'semantic round-trip ... IDENTICAL'. This is circular: no committed graph exists by design, so verify compares against the build just made.
```

- **item**

````text
Real parity check: extract the ```json block from the scratch build, append one LF, and run sha256sum on it and on both <skills>/{change-flow,flowmaster-validate}/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json. All three are 90021eb7... at 569835 B. Rerun after every graph edit; the bundled copies must be replaced with the new block.
````

- **item**

```text
PR skill structural validator: PYTHONDONTWRITEBYTECODE=1 python3 <skills>/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py prints PASS today. It stops at the first missing label, so enumerate every failure with the AST harness at /tmp/claude-0/preflight/allmissing.py <skill-dir>.
```

- **item**

```text
Relay self-test: PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/claude-0 python3 <skills>/session-relay-flowmaster/scripts/validate_relay_manifest.py --self-test -> PASS, 230 cases, 0 failed. It writes temporary files only under TMPDIR and never reads SKILL.md.
```

- **item**

```text
Suite on a scratch copy, never the installed tree: cp -r <skills> /tmp/claude-0/preflight/skills. Then run python3 .../flowmaster-validate/scripts/validate_flowmaster.py --skills-root /tmp/claude-0/preflight/skills (FLOWMASTER_SUITE_PASS); python3 .../flowmaster-validate/scripts/validate_gcfpe_20260914.py <copy>/change-flow --contract <copy>/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json (ok, []); and python3 .../flowmaster-validate/scripts/validate_gcfpe_current.py <copy>/change-flow (ok, []).
```

- **item**

```text
Graph-to-contract reconciliation of a candidate build: import validate_gcfpe_20260914 from the scratch flowmaster-validate/scripts and call validate_graph_contract(contract, graph_json_block). Baseline returns []; the simulated plan build returns the 8 mismatch codes listed in the parity entry.
```

- **item**

```text
Closure: PYTHONDONTWRITEBYTECODE=1 python3 /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/closure.py <ID> --json. It reads only docs/graph/parts/prompts/*.json, not global.json. Today: PR-40 has upstream [DOC-20] and downstream [PR-10, PR-30, RS-10]. PR-20 has upstream [DOC-10, PR-10] and radius 21. PR-35 has upstream [ESC-40, PR-30, RS-20, RS-40].
```

- **item**

```text
Self-identity digest for flowmaster-validate: validate_gcfpe_20260914.skill_tree_digest(Path('<copy>/flowmaster-validate')) gives eb9634d6..., matching SKILL.md:9 today. Recompute it after every flowmaster-validate edit.
```

- **item**

```text
No generator exists for the direct-handoff contract (route_edges, state_routes, transition_contract and the rest). Step 15 cannot be carried out from the graph parts with current tooling.
```

#### pr-relay-graph — Live-window risks

- **item**

```text
PART-09, if bodies land first: the PR-30 body hands off to a new dedicated PR-35 session, but the installed glow-hde-pr-development (the primary skill named in the bodies' continuity list) says at :53 'Remain in the one dedicated PR-development session across both phases' and at :82 'Do not ... create another PR/session/Proceed'. The installed relay says 'exactly one complete same-session PR-35 handoff' (:283), and the installed change-flow contract has PR-35 session_class SAME_DEDICATED_PR_DEVELOPMENT_SESSION_AS_PR-30. A PR-30 run in the window gets contradictory authority. It either stops as PRODUCT_OWNER_DECISION_REQUIRED, or sends PR-35 a same-session handoff that the new PR-35 body and registry input ('session_disposition: NEW_DEDICATED') do not expect.
```

- **item**

```text
PART-11: the new PR-35 body says to stay subscribed and emit the PR-40 handoff on the merge event. The installed skill (:110, :164) and relay (:283) still return control with a conditional PR-40 block for Nathan to paste after merging. That can produce two PR-40 invocations (Nathan's paste plus the subscription dispatch) or none, if the subscribed session ends its turn as the old skill directs. PR-40's independent, read-only merge verification limits the damage, but duplicate PR-40 sessions are possible.
```

- **item**

```text
PART-04: the new bodies require the destination prompt's full name, version and direct Notion URL, and no branch or commit. The installed relay (:259, :279) removes URLs and page IDs from prompt text and uses versionless names, so relay-built handoffs may fail the receiving body's 'no unlinked filenames' rule. The installed PR skill (:82, :162) still packs worktree, branch, remote head and restated status or decisions into handoffs. The receivers tolerate extra content, so this is mainly noise, but it contradicts C-HANDOFF.
```

- **item**

```text
PART-02: the new bodies say Notion is read-only except where a destination rule names it, but the installed relay :268 still calls Notion 'the preferred live control plane for current task ... and handoff state'. A relay run with an authorized update_control_record would write live state to Notion, against the new rule. Writes still need explicit authorization, so the risk is limited to authorized runs.
```

- **item**

```text
PART-07 and PART-06 (lower risk): the installed PR skill has neither the C-LAT decision tree nor an In-flight decisions section. PR runs in the window may send findings to rescope that the new bodies would decide in flight, and their results will lack the section the bodies now describe. The registry guards check bodies, not results.
```

- **item**

```text
Child change (high for that branch): a PR-40 body that routes REJECT to a PR-20 re-plan with a new Proceed, new session and new PR conflicts with every installed surface: the PR skill (:27 'never requires or creates a second Proceed'; :77 and :158 one PR per work unit; :82); the installed change-flow contract (NATHAN_PROCEED 'never a second Proceed'; PR-40 REJECT routes to PR-30); and R1 GCF-15 STOP_SECOND_APPROVAL_OBJECT_REQUESTED. A re-plan started in the window would be stopped or flagged as a violation until the packages install.
```

- **item**

```text
Graph parts and bundled contract: if the execution PR merges before change-flow and flowmaster-validate are installed, a build from main produces a token that differs from the installed bundled graph (90021eb7...). The installed change-flow still routes by the old bundled route_edges (PR-40 REJECT to PR-30, the manual-merge boundary) while the parts and bodies describe new routes. If the skills install first, the reverse holds. Record this as an expected transitional mismatch, not a defect.
```

- **item**

```text
Install order: installed flowmaster-validate reads the installed glow-hde-pr-development SKILL.md (validate_gcfpe_20260914.py:2590-2606, validate_gcfpe_current.py:646-655) and pins the relay revision (validate_flowmaster.py:182). Installing only some of the four packages makes the installed suite fail, as the SKILL_CONTRACT and PR_SKILL_CONTRACT_MISSING simulations showed. Install all four, then run the full flowmaster-validate suite once. The plan's Product Owner install action checks only freeze digests.
```

- **item**

```text
Trigger surface: until install, the synced manifest.json description of glow-hde-pr-development still reads 'in its single dedicated development session', so skill selection contradicts the new bodies during the window.
```

- **item**

```text
PART-12: nothing in my surface reads the header lines being deleted. The graph node titles and candidate_version come from titles, and the PR skill resolves the version from the page title (:25). The installed flowmaster-validate body check is a known break covered elsewhere.
```

#### pr-relay-graph — Notes

- **item**

```text
Everything was read-only. The only writes were under /tmp/claude-0/preflight: scratch skill copies (skills/, simA/, sim_*/, simR/), parts_sim/, graph.md, embedded.json, graph_sim.md and the harnesses allmissing.py, litmap.py, simstep.py and graphsim.py. All Python ran with PYTHONDONTWRITEBYTECODE=1. git status for docs/graph is clean. The installed synced skill tree was not touched, and no git, Notion or prompt-body fetches were made.
```

- **item**

```text
Baselines all PASS: the PR skill validator; the relay self-test (230/230); validate_flowmaster (FLOWMASTER_SUITE_PASS); validate_gcfpe_20260914 (ok); validate_gcfpe_current (ok); and graph build and verify (55 nodes, 227 edges, 55 state_routes, IDENTICAL).
```

- **item**

```text
Confirmed and extended the known defects. The simulated C-SESSION edit fails the PR skill's own validator at :38 and :55. It also fails flowmaster-validate validate_gcfpe_20260914.py:2594 as SKILL_CONTRACT:glow-hde-pr-development:<ten-field literal>. Once SKILL.md:10 is also edited, validate_gcfpe_current.py:652 fails as FMV-GCF-CURRENT-001. Step 35 names only validator ':32-34', and ':33-34' guard ownership, which the change keeps.
```

- **item**

```text
Step 35's SKILL.md line list (:3, :53, :55, :82, :164) misses every other line that asserts one shared session: :10, :22, :27 ('followed in the same session by PR-35') and :158 ('ten-field continuity list'). :100 and :141 should be reworded to name each phase's own session. Leaving :10 unedited lets two checks pass on stale text.
```

- **item**

```text
Whole-line replacement at the plan's anchors (simulated) fails these literals: step 14 fails validator :52 and :54, and flowmaster-validate :2595. Step 19 fails :54. Step 37 fails :47 and :48. Step 40 fails :45, :46, :59, :81 and :83, and flowmaster-validate :2593. Steps 10, 20, 24 and 27 fail nothing, but step 20's anchor (:59, where `PR_IMPLEMENTATION_RESULT` does not appear) and step 10's anchor (mid-sentence at :155) are wrong, and step 27 drops an unguarded rule.
```

- **item**

```text
Build output does feed the bundled candidate-graph contract: the embedded JSON block equals both bundled files byte for byte. So every graph part edit, including the R1 re-pin in global.json protected_identities, forces a new bundled graph, new hash, byte and edge-count pins, and regeneration of the contract fields that mirror the graph. The plan's step 15 covers only transition_contract, and no generator exists.
```

- **item**

```text
The graph builder's validation cannot catch semantic errors: the endpoint check is always true. It passed a simulated build carrying every planned edit and a zeroed R1 pin.
```

- **item**

```text
The per-part edge_indices already disagree with edge counts: 235 indices for 227 edges, plus mismatches in CF-C-10, ESC-40 and QA-70. Edge order, and so contract parity, depends on how the transform places or removes edges.
```

- **item**

```text
Step 29's wording 'added_boundaries.session' names a contract field, not a graph field. The graph has pr_continuity_contract.adds.session, and adds.cross_session_route and the PR-35 node's cross_session_route also need a decision.
```

- **item**

```text
The child's graph analysis cites only global.json:48. The same text is duplicated at global.json:311 (boundary_transitions), PR-20.json:56 says 'awaits the original Product Owner Proceed', and PR-40.json:262 state_route_order must be renamed in step with the branch.
```

- **item**

```text
session-relay-flowmaster's own validator never reads SKILL.md, so none of steps 2, 14, 19, 35 or 40 can be guarded there. Any regression guard must live in flowmaster-validate validate_flowmaster.py CONTRACT_FORBIDDEN (:323-335). The CONTROL_PLANE model (NOTION|NONE) is left stale by C-NOTION and needs an explicit disposition.
```

- **item**

```text
Recommend scoping step 34's 'grep = 0' acceptance to current artifacts. Frozen historical contracts carry 52807e58, and one of them is hash-pinned at bf5140c9.
```

### registry-audit — registry and governance-audit skill (21 findings)

#### `registry-audit:0` — WOULD_FAIL — step 46; also the 'audit passes / injected regression fails' verification of 7, 11, 17, 21, 25, 43 (gate)

- **Check or surface:** amthor audit CLI snapshot pinning (sha256 per body) + SRC-003 byte re-compare
- **Location:** amthor-workspace-governance-audit/scripts/audit_workspace_governance.py:466-468, :573-574; SKILL.md:104-110; prompt-corpus-policy.md:104, :110

- **Asserts**

```text
record["sha256"] = sha256_bytes(data) ... if text is not None and sha256_text(text) != source.get("sha256"): ... "SRC-003" ... || policy: "3. **Never an identity.** Not hashed, not byte-compared" / "Still prohibited, without exception: mirrors, exports, snapshots"
```

- **Required plan step**

```text
Step 46 (and each per-step verification) must name the policy-compliant method: evaluate each row's audit_assertions in memory by importing load_data and _evaluate_assertions from a scratch copy of the skill. Feed it the body text read from Notion, the same {id: text} stdin JSON used for --bodies-stdin. Build no snapshot, compute no hash, and write no WGA-*-Evidence.json, because that file embeds the body digests. This matches postflight-procedure.md:44-45 ('pipe it to the shipped validator with --bodies-stdin, run that row's audit_assertions, discard it'). Record the method in §E.
```

- **Invariant**

```text
The corpus-policy invariant is kept. The audit skill's snapshot and hash procedure is the defective element under the policy. Nothing is weakened: the same assertions are evaluated, only without a persisted, hashed corpus.
```

#### `registry-audit:1` — WOULD_FAIL — step 46; per-step 'audit passes' in 7, 11, 17, 21, 25, 33, 39, 43 (gate)

- **Check or surface:** audit_governance verdict: INDETERMINATE without a semantic packet; INV-001 for every registry row absent from the snapshot
- **Location:** audit_workspace_governance.py:585-591, :622-623, :793

- **Asserts**

```text
"INV-001", "ERROR", "prompt", ... "Expected active prompt absent from observed snapshot" ... if not semantic_complete: verdict = "INDETERMINATE" ... return 0 if result["verdict"] in {"PASS", "PASS WITH WARNINGS"} else 2
```

- **Required plan step**

```text
Define 'audit passes' as: zero findings from that row's assertions on the edited body. Define 'injected regression fails' as: the findings on the mutated body, minus the findings on the clean body, equal exactly {(rule_id, 'Required pattern absent: <value>' or 'Forbidden pattern matched: <value>')}. Neither the CLI verdict nor its exit code can serve. A scratch run with one synthetic PR-35 body gave INDETERMINATE with 54 INV-001 findings, and FAIL with 54 INV-001 even with semantic complete:true.
```

- **Invariant**

```text
The CLI's completeness invariants are real but do not apply to a per-row assertion proof. They are not weakened, only not used for this purpose.
```

#### `registry-audit:2` — UNCERTAIN — step 11, 17 (row selection '53 nonterminal rows') (PART-03, PART-04)

- **Check or surface:** registry NEXT_PROMPT_HANDOFF roster, and flowmaster-validate HANDOFF_LITERAL_EXEMPT (a derived copy of it)
- **Location:** project-prompt-contract-registry.md:3643-3645 (PR-35 carries it under rule_id CTR-002, not TOP-001); flowmaster-validate/scripts/validate_gcfpe_20260914.py:2182-2188

- **Asserts**

```text
PR-35: required_literals: - value: NEXT_PROMPT_HANDOFF / rule_id: CTR-002 || HANDOFF_LITERAL_EXEMPT = frozenset({"GCFPE-MGMT-10", "PR-50"})
```

- **Required plan step**

```text
State the selector exactly: rows whose audit_assertions.required_literals contain value NEXT_PROMPT_HANDOFF. Assert that count == 53, PR-35 is in the set and GCFPE-MGMT-10 and PR-50 are not. Selecting on rule_id TOP-001 gives 52 rows and drops PR-35, one of only two bodies whose handoff lists branch/worktree/head. Selecting on graph nonterminality gives 54 rows (GCFPE-MGMT-10 has handoff branches to PR-10 and ORIGINAL_NATIVE_STAGE). GCFPE-MGMT-10 gets no C-ART or C-HANDOFF, so it would fail the guards from steps 11 and 17.
```

- **Invariant**

```text
Kept. The 53-row handoff roster is unchanged, and the new guards must use the same roster as flowmaster-validate.
```

#### `registry-audit:3` — WOULD_FAIL — step 17 (PART-04)

- **Check or surface:** proposed forbidden_regex on 'branch, worktree, commit' inside the handoff paragraph
- **Location:** MODIFICATION-20260923-alpha-feedback-open-entries.md:641 (step 17) against C-HANDOFF :559-560 and C-SESSION :588-591

- **Asserts**

```text
step 17: "`forbidden_regex` on \"branch, worktree, commit\" inside the handoff paragraph (bounded by `NEXT_PROMPT_HANDOFF`)" || C-HANDOFF: "It carries no branch and no commit" || C-SESSION: "workspace/worktree, branch, pull request"
```

- **Required plan step**

```text
Do not use a bare-token pattern. In scratch, NEXT_PROMPT_HANDOFF[\s\S]{0,600}?\b(?:branch|worktree|commit)\b matched the clean canonical text itself ('...the minimum context it needs. It carries no branch'). Routing-sense 'branch' ('each nonterminal branch emits one NEXT_PROMPT_HANDOFF') and the verb 'commit' ('commit and push the artifact') are also common near handoff rules. Use the paragraph-bounded, noun-form pattern given in notes (rule_id TOP-001). In scratch it fires on an injected old list and is silent on C-PLACE+C-HANDOFF, C-PLACE+C-SESSION and routing-sense text. Run it as a clean control over all 53 edited bodies before adoption. Adjudicate DOC-20 and PR-40, where landed-lineage 'commit identity' text sits near handoffs, by readback, never by exemption.
```

- **Invariant**

```text
This deliberately reverses the handoff content (D23-B: a handoff carries no branch or commit). Entry-recovery checks in PR-30 and PR-35 must stay outside the guard's scope. That is achieved by anchoring on NEXT_PROMPT_HANDOFF within one paragraph, not by exempting rows.
```

#### `registry-audit:4` — UNCERTAIN — step 11 (PART-03)

- **Check or surface:** proposed required_regex 'never carries the only copy'
- **Location:** MODIFICATION-20260923-alpha-feedback-open-entries.md:635 (step 11) and :553-554 (C-ART source is hard-wrapped between 'never' and 'carries')

- **Asserts**

```text
C-ART: "The handoff names that artifact; it never\n  > carries the only copy of a fact." || step 11: "`required_regex: 'never carries the only copy'`"
```

- **Required plan step**

```text
Use value 'never\s+carries\s+the\s+only\s+copy' (rule_id CTR-002). In scratch, the literal-space pattern failed on the wrapped variant and the \s+ pattern passed both. The evaluator uses re.MULTILINE only, not DOTALL (audit_workspace_governance.py:539).
```

- **Invariant**

```text
A new guard for D23-A. Note D11 (decision-record:584-600): an assertion should test behaviour, not wording. A canonical-sentence assertion is acceptable only because §P fixes the wording, and the record should say so.
```

#### `registry-audit:5` — WOULD_FAIL — step 43 (with 42) (PART-12)

- **Check or surface:** required_regex SRC-001 'Prompt [Vv]ersion: `?091426\.1`?' and INV-003 'Ecosystem release: `?GCFPE-20260914\.1`?' on all 55 rows
- **Location:** project-prompt-contract-registry.md:240-243 (CF-C-10; the same pair on every row, 55x each)

- **Asserts**

```text
- value: 'Prompt [Vv]ersion: `?091426\.1`?'
  rule_id: SRC-001
- value: 'Ecosystem release: `?GCFPE-20260914\.1`?'
  rule_id: INV-003
```

- **Required plan step**

```text
Step 43 covers the removal, but the replacement forbidden_regex must be windowed to the header. C-HANDOFF keeps 'name, version and direct Notion URL' in handoff blocks, so an unanchored 'Prompt [Vv]ersion:' fires on any version line in a handoff template. In scratch, even today's required regex matched a template line 40 lines down: it never proved the header existed. Use the three \A-anchored first-8-nonblank-line patterns in notes, matching flowmaster's header window. Step 43 omits a guard for 'Set:', which step 42 also deletes; add it.
```

- **Invariant**

```text
D23-G deliberately reverses this and supersedes D11's in-body version assertion. The release binding does not survive at ERROR severity. Afterwards the only in-audit binding is expected_title '— 091426.1' through NAM-001 (audit_workspace_governance.py:602-603), which is WARNING severity and runs only when the source supplies a title. §E should record this as moving the binding to the register, not as keeping it.
```

#### `registry-audit:6` — WOULD_PASS — step 7 (and 3, 4, 5) (PART-02)

- **Check or surface:** proposed forbidden_regex CONTROL_NOTION
- **Location:** MODIFICATION-20260923-alpha-feedback-open-entries.md:631; decision-record D14 :714-742

- **Asserts**

```text
D14: "Verifying that the banned vocabulary is absent does not establish that the retired behaviour is gone." ... "no ruling is considered applied until a guard exists that would catch its reintroduction, and that guard has been fired by an injected regression."
```

- **Required plan step**

```text
Add a functional companion on all 55 rows: 'operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b' (CTR-001). In scratch it catches the old sentence reworded without the token and is silent on C-NOTION. Also add guards for steps 4 and 5, which currently have none: QA-10 row forbidden 'Notion and repository persistence' (CTR-001), and forbidden 'Notion-resident artifact' (CTR-001) on the 10 rows of step 5 or on all 55. CONTROL_NOTION appears in no graph part or skill, so the token guard alone is silent before and after the change on 48 bodies.
```

- **Invariant**

```text
A new guard for the Class B Notion policy. The token guard is kept, and the functional pattern adds what D14 requires.
```

#### `registry-audit:7` — UNCERTAIN — step 33 (PART-09)

- **Check or surface:** PR-35 authored inputs / session fields (YAML typing)
- **Location:** project-prompt-contract-registry.md:3604-3606, :3611

- **Asserts**

```text
session_class: SAME_SESSION_CONTINUATION / session_role: You are the same dedicated PR-development session ... / - same dedicated PR session reference with session_disposition RETAIN_EXISTING
```

- **Required plan step**

```text
Quote the new input. Written as a plain '- session_disposition: NEW_DEDICATED', PyYAML parses it as a mapping {'session_disposition': 'NEW_DEDICATED'}, not a string (verified in scratch). validate_project_registry never type-checks inputs, so it passes silently. Also set session_role to the graph receiving_role of step 30 verbatim: 52 of 55 rows already match node.receiving_role exactly, and PR-35 is one of the three that do not. Rewrite creator_role at :3606 too, since the step only names session_class.
```

- **Invariant**

```text
D23-D deliberately reverses the same-session contract.
```

#### `registry-audit:8` — WOULD_PASS — step 33 (PART-09)

- **Check or surface:** PR-35 forbidden mutation
- **Location:** project-prompt-contract-registry.md:3633

- **Asserts**

```text
- Add an R1 row, actor, approval, Proceed, work unit or session
```

- **Required plan step**

```text
Do not just delete 'session'. Replace the line with '- Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session'.
```

- **Invariant**

```text
Mostly kept. Only PR-35's own dedicated session reverses. Dropping the word 'session' would also stop guarding against a third session being added, which would be a check quietly weakened (AF-001).
```

#### `registry-audit:9` — UNCERTAIN — step 31, 33 (PART-09)

- **Check or surface:** RS-40 and PR-40 authored session text
- **Location:** project-prompt-contract-registry.md:5108-5109 (RS-40), :3708 (PR-40 input)

- **Asserts**

```text
RS-40 session_role: You are the same dedicated PR engineering session for the exact suspended work unit. || PR-40: - Existing PR reviewer/session lineage for a rereview, the dedicated PR session identity, ...
```

- **Required plan step**

```text
Step 33 cites :5108 but gives no text. Supply one, for example 'You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.' Also change RS-40.json node.receiving_role in step 31 to the identical string: today registry and graph agree for RS-40, and editing only the registry creates drift. Add a step to edit PR-40 :3708 'the dedicated PR session identity' to 'the PR-30 and PR-35 session identities'.
```

- **Invariant**

```text
Reversal under D23-D. Registry-graph role agreement is a de facto convention that should be kept.
```

#### `registry-audit:10` — WOULD_FAIL — step 38, 39 (PART-11)

- **Check or surface:** D13-derived outputs[].consumers and required_interfaces for PR-35 and RS-40, checked by the postflight registry-vs-graph drift check
- **Location:** project-prompt-contract-registry.md:3623-3624, :3682-3683 (PR-35); :5123-5126, :5141-5144 (RS-40); POSTFLIGHT-REPORT-r27.md:61; decision-record.md:700-705

- **Asserts**

```text
PR-35 consumers: - RS-20 || D13: "routing and result states are **derived** into the registry from `docs/graph/parts/`, never authored independently there ... Where the registry and the graph disagree, the graph wins and the registry is regenerated."
```

- **Required plan step**

```text
After step 38, regenerate these fields; do not hand-edit them. PR-35 consumers and required_interfaces become [PR-40, RS-20]. If RS-40's merge_pending boundary edge (to NATHAN_MANUAL_MERGE_ASSERTION) also becomes a prompt edge, RS-40 becomes [PR-30, PR-35, PR-40, RS-20]. If step 38 adds a result state (for example one for 'merge observed'), regenerate outputs[].states for PR-35 and RS-40. Step 39 edits only the PR-40 input at :3710 and misses all of this. No regeneration script exists (see tooling), so the plan must add one as a scripted step.
```

- **Invariant**

```text
Kept: the registry equals the graph. The values follow the deliberate graph reversal (direct_PR35_to_PR40_automatic_edge becomes true).
```

#### `registry-audit:11` — WOULD_FAIL — step CHILD (pr40-reject-replans PART-01)

- **Check or surface:** D13-derived PR-40 consumers and required_interfaces; PR-20 authored inputs; the postflight PR-20 inputs check
- **Location:** project-prompt-contract-registry.md:3717-3720, :3735-3738 (PR-40); :3428-3429 (PR-20 inputs); POSTFLIGHT-REPORT-r27.md:63

- **Asserts**

```text
PR-40 consumers: - PR-10 - PR-30 - RS-10 || PR-20 inputs: - PR_INSTRUCTION_ID || r27 (f): "`PR-20`'s registry `inputs` are exactly `[\"PR_INSTRUCTION_ID\"]`."
```

- **Required plan step**

```text
Regenerate PR-40 consumers and required_interfaces from the moved part, from [PR-10, PR-30, RS-10] to [PR-10, PR-20, RS-10]. PR-40 has only one edge to PR-30 (reject_existing_pr_owner), so PR-30 drops out. Add a PR-20 input, for example 'PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the same WORK_UNIT_ID in a new dedicated session seeded by Nathan'. The next postflight should restate check (f) by its real criterion ('no QA Guide or QA Plan') and not as 'exactly [PR_INSTRUCTION_ID]'.
```

- **Invariant**

```text
D13 agreement is kept. The PR-20 inputs check guards 'no QA Guide or QA Plan', which is kept. Only the one-input shape is reversed.
```

#### `registry-audit:12` — WOULD_FAIL — step CHILD; 32-36; 37-40; 18 (D23-D, D23-E, D23-F, D23-B placement)

- **Check or surface:** D23 'tested guard' requirement: no registry assertion is listed for these rulings
- **Location:** gcfpe.decision-record.md:1280-1283

- **Asserts**

```text
Each ruling gets a registry assertion with an injected must-fail regression, as listed in the Modification's §P. **Until those land, `D23` is ruled but not applied.**
```

- **Required plan step**

```text
Add guard steps with injected regressions, YAML in notes. D23-D (PART-09): forbidden old continuity-list form on the ~17 continuity bodies, and required 'they do not share a session' on PR-30, PR-35 and RS-40. D23-E (PART-10/11): required subscribe/do-not-poll/observed-merge wording on PR-35, RS-40 and PR-40. D23-F (child): forbidden the old PR-30 continuation clause on PR-40, and required PR-40's review artifact among PR-20's inputs. D23-B placement (PART-05): required 'ends with the NEXT_PROMPT_HANDOFF block' on the 53 rows, plus the ASK OK? ordering on QA-60, QA-80, RS-10 and RS-30. Without these, step 33's and step 39's 'audit passes' is vacuous: no deterministic assertion reads session_class, inputs or merge wording.
```

- **Invariant**

```text
New guards for deliberate reversals. Each new expectation must still guard what is kept: no extra role, approval, Proceed or work unit; no polling; no agent merge; PR-40's independent verification.
```

#### `registry-audit:13` — WOULD_FAIL — step 46, 47 (gate / skills)

- **Check or surface:** amthor-workspace-governance-audit SKILL.md Alpha-feedback invariants, which the semantic maker/reader review enforces
- **Location:** amthor-workspace-governance-audit/SKILL.md:38, :40, :41, :43, :44, :47, :49

- **Asserts**

```text
:38 "carries every already-existing required artifact ... or its direct Notion URL for a Notion-resident artifact; carries status, decisions, constraints, unresolved items, next action, and expected output" :40 "adds no role, approval, ... Proceed, session, ... or cross-session route" :49 "Nathan's later invocation asserts only that Nathan manually merged"
```

- **Required plan step**

```text
Add amthor-workspace-governance-audit as a fifth package in step 47, under D24 review. Amend :38 to C-HANDOFF and drop the Notion-resident clause; :40, :41 and :43 to C-SESSION; :49 to C-DISPATCH (keeping 'MERGE_PENDING is historical', 'PR-40 independently verifies' and no-merge); :44 to one Proceed per plan cycle under D23-F; :47 to 'the recorded phase's own session'. Bump the revision at SKILL.md:10. Without this, step 46's own governance audit judges the 53 new bodies against the reversed rules and fails, and it keeps failing after the four packages are installed.
```

- **Invariant**

```text
Mixed. Reversed: handoff completeness (D23-B), the same session (D23-D), the merge-assertion trigger (D23-E) and the single Proceed (D23-F). Kept, and must still be guarded: one fenced text block; destination name, version and URL; no blanks, menus or alternates; the nine shared continuity fields; no agent merge; no polling; PR-40 independent verification.
```

#### `registry-audit:14` — WOULD_FAIL — step 46, 47 (gate / skills)

- **Check or surface:** amthor references restating the same invariants
- **Location:** amthor-workspace-governance-audit/references/interoperability-contracts.md:13, :18, :53-54, :68, :74, :96; references/behavioral-fixtures.md:48-50, :52

- **Asserts**

```text
interop:18 "The sole GCFPE exception is one selected PR-30 → PR-35 same-session phase continuation inside existing R1 row GCF-17; it adds no role, approval, ... Proceed, session, ... or cross-session route." interop:74 "Nathan's later invocation asserts only a manual merge"
```

- **Required plan step**

```text
Amend these lines in the same fifth package, to the canonical wordings (C-HANDOFF, C-SESSION, C-DISPATCH).
```

- **Invariant**

```text
The same reversed and kept split as SKILL.md.
```

#### `registry-audit:15` — WOULD_FAIL — step 34, 47 (PART-09 (R1 GCF-17 re-pin))

- **Check or surface:** run_fixture_suite.py SkillSelfContractFixtures.test_exact_gcf17_continuity_parity, plus the revision pin
- **Location:** amthor-workspace-governance-audit/scripts/run_fixture_suite.py:24, :303-310 (revision pin at :307)

- **Asserts**

```text
EXACT_GCF17_CONTINUITY = "The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; ..." ... self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", skill)
```

- **Required plan step**

```text
When the audit skill is amended, replace the constant with the re-pinned GCF-17 wording from step 34, byte-for-byte, and move the :307 pin together with SKILL.md:10. In a scratch copy, removing 'dedicated PR-development session;' from the three .md files gave 1 failure of 34 tests.
```

- **Invariant**

```text
A derived copy of the R1 oracle row. It must be updated to the new pin, not deleted, because the parity guard between SKILL.md, the references and the fixtures stays valuable.
```

#### `registry-audit:16` — UNCERTAIN — step 44 (C-VERSION, prospective) (PART-12)

- **Check or surface:** amthor predecessor-archive invariant
- **Location:** amthor-workspace-governance-audit/SKILL.md:32

- **Asserts**

```text
After authorized selection, verify each predecessor prompt moved intact to the existing scope-appropriate archive and was not deleted, overwritten, or treated as runnable.
```

- **Required plan step**

```text
In the fifth package, narrow this to 'each member that received a successor page'. Under C-VERSION an unchanged member keeps its page, so the current wording would flag the next release.
```

- **Invariant**

```text
Kept for changed members (archive intact, never deleted). Reversed for unchanged members.
```

#### `registry-audit:17` — WOULD_PASS — step 3-5, 8, 13, 18, 20, 22, 32, 37, 39, 42 (all body edits) (all body parts)

- **Check or surface:** registry evidence_contract byte count and SHA-256 (55 rows), and the body_extraction_convention identity claim
- **Location:** project-prompt-contract-registry.md:79-80 (applies_to), :55-56, each row's evidence_contract (e.g. :203-206); authoritative-surfaces.md:59

- **Asserts**

```text
applies_to: 'The evidence_contract byte count and SHA-256 on each row below, which are the body identity for validation.'
```

- **Required plan step**

```text
Add a registry step recording a dated disposition: the evidence_contract identities describe the pre-D23 bodies and are no longer the body identity for validation. They cannot be regenerated, because hashing bodies is prohibited (prompt-corpus-policy.md:104, :110). Correct authoritative-surfaces.md:59 to match. No live check consumes the digests any more (the SF10-12 pins are retired), so nothing fails. But the approved registry would state a false identity, against the rule in prompt-validation-procedure.md:49.
```

- **Invariant**

```text
The invariant that the recorded identity matches the live body is deliberately abandoned by the corpus policy. Record it so; do not silently leave it.
```

#### `registry-audit:18` — WOULD_PASS — step 43 (PART-12)

- **Check or surface:** ecosystem-change-management instrument table
- **Location:** docs/prompt_ecosystem_management/ecosystem-change-management.md:141

- **Asserts**

```text
499 assertions across 55 prompts, 0 failing. `required_regex` binds release identity and Canon source; `forbidden_regex` guards D7 against Drive reintroduction
```

- **Required plan step**

```text
Update the sentence. After step 43, required_regex binds only the Canon source, and the count is 831 today (not 499). Better to drop the count than pin it again (r27 W2).
```

- **Invariant**

```text
A documentation record, not a check. It is deliberately reversed by D23-G.
```

#### `registry-audit:19` — WOULD_PASS — step 7, 11, 17, 21, 25, 26, 33, 39, 43, CHILD (registry)

- **Check or surface:** validate_project_prompt_registry (structure, lane, sequence, TOP-001 consumer closure) and the YAML parse
- **Location:** amthor-workspace-governance-audit/scripts/audit_workspace_governance.py:249-322 (TOP-001 at :310-316); :50-73 fenced-yaml loader

- **Asserts**

```text
if isinstance(consumer, str) and re.fullmatch(r"[A-Z]+(?:-[A-Z]+)*-\d+", consumer) and consumer not in keys: ... "TOP-001" ... "Unknown prompt consumer"
```

- **Required plan step**

```text
Run it after each registry edit (baseline today: valid true, problems []). Make the edits as a line-anchored scripted insertion, then compare the old and new registries semantically through load_data. A yaml.safe_dump round trip would reflow and requote the whole 5301-line Markdown-wrapped file.
```

- **Invariant**

```text
Kept. It checks structure only and cannot catch mistyped inputs (see step 33) or D13 drift.
```

#### `registry-audit:20` — WOULD_PASS — step 33 (PART-09)

- **Check or surface:** registry schema session_class enum (documentation only)
- **Location:** amthor-workspace-governance-audit/references/project-prompt-registry-schema.md:42

- **Asserts**

```text
session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN
```

- **Required plan step**

```text
Optional, in the fifth package: add DEDICATED_PR_REVIEW_SESSION to the documented enum. The enum is already drifted (SAME_SESSION_CONTINUATION), and no script enforces it.
```

- **Invariant**

```text
Documentation drift, not a check.
```

#### registry-audit — Tooling

- **item**

```text
Registry structure check. Run from a scratch copy, never inside the synced directory. cp -r /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/amthor-workspace-governance-audit <scratch>/wga && cd <scratch>/wga/scripts && PYTHONDONTWRITEBYTECODE=1 python3 validate_project_prompt_registry.py /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md. Baseline measured today: {"valid": true, "problems": []}, exit 0.
```

- **item**

```text
Audit-skill fixture suite: cd <scratch>/wga/scripts && TMPDIR=<scratch>/tmp PYTHONDONTWRITEBYTECODE=1 python3 run_fixture_suite.py. Baseline: 34 tests OK. It writes to tempfile, hence TMPDIR. The suite has no Glow-registry fixtures. Precedent for a new guard is AddendumSchemaGuardFixtures (run_fixture_suite.py:319-379): fires on the injected case, silent on the clean control and the negative controls, and no finding when the guard is absent. Durable fixtures for the step 7, 17 and 43 patterns require the fifth skill package.
```

- **item**

```text
Row assertions against live bodies (D22-compliant, no snapshot, no hash). Set PYTHONDONTWRITEBYTECODE=1 and run python3 with a heredoc: sys.path.insert(0,'<scratch>/wga/scripts'); from audit_workspace_governance import load_data, _evaluate_assertions; reg=load_data('<worktree>/docs/prompt_ecosystem_management/project-prompt-contract-registry.md'); rows={r['prompt_key']:r for r in reg['prompts']}; bodies=json.load(sys.stdin) (the same {id:text} JSON piped to --bodies-stdin); for pid,t in bodies.items(): print(pid,[(f['rule_id'],f['observed']['summary']) for f in _evaluate_assertions(rows[pid],t,rows[pid]['notion_page_id'])]). Verified on a synthetic body: a clean row gives [], and adding 'In-flight decisions' to the row gives exactly [('CTR-002','Required pattern absent: In-flight decisions')].
```

- **item**

```text
Must-fail regression, same process. Mutate the in-memory text (delete the canonical sentence for a required_regex; append the old wording in the same paragraph for a forbidden_regex). Require set(findings(mutated)) - set(findings(clean)) == {(rule_id, exact summary)} for that row, so the regression fails for the right reason. Rows carry several assertions under the same rule_id, so filter on (rule_id, value), not rule_id alone.
```

- **item**

```text
D13 derivation. No regeneration script exists in the repository or in any synced skill. graph_parts.py offers only split, assemble, validate, build and verify; closure.py computes closure only; no .py file writes registry consumers. The derivation that reproduces the current registry with 0 drift on all 55 rows (checked in scratch): consumers = required_interfaces = sorted({e['to'] for e in part['edges'] if e['to_kind']=='prompt' and e['to']!=part['id']}), and set(outputs[].states) = set(node['result_states']). Self-loops are excluded, as in r27 check (d). required_interfaces are always sorted; consumers are unsorted in 10 rows. Rewrite only the rows whose set changes, in sorted order: PR-35, RS-40 (step 38) and PR-40 (child). session_class and session_role are authored, not derived: they differ from the graph for PR-35, IA-30 and IA-40.
```

- **item**

```text
CI: the registry path is in _DOCUMENTATION_PREFIXES (ci/checks/classify_ci_changes.py:107-116; any path under it returns no lanes at :1506-1507). No CI lane validates the registry or the guards; all validation is agent-run on demand (README.md:84-88).
```

#### registry-audit — Live-window risks

- **item**

```text
No production PR, QA or Ops session reads the registry or the audit skill at runtime. The live-window breakage from this surface falls on governance audits, postflights and the step-46 gate, not on workflow execution.
```

- **item**

```text
Registry on main versus live Notion bodies: until the execution PR merges, main carries the old registry. Once step 42 deletes the header lines in Notion, any audit against main's registry reports 110 ERROR findings: SRC-001 'Prompt [Vv]ersion: `?091426\.1`?' and INV-003 'Ecosystem release: …' on all 55 rows. Merging the registry first fails in the other direction: the new forbidden-header and required C-ART/C-DEC/C-LAT patterns fire on unedited bodies. No ordering keeps both green, so §E must declare the window, and in-window audits must name the registry commit they used.
```

- **item**

```text
The installed amthor-workspace-governance-audit is not among the four step-47 packages. Its semantic maker/reader invariants (SKILL.md:38, :40, :41, :43, :44, :49) will flag every C-HANDOFF, C-SESSION and C-DISPATCH body as a defect. That happens during the window, in step 46's own gate, and after the four skills are installed, until a fifth package lands.
```

- **item**

```text
An operator following the audit SKILL.md as written (:104-126: local snapshot plus build_snapshot_manifest hashing) during the window would breach prompt-corpus-policy D22 condition 3 and the snapshot prohibition. Any run that omits bodies or the semantic packet returns INDETERMINATE or INV-001 FAIL, a number rather than evidence.
```

- **item**

```text
During the window, main's registry still declares PR-35 as SAME_SESSION_CONTINUATION with input 'session_disposition RETAIN_EXISTING' and forbids it adding a session. It still gives PR-40 the input 'Nathan's later invocation…' and consumer PR-30 (child change). Maker/reader reconciliation of the edited PR-35, PR-40, PR-20 and RS-40 bodies therefore produces declared-versus-observed disagreements (CTR-002, TOP-001, SES-001) that are artefacts of the window.
```

- **item**

```text
D23 is 'ruled but not applied' until the guards land (decision-record:1282-1283). In the window no reintroduction guard exists on main, so a concurrent body edit restoring CONTROL_NOTION, a branch/worktree handoff list or a header line would pass every deterministic check on main.
```

- **item**

```text
From the first body edit, the evidence_contract byte counts and SHA-256 values on main no longer identify the live bodies. The retired SF10-12 bench in docs/ephemeral/gcfpe.round20.sf10-bench/bench.py treats them as the root of trust. If anyone runs it, it reports a mismatch on every edited body.
```

#### registry-audit — Notes

- **item**

```text
Confirmed the known flowmaster-validate defects are outside this surface. This surface adds four gaps: (1) the governance-audit CLI cannot lawfully or meaningfully evaluate the new guards (it hashes the corpus and needs all 55 bodies plus a semantic packet); (2) no registry guard exists for D23-B placement, D23-D, D23-E or D23-F, though D23 requires one per ruling; (3) the D13-derived PR-35, RS-40 and PR-40 consumers are not regenerated, and no script exists to do it; (4) the audit skill's own SKILL.md, references and fixture constant restate the reversed rules but are not in the step-47 package set.
```

- **item**

```text
How the evaluator works (audit_workspace_governance.py:520-545, :585-608). required_literals test 'value not in text' and forbidden_literals test 'value in text'. Both regex kinds use re.search(value, text, flags=re.MULTILINE), with no DOTALL or IGNORECASE, so a multi-line span needs [\s\S] or explicit \n, as the existing addendum_id regex does. Default rule_id is CTR-002 for required_* and CTR-001 for forbidden_*. Every assertion finding is ERROR whatever its rule_id. Bodies arrive only as files named in a snapshot manifest (source kind prompt, notion_prompt or notion_page, source_id equal to the row's notion_page_id). There is no stdin mode and no Notion access. The registry is read from the first fenced yaml block of the .md file. Rule-ID usage today: CTR-001 275, CTR-002 229, SRC-001 165, INV-003 110, TOP-001 52 (plus PR-35's CTR-002 handoff literal), over 831 assertions (114 required_literals, 0 forbidden_literals, 167 required_regex, 550 forbidden_regex). Convention: storage and behaviour prohibitions use CTR-001; required contract content uses CTR-002; the handoff block uses TOP-001; release identity uses SRC-001 or INV-003. Nothing in the audit scripts hard-codes Prompt Version or 55. The hard-coded expectations are the Glow approval literals (:318-321), the schema string (:23), and the fixture-suite GCF-17 constant and revision pin 1.11.3.
```

- **item**

```text
Step 7 YAML (all 55 rows, append to forbidden_regex): '- value: CONTROL_NOTION' / 'rule_id: CTR-001', and '- value: ''operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b''' / 'rule_id: CTR-001'. Extra guards for steps 4 and 5: on the QA-10 row '- value: Notion and repository persistence' (CTR-001); on the 10 rows of step 5 (or all 55) '- value: Notion-resident artifact' (CTR-001). Regression: append 'Concise authorized operational state and pointers remain `CONTROL_NOTION`.' to one edited body in memory; expect exactly (CTR-001, 'Forbidden pattern matched: CONTROL_NOTION'). Clean control: C-NOTION alone gives no finding (checked in scratch).
```

- **item**

```text
Step 11 YAML (53 rows whose required_literals contain NEXT_PROMPT_HANDOFF, append to required_regex): '- value: ''never\s+carries\s+the\s+only\s+copy''' / 'rule_id: CTR-002'. Regression: delete the C-ART sentence from one body in memory; expect (CTR-002, 'Required pattern absent: never\s+carries\s+the\s+only\s+copy').
```

- **item**

```text
Step 17 YAML (same 53 rows, append to forbidden_regex): '- value: ''NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,600}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)''' / 'rule_id: TOP-001'. It compiles and round-trips through YAML single quotes. Scratch results: fires on an old inline list and an old bulleted list; silent on C-PLACE+C-HANDOFF and C-PLACE+C-SESSION in one paragraph, on routing-sense 'branch', and on 'commit and push the artifact'. Regression: append ' It carries the same session, worktree, branch, PR and head commit.' to the paragraph holding PR-35's NEXT_PROMPT_HANDOFF sentence.
```

- **item**

```text
Step 21 YAML (PR-30, PR-35, RS-40): '- value: In-flight decisions' / 'rule_id: CTR-002'. Step 25 YAML (PR-10, PR-20, PR-30, PR-35, PR-40, RS-10, RS-20, DOC-10, DOC-20, IA-30): '- value: Decide it during work' / 'rule_id: CTR-002', and, recommended because it guards the D23-C definition itself, '- value: ''\*{0,2}Material\*{0,2} means a change to the Epic-level commitment''' / 'rule_id: CTR-002'. Do not add a forbidden 'material boundary': step 22 replaces it only in routing sentences, so legitimate uses may remain. Regression: remove the C-DEC section or the C-LAT block in memory.
```

- **item**

```text
Step 26: replace registry:3531 with '- Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35'. It parses as a plain scalar. It is the file's only 'review-correct' occurrence, so the grep check gives 0.
```

- **item**

```text
Step 33 YAML (PR-35 row): 'session_class: DEDICATED_PR_REVIEW_SESSION'; session_role equal to the step-30 receiving_role verbatim ('You are the dedicated PR-35 session for one work unit, entered from PR-30''s handoff; you continue its existing pull request.'); 'creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.'; the input as a quoted string, '- ''session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID'''; and forbidden '- Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session'. RS-40 :5108-5109 and PR-40 :3708: see the dependencies. No deterministic assertion evaluates these fields, so 'audit passes' needs the D23-D guard below.
```

- **item**

```text
Step 39: PR-40 :3710 becomes '- The observed merge event for the identified PR, delivered to the subscribed PR-35 session, or Nathan''s assertion that he manually merged it where no subscription existed'. Then regenerate the derived PR-35 and RS-40 consumers and required_interfaces (and states if a state is added) from the step-38 parts.
```

- **item**

```text
Step 43 YAML (55 rows): delete the two required_regex entries (SRC-001 Prompt Version, INV-003 Ecosystem release) and append three forbidden_regex entries windowed to the first 8 nonblank lines. '- value: ''\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_-]*(?:\*\*)?Prompt [Vv]ersion:''' / 'rule_id: SRC-001'; the same prefix with 'Ecosystem release:' / 'rule_id: INV-003'; the same prefix with 'Set:' / 'rule_id: SRC-001'. Scratch results: both header conventions fire; a clean header is silent; a version line in a handoff template 40 lines down is silent. Regression: insert 'Prompt Version: 091426.1' after the Prompt ID line.
```

- **item**

```text
Missing D23 guards, proposed YAML. Each still needs a clean-control run over the edited bodies before adoption, because body wording was not read here. D23-D, on the continuity-list rows from step 32's readback: forbidden '''Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session''' (CTR-001); on PR-30, PR-35 and RS-40, required '''they do not share a session''' (CTR-002). Do not forbid 'same-session' broadly: PR-35's own RECOVERY_PENDING branch is a legitimate 'same-session re-entry'. D23-E, on PR-35 and RS-40: required '''[Ss]ubscribe to the pull request''', '''do not poll''' and '''observed merge event''' (CTR-002); on PR-40, required '''observed merge event''' (CTR-002). D23-F (child): on PR-40, forbidden '''original Proceed and a suitable actual authorized implementation vehicle''' (CTR-001), the phrase the child change quotes from PR-40's body; on PR-20, required '''PR_WORK_UNIT_LINEAGE_REVIEW''' (CTR-002). The positive PR-40 to PR-20 naming is already enforced by flowmaster's PROMPT_HANDOFF_RECEIVER once the graph moves. D23-B placement, on the 53 rows: required '''ends with the `?NEXT_PROMPT_HANDOFF`? block''' (TOP-001); on QA-60, QA-80, RS-10 and RS-30, forbidden '''\bends? `ASK OK\?`''' (CTR-002), after confirming the new wording does not reuse 'end `ASK OK?`'.
```

- **item**

```text
A contradiction inside the plan that touches registry identity. The conventions edit 091426.1 bodies in place with notion-update-page, step 42 keeps the titles, and step 44 records current_version 091426.1 for all members. Yet C-VERSION says 'A member whose body changes gets a successor page at the new version', and C-HANDOFF says 'an issued version is never edited'. If EXECUTE follows C-VERSION literally, every changed row's notion_page_id, notion_url, expected_title, controlling_sources, supersedes and superseded_by would change, along with the registry header and release, audit_contracts.selected_binding and authority_sources. None of that is planned. The plan should say explicitly that C-VERSION applies from the next release on, or add the successor-row steps.
```

- **item**

```text
Cross-surface pointers, not in this surface: PR-35.json node.cross_session_route is False, and step 30 flips only adds_session. Removing the two NATHAN_MANUAL_MERGE_ASSERTION boundary rows (PR-35, RS-40) at step 38 affects flowmaster's SYMBOLIC_DESTINATIONS comment and count. epic-reengineering-interoperability.md:49 ('The sole downstream native input remains PR_INSTRUCTION_ID') is historical (GCFPE-20260909.1) and unreferenced by SKILL.md, so treat it as provenance.
```

- **item**

```text
Scratch hygiene: every probe ran under /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad with PYTHONDONTWRITEBYTECODE=1. No prompt body was fetched. Only synthetic text and the canonical §P wordings were used. The scratch skill copy and tmp directories were deleted, and nothing was written to the synced skills directory or the repository.
```


## Part 2 — critics of the amendment draft (workflow wf_d3847211-6a7)

The first run's critic was interrupted by a user interrupt and returned nothing. These three ran afterwards against the first draft of Amendment 1.

### sweep — completeness sweep (28 findings)

#### `sweep:0` — BLOCKER — A1-5 / A1-7 / step 38 (RS-40 PR-35 phase)

- **Location:** /home/user/glow-hdengine-v2/docs/graph/parts/prompts/RS-40.json:21

- **Evidence**

```text
RS-40.json merge_pending -> NATHAN_MANUAL_MERGE_ASSERTION 'recorded PR-35 phase result; historical pre-merge evidence'; global.json:39 origin_prompt 'PR-35_OR_RS-40'; A1-7 re-conditions boundary->PR-40 to 'where no subscription observed the merge'; route_sim adds MERGE_OBSERVED to PR-35 only. With RS-40 mirrored (measured): 229 edges, 91f409e8.../284, not 56e808b2.../283.
```

- **Problem**

```text
Original steps 37 and 39, which E3 keeps, put C-SUB and C-DISPATCH into RS-40's PR-35 phase, and that phase runs in the subscribed PR-35 session. But A1-5 and A1-7 give RS-40 no MERGE_OBSERVED state and no RS-40 -> PR-40 edge. The shared boundary edge (origin PR-35_OR_RS-40) now fires only 'where no subscription observed the merge'. So a subscribed RS-40 path has no lawful route to PR-40: it either dead-ends or dispatches twice. PROMPT_HANDOFF_RECEIVER only checks that graph receivers are named in the body, so nothing fails. The A1-7 diff that Nathan approves as 'the complete diff' leaves this out.
```

- **Fix**

```text
Decide RS-40 in A1-5 and A1-7 before approval. Recommended: RS-40 gains MERGE_OBSERVED, placed after MERGE_PENDING in result_states and state_route_order, and an appended RS-40 -> PR-40 edge 'merge_observed' (automatic false, COMPLETE_NEXT_PROMPT_HANDOFF). Its merge_pending condition gains 'conditional PR-40 invocation for Nathan only where no subscription observes the merge'. Add both rows to the A1-7 table, then re-simulate and pin the exact digest, row count and edge count; with illustrative wording that is 91f409e8cbfa508729298fd3f4d2b8f6/284 and 229 edges. Set E4 item 1 to that edge count. Derive RS-40 consumers and required_interfaces as [PR-30, PR-35, PR-40, RS-20]. The positive DIRECT/GRAPH_DIRECT_PR40 rule must allow exactly PR-35 and RS-40. Add an RS-40 observed-merge fixture. The alternative is to drop C-SUB and C-DISPATCH from RS-40 in steps 37 and 39 and say how an RS-40 merge reaches PR-40.
```

#### `sweep:1` — GAP — N3 / N7 (C-TOP forbidden pattern)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:326

- **Evidence**

```text
Pattern '\b(?:launch|spawn|auto-?start)\w*\b[^.\n]{0,60}\bsession\b' vs C-TOP (:80) 'It never creates, launches or schedules another session;'. Measured with re.search(MULTILINE): match 'launches or schedules another session'. Reworded 'creates, starts or schedules another session': no match; both N3 regressions still fire.
```

- **Problem**

```text
N7 adds C-TOP to all 54 bodies, and this forbidden pattern matches C-TOP itself. E4 item 8 (zero findings) therefore fails on every row, and the clean-control step sends 54 hits to Nathan mid-EXECUTE.
```

- **Fix**

```text
Reword C-TOP's last sentence to 'It never creates, starts or schedules another session; it returns control, with the handoff where there is one.' This keeps the pattern strict: no match on the new text, and both regressions still produce exactly their own finding. Require N3's clean control to cover the literal C-TOP, the C-SESSION addition, C-DISPATCH and C-REPLAN strings before adoption. Do not add a negation exemption to the pattern; that would weaken it.
```

#### `sweep:2` — GAP — N3 (amendment defect #10, D23-E guard)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:44

- **Evidence**

```text
Defect #10: 'Four rulings have no guard: D23-B placement, D23-D, D23-E and D23-F'. N3 adds D23-D and C-TOP; steps 18-19 add D23-B; child C5 adds D23-F; no step adds D23-E. validate_gcfpe_20260914.py:2443 exact_markers['PR-35'] = (REMOTE_EVIDENCE_PENDING, PR_REMOTE_ACTION_LEDGER, MERGE_PENDING).
```

- **Problem**

```text
D23-E (subscribe, do not poll, dispatch on the observed merge) still has no guard. A body that loses C-SUB or C-DISPATCH (PR-35, RS-40, PR-40) passes every check, although D23 requires a guard per ruling.
```

- **Fix**

```text
Add D23-E to N3 using preflight registry-audit:12's YAML. On PR-35 and RS-40, required_regex '[Ss]ubscribe to the pull request', 'do not poll' and 'observed merge event' (CTR-002). On PR-40, required 'observed merge event' (CTR-002). Each gets a deletion regression that yields exactly its own (rule_id, summary). Also add 'MERGE_OBSERVED' to exact_markers['PR-35'] at validate_gcfpe_20260914.py:2443, and to RS-40 if it gets the route, with a must-fail regression.
```

#### `sweep:3` — GAP — step 38 (MERGE_OBSERVED 'and its four pins')

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:37

- **Evidence**

```text
'PR-35 complete result vocabulary': 'The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`' (only at SKILL.md:57). Same closed list at change-flow/SKILL.md:305, flowmaster-validate/SKILL.md:166, behavior-cases.md:21; contract pr_development_contract.pr35_result_vocabulary.
```

- **Problem**

```text
The 'four pins' are fv-rest:21's flowmaster-validate :853/:1747/:1921 and change-flow :1008. None of them covers this required literal. Adding MERGE_OBSERVED at SKILL.md:57 fails validator :37; leaving it out means the skill declares a closed vocabulary that excludes the new result. The prose copies and the contract key are unlisted; the key is also missing from A1-2's regenerator list. Every site is an exact ordered list, but no insertion position is given.
```

- **Fix**

```text
Fix one ordered list: [MERGE_PENDING, MERGE_OBSERVED, RESCOPE_PENDING, RECOVERY_PENDING, REMOTE_EVIDENCE_PENDING, PRODUCT_OWNER_DECISION_REQUIRED], the order route_sim used. Apply it at validate_gcfpe_20260914.py:853-856 and change-flow validator :1008-1010. At the PR skill's validator :37 and SKILL.md:57, use the new six-value sentence and add the old five-value sentence to the forbidden list. Apply it too at change-flow/SKILL.md:305, flowmaster-validate/SKILL.md:166 and behavior-cases.md:21. In the graph, update PR-35.json node result_states and state_vocabularies.PR-35_RESULT. In the contract, update pr_development_contract.pr35_result_vocabulary and member_registry, adding both to A1-2's key list. Derive the registry PR-35 states. Injecting each old list must fail.
```

#### `sweep:4` — GAP — step 35 (glow-hde-pr-development validator literals)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:44

- **Evidence**

```text
:44 'merge-ready ownership': 'Continue in the same dedicated PR session until all applicable predicates are true' (only at SKILL.md:100); :63 'same PR continuation': 'same dedicated PR session, workspace/worktree, branch, open PR' (only at SKILL.md:141). Step 35 edits :100 and :141 but names only validator :32/:38/:55 (replace) and :31/:33/:34 (keep).
```

- **Problem**

```text
Rewording :100 and :141 to name each phase's own session, as the pr-relay notes ask, fails these two required literals. Keeping them keeps the shared-session wording the step exists to remove. No preflight row covers either.
```

- **Fix**

```text
Add to step 35: replace :44 with 'Continue in this phase's own dedicated session until all applicable predicates are true', and :63 with 'the recorded phase's own dedicated session, workspace/worktree, branch, open PR'. Add both old literals to the forbidden list after confirming they occur nowhere else; injecting the old text must fail. Step 35 and child C6 both edit :10, :27 and :158. Compute one combined replacement per line, keeping the validator :31 and :64 literals.
```

#### `sweep:5` — GAP — A1-6 / step 47 / N4 (skill package set)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/tw-flowmaster/SKILL.md:319

- **Evidence**

```text
tw-flowmaster:319-321 are byte-identical to session-relay:283-285: 'exactly one complete same-session PR-35 handoff ... PR-35 supplies the actual populated PR-40 handoff conditional on merge ... The Product Owner's PR-40 invocation supplies merge approval'; :304 = relay:259; :315 ~ relay:279; :311 puts 'PR/commit references' in handoff metadata. No preflight row, amendment or child step names tw-flowmaster.
```

- **Problem**

```text
Steps 14, 19, 35 and 40 and N4 converge and guard only the relay's copy. After cut-over the installed tw-flowmaster still teaches same-session PR-35, PR-40 entered on Nathan's assertion, versionless prompt locators (against C-HANDOFF) and commit references in handoffs. Its GCFPE binding says 'Preserve this boundary through coordination, relays, documentation and remediation'. No check fails.
```

- **Fix**

```text
Add tw-flowmaster as a sixth package. Replace :319 and :321 with the relay's new :283 and :285 bytes, and :304 and :315 with the relay's step-14/19 text. Drop 'PR/commit references' from :311's handoff metadata and keep them in the usage record. Bump TW_FLOWMASTER_SPECIALIZATION_REVISION 1.1.6 -> 1.2.0 at SKILL.md:9 and validate_flowmaster.py:128. Add N4's two phrases and 'The Product Owner's PR-40 invocation supplies merge approval' to CONTRACT_FORBIDDEN['tw-flowmaster'], each with a must-fail regression. Include it in the E5 (D24) review and the A1-4 install. If it stays out, record it under D23 as a known contradiction with a spawned Modification.
```

#### `sweep:6` — GAP — Rulings received during PLAN (C-TOP into change-flow) / step 35

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/change-flow/SKILL.md:158

- **Evidence**

```text
change-flow:158 '3. a fresh spawned session in its own worktree only when no existing authoritative session can do the work.'; :140 'before spawning new work'; :145 'Verify a newly spawned session'. The Flowmaster core is byte-identical in 5 skills (sha prefix 4e565e40...); validate_flowmaster fails 'embedded Primary core is not byte-identical'; flowmaster-primary pinned 0665507....
```

- **Problem**

```text
The D23 clarification says: 'No session creates, launches or schedules another session, by any tool or mechanism.' Step 35 puts the top-level sentence into change-flow's specialization. But change-flow orchestrates main-ecosystem stages, and its core, which cannot be edited without moving Primary, still permits spawning a session. The file ends up with both rules and no stated precedence.
```

- **Fix**

```text
Add a GCFPE override to change-flow's specialization block, outside the core: 'For every GCFPE main-ecosystem stage, Primary's control-hierarchy option 3 does not apply: Change Flow never creates, spawns, launches or schedules a session; when no existing authoritative session can do the work it returns the paste-ready NEXT_PROMPT_HANDOFF and stops for Nathan to create the session.' Add it to CONTRACT_REQUIRED['change-flow'] in validate_flowmaster.py (CONTRACT_FORBIDDEN is never applied to change-flow), with a deletion regression.
```

#### `sweep:7` — GAP — A1-1 (successor oracle and runtime map re-pointing) / step 34

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:24

- **Evidence**

```text
ORACLE_RELATIVE and CHANGE_RUNTIME_MAP_RELATIVE (:24-26) are fixed filenames; OPTIONAL_REFERENCES['change-flow'] (:360-364) = {runtime map, gcfpe-current alias}, and :1115-1126 fails both an unapproved link and an unlinked listed file. Same paths at validate_gcfpe_20260914.py:2610, validate_gcfpe_current.py:659, run_change_flow_fixtures.py:15, change-flow/SKILL.md:557.
```

- **Problem**

```text
A1-1 says the live validators are re-pointed to the successors but lists no path sites, and the preflight pin list covers hashes only. Linking the successor map, or the 091426.1 contract under A1-6, from change-flow/SKILL.md fails validate_flowmaster until OPTIONAL_REFERENCES changes. run_change_flow_fixtures keeps reading the historical oracle, so GCF-17.LINEAGE -> GCF-14 is never tested. Once EXPECTED_ORACLE_SHA256 (:37) moves, nothing pins the historical oracle file's bytes.
```

- **Fix**

```text
Add a path table to A1-1 with the successor filenames. Re-point :24-26, REQUIRED_REFERENCES[flowmaster-validate] (:355; add the successor oracle and source matrix), OPTIONAL_REFERENCES[change-flow] (:360-364; add the successor map and, under A1-6, the linked 091426.1 contract), validate_gcfpe_20260914.py:2610, validate_gcfpe_current.py:659, run_change_flow_fixtures.py:15, the change-flow/SKILL.md:557 link and flowmaster-validate/SKILL.md:244. Add HISTORICAL_ORACLE_SHA256 = 52807e58... for the old oracle file, with a regression that flips one byte and must fail. Add fv-rest:27's R1 fixture (GCF-17.LINEAGE -> GCF-14, positive) to fixtures/change-flow/scenarios.json under C8.
```

#### `sweep:8` — GAP — E4 item 4; preflight fv-main:20

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:252

- **Evidence**

```text
E4 item 4 runs only validate_strength_middleware, validate_epic_alpha, validate_epic_reengineering and their runners. fv-main:20 says to re-pin 5574666e at 'validate_integrated_readiness.py:8/:151, validate_pre_guide_correction.py:9/:67, validate_strength_middleware.py:14'. Measured on scratch copies today: all 12 historical-layer commands exit 0.
```

- **Problem**

```text
Under A1-1 the historical map keeps 5574666e. Following fv-main:20 would re-pin historical-layer validators, falsifying history. Four of those validators and three runners are also outside E4, so breaking them would go unseen. 'Historical records excluded' does not clearly cover validator pins.
```

- **Fix**

```text
Say in A1-1 and step 34 that historical-layer pins are never edited: validate_strength_middleware.py:14, validate_integrated_readiness.py:8/:150, validate_pre_guide_correction.py:9/:66, validate_final_scan.py:68, final-cycle-scan-extension.json:3 and the correction-layer JSONs. Mark fv-main:20 SUPERSEDED for those sites. Extend E4 item 4 to all 12 commands, each exiting 0: the three named validators and their runners, plus validate_integrated_readiness.py, validate_pre_guide_correction.py, validate_final_scan.py, validate_alpha_feedback.py, run_integrated_readiness_fixtures.py --change-directory, run_final_scan_fixtures.py --change-directory and run_alpha_feedback_fixtures.py.
```

#### `sweep:9` — GAP — Step changes preamble (disposition rule)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:274

- **Evidence**

```text
'EXECUTE records a disposition in §E for every WOULD_FAIL and UNCERTAIN row'. WOULD_PASS rows needing none include fv-main:6, :7, :28 (fixtures green while asserting reversed rules), :31 (versioned_sibling_successors), :32 (receiver_compatibility), pr-relay-graph:18 (relay :624), registry-audit:20.
```

- **Problem**

```text
WOULD_PASS is exactly the class that no check will ever surface: a stale expectation that stays green (AF-001). Exempting it lets reversed-rule fixtures and contract keys survive silently, although E2 says 'Edits per the preflight rows'.
```

- **Fix**

```text
Replace the sentence with: 'EXECUTE records a disposition in §E for every preflight row, WOULD_PASS included: fixed by step N (with the regression that proves it), superseded by amendment section X, kept deliberately with the reason, or out of scope with a spawned Modification.'
```

#### `sweep:10` — GAP — A1-2 (explicit mapping values) / A1-5 (event_2, pr35_observed_merge_edge)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:3166

- **Evidence**

```text
receiver_compatibility.PR-35 same_session_workspace_worktree_branch_open_pr_original_proceed:true; PR-40 nathan_manual_merge_assertion_required:true; route_graph_semantics same_session_phase_continuation/pr40_entry (:11508-11512); ordinary_pr_work_unit [...,'PR-35','NATHAN_MANUAL_MERGE_ASSERTION','PR-40']; event_2 fact/time; rescope preserved_lineage 'PR_DEVELOPMENT_SESSION'.
```

- **Problem**

```text
A1-2 names these keys but gives no target values, and most of them are read by no check (fv-main:32), so the regenerator's author would choose them unreviewed. A1-5 gives event_2 as a single string, but the validator checks event_2.actor and .fact separately. It also does not say where pr35_observed_merge_edge goes; a new top-level key trips EXPECTED_CONTRACT_TOP_LEVEL_KEYS in both validators (flowmaster :339, change-flow :208).
```

- **Fix**

```text
Add a value table to A1-2 for the §10 reviewers. receiver_compatibility.PR-35: dedicated_top_level_pr35_session true and same_workspace_worktree_branch_open_pr_original_proceed true. PR-40: entry_fact 'OBSERVED_MERGE_EVENT_OR_NATHAN_ASSERTION_WHERE_NO_SUBSCRIPTION', keeping the three verification flags. route_graph_semantics per C-SESSION and C-DISPATCH. ordinary_pr_work_unit [PR-10, PR-20, NATHAN_PROCEED, PR-30, PR-35, PR-40] plus pr35_no_subscription_fallback [PR-35, NATHAN_MANUAL_MERGE_ASSERTION, PR-40]. event_2: actor unchanged, fact 'product_owner_manual_merge_observed_or_asserted', time 'observed by the subscribed PR-35 session, else asserted at the later PR-40 invocation'. pr35_observed_merge_edge inside post_merge_three_event_contract, in graph and contract. preserved_lineage 'PR_PHASE_SESSION'. versioned_sibling_successors kept, with the reason. Each new value gets a check and a regression that re-injects today's value.
```

#### `sweep:11` — GAP — preflight fv-main:2, fv-main:13, fv-rest:1, fv-rest:2, pr-relay-graph:27, registry-audit:10

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/preflight_render.md:21

- **Evidence**

```text
fv-main:2 adds fixture 'reject-cross-session-route=1', but step 29-31 sets cross_session_route 1. fv-main:13: 'direct_PR35_to_PR40_automatic_edge becomes True'; registry:10 '(... becomes true)'; pr-relay:27 'dispatch is a paste or a session launch'. fv-rest:1/:2 re-pin the current-alias contract at :805-806 and edit the historical runtime map in place.
```

- **Problem**

```text
E2 says 'Edits per the preflight rows' and step 34 says 'the pin sites are the complete list in preflight'. These six rows' required steps now contradict A1-1, A1-5 and the D23 clarification. One would add a fixture that rejects the approved state. Three would record an automatic PR-35 -> PR-40 edge, against the rule that nothing is created automatically. Two would rewrite frozen history.
```

- **Fix**

```text
Mark these rows SUPERSEDED in the amendment itself, before E2. fv-main:2: the negative fixture becomes 'reject cross_session_route = 0'. fv-main:13, registry-audit:10 and pr-relay-graph:27: direct_PR35_to_PR40_automatic_edge stays false (A1-5). fv-rest:1 and :2: the alias contract and the historical map keep their bytes; only the successor map is pinned (A1-1, A1-6).
```

#### `sweep:12` — GAP — step 35 / step 40 / child C7 (change-flow must-fail regressions)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:1340

- **Evidence**

```text
'() if name == "change-flow" else CONTRACT_FORBIDDEN.get(name, ())': CONTRACT_FORBIDDEN is never applied to change-flow. change-flow's own validator (:1020-1031) only checks require(text in skill). Retired phrases at change-flow :301 'one dedicated PR-development session', :307 'same-session PR-30 → PR-35 phase continuation', :331 and :353 (the merge assertion).
```

- **Problem**

```text
The PO rule requires an injected must-fail regression for every reversed literal. For change-flow there is no mechanism that fails when a retired sentence is put back, so its C-SESSION, C-DISPATCH and C-PROCEED reversals cannot be proven.
```

- **Fix**

```text
Add the retired change-flow phrases to the successor oracle's prohibited_active_patterns, as new FMV-GCF-OBSOLETE-0xx rules checked on active text outside the prohibitions block. Alternatively, add a forbidden-phrase loop to change-flow/scripts/validate_gcfpe_20260914.py. Each phrase gets one regression that must yield exactly that finding.
```

#### `sweep:13` — GAP — step 40 / step 35 (change-flow line lists)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/change-flow/SKILL.md:353

- **Evidence**

```text
:353 'A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred'; :453 'GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35'. Step 40 names change-flow :331 and :366; child C7 names :455. Only fv-rest:19 (UNCERTAIN, 'or record them as intentionally untouched') covers these.
```

- **Problem**

```text
change-flow's authority order ranks the skill above the stage prompt, so these stale lines would override the new bodies at runtime and contradict the successor GCF-17 row. The only preflight row covering them still offers 'intentionally untouched' as an option.
```

- **Fix**

```text
Add :353 to step 40, replacing the assertion sentence with: 'Where the subscribed PR-35 session observed the merge, that event is the fact PR-40 is entered on; where no subscription existed, Nathan's later PR-40 invocation asserts the manual merge; neither is a merge approval or instruction.' Add :453 to step 35, mirroring the successor GCF-17 name, actor and session, and add :450-:451 if that prose changes. Do not allow 'intentionally untouched' for lines that restate a reversed rule.
```

#### `sweep:14` — GAP — A1-5 (fallback trigger) / C-SUB

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:184

- **Evidence**

```text
A1-5: 'The fallback block is pasted only when PR-35's result says no subscription was made'. subscribe_pr_activity tool contract: 'If a Claude agent (PR Steward) is already watching the PR, the call succeeds but this session will NOT receive events — the tool result says so.'
```

- **Problem**

```text
A subscription call can succeed without delivering events to the PR-35 session. PR-35 then records 'subscribed', the fallback block is withheld, no merge event ever arrives, and PR-40 is never entered.
```

- **Fix**

```text
Tie the fallback in A1-5 and C-SUB to delivery rather than to the call: 'record the subscription as active only when the tool result confirms this session receives the PR's events; otherwise the result states that no subscription delivers events and includes the fallback PR-40 block.' Add a fixture: subscription accepted but not delivering -> fallback block present.
```

#### `sweep:15` — GAP — Rulings received during PLAN ('The rule is carried into') / child C4-C5

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/gcfpe.decision-record.md:1315

- **Evidence**

```text
D23 clarification rule 1 names 'PR-35 in its own session (D23-D), PR-40 after the merge (D23-E), and PR-20 for a re-plan (D23-F)'; its Guard (:1345-1350) lists 'the graph role and the registry role for each affected prompt'. The amendment (:87-91) carries the rule only into PR-35's receiving_role and session_role.
```

- **Problem**

```text
The decision record promises role-level guards for PR-40 and PR-20, and neither the amendment nor the child plan delivers them.
```

- **Fix**

```text
Either append C-TOP's top-level clause to the PR-40 and PR-20 graph receiving_role and registry session_role as identical strings (contract member_registry regenerated; GRAPH_NODE_CONTRACT parity plus a regression), or add a D23 successor note saying the body-level C-TOP and the N3 guards carry the rule for PR-40 and PR-20 and their roles stay unchanged.
```

#### `sweep:16` — GAP — child C6 (re-plan vs recover-before-create)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/SKILL.md:41

- **Evidence**

```text
Recovery step 3: 'Match prior work using evidence such as repository origin, work-unit identity, branch, commit ancestry, artifact lineage, and PR head'; step 4: 'Reuse the verified existing workspace and completed valid work'; :77 'Reuse an existing PR for the same branch/work unit instead of creating another.' C6 edits only :77, :82 and :158.
```

- **Problem**

```text
A re-plan keeps the same WORK_UNIT_ID. The second-cycle PR-30 (and PR-20) recovery will therefore match the merged first-cycle branch and PR as 'prior work' and try to resume or reuse them, as the preflight live-window note warns. Nothing limits recovery to the current plan cycle.
```

- **Fix**

```text
Add to C6: recovery step 3 matches on work-unit identity and the current PR_IMPLEMENTATION_PLAN identity, and 'a PR merged under an earlier plan cycle is landed history; never resume, reuse or push to it.' Mirror this in amthor SKILL.md:43 under C10. Add a case under '## PR-40 rejection re-plan': merged prior PR present -> a new branch and PR are created.
```

#### `sweep:17` — MINOR — step 41

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/prompt-body-content-policy.md:88

- **Evidence**

```text
'`prompt_identity_header_valid` now: - **requires** identity — title, `Prompt ID:`, `Prompt version:`, `Ecosystem release:`, exactly one `Notion URL:` line...'. Step 41 edits only :33-34.
```

- **Problem**

```text
Once E2 inverts the header check, the policy's Enforcement section misstates what the validator requires.
```

- **Fix**

```text
Extend step 41 to :88: 'requires identity — title, `Prompt ID:`, exactly one `Notion URL:` line whose page identity matches the registry binding; rejects `Prompt version:`, `Set:` and `Ecosystem release:` in the header window as `PROMPT_BODY_RELEASE_HEADER` (D23-G)'.
```

#### `sweep:18` — MINOR — N1 / N2

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/authoritative-surfaces.md:29

- **Evidence**

```text
':29 Graph proof token | 55 nodes · 227 edges · 55 state_routes · 569,902 bytes · sha256 1d0b7258…' and 'A session that builds and gets the same token has proved agreement'. Build today: 569835 B / 90021eb7; after E1: 228 edges, 572120 B, 3ce18159 (simulated). ecosystem-change-management.md:176 'the release carries two header conventions'.
```

- **Problem**

```text
The orientation page's token is already stale, and E1 changes the edge count, so a session orienting from it will read the difference as drift. The CHK-002 example becomes false once step 42 lands.
```

- **Fix**

```text
In N1, restate authoritative-surfaces.md:29 and :45-46, and ecosystem-change-management.md:143, with the E4 item-1 token after merge, or label them dated. Change ecosystem-change-management.md:176 to 'carried, until D23-G removed them,'.
```

#### `sweep:19` — MINOR — step 37

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/SKILL.md:121

- **Evidence**

```text
Original step 37 targets 'glow-hde-pr-development:112, :121'; the amendment re-anchors only :112. :121 reads '- poll only when a pending remote result can change the next action;'.
```

- **Problem**

```text
:121 is now unassigned. Under C-SUB, polling should apply only where no subscription delivers the result.
```

- **Fix**

```text
In step 37, change :121 to '- where no subscription delivers it, poll only when a pending remote result can change the next action;', or record it as kept deliberately.
```

#### `sweep:20` — MINOR — step 35

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/SKILL.md:393

- **Evidence**

```text
'A verified PR-30_POSTPUBLICATION or PR-35 approval uses RS-40 and resumes the recorded phase in the same session/worktree/branch/open PR under the original Proceed.' No preflight row cites it.
```

- **Problem**

```text
This shared-session restatement is not in any row; amthor :47's equivalent is converged to 'the recorded phase's own session'.
```

- **Fix**

```text
Add to step 35: 'resumes the recorded phase in that phase's own session, worktree, branch and open PR under the original Proceed'.
```

#### `sweep:21` — MINOR — child C9 (receiver_compatibility.PR-30)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:1

- **Evidence**

```text
receiver_compatibility.PR-30 = {accepted_contexts: [PROCEEDED_PREPUBLICATION, OPEN_PR_POSTPUBLICATION_RECOVERY], accepted_final_replay: false, overlay_approvals: [...]}. It has no PR-40 return context to drop.
```

- **Problem**

```text
'receiver_compatibility.PR-30 drops the PR-40 return' changes nothing, because fv-main:32's premise was wrong. C9's verification therefore proves nothing.
```

- **Fix**

```text
Replace it with a negative assertion: no receiver_compatibility entry except PR-20 accepts a PR_WORK_UNIT_LINEAGE_REVIEW REJECT. Add a regression that gives it to PR-30 and must fail.
```

#### `sweep:22` — MINOR — child C7 (:313/:323 anchors)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/change-flow/SKILL.md:313

- **Evidence**

```text
:313 'The PR session never approves its own rescope, rewrites an approved base, restarts IA-30/IA-40, requests a second Proceed, reruns accepted-final work, or invokes PR-50.' :323 'No decision ... creates another Proceed, reruns accepted-final work, or routes automatically to PR-50.'
```

- **Problem**

```text
These are rescope sentences, and the child keeps their rule: C-PROCEED says a rescope return never creates a second Proceed. Replacing them with C-PROCEED would delete the accepted-final and PR-50 prohibitions, the same defect class as amendment #12.
```

- **Fix**

```text
C7: keep :313 and :323 verbatim, append C-PROCEED as its own sentence after :301, and change :455 per the successor row.
```

#### `sweep:23` — MINOR — N1 (registry body identities)

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md:3747

- **Evidence**

```text
PR-40 source_snapshot: path candidate/prompts/PR-40.md, sha256 9350d497..., bytes 54974, completeness COMPLETE, extracted_as_of 2026-09-17. The same block is on all 55 rows.
```

- **Problem**

```text
N1 marks only evidence_contract as a stale pre-D23 body identity. source_snapshot is a second per-row body identity that stops describing the bodies just the same.
```

- **Fix**

```text
Extend N1 to cover source_snapshot (sha256, bytes, completeness) on all 55 rows.
```

#### `sweep:24` — MINOR — A1-1 / child C3 (GCF-14 input)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json:1

- **Evidence**

```text
GCF-14 consumes [pr_instruction, approved_implementation_plan_lineage, current_repository]; GCF-17.LINEAGE produces [pr_work_unit_lineage_review]; child C5 makes PR_WORK_UNIT_LINEAGE_REVIEW a PR-20 input. graph_findings never compares next with consumes.
```

- **Problem**

```text
The successor row routes GCF-17.LINEAGE -> GCF-14, but GCF-14 does not consume the review that carries the defect. R1 and the registry disagree about the re-plan's input, and no check notices.
```

- **Fix**

```text
Either add pr_work_unit_lineage_review to GCF-14.consumes in the successor oracle (a third changed row: update A1-1's 'Two rows change' and the successor matrix), or record why the R1 row leaves it out.
```

#### `sweep:25` — MINOR — A1-6 / child C10 (amthor invariants)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/amthor-workspace-governance-audit/SKILL.md:36

- **Evidence**

```text
The 'Audit these Alpha-feedback invariants' list, which the semantic maker/reader review enforces, has no top-level-only or no-automated-session invariant. A1-6 converges only C-HANDOFF, C-SESSION and C-DISPATCH, plus C-PROCEED via C10.
```

- **Problem**

```text
The semantic audit will never check the D23 clarification.
```

- **Fix**

```text
Add a bullet: 'Every main-ecosystem prompt (all but GCFPE-MGMT-10) runs as its own top-level session Nathan creates; none runs as a subagent, forked or workflow agent; none creates, launches or schedules a session; workers within a task are allowed.'
```

#### `sweep:26` — MINOR — E2 / preflight fv-main:24 (bundled graph copies)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/SKILL.md:59

- **Evidence**

```text
'Any existing Drive or repository copy of an assembled graph is historical. Do not update it, do not mint a replacement, and do not treat it as authoritative.' E2 writes new bundled graph copies into two skills. fv-main:24 asked to 'resolve a conflict'; the amendment does not.
```

- **Problem**

```text
The installed graph-contract skill tells a session not to mint the replacement copies that E2 requires.
```

- **Fix**

```text
State in E2, or in a D23 successor note, that bundled skill references are validator fixtures built from the parts, not Drive or repository copies, so the rule does not apply to them.
```

#### `sweep:27` — MINOR — A1-3 (per-member revision date)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:154

- **Evidence**

```text
A1-3: 'the register records each changed member's revision date (2026-09-23, this Modification)'. prompt-validation-procedure.md:49: 'Every recorded identity has a consumer that fails on mismatch... Before recording one, name the check that reads it.'
```

- **Problem**

```text
The revision date is the only thing that distinguishes the edited 091426.1 bodies, and nothing reads it, so a missed or wrong date passes.
```

- **Fix**

```text
Name its consumer (for example, the E6 re-scan compares the register's changed-member set with the E3 edit set and fails on a difference), or label the date informational rather than an identity.
```

### coverage — coverage audit (28 findings)

#### `coverage:0` — BLOCKER — N3 (C-TOP session-creation guard) with N7; D23 clarification guard

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:80

- **Evidence**

```text
C-TOP: "It never creates, launches or schedules another session". N3 forbidden (CTR-001), at :326: `\b(?:launch|spawn|auto-?start)\w*\b[^.\n]{0,60}\bsession\b`. Measured on a copy (/tmp/claude-0/critic/n3.py): re.search(F2, C-TOP) matches 'launches or schedules another session'.
```

- **Problem**

```text
The canonical sentence N7 places in all 54 main-ecosystem bodies trips its own forbidden guard. E4 item 8 ('zero findings on every row') therefore cannot pass. The clean control would only rediscover this; it is certain now, so the guard as written cannot be adopted.
```

- **Fix**

```text
Replace the pattern with `\b(?:launch|spawn|auto-?start)(?:e?s|ed|ing)?\s+(?:a|an|the|another|new|its|their)\b[^.\n]{0,40}\bsession\b` (CTR-001). Measured: it is silent on C-TOP, C-SESSION, C-DISPATCH and C-REPLAN. It fires on 'launch a new session for PR-40', 'launches another session', 'spawn the PR-35 session' and 'auto-start a session'. State explicitly (AF-001) that it is narrower: a verb separated from its object by a conjunction is no longer caught. The clean control still runs before adoption.
```

#### `coverage:1` — BLOCKER — registry-audit:12 (D23-E guard), N3

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:44

- **Evidence**

```text
Defect table row 10: "Four rulings have no guard: D23-B placement, D23-D, D23-E and D23-F". N3 (:317-335) adds guards only for D23-D and C-TOP; steps 18-19 cover D23-B placement; C5 covers D23-F. No subscribe, do-not-poll or observed-merge assertion appears anywhere. decision-record:1283: "Until those land, D23 is ruled but not applied."
```

- **Problem**

```text
D23-E is still unguarded, although the amendment names that as a defect. Without a guard, the step 37-40 edits have only a vacuous 'audit passes', and the withdrawn launch option could return to a body undetected.
```

- **Fix**

```text
Add D23-E to N3. On PR-35 (and RS-40, per the RS-40 ruling), require `[Ss]ubscribe to the pull request`, `do not poll` and `observed merge event` (CTR-002). On PR-40, require `observed merge event` (CTR-002). On PR-35 and RS-40, forbid `launched as a new session` (CTR-001). Add regressions (delete C-SUB, delete C-DISPATCH, inject the old launch clause), each yielding exactly its own finding. Measured: the three required patterns match the amendment's C-SUB and C-DISPATCH as written.
```

#### `coverage:2` — GAP — registry-audit:10, pr-relay-graph:27 (also fv-main:11, fv-main:12, fv-main:33); §P step 39, A1-5, A1-7, A1-2 registry deriver

- **Location:** /home/user/glow-hdengine-v2/docs/graph/parts/prompts/RS-40.json:21

- **Evidence**

```text
RS-40 has its own merge_pending branch to NATHAN_MANUAL_MERGE_ASSERTION: condition 'recorded PR-35 phase result; historical pre-merge evidence', next_prompt_handoff_count 1. §P step 39 (not amended): "Insert C-DISPATCH in PR-35 and RS-40". A1-5 and A1-7 add MERGE_OBSERVED and the PR-40 edge for PR-35 only. The deriver rewrites PR-35 and PR-40 only.
```

- **Problem**

```text
The RS-40 body would carry C-DISPATCH ('return MERGE_OBSERVED with the paste-ready PR-40 handoff') while RS-40 has no MERGE_OBSERVED state and no edge to PR-40. Its merge_pending condition also lacks the no-subscription qualifier that PR-35's gains. That is body-graph drift under D13, and the scope of the D23-E guard is undefined.
```

- **Fix**

```text
Rule RS-40 explicitly. Either (a) C-DISPATCH goes to PR-35 only, RS-40 keeps replaying the recorded MERGE_PENDING, and RS-40's merge_pending condition gets the same fallback qualifier as PR-35's (add that row to A1-7 and re-simulate the digest); or (b) RS-40 gains MERGE_OBSERVED and an RS-40 to PR-40 edge, the registry deriver covers RS-40, and A1-7 is re-simulated. Amend step 39 to match.
```

#### `coverage:3` — GAP — A1-5, C-DISPATCH, A1-7 (merge rows), step 39

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:185

- **Evidence**

```text
A1-5: "fallback block is pasted only when PR-35's result says no subscription was made". A1-7: "where no subscription observes the merge" and "where no subscription observed the merge". Step 39: "where no subscription existed". C-DISPATCH (:71-76): "The observed merge event replaces his merge assertion as the fact PR-40 is entered on", with no fallback clause.
```

- **Problem**

```text
The amendment uses three different fallback predicates, and the canonical C-DISPATCH omits the fallback that A1-5 keeps. Suppose a subscription was made but never delivers, for example because the PR-35 session ended before Nathan merged (a subscription lasts only as long as its session). Then A1-5 forbids the fallback and nothing starts PR-40. Preventing a double dispatch rests on Nathan reading the result, with no guard.
```

- **Fix**

```text
Use one predicate everywhere, e.g. 'where no MERGE_OBSERVED result was returned for this merge'. Add that fallback sentence to C-DISPATCH itself, and carry it into the A1-7 conditions (re-simulate), step 39's registry input, event_2 and the glow-hde-pr-development :164 rewrite. Add a fixture: fallback used after a subscription that did not deliver is accepted.
```

#### `coverage:4` — GAP — Amendment precedence clause vs §P PART-11 ruling row and §P C-DISPATCH (session-launch option)

- **Location:** /home/user/glow-hdengine-v2/docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md:599

- **Evidence**

```text
§P:532: "Dispatch is a paste, or a session launch where the surface provides one". §P:599 C-DISPATCH: "paste-ready, or launched as a new session where the surface provides one". amendment1.md:9: "The original §P above is left as written. Where this amendment changes a step, the amendment governs." decision-record:1213: the wording applied is "the canonical wording in that Modification's §P".
```

- **Problem**

```text
The rulings table and the canonical wording are not steps. By the amendment's own precedence clause, the launch-option wording that D23 cites as authoritative is therefore not superseded. Only the decision-record clarification withdraws it.
```

- **Fix**

```text
Widen the clause: "Where this amendment changes a step, a ruling or a canonical wording, the amendment governs. The §P PART-11 ruling row ('or a session launch where the surface provides one') and §P C-DISPATCH are superseded by the C-DISPATCH above."
```

#### `coverage:5` — GAP — N3 D23-D guard and C-TOP required guard (with E4 item 9)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:319

- **Evidence**

```text
Both guards use `never\s+as\s+a\s+subagent` (:319, :322). Measured on a copy, with C-SESSION's new sentence and C-TOP in one body: deleting the C-SESSION sentence still matches (True), and deleting C-TOP still matches (True).
```

- **Problem**

```text
On PR-30, PR-35 and RS-40, neither required-guard regression can fail ('deleting that sentence must fail' cannot be met). With the same rule_id and summary, E4 item 9's 'exactly its own finding' also cannot tell the two guards apart.
```

- **Fix**

```text
D23-D: require `never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30`. C-TOP: require `never\s+as\s+a\s+subagent\s+of\s+another\s+session`. Measured: each fails only when its own sentence is deleted. Run both regressions on PR-35.
```

#### `coverage:6` — GAP — D23 clarification guard: the graph role and registry role surfaces (steps 29-31, 33)

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/gcfpe.decision-record.md:1349

- **Evidence**

```text
D23 clarification: the rule is carried into "the graph role and the registry role for each affected prompt". "Each surface gets a guard with an injected must-fail regression (D14)." The amendment puts the top-level sentence into PR-35's receiving_role and session_role. The only checks on them are GRAPH_NODE_CONTRACT parity and none on session_role (registry-audit:7).
```

- **Problem**

```text
Deleting the never-a-subagent clause from the role in the graph, contract and registry together passes every check, because the regenerator keeps parity. The D23 guard requirement is unmet for these two surfaces.
```

- **Fix**

```text
Add a flowmaster-validate literal requiring member_registry['PR-35'].receiving_role to contain 'never a subagent of another session'. Add an E4 item-8 assertion that the registry PR-35 session_role equals the graph receiving_role and contains that phrase. Give each a must-fail regression.
```

#### `coverage:7` — GAP — E2 'Edits per the preflight rows' and §E disposition (conflicting rows: fv-main:2, fv-main:9, fv-main:13, fv-main:20, fv-main:22, fv-rest:1, fv-rest:20, pr-relay-graph:27, pr-relay-graph:30, registry-audit:10)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:237

- **Evidence**

```text
fv-main:2 wants cross_session_route:0 and a reject fixture, but step 29-31 sets 1. fv-main:9 gives 281/282 rows, but A1-7 gives 283. fv-main:13, pr-relay-graph:27 and registry-audit:10 have the automatic edge becoming true; A1-5 keeps it false. fv-rest:20 rewrites HANDOFF-POS-02 despite the kept fallback. fv-main:20 re-pins validate_strength_middleware:14, against E4 item 4. fv-rest:1, fv-main:22 and pr-relay-graph:30 name GCF-15, 16 and 14.
```

- **Problem**

```text
The precedence clause orders §P against the amendment, not preflight rows against the amendment. E2 imports every row, including ones that contradict the amendment's own rulings.
```

- **Fix**

```text
Add: "Where a preflight row's required step conflicts with a ruling or step of this amendment, the amendment governs." List the superseded rows with their governing ruling, and have §E dispositions cite it.
```

#### `coverage:8` — GAP — §E disposition rule (WOULD_PASS rows: fv-main:19, fv-main:28, fv-main:31, fv-main:32, fv-rest:3, fv-rest:23, pr-relay-graph:2, pr-relay-graph:15, pr-relay-graph:17, pr-relay-graph:18, pr-relay-graph:19)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:275

- **Evidence**

```text
"EXECUTE records a disposition in §E for every WOULD_FAIL and UNCERTAIN row". 29 of the 121 rows are WOULD_PASS, and every one carries a required plan step. Several describe checks that stay green while certifying reversed rules (e.g. fv-main:28: HANDOFF-POS-02 'Stays green while asserting the reversed manual-assertion trigger').
```

- **Problem**

```text
As worded, the rule never requires a disposition for the stale-green rows, which are exactly the ones that will not flag themselves (AF-001).
```

- **Fix**

```text
Reword: "for every row whose required plan step is non-empty, whatever its effect".
```

#### `coverage:9` — GAP — fv-main:20, fv-rest:1, fv-rest:8 (and fv-main:21); A1-1 successor oracle and runtime map

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:24

- **Evidence**

```text
validate_flowmaster.py:24-26 hard-code the oracle and runtime-map paths. :355 REQUIRED_SCRIPTS lists the oracle path. :360-364 OPTIONAL_REFERENCES is a closed allowlist ('unapproved reference-file dependency'). run_change_flow_fixtures.py:15, validate_gcfpe_20260914.py:2610, validate_gcfpe_current.py:659, validate_integrated_readiness.py:150, validate_pre_guide_correction.py:66 and validate_final_scan.py:68 open the files by fixed name.
```

- **Problem**

```text
A1-1 keeps the historical bytes and re-points the 'live validators', but names no successor filenames and gives no live-versus-historical split. No preflight row lists the path constants or allowlists, because the preflight assumed in-place edits. fv-main:20's site list re-pins validate_strength_middleware.py:14, which E4 item 4 requires to stay unchanged.
```

- **Fix**

```text
Name the successor files. Classify every path and hash site as live (re-point) or historical (keep), including validate_integrated_readiness, validate_pre_guide_correction, validate_final_scan and their runners, and validate_gcfpe_current.py:81 and :660. Add the successor files to REQUIRED_SCRIPTS and OPTIONAL_REFERENCES as explicit allowlist changes, each with a must-fail regression.
```

#### `coverage:10` — GAP — fv-rest:6 (A1-1 digest provenance and authority block)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:534

- **Evidence**

```text
The oracle authority block holds r1_contract_matrix_sha256 faa7fb7d…, r1_frozen_snapshot_sha256 5a6d89ed… and r1_verdict R1_CANONICAL_TRUTH_LOCK_PASS. FMV-ORACLE-006 requires exactly 12 row fields. A1-1 says the changed rows' source_row_sha256 becomes "the digest of that row in a successor source matrix … The authority block records both matrices."
```

- **Problem**

```text
Three things are undefined. (1) The byte serialization of 'that row', so the digest is not reproducible. (2) How the validator knows which rows bind to the successor matrix without a 13th row field. (3) Whether the successor keeps the original R1_CANONICAL_TRUTH_LOCK_PASS verdict and frozen snapshot, which attest only the original rows.
```

- **Fix**

```text
Define the successor matrix row format and its serialization. Bind the rows through an authority-level list (e.g. successor_rows: [GCF-17, GCF-17.LINEAGE]) with its own digest. Scope r1_verdict and the frozen snapshot to the original matrix explicitly. Add regressions: a successor row edited without its matrix row must fail, and so must a third row added to the list.
```

#### `coverage:11` — GAP — fv-rest:3 (and fv-main:19): the replacement expectation for protected_r1_46_rows_unchanged

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:127

- **Evidence**

```text
"protected_r1_46_rows_unchanged becomes false, while r1_rows stays 46 and pr35_adds_r1_row stays false … Each gets an injected regression proving the old claim now fails".
```

- **Problem**

```text
A false flag guards nothing that is kept. The kept invariant is that the other 44 rows are unchanged. Once the whole-file oracle pin is re-stamped, only their external digests remain, which no in-skill check can recompute. That breaches the PO rule that a reversed check gets a replacement expectation guarding what is kept.
```

- **Fix**

```text
Add a check that every successor row other than GCF-17 and GCF-17.LINEAGE equals the kept historical oracle's row in all 12 fields. Add a must-fail regression that mutates one unchanged row (e.g. GCF-16.session).
```

#### `coverage:12` — GAP — fv-main:17, pr-relay-graph:31 (step 12, A1-2 transition_contract)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:285

- **Evidence**

```text
Step 12: "The contract regenerator carries these into transition_contract, and validate_gcfpe_20260914.py:1482-1500 is updated as an explicit reversal". fv-main:17 asks for status/next_action set false, a decision on epic_change_and_work_unit, and a subset parity check. GRAPH_HANDOFF_CONTRACT_MISMATCH compares only a few scalar fields.
```

- **Problem**

```text
No field list is given, epic_change_and_work_unit is undecided, and the parity check is not adopted. A mapping that leaves transition_contract stale still passes.
```

- **Fix**

```text
Enumerate each transition_contract key's new value in step 12. Decide epic_change_and_work_unit (C-HANDOFF does not require it). Add the check that graph handoff_contract.prohibited is a subset of transition_contract.prohibited_references, with a must-fail regression.
```

#### `coverage:13` — GAP — fv-main:32, fv-rest:12, fv-main:31 (A1-2 explicit contract-only mapping)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:136

- **Evidence**

```text
fv-rest:12: receiver_compatibility PR-35 'same_session_…': true and PR-40 'nathan_manual_merge_assertion_required': true. fv-main:32: route_graph_semantics.same_session_phase_continuation and .pr40_entry, and pr30_ownership. fv-main:31: preservation.versioned_sibling_successors. A1-2 names the key groups but gives no values; C9 gives values for PR-20 and PR-30 only.
```

- **Problem**

```text
No check reads these keys. The regenerator must first reproduce today's bytes, so any key it does not remap carries the reversed rule forward silently.
```

- **Fix**

```text
State each value: PR-35 new dedicated session (same_session false); PR-40 entered on the observed merge or the fallback assertion; same_session_phase_continuation false or renamed; pr40_entry per A1-5; preservation kept for 091426.1 under A1-3, and say so. Add subset checks for receiver_compatibility.
```

#### `coverage:14` — GAP — fv-rest:21 (step 38: 'MERGE_OBSERVED joins the PR-35 result vocabulary and its four pins')

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:37

- **Evidence**

```text
The vocabulary is pinned or restated in more places than four: glow-hde-pr-development SKILL.md:57 with its validator literal :37 ('The PR-35 result vocabulary is exactly `MERGE_PENDING`, …'), behavior-cases.md:21; change-flow SKILL.md:305 and its validator :1009; flowmaster-validate validate_gcfpe_20260914.py:854 and SKILL.md:166; plus :1921, :1292 and the fixture named in the preflight.
```

- **Problem**

```text
'Four pins' is not a list. The exact-sentence literal at :37 is a validator reversal with no must-fail regression. If the skill sentence is left alone, the primary skill states a five-state vocabulary that excludes MERGE_OBSERVED.
```

- **Fix**

```text
List every site in step 38. Treat the :37 literal as an explicit reversal: a new literal, plus the old sentence added to the forbidden list.
```

#### `coverage:15` — GAP — fv-rest:19, fv-main:34 (prose that restates reversed rules)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/change-flow/SKILL.md:453

- **Evidence**

```text
change-flow:453: "GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35". change-flow:275: "one dedicated PR-development session … same-session PR-35". flowmaster-validate SKILL.md:165: "its same-session PR-35 handoff"; :173: "Nathan's later invocation asserts the manual merge"; :294: "One dedicated PR session plans and implements one work unit".
```

- **Problem**

```text
No step assigns these lines. C7 covers only :455, and step 24 touches :453-454 for C-LAT only. After install, the skills restate the reversed rules.
```

- **Fix**

```text
Add them to steps 35 and 40 and to C7 (C-SESSION; C-DISPATCH with its fallback; the successor GCF-17 row), or record each one in §E as intentionally untouched, with a reason.
```

#### `coverage:16` — GAP — pr-relay-graph:8, pr-relay-graph:15 (step 40 at glow-hde-pr-development:164; behavior-cases.md:87)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:304

- **Evidence**

```text
Step 40: "At :164, remove only the manual-assertion clause". A1-5: "Nathan's merge-assertion boundary stays as the fallback where no subscription existed." behavior-cases.md:87 ("The conditional prompt separately requires Nathan's later manual-merge assertion") is in no step.
```

- **Problem**

```text
Deleting the clause leaves the primary skill with no statement of the fallback path the plan keeps, and the behaviour case stays stale.
```

- **Fix**

```text
Rewrite the :164 clause to the single fallback predicate instead of deleting it. Add behavior-cases.md:87 to step 40 with the same wording.
```

#### `coverage:17` — GAP — Step 35's added anchors :100 and :141 (the amendment repeats its own defect 12)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-hde-pr-development/SKILL.md:141

- **Evidence**

```text
Measured on a copy: :100 carries the required literal 'merge-ready ownership' ("Continue in the same dedicated PR session until…"). :141 carries 'same PR continuation' ("same dedicated PR session, workspace/worktree, branch, open PR"), 'continuation prompt', 'original Proceed', 'accepted-final preservation' and 'open PR RS-40'. Step 35 names only :31/:33/:34 (keep) and :32/:38/:55 (replace).
```

- **Problem**

```text
Editing these lines breaks kept literals. 'same PR continuation' restates the shared session that D23-D reverses, so it needs a replacement, a forbidden entry and a regression; nothing says so.
```

- **Fix**

```text
State the treatment per literal. Keep the four kept-rule literals verbatim. Replace 'same PR continuation' with a phase-own-session literal, add the old text to the forbidden list, and give it a must-fail regression. Treat :100 the same way if its wording changes.
```

#### `coverage:18` — GAP — registry-audit:9 (the RS-40 role, and the PR-40 inputs)

- **Location:** /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md:5108

- **Evidence**

```text
RS-40 session_role: "You are the same dedicated PR engineering session for the exact suspended work unit." PR-40 inputs: "…the dedicated PR session identity…" and "The complete PR-35 result whose earlier MERGE_PENDING is historical pre-merge evidence". The amendment says only "RS-40's receiving_role matches the registry's", and step 39 edits only the last PR-40 input.
```

- **Problem**

```text
No replacement text is given for RS-40's role in the graph or the registry. PR-40's session-identity input and its PR-35-result input still assume one session and MERGE_PENDING only.
```

- **Fix**

```text
Give RS-40's new role verbatim for both the graph and the registry (it resumes the recorded phase in that phase's own dedicated session). Change PR-40's :3708 input to 'the PR-30 and PR-35 session identities', and let its PR-35-result input accept MERGE_OBSERVED.
```

#### `coverage:19` — MINOR — fv-main:11, fv-main:28, pr-relay-graph:22, fv-rest:20 (step 38 checks and fixtures)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:302

- **Evidence**

```text
Step 38: "Rewrite DIRECT_PR35_PR40_EDGE, GRAPH_DIRECT_PR40_EDGE, PR40_MANUAL_MERGE_BOUNDARY, POST_MERGE_* and ROUTE_GRAPH_SHORTHAND to the new shape." There is no fixture list for PART-11.
```

- **Problem**

```text
Four things are missing. (1) The replacement exact assertion is not written. (2) Narrowing GRAPH_DIRECT_PR40_EDGE to {PR-30} is not stated as a narrowing (AF-001). (3) HANDOFF-POS-02 must stay for the fallback, yet fv-rest:20 would rewrite it. (4) There is no negative for a PR-40 handoff emitted before any merge event, which guards 'no entry before Nathan merges'.
```

- **Fix**

```text
Write into step 38: exactly one PR-35 to PR-40 edge, automatic false, transport COMPLETE_NEXT_PROMPT_HANDOFF, state MERGE_OBSERVED, condition naming the observed merge. Keep HANDOFF-POS-02 and add a MERGE_OBSERVED positive. Add negatives for automatic:true, a missing merge condition, and a PR-40 handoff before any merge event. State the narrowing.
```

#### `coverage:20` — MINOR — fv-main:22, fv-rest:27 (child: GCF-14/15 disposition and the R1 path fixture)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json:1

- **Evidence**

```text
GCF-14.session: "One new work-unit session bound to one planned PR work unit". GCF-15.session: "Manual operator invocation into the same dedicated PR session." The child correction discusses GCF-15, 16 and 17.LINEAGE only. C8's fixtures are 091426.1 behaviour fixtures only.
```

- **Problem**

```text
Both rows are UNCERTAIN and have no recorded disposition. The R1-level route GCF-17.LINEAGE to GCF-14 has no path fixture (FMV-GCF-EDGE-003 checks `next`).
```

- **Fix**

```text
Record in the child why GCF-14 and GCF-15 need no change: read per plan cycle, the re-plan session is the GCF-14 session of the new cycle. Add a fixture in fixtures/change-flow/scenarios.json that fails with FMV-GCF-EDGE-003 against the historical oracle and passes against the successor.
```

#### `coverage:21` — MINOR — pr-relay-graph:14 (child C6 verification)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/child_p.md:56

- **Evidence**

```text
C6 verification: "the old sentence at :27 fails when injected". The validator checks required literals for presence only. Old :27: "…followed in the same session by PR-35 review remediation… continuation preserves the original Proceed and never requires or creates a second Proceed."
```

- **Problem**

```text
A new required literal cannot make an injected old sentence fail, and C6 adds no forbidden entry.
```

- **Fix**

```text
Add the forbidden entry 'followed in the same session by PR-35' without narrowing any existing entry. Verify that injecting the old sentence yields exactly that finding.
```

#### `coverage:22` — MINOR — fv-main:16 (the glow-graph-contract no-replacement rule)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/SKILL.md:59

- **Evidence**

```text
"Any existing Drive or repository copy of an assembled graph is historical. Do not update it, do not mint a replacement". E2 and E4 item 1 rewrite the bundled graph copies in two skills.
```

- **Problem**

```text
fv-main:16 asked for this conflict to be resolved; the amendment is silent.
```

- **Fix**

```text
Record that copies bundled in a skill are outside that rule, or amend the rule within the package.
```

#### `coverage:23` — MINOR — pr-relay-graph:18 (relay :624)

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/session-relay-flowmaster/SKILL.md:624

- **Evidence**

```text
"NOTION_REFERENCE: a versionless resource name plus its verified directory path". C-HANDOFF requires "full name, version and direct Notion URL".
```

- **Problem**

```text
Undecided: the relay would strip the version and URL that the new bodies require.
```

- **Fix**

```text
Add :624 to step 14, or record it in §E as out of scope with a reason.
```

#### `coverage:24` — MINOR — registry-audit:19, registry-audit:20

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:236

- **Evidence**

```text
E1: "Registry: guards, derived fields and dispositions." The validator runs only once, in E4 item 6. registry-audit:19 asks for line-anchored scripted insertion and a semantic compare through load_data after each edit. registry-audit:20 (optional) is the session_class enum doc.
```

- **Problem**

```text
Structural validity is checked, but an insertion that reflows the YAML or mistypes an input is not caught. The optional enum doc is unaddressed.
```

- **Fix**

```text
Require scripted line-anchored insertion and a load_data semantic diff in E1. Dispose of registry-audit:20 in §E.
```

#### `coverage:25` — MINOR — A1-7 row accounting (fv-main:9, fv-rest:14)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:204

- **Evidence**

```text
Reproduced on a copy of route_sim: 7380cd14…/282 → 56e808b24d375c4186518d90485d244e/283. routing_surface hashes one row per whole edge and one per state_routes key; the state_routes entries of DOC-10, PR-10, PR-20, PR-30, PR-35, PR-40 and RS-40 change.
```

- **Problem**

```text
20 of the 283 digest rows move (12 edges changed, 1 added, 7 state-route rows), not '12 rows change and 1 is added'. The 7 restate the same branch conditions, so the content is complete, but the count Nathan reads is not.
```

- **Fix**

```text
Say that the 7 state-route rows also move, and that they restate the table's conditions.
```

#### `coverage:26` — MINOR — How it was found (evidence attribution)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/preflight_render.md:302

- **Evidence**

```text
amendment1.md:15: "a completeness critic then swept for literals they missed". preflight_render.md:302: "## critic — NO RESULT". No critic output exists in the scratch results.
```

- **Problem**

```text
The evidence file to be committed contradicts the method as described (AGENTS.md: record actual results and limitations).
```

- **Fix**

```text
State that the critic returned no result, and say where the lines it would have found (e.g. :100, :141) came from.
```

#### `coverage:27` — MINOR — N7 and PR-50

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:344

- **Evidence**

```text
N7: "C-TOP is added to the 54 main-ecosystem bodies at E3, with the step 18 placement edit, in the same page edit." Verified on a registry copy: the steps 8/11 selector gives 53 rows, PR-35 in, GCFPE-MGMT-10 and PR-50 out.
```

- **Problem**

```text
PR-50 receives no step-18 edit, so 'in the same page edit' cannot apply to it.
```

- **Fix**

```text
Give PR-50 its own C-TOP edit, placed beside its return rule.
```

### adversary — adversarial test of the amendment draft (21 findings)

#### `adversary:0` — BLOCKER — amendment N3 — C-TOP forbidden patterns (and D23 wording they sit beside)

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:326

- **Evidence**

```text
re.search(v,text,re.M): `\b(?:launch|spawn|auto-?start)\w*\b[^.\n]{0,60}\bsession\b` MATCHES C-TOP itself ('It never creates, launches or schedules another session', :80) and 'do not launch a new session'; F1 matches 'Never run PR-35 as a subagent' and 'run them as a subagent pool'; both MISS 'Launch a new session for PR-40.' / 'Run PR-35 as a subagent.'; F3 misses 'mcp__Claude_Code_Remote__create_session'.
```

- **Problem**

```text
The session-creation pattern fires on the required canonical text, so the clean control fails on all 54 rows and the 'launch a new session for PR-40' regression can never produce its own finding (the finding is already present on clean text). F1/F2 are negation-blind and case-sensitive; F2 also fires on worker phrasing 'spawn worker subagents for parallel reads within this session'; F3's leading \b misses fully-qualified tool names and omits send_later. N3 cannot be adopted as written.
```

- **Fix**

```text
Replace with these tested values (clean on all 13 canonical texts and on 9 worker/negated phrasings, match all 11 injections incl. capitalised ones, compile, round-trip YAML single quotes). <PID> = (?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt). F1: (?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?<PID>\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b. F2: (?i)(?<!never )(?<!not )(?<!no )(?<!n't )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?<PID>. F3: (?:create_session|create_trigger|fire_trigger|send_later|spawn[-_]session)\b. Stated explicitly per AF-001: the new F2 is NARROWER than the draft — a bare 'launch a new session.' naming no prompt is no longer caught. If Nathan wants the broad form, keep broad F2 with (?i) and instead reword C-TOP and the D23 clarification to avoid the token 'launches'.
```

#### `adversary:1` — BLOCKER — A1-5 / A1-7 routing pin, E4 item 1 token — RS-40

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/route_sim.py:1

- **Evidence**

```text
Reconstructed pre-revision sim (amendment wording) -> ('56e808b24d375c4186518d90485d244e', 283), 227->228 edges: matches A1-7. Current route_sim.py (8552 B, mtime 2026-09-23T04:27:37Z; amendment1.md unchanged since 03:48:46Z) adds RS-40 merge_observed -> ('65299e7197199e1c93cb059830f0d6b4', 284), 229 edges. Graph: RS-40->NATHAN_MANUAL_MERGE_ASSERTION (MERGE_PENDING); boundary origin_prompt 'PR-35_OR_RS-40'.
```

- **Problem**

```text
As written, RS-40 still receives C-SUB and C-DISPATCH (original steps 37 and 39, not amended), but only PR-35 gets MERGE_OBSERVED and a PR-40 edge, so an RS-40-resumed PR-35 phase is told to return a result it cannot route. The sim has since been revised to fix this, which changes the digest, row count, edge count and three conditions, so A1-7's 'Approving this amendment is that reading' would approve a diff EXECUTE no longer intends, and E4 item 1's 228-edge token is stale.
```

- **Fix**

```text
Before approval, either (a) update A1-7 to the RS-40-inclusive diff (exact digest, 284 rows, 229 edges, the RS-40 merge_observed and merge_pending rows and the reworded PR-35/boundary conditions), E4 item 1's token, A1-5's text and the registry-deriver row set (PR-35, PR-40, RS-40); or (b) remove C-SUB/C-DISPATCH from RS-40 and state that RS-40 ends at MERGE_PENDING with the fallback only. Re-run the sim from the final text and record the script's sha256 with the result.
```

#### `adversary:2` — GAP — A1-2 contract regenerator — mirrored-key list and byte-for-byte acceptance test

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_gcfpe_20260914.py:1285

- **Evidence**

```text
json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False)+'\n' reproduces 606657 B / 2b78f877 (sort_keys=False too; ensure_ascii=True gives 607719 B). Prototype with only A1-2's listed keys over the amendment graph: validate_graph_contract -> ['GRAPH_DIRECT_PR40_EDGE','GRAPH_STATE_VOCABULARY_MISMATCH']. From a template stripped of mirrored keys, the listed keys do not reproduce 2b78f877; the full set does.
```

- **Problem**

```text
The recipe exists, so A1-2 is not blocked on serialization. But the mirrored list leaves out pairs the validators compare: pr_development_contract.{pr30,pr35}_result_vocabulary, r1_row, primary_skill, invented_session_inspection_endpoint_prohibited and unsupported_platform_limitation_claim_prohibited; authoring_context_vocabulary; pr_return_phase_contract.routes; rescope_contract.decision_vocabulary; route_graph.{prepublication_rescope, postpublication_pr30_rescope, pr35_rescope}, which A1-2 calls contract-only but which mirror phase_aware_rescope_sequences; artifact_availability_contract, qa_closure_contract, terminal_contract and selection_status; the abort_prompt and pf10_addendum_contract fields; transition_contract first_line, fence_language and actual_branch_only; and member_registry.graph_predecessor_union_destinations (change-flow validator :845). As written, the regenerator fails E4 item 2 on the amendment's own MERGE_OBSERVED. The byte test is also a tautology when the template is today's contract, because a no-op script passes it.
```

- **Fix**

```text
Amend A1-2 in three parts. (1) Recipe: UTF-8 json.dumps(indent=2, sort_keys=True, ensure_ascii=False) plus a trailing '\n'. (2) Mirrored set: every pair read by validate_graph_contract :1176-1382 and by change-flow validate_gcfpe_20260914.py:760-848, as listed. (3) Acceptance test: delete every mirrored key from the template, regenerate from today's build and require 2b78f877/606657; as a negative control, change one edge condition in a scratch part and require route_edges, state_routes and source_snapshot.frozen_candidate_graph.sha256 to change.
```

#### `adversary:3` — GAP — step 12 / A1-2 — transition_contract mapping

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_gcfpe_20260914.py:1482

- **Evidence**

```text
Graph handoff_contract.required is a list of 6 strings, and its prohibited list has 9 entries. Contract transition_contract holds 18 scalar flags (e.g. 'status_completed_work_decisions_constraints_unresolved_authority': true, 'epic_change_and_work_unit': true) and prohibited_references has 5. validate_graph_contract compares only first_line, fence_language and actual_branch_only.
```

- **Problem**

```text
Step 12 says the regenerator 'carries these into transition_contract', but list strings have no structural mapping to flag keys. The flags to remove or add are unnamed, so the explicit reversal of :1482-1500 has no defined target.
```

- **Fix**

```text
Name the exact new transition_contract. Remove the flags status_completed_work_decisions_constraints_unresolved_authority, epic_change_and_work_unit and next_action_and_expected_output. Name the added flags (e.g. artifact_repository_paths_with_labels, pr_reference_when_continuing, exceptional_context_only, no_branch_or_commit, no_restated_artifact_content) and the new prohibited_references set. Put the mapping in the regenerator's explicit table. Make HANDOFF_CONTRACT an exact-key check whose must-fail regression reinserts an old flag.
```

#### `adversary:4` — GAP — defect #10 / N3 — D23-E has no guard

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:44

- **Evidence**

```text
Defect #10: 'Four rulings have no guard: D23-B placement, D23-D, D23-E and D23-F'. N3 (:317-335) covers D23-D and C-TOP; D23-B is at steps 18-19 and D23-F at child C5. A grep for 'observed merge event|do not poll|subscribe to the pull' finds only C-DISPATCH and step 39 text, and no assertion.
```

- **Problem**

```text
D23-E still has no registry guard, although D23's tested-guard section requires one per ruling. The preflight's proposed YAML for it was dropped.
```

- **Fix**

```text
Add D23-E guards to N3 (CTR-002). On PR-35 and RS-40, require '[Ss]ubscribe to the pull request', 'do not poll' and 'observed merge event'; on PR-40, require 'observed merge event'. Measured: each matches its canonical home (C-SUB, amended C-DISPATCH). The '[Ss]ubscribe…' value must be YAML-quoted, because as a plain scalar it raises ParserError. Regressions: delete C-SUB; delete only the 'do not poll' clause; delete only the observed-merge sentence. Deleting all of C-DISPATCH yields two findings.
```

#### `adversary:5` — GAP — N3 D23-D + C-TOP required pattern; step 21 / step 20 literal

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:318

- **Evidence**

```text
Measured on a row carrying both amended C-SESSION and C-TOP (PR-30, PR-35, RS-40, ~17 continuity rows): deleting C-TOP, or deleting the C-SESSION sentence, leaves 'never\s+as\s+a\s+subagent' satisfied, so no finding. C-LAT also says 'record it under *In-flight decisions*', so deleting C-DEC on PR-30/PR-35 gives no finding; the regression fires only on RS-40.
```

- **Problem**

```text
The D23-D and C-TOP guards share one pattern and one rule_id, so each masks the other's deletion regression. Their findings are identical under E4 item 9's {(rule_id, summary)} comparison, so they cannot be told apart. C-LAT masks step 21's literal and the literal step 20 adds to the glow-hde-pr-development validator.
```

- **Fix**

```text
Use distinct patterns (tested and YAML-safe). D23-D: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30' (matches C-SESSION only). C-TOP: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session' (matches C-TOP only). Steps 20-21: 'An\s+\*?In-flight decisions\*?\s+section' (matches C-DEC only). Otherwise, name RS-40 as the only valid regression row.
```

#### `adversary:6` — GAP — step 7 functional companion; preflight evidence rendering

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:282

- **Evidence**

```text
The amendment's table cell reads `…\b(?:remains?\|lives?\|stays?)\b…`. Copied literally, Python reads \| as a literal pipe, so the regression 'Concise operational state and pointers remain in Notion.' gets NO MATCH. The raw form in pf_rest2.txt matches. Both forms miss 'Operational state and pointers remain in Notion.' (case-sensitive). render_preflight.py cell() escapes every '|', Notes included.
```

- **Problem**

```text
The regexes exist only in markdown table cells and in an evidence file whose renderer escapes pipes even outside tables. The rendered preflight-2026-09-23.md therefore carries corrupted step 7 and step 17 regexes, and copying either gives a guard that silently never fires. The companion also misses a capitalised sentence start.
```

- **Fix**

```text
Put each guard's exact YAML value in a fenced code block (not a table cell), and render Notes without pipe escaping or cite the raw journal. Change the companion to '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b' (measured clean on C-NOTION). Give it its own must-fail regression: 'Operational state and pointers stay in Notion.'
```

#### `adversary:7` — GAP — A1-1 successor oracle — pin sites and kept-invariant checks

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:24

- **Evidence**

```text
Pins: ORACLE_RELATIVE :24, CHANGE_RUNTIME_MAP_RELATIVE :25-27, EXPECTED_ORACLE_PROFILE :33, ORACLE sha :37-39, MAP sha :40-42, CONTRACT_REQUIRED change-flow :147-148, REQUIRED_SCRIPTS :338-356, OPTIONAL_REFERENCES :360-364, maintenance_metadata :684-687, run_change_flow_fixtures.py:15. The default suite runs no historical validator (:803-805). The oracle's required_global_tokens carry the old profile id.
```

- **Problem**

```text
The successor design can be built without weakening any check, but the amendment lists only the preflight's in-place pins, not the pin sites for the new files. Once :24-42 point at the successors, the default suite no longer checks the historical oracle (52807e58) or runtime map (5574666e); they are checked only at E4 item 4. That is a quiet weakening. Nothing states that the other 44 rows must stay identical. The oracle maps 'CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0' to 3.2.9 (:686), which step 47 moves to 3.3.0. The pin chain in E2 starts at the graph, although the graph pins the oracle's sha.
```

- **Fix**

```text
(a) Move every listed site, plus validate_gcfpe_20260914.py:1127-1133, :1375-1382, :1951-1967 and :2610-2612; the validation profile; protected_identities in both contract copies; global.json:551-557; change-flow SKILL.md:17, :19 and :557; flowmaster-validate SKILL.md:145-149 and :244-249. Leave the historical validators and runners on the historical paths. (b) Add checks: historical oracle and map shas are still verified; the 44 unchanged rows equal the historical rows field for field; the authority block keeps r1_contract_matrix_sha256 faa7fb7d and adds successor_source_matrix_sha256 and successor_rows; rows keep exactly 12 fields (FMV-ORACLE-006). (c) Must-fail regressions: a third row edited with every sha re-stamped; a changed row without a matching matrix edit; one flipped matrix byte. (d) Pin order: matrix → oracle → map → graph → contract → profile → literals → fixtures → SKILL_TREE_SHA256.
```

#### `adversary:8` — GAP — A1-1 successor source matrix — format and digest rule

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:109

- **Evidence**

```text
155 candidate formulas (JSON and table-line variants) reproduced 0 of the 5 tested source_row_sha256 values, which confirms the historical digests cannot be recomputed. The oracle and runtime map bytes reproduce with json.dumps(indent=2, sort_keys=False, ensure_ascii=False)+'\n', which preserves key order; the contract instead uses sort_keys=True.
```

- **Problem**

```text
'The validator recomputes those two digests from it' is feasible only once the matrix format, row addressing and digest formula are fixed, and the amendment gives none of them. Nothing binds the matrix row's content to the oracle row's fields, so the digest would prove only bytes.
```

- **Fix**

```text
Specify the matrix file r1-successor-source-20260923.md: one fenced json block per changed row, holding the 11 content fields plus supersedes_source_row_sha256 (the historical digest). Row digest = sha256 of UTF-8 json.dumps(content fields, sort_keys=True, ensure_ascii=False, separators=(',',':')). The validator checks: the matrix sha pin; oracle row fields equal matrix fields; source_row_sha256 equals the formula; supersedes equals the historical row's digest. Write the successor oracle and map with sort_keys=False.
```

#### `adversary:9` — GAP — A1-5 / step 38 — MERGE_OBSERVED vocabularies and pins

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:302

- **Evidence**

```text
Sites: validate_gcfpe_20260914.py:853-856 EXPECTED_PR35_RESULTS (:1747, :1920); change-flow validate_gcfpe_20260914.py:1007-1010 literal list; glow-hde-pr-development validator :37 (SKILL.md:57, behavior-cases.md:21); GRAPH_STATE_VOCABULARY_MISMATCH :1292; paired result_states :1221-1237; registry :3616-3624; fixture runner :101-108, :361, :363; PROMPT_ROUTE_SEMANTICS :2443.
```

- **Problem**

```text
'Its four pins' are neither named nor enough. Not explicitly covered: the contract side of the vocabulary mirror; change-flow :1007-1010; glow-hde-pr-development :37; fixture reject-pr35-direct-pr40 (:361), which expects failure on exactly the edge A1-5 adds; PR-35's PROMPT_ROUTE_SEMANTICS markers; MERGE_OBSERVED's position in the order-sensitive lists; registry sort order and consumers [PR-40, RS-20]; the docs (change-flow SKILL.md:305, flowmaster-validate :166, relay :283, amthor SKILL.md:49 and interoperability-contracts.md:74); a route_graph shorthand for the observed path.
```

- **Fix**

```text
Enumerate every site in step 38. Fix the order: [MERGE_PENDING, MERGE_OBSERVED, RESCOPE_PENDING, RECOVERY_PENDING, REMOTE_EVIDENCE_PENDING, PRODUCT_OWNER_DECISION_REQUIRED]. Replace DIRECT_PR35_PR40_EDGE and GRAPH_DIRECT_PR40_EDGE with: exactly one PR-35→PR-40 edge (prompt, automatic false, COMPLETE_NEXT_PROMPT_HANDOFF, sole state MERGE_OBSERVED); PR-30→PR-40 still forbidden. Reverse :361 into a must-fail second or automatic edge. Add fixtures: one positive MERGE_OBSERVED case, and negatives with no subscription, before merge, and agent merge. Add a MERGE_OBSERVED marker for PR-35.
```

#### `adversary:10` — GAP — A1-6 overlay re-point; child C9 verification

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_gcfpe_current.py:615

- **Evidence**

```text
The alias path is the default at validate_gcfpe_current.py:615, run_gcfpe_current_fixtures.py:104 and validate_flowmaster.py:363 (OPTIONAL_REFERENCES) and :818, and change-flow SKILL.md:559/:563 resolve the contract_id to the alias. The v4 validator names receiver_compatibility only in its top-level key list (:380). The v3 validate_receiver_contract (:408) has no v4 counterpart.
```

- **Problem**

```text
A1-6 does not list the sites to re-point. Its claim that re-pointing 'replaces stale checks rather than weakening any' leaves out that the 091426.1 contract's receiver_compatibility has no content check. This plan and the child both edit it: PR-35's same_session_… flag, PR-40's nathan_manual_merge_assertion_required, and a new PR-20 key in C9. C9's verification ('validate_graph_contract returns []') never reads receiver_compatibility, so it proves nothing.
```

- **Fix**

```text
List the re-point sites and say whether the alias stays linked. Add a v4 exact-content check for receiver_compatibility: the PR-20 re-plan entry, PR-30 without the PR-40 return, the PR-35 dedicated session, and PR-40 entered on an observed merge or Nathan's assertion. Give each a must-fail regression, and use this check as C9's verification.
```

#### `adversary:11` — GAP — A1-4 cut-over and freeze

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:166

- **Evidence**

```text
Order: merge -> install -> digest check and installed suite -> land bodies -> re-scan -> 'I make the Notion control edits (steps 6, 9, 16, 36, 44)'. Freeze: '…from your merge until the re-scan passes.' The child's C11 ('Made at the cut-over') is missing from this list. The rule behind 'PR sessions are already held until install, by your rule' was not found in the decision record or the Modification.
```

- **Problem**

```text
The freeze ends before the Hub handoff format (step 16), the output standard (step 9) and the register versions (step 44, the only home of member versions once header lines are gone) are updated, and before C11. The amendment also leaves unspecified: sessions already in flight at the merge; who ends the freeze; the abort path if any cut-over step fails; PYTHONDONTWRITEBYTECODE=1 for installed runs (step 1's lesson); pinning 'main' to the merge commit; and review of the E3 rules script that lands the 55 bodies.
```

- **Fix**

```text
Make the freeze run from Nathan's merge, with no lifecycle session in flight, until the executing session reports readback of steps 6, 9, 16, 36, 44 and C11 plus the re-scan, and Nathan lifts it. On any failure, stop and keep the freeze; retain the previous .skill digests for reinstall. Commit the rules script and add it to E5's review set. Run installed tools with PYTHONDONTWRITEBYTECODE=1 and evaluate the registry at the merge sha. Assign N1, N2 and N5 to E1, and N4 and N6 to E2.
```

#### `adversary:12` — GAP — A1-7 reproducibility of the pinned digest

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:202

- **Evidence**

```text
56e808b2 depends on choices absent from the text. The new edge is cloned from PR-35→RS-20 (transport COMPLETE_NEXT_PROMPT_HANDOFF, route_kind NATIVE_RESULT, source_evidence candidate/prompts/c/PR-35.md, handoff_count 1), and merge_observed is inserted after merge_pending. routing_surface sorts edge rows but hashes each state_routes list in its order. graph_parts gives the new edge index 135, which collides with an existing index.
```

- **Problem**

```text
A1-7 says the diff was 'simulated from the exact wording below', but EXECUTE cannot reproduce the digest from that wording alone and would stop under A1-7's own rule. The claim that 'the new edge is appended' is also wrong (the digest is unaffected).
```

- **Fix**

```text
Put the complete new edge object(s) and the state_route_order and vocabulary insertion positions into the amendment. Alternatively, commit the sim script with the E1 evidence and cite its sha256 as the authority. Drop 'appended'.
```

#### `adversary:13` — GAP — E4 item 4 — historical-layer validators

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:252

- **Evidence**

```text
Scratch copy: run_epic_alpha_fixtures.py with no argument gives fixture_suite_ok false; with the change-flow dir, true. validate_strength_middleware and validate_epic_alpha need change_directory, and validate_epic_reengineering needs --change-flow. run_final_scan_fixtures and run_integrated_readiness_fixtures reject any argument. validate_alpha_feedback, validate_final_scan, validate_integrated_readiness and validate_pre_guide_correction are not named.
```

- **Problem**

```text
E4 promises every command 'named with the arguments it takes', but item 4 names 3 of 12 historical validators and runners and gives no arguments. One of the named runners already fails at baseline without its argument, so 'passes' cannot serve as the criterion.
```

- **Fix**

```text
List every historical validator and runner with its exact invocation, record today's baseline result for each, and require each post-change result to equal its baseline.
```

#### `adversary:14` — GAP — steps 18-19 ASK OK? guard; child C4 entries

- **Location:** /home/user/glow-hdengine-v2/docs/ephemeral/modifications/MODIFICATION-20260923-alpha-feedback-open-entries.md:567

- **Evidence**

```text
C-PLACE: 'In the four bodies that also "end `ASK OK?`", `ASK OK?` moves to the line immediately before the block' is an instruction to the worker, not body text. The preflight's 'ordering guard' is the forbidden '\bends? `ASK OK\?`', which bans a wording rather than checking order. Child C4 gives PR-20's new entry and PR-30's changed entry in prose only.
```

- **Problem**

```text
The four ASK OK? bodies and the child's PR-20/PR-30 entries have no canonical wording. The rules script would have to improvise body text, against §P's no-improvisation rule, and the ordering guard cannot be written or given a regression.
```

- **Fix**

```text
Add canonical texts for the ASK OK? variant of C-PLACE and for the PR-20 re-plan entry and the PR-30 entry. Derive the ordering guard from the canonical ASK OK? sentence, e.g. require its literal, and give it a must-fail regression that reorders the lines.
```

#### `adversary:15` — MINOR — E4 items 8-9 — evaluator interface

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/amthor-workspace-governance-audit/scripts/audit_workspace_governance.py:520

- **Evidence**

```text
def _evaluate_assertions(record, text, source_ref) takes one row and one text. Findings have the shape {'rule_id', 'observed': {'summary': …}}, with no top-level 'summary'. Regexes are evaluated with re.search(value, text, flags=re.MULTILINE).
```

- **Problem**

```text
Item 8 says the gate 'passes it the same {id: text}', and item 9 compares {(rule_id, summary)}; neither matches the real interface.
```

- **Fix**

```text
Loop over rows and call _evaluate_assertions(row, bodies[row['prompt_key']], ref). Compare {(f['rule_id'], f['observed']['summary'])}.
```

#### `adversary:16` — MINOR — E4 item 3 — candidate root

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/scripts/validate_flowmaster.py:1166

- **Evidence**

```text
Baseline FLOWMASTER_SUITE_PASS was measured with --gcfpe-contract <contract> --gcfpe-candidate-root <dir>, where <dir> held only graph/GCFPE-20260914.1-Candidate-Graph-Contract.json. Passing --gcfpe-contract alone exits 2 ('must be supplied together').
```

- **Problem**

```text
<root> is a placeholder, and the flag's help text still mentions prompts/. A prompts/ mirror would breach the corpus policy.
```

- **Fix**

```text
State that <root> is a scratch directory containing only graph/GCFPE-20260914.1-Candidate-Graph-Contract.json, which is the embedded JSON of item 1's build (per the profile's relative_to_candidate_root).
```

#### `adversary:17` — MINOR — step 47 — second revision identity

- **Location:** /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/flowmaster-validate/SKILL.md:8

- **Evidence**

```text
FLOWMASTER_VALIDATE_REVISION is 3.2.16, but validator_revision '3.2.14' appears at four sites: validate_flowmaster.py:1221, validate_gcfpe_20260914.py:1090, run_gcfpe_20260914_fixtures.py:702 and validation-profile.json:45.
```

- **Problem**

```text
Step 47 moves only 3.2.16 → 3.3.0, although validation behaviour changes, so validator_revision must move too.
```

- **Fix**

```text
Move validator_revision at all four sites in the same pin set.
```

#### `adversary:18` — MINOR — A1-2 — script home

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:144

- **Evidence**

```text
'Both scripts are committed under docs/ephemeral/modifications/evidence/'. glow-graph-contract SKILL.md says its scripts 'ship with this skill, because they are reusable behaviour', and docs/ephemeral 'is cleared manually'.
```

- **Problem**

```text
The regenerator and deriver are reusable machinery. Kept in ephemeral storage, they will be pruned, and defect #1 ('no generator exists') returns at the next graph change.
```

- **Fix**

```text
Record a follow-up, or add a sixth package, to ship both scripts in glow-graph-contract/scripts. Keep the evidence copy for this review.
```

#### `adversary:19` — MINOR — step 17 — stated limits

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/amendment1.md:289

- **Evidence**

```text
The preflight's raw pattern is clean on all canonical texts and on a combined C-PLACE+C-HANDOFF+C-SESSION+C-TOP paragraph. It fires on the named regression and on '…the branch and the commit SHA', but not on a bare 'names the branch and the commit'.
```

- **Problem**

```text
A bare-noun reintroduction is deliberately not caught, and nothing records that.
```

- **Fix**

```text
Record the limit in §E, and cite the exact YAML value in a code block.
```

#### `adversary:20` — MINOR — child C5 — PR-20 guard

- **Location:** /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/child_p.md:56

- **Evidence**

```text
C5 requires the literal 'PR_WORK_UNIT_LINEAGE_REVIEW' on PR-20. The graph parts name it only in PR-40.json. Whether PR-20's body already names it was not checked, because no body was read.
```

- **Problem**

```text
If the current PR-20 body already contains the literal, the guard is vacuous and its deletion regression cannot fire.
```

- **Fix**

```text
Run the clean control on PR-20's current body first. If the literal is already present, use 'PR_WORK_UNIT_LINEAGE_REVIEW[^.\n]{0,80}\bREJECT\b' or the canonical PR-20 entry sentence instead.
```

