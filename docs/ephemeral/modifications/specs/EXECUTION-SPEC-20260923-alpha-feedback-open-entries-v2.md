---
artifact_type: GCFPE_MODIFICATION_EXECUTION_SPECIFICATION
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
also_serves: MODIFICATION-20260923-pr40-reject-replans
version: v2
written: 2026-09-23
status: APPROVED WITH AMENDMENT 1 (Nathan, 2026-09-23)
compiled_by: workflow wf_6c82e4c3-777 (8 section drafters, 1 verifier); sections 0, 2, 9-12 by the plan's author
---

# Execution specification — Amendment 1

This file holds the exhaustive detail behind `Amendment 1` in the Modification's §P. It gives:
- every edit, literal and guard value;
- every pin site;
- every command, with its arguments and baseline result;
- the disposition of every finding.

**How to read it.**
- This is v2. §12's decisions, and the addendum at its end, are written into every section.
- **Nothing is left open.** An option not stated here is void.
- **If this file seems to contradict one of the amendment's rulings, the ruling governs,** and
  EXECUTE stops and takes it to Nathan.
- **v1** (`EXECUTION-SPEC-…-v1.md`) is kept as the record of how each choice was made.

**Corpus policy.** No prompt body was read to write this file, and none is quoted in it. Every regex
and literal sits in a fenced block, unescaped.


## §0 Stages, and how this specification governs

**Stages.** Each is defined once, here. Every other section cites these names.

| stage | what | where |
|---|---|---|
| **E1** | Repository edits: graph parts except `protected_identities`, the registry, the decision-record notes, and the policy and documentation files | the execution branch, commit 1 |
| **E2** | Skill work on scratch copies. Build the successor source matrix, then the successor oracle and runtime map. Write the successor oracle's digest into `global.json` `protected_identities` (execution branch, commit 2). Then rebuild, regenerate the contract, and follow the pin order in §5 | scratch copies, and the execution branch |
| **E3** | Bodies computed in memory by the body rules script. Nothing is landed | memory only |
| **E4** | The gate (§9) | §E |
| **E5** | The review (§10) | §E and the verdict files |
| **E6** | Delivery and cut-over (§11) | Notion and §E |

**Precedence:**
1. The amendment's rulings (A1-1 to A1-8, and the rulings received).
2. This section and §12.
3. The other sections of this specification.
4. The original §P.
5. The findings.

**Where the sections left a question open, §12 settles it, and every section is read with §12
applied.** Where a section offers options, the one §12 names is the specification; the others are
void. A choice that would contradict a ruling is not settled here: EXECUTE stops and takes it to
Nathan.

## §1 Precedence, superseded findings, and the disposition of every finding

This section gives every preflight row (121) and every critic finding (77) exactly one disposition, and says where each one is carried. It is v1's §1 with every §12 decision applied inline: each value a decision chose cites it, as "(§12 X-n)". No row is left open.

### 1.1 Precedence

This is §0's order, stated for the findings.
1. **Amendment 1 governs.** Its *Precedence* paragraph: wherever it changes a step, a ruling or a canonical wording, it governs, and "the same holds against any preflight row or critic finding that disagrees with it". The decision record's `D23` successor sections rank with it, as rulings it cites:
   - the *Correction* (GCF-17.LINEAGE, not GCF-15);
   - the *Clarification*: every main-ecosystem prompt runs as its own top-level session and never as a subagent, forked agent or workflow agent of another session; nothing creates a session automatically, and Nathan creates every session; a session may use subagents as workers within its own task;
   - the *Successor, Amendment 1 approved* (A1-1, A1-3, A1-5, A1-8 recorded against `D23-D` to `D23-G`);
   - the *Successor, the triage prompt is also outside the main ecosystem*: `GCFPE-MGMT-10` and the *Modification Intake and Triage* prompt are excepted from the Clarification's rules. The triage prompt is not one of the 55 registry members, so nothing in Amendment 1 changes for it.

   The follow-up's §P (child steps C1–C11) governs its own steps and shares the parent's package, gate, review and cut-over.
2. **§0 and §12 of this specification.** §12 settles every question a section left open; an option it does not name is void.
3. **The other sections of this specification.**
4. **The original §P**, where the amendment is silent: its rulings table, canonical wording (C-*) and steps 0–48.
5. **Findings come last.** A finding supplies a value only where none of the above speaks, and never against them.

**What the amendment changes in §P**, and so what every finding is read against:
- Steps 0 and 1 stand; they ran under the original approval.
- §P's PART-11 ruling row (the session-launch option), §P's C-SUB and §P's C-DISPATCH are superseded by A1-5's C-SUB and C-DISPATCH.
- Step 15 runs only through A1-2's contract regenerator (defect 1).
- Step 34's in-place re-pin is replaced by A1-1's successor oracle (defect 3). Historical oracle, runtime map, correction layers and historical contracts keep their bytes; their validators and pins are never edited.
- Step 38: the flag below stays false, the merge-assertion boundary stays as the fallback, and the observed-merge edges are recorded as `observed_merge_edges` inside `post_merge_three_event_contract` (A1-5; §12 V-2). PR-35 → PR-40 and RS-40 → PR-40 are paste edges (A1-7).

```
"direct_PR35_to_PR40_automatic_edge": false
```

- Every fallback condition, including step 39's "where no subscription existed", is worded as A1-5's single predicate:

```
only where no `MERGE_OBSERVED` result was returned for this merge
```

- C-VERSION's successor-page rule applies from the next release, and 091426.1 is edited in place (A1-3). Steps 41–43 run in this cut-over, so the bodies drop their release-bound header lines now (`D23-G`; §12 S-1).
- Step 46 is replaced by E4, and step 47 by E5 (`D24`): six packages (A1-6), one cut-over under a freeze (A1-4), new revisions with every pin moving.
- C-TOP is new, and C-SESSION gains its PR-35 clause (A1-8).
- The routing surface moves only as A1-7's table says: 15 rows, 13 changed and 2 new edge rows, plus 7 state-route rows (§12 V-11). Its identities, and the simulation that is their authority:

```
routing surface   fecc319bdd4ce7ee6201cb77d7231861 / 284 rows
graph             229 edges
simulation        route_sim_final.py  sha256 e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26
```

**The first draft.** The critics worked against the first draft of the amendment, so their targets cite its numbering (N1–N7, the step-changes table). Where Amendment 1 carries the same content, the finding is placed there:
- N3 and N7 are A1-8 and spec §7;
- N4 (the skill package set) and N6 (the relay override and its guards) are A1-6, at E2;
- the first draft's A1-1 to A1-7 keep their numbers.

Amendment 1 carries none of the first draft's step-changes table, N1, N2 or N5. §12 S-2 compiles N1, N2 and N5's scope line as E1 repository edits, so every finding whose only home was one of those is placed.

### 1.2 Superseded findings

**Superseded in full (6).** In each case the finding's required action is overridden. Where another section places something at the same site, it places the amendment's replacement, not the finding's action; the disposition stays SUPERSEDED (verifier conflict 11).
- **fv-main:13** — A1-5 keeps `direct_PR35_to_PR40_automatic_edge` false. The `event_2` update it also asks for is carried by A1-2 ("observed or asserted"), with the values of §12 V-3.
- **fv-main:20** — A1-1: a successor runtime map, not an in-place edit. The historical-layer pins it lists are never edited; the live sites re-point to the successor, which spec §5.6 places.
- **fv-main:28** — A1-5: `MERGE_PENDING` always carries the conditional PR-40 block as the fallback, so HANDOFF-POS-02 stays (coverage:19) rather than being inverted. Spec §8b keeps it.
- **fv-main:31** — A1-2 with A1-3: `versioned_sibling_successors` is kept, because it is true of how 091426.1 was made.
- **fv-rest:1** — A1-1: no in-place runtime-map edit; the historical map and the 091326.2 alias keep their bytes. Its list of child rows (GCF-15, GCF-16, GCF-14) is replaced by the `D23` correction and A1-1 (GCF-17.LINEAGE, and GCF-14's `consumes`). Spec §5.6 places the successor map.
- **coverage:0** — A1-8: C-TOP says "starts", and the guards forbid creating a session to run a named prompt. Its unnamed-object pattern is not adopted.

**Superseded in part; the rest of the row is placed (23).**
- fv-main:2 — its map with `cross_session_route` 0 and its negative fixture for 1; the value is 1 and the negative fixture sets 0 (§12 V-1).
- fv-main:9 — its 281/282-row figures; A1-7's 284 rows govern.
- fv-main:15 — its 226-edge figure; A1-5 keeps the boundary, and A1-7 gives 229.
- fv-main:22, fv-rest:27 — re-pinning GCF-14 and GCF-15; A1-1 keeps their session wording, read per plan cycle.
- pr-relay-graph:30 — the GCF-15 row; the `D23` correction names GCF-17.LINEAGE.
- fv-rest:2 — re-pinning the alias contract; A1-6 takes the finding's other route and re-points the overlay, and the alias is unlinked with its bytes kept (§12 S-5).
- fv-rest:20 — its DOC-20 phrase edit and its HANDOFF-POS-02 rewrite; A1-5 leaves DOC-20 → PR-40 unchanged and keeps the fallback block.
- fv-rest:22 — padding the fixture header to seven or more nonblank lines; the floor becomes 4 (§12, §8b O28 (a)).
- fv-rest:23 — recording the alias as a known contradiction; A1-6 re-points the overlay (§12 S-5).
- fv-rest:28 — its `global.json:48` wording; A1-7's wording governs (child C2).
- pr-relay-graph:8 — deleting the manual-merge clause at `glow-hde-pr-development/SKILL.md:164`; under A1-5 it is rewritten to the fallback predicate (coverage:16).
- pr-relay-graph:25 — new edges "at 235 and above"; A1-7's simulation places them, at indices 128 and 129 (§12 §4 OQ-10).
- pr-relay-graph:27, registry-audit:10 — the premise that the automatic-edge flag becomes true, and pr-relay-graph:27's `DOC-20.json:151` edit; A1-5.
- registry-audit:18 — its sentence "`required_regex` now binds only the Canon source"; §12 S-2 gives N2's sentence. Its advice to drop the count is kept.
- sweep:0 — its illustrative digest; A1-7.
- sweep:1 — keeping the broad session pattern; A1-8 adopts named-prompt guards and states the narrowing.
- sweep:11 — its fv-rest:1/fv-rest:2 re-pin part; A1-1 (spec §5.13).
- sweep:13 — its predicate "where no subscription existed"; A1-5's single predicate.
- coverage:6 — its role literal "never a subagent of another session"; the guard phrase is `never as a subagent, forked agent or workflow agent of PR-30` (§12 W-1).
- adversary:1 — its interim digest; A1-7.
- adversary:14 — its line-reorder regression; the guard is a required pattern on the variant's sentence with a deletion regression, plus G08's forbidden old wording, and §E records that ordering in the output can be checked only on outputs (§12 W-5).

### 1.3 How to read the table

- **Order.** Preflight readers `fv-main`, `fv-rest`, `pr-relay-graph`, `registry-audit`, then critics `sweep`, `coverage`, `adversary`; each by number. This is the order of the rendered evidence file.
- **PLACED** — a home exists and the action is determinate.
- **SUPERSEDED** — the amendment overrides the finding's required action (§1.2).
- **OUT_OF_SCOPE** — the amendment's *Noticed, not in scope* list carries it. Its items in order:
  1. `validate_gcfpe_current.py:602` NameError;
  2. the audit skill's snapshot procedure;
  3. `flowmaster-validate/SKILL.md:178`;
  4. `glow-graph-contract/SKILL.md:13`, `:134`;
  5. per-part `edge_indices` and the builder's index collision;
  6. the derivation scripts' home;
  7. making `glow-graph-contract/SKILL.md` state explicitly that skill-bundled graph copies are validator fixtures built from the parts (§12 S-3).
- **DOCUMENTATION_ONLY** — no action needed. No finding qualifies.
- **UNPLACED** — no home. No finding qualifies after §12.
- **Citations.** A1-1 to A1-8, E4 and E5 are Amendment 1's rulings. "Defect N" is row N of its defect table, which names its answer. "New revisions" is its revision list. "Precedence clause" is its *Precedence* paragraph. "D23 correction" and "D23 clarification" are the decision record's successor sections. "Step N" is original §P. "Cn" is a child step. "§12 X-n" is a decision of §12; "§12, §8a On" or "§12, §8b On" is §12's settlement of that section's question. Spec sections: §2 baseline, §3 canonical wording, §4 graph transforms, §5 R1 successor, pin sites and pin order, §6 contract regenerator, §7 registry, §8 skill edits, §9 gate, §10 review, §11 cut-over.

### 1.4 Disposition of every finding

| id | effect or severity | disposition | where |
|---|---|---|---|
| fv-main:0 | WOULD_FAIL | PLACED | step 42 (D23-G), run in this cut-over (§12 S-1); spec §8 header check inverted, nonblank floor 4 (§12, §8b O28 (a)) |
| fv-main:1 | WOULD_FAIL | PLACED | step 42, run in this cut-over (§12 S-1); spec §8 fixtures (header rebuilt, three-key negatives, URL-label negatives kept); floor 4 (§12, §8b O28 (a)) |
| fv-main:2 | WOULD_FAIL | PLACED | step 29 (graph key is `pr_continuity_contract.adds`); A1-2 mirror; spec §4, §8 exact map with `cross_session_route` 1 and a negative fixture for 0 (§12 V-1); its 0-valued map and fixture for 1 superseded (§1.2) |
| fv-main:3 | WOULD_FAIL | PLACED | step 29; A1-2 (`shared_exactly_one` copied); spec §8 nine-field literal |
| fv-main:4 | WOULD_FAIL | PLACED | A1-2 regenerator (defect 1); spec §6 |
| fv-main:5 | WOULD_FAIL | PLACED | steps 29–30; spec §8 fixture and fixture pin |
| fv-main:6 | WOULD_PASS | PLACED | steps 29–30; spec §8 (new-session case inverted per fv-rest:16; extra-Proceed kept) |
| fv-main:7 | WOULD_PASS | PLACED | steps 13, 29–31; spec §8 fixtures |
| fv-main:8 | WOULD_FAIL | PLACED | A1-2 (member_registry pairs); A1-8 (PR-35 role clause, string per §12 W-1); PR-20 and PR-40 roles stay (§12 W-3), so its conditional PR-20 update does not arise |
| fv-main:9 | WOULD_FAIL | PLACED | A1-7 (approving is the reading; its digest, 284 rows); the finding's 281/282-row figures superseded |
| fv-main:10 | WOULD_FAIL | PLACED | A1-2 regenerator; spec §6 |
| fv-main:11 | WOULD_FAIL | PLACED | A1-5, A1-7 (PR-35 and RS-40 paste edges); spec §8 |
| fv-main:12 | WOULD_FAIL | PLACED | A1-5 (fallback boundary kept; DOC-20 edge unchanged; shorthand `pr35_merge_pending_fallback`, §12 V-4); spec §8 |
| fv-main:13 | WOULD_FAIL | SUPERSEDED | A1-5: `direct_PR35_to_PR40_automatic_edge` stays false; its event_2 update is carried by A1-2, with the values of §12 V-3 |
| fv-main:14 | WOULD_FAIL | PLACED | A1-2 (shorthands revised per §12 V-4, re-plan shorthand `pr40_reject_replan`); C8; spec §6, §8 |
| fv-main:15 | WOULD_FAIL | PLACED | A1-7 (229 edges); its 226 figure superseded because A1-5 keeps the boundary; spec §5 |
| fv-main:16 | WOULD_FAIL | PLACED | E4 (spec §9 items 1–3); spec §5 pin order; the bundled graph copies are validator fixtures built from the parts (§12 S-3) |
| fv-main:17 | WOULD_FAIL | PLACED | A1-2 (flags follow C-HANDOFF; exact-key check); graph ⊆ contract prohibited-reference subset check with a must-fail regression (§12 V-6); spec §6, §8 |
| fv-main:18 | WOULD_FAIL | PLACED | A1-1 (live pins move to the successor); spec §5 pin sites |
| fv-main:19 | WOULD_PASS | PLACED | A1-2 (R1 flags tell the truth: `r1_oracle_changed` true, `protected_r1_46_rows_unchanged` false, §12 V-7); A1-1 (46 rows; 43-row check N9) |
| fv-main:20 | WOULD_FAIL | SUPERSEDED | A1-1: successor runtime map; historical map, validators and pins are never edited. The amendment's replacement, not the finding's action, is what spec §5.6 places |
| fv-main:21 | WOULD_FAIL | PLACED | A1-1 (historical files and pins kept, live sites re-pointed; step 34 superseded) |
| fv-main:22 | UNCERTAIN | PLACED | D23 correction; A1-1 (GCF-17, GCF-17.LINEAGE, GCF-14; GCF-14/15 session wording stays) |
| fv-main:23 | WOULD_FAIL | PLACED | spec §5 pin order (`SKILL_TREE_SHA256` last); E4 |
| fv-main:24 | WOULD_FAIL | PLACED | step 35; defect 12, spec §8 (replace) |
| fv-main:25 | UNCERTAIN | PLACED | defect 12, spec §8 (keep); New revisions (every pin moves) |
| fv-main:26 | WOULD_FAIL | PLACED | step 35; spec §8; C-SESSION's backticks dropped in skill text, A1-8's sentence last (§12 W-6) |
| fv-main:27 | WOULD_FAIL | PLACED | E4 (edited copy; one must-fail regression per reversed literal); E5 |
| fv-main:28 | WOULD_PASS | SUPERSEDED | A1-5: MERGE_PENDING keeps the conditional PR-40 block, so HANDOFF-POS-02 stays (coverage:19); spec §8b keeps it, which is the amendment's action, not the finding's |
| fv-main:29 | WOULD_FAIL | PLACED | spec §5 pin chain (fixture sha, profile count, id literals); spec §8 |
| fv-main:30 | UNCERTAIN | PLACED | child C8 |
| fv-main:31 | WOULD_PASS | SUPERSEDED | A1-2 with A1-3: `versioned_sibling_successors` is kept, being true of 091426.1 |
| fv-main:32 | WOULD_PASS | PLACED | A1-2 value table (spec §6); A1-6 receiver check; C9 (PR-30 unchanged, sweep:21); contract-only texts per §12 W-8 |
| fv-main:33 | UNCERTAIN | PLACED | E4 (55 edited bodies through the edited validator); A1-4 readback; C4 |
| fv-main:34 | WOULD_PASS | PLACED | step 45 (C-D22, code sites added; each site's reason clause replaced by the C-D22 reason, §12 W-7); steps 35, 40 (`SKILL.md:164-165`, `:173`); spec §8 |
| fv-main:35 | UNCERTAIN | PLACED | A1-2 (4.1.0); A1-5 (edges recorded as `observed_merge_edges` inside `post_merge_three_event_contract`, no new top-level key; §12 V-2) |
| fv-rest:0 | WOULD_FAIL | PLACED | A1-1 (oracle pin moves to the successor; historical digest still verified); spec §5 |
| fv-rest:1 | WOULD_FAIL | SUPERSEDED | A1-1: no in-place map edit, historical map and alias keep their bytes; rows per D23 correction. Spec §5.6 places the amendment's successor map, not the finding's action |
| fv-rest:2 | WOULD_FAIL | PLACED | A1-6 (overlay re-pointed, the finding's second route); A1-1 (alias bytes kept); alias unlinked from `change-flow/SKILL.md` and `OPTIONAL_REFERENCES`, defaults re-pointed to the 091426.1 contract (§12 S-5) |
| fv-rest:3 | WOULD_PASS | PLACED | A1-2 (flags truthful, §12 V-7); A1-1 (43 unchanged rows, N9 with historical order; re-stamp regression) |
| fv-rest:4 | WOULD_FAIL | PLACED | A1-1; spec §5 pin sites |
| fv-rest:5 | UNCERTAIN | PLACED | A1-1; spec §5 pin sites (live documentation pin) |
| fv-rest:6 | UNCERTAIN | PLACED | A1-1 (successor matrix, digest formula, authority block) |
| fv-rest:7 | WOULD_PASS | PLACED | A1-1 (new profile id) |
| fv-rest:8 | WOULD_FAIL | PLACED | A1-1 (historical layers untouched); E4 (twelve historical commands equal baseline) |
| fv-rest:9 | WOULD_FAIL | PLACED | spec §5 pin order (`SKILL_TREE_SHA256` last) |
| fv-rest:10 | WOULD_FAIL | PLACED | E4 (spec §9 item 1); spec §5 pin chain; 229 edges (A1-7) |
| fv-rest:11 | WOULD_FAIL | PLACED | A1-2 (revision 4.1.0); spec §5 pin chain |
| fv-rest:12 | WOULD_FAIL | PLACED | A1-2 regenerator (defect 1); spec §6 |
| fv-rest:13 | WOULD_FAIL | PLACED | A1-2 (exact-key handoff check); E4 must-fail; spec §8 fixture |
| fv-rest:14 | WOULD_FAIL | PLACED | A1-7 |
| fv-rest:15 | WOULD_FAIL | PLACED | steps 29–30; spec §4, §8 exact map, `cross_session_route` 1 (§12 V-1) |
| fv-rest:16 | WOULD_FAIL | PLACED | steps 29–31; spec §8 fixtures and pins |
| fv-rest:17 | WOULD_FAIL | PLACED | step 35; spec §8; C-SESSION's backticks dropped in skill text (§12 W-6) |
| fv-rest:18 | WOULD_FAIL | PLACED | step 35; spec §8 (cross-skill nine-field pins; `:10` added) |
| fv-rest:19 | UNCERTAIN | PLACED | steps 35, 40; spec §8: every prose line restating a reversed rule is converged (§12 S-4); `change-flow:366` and `glow-hde-pr-development:135` stay verbatim only where §E records that the line restates no reversed rule |
| fv-rest:20 | WOULD_FAIL | PLACED | A1-5 (positive PR-35/RS-40 rule, PR-30 ban kept); spec §8; its DOC-20 and POS-02 parts superseded by A1-5 |
| fv-rest:21 | UNCERTAIN | PLACED | A1-5 (MERGE_OBSERVED, ordered vocabulary); C4 (PR-40 keeps "historical pre-merge") |
| fv-rest:22 | WOULD_FAIL | PLACED | steps 42–43, run in this cut-over (§12 S-1); spec §8 fixtures; floor 4 (§12, §8b O28 (a)); its pad-to-seven header superseded (§1.2) |
| fv-rest:23 | WOULD_PASS | PLACED | A1-6 (overlay re-pointed to 091426.1; §12 S-5); spec §8; its "record the alias as a known contradiction" superseded (§1.2) |
| fv-rest:24 | WOULD_FAIL | OUT_OF_SCOPE | Noticed, item 1: `validate_gcfpe_current.py:602` NameError |
| fv-rest:25 | UNCERTAIN | PLACED | defect 12, spec §8 (block-shape sentence kept) |
| fv-rest:26 | WOULD_FAIL | PLACED | New revisions; every pin moves (spec §8) |
| fv-rest:27 | UNCERTAIN | PLACED | D23 correction; A1-1 (LINEAGE `next` gains GCF-14); C3 fixture |
| fv-rest:28 | WOULD_PASS | PLACED | C2 (wording per A1-7, which supersedes the finding's), C4, C8; single-Proceed guards kept |
| fv-rest:29 | WOULD_PASS | PLACED | E4; spec §9 (exact commands, candidate root) |
| pr-relay-graph:0 | WOULD_FAIL | PLACED | step 35; defect 12, spec §8 (replace; old text forbidden) |
| pr-relay-graph:1 | WOULD_FAIL | PLACED | step 35; spec §8 (nine-field literal at every site, `:158`, cases `:13`) |
| pr-relay-graph:2 | WOULD_PASS | PLACED | step 35; C6 (combined lines); spec §8 |
| pr-relay-graph:3 | UNCERTAIN | PLACED | defect 12, spec §8 (keep `:33`, `:34`) |
| pr-relay-graph:4 | UNCERTAIN | PLACED | defect 12, spec §8 (keep `:31`) |
| pr-relay-graph:5 | UNCERTAIN | PLACED | step 14; defect 12, spec §8 (clause only; RS-40 qualification kept; `:22` tail deleted, §12, §8a O4 (a)) |
| pr-relay-graph:6 | WOULD_FAIL | PLACED | steps 14, 19; defect 12, spec §8 (first sentence kept; `:133` added, its branch-state clause dropped, §12, §8a O8 (b); `:162` second sentence replaced by C-HANDOFF, C-PLACE at its end) |
| pr-relay-graph:7 | UNCERTAIN | PLACED | step 40; defect 12, spec §8 (C-DISPATCH appended; four literals kept) |
| pr-relay-graph:8 | WOULD_FAIL | PLACED | step 40; spec §8; clause rewritten to A1-5's fallback predicate, not deleted (coverage:16) |
| pr-relay-graph:9 | UNCERTAIN | PLACED | step 37; defect 12, spec §8 (C-SUB before `:112`) |
| pr-relay-graph:10 | WOULD_PASS | PLACED | step 20; spec §8 (anchor `:108`; literal made distinct per adversary:5) |
| pr-relay-graph:11 | WOULD_PASS | PLACED | step 10; spec §8 (C-ART after `:158`, §12 §8a; literal added) |
| pr-relay-graph:12 | WOULD_PASS | PLACED | step 24; spec §8 (procedure kept; literal; cases `:49`) |
| pr-relay-graph:13 | WOULD_PASS | PLACED | step 27; defect 12 (sentence kept) |
| pr-relay-graph:14 | UNCERTAIN | PLACED | child C6 |
| pr-relay-graph:15 | WOULD_PASS | PLACED | steps 35, 40; C6 heading; headings added for C-DEC, C-LAT, C-SUB and MERGE_OBSERVED (§12, §8a O16 (b)); spec §8 |
| pr-relay-graph:16 | UNCERTAIN | PLACED | New revisions (1.3.0, 3.1.0; every pin moves) |
| pr-relay-graph:17 | WOULD_PASS | PLACED | `CONTROL_PLANE` keeps its enum; the S-7 sentence is placed at relay `:353` and `:372` (§12 S-7); spec §8b |
| pr-relay-graph:18 | WOULD_PASS | PLACED | step 14 (`:273`, `:279`, and `:624` per §12 S-6; `:259` drops "/handoff", §12, §8b O17 (b)); spec §8 |
| pr-relay-graph:19 | WOULD_PASS | PLACED | `flowmaster-validate` `CONTRACT_FORBIDDEN`: the same four phrases for the relay and `tw-flowmaster`, each with a must-fail regression (§12, §8b O4 (b)); spec §8b |
| pr-relay-graph:20 | WOULD_FAIL | PLACED | E4 (spec §9 item 1); spec §5 pin chain |
| pr-relay-graph:21 | WOULD_FAIL | PLACED | A1-2 regenerator; spec §6 |
| pr-relay-graph:22 | WOULD_FAIL | PLACED | A1-5, A1-7; spec §8 (narrowing stated) |
| pr-relay-graph:23 | WOULD_PASS | PLACED | E4 (spec §9 item 1 proves assembly only; item 2 parity) |
| pr-relay-graph:24 | WOULD_FAIL | PLACED | child C1 |
| pr-relay-graph:25 | UNCERTAIN | PLACED | C1 (index 172 kept); A1-7 simulation is the authority; new edges take indices 128 and 129, and no two placed edges share an index (§12 §4 OQ-10); the builder's index collision is Noticed, item 5 |
| pr-relay-graph:26 | WOULD_FAIL | PLACED | child C2 |
| pr-relay-graph:27 | UNCERTAIN | PLACED | A1-5 (fallback kept, automatic false, launch withdrawn, DOC-20 unchanged); A1-7 (229) |
| pr-relay-graph:28 | UNCERTAIN | PLACED | steps 29–30 field names; A1-2 mirror; spec §4; `cross_session_route` 1 (§12 V-1) |
| pr-relay-graph:29 | UNCERTAIN | PLACED | A1-7 (PR-40, DOC-10 rows; DOC-20 `material_delta` unchanged) |
| pr-relay-graph:30 | WOULD_FAIL | PLACED | A1-1; D23 correction (LINEAGE, not GCF-15); historical contracts frozen |
| pr-relay-graph:31 | UNCERTAIN | PLACED | A1-2 (flags follow C-HANDOFF); spec §6, §8 |
| pr-relay-graph:32 | WOULD_FAIL | PLACED | spec §5 pin order; step 45 code comment (spec §8) |
| pr-relay-graph:33 | WOULD_PASS | OUT_OF_SCOPE | Noticed, item 4: `glow-graph-contract/SKILL.md:13`, `:134` stale counts |
| registry-audit:0 | WOULD_FAIL | PLACED | E4 (in memory, no snapshot or hash; defect 8); spec §9 item 8 |
| registry-audit:1 | WOULD_FAIL | PLACED | E4; spec §9 items 8–9 |
| registry-audit:2 | UNCERTAIN | PLACED | steps 8, 11, 17; spec §7 (53-row selector) |
| registry-audit:3 | WOULD_FAIL | PLACED | step 17; spec §7 (anchored pattern, clean control, limits) |
| registry-audit:4 | UNCERTAIN | PLACED | step 11; spec §7 |
| registry-audit:5 | WOULD_FAIL | PLACED | step 43, run in this cut-over (§12 S-1); spec §7 (header-window guards G12–G14 incl. `Set:`, with the verifier's decorated-header prefix, §12 Registry guards) |
| registry-audit:6 | WOULD_PASS | PLACED | steps 4, 5, 7; spec §7 (G04 on the 10 step-5 rows, §12 Registry guards; companion per adversary:6) |
| registry-audit:7 | UNCERTAIN | PLACED | step 33; spec §7 (quoted input; role parity); PR-35 role string per §12 W-1 |
| registry-audit:8 | WOULD_PASS | PLACED | step 33; spec §7 (forbidden line text) |
| registry-audit:9 | UNCERTAIN | PLACED | its RS-40 role text adopted verbatim for graph and registry, `creator_role` changed, and mirrored into `member_registry['RS-40']` (§12 W-2); its `:3708` edit (spec §7) |
| registry-audit:10 | WOULD_FAIL | PLACED | A1-2 deriver (PR-35, PR-40, RS-40); spec §7; automatic-edge premise superseded by A1-5 |
| registry-audit:11 | WOULD_FAIL | PLACED | child C5 (deriver; PR-20 input without backticks, §12 Registry guards); its postflight note is recorded in §E (§12 Other settlements, §1) |
| registry-audit:12 | WOULD_FAIL | PLACED | defect 10, spec §7; A1-8 guards; ASK OK? variant and its guards (§12 W-5); PR-40 entry wording (§12 W-4); masking anchors (§12 Registry guards) |
| registry-audit:13 | WOULD_FAIL | PLACED | A1-6 (fifth package); C10; spec §8 |
| registry-audit:14 | WOULD_FAIL | PLACED | A1-6; spec §8 |
| registry-audit:15 | WOULD_FAIL | PLACED | A1-6; spec §8 (nine-field constant; revision pin) |
| registry-audit:16 | UNCERTAIN | PLACED | A1-6; A1-3 (C-VERSION prospective); spec §8 |
| registry-audit:17 | WOULD_PASS | PLACED | E1 edit N1: new key `body_identity_disposition` under `body_extraction_convention`; `authoritative-surfaces.md:59` corrected (§12 S-2) |
| registry-audit:18 | WOULD_PASS | PLACED | E1 edit N2: `ecosystem-change-management.md:141`, no count (§12 S-2); its "binds only the Canon source" sentence superseded by S-2's (§1.2) |
| registry-audit:19 | WOULD_PASS | PLACED | A1-2 (line-anchored insertion; `load_data` diff); E4 |
| registry-audit:20 | WOULD_PASS | PLACED | `DEDICATED_PR_REVIEW_SESSION` added to the schema enum doc in the fifth package (§12 S-8) |
| sweep:0 | BLOCKER | PLACED | A1-5, A1-7 (RS-40 edge; A1-7 digest, 284 rows, 229 edges); A1-2 deriver; spec §8; its illustrative digest superseded |
| sweep:1 | GAP | PLACED | A1-8 (C-TOP says "starts"); its keep-the-broad-pattern advice superseded by A1-8's guards |
| sweep:2 | GAP | PLACED | defect 10, spec §7 (D23-E guards); spec §8 (`exact_markers`); PR-40 entry wording (§12 W-4) |
| sweep:3 | GAP | PLACED | A1-5 (one ordered vocabulary); spec §4, §6, §8 |
| sweep:4 | GAP | PLACED | step 35; defect 12, spec §8; C6 combined lines |
| sweep:5 | GAP | PLACED | A1-6 (sixth package, relay bytes); New revisions (1.2.0); E5; A1-4; `CONTRACT_FORBIDDEN` four phrases for both skills (§12, §8b O4 (b)); `:311` per §12, §8b O24 (a) |
| sweep:6 | GAP | PLACED | A1-6 (GCFPE override outside the core; `CONTRACT_REQUIRED`) |
| sweep:7 | GAP | PLACED | A1-1 (successor files; historical digests still verified); C3; spec §5 |
| sweep:8 | GAP | PLACED | A1-1 (historical pins never edited); E4 (twelve commands); spec §2, §9 |
| sweep:9 | GAP | PLACED | this section (every row, WOULD_PASS included) |
| sweep:10 | GAP | PLACED | A1-2 (value table; event_2 per §12 V-3; `versioned_sibling_successors` kept); A1-5; spec §6 |
| sweep:11 | GAP | PLACED | Precedence clause; this section; its fv-main:2 part per §12 V-1; its fv-rest:1/fv-rest:2 part superseded (§1.2) |
| sweep:12 | GAP | PLACED | A1-6 (change-flow retired-phrase check): a case-insensitive forbidden-phrase loop in `change-flow/scripts/validate_gcfpe_20260914.py`, including the old `:450` imperative (spec §8b.3; §12, §8b O15 (b); §12 W-9) |
| sweep:13 | GAP | PLACED | steps 35, 40; spec §8 (`:353`, `:453`); no line restating a reversed rule stays untouched (§12 S-4); its "where no subscription existed" predicate superseded by A1-5 (§1.2) |
| sweep:14 | GAP | PLACED | A1-5 (active only on confirmed delivery; fallback always carried) |
| sweep:15 | GAP | PLACED | its second option: PR-20 and PR-40 roles stay, body-level C-TOP and its guards carry the rule, and the `D23` clarification's *Guard* paragraph is corrected (§12 W-3) |
| sweep:16 | GAP | PLACED | child C6; C10 |
| sweep:17 | MINOR | PLACED | step 41, run in this cut-over, also covers `prompt-body-content-policy.md:88` (§12 S-1; text in §3) |
| sweep:18 | MINOR | PLACED | E1 edits: the token lines are labelled "as measured before `D23`", not restated; `ecosystem-change-management.md:176` reworded (§12 S-2) |
| sweep:19 | MINOR | PLACED | step 37; spec §8a `:121` edit, sweep:19's wording (see Unsettled U-1) |
| sweep:20 | MINOR | PLACED | step 35; spec §8 (flowmaster-validate `SKILL.md:393`) |
| sweep:21 | MINOR | PLACED | child C9 |
| sweep:22 | MINOR | PLACED | child C7 |
| sweep:23 | MINOR | PLACED | E1 edit N1, covering `evidence_contract` and `source_snapshot` identities (§12 S-2) |
| sweep:24 | MINOR | PLACED | A1-1 (GCF-14 `consumes`; three rows change) |
| sweep:25 | MINOR | PLACED | A1-8 (semantic invariant in the fifth package); spec §8 |
| sweep:26 | MINOR | PLACED | bundled graph copies are validator fixtures built from the parts, outside `glow-graph-contract/SKILL.md:59` (§12 S-3) |
| sweep:27 | MINOR | PLACED | A1-3 (the date is informational) |
| coverage:0 | BLOCKER | SUPERSEDED | A1-8: C-TOP reworded, and guards forbid a session for a named prompt; its pattern not adopted |
| coverage:1 | BLOCKER | PLACED | defect 10, spec §7 (D23-E guards and regressions); PR-40 entry wording (§12 W-4) |
| coverage:2 | GAP | PLACED | A1-5, its option (b); A1-7; A1-2 deriver (RS-40) |
| coverage:3 | GAP | PLACED | A1-5 (one fallback predicate, in C-DISPATCH and the A1-7 rows); spec §8 fixture |
| coverage:4 | GAP | PLACED | Precedence clause (supersedes the §P PART-11 row and C-DISPATCH) |
| coverage:5 | GAP | PLACED | A1-8 (distinct patterns); spec §7 |
| coverage:6 | GAP | PLACED | D23 clarification, *Guard*; A1-8; spec §7, §8; guard phrase `never as a subagent, forked agent or workflow agent of PR-30`, shared by the registry and the new `flowmaster-validate` check on `member_registry['PR-35'].receiving_role` (§12 W-1); its own phrase superseded (§1.2) |
| coverage:7 | GAP | PLACED | Precedence clause; this section |
| coverage:8 | GAP | PLACED | this section |
| coverage:9 | GAP | PLACED | A1-1 (successor files; live versus historical); spec §5 |
| coverage:10 | GAP | PLACED | A1-1 (matrix format, formula, authority block) |
| coverage:11 | GAP | PLACED | A1-1 (43 unchanged rows field for field; re-stamp regression) |
| coverage:12 | GAP | PLACED | A1-2 (handoff flags; exact-key check); spec §6; subset check with a must-fail regression (§12 V-6) |
| coverage:13 | GAP | PLACED | A1-2 value table; A1-6 receiver check; `same_session_phase_continuation` renamed, contract-only texts per §12 W-8 |
| coverage:14 | GAP | PLACED | A1-5; spec §8 (every site; `:37` reversal) |
| coverage:15 | GAP | PLACED | steps 35, 40; spec §8: every line restating a reversed rule is converged (§12 S-4) |
| coverage:16 | GAP | PLACED | A1-5; step 40; spec §8 (`:164`, cases `:87`) |
| coverage:17 | GAP | PLACED | defect 12, spec §8 (per-literal treatment at `:100`, `:141`) |
| coverage:18 | GAP | PLACED | RS-40 role (§12 W-2); PR-40 inputs `:3705` and `:3710` (§12 W-4) |
| coverage:19 | MINOR | PLACED | A1-5, A1-7; spec §8 (assertions, fixtures, narrowing) |
| coverage:20 | MINOR | PLACED | A1-1 (GCF-14/15 read per plan cycle); C3 |
| coverage:21 | MINOR | PLACED | child C6; its fix, the forbidden entry `followed in the same session by PR-35` with regression R-C6-27, is compiled in spec §8a |
| coverage:22 | MINOR | PLACED | its first fix: skill-bundled copies are recorded as outside the rule, being validator fixtures built from the parts (§12 S-3); making `glow-graph-contract` say so is Noticed, item 7 |
| coverage:23 | MINOR | PLACED | relay `:624` gains the S-6 sentence (§12 S-6) |
| coverage:24 | MINOR | PLACED | A1-2 (line-anchored; `load_data` diff); its registry-audit:20 part per §12 S-8 |
| coverage:25 | MINOR | PLACED | A1-7 (15 route rows, 13 changed and 2 new, plus the 7 state-route rows; the amendment's "16" corrected, §12 V-11) |
| coverage:26 | MINOR | PLACED | amendment, *How it was found* (the critic returned nothing) |
| coverage:27 | MINOR | PLACED | A1-8 (PR-50 is a separate edit) |
| adversary:0 | BLOCKER | PLACED | A1-8 (named-prompt guards; narrowing stated); spec §7 |
| adversary:1 | BLOCKER | PLACED | A1-5 (RS-40 included); A1-7 (digest, 284 rows, 229 edges; simulation sha256 recorded); its interim digest superseded |
| adversary:2 | GAP | PLACED | A1-2 (recipe; full compared-pair set; strip-and-regenerate test; negative control) |
| adversary:3 | GAP | PLACED | A1-2 (exact-key handoff check); spec §6 |
| adversary:4 | GAP | PLACED | defect 10, spec §7; PR-40 entry wording (§12 W-4) |
| adversary:5 | GAP | PLACED | A1-8 (distinct patterns); spec §7 (C-DEC pattern) |
| adversary:6 | GAP | PLACED | spec §7 (fenced values; case-insensitive companion; own regression) |
| adversary:7 | GAP | PLACED | A1-1 (sites, kept checks, regressions); spec §5 pin order |
| adversary:8 | GAP | PLACED | A1-1 (matrix format, digest formula) |
| adversary:9 | GAP | PLACED | A1-5; spec §8 (vocabulary sites; `:361` reversed; fixtures) |
| adversary:10 | GAP | PLACED | A1-6 (re-point; receiver content check on all seven receivers, §12 V-5); C9; alias per §12 S-5 |
| adversary:11 | GAP | PLACED | A1-4 (freeze, stop rule, rollback, rules script in E5, bytecode, merge commit); N1, N2 and N5's scope line are E1 edits (§12 S-2); N4's and N6's content (package set, relay override and guards) is A1-6's, at E2 |
| adversary:12 | GAP | PLACED | A1-7 (the committed simulation and its sha256 are the authority); new edges take indices 128 and 129 (§12 §4 OQ-10); collision is Noticed, item 5 |
| adversary:13 | GAP | PLACED | E4 (twelve historical commands equal baseline); spec §2, §9 |
| adversary:14 | GAP | PLACED | ASK OK? variant text and guards (§12 W-5); child half placed (C-PR20-ENTRY, C-PR30-ENTRY); its line-reorder regression superseded (§1.2) |
| adversary:15 | MINOR | PLACED | spec §9 items 8–9 (real interface) |
| adversary:16 | MINOR | PLACED | spec §2, §9 (`<root>` defined) |
| adversary:17 | MINOR | PLACED | New revisions (validator revision moves alongside) |
| adversary:18 | MINOR | OUT_OF_SCOPE | Noticed, item 6: the scripts ship in `glow-graph-contract` (A1-2) |
| adversary:19 | MINOR | PLACED | spec §7 (limit recorded; value fenced) |
| adversary:20 | MINOR | PLACED | child C5 (clean control on today's PR-20 body) |

### 1.5 Counts

| disposition | preflight | critic | total |
|---|---|---|---|
| PLACED | 114 | 75 | 189 |
| SUPERSEDED | 5 | 1 | 6 |
| OUT_OF_SCOPE | 2 | 1 | 3 |
| DOCUMENTATION_ONLY | 0 | 0 | 0 |
| UNPLACED | 0 | 0 | 0 |
| **total** | **121** | **77** | **198** |

- **198 rows, confirmed.** The table holds every key of `raw_findings.json` exactly once: 121 preflight rows and 77 critic findings, and no others.
- **From v1:** the 19 UNPLACED rows are all PLACED, each on the §12 decision its row cites. Nothing else changed disposition. coverage:22 is PLACED on its first fix (§12 S-3), and the explicit skill statement it also offers is Noticed, item 7.
- **65 rows cite a §12 decision.** No row names an open question.
- **23 rows are superseded in part** (§1.2), and the 6 rows superseded in full are unchanged from v1.
- **The five blockers** (sweep:0, coverage:0, coverage:1, adversary:0, adversary:1) match the amendment's count. Four are placed, and coverage:0 is superseded by A1-8.

### 1.6 Records for §E that this section's rows rely on

These are recorded, not decided, here; each is §12's.
- registry-audit:11's note that the next postflight restate its check (f) (§12 Other settlements, §1).
- `change-flow:366` and `glow-hde-pr-development:135` stay verbatim only where §E records that the line restates no reversed rule; otherwise they are converged (§12 S-4).
- Ordering of `ASK OK?` in the output can be checked only on outputs (§12 W-5).
- `RS-40`'s `session_class DEDICATED_ONE_OFF` is left unchanged, a pre-existing inaccuracy out of scope (§12 S-9). It is not one of the 198 findings.

### Unsettled

- **U-1. `glow-hde-pr-development/SKILL.md:121`, the polling rule (sweep:19; v1 §1 OQ-20).** §12 cites no decision for v1 §1 OQ-20. Spec §8a compiles one edit at `:121` without an `O`-number, sweep:19's qualifier ("where no subscription delivers it, poll only when …"), and §12 S-4's convergence rule is consistent with it. sweep:19 is PLACED on that compiled edit. Confirm this, or state that the line is kept verbatim and record it in §E.

## §2 Baseline, measured 2026-09-23

Every identity and result below was measured in this session. E2 starts by re-measuring each one,
and **stops if any value differs**: that would mean the installed tree moved.

### Installed skill digests (`freeze.py`, file count then sha256)

```
flowmaster-validate                 29  b9ca212ac1275f16af12d34ad15d3df6e95fc71a95f2ce1ab56ee7245a3317af
change-flow                         21  80e877c20fa9be5b3a438b7be1f0d866f9e187efd0fe1bc1a857e03f56dbcff8
glow-hde-pr-development              4  e109d47ac9410a7794c6fd03d0de6237b4a2b9a746d7d4b10138c117f06dc843
session-relay-flowmaster             5  4ef8daa3faabc085b940ea0a93153892bff049d261521761ead9aa36f8a3a2ca
amthor-workspace-governance-audit   15  6cd088a00c5bbcb325a630e1145926cad30f42a2e294853d55c79e5eb7178bfc
tw-flowmaster                        2  fa3fac85b69c0f58b87970ba506acfb9e0095b018431f86f9669c71dbea03ec4
glow-graph-contract                  6  4e671ddc935b629f7285baeb42b93c9848b19fdeb1be39ebfcaa35c2d171f1b8   (not repackaged)
```

`flowmaster-validate`'s declared `SKILL_TREE_SHA256` is `eb9634d6…`. It measured equal: the default
suite passed on the installed tree.

### Identities the change moves

```
bundled graph (both skills)        569835 B  sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223
graph build token                  55 nodes, 227 edges, 55 state_routes, 280 state-route rows
direct-handoff contract (both)     606657 B  sha256 2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b  revision 4.0.6
routing surface                    7380cd14430777675f1e8b2cdfa4a0da / 282 rows
R1 oracle (historical, kept)       sha256 52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e   46 rows
R1 runtime map (historical, kept)  sha256 5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e
```

### Target identities, from the routing simulation

`route_sim_final.py`, sha256 `e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26`,
committed with the evidence.

```
graph build token                  55 nodes, 229 edges, 55 state_routes
bundled graph                      574175 B  sha256 b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7
routing surface                    fecc319bdd4ce7ee6201cb77d7231861 / 284 rows
```

The simulated graph still carries today's R1 oracle digest in `protected_identities`, so its bytes
are not final: the digest changes once the successor oracle's hash is written in (§5 pin order). The
routing surface covers only `route_edges` and `state_routes`, so it is final.

### Validator baseline

Measured on a full scratch copy of the synced skills tree, with `PYTHONDONTWRITEBYTECODE=1` and
`TMPDIR` inside the scratch copy. Several validators need their sibling skills, so run nothing on a
partial copy.

**`<fv>`** means `<copy>/flowmaster-validate/scripts`, and **`<cf>`** means `<copy>/change-flow`.

**Live suites.** Their post-change result must be a pass:

```
python3 <fv>/validate_flowmaster.py --skills-root <copy>                                  FLOWMASTER_SUITE_PASS
python3 <fv>/validate_flowmaster.py --skills-root <copy> --strict-warnings \
    --gcfpe-contract <cf>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json \
    --gcfpe-candidate-root <root>                                                         FLOWMASTER_SUITE_PASS
python3 <fv>/validate_gcfpe_20260914.py <cf> --contract <cf>/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
                                                                                          "ok": true, errors []
python3 <fv>/run_gcfpe_20260914_fixtures.py <cf> --contract <same>                       fixture_suite_ok true, 172 cases, 0 failed
python3 <fv>/validate_gcfpe_current.py <cf>                                               "ok": true
python3 <fv>/run_gcfpe_current_fixtures.py <cf>                                           fixture_suite_ok true
python3 <fv>/run_change_flow_fixtures.py                                                  fixture_suite_ok true
python3 <cf>/scripts/validate_gcfpe_20260914.py                                          passes (fail-fast; exit 0)
python3 <copy>/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py        PASS
TMPDIR=<tmp> python3 <copy>/session-relay-flowmaster/scripts/validate_relay_manifest.py --self-test
                                                                                          PASS, 230 cases, 0 failed
cd <copy>/amthor-workspace-governance-audit/scripts && TMPDIR=<tmp> python3 run_fixture_suite.py
                                                                                          34 tests OK
cd <copy>/amthor-workspace-governance-audit/scripts && python3 validate_project_prompt_registry.py \
    <repo>/docs/prompt_ecosystem_management/project-prompt-contract-registry.md          {"valid": true, "problems": []}
```

**`<root>` is a scratch directory holding only `graph/GCFPE-20260914.1-Candidate-Graph-Contract.json`,
the embedded JSON of the item-1 build.** It holds no `prompts/` directory, because that would mirror
the prompt corpus.

**Historical layer.** Each post-change result must equal its baseline, byte for byte:

```
python3 <fv>/validate_strength_middleware.py <cf>                      "ok": true
python3 <fv>/validate_epic_alpha.py <cf>                               "ok": true
python3 <fv>/validate_epic_reengineering.py --change-flow <cf>         "status": "PASS"
python3 <fv>/run_strength_middleware_fixtures.py <cf>                  fixture_suite_ok true
python3 <fv>/run_epic_alpha_fixtures.py <cf>                           fixture_suite_ok true
python3 <fv>/validate_integrated_readiness.py                          exit 0, no output
python3 <fv>/validate_pre_guide_correction.py                          exit 0, no output
python3 <fv>/validate_final_scan.py                                    exit 0, no output
python3 <fv>/validate_alpha_feedback.py                                exit 0, no output
python3 <fv>/run_integrated_readiness_fixtures.py                      fixture_suite_ok true
python3 <fv>/run_final_scan_fixtures.py                                fixture_suite_ok true
python3 <fv>/run_alpha_feedback_fixtures.py                            fixture_suite_ok true
```

The graph builder and closure run from the repository:

```
python3 <copy>/glow-graph-contract/scripts/graph_parts.py build <repo>/docs/graph/parts <scratch>/graph.md
python3 <repo>/docs/prompt_ecosystem_management/closure.py <PROMPT-ID> --json
```

## §3 Canonical wording, final

Every fixed text that EXECUTE places, in its final form, with §12 applied. Precedence: the amendment governs §P's canonical wording and steps where they differ (amendment, *Precedence*); A1-5's C-SUB and C-DISPATCH supersede §P's C-SUB, C-DISPATCH and PART-11 ruling row; the follow-up's texts are its §P *Canonical wording*; §12 settles every choice v1 left open, cited as "(§12 X-n)". A worker who cannot place a text reports it and does not improvise (§P *Canonical wording*). Nothing here is re-authored per prompt.

**Scope of the session rule.** Every main-ecosystem prompt, that is every GCFPE prompt except `GCFPE-MGMT-10`, runs as its own top-level session and is never a subagent, forked agent or workflow agent of another session. Nothing creates a session automatically; Nathan creates every session. A session may use subagents as workers within its own task (`D23` clarification). The *Modification Intake and Triage* prompt is also outside the main ecosystem and is not one of the 55 registry members, so no text below changes for it (`D23` successor, triage).

**Conventions.**
- A code block is the exact string. Hard wraps in the source files are not part of a text: a wrapped line joins the next with one space. C-LAT keeps its blank line and its numbered items on their own lines. Asterisks and backticks are part of the text.
- Phases are §0's: **E1** repository work on the execution branch (graph parts, registry, decision-record notes, policy and documentation files); **E2** skill work in scratch copies; **E3** bodies computed in memory by the body rules script, which holds these texts and anchor patterns, never body text (A1-4 item 2); **cut-over** lands bodies and Notion control edits after the six packages are installed (A1-4 item 5).
- "Converges on" for a skill line means the text is placed while every kept validator literal on that line stays. The keep/replace/forbid marking per literal is spec §8 (amendment defect 12).
- Line numbers are those of today's installed trees and repository, as the plan and findings cite them.
- Skill-site decisions below cite §12's settlement of §8's own question ids, as "(§12, §8a On)" or "(§12, §8b On)". Spec §8 holds the edit itself.

### 3.1 Texts unchanged from §P

**C-NOTION** (PART-02).

```text
Concise operational state, results and pointers live in the repository under `docs/ephemeral/`. Notion holds the published prompt bodies and the maintenance surfaces a destination rule names; this prompt reads Notion and writes to it only where its task instruction directs a write.
```

- **Goes:** the bodies of PR-10, PR-20, PR-30, PR-40, OPS-10, OPS-20 and OPS-30, replacing the sentence that ends in `CONTROL_NOTION` (step 3). The relay's adapted form is in 3.5 (step 2).
- **Placed by:** step 3, computed at E3, landed at cut-over.

**C-ART** (PART-03).

```text
Before emitting any handoff, write every result this prompt produces — verdict or state, decisions, test and validation results with their outcomes, constraints, unresolved items and owners — into its output artifact, and read it back. The handoff names that artifact; it never carries the only copy of a fact.
```

- **Goes, bodies:** as the first sentence of the result or output section (the section naming the output artifact) of the 53 bodies whose registry row's `required_literals` contain `NEXT_PROMPT_HANDOFF` (step 8; selector registry-audit:2: PR-35 in, GCFPE-MGMT-10 and PR-50 out; measured 53).
- **Goes, skills:** `glow-hde-pr-development`, as a new paragraph after SKILL.md:158, not mid-sentence at :155 as step 10 says (pr-relay-graph:11; §12, §8a O1). Relay `:273` and `change-flow:277`, which carry results "in the existing handoff", both take "in the output artifact that the handoff names" (§12, §8b O18 (b)). `amthor-workspace-governance-audit` gains an invariant for C-ART (§12, §8a O21 (b)).
- **Placed by:** step 8 (E3, cut-over); step 10 (E2). The step-9 Hub sentence is a separate literal (3.5).
- **Note:** the §P source wraps between "never" and "carries"; the placed text has one space there (registry-audit:4).

**C-HANDOFF** (PART-04; replaces each body's handoff field list).

```text
The block names the exact destination prompt by full name, version and direct Notion URL; the receiving role and session; each input artifact by repository path, with a one-line label; the pull request reference when the receiver continues an existing PR; and, only for a condition those artifacts do not already record, the minimum context it needs. It carries no branch and no commit: an artifact is identified by its versioned filename, and an issued version is never edited. It does not restate history, architecture, decisions, scope, acceptance criteria, workflow rules or artifact contents that the named prompt, canon or files hold. No placeholders, menus, alternate destinations, "above", prior-chat reconstruction or unlinked filenames.
```

- **"An issued version is never edited"** covers the handoff's input artifacts, so the text stays as it is alongside A1-3's in-place edit of 091426.1 (§12 Other settlements, §3).
- **Goes, bodies:** the same 53 bodies, replacing the handoff field-list paragraph anchored on the sentence containing `NEXT_PROMPT_HANDOFF` (step 13). The replacement keeps the `NEXT_PROMPT_HANDOFF` literal and is made in the same page edit as C-PLACE (fv-main:33). PR-30 step 6 and PR-35's *Required inputs* drop branch, worktree, commit and head as handoff content and keep them as entry-recovery checks (step 13).
- **Goes, skills (field-list clauses only, never whole lines):**
  - `glow-hde-pr-development` SKILL.md:22, whose tail is deleted because recovery covers it, and whose postpublication-qualification literal stays (pr-relay-graph:5; §12, §8a O4 (a)); :82; :133, which drops its branch-state clause (pr-relay-graph:6; §12, §8a O8 (b)); :162, whose first sentence stays verbatim and whose second sentence is replaced whole by C-HANDOFF (pr-relay-graph:6, fv-rest:25; §12, §8a O23 (a)).
  - `change-flow` :295. `:313` stays verbatim (child C7; §12, §8b O10).
  - `session-relay-flowmaster` :259, which drops "/handoff" from its scope (§12, §8b O17 (b)); :273 (C-ART above); :279, as C-HANDOFF then C-PLACE (pr-relay-graph:18; §12, §8b O19); :624 (§12 S-6; text in 3.6).
  - `amthor-workspace-governance-audit` SKILL.md:38, dropping the Notion-resident clause, and `references/interoperability-contracts.md` (registry-audit:13, :14).
  - `tw-flowmaster` :304, which drops "/handoff" like relay :259, and :315, whose whole line equals the relay's new :279 (sweep:5, A1-6; §12, §8b O17 (b), O19). `:311` takes §8b's simulated text (sweep:5; §12, §8b O24 (a)).
  - Required literal `It carries no branch and no commit`, with a deletion regression, in `glow-hde-pr-development` and in `change-flow`'s validator (§12, §8a O12 (b); §12, §8b O16 (b)).
- **Goes, Notion:** Hub § *Handoff format — required structure*, replacing the 16-section list with C-HANDOFF followed by the step-16 sentence in 3.5 (step 16).
- **Carried as fields, not text:** graph `handoff_contract.required` and `.prohibited` (step 12, E1; lists in 3.6); contract `transition_contract` flags, set by the regenerator, with `HANDOFF_CONTRACT` an exact-key check (A1-2, E1; §12 V-6).
- **Placed by:** 13 (E3, cut-over), 14 (E2), 16 (cut-over), 12 and A1-2 (E1).

**C-PLACE** (PART-05).

```text
The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a few lines naming what was produced and where; the artifact holds the rest.
```

- **Goes, bodies:** after the handoff rule in the 53 handoff-roster bodies (§12 Other settlements, §3: 53, without GCFPE-MGMT-10); the 16 bodies that say the response "contains" the block now say "ends with" (step 18, whose verification counts 53). The four `ASK OK?` bodies take the variant in 3.2.
- **Goes, skills:** `glow-hde-pr-development` :162, at the end of the line, after the C-HANDOFF sentence (pr-relay-graph:6; §12, verifier conflict 15); `change-flow` :295; `session-relay-flowmaster` :279, after C-HANDOFF (§12, §8b O19), and `tw-flowmaster` :315 with it (step 19). `amthor-workspace-governance-audit` gains an invariant for C-PLACE (§12, §8a O21 (b)).
- The existing block-shape sentences (one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`) stay verbatim (fv-rest:25).
- **Guard anchor:** the registry's required guard G07 anchors on this text's first sentence, and its regression deletes that sentence (§12 Registry guards, masking).
- **Placed by:** 18 (E3, cut-over, same page edit as step 13), 19 (E2).

**C-DEC** (PART-06, added to `PR_IMPLEMENTATION_RESULT`).

```text
An *In-flight decisions* section, one row per decision taken without a rescope: what changed, why it was necessary to deliver the approved scope, and what was tested, by test identity and outcome. `NONE` when there were none.
```

- **Goes:** the `PR_IMPLEMENTATION_RESULT` section of PR-30, PR-35 and RS-40 (step 20). In `glow-hde-pr-development`, at SKILL.md:108, which names the result artifact, not at :59 as step 20 says (pr-relay-graph:10). `behavior-cases.md` gains a heading for it (§12, §8a O16 (b)).
- **Placed by:** step 20 (bodies E3, cut-over; skill E2).

**C-LAT** (PART-07; PR lane only).

```text
**Material** means a change to the Epic-level commitment: its outcome or objective; approved acceptance criteria; a protected architectural, security, data-model or external-contract boundary; the scope of several planned work units; an accepted dependency or cross-team commitment; or budget, schedule or risk needing Product Owner direction. A planned approach found incomplete, impractical or inferior is not by itself material.

**Decide it during work:**
1. Is it material, as above? Then take the formal rescope route.
2. Otherwise, is it obvious, necessary to deliver the approved scope, and consistent with the Epic's objective and controlling constraints? Then decide it, implement it, test it, and record it under *In-flight decisions*. That holds even if the plan did not anticipate it.
3. Otherwise, do not do it. Record it as a candidate for its owner.
```

- **Goes, bodies:** once, in the section that sends findings to RS, in PR-10, PR-20, PR-30, PR-35, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30; in those routing sentences "material boundary" becomes the step-22 literal in 3.5 (step 22). OPS-*, QA-*, CL-* and ESC-* are out of scope (step 22).
- **Goes, skills:** `glow-hde-pr-development` :65, :128, :135, placed as §8a compiles it (§12, §8a O2 (a)), with the numbered procedure :130-133 intact, and `behavior-cases.md`:49 converged (pr-relay-graph:12). `:135` stays verbatim only where §E records that it restates no reversed rule; otherwise it converges (§12 S-4). `behavior-cases.md` gains a heading for C-LAT (§12, §8a O16 (b)). `change-flow` :453-454 (step 24). `change-flow` :313 and :323 stay verbatim (child C7; §12, §8b O10), and C-LAT is placed beside them, not in them; see Unsettled U-2.
- **Graph:** step 23's condition wording is superseded by the A1-7 conditions in 3.7.
- **Placed by:** 22 (E3, cut-over), 24 (E2).

**C-VERSION** (PART-12, the release rule). Text unchanged, placed with a qualifier (§12 S-1).

```text
A release's membership and each member's current version live in the register and the complete-prompt-set catalog. A member whose body changes gets a successor page at the new version; a member whose body does not change keeps its page, and the register records it in the new release. Bodies carry no release-bound header line.
```

The qualifier, placed with C-VERSION at each of its sites (§12 S-1):

```text
It applies from the release after 091426.1; 091426.1's bodies were edited in place by `MODIFICATION-20260923-alpha-feedback-open-entries` (`D23-G`).
```

- **This run** (A1-3; §12 S-1): steps 41–43 run in this cut-over, so the bodies drop their release-bound header lines now (`D23-G`). The successor-page rule applies from the release after 091426.1: this run edits the 091426.1 bodies in place. The register records each changed member's revision date, which is informational: nothing reads it and it identifies nothing. The contract and skill revisions move, so the bytes stay distinguishable. The contract's `versioned_sibling_successors` stays `true`, because it is true of how 091426.1 was made (A1-2).
- **Goes:**
  - `prompt-body-content-policy.md` :33-34, where `Prompt version:` and `Ecosystem release:` leave the legitimate list and C-VERSION with its qualifier is added (step 41);
  - `prompt-body-content-policy.md` :88, the Enforcement line, in sweep:17's wording (step 41; §12 S-1; text in 3.5);
  - the Notion register and complete-prompt-set catalog, as the release rule with its qualifier, with a per-member `current_version` column, all `091426.1` (step 44).
- A related skill literal, `amthor-workspace-governance-audit` SKILL.md:32 narrowed to "each member that received a successor page", is spec §8 (registry-audit:16).
- **Placed by:** 41 (E1), 44 (cut-over).

**C-D22** (PART-13). §P defines it as the `D22` wording of `prompt-corpus-policy.md`, *Amendment*. The text EXECUTE places is step 45's reason:

```text
a path option invites a standing directory; a transient read file is allowed under `D22`
```

- **Goes:** at every site, the C-D22 reason replaces that site's reason clause, verbatim (§12 W-7; §12, §8b O26). The sites:
  - `flowmaster-validate` SKILL.md:231-232, replacing "a file persists, and a persisted corpus is what the policy forbids" (step 45);
  - SKILL.md:60, replacing "a file persists" in "because a file persists";
  - `scripts/validate_gcfpe_20260914.py` comment :2657-2659, replacing "a file would persist, and a persisted corpus is what the policy forbids";
  - `scripts/run_gcfpe_20260914_fixtures.py`:726, replacing "a file would persist" (fv-main:34).
- The no-path-option behaviour is kept; only its stated reason changes (fv-main:34). The docstring at :2288-2291 has no reason clause; see Unsettled U-3.
- **Placed by:** step 45 (E2).

### 3.2 Texts added or amended by Amendment 1

**C-SESSION** (PART-09), amended.

```text
PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. The phases share one `WORK_UNIT_ID`, original Proceed, workspace/worktree, branch, pull request, PR instruction, detailed plan, primary skill authority and recovery lineage; they do not share a session. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
```

- **Changes from §P** (§12 W-6): the backticks around PR-30 and PR-35 in the first sentence are dropped, so the kept literal "PR-30 and PR-35 are two phases" matches `change-flow`'s validator (:1020-1021) and `flowmaster-validate`'s `CHANGE_FLOW_CONTRACT` (:2580-2586), which §P's text fails (fv-main:26, fv-rest:17; measured). A1-8's sentence goes last.
- **Goes, bodies:** the ~17 bodies stating one shared session, replacing the continuity-list paragraph; readback: "dedicated PR-development session" is absent from every continuity list (step 32).
- **Goes, skills (step 35, sites extended by findings).** Every prose line that restates a reversed rule converges; none is left untouched (§12 S-4).
  - `glow-hde-pr-development`: description :3, and :10, :22, :27 (pr-relay-graph:2, :4), :53, :55 (pr-relay-graph:1), :82, :100, :141 (sweep:4, coverage:17), :158 (pr-relay-graph:1), :164; and `behavior-cases.md` :7, :11, :13, :17 (pr-relay-graph:15), with `behavior-cases.md`:57 converged (§12, §8a O15 (b)). The "adds no … session" lists read "any session beyond its own dedicated PR-35 session", the registry wording (§12, §8a O7 (b)); `behavioral-fixtures.md`:49 stays verbatim.
  - `change-flow`: :275, glued as "The policy for each planned PR work unit, run in two dedicated sessions, …" (§12, §8b O5 (a)); :301, :303, :307; :321, in sweep:20's wording (§12, §8b O34 (b)); :365, taking C-SESSION's second and third sentences (§12, §8b O6 (a)); :366 stays verbatim only where §E records that it restates no reversed rule, and otherwise converges (§12 S-4); :411, deleting "manual-merge-assertion " (§12, §8b O7 (a)); :450 per W-9 (3.6); :453, taking A1-1's actor cell and A1-1's PR-35 session cell (fv-rest:19, coverage:15; §12, §8b O8 (b)).
  - `session-relay-flowmaster` :283, with C-SESSION prepended to the line and "supplies merge approval" reworded to "is not a merge approval or merge instruction" (§12, §8b O20 (a), (b)); :285, converged to "resume in the recorded phase's own session" (§12, §8b O21 (b)).
  - `tw-flowmaster` :319 and :321, byte-identical to the relay's new :283 and :285 (sweep:5, A1-6).
  - `flowmaster-validate` SKILL.md :164-165, and :294, taking C-SESSION's second and third sentences (fv-main:34, coverage:15; §12, §8b O25 (a)).
  - `amthor-workspace-governance-audit` SKILL.md :40, :41, :43, :47 and `interoperability-contracts.md` :13, :18, :53-54, :68, :96 (registry-audit:13, :14).
  - C-SESSION's top-level sentence (its last) is a `CONTRACT_REQUIRED` entry for the relay and `tw-flowmaster`, with a deletion regression (§12, §8b O16 (b)).
- **Also carried by:** PR-35's role in the graph, the contract and the registry (A1-8; §12 W-1; 3.4); the GCF-17 successor row, in its own A1-1 wording.
- **Placed by:** 32 (E3, cut-over), 35 (E2).

**C-SUB** (PART-10), A1-5; supersedes §P's C-SUB.

```text
At entry, subscribe to the pull request's activity where the surface provides it, and record the subscription as active only when the tool result confirms that this session receives the pull request's events. Act on review, comment and check events as they arrive. Without an active subscription, `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. Subscribing is not polling, and it creates no session.
```

- **Goes:** the PR-35 body; RS-40's PR-35 phase (step 37). `glow-hde-pr-development`: its own sentence before SKILL.md:112, which stays verbatim (pr-relay-graph:9); :121 is also in step 37, and its edit is spec §8a's (sweep:19; see §1, Unsettled U-1). A heading for C-SUB goes in `behavior-cases.md` (§12, §8a O16 (b)).
- **Required literal** `Subscribing is not polling`, with a deletion regression, in `glow-hde-pr-development` (§12, §8a O12 (b)).
- **Guard anchor:** the registry's required guard G24 anchors on "stay subscribed and do not poll" in C-DISPATCH below (§12 Registry guards, masking).
- **Why it differs from §P:** a subscription counts as active only when the tool confirms this session receives the PR's events (A1-5; sweep:14).
- **Placed by:** 37 (bodies E3, cut-over; skill E2).

**C-DISPATCH** (PART-11), A1-5; supersedes §P's C-DISPATCH and the PART-11 ruling row's launch option.

```text
At `MERGE_PENDING`, return control with the result, including the conditional `PR-40` block for Nathan, which is usable only after he merges and only where no `MERGE_OBSERVED` result was returned for this merge; stay subscribed and do not poll. When the active subscription delivers the merge of the identified PR — a merge Nathan performs — return `MERGE_OBSERVED` with the paste-ready `PR-40` handoff and return control. Nathan creates the PR-40 session and pastes it. The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently. No agent merges, and no session is created by an agent.
```

- **Goes, bodies:** PR-35 and RS-40 (step 39). RS-40 carries it because it resumes the PR-35 phase in the same subscribed PR-35 session and gains `MERGE_OBSERVED` (A1-5).
- **Goes, skills (step 40, sites extended by findings):**
  - `glow-hde-pr-development` :110, appended after the existing sentences, never replacing them (pr-relay-graph:7); :164, removing only the manual-assertion clause and keeping the rescope sentence and PR-40's independent-verification literal (pr-relay-graph:8, coverage:16); `behavior-cases.md`:87 (pr-relay-graph:15, coverage:16), and a `MERGE_OBSERVED` heading there (§12, §8a O16 (b)).
  - `change-flow` :331; :366 (subject to §12 S-4, as above); :455 through the successor GCF-17.LINEAGE row (child C7), in §8b's text, whose words come from the fallback predicate, C-DISPATCH and A1-7's `reject_replan` condition (§12, §8b O9 (a)).
  - `session-relay-flowmaster` :283-285 and `tw-flowmaster` :319-321, as under C-SESSION (sweep:5).
  - `flowmaster-validate` SKILL.md:173 (fv-main:34, coverage:15).
  - `amthor-workspace-governance-audit` SKILL.md:49 and `interoperability-contracts.md`:74, keeping "MERGE_PENDING is historical", PR-40's independent verification and no-merge (registry-audit:13, :14); plus a `MERGE_OBSERVED` acceptance fixture (§12, §8a O21 (b)).
  - Required literal `no session is created by an agent`, with a deletion regression, in `glow-hde-pr-development` and in `change-flow`'s validator (§12, §8a O12 (b); §12, §8b O16 (b)).
- **Guard anchors:** the registry's required guards G24 and G25 anchor on "stay subscribed and do not poll" and "The observed merge event is the fact PR-40 is entered on"; each regression deletes that sentence (§12 Registry guards, masking).
- **Placed by:** 39 (E3, cut-over), 40 (E2).

**C-TOP** (A1-8), new.

```text
This prompt runs in a top-level session that Nathan creates, or re-enters by pasting a handoff, and never as a subagent of another session. It may use subagents as workers within its own task. It never creates, starts or schedules another session; it returns control, with the handoff where there is one.
```

- **Goes:** the 54 main-ecosystem bodies, every GCFPE body except GCFPE-MGMT-10, beside the handoff or return rule. For the 53 handoff-roster bodies it is placed with the step-18 edit; PR-50 has no handoff, so it gets a separate edit beside its return rule (A1-8, coverage:27). No C-TOP text goes into `glow-hde-pr-development` (§12, §8a O13 (a)).
- **Carries the rule for PR-20 and PR-40,** whose roles stay unchanged (§12 W-3).
- **Wording note:** the last sentence says "starts", not "launches", so the forbidden session-creation guard does not match the canonical text itself (sweep:1; coverage:0; measured below).
- **Placed by:** A1-8, computed at E3, landed at cut-over.

**GCFPE override** (A1-6), new.

```text
For every GCFPE main-ecosystem stage, the core's option to create a fresh session does not apply: this skill never creates, spawns, launches or schedules a session; when no existing authoritative session can do the work, it returns the paste-ready `NEXT_PROMPT_HANDOFF` and stops for Nathan.
```

- **Goes:** in each skill's specialization text outside the byte-identical Flowmaster core, which is left unchanged (A1-6; sweep:6). Positions (§12, §8b O1 (a)):
  - `change-flow`: a new paragraph after `:263`;
  - `session-relay-flowmaster`: after `:255`;
  - `tw-flowmaster`: the first paragraph under `### GCFPE binding`.
- **Held by:** a `CONTRACT_REQUIRED` entry holding the whole text, so any edit fails (§12, §8b O3 (a)).
- **Session-creation guards and skill text:** no session-creation regex applies to skill text. `CONTRACT_FORBIDDEN` entries are exact phrases, and each is tested against this override and the governance-audit invariant (§12 Other settlements, §3). The relay and `tw-flowmaster` take the same four `CONTRACT_FORBIDDEN` phrases, each with a must-fail regression (§12, §8b O4 (b)).
- **Placed by:** A1-6, at E2.

**C-PLACE, `ASK OK?` variant** (§12 W-5). It is C-PLACE verbatim, then one sentence restating §P step 18's instruction:

```text
The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a few lines naming what was produced and where; the artifact holds the rest. `ASK OK?` is the line immediately before the block.
```

- **Goes:** QA-60, QA-80, RS-10 and RS-30, in place of C-PLACE, with the body's `ASK OK?` line moved to the line immediately before the block (step 18).
- **Guard** (§12 W-5), both parts:
  - a required pattern on the sentence "`ASK OK?` is the line immediately before the block.", with a regression that deletes it;
  - G08's forbidden old wording (the second pattern below).
- **Recorded in §E:** ordering in the *output* can be checked only on outputs (§12 W-5).
- **Constraints it meets (measured):** it still matches the placement guard (first pattern below), and it does not reuse "end `ASK OK?`", so the forbidden pattern (second) stays silent (registry-audit:12 and its notes):

```text
ends with the `?NEXT_PROMPT_HANDOFF`? block
\bends? `ASK OK\?`
```

### 3.3 Texts from the follow-up plan

**C-REPLAN** (replaces *PRECISE IN-SCOPE DEFECT → existing PR owner* in PR-40).

```text
**PRECISE IN-SCOPE DEFECT → re-plan.** When the landed work has a precise in-scope implementation, review, corrected-code or PR-lineage defect, return `REJECT` with the finding in `PR_WORK_UNIT_LINEAGE_REVIEW`, and hand off to `PR-20` for a new per-PR plan for the same `WORK_UNIT_ID`. PR-20 runs in a new dedicated top-level session that Nathan creates and seeds with this handoff; no session is created automatically. That plan goes through its own Product Owner Proceed, then PR-30, PR-35 and PR-40 again. The earlier Proceed is spent and is never reused.
```

- **Goes:** the PR-40 body, replacing the existing-PR-owner branch; the body names PR-20 and keeps "historical pre-merge", "independent" and `glow-merged-change-attribution-lock` (C4; fv-main:33).
- **Placed by:** C4 (E3, cut-over).

**C-PROCEED** (the single-Proceed rule, restated).

```text
One Proceed per approved per-PR plan. A continuation — PR-30 to PR-35, a rescope return, a recovery — never requires or creates a second Proceed. Only a PR-40 `REJECT` re-plan creates a new plan, and that plan receives its own Proceed.
```

- **Goes, bodies:** every body that carries the single-Proceed sentence, replacing it (C4). The body rules script anchors on that sentence and reports every body it edits; §E lists them, and E4 checks them (§12 Other settlements, §3).
- **Goes, skills:**
  - `glow-hde-pr-development` :10, :17-18, :27, one combined replacement per line with step 35 at :10 and :27 (C6); `:17` loses "original" (§12, §8a O3 (a)). The new required literal taken from C-PROCEED is §8a's O9 (a) value; the old continuity lists and "ten-field" are forbidden, each with a regression (§12, §8a O9 (a), O10 (b)). The forbidden entry `followed in the same session by PR-35`, with regression R-C6-27, guards the old `:27` sentence (coverage:21).
  - `change-flow`, as its own sentence after :301, with :313 and :323 verbatim (C7; sweep:22; §12, §8b O10), and a required literal in `change-flow`'s validator with a deletion regression (§12, §8b O16 (b)).
  - `amthor-workspace-governance-audit` SKILL.md:44, "one Proceed per plan cycle" (C10), with a re-plan fixture (§12, §8a O21 (b)).
- **Placed by:** C4 (E3, cut-over); C6, C7, C10 (E2).

**C-PR20-ENTRY** (added to PR-20's entry).

```text
**Re-plan entry.** This prompt also accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` whose result is `REJECT` (`reject_replan`) for an existing `WORK_UNIT_ID`. It then runs in a new top-level session that Nathan creates, plans that work unit again from the landed state and the finding, and ends at a new `AWAITING_PO_PROCEED` for the new plan. A pull request merged under an earlier plan cycle is landed history: never resume, reuse or push to it.
```

- **Goes:** the PR-20 body's entry (C4). Its opening is the `CTR-002` guard's target (C5).
- **Placed by:** C4 (E3, cut-over).

**C-PR30-ENTRY** (replaces PR-30's PR-40 return context).

```text
PR-30 starts only from the Proceed of its own plan. A PR-40 finding never returns here directly; it re-plans through PR-20 (`D23-F`).
```

- **Goes:** the PR-30 body, replacing its PR-40 return context (C4).
- **Placed by:** C4 (E3, cut-over).

### 3.4 Role strings and registry literals

**PR-35 `session_class`** (steps 30, 33):

```text
DEDICATED_PR_REVIEW_SESSION
```

The schema enum doc at `project-prompt-registry-schema.md:42` gains this class, in the fifth package (§12 S-8).

**PR-35 role** (§12 W-1). Step 30's sentence followed by A1-8's clause, verbatim. One string goes to four places: graph `PR-35.json` `node.receiving_role` (step 30, E1); contract `member_registry['PR-35'].receiving_role` in both copies, set by the regenerator from the graph (A1-2; fv-main:8); and registry PR-35 `session_role`, equal to the graph string verbatim and single-quoted in YAML if needed (registry-audit:7).

```text
You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
```

Its guard phrase, shared by the registry role-parity check and the new `flowmaster-validate` check on `member_registry['PR-35'].receiving_role` (§12 W-1; verifier unplaced 2):

```text
never as a subagent, forked agent or workflow agent of PR-30
```

**PR-35 registry fields besides the role** (step 33; registry-audit:7 and its notes). `creator_role`:

```text
The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.
```

The new input (step 33, with the wording of registry-audit:7's notes), written as a quoted YAML string so it does not parse as a mapping (registry-audit:7):

```text
session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID
```

The forbidden-additions line, which keeps guarding against a third session instead of dropping the word "session" (registry-audit notes, step 33):

```text
Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session
```

**RS-40 role** (§12 W-2; registry-audit:9, coverage:18). Graph `RS-40.json` `node.receiving_role` and registry `session_role` change together, from "You are the same dedicated PR engineering session for the exact suspended work unit.", and the regenerator mirrors the graph string into `member_registry['RS-40'].receiving_role` (§12 W-2; verifier conflict 16):

```text
You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.
```

RS-40's registry `creator_role` (§12 W-2):

```text
the recorded phase's own dedicated session for the exact suspended work unit.
```

RS-40's `session_class` `DEDICATED_ONE_OFF` is left unchanged, and §E records it as a pre-existing inaccuracy out of scope (§12 S-9).

**PR-20 and PR-40 roles stay unchanged** (§12 W-3). Body-level C-TOP and its guards carry the rule for them. The `D23` clarification's *Guard* paragraph is corrected to match (text in 3.6).

**PR-20 registry input** (C5), as a quoted string, without backticks, following the registry's convention (§12 Registry guards):

```text
PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the same WORK_UNIT_ID in a new dedicated session Nathan seeds
```

**PR-40 registry inputs.** At :3708, "the dedicated PR session identity" becomes (registry-audit:9, coverage:18):

```text
the PR-30 and PR-35 session identities
```

**PR-40 entry wording** (§12 W-4). The same string goes in the PR-40 body's entry and in the registry input at :3710. The registry's `D23-E` guard on PR-40 reads it (registry-audit:12; coverage:1; sweep:2; adversary:4):

```text
PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.
```

PR-40's PR-35-result input at :3705 becomes (§12 W-4):

```text
The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.
```

**`MERGE_OBSERVED` in the registry's `outputs[].states`** for PR-35 and RS-40 goes in ASCII order, because those lists are sorted, which puts it before `MERGE_PENDING`. Everywhere else it goes in A1-5's order (§12 V-12).

**Governance-audit invariant** (A1-8's semantic invariant, added to the fifth package; wording sweep:25). A bullet in `amthor-workspace-governance-audit` SKILL.md's Alpha-feedback invariants list (:36):

```text
Every main-ecosystem prompt (all but GCFPE-MGMT-10) runs as its own top-level session Nathan creates; none runs as a subagent, forked or workflow agent; none creates, launches or schedules a session; workers within a task are allowed.
```

- Its parenthetical stays accurate under the triage successor: the *Modification Intake and Triage* prompt is not a registry member, and nothing in Amendment 1 changes for it (`D23` successor, triage).
- `CONTRACT_FORBIDDEN`'s exact phrases are tested against this text (§12 Other settlements, §3).

### 3.5 Literals fixed by individual steps

These are not C-texts, but each is placed verbatim.

**Step 2** — C-NOTION in the relay's list form, replacing `session-relay-flowmaster` SKILL.md:268 (E2). :269 is out of scope.

```text
Notion holds the published prompt bodies and the maintenance surfaces a destination rule names; live task, handoff and decision state lives in the repository under `docs/ephemeral/`
```

**Step 4** — QA-10, replacing "Notion and repository persistence" at all 6 occurrences (E3, cut-over).

```text
repository persistence, Notion read-only unless a destination rule names the page
```

**Step 6** — Notion, HDE Change Flow Overview § *CRD Alpha Test 1 — manual run tracking*, as a prefix (cut-over).

```text
Historical — Alpha Test 1 is complete (2026-09-07). Not current guidance.
```

**Step 9** — Notion, Hub § *Prompt ecosystem worker output standard*, replacing "it goes in the correct numbered section of the handoff or the artifact" (cut-over).

```text
it goes in the artifact, and the handoff names the artifact
```

**Step 16** — Notion, Hub § *Handoff format — required structure*, after C-HANDOFF (cut-over).

```text
sections the artifact already holds are named, not repeated
```

**Step 22** — the C-LAT bodies, replacing "material boundary" in the routing sentences that send findings to RS (E3, cut-over).

```text
material change (as defined above)
```

**Step 26** — registry :3531, as a list item (E1).

```text
Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35
```

**Step 27** — `glow-hde-pr-development` SKILL.md:79 (E2).

```text
Bundle related implementation changes into one locally verified push when practical.
```

**Step 36** — Notion, register § *Current explicit membership* and Flow Index § *Native flow changes*, replacing "same-session PR-35" (cut-over).

```text
PR-35 in its own dedicated session
```

**C11** — Notion, Flow Index, appended to "It is not restarted or duplicated by … a new session" (cut-over).

```text
except a PR-40 `REJECT` re-plan, which is a new plan with its own Proceed (`D23-F`)
```

**Step 41, `:88`** — `prompt-body-content-policy.md:88`, the Enforcement line's requirement clause for `prompt_identity_header_valid`, in sweep:17's wording (§12 S-1; E1):

```text
requires identity — title, `Prompt ID:`, exactly one `Notion URL:` line whose page identity matches the registry binding; rejects `Prompt version:`, `Set:` and `Ecosystem release:` in the header window as `PROMPT_BODY_RELEASE_HEADER` (D23-G)
```

### 3.6 Texts settled by §12

**Documentation and decision-record texts, E1** (§12 S-2, W-3).

- **N1**, a new key `body_identity_disposition` under `body_extraction_convention` in the registry. It states that the `evidence_contract` and `source_snapshot` identities describe the bodies before `D23` and no longer identify them (§12 S-2). §12 gives its content, not its string; see Unsettled U-4.
- **`authoritative-surfaces.md:59`** is corrected to match N1. Its token lines `:29` and `:45-46`, and `ecosystem-change-management.md:143`, are labelled with this phrase, not restated (§12 S-2):

```text
as measured before `D23`
```

- **N2**, `ecosystem-change-management.md:141` (§12 S-2):

```text
`required_regex` binds the Canon source and the `D23` canonical wordings; `forbidden_regex` guards `D7`, the `D23` reversals and session creation.
```

- **`ecosystem-change-management.md:176`** becomes (§12 S-2):

```text
carried, until `D23-G` removed them,
```

- **`execution-and-delegation-model.md`** gains the scope line in the `D23` clarification's words (§12 S-2). S-2 cites this as §3 open question 13; in v1 it is question 9, and question 13 is relay `:624`, which S-6 settles.

```text
its subagents are maintenance workers, and never a way to run a main-ecosystem prompt
```

- **The `D23` clarification's *Guard* paragraph** is corrected to say (§12 W-3):

```text
PR-35's graph, contract and registry role, and every main-ecosystem body (C-TOP).
```

**Relay and `change-flow` lines, E2** (§12 S-6, S-7, W-9).

- **Relay `:624`** gains (§12 S-6):

```text
A runtime handoff still names its destination by full name, version and direct Notion URL (C-HANDOFF); `NOTION_REFERENCE` stays versionless for reusable prompt text.
```

- **Relay `:353` and `:372`:** `CONTROL_PLANE` keeps its enum, and each line gains (§12 S-7):

```text
`NOTION` means a maintenance surface that a destination rule names; live task, handoff and decision state lives in the repository.
```

- **`change-flow:450`** becomes the line below. The old imperative joins the retired-phrase list, which is matched case-insensitively (§12 W-9; §12, §8b O15 (b)):

```text
GCF-14 — Nathan creates one dedicated top-level PR session for one planned PR work unit.
```

- **Relay `:255` and `:713`** are scoped to non-GCFPE exchanges, and after `:255` the relay gains (§12 W-9; §12, §8b O2 (b)):

```text
For a GCFPE main-ecosystem stage, return the paste-ready `NEXT_PROMPT_HANDOFF` and stop for Nathan; provisioning does not apply.
```

- **`glow-hde-pr-development:173`** drops "hidden ", so "Do not create hidden sessions" reads "Do not create sessions" (§12 W-9; §12, §8a O14 (b)).

**Contract-only texts, set at E1 through the regenerator** (§12 W-8). Each changed value gets an exact-value check with a must-fail regression (§12 W-8).

- **`route_graph_semantics.same_session_phase_continuation`** is renamed `pr30_to_pr35_phase_continuation`, with the value:

```text
PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent.
```

- **`route_graph_semantics.pr40_entry`** becomes the W-4 sentence in 3.4:

```text
PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.
```

- **New key `route_graph_semantics.pr40_reject_replan`:**

```text
A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new Proceed for the new plan (D23-F).
```

- **`pr_development_contract.pr30_ownership[5]`:**

```text
complete PR-35 handoff to the dedicated PR-35 session
```

**Graph and contract strings owned by §4 and §6, quoted here for completeness.**
- **Handoff contract lists** (§12 W-10). `handoff_contract.required` keeps "exact selected prompt full name/version/direct Notion URL" and "receiving role and exact session", and adds "input artifact repository paths with one-line labels", "pull request reference when the receiver continues an existing PR" and "minimum exceptional context only for a condition the artifacts do not record". `handoff_contract.prohibited` gains "branch", "commit" and "restated artifact content", appended in that order.
- **`transition_contract.prohibited_references`** gains, in this order: "branch", "commit", "restated artifact content", "menu", "metadata-only summary", "blank form" and "placeholder after publication" (§12 V-6).
- **PR-35's `native_function`** gains this clause before its final period (§12 V-8):

```text
; return MERGE_OBSERVED when an active subscription observes Nathan's merge
```

- **`event_2`** (§12 V-3): `actor` "Nathan / Product Owner"; `fact` "product_owner_manual_merge_observed_or_asserted"; `value` `true`; `time`:

```text
observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge
```

- **`receiver_compatibility.PR-40.entry_fact`** (§12 V-4):

```text
MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED
```

### 3.7 Graph conditions (A1-7, including the follow-up's three rows)

The authority for the full edge objects and insertion positions is `route_sim_final.py`, sha256 `e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26` (A1-7). The 15 condition strings, read from its constants, each equal the A1-7 table's *after* cell verbatim (measured). They are A1-7's 15 rows: 13 changed and 2 new edge rows; the 7 state-route rows follow from them (§12 V-11). Keys name the part and branch:

```json
{
 "PR-10/material_boundary": "a material change to the Epic-level commitment (D23-C) is substantiated",
 "PR-20/material_boundary": "the planning result substantiates a material change to the Epic-level commitment (D23-C)",
 "PR-40/reject_material_boundary_proposal": "a substantiated material change to the Epic-level commitment (D23-C) requires a new bounded rescope proposal",
 "DOC-10/material_boundary": "repository evidence proves a complete bounded material change to the Epic-level commitment (D23-C)",
 "PR-30/pr_candidate_published": "one complete PR-35 handoff to the dedicated PR-35 session for the same work unit and pull request",
 "RS-40/recovery_pr30": "recorded resumed phase is PR-30_POSTPUBLICATION; PR-30 session/vehicle re-entry",
 "RS-40/recovery_pr35": "recorded resumed phase is PR-35; PR-35 session/vehicle re-entry",
 "PR-35/merge_pending": "conditional PR-40 invocation for Nathan, usable only after he manually merges and only where no MERGE_OBSERVED result was returned for this merge",
 "RS-40/merge_pending": "recorded PR-35 phase result; historical pre-merge evidence; its conditional PR-40 invocation is usable only where no MERGE_OBSERVED result was returned for this merge",
 "PR-20/awaiting_po_proceed": "one complete executable approved-scope plan awaits the Product Owner Proceed for that plan",
 "_other_edges original_proceed = boundary_transitions.NATHAN_PROCEED": "the explicit Proceed for the exact approved per-PR plan; never a second Proceed for the same plan",
 "_other_edges manual_merge_then_lineage_review = boundary_transitions.NATHAN_MANUAL_MERGE_ASSERTION": "Nathan has manually merged the identified PR, no MERGE_OBSERVED result was returned for this merge, and he invokes the conditional PR-40 block",
 "PR-35/merge_observed (new edge to PR-40)": "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
 "RS-40/merge_observed (new edge to PR-40)": "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
 "PR-40/reject_replan (edge to PR-20, was reject_existing_pr_owner to PR-30)": "a precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed"
}
```

Placed by: steps 23, 31 and 38 as amended by A1-7, and child C1 and C2, at E1. The `NATHAN_PROCEED` condition exists in two copies in `global.json`, `_other_edges` and `boundary_transitions`, and both take the same string (child C2). The two new edges take indices 128 and 129 (§12 §4 OQ-10). The GCF-17, GCF-17.LINEAGE and GCF-14 successor text is A1-1's table and is not repeated here.

### 3.8 Check

**v1's check, still valid for the texts it covered.** A scratch script (`/tmp/claude-0/spec/section3/check.py`, run with `PYTHONDONTWRITEBYTECODE=1`) read the texts out of the plan, amendment and follow-up copies (`extract.py`), not from this section. It read the forbidden list from the installed `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py` (:91-103, 11 entries) and applied it as that validator does: a case-insensitive substring test.

```text
texts checked: 59
  18 canonical (3.1-3.3, the ASK OK? variant and the C-D22 reason)
  11 role and registry strings (3.4, including both PR-35 options, step 30's original PR-35 string
     and the PR-40 :3710 preflight wording)
  10 step literals (3.5), 15 graph conditions (3.6), 5 A1-1 successor-row fragments
hits, validator forbidden list:                             0
hits, 'when a denial requires correction':                  0
hits, full PR-20 regex (validate_gcfpe_artifact_timing.py:76): 0
hits, PR-20 future-revision string (same file, :78):         0
hits, entries C6 and findings propose adding to the list:   0
  (C6 'followed in the same session by PR-35'; old literals at validator :32, :37, :38, :44, :55, :63)
C-SESSION final contains 'PR-30 and PR-35 are two phases':  True  (§P form: False)
code blocks in 3.1-3.6 equal to the extracted strings:       all (round-trip)
artifact-timing body checks, all 59 texts as PR-10..PR-50, RS-10, RS-30, QA-10, QA-60, QA-80 bodies: []
```

The PR-35 role adopted by §12 W-1 (v1 option (b)) and the RS-40 role adopted by §12 W-2 were among those 59 texts. In v1's check, each guard pattern the findings propose was run against these texts. Every required pattern matched its home text and no other canonical text: C-ART, C-DEC, C-LAT (two patterns), C-PLACE and its variant, C-SESSION (two), C-TOP, C-SUB, C-DISPATCH (two) and C-PR20-ENTRY. Every proposed forbidden pattern was silent on all 59 texts and on the C-PLACE + C-HANDOFF, C-PLACE + C-SESSION and C-PLACE + C-HANDOFF + C-SESSION + C-TOP combinations. The only matches came from the first draft's withdrawn session-creation pattern, below, on two skill texts: the A1-6 override and the governance-audit invariant. No session-creation regex applies to skill text, and `CONTRACT_FORBIDDEN`'s exact phrases are tested against both texts instead (§12 Other settlements, §3).

```text
\b(?:launch|spawn|auto-?start)\w*\b[^.\n]{0,60}\bsession\b
```

**Added for v2: the texts §12 introduced.** It was run in memory for v2 (`python3 -B`, nothing written), over the 22 distinct code-block texts in this section that v1 did not hold: the S-1 qualifier, the W-1 guard phrase, the W-2 `creator_role`, the PR-20 input without backticks, the two W-4 texts, the step-41 `:88` text, the S-2 texts, the W-3 *Guard* text, the S-6, S-7 and W-9 lines, the W-8 texts, and the V-3, V-4 and V-8 strings.

```text
source of each new text:  21 verbatim in §12, the D23 clarification or sweep:17's fix;
                          1 (PR-20 input) equal to v1's text with its backticks removed
hits, validator forbidden list (11 entries, case-insensitive): 0
hits, 'followed in the same session by PR-35':                 0
hits, 'when a denial requires correction':                     0
hits, withdrawn session-creation pattern:                      0
masking anchors, occurrences in each home text:
  G07 'The final response ends with the `NEXT_PROMPT_HANDOFF` block.'   1 (C-PLACE), 1 (ASK OK? variant)
  G24 'stay subscribed and do not poll'                                 1 (C-DISPATCH)
  G25 'The observed merge event is the fact PR-40 is entered on'        1 (C-DISPATCH)
ASK OK? sentence present only in the variant:                            True
v1 §3 code blocks kept byte-identical: 40 of 42; the other two are the void PR-35 option (a)
  and the backticked PR-20 input that §12 replaced
```

### Unsettled

- **U-2. Where C-LAT (and step 14's field-list clause) goes in `change-flow`.** §12 keeps `:313` and `:323` verbatim (child C7; §8b O10), which is v1 §3 open question 12's option (a): C-LAT and C-HANDOFF are placed beside those lines. Neither §12 nor §8b fixes the position beside them, or whether C-LAT at `:453`–`:454` (step 24) also falls under that choice.
- **U-3. The C-D22 docstring at `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2288`–`:2291`.** W-7 replaces each site's reason clause with the C-D22 reason. The docstring has no reason clause, so W-7 has nothing to replace there. §12 does not say whether C-D22 is added to it or the docstring is left unchanged.
- **U-4. The strings for N1 and `authoritative-surfaces.md:59`.** §12 S-2 fixes N1's key, position and content, and says `:59` "is corrected to match", but gives no string for either.
- **U-5. The frame of the `execution-and-delegation-model.md` scope line.** §12 S-2 places it "in the `D23` clarification's words", which are the phrase in 3.6. Its lead-in, capitalisation and position in the file are not given.
- **U-6. Order of the two new relay texts after `:255`.** The GCFPE override goes after `:255` (§8b O1 (a)), and W-9's provisioning sentence also goes after `:255`. §12 does not say which comes first.

§1's Unsettled U-1 (`glow-hde-pr-development:121`) also bears on C-SUB in 3.2.

## §4 Graph transforms

This section lists every edit EXECUTE makes in `/home/user/glow-hdengine-v2/docs/graph/parts`. It compiles:
- original steps 12, 23, 29, 30, 31, 34 and 38 (§P);
- amendment rulings A1-1, A1-2, A1-5, A1-7 and A1-8;
- the follow-up plan's C1 and C2;
- the `D23` successor note "Amendment 1 approved" in `docs/prompt_ecosystem_management/gcfpe.decision-record.md`;
- the §12 decisions, applied inline and cited by their §12 id;
- the findings cited on each item.

Every literal is fixed. Where v1 left a choice, only the value §12 chose appears here. The few points §12 does not settle are listed in §4.12.

**Files edited:** `global.json` and seven prompt parts, `PR-35.json`, `RS-40.json`, `PR-40.json`, `PR-20.json`, `PR-30.json`, `PR-10.json` and `DOC-10.json`. The other 48 prompt parts are not edited. `PR-20.json` and `PR-40.json` take routing edits only; their roles stay (§12 W-3).

### 4.1 Rules for the transform

1. **Scripted, never by hand.** Every edit is made by a scripted JSON transform (§P step conventions).
2. **Serialization.** Every file the transform writes is UTF-8, in exactly this form:
   ```
   json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
   ```
   Measured: this is the simulation's `save()`, and `graph_parts.py split` uses the same writer. It reproduces all 56 current part files byte for byte.
3. **Authority.** A1-7 makes the simulation's sha256 "the authority for the full edge objects and insertion positions". So the routing portion of the final parts must equal the simulation's `parts_new` output exactly. V3 in §4.10 checks this. The routing digest alone does not, as the negative controls in §4.10 show.
4. **Completeness.** A1-7 calls its table "the complete diff" of routing, so no route condition outside §4.6 changes. §4.5 lists the conditions and roles that stay for that reason.
5. **Where the parts land: two commits on the execution branch** (A1-4, step 1; §0; §12 §4 OQ-1).
   - **Commit 1, stage E1:** every edit in this section except G16.
   - **Commit 2, stage E2:** G16 alone, written once the successor oracle exists (§5.11).

### 4.2 The simulation, reproduced

The authority file is committed at `/home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/route_sim_final.py`. It is byte-identical to the scratch copy v1 cited (`/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/route_sim_final.py`). Measured sha256 of both:
```
e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26
```
What it does:
1. It copies the parts.
2. It applies the A1-7 conditions, the child's in-place re-target and both `MERGE_OBSERVED` additions.
3. It builds base and new graphs with `glow-graph-contract/scripts/graph_parts.py build`.
4. It computes `routing_surface` with `flowmaster-validate/scripts/validate_gcfpe_20260914.py`.

It was rerun for this v2 on a copy. The copy differs only at line 10, the `W` path (`diff` shows that one line and nothing else):
```
mkdir -p /tmp/claude-0/v2work
cp /home/user/glow-hdengine-v2/docs/ephemeral/modifications/evidence/route_sim_final.py /tmp/claude-0/v2work/route_sim_final.copy.py
sed -i 's#^W = ".*"$#W = "/tmp/claude-0/v2work/routesim"#' /tmp/claude-0/v2work/route_sim_final.copy.py
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/claude-0/v2work/route_sim_final.copy.py
```
Output, measured 2026-09-23, with exit 0 and no builder `WARNING` lines:
```
BASE build: 55 nodes, 227 edges, 55 state_routes |        embedded JSON 569835 bytes  sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223 |        validation PASS -> /tmp/claude-0/v2work/routesim/graph_base.md ('7380cd14430777675f1e8b2cdfa4a0da', 282)
NEW  build: 55 nodes, 229 edges, 55 state_routes |        embedded JSON 574175 bytes  sha256 b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7 |        validation PASS -> /tmp/claude-0/v2work/routesim/graph_new.md ('fecc319bdd4ce7ee6201cb77d7231861', 284)
state_routes keys changed: ['DOC-10', 'PR-10', 'PR-20', 'PR-30', 'PR-35', 'PR-40', 'RS-40']
edge count 227 -> 229
```
**Reproduced exactly:** routing surface `fecc319bdd4ce7ee6201cb77d7231861` over 284 rows, 229 edges, and an embedded graph of 574175 bytes with sha256 `b1911cf5…`. These are the values Nathan approved in the `D23` successor note.

**Row accounting: 15 edge rows** (§12 V-11). This was measured by recomputing the `routing_surface` rows of both builds. There are 282 rows before and 284 after:
- 20 rows exist only before: 13 edge rows and 7 state-route rows.
- 22 rows exist only after: 15 edge rows (13 changed edges and 2 new ones) and 7 state-route rows.
- The 7 state-route rows belong to DOC-10, PR-10, PR-20, PR-30, PR-35, PR-40 and RS-40.

A1-7's prose "16 route rows change or are added" is corrected to 15, which is what its own table lists and what was measured (§12 V-11; verifier conflict 8). The digest reproduces, so A1-7's stop rule is not triggered.

**What 574 175 bytes / `b1911cf5…` identifies: the routing-only checkpoint** (§12 V-10). The simulation applies none of the non-routing edits: G5, G6, G8–G10, G14–G16 in §4.3, and P35-6 to P35-10 and R40-8 in §4.4. Those edits leave the digest and the edge count unchanged but change the embedded bytes, for two reasons:
- `routing_surface` reads only `edges` and `state_routes`;
- the builder derives `state_routes` only from the edges, `state_route_order` and `state_routes_extra`, which is empty in every part.

Measured in v1: adding only the fixed-value PART-09 edits (G8–G10, P35-6, P35-8 and P35-9) gives 229 edges and 574112 bytes, with sha256 `26093c3a41581979f5b4fc617a8e72d05ca6873997e47fb63bebed3b6189078c`. The digest stays `fecc319b…`/284.

**Measured for this v2: the whole commit-1 state.** Every E1 edit of §4.3 and §4.4 was applied, with the §12 values, to a copy of the simulation's `parts_new` (`/tmp/claude-0/v2work/nonrouting.py`, writing only under `/tmp/claude-0/v2work/parts_final`). `protected_identities.r1_oracle_sha256` was left at `52807e58…`, as in commit 1. The build gave:
```
build: 55 nodes, 229 edges, 55 state_routes |        embedded JSON 575074 bytes  sha256 716c4cfc8058c177f28c8405b8e3fb9fa6b1ddf9f6c5832ad338d169fe932947 |        validation PASS
routing_surface -> ('fecc319bdd4ce7ee6201cb77d7231861', 284)
```
G16 then replaces one 64-hex value with another, so the final embedded graph keeps 575 074 bytes but takes a new sha256. EXECUTE measures and records the final bytes and sha256 at E2 (§12 V-10). They are never 574 175 / `b1911cf5…`, which stays the routing-only checkpoint.

### 4.3 `global.json`: field-level edits

**G1. `_other_edges[1].condition`, the merge-assertion boundary → PR-40.** Source: A1-7; A1-5's fallback wording. New value:
```
Nathan has manually merged the identified PR, no MERGE_OBSERVED result was returned for this merge, and he invokes the conditional PR-40 block
```
Every other key of this edge is unchanged. The full object is E2 in §4.6.

**G2. `boundary_transitions.NATHAN_MANUAL_MERGE_ASSERTION[0].condition`.** It takes the same string as G1. The builder does not reconcile the two copies (pr-relay-graph:26, pr-relay-graph:27), and the routing digest does not read this copy (N2 in §4.10).

**G3. `_other_edges[2].condition`, the Proceed boundary → PR-30.** Source: child C2 and A1-7; fv-rest:28, pr-relay-graph:26. `branch_id` stays `original_proceed`, because A1-7 changes only the condition. New value:
```
the explicit Proceed for the exact approved per-PR plan; never a second Proceed for the same plan
```

**G4. `boundary_transitions.NATHAN_PROCEED[0].condition`.** It takes the same string as G3. Child C2: "Both `global.json` copies must be identical."

**G5. `handoff_contract.required`.** Source: step 12 and §12 W-10. A1-2 governs the contract's `transition_contract`, not this list. The list keeps its two surviving strings and adds three, in this order. The three items "Epic/change and work unit", "status, completed work, …" and "next action and expected output", and the old artifact item, leave the list (pr-relay-graph:31). New value:
```json
[
  "exact selected prompt full name/version/direct Notion URL",
  "receiving role and exact session",
  "input artifact repository paths with one-line labels",
  "pull request reference when the receiver continues an existing PR",
  "minimum exceptional context only for a condition the artifacts do not record"
]
```
The value it replaces, for reference:
```json
[
  "exact selected prompt full name/version/direct Notion URL",
  "receiving role and exact session",
  "Epic/change and work unit",
  "artifact repository paths, direct Notion URLs where the artifact is Notion-resident, and repository/PR references",
  "status, completed work, decisions, constraints, unresolved items, preserved authority",
  "next action and expected output"
]
```

**G6. `handoff_contract.prohibited`.** Source: step 12 and §12 W-10. The nine current entries stay in order, and these three are appended, in this order:
```
branch
commit
restated artifact content
```
New value:
```json
[
  "menu",
  "metadata-only summary",
  "blank form",
  "placeholder after publication",
  "Library ID",
  "unlinked filename",
  "above",
  "conversation reconstruction",
  "model/strength/reasoning/eligibility/suitability/account/configuration route",
  "branch",
  "commit",
  "restated artifact content"
]
```
This graph list must be a subset of the contract's `transition_contract.prohibited_references`, which the §6 subset check enforces (§12 V-6).

**G7. The other `handoff_contract` keys stay unchanged:**
- `complete_paste_ready_prompt` stays `true` (step 12).
- `actual_branch_only` `true`, `fence_language` `"text"`, `first_line` `"NEXT_PROMPT_HANDOFF"` and both block counts are kept (pr-relay-graph:31).

`GRAPH_HANDOFF_CONTRACT_MISMATCH` reads only these keys, so G5 and G6 do not affect graph–contract parity. The contract side belongs to A1-2 and §6 (fv-main:17, fv-rest:13, coverage:12, adversary:3).

**G8. `pr_continuity_contract.shared_exactly_one`.** Source: step 29; C-SESSION ("they do not share a session"). The transform removes exactly the entry `"dedicated PR-development session"` and keeps the other nine in order. Result:
```json
[
  "WORK_UNIT_ID",
  "original Product Owner Proceed",
  "workspace/worktree",
  "branch",
  "pull request",
  "PR instruction",
  "detailed PR plan",
  "primary skill authority",
  "continuous recovery/artifact lineage"
]
```

**G9 and G10. `pr_continuity_contract.adds`.**
- The graph key is `adds`. Step 29's `added_boundaries` is the contract's name for it, and no `added_boundaries` key is written into the graph (fv-main:2, pr-relay-graph:28).
- **G9:** `session` goes from 0 to 1 (step 29).
- **G10:** `cross_session_route` goes from 0 to 1 (§12 V-1; fv-rest:15, pr-relay-graph:28). The PR-30 → PR-35 handoff now crosses sessions. fv-main:2 is superseded in this part only, and its negative fixture becomes the one that sets `cross_session_route` to 0 (§6, §8b).
- The nine other keys stay 0 (fv-main:2, fv-rest:15).

Result:
```json
{
  "approval": 0,
  "cross_session_route": 1,
  "duplicate_work_vehicle": 0,
  "merge_authority": 0,
  "proceed": 0,
  "product_owner_gate": 0,
  "r1_row": 0,
  "role": 0,
  "session": 1,
  "work_unit": 0,
  "work_vehicle": 0
}
```
The contract's `added_boundaries` and `PR35_ADDED_BOUNDARY` carry the same map (§12 V-1; §6).

**G11. `proofs["PR-35_same_r1_row_as_PR-30"]` stays `true`** (step 29: "same R1 row, new session"). `pr_continuity_contract.r1_row` stays `"GCF-17"`.

**G12. `post_merge_three_event_contract.direct_PR35_to_PR40_automatic_edge` stays `false`** (A1-5; the `D23` successor note "Amendment 1 approved", which corrects `D23-E`'s parenthetical). This supersedes step 38's "= true" and the findings that followed it: fv-main:13, registry-audit:10 and pr-relay-graph:27 (sweep:11).

**G13. The rest of the post-merge contract stays unchanged:**
- `agent_merge_authorized` stays `false`;
- `event_1` and `event_3` are unchanged (fv-main:13; A1-5 C-DISPATCH: "No agent merges", and "`PR-40` still verifies the merged state and landed lineage independently").

**G14. `post_merge_three_event_contract.event_2`** (A1-2: "`event_2` becomes 'observed or asserted'"; §12 V-3). `actor` and `value` are unchanged. `fact` becomes sweep:10's literal. `time` is worded on A1-5's single fallback condition, which supersedes sweep:10's "else asserted" (verifier conflict 1, contradiction 6). Final object:
```json
{
  "actor": "Nathan / Product Owner",
  "fact": "product_owner_manual_merge_observed_or_asserted",
  "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge",
  "value": true
}
```
The A1-2 regenerator copies the whole `post_merge_three_event_contract` into the contract (fv-main:10; `GRAPH_POST_MERGE_CONTRACT_MISMATCH`). The validator literals for `event_2` belong to §8b (fv-main:13; §8b O33 (b)).

**G15. `post_merge_three_event_contract.observed_merge_edges`, a new key** (A1-5: "The observed-merge edge is recorded inside `post_merge_three_event_contract`"; §12 V-2; the `D23` successor note "Amendment 1 approved"). It is a list of two summary objects, one for each observed-merge edge, PR-35's (E4) and then RS-40's (E5). sweep:10's key name `pr35_observed_merge_edge` is superseded. New value, as the §4.1 writer serializes it:
```json
[
  {
    "automatic": false,
    "branch_id": "merge_observed",
    "from": "PR-35",
    "state": "MERGE_OBSERVED",
    "to": "PR-40",
    "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
  },
  {
    "automatic": false,
    "branch_id": "merge_observed",
    "from": "RS-40",
    "state": "MERGE_OBSERVED",
    "to": "PR-40",
    "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
  }
]
```
- Each object's six values equal the corresponding fields of E4 and E5 in §4.6 (`state` is the branch's `state`).
- The key is outside the routing digest.
- The same value goes into the contract's `post_merge_three_event_contract`, through the regenerator (§6). A literal check with a must-fail regression guards it (§12 V-2; §8b O33 (b)).

The whole post-merge object after G12–G15, as the §4.1 writer serializes it:
```json
{
  "agent_merge_authorized": false,
  "direct_PR35_to_PR40_automatic_edge": false,
  "event_1": {
    "fact": "prior_pr35_result",
    "producer": "PR-35",
    "time": "pre_merge_historical_evidence",
    "value": "MERGE_PENDING"
  },
  "event_2": {
    "actor": "Nathan / Product Owner",
    "fact": "product_owner_manual_merge_observed_or_asserted",
    "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge",
    "value": true
  },
  "event_3": {
    "consumer": "PR-40",
    "fact": "pr40_actual_merge_verification",
    "independent": true,
    "values": [
      "VERIFIED",
      "PENDING"
    ]
  },
  "observed_merge_edges": [
    {
      "automatic": false,
      "branch_id": "merge_observed",
      "from": "PR-35",
      "state": "MERGE_OBSERVED",
      "to": "PR-40",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "automatic": false,
      "branch_id": "merge_observed",
      "from": "RS-40",
      "state": "MERGE_OBSERVED",
      "to": "PR-40",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    }
  ]
}
```

**G16. `protected_identities.r1_oracle_sha256`: stage E2, commit 2** (§0). Source: A1-1, under which the live surfaces re-point to the successor; also fv-main:18, pr-relay-graph:30 and adversary:7.
- **Value:** the sha256 of the successor oracle file `flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json`, as finally written.
- **When:** it cannot be computed until that file exists. It is taken in the §5.11 pin order: matrix → oracle → runtime map → graph → contract → profile → literals → fixtures → `SKILL_TREE_SHA256` (adversary:7 (d)).
- **The oracle is computed once,** with all three changed rows: GCF-17, GCF-17.LINEAGE and GCF-14 (A1-1, child C3; the `D23` successor note). The GCF-15 in pr-relay-graph:30 is the error the decision record's `D23` correction fixes.

The value that leaves the graph:
```
52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e
```
The other four keys are unchanged:
- `r1_rows` 46, `r1_core_rows` 26 and `r1_material_rows` 20 (A1-1: "the oracle keeps 46 rows (26 core, 20 material)");
- `flowmaster_primary_core_sha256` (A1-6: the shared core stays byte-identical).

This value is not in the routing digest. The historical oracle and its own pins keep their bytes (A1-1), and so does every historical contract that records `52807e58…` (fv-main:21).

**G17. Unchanged in `global.json`:**
- `boundary_nodes`. `NATHAN_MANUAL_MERGE_ASSERTION` stays as the fallback boundary (A1-5: `MERGE_PENDING` "always carries the conditional PR-40 block as the fallback"). This answers pr-relay-graph:27 and keeps fv-main:12's single boundary edge.
- `_other_edge_indices`.
- `_other_state_vocabularies`, including `PR_RETURN_PHASE`. Step 31's "RS-40's `PR_RETURN_PHASE: PR-35` resumes in the PR-35 session" is carried by the RS-40 conditions in E14 and E15, and by R40-8.
- `pr_continuity_contract.phase_aware_rescope_sequences`, `.prompts` and `.primary_skill`.
- `_prologue`. The builder re-stamps its hash lines in the built file only.

### 4.4 `prompts/*.json`: field-level edits

All `edge_indices` lists stay unchanged in every part.

**`PR-35.json`**
- **P35-1.** `edges[0].route_branches[0].condition` (`merge_pending`). Source: A1-7 and A1-5. The full object is E10.
  ```
  conditional PR-40 invocation for Nathan, usable only after he manually merges and only where no MERGE_OBSERVED result was returned for this merge
  ```
- **P35-2. Append the new edge as the last element, `edges[4]`.** Source: A1-5, A1-7.
  - The full object is E4. It is the simulation's clone of `edges[3]` (PR-35 → RS-20) with `to`, `state_predicates` and the branch changed (adversary:12).
  - `automatic` is `false`, because every edge is a paste (A1-5).
  - `edge_indices` stays `[164, 165, 166, 167]` and gains no entry. The simulation adds none, and A1-7 makes it the authority for insertion positions. pr-relay-graph:25's "append at 235 and above" is superseded by it; see §4.8.
- **P35-3.** `node.result_states` takes A1-5's order:
  ```json
  ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  ```
- **P35-4.** `state_vocabularies["PR-35_RESULT"]` takes the same list (A1-5, sweep:3, adversary:9).
- **P35-5.** `state_route_order` becomes:
  ```json
  ["merge_pending", "merge_observed", "rescope_pending", "recovery_pending", "remote_evidence_pending", "product_owner_decision_required"]
  ```
- **P35-6.** `node.session_class` becomes `"DEDICATED_PR_REVIEW_SESSION"` (step 30).
- **P35-7. `node.receiving_role`** (step 30 and A1-8; §12 W-1). Step 30's sentence, followed by C-SESSION's A1-8 clause verbatim. Today's value is `"Same dedicated PR engineer in the same PR-development session; no new role."` New value:
  ```text
  You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
  ```
  - The registry's PR-35 `session_role` equals it verbatim, single-quoted in YAML if needed (registry-audit:7; §7).
  - The contract's `member_registry["PR-35"].receiving_role` is copied from it (fv-main:8; §6).
  - The shared guard phrase is `never as a subagent, forked agent or workflow agent of PR-30` (§12 W-1; verifier unplaced 2). coverage:6's phrase is superseded.
- **P35-8.** `node.adds_session` goes from `false` to `true` (step 30).
- **P35-9.** `node.cross_session_route` goes from `false` to `true` (§12 V-1; fv-rest:15, pr-relay-graph:28).
- **P35-10. `node.native_function`** gains "; return MERGE_OBSERVED when an active subscription observes Nathan's merge" before its final period (§12 V-8). It is a `GRAPH_NODE_CONTRACT` paired field, so the regenerator copies it to `member_registry["PR-35"].native_function` (§6). Today's value:
  ```text
  Continue the same proceeded PR work unit after initial publication; resolve reviews, retest, publish coherent corrections, verify current-head CI/reviews/head/mergeability, and return MERGE_PENDING without merging.
  ```
  New value:
  ```text
  Continue the same proceeded PR work unit after initial publication; resolve reviews, retest, publish coherent corrections, verify current-head CI/reviews/head/mergeability, and return MERGE_PENDING without merging; return MERGE_OBSERVED when an active subscription observes Nathan's merge.
  ```
- **Unchanged:**
  - `r1_mapping` stays `"GCF-17"`;
  - the other `adds_*` flags stay `false`;
  - `title`, `candidate_url` and `output_artifacts`.

**`RS-40.json`**
- **R40-1.** `edges[0].route_branches[0].condition` (`merge_pending`). Source: A1-7. The full object is E13.
  ```
  recorded PR-35 phase result; historical pre-merge evidence; its conditional PR-40 invocation is usable only where no MERGE_OBSERVED result was returned for this merge
  ```
- **R40-2.** `edges[2].route_branches[0].condition` (`recovery_pr30`). Source: A1-7 and step 31. The full object is E14.
  ```
  recorded resumed phase is PR-30_POSTPUBLICATION; PR-30 session/vehicle re-entry
  ```
- **R40-3.** `edges[3].route_branches[1].condition` (`recovery_pr35`). Source: A1-7 and step 31. Branches `[0]` and `[2]` of that edge are unchanged. The full object is E15.
  ```
  recorded resumed phase is PR-35; PR-35 session/vehicle re-entry
  ```
- **R40-4. Append the new edge as the last element, `edges[5]`.** Source: A1-5 ("Both PR-35 and RS-40 gain it") and A1-7; sweep:0, coverage:2. The full object is E5, the clone of `edges[4]` (RS-40 → RS-20). `edge_indices` stays `[228, 229, 230, 231, 232]`.
- **R40-5.** `node.result_states` becomes this list, with `MERGE_OBSERVED` directly after `MERGE_PENDING` (A1-5):
  ```json
  ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  ```
- **R40-6.** `state_route_order` becomes:
  ```json
  ["source_resolution_error", "pr_candidate_published", "merge_pending", "merge_observed", "rescope_pending", "recovery_pr30", "recovery_pr35", "remote_evidence_pending", "product_owner_decision_required"]
  ```
- **R40-7.** `state_vocabularies` stays `{}`. RS-40 has no vocabulary key, so the simulation's vocabulary loop does nothing here.
- **R40-8. `node.receiving_role`** (step 31; registry-audit:9, coverage:18; §12 W-2). Today's value, which C-SESSION makes untrue for the PR-35 phase:
  ```
  You are the same dedicated PR engineering session for the exact suspended work unit.
  ```
  New value, identical in the graph and the registry `session_role`, and mirrored into the contract's `member_registry["RS-40"].receiving_role` (verifier conflict 16):
  ```text
  You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.
  ```
  RS-40's registry `creator_role` also changes under W-2. It has no graph field and belongs to §7.
- **Unchanged:** `session_class` `"DEDICATED_ONE_OFF"`, which §E records as a pre-existing inaccuracy out of scope (§12 S-9); `predecessor_union_destinations`; and every other branch.

**`PR-40.json`** (child C1, A1-7)
- **P40-1. `edges[4]` is replaced in place and keeps `edge_indices[4]` = 172** (child C1; pr-relay-graph:25). Three fields change, and every other key is unchanged (E11):
  - `to` goes from `"PR-30"` to `"PR-20"`;
  - `route_branches[0].branch_id` goes from `"reject_existing_pr_owner"` to `"reject_replan"`;
  - `route_branches[0].condition` becomes:
  ```
  a precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed
  ```
- **P40-2.** `state_route_order[1]` goes from `"reject_existing_pr_owner"` to `"reject_replan"` (child C1; pr-relay-graph:24). Without this, the builder silently moves the row to the end and the digest changes (N1).
- **P40-3.** `edges[5].route_branches[0].condition` (`reject_material_boundary_proposal`). Source: A1-7; pr-relay-graph:29. The full object is E12.
  ```
  a substantiated material change to the Epic-level commitment (D23-C) requires a new bounded rescope proposal
  ```
- **Unchanged:**
  - `node.receiving_role` stays (§12 W-3; sweep:15). Body-level C-TOP and its guards carry the top-level rule for PR-40;
  - `node.predecessor_union_destinations`, which is the predecessor's record and still lists PR-30; no source edits it.

**`PR-20.json`**
- **P20-1.** `edges[1].route_branches[0].condition` (`awaiting_po_proceed`). Source: child C2 and A1-7. The full object is E7.
  ```
  one complete executable approved-scope plan awaits the Product Owner Proceed for that plan
  ```
- **P20-2.** `edges[4].route_branches[0].condition` (`material_boundary`). Source: A1-7, which supersedes step 23's "as C-LAT defines it" wording. The full object is E8.
  ```
  the planning result substantiates a material change to the Epic-level commitment (D23-C)
  ```
- **Unchanged:** `node.receiving_role` stays (§12 W-3; sweep:15). Body-level C-TOP and its guards carry the top-level rule for PR-20.

**`PR-30.json`**
- **P30-1.** `edges[2].route_branches[0].condition` (`pr_candidate_published`). Source: A1-7 and step 31. The full object is E9.
  ```
  one complete PR-35 handoff to the dedicated PR-35 session for the same work unit and pull request
  ```
- **Unchanged:** `node.receiving_role`, whose "same … session" is PR-20's session. C-SESSION keeps it: "PR-30's session plans with PR-20 and builds."

**`PR-10.json`**
- **P10-1.** `edges[4].route_branches[0].condition` (`material_boundary`). Source: A1-7 and step 23. The full object is E6.
  ```
  a material change to the Epic-level commitment (D23-C) is substantiated
  ```

**`DOC-10.json`**
- **D10-1.** `edges[3].route_branches[0].condition` (`material_boundary`). Source: A1-7; pr-relay-graph:29. The full object is E1.
  ```
  repository evidence proves a complete bounded material change to the Epic-level commitment (D23-C)
  ```

**Not edited:**
- `DOC-20.json`. A1-5 leaves the DOC-20 → PR-40 edge unchanged, and A1-7 leaves `material_delta` unchanged. This supersedes pr-relay-graph:27's request for DOC-20.json:151.
- `OPS-10`, `OPS-20`, `OPS-30` and `QA-10`. §P's PART-07 ruling covers the PR lane only.
- `RS-20`. Rescope's single Proceed is out of scope (child plan, "Not in scope").
- Every other part.

### 4.5 Wording that stays because A1-7's diff is complete

After the transform, these conditions and roles still use session or Proceed language. None of them is in A1-7's table, so they stay: changing any of the conditions would move the digest.
```
PR-30  recovery_pending       "complete same-session re-entry; no new vehicle"          (PR-30 re-enters its own session)
PR-35  recovery_pending       "complete same-session re-entry with checkpoint"          (PR-35 re-enters its own session)
PR-20  same_owner_recovery    "a bounded planning defect is repairable by the same dedicated PR planning session"
RS-20  (two branches)         "existing repair owner/phase is PR-30|PR-35 under the original Proceed; no addendum"   (rescope)
DOC-20 landed_lineage_review  "actual merged state or landed-lineage review is required after Nathan asserts the manual merge"   (A1-5)
OPS-10, OPS-20, OPS-30, QA-10 "material ... boundary" conditions                        (PR lane only)
PR-30  node.receiving_role    "You are the same dedicated PR engineering session for one exact approved work unit."
```
The PR-20 and PR-40 `node.receiving_role` values also stay, for a different reason: §12 W-3. The `D23` clarification's *Guard* paragraph is corrected to name "PR-35's graph, contract and registry role, and every main-ecosystem body (C-TOP)".

### 4.6 The exact edge objects, from the simulation's `new` build: authority for the digest

There are 15 objects: 13 changed and 2 new. Each is shown as it appears in the built graph, which is identical to its part-file object. Each routing-surface row sha256 is computed as follows; the rows are sorted and hashed together into `fecc319b…`:
```
sha256(("E\x1f" + json.dumps(edge, sort_keys=True, separators=(",", ":"))).encode())
```

**E1. CHANGED — DOC-10 → RS-10, branch(es) `material_boundary`.** Part location `prompts/DOC-10.json` `edges[3]`; `edge_indices` 68 (unchanged); built position 68. Routing-surface row sha256 `6b857aec7f14684f815c90a02de4467040b21a7412890623f04f7be0df2880c5`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "DOC-10",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "DRAFT",
        "PENDING",
        "BLOCKED"
      ],
      "branch_id": "material_boundary",
      "condition": "repository evidence proves a complete bounded material change to the Epic-level commitment (D23-C)",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "CONDITIONAL_RECOVERY",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/b/DOC-10.md",
        "section": "Required result and routing"
      },
      "state": null,
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "DRAFT",
    "PENDING",
    "BLOCKED"
  ],
  "to": "RS-10",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E2. CHANGED — NATHAN_MANUAL_MERGE_ASSERTION → PR-40, branch(es) `manual_merge_then_lineage_review`.** Part location `global.json` `_other_edges[1]`; `_other_edge_indices[1]` 123 (unchanged); built position 123. Routing-surface row sha256 `d2983a1f2bb2c51c384aed760c3a29c5719ef9a6eced3be730f896403ab85704`.

```json
{
  "automatic": false,
  "branch_id": "manual_merge_then_lineage_review",
  "condition": "Nathan has manually merged the identified PR, no MERGE_OBSERVED result was returned for this merge, and he invokes the conditional PR-40 block",
  "from": "NATHAN_MANUAL_MERGE_ASSERTION",
  "from_kind": "boundary",
  "immediate": true,
  "origin_prompt": "PR-35_OR_RS-40",
  "origin_state": "MERGE_PENDING",
  "to": "PR-40",
  "to_kind": "prompt",
  "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
}
```

**E3. CHANGED — NATHAN_PROCEED → PR-30, branch(es) `original_proceed`.** Part location `global.json` `_other_edges[2]`; `_other_edge_indices[2]` 124 (unchanged); built position 124. Routing-surface row sha256 `8559b6888d0d3a5ca4dfc0c85cb7ac41176ffb3a09878b4bd787f599bf5f8650`.

```json
{
  "automatic": false,
  "branch_id": "original_proceed",
  "condition": "the explicit Proceed for the exact approved per-PR plan; never a second Proceed for the same plan",
  "from": "NATHAN_PROCEED",
  "from_kind": "boundary",
  "immediate": true,
  "origin_prompt": "PR-20",
  "origin_state": "AWAITING_PO_PROCEED",
  "to": "PR-30",
  "to_kind": "prompt",
  "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
}
```

**E4. NEW — PR-35 → PR-40, branch(es) `merge_observed`.** Part location `prompts/PR-35.json` `edges[4]`; no `edge_indices` entry; builder assigns 128; built position 128. Routing-surface row sha256 `d5080cb306f2b364052a78c51afb820c4e0cbd3c7490ae61c669b77a5dfcc7c3`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-35",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "MERGE_OBSERVED"
      ],
      "branch_id": "merge_observed",
      "condition": "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-35.md",
        "section": "Required result and routing"
      },
      "state": "MERGE_OBSERVED",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "MERGE_OBSERVED"
  ],
  "to": "PR-40",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E5. NEW — RS-40 → PR-40, branch(es) `merge_observed`.** Part location `prompts/RS-40.json` `edges[5]`; no `edge_indices` entry; builder assigns 129; built position 129. Routing-surface row sha256 `25b411c5b3e2c4606f296ce984a41124cb0e5f0bd13438b0afb00c1f43b69396`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "RS-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "MERGE_OBSERVED"
      ],
      "branch_id": "merge_observed",
      "condition": "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "MERGE_OBSERVED",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "MERGE_OBSERVED"
  ],
  "to": "PR-40",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E6. CHANGED — PR-10 → RS-10, branch(es) `material_boundary`.** Part location `prompts/PR-10.json` `edges[4]`; `edge_indices` 154 (unchanged); built position 149. Routing-surface row sha256 `069eb8ce910dbeba1abe420db0fdee925c9aadbf0132bef92338bb3b3211081d`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-10",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "DRAFT",
        "BLOCKED"
      ],
      "branch_id": "material_boundary",
      "condition": "a material change to the Epic-level commitment (D23-C) is substantiated",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "CONDITIONAL_RECOVERY",
      "route_steps": [
        "PR-10 -> RS-10",
        "RS-10 complete proposal -> RS-20"
      ],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-10.md",
        "section": "Required result and routing"
      },
      "state": null,
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "DRAFT",
    "BLOCKED"
  ],
  "to": "RS-10",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E7. CHANGED — PR-20 → NATHAN_PROCEED, branch(es) `awaiting_po_proceed`.** Part location `prompts/PR-20.json` `edges[1]`; `edge_indices` 156 (unchanged); built position 151. Routing-surface row sha256 `04407d09933e5fd0e023dff06750cd2cc00dde7108738c7e007258286dfb4996`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-20",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "AWAITING_PO_PROCEED"
      ],
      "branch_id": "awaiting_po_proceed",
      "condition": "one complete executable approved-scope plan awaits the Product Owner Proceed for that plan",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-20.md",
        "section": "Required result and routing"
      },
      "state": "AWAITING_PO_PROCEED",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "AWAITING_PO_PROCEED"
  ],
  "to": "NATHAN_PROCEED",
  "to_kind": "boundary",
  "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
}
```

**E8. CHANGED — PR-20 → RS-10, branch(es) `material_boundary`.** Part location `prompts/PR-20.json` `edges[4]`; `edge_indices` 159 (unchanged); built position 154. Routing-surface row sha256 `d0e9ed028a94e70c8aee49b0bdabc39e4074f904bf85474c761578cf3633abec`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-20",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "DRAFT",
        "BLOCKED"
      ],
      "branch_id": "material_boundary",
      "condition": "the planning result substantiates a material change to the Epic-level commitment (D23-C)",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "CONDITIONAL_RECOVERY",
      "route_steps": [
        "PR-20 -> RS-10",
        "RS-10 complete proposal -> RS-20"
      ],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-20.md",
        "section": "Required result and routing"
      },
      "state": null,
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "DRAFT",
    "BLOCKED"
  ],
  "to": "RS-10",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E9. CHANGED — PR-30 → PR-35, branch(es) `pr_candidate_published`.** Part location `prompts/PR-30.json` `edges[2]`; `edge_indices` 162 (unchanged); built position 157. Routing-surface row sha256 `9e80504ee1a76210e1c2df6da9e9fc0071c978b01dd7e1e28990bbf1cc8d9d08`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-30",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "PR_CANDIDATE_PUBLISHED"
      ],
      "branch_id": "pr_candidate_published",
      "condition": "one complete PR-35 handoff to the dedicated PR-35 session for the same work unit and pull request",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-30.md",
        "section": "Required result and routing"
      },
      "state": "PR_CANDIDATE_PUBLISHED",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "PR_CANDIDATE_PUBLISHED"
  ],
  "to": "PR-35",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E10. CHANGED — PR-35 → NATHAN_MANUAL_MERGE_ASSERTION, branch(es) `merge_pending`.** Part location `prompts/PR-35.json` `edges[0]`; `edge_indices` 164 (unchanged); built position 159. Routing-surface row sha256 `06f8f999ef3282c005355c6fd85aa8d6ae006a50b86cedc909a486e3c454b2a4`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-35",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "MERGE_PENDING"
      ],
      "branch_id": "merge_pending",
      "condition": "conditional PR-40 invocation for Nathan, usable only after he manually merges and only where no MERGE_OBSERVED result was returned for this merge",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-35.md",
        "section": "Required result and routing"
      },
      "state": "MERGE_PENDING",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "MERGE_PENDING"
  ],
  "to": "NATHAN_MANUAL_MERGE_ASSERTION",
  "to_kind": "boundary",
  "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
}
```

**E11. CHANGED, re-targeted in place (was PR-40 → PR-30, branch `reject_existing_pr_owner`) — PR-40 → PR-20, branch(es) `reject_replan`.** Part location `prompts/PR-40.json` `edges[4]`; `edge_indices` 172 (unchanged); built position 167. Routing-surface row sha256 `88ed4e6b6b1d2916ec2fc059cd8103d780b4d3a076bbd03d4833968ade70e429`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "REJECT"
      ],
      "branch_id": "reject_replan",
      "condition": "a precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-40.md",
        "section": "Required result and routing"
      },
      "state": "REJECT",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "REJECT"
  ],
  "to": "PR-20",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E12. CHANGED — PR-40 → RS-10, branch(es) `reject_material_boundary_proposal`.** Part location `prompts/PR-40.json` `edges[5]`; `edge_indices` 173 (unchanged); built position 168. Routing-surface row sha256 `b97b384577330585d7603992fee38c5293a46201655dbbfa8a45861d32f13183`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "PR-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "REJECT"
      ],
      "branch_id": "reject_material_boundary_proposal",
      "condition": "a substantiated material change to the Epic-level commitment (D23-C) requires a new bounded rescope proposal",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [
        "PR-40 -> RS-10",
        "RS-10 complete proposal -> RS-20",
        "RS-20 REVISION_REQUIRED -> RS-30"
      ],
      "source_evidence": {
        "path": "candidate/prompts/c/PR-40.md",
        "section": "Required result and routing"
      },
      "state": "REJECT",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "REJECT"
  ],
  "to": "RS-10",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E13. CHANGED — RS-40 → NATHAN_MANUAL_MERGE_ASSERTION, branch(es) `merge_pending`.** Part location `prompts/RS-40.json` `edges[0]`; `edge_indices` 228 (unchanged); built position 222. Routing-surface row sha256 `49041986c93bcd2758f4270fed6a2218ad99ffa6aef7029207b58fd647958f10`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "RS-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "MERGE_PENDING"
      ],
      "branch_id": "merge_pending",
      "condition": "recorded PR-35 phase result; historical pre-merge evidence; its conditional PR-40 invocation is usable only where no MERGE_OBSERVED result was returned for this merge",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "MERGE_PENDING",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "MERGE_PENDING"
  ],
  "to": "NATHAN_MANUAL_MERGE_ASSERTION",
  "to_kind": "boundary",
  "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
}
```

**E14. CHANGED — RS-40 → PR-30, branch(es) `recovery_pr30`.** Part location `prompts/RS-40.json` `edges[2]`; `edge_indices` 230 (unchanged); built position 224. Routing-surface row sha256 `0c1aceb1af321face47b8dbfc34780b8d95f97d9b96970774ed6bd8365d17cb8`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "RS-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "RECOVERY_PENDING"
      ],
      "branch_id": "recovery_pr30",
      "condition": "recorded resumed phase is PR-30_POSTPUBLICATION; PR-30 session/vehicle re-entry",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "RECOVERY_PENDING",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "RECOVERY_PENDING"
  ],
  "to": "PR-30",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

**E15. CHANGED — RS-40 → PR-35, branch(es) `pr_candidate_published`, `recovery_pr35`, `remote_evidence_pending`.** Part location `prompts/RS-40.json` `edges[3]`; `edge_indices` 231 (unchanged); built position 225. Routing-surface row sha256 `4903a49c2de3aae04f1d7bbba6c4ab54b33b6b37033db2278f1d63c01023a32d`.

```json
{
  "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
  "automatic": false,
  "from": "RS-40",
  "from_kind": "prompt",
  "immediate": true,
  "route_branches": [
    {
      "applicable_states": [
        "PR_CANDIDATE_PUBLISHED"
      ],
      "branch_id": "pr_candidate_published",
      "condition": "recorded PR-30_POSTPUBLICATION phase result",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "PR_CANDIDATE_PUBLISHED",
      "terminal_for_invocation": false
    },
    {
      "applicable_states": [
        "RECOVERY_PENDING"
      ],
      "branch_id": "recovery_pr35",
      "condition": "recorded resumed phase is PR-35; PR-35 session/vehicle re-entry",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "RECOVERY_PENDING",
      "terminal_for_invocation": false
    },
    {
      "applicable_states": [
        "REMOTE_EVIDENCE_PENDING"
      ],
      "branch_id": "remote_evidence_pending",
      "condition": "PR-35 only; durable checkpoint",
      "next_prompt_handoff_count": 1,
      "public_result": true,
      "route_kind": "NATIVE_RESULT",
      "route_steps": [],
      "source_evidence": {
        "path": "candidate/prompts/d/RS-40.md",
        "section": "Required result and routing"
      },
      "state": "REMOTE_EVIDENCE_PENDING",
      "terminal_for_invocation": false
    }
  ],
  "state_predicates": [
    "PR_CANDIDATE_PUBLISHED",
    "RECOVERY_PENDING",
    "REMOTE_EVIDENCE_PENDING"
  ],
  "to": "PR-35",
  "to_kind": "prompt",
  "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
}
```

### 4.7 Final ordered lists and state-route rows

These are from the simulation's `new` build. Three orderings are ruled or measured:
- The `MERGE_OBSERVED` vocabulary order is A1-5's single ordered vocabulary (sweep:3, adversary:9). The registry's `outputs[].states` lists are the one exception, in ASCII order (§12 V-12; §7).
- Each `merge_observed` route sits immediately after `merge_pending`.
- PR-40's renamed entry keeps position 1.
```
PR-35 state_route_order                  ["merge_pending", "merge_observed", "rescope_pending", "recovery_pending", "remote_evidence_pending", "product_owner_decision_required"]
PR-35 node.result_states                 ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
PR-35 state_vocabularies["PR-35_RESULT"] ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
RS-40 state_route_order                  ["source_resolution_error", "pr_candidate_published", "merge_pending", "merge_observed", "rescope_pending", "recovery_pr30", "recovery_pr35", "remote_evidence_pending", "product_owner_decision_required"]
RS-40 node.result_states                 ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
RS-40 state_vocabularies                 {}
PR-40 state_route_order                  ["accept", "reject_replan", "reject_instruction_owner", "reject_material_boundary_proposal", "pending_native_owner", "pending_terminal", "lineage_review_terminal"]
```
The 7 state-route rows that move, with their branch order and routing-surface row sha256. Each row hash is computed as follows:
```
sha256(("S\x1f" + key + "\x1f" + json.dumps(rows, sort_keys=True, separators=(",", ":"))).encode())
```
```
DOC-10  11f5f28fa217c0fad3b1cdc79062d43ecb5e6fada34a015c2212db4762a089f2  ["instruction_ready", "material_boundary", "repairable_instruction_defect", "instruction_terminal"]
PR-10  f9fbdcdb040606d88c0bdbec262f25a7539b4b607f7181e9f1c60580046f307e  ["instruction_ready", "material_boundary", "same_owner_recovery", "upstream_owner_recovery", "instruction_terminal"]
PR-20  c7ea28e4e1301904d8e3fa22d42a106116fc2c5863c905b52396540c01fe0fc2  ["awaiting_po_proceed", "material_boundary", "same_owner_recovery", "upstream_owner_recovery", "planning_terminal"]
PR-30  d5d6a47fcaedf9bd0e5d830fcb55158d1704369522c579d9d18aec519fb8cf79  ["pr_candidate_published", "rescope_pending", "recovery_pending", "product_owner_decision_required", "pr30_terminal"]
PR-35  b514f7a163a24d2e777553274d9fb7f076013005b09cd2c8bf5257513d179731  ["merge_pending", "merge_observed", "rescope_pending", "recovery_pending", "remote_evidence_pending", "product_owner_decision_required"]
PR-40  4b578df5ccbf60d933081fb31f891a5656649fa59f212894cc277ee3f885bbf6  ["accept", "reject_replan", "reject_instruction_owner", "reject_material_boundary_proposal", "pending_native_owner", "pending_terminal", "lineage_review_terminal"]
RS-40  b8477dc9d4968f9fe41c5c77ead05084b7fb7af00184cb6a68091d98e6279ee1  ["source_resolution_error", "pr_candidate_published", "merge_pending", "merge_observed", "rescope_pending", "recovery_pr30", "recovery_pr35", "remote_evidence_pending", "product_owner_decision_required"]
```
**Inbound edges after the transform (measured).** All are `automatic: false`.
```
to PR-40: DOC-20 (landed_lineage_review), NATHAN_MANUAL_MERGE_ASSERTION (manual_merge_then_lineage_review), PR-35 (merge_observed), RS-40 (merge_observed)
to PR-20: DOC-10 (instruction_ready), PR-10 (instruction_ready), PR-20 (same_owner_recovery), PR-40 (reject_replan)
```

### 4.8 Edge placement and the builder's edge indices (adversary:12)

All of the following was measured by tracing `graph_parts.py assemble` on both builds.
- **The builder's counter starts at 125.** `global.json` declares 13 `_other_edge_indices` (122–134) for its 3 `_other_edges`. The builder zips the two lists, so only 122–124 are used, and its counter for edges without an index starts at 125.
- **Three edges have no index today:** `CF-C-10` `edges[4]`, and `ESC-40` `edges[3]` and `edges[4]`. The builder gives them 125, 126 and 127. `QA-70` also has 5 indices for 4 edges (pr-relay-graph:25).
- **The two new edges get 128 and 129.** They carry no index, and the builder gives them 128 (PR-35, since `PR-35.json` sorts before `RS-40.json`) and 129 (RS-40). This places them at built positions 128 and 129, among the other edges rather than at the end.
- **What the collision is** (§12 §4 OQ-10). 128 and 129 are also entries of `_other_edge_indices`, which no edge carries. That is the collision: with the declared list, not with a placed edge. In the new build all 229 placed edges have distinct indices. adversary:12 reports 135, which `OPS-10`'s first edge carries. The builder never assigns 135, because its counter does not start at max(`_other_edge_indices`)+1. The amendment's edge-index bullet is corrected to this measurement.
- **The digest is unaffected either way,** because `routing_surface` sorts its rows.
- **Placement still matters.** It changes the embedded bytes, and the order of the contract's `route_edges`, which the regenerator copies. Measured: giving the PR-35 edge an explicit index of 235 (N3), or inserting it at `edges[0]` (N4), leaves the digest at `fecc319b…`/284 but changes the graph sha256. This is why V3 compares the parts with the simulation.
- **Fixing the builder is out of scope** (amendment, "Noticed, not in scope").

### 4.9 Order of operations (§0; §12 V-10)

1. **E1, the routing transform first.** Apply exactly the simulation's transform: G1–G4 and every routing item of §4.4 (P35-1 to P35-5, R40-1 to R40-7, P40-1 to P40-3, P20-1, P20-2, P30-1, P10-1 and D10-1). Build to scratch (V1) and check the A1-7 checkpoint:
   - 55 nodes, 229 edges, embedded JSON 574 175 bytes, sha256 `b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7`;
   - routing surface `('fecc319bdd4ce7ee6201cb77d7231861', 284)`;
   - every part file equal to the simulation's `parts_new` (V3, first table).
2. **E1, then the non-routing edits:** G5, G6, G8–G10, G14, G15, P35-6 to P35-10, and R40-8. G7, G11–G13 and G17 are "stays" items and need no action. Rebuild to scratch and re-check the routing surface `fecc319b…`/284 and 229 edges. Record the build's bytes and sha256 (measured on a copy: 575 074 B, `716c4cfc…`; §4.2). Every part file must equal V3's second table. **This state is commit 1.**
3. **E2, G16.** It waits for the successor oracle file and follows the §5.11 pin order (adversary:7). Write `<SUCC_ORACLE>` into `protected_identities.r1_oracle_sha256`. **This is commit 2.**
4. **One final build**, from the commit-2 parts. Re-check `fecc319b…`/284 and 229 edges, and record the final bytes and sha256 (§12 V-10). Its embedded JSON block plus one LF becomes the bundled graph in both skills, and the pin chain continues from it (fv-main:16, fv-rest:10, pr-relay-graph:20; §5.11, §6). The skill-bundled graph copies are validator fixtures built from the parts, so writing them breaks no rule of `glow-graph-contract/SKILL.md:59` (§12 S-3). The A1-2 contract regenerator reads the same build, and the A1-2 registry deriver reads the same parts.

### 4.10 Verification

**V1. Build to scratch, never into the repository.**
```
PYTHONDONTWRITEBYTECODE=1 python3 /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/scripts/graph_parts.py build <execution-worktree>/docs/graph/parts <scratch>/graph.md
```
It must print `55 nodes, 229 edges, 55 state_routes`, no `WARNING` line and `validation PASS`. The builder's endpoint check always passes, so this shows only that the parts assemble (pr-relay-graph:23). Parity with the contract is an E4 item (§6, §9).

**V2. Routing digest.** Take the embedded JSON block of the V1 build and run `routing_surface({"route_edges": edges, "state_routes": state_routes})` from a scratch copy of `flowmaster-validate/scripts`. It must return, at every checkpoint of §4.9:
```
('fecc319bdd4ce7ee6201cb77d7231861', 284)
```

**V3. Equality with the simulation.** Rerun the simulation copy as in §4.2.

*After the routing transform only (§4.9 step 1):* all 56 part files equal the simulation's `parts_new`. The eight changed files hash to these checkpoint values:
```
global.json  base 9cc3b8852e2c0247ff9859c7f1f6728ca0006889f5ff40be0c68f465da92b76c 28873  ->  sim 87ccfb1c179ad2dea50f541fd35522a1564b9741d821f3b589433fb32e323124 29037
prompts/DOC-10.json  base 04a6204f3c0e599942498168f47cae09d7cee7ed21275ce146241472af66b69a 5737  ->  sim f715cee5815c3f7f149dd618f485e689636f154b204460af67715086a8c3a72a 5772
prompts/PR-10.json  base a41e5e7ee60ac0cdba569878eb767c7c06204ea0234b46fd97255f936f1d145d 6746  ->  sim a5ceb711b4d859ddd81734a3811ccb5ff4cb16ee61fbccce49d22193b7320a37 6729
prompts/PR-20.json  base 0a8051e302faad73232b91694937bf69f510fa2d17476e665f1ad2135915885e 6848  ->  sim c7043b60c2f6f25a05fd8de26f323acf86570bd3dc72fad462165a8c9af99faf 6844
prompts/PR-30.json  base 51ef5f6b593f8f339a5e0e2806c95435ccf2d52897fff7fca7658d2328d4c885 6298  ->  sim 0b062ecec0c67fd5e9f3a8190895218d9915819e999ca894250a49e51262aa4b 6351
prompts/PR-35.json  base 2c1c7aa9be3413d19113f5dbd4847d4024646c8f6b8d05aba72e12973bb62b4c 6657  ->  sim d315a3c70113fcbffefb5081afb0a0dc7a5dad7fe22ac438b92721fbaac470af 7815
prompts/PR-40.json  base cfe991001f13e5f6a1561901ffaef6febeb435b98f783b8bae38b6e8e1d1f493 8488  ->  sim 9a762c3f7753fe78d5af694033609f8c821c3d6b07bb4a8680732f2304273111 8570
prompts/RS-40.json  base 3be8a22dfbd2d645f5bf44baf3a311063d04c2f961d046a614f28bf5e87250ff 8806  ->  sim 6916dbe138827227ba5bcd5a453be972322be3590566ffc6c48f978896033cf2 9995
```

*After every E1 edit (§4.9 step 2, commit 1):* each part file equals the simulation's `parts_new` except at exactly these JSON paths:
```
global.json
  $.handoff_contract.required
  $.handoff_contract.prohibited
  $.pr_continuity_contract.shared_exactly_one
  $.pr_continuity_contract.adds.session
  $.pr_continuity_contract.adds.cross_session_route
  $.post_merge_three_event_contract.event_2.fact
  $.post_merge_three_event_contract.event_2.time
  $.post_merge_three_event_contract.observed_merge_edges
prompts/PR-35.json
  $.node.session_class
  $.node.receiving_role
  $.node.adds_session
  $.node.cross_session_route
  $.node.native_function
prompts/RS-40.json
  $.node.receiving_role
every other path of all 56 files: equal to parts_new
```
Measured on the copy of §4.2 (`/tmp/claude-0/v2work/parts_final`). The three files that differ from the simulation hash to:
```
global.json          ef4abb9cda68a9b75495036981903c76e822d6926421eb754ff0e0067f5dda60 29598
prompts/PR-35.json   c32a2fa5bc20076a98330095def964c4a48adf073d50a1fedd8f1208fcc87702 8098
prompts/RS-40.json   45ba0728ee8c661c2984ce56ff060f789a299d3b4e9ccd06c24dd7a3e531fe5d 10050
```
DOC-10, PR-10, PR-20, PR-30 and PR-40 keep their simulation hashes in commit 1 and in the final parts; PR-20 and PR-40 do so because their roles stay (§12 W-3).

*After G16 (§4.9 step 3, commit 2):* `global.json` differs from its commit-1 bytes at `$.protected_identities.r1_oracle_sha256` only. Its byte count stays 29 598.

**V4. The copies are equal.** G1 equals G2, and G3 equals G4 (child C2: "the two copies are byte-equal").

**V5. Closure.** Command:
```
PYTHONDONTWRITEBYTECODE=1 python3 /home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/closure.py <ID> --parts <parts>/prompts --json
```
Measured on the simulation's parts. The results meet child C1's expectation and step 38's (PR-35 upstream of PR-40):
```
prompt  upstream                        downstream                     radius before -> after
PR-10   [GCFPE-MGMT-10, IA-30, PR-40]   [PR-10, PR-20, RS-10]          24 -> 24
PR-20   [DOC-10, PR-10, PR-40]          [PR-20, RS-10]                 21 -> 22
PR-30   [ESC-40, RS-20, RS-40]          [PR-30, PR-35, RS-20]           7 -> 6
PR-35   [ESC-40, PR-30, RS-20, RS-40]   [PR-35, PR-40, RS-20]           6 -> 7
PR-40   [DOC-20, PR-35, RS-40]          [PR-10, PR-20, RS-10]           9 -> 11
RS-40   [RS-20]                         [PR-30, PR-35, PR-40, RS-20]    4 -> 5
DOC-10  [DOC-20]                        [DOC-10, PR-20, RS-10]         22 -> 22
```
Step 12's "`closure.py` unchanged for all prompts" holds for step 12 alone, because `closure.py` reads no `global.json` key. It does not hold for the whole transform. The non-routing edits change no edge, so the table holds for the final parts too.

**Negative controls, measured on copies of the simulation's `parts_new`.** Each shows which check catches which omission:
```
N1  PR-40 state_route_order entry not renamed     digest 70c9189ceadedf1f4f60a61a38906924/284, no builder warning   -> caught by V2
N2  boundary_transitions copies left unedited     digest fecc319b.../284 unchanged; 574093 bytes                    -> caught by V3 and V4, not by V1 or V2
N3  new PR-35 edge given edge_indices entry 235   digest unchanged; sha256 c1fbb70023742abe...                      -> caught by V3, not by V1 or V2
N4  new PR-35 edge inserted at edges[0]           digest unchanged; sha256 8c6f4f468ed9745b...                      -> caught by V3, not by V1 or V2
```

### 4.11 Findings placed in this section

- **Applied here.**
  - Field names and values: fv-main:2 (graph half, less `cross_session_route`), fv-rest:15, pr-relay-graph:28; `cross_session_route` 1 by §12 V-1.
  - The PR-35 node's graph half: fv-main:8; the role string by §12 W-1.
  - Rename and placement: pr-relay-graph:24, pr-relay-graph:25 (in-place re-target; "235 and above" superseded by the simulation).
  - The two copies and PR-20: pr-relay-graph:26, fv-rest:28.
  - The added PART-07 conditions, with DOC-20 unchanged: pr-relay-graph:29.
  - The graph's pin site, computed once after the oracle, with GCF-15 corrected to GCF-17.LINEAGE and GCF-14: fv-main:18, pr-relay-graph:30, adversary:7.
  - The ordered vocabulary: sweep:3, adversary:9.
  - RS-40 mirrored: sweep:0, coverage:2.
  - `event_2.fact`: sweep:10.
  - The simulation as authority, and the placement note: adversary:12.
  - Row accounting, 15 rows: coverage:25 (§12 V-11).
  - Step 12's graph half: pr-relay-graph:31, with the lists of §12 W-10.
  - The PR-35 role: registry-audit:7 (§12 W-1). The RS-40 role: registry-audit:9, coverage:18 (§12 W-2).
- **Superseded, with the ruling or decision that governs.**
  - `direct_PR35_to_PR40_automatic_edge` becoming `true` in fv-main:13, pr-relay-graph:27 and registry-audit:10: A1-5, via sweep:11, and the `D23` successor note.
  - fv-main:2's `cross_session_route` 0, in that part only: §12 V-1.
  - sweep:10's key name `pr35_observed_merge_edge` and its `event_2.time` "else asserted": §12 V-2 and V-3, on A1-5's single fallback condition.
  - coverage:6's role-guard phrase: §12 W-1.
  - sweep:15's request to change the PR-20 and PR-40 roles: §12 W-3.
  - The 281/282-row and 283-row figures in fv-main:9 and sweep:0: A1-7's `fecc319b…`/284.
  - pr-relay-graph:27's DOC-20.json:151 edit: A1-5.
- **Human re-pin.** fv-rest:14 and fv-main:9 (by the pin's own rule, a human re-pins it after reading the diff): the diff is A1-7, reproduced in §4.2 and approved in the `D23` successor note.
- **Scoped here.** The grep-scope part of fv-main:21: the graph's single pin site moves, and historical files keep `52807e58…`.
- **Weak gate recorded.** pr-relay-graph:23: V1 counts as assembly only.
- **Cross-referenced to other sections, not placed here.**
  - Contract regeneration and parity: fv-main:4, fv-main:10, fv-main:17, fv-rest:12, fv-rest:13, pr-relay-graph:21, coverage:12, adversary:2, adversary:3.
  - Bundled graph and pin chain: fv-main:16, fv-rest:10, pr-relay-graph:20.
  - Validator literals: fv-main:3, fv-main:11, fv-main:12, fv-main:19, fv-rest:20, fv-rest:21.
  - Registry: registry-audit:10, registry-audit:12.

### 4.12 Unsettled

§12 settles every open question of v1's §4 (OQ-1 to OQ-10). What it does not settle:
- **The order of `handoff_contract.required`.** §12 W-10 says the list "keeps the two surviving strings … and adds three" without stating the order. G5 reads it as the two survivors first, in today's order, then the three in W-10's order. The routing digest is unaffected. The contract's `transition_contract` is keyed and has no list order (§12 V-6). E5 confirms the reading.

## §5 Successor R1 oracle

This section compiles A1-1 together with child step C3, the `D23` correction ("D23-F names the wrong R1 row") and the `D23` successor note "Amendment 1 approved" ("The R1 oracle gets a successor, not an in-place edit. Three rows change: GCF-17, GCF-17.LINEAGE and GCF-14"). The §12 "Successor oracle" block settles every question v1 left open here (§5 OQ-1 to OQ-14), and §12 V-7 settles OQ-8; each is applied inline and cited by id. The few points §12 does not settle are listed in §5.14.

Line numbers refer to today's installed tree, the §2 baseline. Paths are written in full from the skill root (§12, verifier conflict 19). Values marked **PROTOTYPE** were produced on scratch copies (v1 under `/tmp/claude-0/spec/s5/`; this v2 under `/tmp/claude-0/v2work/`). EXECUTE recomputes every one of them.

The work is stage E2 (§0): the matrix, the oracle and the map are built on scratch copies of the skills, and the oracle digest reaches the repository only through G16 in commit 2 (§4.3).

### 5.1 The three files (A1-1)

```
flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json        successor oracle
change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json    successor runtime map
flowmaster-validate/references/r1-successor-source-20260923.md                         successor source matrix
```

- The matrix ships in the `flowmaster-validate` package, so `SKILL_TREE_SHA256` covers it.
- **The repository keeps a byte-identical copy** at `docs/prompt_ecosystem_management/r1-successor-source-20260923.md` (A1-1; §12 OQ-6). It lives there because it is an authority source, not a Modification's evidence.
- **A builder script** produces the matrix, the oracle and the map. It is committed with the evidence and reviewed in E5 (§12 OQ-11 (a)).
- The historical oracle, the historical runtime map, the correction layers and the historical contracts stay in their packages with unchanged bytes. Their validators and pins are never edited (A1-1; fv-rest:8; sweep:8). §5.9 lists them.

### 5.2 Profile id (A1-1; fv-rest:7)

```
GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1
```

The id is new because corrected bytes must not reuse an identity (fv-rest:7). The old id `GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1` stays in the historical oracle and the historical map.

### 5.3 How the successor oracle is produced (A1-1; adversary:8; sweep:24)

1. Read the historical oracle's bytes and confirm their digest before using them:
   ```
   52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e
   ```
2. Deep-copy it and change exactly these:
   - `profile_id` (§5.2);
   - in `required_global_tokens`, the one entry `GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1`, replaced in place by the new profile id (§12 OQ-2 (a));
   - `authority`, by additions only (§5.5);
   - the ten row fields below;
   - then `source_row_sha256` of the three changed rows (§5.4).
3. Copy everything else verbatim:
   - the top-level keys `schema_version`, `generated_for_run`, `coverage`, `special_destinations`, `external_inputs`, `terminal_outputs` and `prohibited_active_patterns`, and every other entry of `required_global_tokens`, in place;
   - the other 43 rows, the row order, and the key order in every object.
4. Serialize with the recipe below.

**Changed row fields.** These are the final values. They come from the A1-1 table, with GCF-17.LINEAGE from child C3 and D23, and GCF-14 from sweep:24.

```json
{
  "id": "GCF-17",
  "name": "Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session",
  "actor": "Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)",
  "session": "PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session.",
  "failure_stop_condition": "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: the phase's own PR session/IA rescope."
}
```

```json
{
  "id": "GCF-17.LINEAGE",
  "next": ["GCF-14", "GCF-19", "GCF-20"],
  "failure_stop_condition": "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA."
}
```

```json
{
  "id": "GCF-14",
  "consumes": ["pr_instruction", "approved_implementation_plan_lineage", "current_repository", "pr_work_unit_lineage_review"]
}
```

**Two readings of the A1-1 table are confirmed** (§12 OQ-4):
- the "…" in the two `failure_stop_condition` cells keeps today's unchanged prefix;
- GCF-14's "… plus" appends `pr_work_unit_lineage_review` as the last item of `consumes`.

The values they replace, measured on the historical oracle:
```
GCF-17          failure_stop_condition  STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: same PR session/IA rescope.
GCF-17.LINEAGE  next                    ["GCF-19", "GCF-20"]
GCF-17.LINEAGE  failure_stop_condition  STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: PR session/reviewer/IA.
GCF-14          consumes                ["pr_instruction", "approved_implementation_plan_lineage", "current_repository"]
```

**What does not change, by ruling:**
- GCF-14 and GCF-15 `session`. Both are read per plan cycle (A1-1; fv-main:22; coverage:20).
- GCF-16, which already allows the re-plan (the D23 correction).
- GCF-15, which is not the stop-condition row (D23 correction; fv-rest:27).
- The PR-40 re-plan keeps the row count: 46 rows, 26 CORE and 20 MATERIAL (A1-1; fv-rest:3).

**Serialization** for both the oracle and the runtime map (A1-1; adversary:8):

```python
(json.dumps(obj, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")
```

Measured on copies, this reproduces both of today's files byte for byte:
- the oracle, 52 767 B, `52807e58…`;
- the runtime map, 45 691 B, `5574666e…`.

`sort_keys=True` does not reproduce the oracle, and neither does `ensure_ascii=True`: the oracle holds 4 non-ASCII characters. The contract's recipe (`sort_keys=True`, §6) must not be used for these two files.

**Measured result (prototype, re-measured for this v2 with the §12 choices).**
- 46 rows: 26 CORE and 20 MATERIAL. Every row has exactly the 12 fields that FMV-ORACLE-006 requires.
- The only differences from the historical oracle are `profile_id`, one entry of `required_global_tokens`, `authority`, and these ten row fields:
  - GCF-14: `consumes`, `source_row_sha256`;
  - GCF-17: `name`, `actor`, `session`, `failure_stop_condition`, `source_row_sha256`;
  - GCF-17.LINEAGE: `next`, `failure_stop_condition`, `source_row_sha256`.
- The oracle is 53 402 B and the map 46 326 B. Both sizes are fixed, because the one value still open, the matrix digest, is always 64 hex characters.

### 5.4 The successor source matrix and its digest formula (A1-1; adversary:8; coverage:10; §12 OQ-5)

**Layout** (§12 OQ-5):
1. **A short prose header.**
2. **One ```` ```json ```` fence per changed row,** three in all, in oracle row order: GCF-14, GCF-17, GCF-17.LINEAGE. Each fence holds `json.dumps(block, indent=2, ensure_ascii=False)` of a block with **exactly 12 keys**:
   - the row's 11 content fields, which are the 12 row fields minus `source_row_sha256` (`id` is one of the 11), in oracle key order;
   - then `supersedes_source_row_sha256`, the historical row's digest, last, in the place the oracle row holds `source_row_sha256`.
3. **After each block,** a line `source_row_sha256: <hex>`, giving the row digest computed by the formula below.
4. The file has no other JSON fence.

**The matrix digest is the sha256 of the file's bytes** (§12 OQ-5).

**Row digest formula (A1-1).** Its value is written into the successor oracle row's `source_row_sha256`, and displayed after the row's block:

```python
CONTENT_FIELDS = ("id", "partition", "name", "change_class", "actor", "session", "consumes",
                  "produces", "next", "approval_contract", "failure_stop_condition")
content = {k: row[k] for k in CONTENT_FIELDS}
source_row_sha256 = hashlib.sha256(
    json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
).hexdigest()
```

The formula applies only to the three successor rows. Measured over the historical content, it does not reproduce the historical digests:
- GCF-14 gives `2d89e467…`, not `4f033c4b…`;
- GCF-17 gives `018ae004…`, not `a2b761a9…`;
- GCF-17.LINEAGE gives `1e73bf70…`, not `46e1c8d0…`.

That is why the 43 kept rows are checked by equality with the historical oracle rather than by the formula (A1-1: the historical digests "cannot be recomputed").

**The three blocks and their digest lines, exactly as they follow the header.** Generated on a copy by the §5.3 recipe and the layout above (`/tmp/claude-0/v2work/succ.py`). Each `supersedes_source_row_sha256` is the historical digest; each `source_row_sha256` line is the formula's value (§5.12). One blank line separates each digest line from the next fence; that spacing, and the header, are the builder's (§5.14).

```json
{
  "id": "GCF-14",
  "partition": "CORE",
  "name": "Dedicated PR session creates the per-PR Implementation Plan",
  "change_class": "PR",
  "actor": "Dedicated PR session",
  "session": "One new work-unit session bound to one planned PR work unit; it must later implement that same unit.",
  "consumes": [
    "pr_instruction",
    "approved_implementation_plan_lineage",
    "current_repository",
    "pr_work_unit_lineage_review"
  ],
  "produces": [
    "per_pr_implementation_plan"
  ],
  "next": [
    "GCF-15"
  ],
  "approval_contract": "The PR session authors; the Product Owner later approves only by running Proceed.",
  "failure_stop_condition": "STOP_PR_INSTRUCTION_OR_REPOSITORY_CONFLICT, STOP_SCOPE_EXPANSION, or STOP_PLAN_INCOMPLETE; recovery owner: same PR session/IA for upstream scope.",
  "supersedes_source_row_sha256": "4f033c4b644dedc5589bcb3fb2a7bdec67e9ff457907f3733c101db2168f2767"
}
```
source_row_sha256: 42db7a9e614ecf943f042a9c012112fd3934f12e504cd4b980f404735b9cfe6b

```json
{
  "id": "GCF-17",
  "partition": "CORE",
  "name": "Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session",
  "change_class": "PR",
  "actor": "Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)",
  "session": "PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session.",
  "consumes": [
    "per_pr_authorized_execution_state",
    "pr_implementation_proceed_invocation",
    "pr_instruction",
    "current_repository"
  ],
  "produces": [
    "pr_or_ordered_lineage",
    "implementation_result_evidence"
  ],
  "next": [
    "GCF-17.LINEAGE",
    "GCF-17.RESCOPE",
    "GCF-19",
    "GCF-20"
  ],
  "approval_contract": "Proceed already supplied PO runtime approval. Normal repository review/evidence follows; no new PO approval binding is created.",
  "failure_stop_condition": "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: the phase's own PR session/IA rescope.",
  "supersedes_source_row_sha256": "a2b761a9bf4328cbac51afd5312fcc13b55178ea5c52d6a213678396269e8043"
}
```
source_row_sha256: 6774529046ba5050b2e62b8cf01b024766c5e99d343d0fcfdd32b0367fb99602

```json
{
  "id": "GCF-17.LINEAGE",
  "partition": "MATERIAL_BRANCH_LOOP_OR_UTILITY",
  "name": "PR Work-Unit Lineage Review",
  "change_class": "PR",
  "actor": "Responsible PR review chain",
  "session": "Review context bound to one planned work unit and its complete ordered PR lineage.",
  "consumes": [
    "pr_instruction",
    "per_pr_implementation_plan",
    "pr_implementation_proceed_invocation",
    "pr_or_ordered_lineage",
    "implementation_result_evidence"
  ],
  "produces": [
    "pr_work_unit_lineage_review"
  ],
  "next": [
    "GCF-14",
    "GCF-19",
    "GCF-20"
  ],
  "approval_contract": "Review/acceptance is evidence-based and not a new Product Owner implementation approval.",
  "failure_stop_condition": "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA.",
  "supersedes_source_row_sha256": "46e1c8d0a127afb4851f9945afd4f7d6c607e48936ea1206ef27ca9e8b1c2061"
}
```
source_row_sha256: 73a133c18b13682cbc57d813b37caacda7ed15b183437515867166bcda70e83e

### 5.5 The authority block (A1-1; adversary:7(b); coverage:10; fv-rest:6; §12 OQ-3)

**Kept verbatim** under the copy rule, in their current order:

```json
"r1_source_manifest_library_id": "libfile_e66c0851b3d88191a6d3e39e34e987c6",
"r1_contract_matrix_library_id": "libfile_9caa654f4a648191bb970b2f32970f22",
"r1_contract_matrix_sha256": "faa7fb7d77066cc491bde957b6d2f7d3255c74833936e3952f97873da27ea2f1",
"r1_frozen_snapshot_sha256": "5a6d89ed366f467ee75a5c71d23bf1a613dc79bb4d56791e812e20d53e53db67",
"r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS"
```

**Appended after them, in this order** (A1-1; §12 OQ-3):

```json
"successor_source_matrix_sha256": "<sha256 of the bytes of r1-successor-source-20260923.md>",
"successor_rows": ["GCF-14", "GCF-17", "GCF-17.LINEAGE"],
"successor_authority": "D23-D, D23-F; Product Owner 2026-09-23"
```

- `successor_rows` is in oracle row order and is compared as a set (N4).
- **Scope of the kept values.** The original matrix digest `faa7fb7d…` attests the rows not listed in `successor_rows`, that is, the 43 unchanged rows (A1-1). No scope key is added. So `EXPECTED_R1_MATRIX_SHA256` and FMV-ORACLE-003 do not move.
- `r1_frozen_snapshot_sha256`, `r1_verdict` and the two library ids attest the original matrix only. N10 pins them to their historical values and states that scope.
- The row binding lives at authority level because FMV-ORACLE-006 forbids a 13th row field (coverage:10; fv-rest:6). Because the runtime map projects `authority`, the map carries these keys too.
- No other pointer key is added. The `D23` authority is carried by `successor_authority` (§12 V-7).

The whole block, as the successor oracle and map carry it (prototype; the matrix digest is written at §5.11 step 2):
```json
{
  "r1_source_manifest_library_id": "libfile_e66c0851b3d88191a6d3e39e34e987c6",
  "r1_contract_matrix_library_id": "libfile_9caa654f4a648191bb970b2f32970f22",
  "r1_contract_matrix_sha256": "faa7fb7d77066cc491bde957b6d2f7d3255c74833936e3952f97873da27ea2f1",
  "r1_frozen_snapshot_sha256": "5a6d89ed366f467ee75a5c71d23bf1a613dc79bb4d56791e812e20d53e53db67",
  "r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS",
  "successor_source_matrix_sha256": "<MATRIX>",
  "successor_rows": [
    "GCF-14",
    "GCF-17",
    "GCF-17.LINEAGE"
  ],
  "successor_authority": "D23-D, D23-F; Product Owner 2026-09-23"
}
```

### 5.6 The runtime-map successor (A1-1; fv-rest:1; fv-main:20)

**The map is the oracle projection** that FMV-GCF-ROW-001 and FMV-GCF-MAP-005 compare against (`validate_flowmaster.py:732-760`). It is built in this key order and serialized with the §5.3 recipe:

```python
{key: oracle[key] for key in ("profile_id", "authority", "coverage", "runtime_rows")}
```

- **Measured:** today's map bytes equal this projection of today's oracle, serialized with the §5.3 recipe.
- **It is always regenerated from the successor oracle,** never edited by hand.
- **Enforcement:** FMV-GCF-ROW-001 covers the rows, FMV-GCF-MAP-005 covers `profile_id`, `authority` and `coverage`, and FMV-GCF-MAP-006 covers the digest.
- **Its digest does not depend on the `required_global_tokens` edit,** because that key is not projected (measured).

### 5.7 Checks

**Existing checks whose value moves and whose meaning stays** (fv-rest:0; fv-rest:4; fv-main:18):
- FMV-ORACLE-007, the successor oracle digest;
- FMV-ORACLE-002, the profile id;
- FMV-ORACLE-003, `faa7fb7d…`, which does not change;
- FMV-ORACLE-004 and -005, 46/26/20;
- FMV-ORACLE-006, the 12 fields;
- FMV-GCF-MAP-006, FMV-GCF-ROW-001, FMV-GCF-MAP-005 and FMV-GCF-INTERFACE-001. FMV-GCF-INTERFACE-001 passes because the successor oracle's `required_global_tokens` carries the new profile id (§12 OQ-2 (a));
- PROFILE_PROTECTED_IDENTITIES, GRAPH_PROTECTED_IDENTITIES and PROTECTED_IDENTITIES;
- R1_RUNTIME_MAP_IDENTITY, in both `validate_gcfpe_20260914.py` and `validate_gcfpe_current.py`.

**New checks N1–N10**, in `flowmaster-validate/scripts/validate_flowmaster.py` and run by the default suite (A1-1: "the suite goes on verifying the historical files' digests"; adversary:7(b); sweep:7).
- **Codes** extend the existing series (§12 OQ-1 (a)): `FMV-GCF-MAP-007` for N2, the historical map's digest, and `FMV-ORACLE-008` onward for the oracle and matrix checks, assigned here in N order.
- N2 needs the change-flow directory, which `validate_change_flow_contract` has.
- The others need the flowmaster-validate directory, which `load_change_oracle` has.

| check | code | what it asserts |
|---|---|---|
| N1 | FMV-ORACLE-008 | **Historical oracle digest** (A1-1; sweep:7, which names the constant `HISTORICAL_ORACLE_SHA256`). `flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json` hashes to `52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e`. It skips when the file is absent, leaving FMV-SKILL-STRUCTURE-001 to report it (§12 OQ-12). |
| N2 | FMV-GCF-MAP-007 | **Historical runtime-map digest** (A1-1; adversary:7(b)). `change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json` hashes to `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`. |
| N3 | FMV-ORACLE-009 | **Matrix digest** (A1-1; adversary:8). The sha256 of the bytes of `flowmaster-validate/references/r1-successor-source-20260923.md` equals `authority.successor_source_matrix_sha256`. It skips when the file is absent (§12 OQ-12). |
| N4 | FMV-ORACLE-010 | **Successor row list** (coverage:10; adversary:7(b)). `authority.successor_rows`, compared as a set, equals the set pinned in the validator, `GCF-14`, `GCF-17` and `GCF-17.LINEAGE`, with no duplicates (§12 OQ-3). This pinned set is what makes the count of kept rows exactly 43. |
| N5 | FMV-ORACLE-011 | **Matrix shape** (adversary:8). The file holds exactly three JSON blocks, whose `id`s equal the pinned set, each with exactly the 12 keys of §5.4. |
| N6 | FMV-ORACLE-012 | **Changed rows equal the matrix** (A1-1). For each pinned row, the oracle row's 11 content fields equal its block's. |
| N7 | FMV-ORACLE-013 | **Digests follow the formula** (A1-1). For each pinned row, `source_row_sha256` equals the §5.4 formula applied to the row. |
| N8 | FMV-ORACLE-014 | **Supersedes the right digest** (adversary:8). Each block's `supersedes_source_row_sha256` equals the historical row's `source_row_sha256`. |
| N9 | FMV-ORACLE-015 | **The 43 unchanged rows** (A1-1; coverage:11; adversary:7(b); §12 OQ-14). Every oracle row outside the pinned set equals the historical row with the same `id` in all 12 fields, and those rows appear in the historical order. N9 is the guard that replaces `protected_r1_46_rows_unchanged: true` (§12 V-7). |
| N10 | FMV-ORACLE-016 | **The kept attestations** (§12 OQ-3; coverage:10). `authority.r1_frozen_snapshot_sha256`, `r1_verdict`, `r1_source_manifest_library_id` and `r1_contract_matrix_library_id` equal their historical values. Its evidence text states that they attest the original matrix only. |

**The R1-literal tie check** (§12 OQ-10). A check ties `flowmaster-validate/scripts/validate_gcfpe_20260914.py`'s R1 literals (its §5.8 sites) to the digests of the successor oracle and successor map files, so they cannot fall stale. Before this check, the candidate suite passed with all of them left at `52807e58…`/`5574666e…`, because the historical files still hash to those values (v1 measurement). Its host and code are listed in §5.14.

**Must-fail regressions.** Each one mutates one thing in a scratch copy or in memory. Under §9 item 9, each must yield exactly its expected finding set. A regression marked "re-stamped" first applies this set, so that only the new check can catch it:

```
re-serialize the successor oracle (5.3) and re-derive the successor map (5.6)
validate_flowmaster.py   EXPECTED_ORACLE_SHA256, EXPECTED_CHANGE_RUNTIME_MAP_SHA256
validate_gcfpe_current.py   the installed successor-map constant (5.8)
authority.successor_source_matrix_sha256   (only when the matrix bytes change)
flowmaster-validate/SKILL.md   SKILL_TREE_SHA256
candidate-suite runs also: validation-profile :35/:37 and the validate_gcfpe_20260914.py R1 literals (5.8)
```

- **G1** (A1-1; adversary:7(c); coverage:11): edit GCF-16 `session`, set its `source_row_sha256` by the formula, and re-stamp. Expected: N9 (FMV-ORACLE-015) on GCF-16 only.
- **G2** (adversary:7(c); coverage:10): edit GCF-17 `session` in the oracle only, set its digest by the formula, and re-stamp, leaving the matrix untouched. Expected: N6 (FMV-ORACLE-012) on GCF-17 only.
- **G3** (A1-1): replace GCF-14's `source_row_sha256` with another 64-hex value and re-stamp. Expected: N7 (FMV-ORACLE-013) on GCF-14 only.
- **G4** (A1-1; adversary:7(c)): flip one byte in the matrix prose, outside the JSON blocks and the digest lines. Expected: N3 (FMV-ORACLE-009) only.
- **G5** (A1-1; sweep:7): flip one byte of `flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json` inside `generated_for_run`. Expected: N1 (FMV-ORACLE-008) only. A flip inside a historical row also fires N9 for that row (measured), which is why the location is fixed.
- **G6** (A1-1): flip one byte of `change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json`. Expected: N2 (FMV-GCF-MAP-007) only.
- **G7** (coverage:10): add GCF-16 to `authority.successor_rows` and re-stamp. Expected: N4 (FMV-ORACLE-010) only.
- **G8** (adversary:8): alter one block's `supersedes_source_row_sha256`, write the new matrix digest into `authority`, and re-stamp. Expected: N8 (FMV-ORACLE-014) only.
- **G9** (C3): evaluate the §5.10 fixture `GCF-LINEAGE-REPLAN-01` against the historical oracle. Expected: FMV-GCF-EDGE-003 only.
- **G10** (A1-2; fv-rest:2; fv-rest:3): a scratch contract with `r1_oracle_changed` false and every other pin re-stamped. Expected: PROTECTED_IDENTITIES.
- **G11** (fv-rest:4; fv-main:18): leave the profile's `r1_oracle_sha256` at `52807e58…`. Expected: exactly the two wrapper findings FMV-GCF-CANDIDATE-CONTRACT-001 and FMV-GCF-CANDIDATE-FIXTURE-PROFILE-001, which carry PROFILE_PROTECTED_IDENTITIES (§12; verifier conflict 18; measured on the v1 prototype).
- **G12** (coverage:9; sweep:7): add a link to the historical map in `change-flow/SKILL.md`. It is valid because `change-flow/SKILL.md:557` links the successor map only (§12 OQ-7 (a)). Expected (measured):
  ```
  FMV-SKILL-STRUCTURE-001  unapproved reference-file dependency: references/glow-hde-canonical-change-flow-r1-runtime-map.json
  ```
- **G13** (coverage:9): delete `flowmaster-validate/references/r1-successor-source-20260923.md`. N3 skips on an absent file (§12 OQ-12), so the one finding is (measured without N3):
  ```
  FMV-SKILL-STRUCTURE-001  missing bundled script: references/r1-successor-source-20260923.md
  ```
- **G14** (§12 OQ-3; coverage:10): change `authority.r1_verdict` in the successor oracle and re-stamp. Expected: N10 (FMV-ORACLE-016) only.
- **G15** (§12 OQ-10): in the candidate suite, leave `validate_gcfpe_20260914.py:1964` at `52807e58…` with every other pin re-stamped. Expected: a set that includes the R1-literal tie check's finding. The exact set is measured at E4 (§5.14).

**Measured (v1 prototype harness, placeholder codes).** G1 to G8 each produced exactly its one expected finding. With no mutation, the checks produced no findings on the prototype files. G14 and G15 are new in this v2 and are first measured at E4.

### 5.8 Live pin and path sites to re-point

These are the sites A1-1 calls "the live validators are re-pointed". `<SUCC_ORACLE>`, `<SUCC_MAP>` and `<MATRIX>` stand for the §5.11 digests.

**`flowmaster-validate/scripts/validate_flowmaster.py`** (adversary:7; sweep:7; coverage:9; fv-rest:0; fv-rest:7):

```
:24      ORACLE_RELATIVE = Path("references/glow-hde-canonical-change-flow-r1-20260923.json")
:25-27   CHANGE_RUNTIME_MAP_RELATIVE = Path("references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json")
:33      EXPECTED_ORACLE_PROFILE = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"
:34-36   EXPECTED_R1_MATRIX_SHA256   unchanged (faa7fb7d...)
:37-39   EXPECTED_ORACLE_SHA256 = "<SUCC_ORACLE>"
:40-42   EXPECTED_CHANGE_RUNTIME_MAP_SHA256 = "<SUCC_MAP>"
:148     "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"      (CONTRACT_REQUIRED["change-flow"])
:147     "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0"        (revision owned by §8; listed because it is in the same tuple)
:345-356 REQUIRED_SCRIPTS["flowmaster-validate"]: keep :355, add
           "references/glow-hde-canonical-change-flow-r1-20260923.json"
           "references/r1-successor-source-20260923.md"
:361-364 OPTIONAL_REFERENCES["change-flow"]: the historical map path is replaced by the successor map path
           "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
         (§12 OQ-7 (a); the 091326.2 alias leaves this list under §12 S-5; A1-6's overlay entry is §8b's)
:684-689 maintenance_metadata: "CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0" -> "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0"
         (adversary:7; today's mapped value is 3.2.9; no profile-id mapping is added, §12 OQ-2 (a))
new      N1-N10 (5.7): the historical oracle and historical map paths and digests (N1, N2); the matrix path;
         the pinned successor set (N4); the four historical authority values (N10)
```

- The `validator_revision` at `:1221` moves under §8.
- **`flowmaster-validate/SKILL.md` must not link to the matrix** as `](references/...)`. `OPTIONAL_REFERENCES` has no `flowmaster-validate` entry, so any such link fails as an unapproved reference-file dependency. The §5.8 SKILL.md lines name it in plain text.

**`flowmaster-validate/scripts/validate_gcfpe_20260914.py`** (fv-main:18; fv-main:19; fv-main:20; fv-rest:3; pr-relay-graph:30; sweep:7):

```
:1130   "r1_oracle_sha256": "<SUCC_ORACLE>"          (PROFILE_PROTECTED_IDENTITIES; :1132 r1_rows 46 kept)
:1131   "r1_runtime_map_sha256": "<SUCC_MAP>"
:1379   "r1_oracle_sha256": "<SUCC_ORACLE>"          (GRAPH_PROTECTED_IDENTITIES; r1_rows 46, r1_core_rows 26, r1_material_rows 20 kept)
:1956   "protected_r1_46_rows_unchanged": False      (§12 V-7; N9 is the replacement guard)
:1964   "r1_oracle_sha256": "<SUCC_ORACLE>"          (PROTECTED_IDENTITIES)
:1965   "r1_rows": 46, "flowmaster_primary_core_changed": False      kept
:1966   "r1_oracle_changed": True, "pr35_adds_r1_row": False          (A1-2 "flags tell the truth"; §12 V-7; pr35_adds_r1_row kept)
:2610   runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
:2611   ... sha256(runtime_map) != "<SUCC_MAP>"
new     the R1-literal tie check (§12 OQ-10; 5.7)
```

**`flowmaster-validate/scripts/validate_gcfpe_current.py`** (fv-main:21; sweep:7):

```
:80     EXPECTED_R1_SHA256           kept (52807e58...; the alias's recorded value, used at :376)
:81     EXPECTED_RUNTIME_MAP_SHA256  kept (5574666e...; the alias's recorded value, used at :376)
new     a separate installed-map constant = "<SUCC_MAP>"
:659    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
:660    compare to the new installed-map constant
```
Its default contract moves to the 091426.1 contract under §12 S-5 (§8b).

**The other sites:**

```
flowmaster-validate/scripts/run_change_flow_fixtures.py:15
        ORACLE_PATH = SKILL_DIR / "references" / "glow-hde-canonical-change-flow-r1-20260923.json"
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json
        :35 "r1_oracle_sha256": "<SUCC_ORACLE>"    :36 "r1_rows": 46 kept    :37 "r1_runtime_map_sha256": "<SUCC_MAP>"
both 091426.1 direct-handoff contract copies (change-flow/references and flowmaster-validate/references), protected_identities:
        :3114 "r1_oracle_sha256": "<SUCC_ORACLE>"    :3113 "r1_oracle_changed": true
        r1_rows 46, r1_core_rows 26, r1_material_rows 20, pr35_adds_r1_row false, flowmaster_primary_core_changed false kept
        written by the regenerator (A1-2, §6); graph_proofs.protected_r1_46_rows_unchanged (:390): false (§12 V-7)
        historical_non_executable_references gains the historical oracle and map filenames (§12 OQ-14; §6)
docs/graph/parts/global.json:555
        "r1_oracle_sha256": "<SUCC_ORACLE>"        (:551-557 otherwise kept; G16, commit 2; rebuilt per §4.9 and §6)
change-flow/SKILL.md
        :17   R1_CONTRACT_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1
        :19   R1_CONTRACT_MATRIX_SHA256 kept (faa7fb7d...)      :21 R1_ROW_COVERAGE: 46/46 kept
        :557  links the successor map only: link target references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json
              and SHA-256 `<SUCC_MAP>` (§12 OQ-7 (a); its "immutable historical baseline" prose is §8's; fv-rest:1)
flowmaster-validate/SKILL.md
        :145  R1_ORACLE_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1
        :147  kept    :149  R1_ORACLE_SHA256: <SUCC_ORACLE>
        :244  The Change oracle is the bundled file references/glow-hde-canonical-change-flow-r1-20260923.json. It pins:
        :246  - projection SHA-256 <SUCC_ORACLE>;
        new   the "It pins:" list also names the successor source matrix and its digest <MATRIX>, and the kept
              historical oracle digest 52807e58... (§12 OQ-13 (a)); wording in 5.14
        :248, :249 kept
        :9    SKILL_TREE_SHA256, last (5.11)
flowmaster-validate/fixtures/change-flow/scenarios.json
        the new scenario GCF-LINEAGE-REPLAN-01, appended at the end (5.10); :3 "oracle_profile": "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1" (§12 OQ-9)
```

**Measured in v1, default suite.** On a copy with only the `validate_flowmaster.py` constants and allowlists, `run_change_flow_fixtures.py:15`, `change-flow/SKILL.md:17` and `:557`, and `validate_gcfpe_current.py:659-660` re-pointed, the default suite returned two findings:
- FMV-GCF-INTERFACE-001, "missing mandatory interface token: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1", which the token replacement of §5.3 removes (§12 OQ-2 (a));
- SKILL_SELF_IDENTITY.

With the token replaced and a re-stamped tree it returned FLOWMASTER_SUITE_PASS, `rows_exact` true, `interfaces_closed` true, and 31/31 change-flow fixtures. With the §5.10 fixture the change-flow count becomes 32; E4 measures it.

**Measured in v1, candidate suite.** The suite (`--gcfpe-contract` with `--gcfpe-candidate-root`) also passed with `validate_gcfpe_20260914.py`, the profile, the graph and the contract still pinning `52807e58…` and `5574666e…`, because the historical files still hash to those values. The R1-literal tie check (§12 OQ-10) now catches a site left unmoved, and the §5.12 residual-hit list remains as a second check.

### 5.9 Historical sites that must not change (A1-1; sweep:8; fv-rest:8; fv-main:21; coverage:9)

**Files kept byte-identical:**

```
flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json
change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json
change-flow/references/strength-analyzer-middleware-correction.json      (:8-9)
change-flow/references/epic-alpha-repair-correction.json                 (:8-9)
change-flow/references/epic-reengineering-correction.json                (:89-90)
change-flow/references/integrated-qa-readiness-correction.json           (:6)
change-flow/references/pre-guide-audit-correction.json                   (:5)
change-flow/references/final-cycle-scan-extension.json                   (:3)
change-flow/references/alpha-feedback-correction.json
change-flow/references/gcfpe-20260912.2-direct-handoff-contract.json
change-flow/references/gcfpe-20260913.1-direct-handoff-contract.json            (:773-776)
change-flow/references/gcfpe-20260913.1-091326.2-direct-handoff-contract.json   (:808-811)
change-flow/references/gcfpe-current-direct-handoff-contract.json               (:805-808; its sha bf5140c9... is pinned at validate_gcfpe_20260914.py:2564)
```

`change-flow/references/gcfpe-current-direct-handoff-contract.json` is the 091326.2 alias. It is unlinked from `change-flow/SKILL.md` and `OPTIONAL_REFERENCES`, and its file is unchanged, as a historical record (§12 S-5).

**Historical-layer scripts, not edited.** They keep reading the historical paths:

```
validate_strength_middleware.py (:14)      validate_epic_alpha.py         validate_epic_reengineering.py
run_strength_middleware_fixtures.py        run_epic_alpha_fixtures.py
validate_integrated_readiness.py (:8, :150-151)    validate_pre_guide_correction.py (:9, :66-67)
validate_final_scan.py (:68-69)            validate_alpha_feedback.py
run_integrated_readiness_fixtures.py (:10, :40)    run_final_scan_fixtures.py (:10, :46)    run_alpha_feedback_fixtures.py
```

**Values inside live files that are not re-pointed:**

```
validate_gcfpe_current.py:80-83          validate_gcfpe_20260914.py:2564
validate_flowmaster.py:34-36             change-flow/SKILL.md:19
flowmaster-validate/SKILL.md:147, :248, :249, and the new historical-oracle mention (§12 OQ-13 (a))
```

**Measured in v1:** on the re-pointed prototype copies, all 12 historical-layer commands from §2 exited 0, and each one's output hashed the same as its baseline.

**Superseded.**
- **Step 34's verification is replaced by §5.12's residual-hit list** and the R1-literal tie check. That verification was "`grep -rc 52807e58` = 0" (fv-main:21; fv-rest:8; pr-relay-graph:30).
- **fv-main:20's re-pins at these sites are dropped:** `validate_strength_middleware.py:14`, `validate_integrated_readiness.py:8`/`:151`, `validate_pre_guide_correction.py:9`/`:67` and `validate_gcfpe_current.py:81` (sweep:8).
- **So are fv-rest:1's in-place map edit and alias `:806` re-pin, and fv-rest:2's alias re-pin** (sweep:11).
- **pr-relay-graph:30's "after the child's GCF-15 row change" does not apply:** GCF-15 does not change (D23 correction).

### 5.10 The R1 path fixture (child C3; fv-rest:27; coverage:20; sweep:7; §12 OQ-9)

It is appended as the last scenario of `flowmaster-validate/fixtures/change-flow/scenarios.json`, with id `GCF-LINEAGE-REPLAN-01`. That file is hand-formatted, and no `json.dumps` variant reproduces it, so the scenario is inserted as text in the file's existing style. The file has no hash pin; only `SKILL_TREE_SHA256` covers it. The file's top-level `oracle_profile` (`:3`) moves to `GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1`. The content:

```json
{
  "id": "GCF-LINEAGE-REPLAN-01",
  "expected_pass": true,
  "expected_rule_ids": [],
  "coverage_mode": "COMPLETE",
  "events": [{"row": "GCF-17.LINEAGE"}, {"row": "GCF-14"}]
}
```

**Measured in v1** with `validate_fixture_payload`:
- against the historical oracle, exactly `["FMV-GCF-EDGE-003"]`;
- against the successor oracle, `[]`.

Against the successor oracle, the existing 31 change-flow fixtures keep their expectations, and `graph_findings` over the successor rows is `[]`. GCF-14's new input has one producer, GCF-17.LINEAGE, and is already a declared terminal output.

### 5.11 Pin order (adversary:7(d); fv-main:16; fv-main:23; fv-rest:9; pr-relay-graph:30)

Each step writes a pin only after the bytes it pins are final. No step pins a later step's output. All of it is stage E2 (§0).

1. **Matrix.** The builder (§5.1) writes the header and the three blocks with their digest lines (§5.4). `sha256(matrix bytes)` is `<MATRIX>`. Copy the file byte for byte to `docs/prompt_ecosystem_management/r1-successor-source-20260923.md` (§12 OQ-6).
2. **Oracle.** Build it by §5.3, writing `<MATRIX>` into `authority.successor_source_matrix_sha256`. The result is `<SUCC_ORACLE>`.
3. **Map.** Derive it by §5.6. The result is `<SUCC_MAP>`.
4. **Graph.** Write `<SUCC_ORACLE>` at `docs/graph/parts/global.json:555` (G16), as **commit 2** on the execution branch (§0; §4.1). Rebuild, re-check `fecc319bdd4ce7ee6201cb77d7231861`/284 and 229 edges, record the final bytes and sha256, and write both bundled copies (§4.9; §6; §12 V-10).
   - The embedded graph keeps the commit-1 build's byte count, measured on a copy as 575 074 B (§4.2), because a 64-hex value replaces another. Only its sha256 changes. Neither `b1911cf5…` (the routing-only checkpoint) nor the commit-1 `716c4cfc…` is final.
5. **Contract, both copies.** `protected_identities.r1_oracle_sha256` becomes `<SUCC_ORACLE>`, `r1_oracle_changed` becomes true, `graph_proofs.protected_r1_46_rows_unchanged` becomes false (§12 V-7), and the step-4 graph digest goes into `source_snapshot` (regenerator, §6).
6. **Profile.** `:35` becomes `<SUCC_ORACLE>` and `:37` becomes `<SUCC_MAP>`, alongside the graph and contract pins (§6).
7. **Literals.** Every §5.8 validator constant, path and SKILL.md line except `flowmaster-validate/SKILL.md:9`.
8. **Fixtures pin.**
   - The §5.10 scenario in `flowmaster-validate/fixtures/change-flow/scenarios.json`, which has no hash pin.
   - The 091426.1 fixture pin: `EXPECTED_FIXTURE_SHA256` at `flowmaster-validate/scripts/validate_gcfpe_20260914.py:945`, which pins `flowmaster-validate/fixtures/gcfpe-20260914.1-091426.1/scenarios.json`, plus the profile's `fixtures.sha256`/`count`, for C8's edits (fv-main:29, §8b). The profile is written a second time here.
9. **`SKILL_TREE_SHA256`** at `flowmaster-validate/SKILL.md:9`, last. The change-flow package has no tree digest.

### 5.12 Prototype values and E4 items

**Determined** by the §5.3 content and the §5.4 formula, with both A1-1 readings confirmed (§12 OQ-4). Re-measured for this v2:

```
GCF-14          source_row_sha256 42db7a9e614ecf943f042a9c012112fd3934f12e504cd4b980f404735b9cfe6b
GCF-17          source_row_sha256 6774529046ba5050b2e62b8cf01b024766c5e99d343d0fcfdd32b0367fb99602
GCF-17.LINEAGE  source_row_sha256 73a133c18b13682cbc57d813b37caacda7ed15b183437515867166bcda70e83e
```

**PROTOTYPE, with the §12 choices** (`/tmp/claude-0/v2work/succ.py`; the matrix digest was a placeholder):

```
oracle      53 402 B   digest fixed only once <MATRIX> is written (5.11 step 2)
runtime map 46 326 B   digest fixed only once <MATRIX> is written (5.11 step 3)
graph      575 074 B   embedded JSON after G16; sha256 recorded at E2 (5.11 step 4)
```

The matrix's own bytes depend on its header (§5.14), so no matrix digest is quoted. v1's prototype digests (matrix `d546dac1…`, oracle `afb439b1…` and `c3861f40…`, map `c02d3d19…`, graph `7c51ed4c…`) are void. They used a placeholder authority key, single-line arrays in the matrix blocks, and a graph without the E1 non-routing edits.

**The E4 items this section owns** are in §9: item 3, the live suites; item 4, the historical layer, which must equal its baseline; and item 9, regressions G1 to G15.

The residual-hit check below, with the R1-literal tie check, replaces step 34's grep:

```
grep -rn -e 52807e58 -e 5574666e <copy>/flowmaster-validate <copy>/change-flow <repo>/docs/graph/parts
```

It must return exactly these hits:
- the §5.9 sites that carry these digests;
- `validate_gcfpe_current.py:80`/`:81`;
- the two new historical constants in `validate_flowmaster.py` (N1, N2);
- the kept historical oracle digest in the "It pins:" list of `flowmaster-validate/SKILL.md` (§12 OQ-13 (a)).

It must return no hit in:
- the successor oracle, the successor map or the matrix;
- the profile;
- the 091426.1 contracts or bundled graphs;
- `docs/graph/parts/global.json`;
- `change-flow/SKILL.md`.

For the old profile id, the check is:

```
grep -rn GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1 <copy>/flowmaster-validate <copy>/change-flow
```

It must hit only the two historical files, `flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json` and `change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json`. The successor oracle's token and `scenarios.json:3` both move to the new id (§12 OQ-2 (a), OQ-9).

### 5.13 Placement of findings

| finding | placed in |
|---|---|
| adversary:7 | §5.8 sites, §5.7 N1–N10, G1/G2/G4, §5.11 order |
| adversary:8 | §5.3 serialization, §5.4 format and formula, N5–N8, G8 |
| coverage:9 | §5.8/§5.9 live-versus-historical split; allowlists, G12/G13 |
| coverage:10 | §5.5 authority binding, N4/N5/N10, G2/G7/G14 (§12 OQ-3) |
| coverage:11 | N9, G1 |
| coverage:20 | §5.3 GCF-14/15 disposition, §5.10 |
| sweep:7 | §5.8 path sites, N1, §5.10 |
| sweep:8 | §5.9; fv-main:20 historical sites superseded |
| sweep:11 | only its fv-rest:1/fv-rest:2 part: superseded (§5.9) |
| sweep:24 | GCF-14 `consumes` (third changed row) |
| fv-main:18, fv-rest:4, fv-rest:5 | §5.8 profile, contracts, SKILL.md `:149`/`:246` |
| fv-main:19, fv-rest:3 | §5.8 `:1956` and `:1964-1966` (A1-2; §12 V-7), N9 as the kept-invariant guard |
| fv-main:20, fv-rest:1 | §5.6 successor map and its pins; in-place edit superseded |
| fv-main:21, fv-rest:2 | §5.8 `validate_gcfpe_current.py` split; alias kept as a file and unlinked (§12 S-5); grep replaced (§5.12) |
| fv-main:22, fv-rest:27 | §5.3 rows, §5.10 fixture |
| fv-rest:0, fv-rest:7 | §5.2, §5.8 |
| fv-rest:6 | §5.4/§5.5; FMV-ORACLE-003 unchanged |
| fv-rest:8 | §5.1, §5.9 |
| pr-relay-graph:30 | §5.11 step 4 |
| fv-main:23, fv-rest:9 | §5.11 step 9 |

Cross-references only, placed elsewhere: fv-main:16, fv-main:29, pr-relay-graph:20, pr-relay-graph:21 and adversary:2 (§6); coverage:15, sweep:12 and sweep:13 (§8b: the prose at `change-flow/SKILL.md:453-455` and `flowmaster-validate/SKILL.md:294` that restates GCF-17).

### 5.14 Unsettled

§12 settles §5 OQ-1 to OQ-14. What it does not settle:
1. **The matrix's prose header, and the spacing between blocks.** §12 OQ-5 fixes a "short prose header" and the block form, not the header's words or the blank lines. Both fix `<MATRIX>` and therefore `<SUCC_ORACLE>`. The builder script (§12 OQ-11 (a)) fixes them, and E5 reviews them.
2. **The builder script's path and name.** §12 says only "committed with the evidence".
3. **The code numbers within the series.** §12 OQ-1 (a) fixes the series (`FMV-ORACLE-008` onward, and `FMV-GCF-MAP-007` for N2). Assigning 008–016 to N1 and N3–N10 in N order is this v2's reading.
4. **The R1-literal tie check's host script and code** (§12 OQ-10). The check is fixed; where it runs and its code are not. It could run in `validate_gcfpe_20260914.py`, which owns the literals, or in `validate_flowmaster.py` as the next `FMV-ORACLE-` code.
5. **Regressions G14 and G15.** §12 adds N10 and the tie check without naming their regressions. This v2 compiles one each, under §12 principle 2 and §9 item 9. G15's exact expected set is measured at E4.
6. **Whether a check reads the matrix's `source_row_sha256:` lines.** §12 OQ-5 puts them in the file. N5–N8 do not read them, and §12 names no check that does. G4 therefore leaves them untouched.
7. **The wording of the new "It pins:" bullets** in `flowmaster-validate/SKILL.md` (§12 OQ-13 (a) names what they list, not the words).

## §6 Contract regenerator and value table

This section compiles A1-2 (the contract regenerator), the contract-only values that A1-2, A1-3, A1-5, A1-6 and the child's C8–C9 change, and the validator checks those values move. It replaces step 15 ("Regenerate from the graph parts; never hand-edit"), which had no tool (fv-main:17, fv-rest:12, pr-relay-graph:21). Every value cites its source. **Every value is final.** Where v1 left a value open, the §12 decision that fixes it is cited beside it (V-*, W-*). Nothing in this section is left open; what §12 does not settle is listed in 6.8.

Abbreviations: `fv` is `flowmaster-validate/scripts/validate_gcfpe_20260914.py`, `cf` is `change-flow/scripts/validate_gcfpe_20260914.py`, and `global.json` is `docs/graph/parts/global.json`.

### 6.1 Recipe (A1-2)

**Inputs**
1. **G**, the graph build. Run `graph_parts.py build` over the edited parts into scratch. Take the lines between the first line equal to ` ```json ` and the last line equal to ` ``` `, join them with `\n`, and append one `\n`. The resulting bytes are the bundled graph that §5 writes to both skills (preflight_notes fv-main tooling). Today they are 569 835 B, `90021eb7…`.
2. **T**, the template: the current 091426.1 direct-handoff contract, today `2b78f877…`, 606 657 B, byte-identical in both skills.
3. **The value table** (6.3), held as an explicit `{key path: value}` map inside the script. It is never read from the graph.

**Steps**
1. Deep-copy T.
2. Write every mirrored path in 6.2 from G. There are 42 contract paths, plus 12 fields for each of the 55 members, 702 paths in all.
3. Write each value-table entry at its path. A removal listed in 6.3 deletes the key, and a rename (W-8) deletes the old key and writes the new one.
4. Serialise:
   ```
   (json.dumps(contract, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
   ```
   Measured: this reproduces today's bytes. `ensure_ascii=True` gives 607 719 B instead (adversary:2).
5. Write the same bytes to both copies. A1-2 says the regenerator "writes both contract copies":
   ```
   flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
   change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json
   ```

**What the script enforces instead of copying**
- G has no `state_vocabularies.PF10_POST_DRAIN_VERIFICATION`, and T has no `pf10_post_drain_verification`. The validators compare this pair (fv:1287-1288) and require it absent (fv `PF10_RETIRED_DRAINAGE_PRESENT`, cf:904-907).
- The member ID set equals the graph's node ID set (fv:1238-1239, cf:831).

**No value-table entry may target a mirrored path.** Mirrored values are authored in the graph parts and reach the contract only through step 2. That applies to:
- `post_merge_three_event_contract`, including its new `observed_merge_edges` (V-2);
- `pr_development_contract.pr35_result_vocabulary`, `.added_boundaries` and `.shared_exactly_one`;
- the `member_registry` fields;
- the routing surfaces.

6.3 shows their before and after values so the whole contract delta can be reviewed. Their source of truth is `global.json` and the prompt parts.

**Pin order.** `protected_identities.r1_oracle_sha256` (6.3) and the graph's own `protected_identities` both need the successor oracle's digest. The regenerator therefore runs after the oracle is final and after the last graph build (§0 E2). Its output feeds the profile and literal re-pins (§5, pin order from adversary:7(d)).

**Where the script lives.** It is committed with the evidence and reviewed in E5 with the packages (A1-2, §10).

### 6.2 The complete mirrored key set

This set is derived from `validate_graph_contract` (fv:1172-1383) and `cf` :760-849. Each line gives the contract path, its graph source, and the validator lines that compare the two.

```
contract path                                                     <- graph source                                             compared at
selection_status                                                  <- selection_status                                         fv:1186-1190
route_edges                                                       <- edges                                                    fv:1241-1242, cf:810
state_routes                                                      <- state_routes                                             fv:1243-1244, cf:811
artifact_availability_contract                                    <- artifact_availability_contract                           fv:1245-1246, cf:762
qa_closure_contract                                               <- qa_closure_contract                                      fv:1247-1248, cf:820
boundary_nodes                                                    <- sorted(boundary_nodes)   (graph keys a dict)             fv:1250-1251, cf:814
boundary_transitions                                              <- boundary_transitions                                     fv:1252-1253, cf:815-818
terminal_contract                                                 <- terminal_contract                                        fv:1254-1255
post_merge_three_event_contract                                   <- post_merge_three_event_contract                          fv:1256-1257
transition_contract.first_line                                    <- handoff_contract.first_line                              fv:1259-1269
transition_contract.fence_language                                <- handoff_contract.fence_language                          fv:1259-1269
transition_contract.actual_branch_only                            <- handoff_contract.actual_branch_only                      fv:1259-1269
pf10_addendum_contract.exact_producer_set                         <- pf10_addendum_contract.exact_producer_set   (set)        fv:1271-1283
pf10_addendum_contract.exactly_one_per_qualifying_approval        <- pf10_addendum_contract.exactly_one_per_qualifying_approval
pf10_addendum_contract.producer_edits_pf10                        <- pf10_addendum_contract.producer_edits_pf10
pf10_addendum_contract.producer_allocates_pf10_number             <- pf10_addendum_contract.producer_allocates_pf10_number
pf10_addendum_contract.producer_claims_canonical_adoption         <- pf10_addendum_contract.producer_claims_canonical_adoption
pf10_addendum_contract.native_outcome_normalization               <- pf10_addendum_contract.native_outcome_normalization
pf10_addendum_contract.never_for                                  <- pf10_addendum_contract.never_for   (set)
authoring_context_vocabulary                                      <- state_vocabularies.AUTHORING_CONTEXT                     fv:1285-1296
pr_development_contract.pr30_result_vocabulary                    <- state_vocabularies["PR-30_RESULT"]
pr_development_contract.pr35_result_vocabulary                    <- state_vocabularies["PR-35_RESULT"]
pr_return_phase_contract.routes                                   <- state_vocabularies.PR_RETURN_PHASE
rescope_contract.decision_vocabulary                              <- state_vocabularies["RS-20_DECISION"]
pr_development_contract.r1_row                                    <- pr_continuity_contract.r1_row                            fv:1298-1316
pr_development_contract.primary_skill                             <- pr_continuity_contract.primary_skill
pr_development_contract.added_boundaries                          <- pr_continuity_contract.adds
pr_development_contract.shared_exactly_one                        <- pr_continuity_contract.shared_exactly_one   (set)
pr_development_contract.invented_session_inspection_endpoint_prohibited  <- pr_continuity_contract.(same)
pr_development_contract.unsupported_platform_limitation_claim_prohibited <- pr_continuity_contract.(same)
route_graph.prepublication_rescope                                <- pr_continuity_contract.phase_aware_rescope_sequences["PR-30_PREPUBLICATION"]
route_graph.postpublication_pr30_rescope                          <- pr_continuity_contract.phase_aware_rescope_sequences["PR-30_POSTPUBLICATION"]
route_graph.pr35_rescope                                          <- pr_continuity_contract.phase_aware_rescope_sequences["PR-35"]
abort_prompt.id                                                   <- abort_contract.prompt                                    fv:1318-1328
abort_prompt.invoker                                              <- abort_contract.manual_invoker
abort_prompt.exact_identified_pr_required                         <- abort_contract.identified_pr_required
abort_prompt.prompt_originated_inbound_edges                      <- abort_contract.prompt_inbound_edges
abort_prompt.automatic_inbound_edges                              <- abort_contract.automatic_inbound_edges
graph_proofs.route_edge_count                                     <- len(edges)                                               cf:804-808
source_snapshot.frozen_candidate_graph.sha256                     <- sha256(G bytes)                                          cf:779-782
source_snapshot.corrected_source_manifest.sha256                  <- source_bindings.source_manifest_file_sha256              cf:772
source_snapshot.corrected_source_manifest.source_snapshot_sha256  <- source_bindings.source_snapshot_sha256                   cf:773
member_registry[<id>].notion_url                                  <- nodes[<id>].candidate_url                                fv:1221-1237
member_registry[<id>].version                                     <- nodes[<id>].candidate_version
member_registry[<id>].title                                       <- nodes[<id>].title
member_registry[<id>].lane                                        <- nodes[<id>].lane
member_registry[<id>].native_function                             <- nodes[<id>].native_function
member_registry[<id>].receiving_role                              <- nodes[<id>].receiving_role
member_registry[<id>].session_class                               <- nodes[<id>].session_class
member_registry[<id>].r1_mapping                                  <- nodes[<id>].r1_mapping
member_registry[<id>].output_artifacts                            <- nodes[<id>].output_artifacts
member_registry[<id>].result_states                               <- nodes[<id>].result_states                                also cf:837-842
member_registry[<id>].predecessor                                 <- nodes[<id>].predecessor
member_registry[<id>].graph_predecessor_union_destinations        <- nodes[<id>].predecessor_union_destinations               cf:843-849
```

**Order in the set-compared lists.** The validators compare three lists as sets (marked "set" above), and the regenerator copies them in graph order. Today the graph's order equals the contract's for all three (measured). `shared_exactly_one` is also compared as an exact ordered list, against `EXPECTED_PHASE_CONTINUITY` (fv:1744). Its graph part must therefore hold the fields in that order.

**Compared, but not copied:**
- `source_snapshot.governing_plan.sha256` and the graph binding for the plan's Drive ID are each pinned to the same constant (cf:766-769, :775; fv `REPAIR_PLAN_SOURCE_PIN`), not to each other. The graph's PF10 binding is also constant-pinned (cf:776).
- `source_snapshot.frozen_candidate_graph.path` is a constant path (cf:784-786).
- The new prohibited-reference subset check (V-6) compares graph `handoff_contract.prohibited` with contract `transition_contract.prohibited_references`, but copies neither: the contract list is a value-table entry (6.3).
- These checks constrain the graph alone:
  - `GRAPH_IDENTITY`, `GRAPH_CANDIDATE_PROFILE`, `GRAPH_BASELINE_PROFILE` and `GRAPH_NODE_SET`;
  - the handoff constants (block counts 1 and 0, and `complete_paste_ready_prompt`);
  - `GRAPH_UNRESOLVED_EDGE`, `GRAPH_PR50_INBOUND_CARDINALITY`, `GRAPH_DIRECT_PR40_EDGE`, `GRAPH_UNRESOLVED_PREDICATES`, `GRAPH_PROOFS` and `GRAPH_PROTECTED_IDENTITIES` (fv:1176-1199, :1330-1382).

  Of these, `GRAPH_DIRECT_PR40_EDGE` moves with step 38 and `GRAPH_PROTECTED_IDENTITIES` moves with §5.

This set is complete for the two functions. The prototype's leave-one-out run confirms that none of the 54 entries is surplus (6.4).

### 6.3 Value table (before → after)

Before values are dumped from today's bundled contract (`2b78f877…`). After values are shown as sorted-key JSON, as serialised. Every After block below parses as JSON (6.7).

#### Contract-only keys (the regenerator's value table)

**`contract_revision`**. Source: A1-2 ("moves from 4.0.6 to 4.1.0"). Settles fv-main:35 and fv-rest:11.

Before:
```json
"4.0.6"
```
After:
```json
"4.1.0"
```

**`transition_contract`**. Sources: A1-2 ("the handoff flags follow C-HANDOFF, and `HANDOFF_CONTRACT` becomes an exact-key check"); §P C-HANDOFF; step 12; D23-B; V-6; fv-main:17, fv-rest:13, pr-relay-graph:31, adversary:3 and coverage:12.

Before:
```json
{
  "actual_branch_only": true,
  "actual_pasteable_complete_prompt": true,
  "blank_form_menu_or_reconstruction_prohibited": true,
  "block": "NEXT_PROMPT_HANDOFF",
  "epic_change_and_work_unit": true,
  "every_required_repository_and_pr_reference": true,
  "exact_destination_full_name_version_direct_notion_url": true,
  "exactly_one_per_nonterminal_result": true,
  "fence_language": "text",
  "first_line": "NEXT_PROMPT_HANDOFF",
  "metadata_only_or_routing_summary_prohibited": true,
  "next_action_and_expected_output": true,
  "prohibited_references": [
    "Library ID",
    "unlinked filename",
    "above",
    "conversation reconstruction",
    "model/strength/reasoning/eligibility/suitability/account/configuration route"
  ],
  "receiving_role_and_exact_session": true,
  "status_completed_work_decisions_constraints_unresolved_authority": true,
  "terminal_has_no_handoff": true,
  "transport": "DIRECT_NATIVE_PROMPT_HANDOFF"
}
```
After (V-6):
```json
{
  "actual_branch_only": true,
  "actual_pasteable_complete_prompt": true,
  "artifact_repository_paths_with_labels": true,
  "blank_form_menu_or_reconstruction_prohibited": true,
  "block": "NEXT_PROMPT_HANDOFF",
  "exact_destination_full_name_version_direct_notion_url": true,
  "exactly_one_per_nonterminal_result": true,
  "exceptional_context_only": true,
  "fence_language": "text",
  "first_line": "NEXT_PROMPT_HANDOFF",
  "metadata_only_or_routing_summary_prohibited": true,
  "no_branch_or_commit": true,
  "no_restated_artifact_content": true,
  "pr_reference_when_continuing": true,
  "prohibited_references": [
    "Library ID",
    "unlinked filename",
    "above",
    "conversation reconstruction",
    "model/strength/reasoning/eligibility/suitability/account/configuration route",
    "branch",
    "commit",
    "restated artifact content",
    "menu",
    "metadata-only summary",
    "blank form",
    "placeholder after publication"
  ],
  "receiving_role_and_exact_session": true,
  "terminal_has_no_handoff": true,
  "transport": "DIRECT_NATIVE_PROMPT_HANDOFF"
}
```
- **Deleted (V-6):** `status_completed_work_decisions_constraints_unresolved_authority` (D23-B reverses it), `epic_change_and_work_unit` and `next_action_and_expected_output` (step 12's required list drops them), and `every_required_repository_and_pr_reference` (replaced by C-HANDOFF's split into the two flags below).
- **Added, each `true` (V-6):** `artifact_repository_paths_with_labels`, `pr_reference_when_continuing`, `exceptional_context_only`, `no_branch_or_commit` and `no_restated_artifact_content`. They encode C-HANDOFF's positive items and its two prohibitions.
- **`prohibited_references`** keeps its five entries in order and appends seven, in V-6's order: "branch", "commit", "restated artifact content" (step 12), then "menu", "metadata-only summary", "blank form" and "placeholder after publication" (the four the graph list holds today, required by the subset check).
- **Kept.** Destination, receiving role and session, paste-ready completeness, one block per nonterminal result, and the ban on menus, "above" and reconstruction, as C-HANDOFF requires and step 12 keeps `complete_paste_ready_prompt`. No source changes the metadata-only prohibition, the transport or the terminal rule.
- **Mirrored.** `first_line`, `fence_language` and `actual_branch_only` are mirrored (6.2) and do not change.
- **The subset check holds on the After state** (measured, 6.7). Graph `handoff_contract.prohibited` gains "branch", "commit" and "restated artifact content", appended in that order (W-10), which makes it the same 12-entry set as `prohibited_references`.

**`receiver_compatibility`**. Sources: A1-2 ("PR-35's receiver entry is a dedicated top-level session; PR-40 is entered on `MERGE_OBSERVED` or, as the fallback, on Nathan's assertion"); A1-5; C9; V-4; V-5; sweep:10, sweep:21, fv-main:32 and adversary:10. `PR-30`, `RS-20`, `RS-30` and `RS-40` are unchanged (C9, sweep:21).

Before (the entries that change; `PR-20` is absent today):
```json
{
  "PR-35": {
    "context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION",
    "same_session_workspace_worktree_branch_open_pr_original_proceed": true
  },
  "PR-40": {
    "attribution_skill_read_only": true,
    "independent_actual_merged_state_and_landed_lineage_verification": true,
    "nathan_manual_merge_assertion_required": true,
    "prior_merge_pending_is_historical_premerge_evidence": true
  }
}
```
After, all seven receivers (V-5 requires the exact content of all seven):
```json
{
  "PR-20": {
    "accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"],
    "earlier_cycle_pr_is_landed_history": true,
    "existing_work_unit_replan": true,
    "new_proceed_for_new_plan": true,
    "new_top_level_session_created_by_nathan": true
  },
  "PR-30": {
    "accepted_contexts": ["PROCEEDED_PREPUBLICATION", "OPEN_PR_POSTPUBLICATION_RECOVERY"],
    "accepted_final_replay": false,
    "delta_in_force_from_turn_after_addendum_created": true,
    "overlay_approvals": ["RS-20:APPROVE", "ESC-40:APPROVE", "IA-30:QUALIFYING_DELTA_APPROVE"]
  },
  "PR-35": {
    "context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION",
    "dedicated_top_level_pr35_session": true,
    "same_workspace_worktree_branch_open_pr_original_proceed": true
  },
  "PR-40": {
    "attribution_skill_read_only": true,
    "entry_fact": "MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED",
    "independent_actual_merged_state_and_landed_lineage_verification": true,
    "prior_merge_pending_is_historical_premerge_evidence": true
  },
  "RS-20": {
    "accepted_inputs": ["RESCOPE_REQUEST", "RESCOPE_PROPOSAL"],
    "bounded_implementation_delta_only": true,
    "decision_owner": "SAME_WHOLE_CHANGE_IA"
  },
  "RS-30": {
    "invented_ia_denial": false,
    "same_artifact_type_author_and_decision_owner": true
  },
  "RS-40": {
    "accepted_approval": "RS-20:RESCOPE_REVIEW:APPROVE",
    "contexts": ["PR-30_POSTPUBLICATION", "PR-35"],
    "delta_in_force_from_turn_after_addendum_created": true,
    "original_proceed": true,
    "requires_existing_open_pr": true
  }
}
```
- **PR-20** is new, with V-5's exact value. It accepts a PR-40 `REJECT` (C9) through the string `PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT`, which follows RS-40's `accepted_approval` convention.
- **PR-35** takes sweep:10's two keys in place of the same-session key.
- **PR-40** keeps its three verification flags (sweep:10; A1-5 "PR-40 still verifies … independently"). `nathan_manual_merge_assertion_required` is deleted, and `entry_fact` carries A1-5's single fallback condition (V-4).
- **PR-30, RS-20, RS-30 and RS-40** are today's values, listed because the new check asserts all seven.
- **Negative control (V-5):** no entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` `REJECT`.

**`route_graph`**. Sources: A1-2 ("the route shorthands are revised, and the re-plan gets one"); C8 (`pr40_reject_replan`); V-4; sweep:10. The three rescope sequences are mirrored and unchanged.

Before:
```json
{
  "abort_manual_only": ["NATHAN_ABORT_INSTRUCTION", "PR-50", "NATHAN_TERMINAL_RETURN"],
  "crd_qa_pass_closure": ["QA-120", "CL-C-10", "CL-20"],
  "epic_qa_pass_closure": ["QA-120", "CL-E-10", "CL-20"],
  "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],
  "postpublication_pr30_rescope": ["PR-30", "RS-20", "RS-40", "PR-30"],
  "pr35_rescope": ["PR-35", "RS-20", "RS-40", "PR-35"],
  "prepublication_rescope": ["PR-30", "RS-20", "PR-30"],
  "rescope_revision": ["RS-20", "RS-30", "RS-20"]
}
```
After:
```json
{
  "abort_manual_only": ["NATHAN_ABORT_INSTRUCTION", "PR-50", "NATHAN_TERMINAL_RETURN"],
  "crd_qa_pass_closure": ["QA-120", "CL-C-10", "CL-20"],
  "epic_qa_pass_closure": ["QA-120", "CL-E-10", "CL-20"],
  "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],
  "postpublication_pr30_rescope": ["PR-30", "RS-20", "RS-40", "PR-30"],
  "pr35_merge_pending_fallback": ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],
  "pr35_rescope": ["PR-35", "RS-20", "RS-40", "PR-35"],
  "pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],
  "prepublication_rescope": ["PR-30", "RS-20", "PR-30"],
  "rescope_revision": ["RS-20", "RS-30", "RS-20"]
}
```
- Two keys are added, `pr35_merge_pending_fallback` (V-4) and `pr40_reject_replan` (C8). No other shorthand is added (V-4); RS-40 gets none.
- Both ordinary sequences keep `NATHAN_PROCEED` at index 2 (cf:944-945). No new value contains a `RETIRED_DRAIN_TOKENS` entry (fv:1628-1629).

**`route_graph_semantics`**. Sources: W-4, W-8; fv-main:32, coverage:13 and sweep:10. `pr35_merge_pending`, `pr50`, `qa_pass_closure` and `rs40` are unchanged; `MERGE_PENDING` stays pre-merge evidence (A1-5).

Before (the entries that change):
```json
{
  "pr40_entry": "Requires Nathan's later manual-merge assertion and PR-40's independent read-only verification.",
  "same_session_phase_continuation": "PR-30 to PR-35 is one lawful same-session phase continuation inside GCF-17, not a new work unit or cross-session route."
}
```
After (the entries that change or are added; `same_session_phase_continuation` is deleted):
```json
{
  "pr30_to_pr35_phase_continuation": "PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent.",
  "pr40_entry": "PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.",
  "pr40_reject_replan": "A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new Proceed for the new plan (D23-F)."
}
```
- `same_session_phase_continuation` is renamed `pr30_to_pr35_phase_continuation`, with W-8's value.
- `pr40_entry` is W-4's sentence, verbatim (W-8).
- `pr40_reject_replan` is new, with W-8's value.

**`pr_development_contract` (its contract-only fields)**. Sources:
- `primary_skill_revision`: A1-6 ("`glow-hde-pr-development` 1.3.0"); fv-main:25, fv-rest:26 and pr-relay-graph:16.
- `pr30_ownership`: W-8; fv-main:32; C-SESSION.
- `merge_pending_requirements`: unchanged (V-9). It keeps "no unresolved material boundary"; PART-07 converges routing sentences only, and §E records it.

Before:
```json
{
  "pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation", "deliberate initial publication", "complete same-session PR-35 handoff"],
  "primary_skill_revision": "1.2.5"
}
```
After:
```json
{
  "pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation", "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session"],
  "primary_skill_revision": "1.3.0"
}
```

**`rescope_contract.preserved_lineage`**. Source: sweep:10, which the amendment does not contradict. It fits A1-5: "RS-40 resumes the PR-35 phase in the same subscribed PR-35 session". The entry is replaced in place, at index 1. `new_proceed_required` stays `false` (C8).

Before:
```json
["PR_RETURN_PHASE", "PR_DEVELOPMENT_SESSION", "WORKSPACE", "WORKTREE", "BRANCH", "OPEN_PR_WHEN_ONE_EXISTS", "COMMIT", "ORIGINAL_PROCEED", "COMPLETED_WORK", "TESTS", "REVIEWS", "CI_STATE", "DECISION", "ARTIFACTS", "UNRESOLVED_WORK"]
```
After:
```json
["PR_RETURN_PHASE", "PR_PHASE_SESSION", "WORKSPACE", "WORKTREE", "BRANCH", "OPEN_PR_WHEN_ONE_EXISTS", "COMMIT", "ORIGINAL_PROCEED", "COMPLETED_WORK", "TESTS", "REVIEWS", "CI_STATE", "DECISION", "ARTIFACTS", "UNRESOLVED_WORK"]
```

**`preservation`: kept unchanged.** A1-2: "`versioned_sibling_successors` is kept, because it is true of how 091426.1 was made (A1-3)". A1-3 edits 091426.1 in place and applies C-VERSION from the next release, and 091426.1 itself was built as versioned siblings of 091326.2. This supersedes fv-main:31's proposal. The before and after values are identical:
```json
{
  "alpha_paused": true,
  "archive_predecessors_intact_only_after_post_promotion_validation": true,
  "automated_orchestration_activated": false,
  "delete_trash_overwrite_reset_or_reconstruct_predecessor": false,
  "predecessor_mutation_during_staging": false,
  "runtime_prompt_invoked_by_repair_implementation": false,
  "selected_predecessor_until_complete_candidate_validation_and_promotion": true,
  "versioned_sibling_successors": true
}
```

**`protected_identities`**. Sources:
- A1-2 ("the R1 identity flags tell the truth: `r1_oracle_changed: true`"); V-7;
- A1-1 (46 rows, 26 core and 20 material; the live validators are re-pointed to the successor);
- A1-6 (the Flowmaster core stays byte-identical);
- fv-main:18, fv-main:19, fv-rest:3 and adversary:7(a).

The successor digest is written in pin order (§5). **No `D23` pointer key is added** (V-7): the successor oracle's authority block carries `D23`.

Before:
```json
{
  "flowmaster_primary_core_changed": false,
  "flowmaster_primary_core_sha256": "4d8bb9bf1c9c85aeba8529995ee97b496d7938571d4b362f49c42aa9aa27d409",
  "pr35_adds_r1_row": false,
  "r1_core_rows": 26,
  "r1_material_rows": 20,
  "r1_oracle_changed": false,
  "r1_oracle_sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e",
  "r1_rows": 46
}
```
After (the digest placeholder is the one value filled at E2, in §5's pin order):
```
{
  "flowmaster_primary_core_changed": false,
  "flowmaster_primary_core_sha256": "4d8bb9bf1c9c85aeba8529995ee97b496d7938571d4b362f49c42aa9aa27d409",
  "pr35_adds_r1_row": false,
  "r1_core_rows": 26,
  "r1_material_rows": 20,
  "r1_oracle_changed": true,
  "r1_oracle_sha256": "<sha256 of flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json, §5>",
  "r1_rows": 46
}
```

**`graph_proofs.protected_r1_46_rows_unchanged`**. Sources: A1-2 ("the R1 identity flags tell the truth"); A1-1 (three rows change); V-7; fv-main:19 and fv-rest:3. The flag becomes `false` and keeps its name. §5's check N9 (the 43 unchanged rows equal the historical rows, in the same order) is its replacement guard. `pr35_same_r1_row_as_pr30` stays `true` (step 29), and `route_edge_count` is mirrored.

Before:
```json
{"pr35_same_r1_row_as_pr30": true, "protected_r1_46_rows_unchanged": true, "route_edge_count": 227}
```
After:
```json
{"pr35_same_r1_row_as_pr30": true, "protected_r1_46_rows_unchanged": false, "route_edge_count": 229}
```

#### Mirrored keys the amendment changes (authored in the graph parts, then copied)

**`post_merge_three_event_contract`** (`global.json`). Sources:
- A1-5: `direct_PR35_to_PR40_automatic_edge` stays `false`; "the observed-merge edge is recorded inside `post_merge_three_event_contract`"; no agent merges.
- A1-2: "`event_2` becomes 'observed or asserted'".
- V-2 (the record) and V-3 (`event_2`).
- sweep:10 and fv-main:13 keep `event_1` and `event_3`.
- The `D23` successor note of 2026-09-23 ("Amendment 1 approved") records that `direct_PR35_to_PR40_automatic_edge` stays `false` and that the new edges are recorded in `observed_merge_edges`. That is the Q6.20 correction, already on record.

Before:
```json
{
  "agent_merge_authorized": false,
  "direct_PR35_to_PR40_automatic_edge": false,
  "event_1": {"fact": "prior_pr35_result", "producer": "PR-35", "time": "pre_merge_historical_evidence", "value": "MERGE_PENDING"},
  "event_2": {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_assertion", "time": "later PR-40 invocation", "value": true},
  "event_3": {"consumer": "PR-40", "fact": "pr40_actual_merge_verification", "independent": true, "values": ["VERIFIED", "PENDING"]}
}
```
After:
```json
{
  "agent_merge_authorized": false,
  "direct_PR35_to_PR40_automatic_edge": false,
  "event_1": {"fact": "prior_pr35_result", "producer": "PR-35", "time": "pre_merge_historical_evidence", "value": "MERGE_PENDING"},
  "event_2": {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted", "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge", "value": true},
  "event_3": {"consumer": "PR-40", "fact": "pr40_actual_merge_verification", "independent": true, "values": ["VERIFIED", "PENDING"]},
  "observed_merge_edges": [
    {"automatic": false, "branch_id": "merge_observed", "from": "PR-35", "state": "MERGE_OBSERVED", "to": "PR-40", "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"},
    {"automatic": false, "branch_id": "merge_observed", "from": "RS-40", "state": "MERGE_OBSERVED", "to": "PR-40", "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"}
  ]
}
```
- `observed_merge_edges` is a list of two summary objects, PR-35 then RS-40 (V-2). The full edge objects stay in `route_edges`.
- `event_2` takes V-3's four values: `actor`, `fact`, `time` and `value`.

**`pr_development_contract`, mirrored fields** (`global.json` `pr_continuity_contract` and `state_vocabularies`). Sources:
- `pr35_result_vocabulary`: A1-5's ordered vocabulary; sweep:3, adversary:9 and route_sim_final.py.
- `added_boundaries`: step 29 (`session` 1) and V-1 (`cross_session_route` 1, because the PR-30 → PR-35 handoff now crosses sessions); fv-rest:15 and pr-relay-graph:28. fv-main:2 is superseded in its `cross_session_route` part only.
- `shared_exactly_one`: step 29 and fv-main:3.

Before:
```json
{
  "added_boundaries": {"approval": 0, "cross_session_route": 0, "duplicate_work_vehicle": 0, "merge_authority": 0, "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 0, "work_unit": 0, "work_vehicle": 0},
  "pr35_result_vocabulary": ["MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
  "shared_exactly_one": ["WORK_UNIT_ID", "original Product Owner Proceed", "dedicated PR-development session", "workspace/worktree", "branch", "pull request", "PR instruction", "detailed PR plan", "primary skill authority", "continuous recovery/artifact lineage"]
}
```
After:
```json
{
  "added_boundaries": {"approval": 0, "cross_session_route": 1, "duplicate_work_vehicle": 0, "merge_authority": 0, "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0, "work_vehicle": 0},
  "pr35_result_vocabulary": ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
  "shared_exactly_one": ["WORK_UNIT_ID", "original Product Owner Proceed", "workspace/worktree", "branch", "pull request", "PR instruction", "detailed PR plan", "primary skill authority", "continuous recovery/artifact lineage"]
}
```
The graph `adds` and the PR-35 node carry the same `cross_session_route: 1` (V-1). `pr30_result_vocabulary` is unchanged.

**`member_registry` mirrored fields** (the `PR-35.json` and `RS-40.json` nodes). Sources:
- PR-35 `session_class` and `receiving_role`: step 30, A1-8, W-1 and fv-main:8.
- PR-35 `native_function`: V-8.
- RS-40 `receiving_role`: W-2 (verifier conflict 16).
- `result_states`: A1-5 ("Both PR-35 and RS-40 gain it") and route_sim_final.py, which measured exactly these two node changes. The vocabulary order is A1-5's (V-12 applies the ASCII order only to the registry's `outputs[].states`).

`version`, `title` and `notion_url` are unchanged (A1-3). **No other member's mirrored field changes.** PR-20's and PR-40's roles stay (W-3): body-level C-TOP and its registry guards (§7 G18–G21) carry the rule for them.

Before:
```json
{
  "PR-35": {
    "native_function": "Continue the same proceeded PR work unit after initial publication; resolve reviews, retest, publish coherent corrections, verify current-head CI/reviews/head/mergeability, and return MERGE_PENDING without merging.",
    "receiving_role": "Same dedicated PR engineer in the same PR-development session; no new role.",
    "result_states": ["MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
    "session_class": "SAME_DEDICATED_PR_DEVELOPMENT_SESSION_AS_PR-30"
  },
  "RS-40": {
    "receiving_role": "You are the same dedicated PR engineering session for the exact suspended work unit.",
    "result_states": ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  }
}
```
After:
```json
{
  "PR-35": {
    "native_function": "Continue the same proceeded PR work unit after initial publication; resolve reviews, retest, publish coherent corrections, verify current-head CI/reviews/head/mergeability, and return MERGE_PENDING without merging; return MERGE_OBSERVED when an active subscription observes Nathan's merge.",
    "receiving_role": "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.",
    "result_states": ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
    "session_class": "DEDICATED_PR_REVIEW_SESSION"
  },
  "RS-40": {
    "receiving_role": "You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.",
    "result_states": ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  }
}
```
- The PR-35 `receiving_role` is W-1's string. It is the same string in `PR-35.json`, the contract `member_registry` and the registry `session_role` (§7.6). Its guard phrase, shared by the registry parity check (§7.7) and the new `flowmaster-validate` check on `member_registry['PR-35'].receiving_role` (§8), is:
  ```text
  never as a subagent, forked agent or workflow agent of PR-30
  ```
- RS-40's `session_class` stays `DEDICATED_ONE_OFF` (S-9).

**The routing surfaces and derived pins.**
- `route_edges`, `state_routes` and `boundary_transitions` follow A1-7. route_sim_final.py (`e0854a55…`) is the authority for the full edge objects and their positions, so they are not restated here.
- `graph_proofs.route_edge_count` goes from 227 to 229.
- `source_snapshot.frozen_candidate_graph.sha256` becomes the sha256 of the final bundled graph. That is not route-sim's `b1911cf5…`: steps 29–30, the non-routing edits and the successor oracle digest move the bytes again (§5; V-10 records the final bytes at E2).

### 6.4 Acceptance test and negative control, prototyped

The prototype is in `/tmp/claude-0/spec/s6/`, run on copies with `PYTHONDONTWRITEBYTECODE=1`. Nothing was written to the skills tree or the repository, and no `__pycache__` was created.
```
regen_contract.py   7c392c820f5091eaa852a0986f30143241d3de160b7d11b9a605883f8ac4a4c8
acceptance.py       3c71acadad925feff69ba2b1b896862d410d4d97ec72ac9165190c9ab19bedfe
after_sim.py        c0ee2a9936546275aa280ae81ed748619a834455ba3d1c3fa0bbd9f422901395
regressions.py      9ff393713d259429ca8998151139f7de7f16b550b9ca4c7f9fdbc175b9ac8f32
```
These are prototypes. The script E5 reviews is the one committed with the evidence.

**Acceptance test (A1-2): the prototype reproduces the bytes exactly.** The procedure:
1. Strip every 6.2 path from today's contract.
2. Regenerate from today's build of a copy of `docs/graph/parts`.
3. Require `2b78f877…`, 606 657 B.

```
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/claude-0/spec/s6/acceptance.py
build today                        55 nodes, 227 edges; 569835 B sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223; == bundled graph: true
paths stripped                     702  (42 contract paths + 55 members x 12 fields)
stripped template                  61859 B  sha256 8e49c365955509a5c32fd15c339d87d8a289a9ad3defab0652f77eccb6e97666
no-op on stripped == target        false   (the test is not the tautology adversary:2 warned of)
regenerated                        606657 B sha256 2b78f877e7a31efb2da8488d7f129794e60bcbdbf9f43e9851a319f83f06b53b   PASS
== both bundled copies             true
validate_graph_contract            []
validate_contract                  []
routing_surface                    7380cd14430777675f1e8b2cdfa4a0da / 282
leave-one-out                      all 42 contract paths and all 12 member fields are load-bearing
```

**Negative control (A1-2): one changed edge condition.** The prototype appended ` (negative control)` to the condition of the PR-10 → RS-10 `material_boundary` branch, in a scratch copy of the parts.
```
build                              227 edges; 569873 B sha256 7a1120701e5d3fba1f569ae487a79aad0e36892acd5ed01e0b3bb04af49e23e7
top-level keys changed             route_edges, state_routes, source_snapshot (frozen_candidate_graph.sha256 only)
regenerated vs new graph           validate_graph_contract = []
stale contract vs new graph        ["GRAPH_EDGE_CONTRACT_MISMATCH", "GRAPH_STATE_ROUTE_CONTRACT_MISMATCH"]
routing surface                    c29b6ab059111433d259612ac6fbfe44 / 282
```

**After-state measurement (v1, before §12).** The graph was route_sim_final.py's parts, with step 29–30 values and sweep:10's `event_2.fact` added. The contract was regenerated with the values v1 could determine; the values §12 later fixed were left at today's values. It is kept as a record of the routing result, not as the final after-state, which E4 measures with every 6.3 value in place.
```
route-sim parts rebuilt            574175 B sha256 b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7 (matches A1-7)
routing_surface(regenerated)       fecc319bdd4ce7ee6201cb77d7231861 / 284   (matches A1-7)
validate_graph_contract            ["GRAPH_DIRECT_PR40_EDGE"]   (graph-only check; step 38 narrows it)
validate_contract, today's fv      CONTRACT_IDENTITY, DIRECT_PR35_PR40_EDGE, GRAPH_PROOFS, HANDOFF_CONTRACT,
                                   HANDOFF_PROHIBITED_REFERENCES, POST_MERGE_THREE_EVENTS, PR35_ADDED_BOUNDARY,
                                   PR35_RESULT_VOCABULARY, PR35_STATE_ROUTES, PR40_MANUAL_MERGE_BOUNDARY,
                                   PROTECTED_IDENTITIES, PR_DEVELOPMENT_CONTRACT, PR_PHASE_CONTINUITY,
                                   ROUTE_GRAPH_SHORTHAND, ROUTING_SURFACE_CHANGED
validate_contract, scratch fv with the 6.5 expectations
                                   DIRECT_PR35_PR40_EDGE, PR40_MANUAL_MERGE_BOUNDARY   (step 38's rewrites)
```
**E4 item 2 (`validate_graph_contract == []`) cannot pass** until step 38 narrows `GRAPH_DIRECT_PR40_EDGE` to PR-30 (coverage:19, adversary:9).

### 6.5 Validator checks whose expectations move

Each moved literal gets a must-fail regression that must add exactly its own code over the clean after-state (§9 item 9). Every check below is in the v4 `validate_contract` of `fv`, reached for schema 4.0 through `validate_gcfpe_current.py:401-405` and `:619-622` (A1-6), unless a `cf` line is also given.

| check | where | what moves | regression |
|---|---|---|---|
| `CONTRACT_IDENTITY` | fv:1386-1400; cf:751 | `contract_revision` | R1 |
| `HANDOFF_CONTRACT` | fv:1482-1494 | from a subset check to: `set(transition_contract) == set(After)`, and every value except `prohibited_references` equals After (V-6) | R2a–R2e |
| `HANDOFF_PROHIBITED_REFERENCES` | fv:1495-1500 | the exact 12-entry set of 6.3 (V-6) | R3a, R3b |
| graph ⊆ contract prohibited-reference subset check (new, V-6) | `validate_graph_contract` | graph `handoff_contract.prohibited` ⊆ contract `prohibited_references` | R3c |
| `POST_MERGE_CONTRACT` | fv:1769-1771 | unchanged (both flags stay `false`, A1-5); kept guarding | R4 |
| `POST_MERGE_THREE_EVENTS` | fv:1772-1780 | `event_2`'s four V-3 values; the exact `observed_merge_edges` list (V-2) | R5a–R5c |
| `ROUTE_GRAPH_SHORTHAND` | fv:1782-1798 | the exact dict becomes 6.3's `route_graph` | R6a–R6c |
| exact-value check on `route_graph_semantics` (new, W-8) | `validate_contract` | the exact dict of 6.3's seven `route_graph_semantics` entries | R16 |
| `PR35_ADDED_BOUNDARY` | fv:1742-1743 | from "all zero" to V-1's exact map | R7a–R7c |
| `PR_PHASE_CONTINUITY` | fv:876-880, :1744-1745 | nine fields | R8 |
| `PR35_RESULT_VOCABULARY` / `PR35_STATE_ROUTES` | fv:853-856, :1747, :1921-1922; cf:1006-1011 | six values | R9 |
| `PR_DEVELOPMENT_CONTRACT` | fv:1714-1741 | `primary_skill_revision`; `pr30_ownership` joins its subset map (W-8) | R10a, R10b |
| `RESCOPE_CONTRACT` | fv:1700-1712 | `preserved_lineage` joins its subset map (W-8) | R17 |
| `PROTECTED_IDENTITIES` | fv:1959-1967 | `r1_oracle_changed`, `r1_oracle_sha256` | R11a, R11b |
| `GRAPH_PROOFS` (contract) | fv:1950-1957 | `protected_r1_46_rows_unchanged` becomes `false` (V-7) | R12 |
| `RECEIVER_CONTRACT:<id>` (new, V-5) | end of `validate_contract` | exact content of all seven receivers; one code per receiver | R13a–R13e |
| `ROUTING_SURFACE_CHANGED` | fv:207-208, :1673-1675; cf:76-77, :919-921 | the pin | R14 |
| `PRESERVATION_CONTRACT` | fv:1968-1977 | unchanged (A1-3); kept guarding | R15 |

New expectations:
```
CONTRACT_IDENTITY / cf:751     "contract_revision": "4.1.0"
HANDOFF_CONTRACT               set(transition_contract) == set(6.3 After) and
                               all(transition_contract[k] == After[k] for k in After if k != "prohibited_references")
HANDOFF_PROHIBITED_REFERENCES  set(prohibited_references) == {"Library ID", "unlinked filename", "above", "conversation reconstruction",
                                "model/strength/reasoning/eligibility/suitability/account/configuration route",
                                "branch", "commit", "restated artifact content",
                                "menu", "metadata-only summary", "blank form", "placeholder after publication"}
subset check (graph)           set(graph handoff_contract.prohibited) <= set(contract transition_contract.prohibited_references)
POST_MERGE_THREE_EVENTS        event_2 == {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted",
                                "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge",
                                "value": True};
                               observed_merge_edges == the two-object list of 6.3, in order (PR-35, RS-40);
                               event_1 and event_3 unchanged
ROUTE_GRAPH_SHORTHAND          route_graph == 6.3 After (ten keys)
route_graph_semantics check    route_graph_semantics == {"pr30_to_pr35_phase_continuation": <W-8>, "pr35_merge_pending": <today>,
                                "pr40_entry": <W-4>, "pr40_reject_replan": <W-8>, "pr50": <today>, "qa_pass_closure": <today>, "rs40": <today>}
PR35_ADDED_BOUNDARY            added_boundaries == {"approval": 0, "cross_session_route": 1, "duplicate_work_vehicle": 0, "merge_authority": 0,
                                "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0, "work_vehicle": 0}
EXPECTED_PHASE_CONTINUITY      ["WORK_UNIT_ID", "original Product Owner Proceed", "workspace/worktree", "branch", "pull request",
                                "PR instruction", "detailed PR plan", "primary skill authority", "continuous recovery/artifact lineage"]
EXPECTED_PR35_RESULTS / cf     ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
PR_DEVELOPMENT_CONTRACT        "primary_skill_revision": "1.3.0";
                               "pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation",
                                "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session"]
RESCOPE_CONTRACT               "preserved_lineage": 6.3 After (15 entries, PR_PHASE_SESSION at index 1)
PROTECTED_IDENTITIES           "r1_oracle_changed": True, "r1_oracle_sha256": <successor oracle sha256>; all other values unchanged
GRAPH_PROOFS                   "protected_r1_46_rows_unchanged": False
RECEIVER_CONTRACT:<id>         for id in sorted(set(EXPECTED_RECEIVERS) | set(receiver_compatibility)):
                                 receiver_compatibility.get(id) == EXPECTED_RECEIVERS.get(id), else RECEIVER_CONTRACT:<id>
                               EXPECTED_RECEIVERS == 6.3 After, all seven entries
EXPECTED_ROUTING_SURFACE       "fecc319bdd4ce7ee6201cb77d7231861", EXPECTED_ROUTING_SURFACE_ROWS = 284   (fv and cf)
```

Must-fail regressions. Each mutates the clean after-state contract (or, for R3c, the graph) in memory and must add exactly the named code. "Measured" marks those run by the v1 prototype; the others are measured at E4.
```
R1   contract_revision = "4.0.6"                                              -> CONTRACT_IDENTITY; cf: FAIL corrected-source contract revision   (measured)
R2a  transition_contract["status_completed_work_decisions_constraints_unresolved_authority"] = True  -> HANDOFF_CONTRACT   (measured)
R2b  transition_contract["epic_change_and_work_unit"] = True                  -> HANDOFF_CONTRACT   (measured)
R2c  transition_contract["actual_pasteable_complete_prompt"] = False          -> HANDOFF_CONTRACT   (existing fixture reject-incomplete-handoff; measured)
R2d  del transition_contract["no_branch_or_commit"]                           -> HANDOFF_CONTRACT
R2e  transition_contract["every_required_repository_and_pr_reference"] = True -> HANDOFF_CONTRACT
R3a  transition_contract["prohibited_references"].remove("branch")            -> HANDOFF_PROHIBITED_REFERENCES   (measured)
R3b  transition_contract["prohibited_references"].append("next action")       -> HANDOFF_PROHIBITED_REFERENCES
R3c  graph handoff_contract["prohibited"].append("next action")               -> the subset check
R4   post_merge_three_event_contract["direct_PR35_to_PR40_automatic_edge"] = True  -> POST_MERGE_CONTRACT   (measured)
R5a  post_merge_three_event_contract["event_2"]["fact"] = "product_owner_manual_merge_assertion"  -> POST_MERGE_THREE_EVENTS   (measured)
R5b  post_merge_three_event_contract["event_2"]["time"] = "later PR-40 invocation"               -> POST_MERGE_THREE_EVENTS
R5c  del post_merge_three_event_contract["observed_merge_edges"][1]                              -> POST_MERGE_THREE_EVENTS
R6a  route_graph["ordinary_pr_work_unit"] = ["PR-10","PR-20","NATHAN_PROCEED","PR-30","PR-35","NATHAN_MANUAL_MERGE_ASSERTION","PR-40"]  -> ROUTE_GRAPH_SHORTHAND   (measured)
R6b  del route_graph["pr40_reject_replan"]                                    -> ROUTE_GRAPH_SHORTHAND   (measured)
R6c  del route_graph["pr35_merge_pending_fallback"]                           -> ROUTE_GRAPH_SHORTHAND
R7a  added_boundaries["session"] = 0                                          -> PR35_ADDED_BOUNDARY   (measured)
R7b  added_boundaries["proceed"] = 1                                          -> PR35_ADDED_BOUNDARY   (existing fixture reject-new-proceed-boundary; measured)
R7c  added_boundaries["cross_session_route"] = 0                              -> PR35_ADDED_BOUNDARY   (V-1's negative fixture)
R8   shared_exactly_one.insert(2, "dedicated PR-development session")         -> PR_PHASE_CONTINUITY   (measured)
R9   pr35_result_vocabulary.remove("MERGE_OBSERVED")                          -> PR35_RESULT_VOCABULARY; cf: FAIL PR-35 results   (measured)
R10a primary_skill_revision = "1.2.5"                                         -> PR_DEVELOPMENT_CONTRACT   (measured)
R10b pr30_ownership[5] = "complete same-session PR-35 handoff"                -> PR_DEVELOPMENT_CONTRACT
R11a protected_identities["r1_oracle_changed"] = False                        -> PROTECTED_IDENTITIES   (measured)
R11b protected_identities["r1_oracle_sha256"] = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"  -> PROTECTED_IDENTITIES   (measured with an all-zero digest; exact once the successor exists)
R12  graph_proofs["protected_r1_46_rows_unchanged"] = True                    -> GRAPH_PROOFS   (measured)
R13a receiver_compatibility["PR-30"]["accepted_inputs"] = ["PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"]  -> RECEIVER_CONTRACT:PR-30   (the V-5 negative control)
R13b receiver_compatibility["PR-35"]["same_session_workspace_worktree_branch_open_pr_original_proceed"] = True  -> RECEIVER_CONTRACT:PR-35
R13c receiver_compatibility["PR-40"]["nathan_manual_merge_assertion_required"] = True  -> RECEIVER_CONTRACT:PR-40
R13d del receiver_compatibility["PR-20"]                                      -> RECEIVER_CONTRACT:PR-20
R13e receiver_compatibility["RS-40"]["accepted_approval"] = "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"  -> RECEIVER_CONTRACT:RS-40
R14  route_edges[0]["route_branches"][0]["condition"] += " x"                 -> ROUTING_SURFACE_CHANGED   (measured)
R15  preservation["versioned_sibling_successors"] = False                     -> PRESERVATION_CONTRACT   (measured)
R16  route_graph_semantics["same_session_phase_continuation"] = route_graph_semantics.pop("pr30_to_pr35_phase_continuation")  -> the route_graph_semantics check
R17  rescope_contract["preserved_lineage"][1] = "PR_DEVELOPMENT_SESSION"      -> RESCOPE_CONTRACT
```
The §8b fixture runner (O29) carries the same mutations as scenarios; §8b's regression names map onto these.

**Checks the mirrored values move, specified elsewhere.** They are listed here so that no moved literal goes unowned.
- **Step 38** (coverage:19, adversary:9, fv-rest:20; §8b 8b.7 rules 5–6):
  - `DIRECT_PR35_PR40_EDGE` (fv:1837-1838);
  - `GRAPH_DIRECT_PR40_EDGE` (fv:1349-1355);
  - `PR40_MANUAL_MERGE_BOUNDARY` (fv:1924-1948), which rejects the new PR-35 → PR-40 and RS-40 → PR-40 prompt edges until rule 6 removes them from its recovery list.
- **The PR-35 role literal** on `member_registry['PR-35'].receiving_role`, the W-1 guard phrase above (§8b).
- **Pin chain, §5:**
  - cf:806's edge count of 227 becomes 229;
  - the bundled-graph pins (cf:21, :777, :781; fv:941-942);
  - the contract byte pins (fv:943-944; profile);
  - the graph's `GRAPH_PROTECTED_IDENTITIES` (fv:1375-1382).
- **§8:**
  - the skill-text literals at cf:1020-1023;
  - the fixture runner's `pr_split` positive case, which requires every `added_boundaries` value to be zero (runner:66-70; fv-main:6) and now takes V-1's map;
  - `reject-pr35-direct-pr40` (runner:361).

### 6.6 Finding dispositions placed here

- **Placed fully:**
  - fv-main:3, :4, :8, :10, :13, :14, :17, :19, :32, :35;
  - fv-rest:3, :12, :13, :15;
  - pr-relay-graph:21, :28, :31;
  - coverage:12, :13; sweep:10, :21; adversary:2, :3, :10.
- **Placed with a partial supersession:** fv-main:2. Its exact-map check is placed; its `cross_session_route: 0` is superseded by V-1.
- **Superseded by A1-2/A1-3:** fv-main:31 (`preservation` is kept).
- **Placed for the contract part only, with the rest in §5 or §8:**
  - fv-main:18 and fv-rest:11 (contract pins);
  - fv-main:25, fv-rest:26 and pr-relay-graph:16 (`primary_skill_revision`);
  - fv-rest:21, sweep:3 and adversary:9 (the vocabulary mirror);
  - fv-rest:20 (the `POST_MERGE_*` half).
- **sweep:10's literals worded on "no subscription"** (`pr35_no_subscription_fallback`, `OBSERVED_MERGE_EVENT_OR_NATHAN_ASSERTION_WHERE_NO_SUBSCRIPTION`, and "else asserted" in `event_2.time`) are superseded by V-3 and V-4, which word them on A1-5's single condition.

### 6.7 Measured (v2 consolidation)

Run on 2026-09-23 with `PYTHONDONTWRITEBYTECODE=1`. Nothing was written outside this file and `s7.md`.
- All 24 ```` ```json ```` blocks in this section parse (`json.loads`). The `protected_identities` After block is fenced without `json`, because it holds the E2 placeholder.
- The After `transition_contract` has 18 keys: today's 17, less the four deleted, plus the five added.
- The After `route_graph` has 10 keys. Its eight kept keys equal today's values, except `ordinary_pr_work_unit`, which drops `NATHAN_MANUAL_MERGE_ASSERTION`.
- The After `route_graph_semantics` has seven keys: today's six, with `same_session_phase_continuation` renamed and `pr40_reject_replan` added.
- Graph `handoff_contract.prohibited` today holds 9 entries. With W-10's three appended, its set equals the 12-entry After `prohibited_references` set, so the subset check passes on the After state and R3c fails it.
- Today's `receiver_compatibility` (read from the bundled contract, `2b78f877…`) holds six receivers. The After map holds seven. Its PR-30, RS-20, RS-30 and RS-40 entries equal today's, and only PR-20 contains `PR_WORK_UNIT_LINEAGE_REVIEW`.
- The regenerator and the regressions R2d, R2e, R3b, R3c, R5b, R5c, R6c, R7c, R10b, R13a–R13e, R16 and R17 were not re-run for this consolidation. E4 runs them on the final after-state.

### 6.8 Unsettled

§12 does not settle these. EXECUTE brings each to Nathan before it relies on it (§0).
1. **The code name of the new `route_graph_semantics` exact-value check** (W-8 orders the check; no section names it).
2. **The code name of the graph ⊆ contract subset check** (V-6 adopts it, and §8b O32 (b) calls it "a new graph-parity code"; no name is given).
3. **Where three W-8 and V-2/V-3 checks live.** This section places `pr30_ownership` in `PR_DEVELOPMENT_CONTRACT`, `preserved_lineage` in `RESCOPE_CONTRACT`, and the `event_2` and `observed_merge_edges` literals in `POST_MERGE_THREE_EVENTS`. That follows §12 principle 5 (the smallest edit), because each value sits inside the object those codes already check. §12 itself names no code for them.

## §7 Registry: guards, derived fields, dispositions

This section compiles every change to `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` in this run:
- the guards, which are the `D14` tested guards that `D23` requires for each ruling ("Until those land, `D23` is ruled but not applied");
- the `D13` fields the registry deriver rewrites;
- the authored row edits;
- the N1 and N2 dispositions (S-2);
- the edit method.

The registry is repository work, so it goes on the execution branch in E1 (§0; A1-4 item 1; child *Order*, "C5 with E1"). **Every value is final.** Where v1 left a choice open, the §12 decision that fixes it is cited beside it. What §12 does not settle is listed in 7.12, and EXECUTE brings it to Nathan (§0).

**Baseline, measured today.**
- 5301 lines, sha256 `c5ae188834d5154826b1bc723a89712cebe4631bee296c56ec856b3947e1d1f7` (re-measured for v2).
- 55 rows and 831 assertions.
- `validate_project_prompt_registry.py` returns `{"valid": true, "problems": []}`, exit 0.

**Precedence.** The amendment governs §P, and it also governs the preflight rows and critic findings. Two consequences:
- **Superseded premise.** Wherever a finding assumes that `direct_PR35_to_PR40_automatic_edge` becomes `true` (registry-audit:10, :12), A1-5 supersedes that premise. The derived values below follow from the graph edges only.
- **Superseded C-SUB and C-DISPATCH.** §P's C-SUB and C-DISPATCH are superseded by A1-5's versions. Where they are tested below, it is only as retired text.

### 7.1 Conventions

**The evaluator.** Every guard below is evaluated by the audit skill's own function, imported from a scratch copy of `amthor-workspace-governance-audit` (registry-audit notes; adversary:15; `audit_workspace_governance.py:520-545`, sha256 `c4ca7f60…`):

```
_evaluate_assertions(record, text, source_ref)
required_regex : finding when not re.search(value, text, flags=re.MULTILINE)   summary "Required pattern absent: " + value
forbidden_regex: finding when re.search(value, text, flags=re.MULTILINE)       summary "Forbidden pattern matched: " + value
compared key   : (f["rule_id"], f["observed"]["summary"])
```

- The evaluator applies no DOTALL flag. It applies no IGNORECASE flag either, except where a value opens with an inline `(?i)`.
- `\A` still anchors at the start of the text under `re.MULTILINE`.
- Every finding is `ERROR`, whatever its `rule_id`.

**Entry form in the file.** Each new entry is appended after the last entry of the row's `audit_assertions.<list>:`. Its value is single-quoted, and every `'` inside it is doubled:

```
    - value: '<value>'
      rule_id: <RULE_ID>
```

Every entry in 7.3 is given in this form. For each, `yaml.safe_load` returns exactly `[{"value": <value>, "rule_id": <RULE_ID>}]` (7.10).

**Row selectors.**
- **ALL55.** Every row.
- **MAIN54.** Every row except `GCFPE-MGMT-10` (A1-8; the `D23` clarification). The triage prompt is not a registry row, so its successor note changes nothing here.
- **NPH53.** The rows whose `required_literals` contain `NEXT_PROMPT_HANDOFF` (registry-audit:2). They measure 53:
  - `PR-35` is in the set, although its literal carries `CTR-002` rather than `TOP-001`;
  - the two rows outside it are `GCFPE-MGMT-10` and `PR-50`;
  - the set is the complement of `flowmaster-validate`'s `HANDOFF_LITERAL_EXEMPT`.

  Selecting on `rule_id` `TOP-001` gives 52 rows and drops PR-35, so that selector must not be used. The selector code:

```
[r["prompt_key"] for r in reg["prompts"]
 if any((x.get("value") if isinstance(x, dict) else x) == "NEXT_PROMPT_HANDOFF"
        for x in (r["audit_assertions"].get("required_literals") or []))]
```

- **STEP5.** `CF-C-10`, `CF-C-20`, `CF-C-30`, `CF-C-40`, `CF-E-10`, `CF-E-20`, `CF-E-30`, `CF-E-40`, `CF-PO-10` and `MGR-10` (step 5).
- **LAT10.** `PR-10`, `PR-20`, `PR-30`, `PR-35`, `PR-40`, `RS-10`, `RS-20`, `DOC-10`, `DOC-20` and `IA-30` (step 22).
- **ASK4.** `QA-60`, `QA-80`, `RS-10` and `RS-30`, the four bodies that end `ASK OK?` (step 18).

**Must-fail regression criterion** (E4 item 9; registry-audit:1; §9). `F` evaluates the whole edited row, which carries several assertions under one `rule_id`. So the value, not the `rule_id` alone, identifies the guard.

```
set(F(row, mutated)) - set(F(row, clean)) == {(rule_id, "Required pattern absent: " + value)}     # required guard
set(F(row, mutated)) - set(F(row, clean)) == {(rule_id, "Forbidden pattern matched: " + value)}   # forbidden guard
```

**Canonical texts used for testing.** They are §3's final strings with §12 applied:
- §P: C-NOTION, C-ART, C-HANDOFF, C-PLACE, C-DEC, C-LAT, C-VERSION and C-D22;
- A1-5: C-SUB and C-DISPATCH;
- A1-8: C-TOP, and C-SESSION with the A1-8 sentence appended and the backticks dropped (W-6);
- A1-6: the GCFPE override; the governance-audit invariant;
- the child: C-REPLAN, C-PROCEED, C-PR20-ENTRY and C-PR30-ENTRY;
- W-5's `ASK OK?` variant of C-PLACE;
- the literals of steps 2, 4 and 22;
- the §12 strings: W-1's PR-35 role, W-2's RS-40 role and creator role, W-4's PR-40 entry sentence and PR-35-result input, the PR-20 input without backticks, W-8's two semantics texts, W-9's `GCF-14` line and relay sentence, S-6's and S-7's relay sentences, S-2's N2 sentence and the scope line.

The 16 texts that §P, A1-5, A1-6, A1-8 and the child define were also tested in their hard-wrapped source form. §P's retired C-SUB and C-DISPATCH, and C-SESSION with §P's backticks, were tested as retired or variant text.

### 7.2 Step 43, first half: the release-identity requirements are removed from all 55 rows

Steps 41–43 run in this cut-over (S-1). These two entries are deleted from every row's `required_regex`. Each is an exact two-line pair (registry-audit:5; `D23-G`):

```
    - value: 'Prompt [Vv]ersion: `?091426\.1`?'
      rule_id: SRC-001
    - value: 'Ecosystem release: `?GCFPE-20260914\.1`?'
      rule_id: INV-003
```

§E records this as moving the release binding to the register (step 44), not as keeping it. Afterwards, the only release binding inside the audit is `expected_title` "— 091426.1", checked by `NAM-001` at WARNING severity and only when a title is supplied (registry-audit:5, invariant note; §E carries the note).

### 7.3 The guards

Every value below was tested on a scratch copy (7.10):
- It compiles.
- It round-trips through YAML single quotes.
- A required value matches its home text, joined and, where a source form exists, wrapped, and matches no other canonical body text.
- A forbidden value matches no canonical text in either form. It also matches none of the seven combined paragraphs below and none of the 20 worker or negated phrasings, which include the four the brief names:
  ```text
  use subagents as workers within this task
  spawn worker subagents for parallel reads within this session
  Run PR-35's tests in a subagent.
  Nathan creates a new session for PR-40 and pastes the handoff.
  ```
  - The combined paragraphs are: C-PLACE + C-HANDOFF + C-SESSION + C-TOP; a handoff rule + C-HANDOFF + C-PLACE + C-TOP; C-PLACE + C-SESSION; C-DISPATCH + C-SUB + C-TOP; a handoff rule + C-HANDOFF + the `ASK OK?` variant + C-TOP; C-REPLAN + C-PROCEED + C-PR30-ENTRY + C-TOP; and one 4004-character paragraph of a handoff rule, C-HANDOFF, C-SESSION, C-DISPATCH, C-SUB, C-PLACE, C-TOP, C-PROCEED, C-REPLAN and W-4's entry sentence.
- Every regression gives exactly its own finding from the real evaluator.

| id | ruling | step or item | list | rule_id | rows | source |
|---|---|---|---|---|---|---|
| G01 | Notion policy (Class B) | 7 | forbidden_regex | CTR-001 | ALL55 | step 7; registry-audit:6 |
| G02 | Notion policy | 7, functional companion | forbidden_regex | CTR-001 | ALL55 | registry-audit:6 as corrected by adversary:6 |
| G03 | Notion policy | 4 | forbidden_regex | CTR-001 | QA-10 | registry-audit:6 |
| G04 | Notion policy | 5 | forbidden_regex | CTR-001 | STEP5 (§12 G04) | registry-audit:6 |
| G05 | D23-A | 11 | required_regex | CTR-002 | NPH53 | step 11; registry-audit:2, :4 |
| G06 | D23-B content | 17 | forbidden_regex | TOP-001 | NPH53 | registry-audit:3 and notes; adversary:19; window per §12 G06 |
| G07 | D23-B placement | 18–19 | required_regex | TOP-001 | NPH53 | registry-audit:12 notes; unique anchor per §12 masking |
| G08 | D23-B, `ASK OK?` old wording | 18–19 | forbidden_regex | CTR-002 | ASK4 | registry-audit:12 notes; adversary:14; W-5 |
| G08A | D23-B, `ASK OK?` placement | 18–19 | required_regex | TOP-001 | ASK4 | W-5 |
| G09 | D23-C | 21 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | step 21 as corrected by adversary:5 |
| G10 | D23-C | 25 | required_regex | CTR-002 | LAT10 | step 25; registry-audit:12 notes |
| G11 | D23-C definition | 25 | required_regex | CTR-002 | LAT10 | registry-audit notes |
| G12 | D23-G | 43 | forbidden_regex | SRC-001 | ALL55 | registry-audit:5 and notes; decorated prefix per §12 |
| G13 | D23-G | 43 | forbidden_regex | INV-003 | ALL55 | registry-audit:5 and notes; decorated prefix per §12 |
| G14 | D23-G (`Set:`) | 43 | forbidden_regex | SRC-001 | ALL55 | registry-audit:5 and notes; decorated prefix per §12 |
| G15 | D23-D, old continuity list | N3 | forbidden_regex | CTR-001 | MAIN54 (§12 G15) | registry-audit:12 notes |
| G16 | D23-D | N3 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | registry-audit:12 notes |
| G17 | D23-D, A1-8 clause | N3 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | A1-8; coverage:5; adversary:5; W-1 |
| G18 | C-TOP required | N3 | required_regex | CTR-002 | MAIN54 | A1-8; coverage:5; adversary:5 |
| G19 | C-TOP forbidden F1 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0; possessive exclusion per §12 |
| G20 | C-TOP forbidden F2 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0; `Nathan` exclusion per §12 |
| G21 | C-TOP forbidden F3 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0, without `send_later` |
| G22 | D23-E, withdrawn launch | N3 | forbidden_regex | CTR-001 | PR-35, RS-40 | coverage:1 |
| G23 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40 | registry-audit:12 notes; adversary:4 |
| G24 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40 | registry-audit:12 notes; adversary:4; unique anchor per §12 masking |
| G25 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40 | registry-audit:12 notes; adversary:4; unique anchor per §12 masking; PR-40 in 7.12 |
| G26 | D23-F | child C5 | forbidden_regex | CTR-001 | PR-40 | child C5 |
| G27 | D23-F | child C5 | required_regex | CTR-002 | PR-20 | child C5 |

Each value below is quoted verbatim from its source, with the §12 correction applied where the table says so. Two values differ from the text of their finding:
- **G02** is adversary:6's corrected form, with `(?i)`.
- **G21** drops `send_later` from adversary:0's F3. A1-8 forbids "naming a session-creating tool", and `send_later` schedules a message into the same session and creates nothing.

G19 and G20 use this prompt-id group, adversary:0's `<PID>` expanded:

```
(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
```

#### Notion policy: G01–G04 (steps 3–5 and 7)

```
    - value: 'CONTROL_NOTION'
      rule_id: CTR-001
    - value: '(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b'
      rule_id: CTR-001
```

G01 and G02 go on ALL55, and both are silent on C-NOTION.

- **G01 regression**, on PR-10. Append the sentence below. It yields only G01's finding, because G02 does not match `` `CONTROL_NOTION` ``.

```text
Concise authorized operational state and pointers remain `CONTROL_NOTION`.
```

- **G02 regression**, on PR-10 (adversary:6). Append:

```text
Operational state and pointers stay in Notion.
```

G03 goes on QA-10 only:

```
    - value: 'Notion and repository persistence'
      rule_id: CTR-001
```

- G03 is silent on step 4's replacement, "repository persistence, Notion read-only unless a destination rule names the page".
- **G03 regression**, on QA-10. Append:

```text
Use Notion and repository persistence for results.
```

G04 goes on the 10 STEP5 rows (§12 *Registry guards*, G04):

```
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
```

- **G04 regression**, on CF-C-10. Insert this sentence after the handoff sentence:

```text
Name each input artifact by repository path, or its direct Notion URL for a Notion-resident artifact.
```

The step-7 note puts G03 and G04 in `forbidden_regex`, the list its step-7 entries use. The registry has 0 `forbidden_literals` entries today.

#### D23-A: G05 (step 11), on NPH53

```
    - value: 'never\s+carries\s+the\s+only\s+copy'
      rule_id: CTR-002
```

- **Home: C-ART.** The pattern matches C-ART with the §P wrap between "never" and "carries", and without it.
- **Regression**, on PR-35. Delete C-ART.

#### D23-B: G06 (step 17), G07, G08 and G08A (steps 18–19)

G06 goes on NPH53. Its window is `{0,1500}?` (§12 *Registry guards*, G06):

```
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
```

- **Clean.** G06 is silent on every canonical text and on the seven combined paragraphs. It is silent on C-HANDOFF's "It carries no branch and no commit" and on C-SESSION's "workspace/worktree".
- **Regressions**, on PR-35. Each is a separate mutation that yields only G06's finding. Insert the sentence below (a) immediately after the sentence that contains `NEXT_PROMPT_HANDOFF`, and (b) at the end of the C-HANDOFF paragraph, 785 characters from the token. The limit is in 7.4.

```text
 It carries the same session, worktree, branch, PR and head commit.
```

G07 goes on NPH53. It anchors on C-PLACE's first sentence, which appears only in the canonical texts (§12 masking):

```
    - value: 'The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.'
      rule_id: TOP-001
```

- **Home: C-PLACE**, and W-5's `ASK OK?` variant, which keeps C-PLACE verbatim.
- **Regression**, on PR-35 and on QA-60. Delete the sentence `The final response ends with the `NEXT_PROMPT_HANDOFF` block.`

G08 and G08A go on ASK4 (W-5, option (c): both parts).

G08 forbids the old wording:

```
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
```

- **Clean.** G08 is silent on C-PLACE and on the `ASK OK?` variant ("`ASK OK?` is the line immediately before the block.").
- **Regression**, on QA-60. Append:

```text
The final response must end `ASK OK?`.
```

G08A requires the variant's added sentence:

```
    - value: '`ASK OK\?` is the line immediately before the block\.'
      rule_id: TOP-001
```

- **Home: the `ASK OK?` variant.** It matches no other canonical text.
- **Regression**, on QA-60 and on RS-30. Delete the sentence `` `ASK OK?` is the line immediately before the block. ``
- **Limit (W-5).** G08A proves the sentence is present. It cannot prove that the output puts `ASK OK?` on the line before the block; §E records that this ordering can be checked only on outputs.

#### D23-C: G09 (step 21), G10 and G11 (step 25)

G09 goes on PR-30, PR-35 and RS-40:

```
    - value: 'An\s+\*?In-flight decisions\*?\s+section'
      rule_id: CTR-002
```

- **Home: C-DEC.** It does not match C-LAT's "record it under *In-flight decisions*". That is why the literal `In-flight decisions` from step 21 is not used: C-LAT masks it on PR-30 and PR-35 (adversary:5).
- **Regression.** Delete C-DEC, on PR-35, where C-LAT is also present, and on RS-40.

G10 and G11 go on LAT10:

```
    - value: 'Decide it during work'
      rule_id: CTR-002
    - value: '\*{0,2}Material\*{0,2} means a change to the Epic-level commitment'
      rule_id: CTR-002
```

- **Home: C-LAT.** Neither pattern matches the step-22 literal or the A1-7 conditions.
- **Regressions**, on PR-35. Each is a separate mutation, so each yields one finding:
  - **G10:** delete only the line `**Decide it during work:**`;
  - **G11:** delete only C-LAT's first paragraph, the definition.
- **Do not add** a forbidden "material boundary" (registry-audit notes).

#### D23-G: G12–G14 (step 43, second half), on ALL55

Each pattern uses the verifier's decorated-header prefix (§12 *Registry guards*, regex error 2) and is windowed to the first 8 nonblank lines of the body. That is `flowmaster-validate`'s header window (§8b `PROMPT_BODY_RELEASE_HEADER`), and it is where step 42 deletes the lines. The prefix is:

```
\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?
```

and the key is followed by:

```
(?:\*\*|__|`)?[ \t]*:
```

The three entries:

```
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Prompt [Vv]ersion(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Ecosystem release(?:\*\*|__|`)?[ \t]*:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?Set(?:\*\*|__|`)?[ \t]*:'
      rule_id: SRC-001
```

- **Caught.** Each catches all 12 decorated forms of its key in the header window: plain, `**K:**`, `**K**:`, `- K:`, `* K:`, `> K:`, `` `K:` ``, `| K: |`, `1. K:`, `# K:`, `__K__:` and `_K:_`. G12 does so for both `Prompt Version` and `Prompt version`.
- **Clean.** The patterns are silent on a header of the title, `Prompt ID:` and `Notion URL:`, followed by `Settings:`, `Setup:`, `1. Setting up:` and `- Set up:` lines, and on C-HANDOFF's "full name, version and direct Notion URL".
- **Window.** A key line at the 8th nonblank line is caught; one at the 9th is not.
- **Regressions**, on PR-35. Insert one line directly after the `Prompt ID:` line, once per guard. Each form is a separate mutation. G12 and G14 share `SRC-001`, and their summaries differ by value.

```text
Prompt Version: 091426.1
```
```text
**Prompt Version**: 091426.1
```
```text
Ecosystem release: GCFPE-20260914.1
```
```text
| Ecosystem release: | GCFPE-20260914.1 |
```
```text
Set: GCFPE-20260914.1 / 091426.1
```
```text
- `Set:` GCFPE-20260914.1 / 091426.1
```

#### D23-D: G15, G16 and G17

G15 goes on MAIN54, and E4's clean control over the 54 edited bodies clears it (§12 *Registry guards*, G15):

```
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
```

- **Clean.** G15 is silent on C-SESSION ("original Proceed, workspace/worktree"). Do not forbid "same-session" broadly: PR-35's own `RECOVERY_PENDING` re-entry is legitimate (registry-audit notes).
- **Regressions.** On PR-35, append the old list. It is `EXACT_GCF17_CONTINUITY` from `amthor-workspace-governance-audit/scripts/run_fixture_suite.py:24`, and the same text sits at `glow-hde-pr-development/SKILL.md:55`. On QA-10, a row outside the three session rows, append the second line.

```text
The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage.
```
```text
It shares the original Proceed, dedicated PR-development session and branch.
```

G16 and G17 go on PR-30, PR-35 and RS-40, each with its own distinct pattern (A1-8; coverage:5):

```
    - value: 'they do not share a session'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30'
      rule_id: CTR-002
```

- **Homes.** G16's home is C-SESSION. G17's home is A1-8's C-SESSION sentence, and G17 does not match C-TOP. G17's phrase is W-1's guard phrase, shared with 7.7 and with `flowmaster-validate`'s role check.
- **Regressions**, each yielding only its own finding:
  - **G16:** delete `; they do not share a session`, on PR-35 and on RS-40;
  - **G17:** delete only A1-8's sentence, on PR-35 and on PR-30.

#### C-TOP: G18 (required), G19–G21 (forbidden), on MAIN54

```
    - value: 'never\s+as\s+a\s+subagent\s+of\s+another\s+session'
      rule_id: CTR-002
```

- **Home: C-TOP.** G18 does not match C-SESSION's "never as a subagent, forked agent or workflow agent of PR-30", so neither guard masks the other (adversary:5).
- **Regression.** Delete C-TOP, on PR-35 and on PR-50. PR-50 gets its own C-TOP edit beside its return rule (A1-8; coverage:27).

G19 gains the possessive exclusion after the prompt id, and G20 gains the `Nathan ` lookbehind (§12 *Registry guards*, G19 and G20). The entries:

```
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?![''’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
```

The `''` in G19 and G20 is the YAML escape for `'`. The values they load to are:

```
(?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b
```
```
(?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)
```

The two §12 additions, as they sit in those values:

```
(?!['’]s\b)
```
```
(?<!Nathan )
```

**Clean.** All three are silent on:
- C-TOP, including its word "starts". The first draft's C-TOP said "launches", and the withdrawn broad pattern matched C-TOP itself (coverage:0; sweep:1).
- The A1-6 override and the other canonical texts, and the seven combined paragraphs.
- The 20 worker or negated phrasings, including the four above and "Hand PR-35's result to a workflow agent for summarising." and "Nathan opens a new session for PR-40.".
- `mcp__Claude_Code_Remote__send_later`.

**What they catch, measured:**
- **G19** catches 8 of 8 injections, capitalised forms included, such as "Run PR-35 as a subagent." and "dispatch PR-40 to a workflow agent".
- **G20** catches 7 of 7, such as "Launch a new session for PR-40." and "spawn a session to run PR-40".
- **G21** catches 5 of 5, such as the fully qualified `mcp__Claude_Code_Remote__create_session`, which has no leading word boundary.

**Regressions**, on PR-35. Append one line per guard:

```text
Run PR-35 as a subagent.
```
```text
Launch a new session for PR-40.
```
```text
Use mcp__Claude_Code_Remote__create_session to open it.
```

E4's clean control runs G19–G21 over the 54 edited bodies. Any hit goes to Nathan and is never exempted (§12 *Registry guards*; registry-audit:3).

#### D23-E: G22–G25

G22 goes on PR-35 and RS-40, and guards the launch option the `D23` clarification withdrew (coverage:1):

```
    - value: 'launched as a new session'
      rule_id: CTR-001
```

- **Clean.** G22 is silent on every canonical text. It matches the superseded §P C-DISPATCH, whose wording G20 does not catch.
- **Regression**, on PR-35. Append:

```text
Emit the PR-40 handoff: paste-ready, or launched as a new session where the surface provides one.
```

G23, G24 and G25 go on PR-35 and RS-40 (registry-audit:12 notes; adversary:4). G24 and G25 anchor on sentences found only in C-DISPATCH (§12 masking):

```
    - value: '[Ss]ubscribe to the pull request'
      rule_id: CTR-002
    - value: 'stay subscribed and do not poll'
      rule_id: CTR-002
    - value: 'The observed merge event is the fact PR-40 is entered on'
      rule_id: CTR-002
```

- **G23's value must stay quoted.** As a plain scalar it raises a `ParserError` (adversary:4; re-measured).
- **Homes:** G23 matches A1-5's C-SUB; G24 and G25 match A1-5's C-DISPATCH, once each.
- **Regressions**, each yielding only its own finding, on PR-35 and on RS-40:
  - **G23:** delete C-SUB;
  - **G24:** delete `; stay subscribed and do not poll`;
  - **G25:** delete the sentence "The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently."

  Deleting all of C-DISPATCH yields two findings, so it is not a valid regression.
- **PR-40.** v1 also placed G25 on PR-40. §12's anchor does not occur in PR-40's body, which carries W-4's entry sentence instead: on a clean PR-40 body built from the canonical texts, §12's G25 value yields its finding (measured). G25 is therefore not placed on PR-40 here, and PR-40's `D23-E` required guard is item 1 of 7.12.

#### D23-F: G26 and G27 (child C5)

G26 goes on PR-40:

```
    - value: 'original Proceed and a suitable actual authorized implementation vehicle'
      rule_id: CTR-001
```

- **Clean.** G26 is silent on C-REPLAN.
- **Regression**, on PR-40. Append:

```text
Return to the existing PR owner, which holds the original Proceed and a suitable actual authorized implementation vehicle.
```

G27 goes on PR-20:

```
    - value: 'accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT'
      rule_id: CTR-002
```

- **Home: C-PR20-ENTRY.**
- **Regression.** Delete C-PR20-ENTRY.
- **Clean control first** (child C5; adversary:20). At E4, G27 is evaluated on today's PR-20 body, read in memory, before any edit. It must produce its finding there, which proves it is not vacuous. That control needs the live body, so it was not run here.

**PR-40 → PR-20 naming.** The positive check that PR-40 names PR-20 is not a registry guard. It is `flowmaster-validate`'s `PROMPT_HANDOFF_RECEIVER`, once the graph moves (registry-audit notes; child C4).

### 7.4 Limits, stated as AF-001 requires

**G06.**
- The window is 1500 characters from the nearest preceding `NEXT_PROMPT_HANDOFF`, and it stops at a blank line.
- Measured: the regression sentence at the end of the C-HANDOFF paragraph, 785 characters from the token, is caught. The same sentence about 2000 characters from the nearest token, after C-HANDOFF, C-SESSION and C-DISPATCH in one paragraph, is not caught, and neither is one after a blank line.
- A bare "names the branch and the commit" is not caught (adversary:19).
- In DOC-20 and PR-40, "commit identity" text may sit near a handoff. Any such hit at E4 is settled by reading the body back, never by exemption (registry-audit:3).

**G19 (F1).**
- It misses "running", "executed", "invoked" and "executing" before a prompt id. It misses the passive "PR-35 is run as a subagent" and a pronoun such as "run it as a subagent".
- It fires on prohibitions that are not negated immediately before the verb:
  - "It is forbidden to run PR-35 as a subagent.";
  - "Do not ever run PR-35 as a subagent.";
  - "PR-35 must never be used to run PR-40 as a subagent.".
- The possessive exclusion silences worker phrasings such as "Run PR-35's tests in a subagent." and "subagents run PR-35's tests in a subagent". A possessive written without an apostrophe ("PR-35s tests") is not excluded.

**G20 (F2).**
- It misses a bare "launch a new session." that names no prompt. A1-8 states this itself and assigns it to the governance audit's semantic invariant.
- It also misses "created a session for PR-40".
- The `Nathan ` lookbehind covers only "Nathan" immediately before the verb. G20 still fires on:
  - "No agent may launch a new session for PR-40." and "No agent may start a session for PR-40.";
  - "without launching a new session for PR-40";
  - "Nathan, not the agent, may open a new session for PR-40." and "Nathan will create a new session for PR-40.", which the new model permits.

  §E records these limits (§12 *Registry guards*).

**G21 (F3).** It catches only the four tool names. `send_later` is excluded deliberately.

**G12–G14.** They do not look past the first 8 nonblank lines.

**G15.** It catches only the "Proceed; dedicated PR-development session" and "Proceed, dedicated PR-development session" forms.

**Masking on real bodies.** G07, G24 and G25 anchor on sentences found only in the canonical texts (§12 masking), so a second, older occurrence of "ends with the `NEXT_PROMPT_HANDOFF` block", "do not poll" or "observed merge event" no longer masks their regressions. If an E3 body carries the anchor sentence itself twice, E4 item 9 fails for that guard and EXECUTE stops.

### 7.5 `D13`-derived fields: the registry deriver

**The rule.** It reproduces all 55 rows today with 0 drift (registry-audit notes; re-measured for v2). It uses union semantics over `outputs[]`: IA-40 has two outputs, and a per-list comparison reports false drift there.

```
for each row r, with P = the E1-built part docs/graph/parts/prompts/<r.prompt_key>.json:
  derived = sorted({e["to"] for e in P["edges"] if e["to_kind"] == "prompt" and e["to"] != P["id"]})
  r["required_interfaces"] == derived                                    # list equality; always sorted today
  set().union(*(o.get("consumers") or [] for o in r["outputs"])) == set(derived)
  set().union(*(o.get("states") or [] for o in r["outputs"])) == set(P["node"]["result_states"])
```

**What the deriver rewrites.** It rewrites only the rows whose derived sets change, and in those rows only `outputs[].consumers`, `outputs[].states` and `required_interfaces`. Against the simulated parts (`route_sim_final.py`, sha256 `e0854a55…`), exactly three rows change: `PR-35`, `PR-40` and `RS-40` (A1-2).
- Consumers are written sorted. Ten other rows keep today's unsorted consumer order untouched.
- `MERGE_OBSERVED` goes into `outputs[].states` in ASCII order, because those lists are sorted today (V-12). That puts it before `MERGE_PENDING`.
- `session_class`, `session_role` and `creator_role` are authored, not derived (registry-audit notes). They are in 7.6.

PR-35 (`:3616-3624`, `:3682-3683`):

```
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:
    - MERGE_OBSERVED
    - MERGE_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    - RESCOPE_PENDING
    consumers:
    - PR-40
    - RS-20
  required_interfaces:
  - PR-40
  - RS-20
```

PR-40 (`:3717-3720`, `:3735-3738`). Its states are unchanged (`ACCEPT`, `REJECT`, `PENDING`), and PR-30 drops out because its only PR-30 edge moves to PR-20 (child C1, C5):

```
    consumers:
    - PR-10
    - PR-20
    - RS-10
  required_interfaces:
  - PR-10
  - PR-20
  - RS-10
```

RS-40 (`:5115-5126`, `:5141-5144`), per A1-5 ("Both PR-35 and RS-40 gain it"), sweep:0 and coverage:2:

```
    states:
    - MERGE_OBSERVED
    - MERGE_PENDING
    - PRODUCT_OWNER_DECISION_REQUIRED
    - PR_CANDIDATE_PUBLISHED
    - RECOVERY_PENDING
    - REMOTE_EVIDENCE_PENDING
    - RESCOPE_PENDING
    - SOURCE_RESOLUTION_ERROR
    consumers:
    - PR-30
    - PR-35
    - PR-40
    - RS-20
  required_interfaces:
  - PR-30
  - PR-35
  - PR-40
  - RS-20
```

**Checks.** Run in E1 after the graph build, and again in E4.
- **Acceptance.** Today's registry against today's parts gives drift `[]`.
- **Post-edit.** The edited registry against the E1 parts gives drift `[]`.
- **Must-fail.** Each negative control reports exactly the listed rows:
  - the unedited registry against the E1 parts gives `['PR-35', 'PR-40', 'RS-40']`;
  - re-injecting `PR-30` into PR-40's consumers gives `['PR-40']`;
  - removing `MERGE_OBSERVED` from RS-40's states gives `['RS-40']`.

### 7.6 Authored row edits

Each edit replaces one exact line, or inserts after one. A new string is written plain when its plain form round-trips through `yaml.safe_load`, and single-quoted otherwise. Measured for v2:
- plain: W-1's PR-35 role, the PR-35 `creator_role`, W-2's RS-40 `creator_role`, W-4's PR-40 entry input and the PR-20 input;
- single-quoted: W-2's RS-40 `session_role` and W-4's PR-35-result input (each contains ": "), and the PR-35 `session_disposition` input, which parses as a mapping unquoted (registry-audit:7).

**Step 26 — PR-30, `:3531`**, `mutations.allowed`. Old:

```
    - Implement, test, commit, publish, and review-correct the exact proceeded PR work unit
```

New:

```
    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35
```

The verification is `grep -c review-correct` = 0, measured 0.

**Step 33 — PR-35** (registry-audit:7, :8 and notes; A1-8; W-1).
- `:3604`:

```
  session_class: DEDICATED_PR_REVIEW_SESSION
```

- `:3605` `session_role`, W-1's string. It equals the graph's `PR-35.json` `node.receiving_role` and the contract's `member_registry['PR-35'].receiving_role` verbatim (§6.3):

```
  session_role: You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
```

- `:3606`:

```
  creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.
```

- `:3611`, replacing `  - same dedicated PR session reference with session_disposition RETAIN_EXISTING`:

```
  - 'session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID'
```

- `:3633`, `mutations.forbidden`. Merely deleting "session" would stop guarding against a third session (AF-001):

```
    - Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session
```

**Step 39, and the other PR-40 inputs** (registry-audit:9; coverage:3, :18; W-4).
- `:3705`, the PR-35-result input, becomes W-4's text:

```
  - 'The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.'
```

- `:3708` replaces "the dedicated PR session identity" with "the PR-30 and PR-35 session identities":

```
  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change IA context and exact return owner
```

- `:3710`, today "Nathan's later invocation asserting the identified PR was manually merged after PR-35 produced MERGE_PENDING", becomes W-4's entry sentence, the same string the PR-40 body carries:

```
  - PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.
```

**Child C5 — PR-20.** Insert after `  - PR_INSTRUCTION_ID` (`:3429`). It carries no backticks, following the registry's convention: 0 of its 182 inputs contain one (§12 *Registry guards*, the PR-20 input):

```
  - PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the same WORK_UNIT_ID in a new dedicated session Nathan seeds
```

The next postflight should restate check (f) by its real criterion, "no QA Guide or QA Plan", and not as "exactly `[PR_INSTRUCTION_ID]`" (registry-audit:11). §E records it; it is not a registry edit.

**RS-40, `:5108-5109`** (registry-audit:9; coverage:18; W-2). `session_role` changes together with the graph's `RS-40.json` `node.receiving_role` to one identical string, and `creator_role` changes with it:

```
  session_role: 'You resume the recorded phase in its own dedicated session: PR-30''s session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.'
  creator_role: the recorded phase's own dedicated session for the exact suspended work unit.
```

RS-40's `session_class` stays `DEDICATED_ONE_OFF`; §E records it as a pre-existing inaccuracy out of scope (S-9).

**PR-20 and PR-40 roles stay unchanged** (W-3). Body-level C-TOP and G18–G21 carry the rule for them.

### 7.7 Role parity check for the D23 clarification (coverage:6)

The `D23` clarification requires a guard on "the graph role and the registry role for each affected prompt". No registry assertion reads `session_role`, so E4 item 8 adds this check, in memory:

```
registry["PR-35"]["session_role"] == graph PR-35.json ["node"]["receiving_role"]     -> else ROLE_PARITY
"never as a subagent, forked agent or workflow agent of PR-30" in graph PR-35.json ["node"]["receiving_role"]   -> else ROLE_CLAUSE
registry["RS-40"]["session_role"] == graph RS-40.json ["node"]["receiving_role"]     -> else ROLE_PARITY
```

- **The clause phrase** is W-1's guard phrase. coverage:6's phrase is superseded (W-1).
- **Must-fail regressions**, measured in v1 for this phrase:
  - removing the clause from the registry role only yields `ROLE_PARITY` alone;
  - removing it from both yields `ROLE_CLAUSE` alone.
- **The contract side** is §6/§8. It is `flowmaster-validate`'s literal on `member_registry['PR-35'].receiving_role`, and the regenerator copies that role from the graph.

### 7.8 N1 and N2 (S-2)

S-2 compiles these as E1 edits. They come from the first draft's N1 and N2, carried by registry-audit:17, :18, sweep:18 and :23.

**N1, in the registry.** A new key, `body_identity_disposition`, under `body_extraction_convention`. It is inserted, and no existing dated statement is edited (`AUTH-001`). It states that the `evidence_contract` and `source_snapshot` identities describe the bodies before `D23` and no longer identify them. Its content:
- **Which identities are stale.** On all 55 rows:
  - the `evidence_contract` byte counts and SHA-256;
  - the `source_snapshot` `sha256`, `bytes` and `completeness` (sweep:23). `applies_to` (`:80-82`) already records these as the 2026-09-17 pre-merge extraction. N1 adds that they do not identify the edited bodies either.
- **Why they are not regenerated.** Hashing bodies is prohibited: `prompt-corpus-policy.md:104` says "Never an identity. Not hashed, not byte-compared", and `:110` lists "body hashes" among what is still prohibited.
- **Which claims it supersedes.** The identity claims at registry `:39` (the `authority_sources` note, "…are the reproducible identity"), `:55-56` (`row_wording_disposition`) and `:79-80` (`body_extraction_convention.applies_to`, "…which are the body identity for validation").
- **Nothing breaks.** No live check consumes these values: the SF10-12 pins are retired. The retired bench `docs/ephemeral/gcfpe.round20.sf10-bench/bench.py` would report a mismatch on every edited body (registry-audit live-window notes).

**N1, outside the registry.**
- `authoritative-surfaces.md:59` is corrected to match: its description still says "with `evidence_contract` byte count and SHA-256 per prompt".
- `authoritative-surfaces.md:29` and `:45-46`, and `ecosystem-change-management.md:143`, state the old graph token "55 nodes · 227 edges · 55 state_routes · 569,902 bytes · sha256 1d0b7258…". Each is labelled *"as measured before `D23`"*, not restated.
- `ecosystem-change-management.md:176` changes "carries" to "carried, until `D23-G` removed them,".

**N2, at `ecosystem-change-management.md:141`.** Today it reads: "499 assertions across 55 prompts, 0 failing. `required_regex` binds release identity and Canon source; `forbidden_regex` guards D7 against Drive reintroduction in any of its four forms." Its assertion sentence becomes S-2's, with no count:

```text
`required_regex` binds the Canon source and the `D23` canonical wordings; `forbidden_regex` guards `D7`, the `D23` reversals and session creation.
```

The count was 831 today and is 1483 on the v2 prototype (7.10).

**Also in E1 under S-2:** `execution-and-delegation-model.md` gains the scope line in the `D23` clarification's words; §3 owns its placement. The words are:

```text
its subagents are maintenance workers, and never a way to run a main-ecosystem prompt.
```

### 7.9 Method: line-anchored insertion and a `load_data` semantic diff (A1-2; registry-audit:19; coverage:24)

**How the script edits the file.**
- It edits the Markdown file's lines, and never round-trips YAML: `yaml.safe_dump` would reflow and requote the whole 5301-line file.
- A row's range runs from the line `- prompt_key: <KEY>` to the next line `- prompt_key: ` or `global_literals:`.
- Every operation names its row and an exact anchor line. Within the row, that anchor occurs exactly once, or first after a named sub-anchor such as `    consumers:` or `  required_interfaces:`. Otherwise the script stops.
- Removals delete an exact two-line pair.
- Appends go after the last item of the named list.

**Order within E1** (§0):
1. graph parts, then the build (§4);
2. the deriver (7.5);
3. 7.2, 7.3 and 7.6;
4. N1 (7.8);
5. the checks below.

**Checks after the edit.** Each must hold.
1. **`load_data(old)` against `load_data(new)`.**
   - Top-level keys other than `prompts` are unchanged, except N1's new key under `body_extraction_convention`.
   - The 55 rows keep their set and order.
   - Per row, the multiset difference of `(value, rule_id)` in each assertion list is exactly the two 7.2 removals plus the guards 7.3 selects for that row.
   - Kept entries keep their order.
   - The non-assertion fields that change are exactly: PR-20 `inputs`; PR-30 `mutations`; PR-35 `creator_role`, `inputs`, `mutations`, `outputs`, `required_interfaces`, `session_class` and `session_role`; PR-40 `inputs`, `outputs` and `required_interfaces`; RS-40 `creator_role`, `outputs`, `required_interfaces` and `session_role`.
2. **Every item of every `inputs` list is a `str`.**
3. **The structure check.** From a scratch copy of the skill, run the command below. It must return `{"valid": true, "problems": []}`.

```
PYTHONDONTWRITEBYTECODE=1 python3 <scratch>/wga/scripts/validate_project_prompt_registry.py <branch>/docs/prompt_ecosystem_management/project-prompt-contract-registry.md
```

4. **The 7.5 drift checks and their negative controls.**
5. **The 7.3 and 7.7 evaluations, at E4 on the E3 bodies.** No snapshot is taken, no hash is computed, and nothing is written that embeds a body digest (E4; registry-audit:0).

**Live window** (registry-audit, live-window notes).
- From the merge until the cut-over lands the bodies, `main`'s registry fails against the unedited live bodies: the new required guards are absent from them. That falls inside the A1-4 freeze.
- The cut-over re-scan uses the registry at the merge commit (A1-4 item 5).
- The registry path is CI-exempt (`_DOCUMENTATION_PREFIXES`), so every check here is run by the agent.

### 7.10 Measured (v2 consolidation)

Run on 2026-09-23 under `/tmp/claude-0/v2work67/`, with `PYTHONDONTWRITEBYTECODE=1`, on a copy of the registry (sha256 `c5ae1888…`, matching the baseline) and a copy of `amthor-workspace-governance-audit` whose `audit_workspace_governance.py` is sha256 `c4ca7f608c5e9bfdb23372e7e3dbd46621088eabb77379796bb6bd6ea07ef120`. The evaluator is its real `_evaluate_assertions` (`re.search`, `re.MULTILINE`). The texts are read from §3 of v1 with the §12 strings added; the 16 source-defined texts equal the earlier extractor's strings. No `__pycache__` was created.

**Static.**
- All 28 guards compile and round-trip through YAML single quotes. So does the 7.12 candidate.
- The 13 required guards each match their home texts, joined and, where a source form exists, wrapped, and match no other canonical body text. G07, G24, G25 and G08A each match their home exactly once.
- The 15 forbidden guards each match no canonical text in either form, none of the seven combined paragraphs and none of the 20 worker or negated phrasings. The four phrasings the brief names produce no finding from any guard.
- G19 catches 8/8 injections, G20 7/7 and G21 5/5. The 7.4 limits are the measured misses and hits.
- G12–G14: 12/12 decorated forms caught for each key, including both `Prompt Version` spellings; the 8th nonblank line is caught and the 9th is not; the control header is silent.
- `STATIC FAILURES: 0`; `HEADER FAILURES: 0`.

**Registry prototype, 5301 → 6612 lines** (sha256 `c9e812b6582e5e7ab9f2df6d649c49b502d7e5dc66cff96c48fdba429f26f1f2`, without N1):
- The semantic diff is exactly as 7.9 lists: no top-level key changes, rows kept in set and order, each row's assertion diff equals the expected one, and kept entries keep their order.
- Guard row counts: G01 55, G02 55, G03 1, G04 10, G05 53, G06 53, G07 53, G08 4, G08A 4, G09 3, G10 10, G11 10, G12 55, G13 55, G14 55, G15 54, G16 3, G17 3, G18 54, G19 54, G20 54, G21 54, G22 2, G23 2, G24 2, G25 2, G26 1, G27 1.
- Assertions go from 831 to 1483.
- Every `inputs` item is a `str`.
- The structure check returns valid true with no problems, exit 0.
- `outputs[].states` for PR-35 and RS-40 are in ASCII order, with `MERGE_OBSERVED` first.

**Deriver.** Against copies of the simulated parts: today's registry against today's parts gives `[]`; the edited registry against the simulated parts gives `[]`; the three negative controls give `['PR-35', 'PR-40', 'RS-40']`, `['PR-40']` and `['RS-40']`.

**Regressions, real evaluator.**
- Synthetic bodies are built only from canonical texts, in two handoff layouts. The ASK4 bodies carry the `ASK OK?` variant in place of C-PLACE; PR-40 carries C-REPLAN and W-4's entry sentence.
- Clean: 0 new-guard findings on 55 rows × 2 layouts.
- 41 regression cases × 2 layouts, all listed in 7.3: each yields exactly its own `(rule_id, observed.summary)`. `REGRESSION FAILURES: 0`.
- Each of the four named worker phrasings, appended to a clean PR-35 body, adds no finding.
- §12's G25 value on a clean PR-40 body yields its finding (7.12 item 1). The candidate there is silent on the clean body, and deleting W-4's sentence yields exactly its finding.

### 7.11 Dispositions of the registry findings

| finding | disposition |
|---|---|
| registry-audit:0, :1 | the gate method and its pass criteria are §9 items 8–9; 7.1 uses them |
| registry-audit:2 | NPH53 selector, 7.1; G05–G07 |
| registry-audit:3 | G06; limits in 7.4 |
| registry-audit:4 | G05 |
| registry-audit:5 | 7.2; G12–G14; the NAM-001 note goes to §E |
| registry-audit:6 | G01–G04 (G02 as corrected by adversary:6); G04 on STEP5 |
| registry-audit:7, :8 | PR-35 edits, 7.6, with W-1's role |
| registry-audit:9 | PR-40 `:3708` and RS-40 roles (W-2), 7.6 |
| registry-audit:10 | deriver, 7.5 (PR-35, RS-40); its "automatic edge becomes true" premise is superseded by A1-5 |
| registry-audit:11 | deriver (PR-40), PR-20 input without backticks, 7.6; the postflight check (f) note goes to §E |
| registry-audit:12 | G07, G08, G08A, G15–G17, G23–G27 |
| registry-audit:13–16 | skill text in `amthor-workspace-governance-audit`, the fifth package: §8, not the registry |
| registry-audit:17 | N1, 7.8 (S-2) |
| registry-audit:18 | N2, 7.8 (S-2) |
| registry-audit:19 | 7.9 |
| registry-audit:20 | the `session_class` enum doc is skill text, §8 (S-8); no registry change |
| coverage:0; sweep:1 | resolved by A1-8's C-TOP ("starts") and adversary:0's F2 (G20); coverage:0's unnamed-object pattern is not adopted, because A1-8 forbids "creating a session to run a named prompt" |
| coverage:1; sweep:2; adversary:4 | G22–G25 (the `exact_markers` literal in sweep:2 is §8) |
| coverage:2; sweep:0; adversary:1 | RS-40 in the deriver's row set, 7.5 |
| coverage:3, :18 | PR-40 inputs `:3705` and `:3710`, 7.6 (W-4) |
| coverage:5; adversary:5 | G09, G17, G18 |
| coverage:6 | 7.7; its phrase is superseded by W-1's |
| coverage:24 | 7.9; registry-audit:20 goes to §8 |
| coverage:27 | G18 on PR-50, with its regression |
| sweep:15 | W-3: PR-20 and PR-40 roles unchanged |
| sweep:18, :23 | N1, 7.8 (S-2) |
| adversary:0 | G19–G21, with §12's G19 and G20 corrections; `send_later` excluded under A1-8 |
| adversary:6 | G02; every value is in a code block |
| adversary:14 | W-5: G08 and G08A |
| adversary:15 | 7.1 |
| adversary:19 | 7.4 |
| adversary:20 | G27's clean control |

### 7.12 Unsettled

§12 does not settle these. EXECUTE brings each to Nathan before E1 relies on it (§0).
1. **PR-40's `D23-E` required guard.** §12 anchors G25 on "The observed merge event is the fact PR-40 is entered on", a C-DISPATCH sentence that only PR-35 and RS-40 carry, and leaves G25's rows unchanged. On PR-40 that anchor is absent, so G25 would fail the clean body. Placing no guard on PR-40 would drop one v1 had (AF-001). The measured candidate anchors on W-4's entry sentence, which is canonical and unique to PR-40's body:

```
    - value: 'PR-40 is entered on the observed merge event'
      rule_id: CTR-002
```

   It compiles, round-trips, matches only W-4's sentence, is silent on the clean PR-40 body, and its deletion regression yields exactly its finding. It is not in the 7.10 counts.
2. **G08A's id and `rule_id`.** W-5 orders a required pattern on the `ASK OK?` sentence, with a deletion regression, and gives neither. This section uses `G08A` and `TOP-001`, the `rule_id` of G07, the placement guard it extends.
3. **PR-40 `:3705` loses its PR-30 clause.** Today the line names two results: "The complete PR-30 result with PR_CANDIDATE_PUBLISHED and the complete PR-35 result …". W-4 gives the whole new line and names only the PR-35 result. Applied as written, PR-40's inputs no longer name the PR-30 result. Whether it is kept, as its own item or in the same line, is not settled.
4. **N1's exact wording**, and the exact corrected wording of `authoritative-surfaces.md:59`. S-2 fixes the key, its position and its content, not the strings.

## §8a Skill edits: glow-hde-pr-development and amthor-workspace-governance-audit

**v2, consolidated.** This section replaces v1 §8a (v1 lines 3974–4814). Every §12 decision is applied
inline, and each choice cites the §12 entry that made it (`§12 §8a Ox`, or the scope/wording id such
as `W-9`, `S-8`). v1's option lists are gone; the options §12 did not name are void (§0). What §12
does not settle is listed once, in 8a.11 *Unsettled*, with the compiled value EXECUTE would place if
Nathan confirms it. Nothing in 8a.1–8a.10 is open.

This section covers two of the six packages (A1-6): `glow-hde-pr-development` (4 files) and
`amthor-workspace-governance-audit` (15 files). All edits are E2 edits on scratch copies (§0).

### 8a.0 Conventions

- **Line numbers** are those of the installed tree at
  `/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502`
  (read-only). On 2026-09-23 every file of both packages was byte-identical to the drafters'
  measurement copy (`diff -r` against `/tmp/claude-0/spec/s8a/skills`), so §2's digests
  (`glow-hde-pr-development` `e109d47a…`, `amthor-workspace-governance-audit` `6cd088a0…`) hold.
  E2 re-measures them and stops on any difference (§2).
- **Every `old:` span below was verified** to occur exactly once in the installed file, by applying the
  whole edit set as scripted exact-substring replacements on a copy
  (`/tmp/claude-0/v2work8/work/apply_skills.py`, sha256 `b6683e6c477affb0…`). Line numbers identify a
  site; the span locates it. Insertions shift later lines.
- **No whole-line replacement** where a kept literal sits on the line (amendment defect 12). Every span
  stops short of a kept literal or carries it into `new:` unchanged.
- **Compile rule.** Canonical texts go in verbatim. Words stating a reversed rule are deleted, and are
  replaced only by words from a canonical text, the A1-7 table, a finding, or a §12 decision. Every
  other word on a line stays. **S-4:** every prose line that restates a reversed rule is converged;
  the lines kept verbatim are listed in 8a.1 with the reason §E records.
- **No session creation in skill text** (D23 clarification; D23 successor notes). No edit below lets a
  main-ecosystem skill create, start, launch or schedule a session. No C-TOP goes into this skill
  (§12 §8a O13 (a)); the rule is carried by C-SESSION's A1-8 sentence, C-SUB, C-DISPATCH and `:173`
  (W-9). No session-creation regex applies to skill text (§12 *Other settlements*, §3).
- **Tokens.** `{C-X}` is §3's text of C-X, byte-exact. `{C-SESSION}` is §3's compiled form: backticks
  dropped, A1-8's sentence last (W-6). The other tokens:

```
{NINE}
The exact ordered nine-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage

{TEN}
The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage

{V6}
The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`

{V5}
The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`

{FALLBACK}
only where no `MERGE_OBSERVED` result was returned for this merge

{LANDED}
A pull request merged under an earlier plan cycle is landed history: never resume, reuse or push to it.

{A18}
PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.

{INVARIANT}
Every main-ecosystem prompt (all but GCFPE-MGMT-10) runs as its own top-level session Nathan creates; none runs as a subagent, forked or workflow agent; none creates, launches or schedules a session; workers within a task are allowed.
```

  - `{NINE}` is `{TEN}` without "dedicated PR-development session;", with "ten-field" read as
    "nine-field" (step 29; pr-relay-graph:1, fv-main:24, fv-rest:18, registry-audit:15).
  - `{V6}` is A1-5's ordered vocabulary (sweep:3, adversary:9, coverage:14).
  - `{FALLBACK}` is A1-5's single fallback predicate, worded one way everywhere (§12 principle 4).
  - `{LANDED}` is C-PR20-ENTRY's last sentence (child C6, sweep:16).
  - `{A18}` is C-SESSION's last sentence, A1-8's addition (W-6).
  - `{INVARIANT}` is §3.4's governance-audit invariant, sweep:25 verbatim; it keeps "launches"
    (§12 §8a O24 (a)).
- **How the PR skill's validator reads.** `required` is a case-sensitive substring test on
  `SKILL.md + "\n" + behavior-cases.md`; `forbidden` is case-insensitive on the same text;
  `case_headings` are tested in `behavior-cases.md` only. It is fail-fast: it prints the first failure
  and exits 1. A forbid regression is written in **injection form** (the old text is added, the new
  text stays).
- **Literal dispositions.** `v:N` is `validate_glow_hde_pr_development.py` line N.
  **KEEP** = verbatim, still present after the edit. **REPLACE** = a new literal in place of the old,
  whose old value is also FORBIDDEN. **FORBID** = appended to `forbidden`. **NEW** = a new required
  literal or heading. Each REPLACE, FORBID and NEW entry names its must-fail regression (8a.4).
- **Regression pass criterion.** Exit 1, the exact expected first line on stdout, and a non-fail-fast
  count (`/tmp/claude-0/spec/s8a/work/allfail.py`) equal to the expected set. The expected set is one
  finding except where 8a.4 names two.

### 8a.1 `glow-hde-pr-development/SKILL.md`

**`:3` — description.** Step 35. No literal sits on this line. Glue as compiled (§12 §8a O22 (a)).
```
old: Glow HDE PR work unit in its single dedicated development session across
new: Glow HDE PR work unit, run in two dedicated sessions, across
```

**`:8` — revision.** `v:26` REPLACE (R-rev). Pins: 8a.5.
```
old: `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5`
new: `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0`
```

**`:10` — "Complete one approved PR work unit…".** Step 35 and child C6, one combined edit.
- `v:31` KEEP (sentence untouched; pr-relay-graph:4).
- `v:32` REPLACE (8a.3; first of its two old occurrences).
- `v:64` KEEP (still at `:55`, `:141`).
- Cross-surface: `validate_gcfpe_current.py:652` read this phrase; it moves with §8b (S-5; §12 §8b O14 (a)).
```
old: Keep the existing GCFPE actor, one dedicated PR-development session, one original Product Owner Proceed, scope, and manual-merge boundaries intact.
new: Keep the existing GCFPE actor, one Proceed per approved per-PR plan, scope, and manual-merge boundaries intact.
```

**`:17` — Proceed intake item.** Child C6. "original" is deleted; `:18` is unchanged (§12 §8a O3 (a)).
```
old: detailed PR implementation Plan covered by the original Proceed, with
new: detailed PR implementation Plan covered by the Proceed, with
```

**`:22` — PR-35 / RS-40 intake item.** Step 14 (C-HANDOFF), step 35 (pr-relay-graph:5).
"same-session" goes; the trailing lineage clause is deleted, because recovery steps `:42`–`:43` inspect
worktrees, branches, PRs and the PR head (§12 §8a O4 (a)).
- `v:52` KEEP ("only when `PR_RETURN_PHASE: PR-35`, the PR-35 handoff" survives: the second span stops
  after it and restores it).
- `v:35` KEEP.
```
old: the complete `PR_CANDIDATE_PUBLISHED` result and same-session PR-35 handoff;
new: the complete `PR_CANDIDATE_PUBLISHED` result and PR-35 handoff;
```
```
old: , the PR-35 handoff; in either case require the exact workspace/worktree, branch, open PR and remote-head lineage;
new: , the PR-35 handoff;
```

**`:27` — "Proceed authorizes the bounded engineering lifecycle…".** Step 35 and child C6.
- No literal sits on this line today.
- FORBID `followed in the same session by PR-35` (child C6; coverage:21 — verifier unplaced 5). R-C6-27.
- NEW `One Proceed per approved per-PR plan` (C-PROCEED's first sentence; §12 §8a O9 (a)). R-CPROC.
```
old: coherent initial publication followed in the same session by PR-35 review remediation
new: coherent initial publication followed by PR-35 review remediation
```
```
old: only for its explicit scope; continuation preserves the original Proceed and never requires or creates a second Proceed.
new: only for its explicit scope. {C-PROCEED}
```

**`:43`–`:44` — recovery steps 3 and 4.** Child C6 cites "`:41` (recovery steps 3 and 4)"; the numbered
list starts at `:41`, so the steps are `:43` and `:44` (anchor correction; sweep:16).
- `:43` takes the child's words (§12 §8a O5 (a)).
- `:44` appends `{LANDED}` after one space (child C6, sweep:16).
- `v:39` "Recover before creating work" (heading `:37`) KEEP.
```
old: 3. Match prior work using evidence such as
new: 3. Match prior work of the current plan cycle using evidence such as
```
```
old: Reconcile partial or ambiguous external effects before retrying them.
new: Reconcile partial or ambiguous external effects before retrying them. {LANDED}
```

**`:53` — the two-phase paragraph.** Step 35; A1-8's clause is inside `{C-SESSION}` (W-6).
- `v:32` REPLACE with `run in two dedicated sessions` (its new value occurs here, inside C-SESSION's
  first sentence, and at `:3`). R-32.
- `v:33`, `v:34`, `v:35` KEEP (pr-relay-graph:3).
- `v:38` REPLACE (pr-relay-graph:0). R-38.
- NEW `never as a subagent, forked agent or workflow agent of PR-30` — the plain-substring form of the
  A1-8 clause, the same guard phrase W-1 fixes for the PR-35 role. R-TOP.
- The "adds no … session" list takes the registry wording "any session beyond its own dedicated PR-35
  session" (§12 §8a O7 (b)).
```
old: Remain in the one dedicated PR-development session across both phases.
new: {C-SESSION}
```
```
old: followed by exactly one complete same-session `PR-35` handoff.
new: followed by exactly one complete `PR-35` handoff to the dedicated PR-35 session.
```
```
old: The phase boundary adds no actor, session, work unit,
new: The phase boundary adds no actor, work unit,
```
```
old: Proceed, R1 row, or authority transfer.
new: Proceed, R1 row, authority transfer, or any session beyond its own dedicated PR-35 session.
```

**`:55` — the continuity list.** Step 29/35 (pr-relay-graph:1).
- `v:55` REPLACE with `{NINE}`; `{TEN}` FORBID. R-55.
- `v:64` KEEP. The sentence after the list is untouched.
- Cross-surface: `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594` moves to `{NINE}` (8a.6).
```
old: {TEN}.
new: {NINE}.
```

**`:57` — result vocabularies.** Step 38 and A1-5. Only the PR-35 list changes.
- `v:36` (PR-30 vocabulary) KEEP. `v:37` REPLACE with `{V6}`; `{V5}` FORBID. R-37.
- The RS-40 sentence stays: RS-40 returns only that phase's lawful result, which now includes
  `MERGE_OBSERVED` (A1-5).
```
old: The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`,
new: The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,
```

**`:59` — not edited.** Step 20's anchor moves to `:108` (pr-relay-graph:10). `v:49`, `v:50`, `v:51`
KEEP. The `flowmaster-validate` marker `PR_REMOTE_ACTION_LEDGER` (`validate_gcfpe_20260914.py:2592`
tuple) KEEP (fv-main:25).

**`:65`, `:126`–`:128` — C-LAT.** Step 24 (pr-relay-graph:12). C-LAT goes after the `:126` heading;
`:128` takes the D23-C term; `:65` points forward (§12 §8a O2 (a)).
- The numbered procedure at `:130`–`:133` stays intact; `v:56`, `v:57`, `v:58`, `v:61`, `v:74` KEEP.
- NEW `Decide it during work`. R-CLAT.
- `{C-LAT}` is §3's two paragraphs and numbered list, each item on its own line.
```
old: route a substantiated material boundary through the existing rescope path.
new: route a substantiated material change (as defined below) through the existing rescope path.
```
```
old: ## Route a real material boundary

When repository evidence proves that the approved work unit cannot be completed without changing approved scope, architecture, requirements, or Plan authority:
new: ## Route a real material boundary

{C-LAT}

When repository evidence proves a material change, as defined above:
```

**`:77` — PR reuse.** Child C6 ("one branch and one PR per plan cycle"). `:77` also repeats the
landed-history rule (§12 §8a O6 (b)). No literal sits on this line.
```
old: Reuse an existing PR for the same branch/work unit instead of creating another.
new: Reuse an existing PR for the same branch/work unit in the current plan cycle instead of creating another. {LANDED}
```

**`:79` — push bundling.** Step 27 (§3.5 literal). "Never push merely to trigger another remote run."
stays (pr-relay-graph:13). No literal sits on this line.
```
old: - Bundle related implementation or review corrections into one locally verified push when practical.
new: - Bundle related implementation changes into one locally verified push when practical.
```

**`:82` — PR-30's stop and handoff.** Step 14 (the field list goes), step 35 (the PR-35 session),
child C6 (per plan cycle). The last sentence takes §12 §8a O6 (b). `v:35` KEEP.
```
old: that invokes the exact selected PR-35 in this same dedicated session with all repository, worktree, branch, PR, remote-head, artifact, test, constraint, unresolved-item, and original-Proceed lineage.
new: that invokes the exact selected PR-35 in the dedicated PR-35 session.
```
```
old: or create another PR/session/Proceed.
new: or create another PR/session/Proceed; one branch and one pull request per plan cycle.
```

**`:100` — merge-readiness loop.** Step 35 (sweep:4, coverage:17). `v:44` REPLACE; old FORBID. R-44.
```
old: Continue in the same dedicated PR session until all applicable predicates are true:
new: Continue in this phase's own dedicated session until all applicable predicates are true:
```

**`:108` — the result artifact.** Step 20, re-anchored here (pr-relay-graph:10). C-DEC is a nested item.
- NEW `An *In-flight decisions* section` (adversary:5). The bare phrase is not used: C-LAT's "record it
  under *In-flight decisions*" would mask the deletion regression. R-CDEC.
```
old: - the complete PR implementation result and handoff artifacts are saved and read back.
new: - the complete PR implementation result (`PR_IMPLEMENTATION_RESULT`) and handoff artifacts are saved and read back; `PR_IMPLEMENTATION_RESULT` includes:
  - {C-DEC}
```

**`:110` — `MERGE_PENDING`.** Step 40: C-DISPATCH is appended; the existing sentences stay
(pr-relay-graph:7).
- `v:45`, `v:46`, `v:81`, `v:82` KEEP. The `flowmaster-validate` no-merge marker (`:2593` tuple) KEEP.
- NEW `no session is created by an agent` (C-DISPATCH's last clause; §12 §8a O12 (b)). R-DISP.
- No `MERGE_OBSERVED` sentence is added at `:164`; C-DISPATCH here states it (§12 §8a O17 (a)).
```
old: or keep polling for that manual action.
new: or keep polling for that manual action. {C-DISPATCH}
```

**New paragraph before `:112` — C-SUB.** Step 37. `:112` stays verbatim (pr-relay-graph:9); `v:47`,
`v:48` KEEP ("exactly one same-session PR-35 re-entry handoff" names PR-35's re-entry into its own
session).
- NEW `Subscribing is not polling` (§12 §8a O12 (b)). R-SUB.
```
old: 
Use `REMOTE_EVIDENCE_PENDING` only in PR-35 when
new: 
{C-SUB}

Use `REMOTE_EVIDENCE_PENDING` only in PR-35 when
```

**`:121` — polling.** Step 37 names `:121`; sweep:19's text. No literal sits on this line.
```
old: - poll only when a pending remote result can change the next action;
new: - where no subscription delivers it, poll only when a pending remote result can change the next action;
```

**`:133` — the RS-20 package.** Step 14 (pr-relay-graph:6). The branch-state clause is deleted, because
C-HANDOFF carries no branch (§12 §8a O8 (b)). `v:58` and `v:61` KEEP (both sit before the span).
```
old: repository/workspace/worktree/branch state, open PR and remote head only when they actually exist, 
new: 
```
(The `old:` span ends in one space; `new:` is empty.)

**`:135` — KEEP verbatim (S-4).** §E records the reason: it restates no reversed rule. "Ordinary
in-scope difficulty or review correction is not rescope" agrees with C-LAT; "never … requests a new
Proceed" agrees with C-PROCEED, because a re-plan's Proceed comes through PR-20, never from the PR
session.

**`:141` — approved open-PR rescope.** Step 35 (sweep:4, coverage:17). `v:63` REPLACE; old FORBID.
R-63. `v:62`, `v:64`, `v:71`, `v:76` KEEP.
```
old: Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR,
new: Resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR,
```

**`:158` — one branch and one PR.** Step 35 and child C6. `v:53` (`docs/ephemeral` on `:157`) KEEP.
FORBID `ten-field` (§12 §8a O10 (b)). R-TENFIELD.
```
old: The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires;
new: The work unit keeps exactly one branch and one pull request per plan cycle, which the nine-field continuity list requires;
```

**C-ART — new paragraph after `:158`.** Step 10 (§12 §8a O1 (a)).
- NEW `never carries the only copy` (pr-relay-graph:11; the registry step-11 string). R-CART.
```
old: for artifacts. The Product Owner merges.

new: for artifacts. The Product Owner merges.

{C-ART}

```

**`:162` — the handoff rule.** Steps 14 and 19 (pr-relay-graph:6, fv-rest:25).
- The first sentence stays verbatim: `v:54` KEEP; the `flowmaster-validate` handoff-shape marker
  (`:2595` tuple) KEEP.
- The whole second sentence is replaced by C-HANDOFF (§12 §8a O23 (a)). "Populate only the actual
  branch.", the not-runnable sentence and the terminal-return sentence stay.
- C-PLACE goes at the end of the line (verifier conflict 15).
- NEW `It carries no branch and no commit` (§12 §8a O12 (b)). R-NOBRANCH.
```
old: It must instruct the receiver to run the exact selected Notion prompt by full name, version, and direct Notion URL; identify the receiving role and exact continuing/dedicated session; identify the change/Epic and work unit; supply every required repository path and repository/PR reference; state current status, completed work, decisions, constraints, unresolved items, and preserved authority; and state the next required action and expected output.
new: {C-HANDOFF}
```
```
old: or unrecoverable work.
new: or unrecoverable work. {C-PLACE}
```

**`:164` — returns by result.** Step 35 (first sentence), step 40 (coverage:16, pr-relay-graph:8,
coverage:3). The fallback clause takes `{FALLBACK}`; "Nathan's later merge assertion" stays as the
fact on the fallback path. `v:83`, `v:59` KEEP. The interruption sentence ("exact same-session
same-phase continuation") stays: it names the phase's own session. No `MERGE_OBSERVED` sentence is
added (§12 §8a O17 (a)).
```
old: At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact same-session PR-35 continuation.
new: At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact PR-35 continuation.
```
```
old: to use it only after Nathan has manually merged the identified PR;
new: to use it only after Nathan has manually merged the identified PR and {FALLBACK};
```

**`:173` — sessions.** W-9 (§12 §8a O14 (b)). No literal sits on this line.
```
old: - Do not create hidden sessions or extra approval stages.
new: - Do not create sessions or extra approval stages.
```

**Lines that mention sessions and stay verbatim (S-4; §E records each reason: none restates the shared
session D23-D reverses, and none lets a session create another):**
- `:21` "the dedicated PR-session identity";
- `:45` "create one only after recording what was checked" (a workspace, not a session);
- `:112` "same-session PR-35 re-entry" and "same-session repository/artifact inconsistency" (PR-35's own
  session);
- `:147` "that same native PR-30 session";
- `:151` "work for the same session".

### 8a.2 `glow-hde-pr-development/references/behavior-cases.md`

Headings are validated; content edits are listed because they converge restated rules (S-4;
pr-relay-graph:15).

**`:7` — Fresh work unit.** Step 35. `v:35` KEEP. The "creates no new … session" list takes the
registry wording (§12 §8a O7 (b)).
```
old: with exactly one complete same-session PR-35 handoff.
new: with exactly one complete PR-35 handoff.
```
```
old: The phase split creates no new role, session, Proceed,
new: The phase split creates no new role, Proceed,
```
```
old: R1 row, work unit, or PR.
new: R1 row, work unit, PR, or any session beyond its own dedicated PR-35 session.
```

**`:11` — PR-30 phase boundary.** Steps 35 and 14, as at `:82`. `v:35` KEEP.
```
old: invokes the exact selected PR-35 in the same dedicated PR-development session with complete lineage.
new: invokes the exact selected PR-35 in the dedicated PR-35 session.
```

**`:13` — the continuity list.** Step 35. `v:64` KEEP. The old text contains `ten-field`, now
forbidden (8a.3), so this edit is required for PASS.
```
old: The shared phase identity preserves the exact ordered ten-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree;
new: The shared phase identity preserves the exact ordered nine-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree;
```

**`:17` — PR-35 review phase.** Step 35.
```
old: Given the complete same-session PR-35 handoff,
new: Given the complete PR-35 handoff,
```

**`:21` — exact phase results.** Step 38. `v:35` KEEP. The old form is guarded by the forbidden entry
`` `MERGE_PENDING`, `RESCOPE_PENDING` `` (§12 §8a O10 (b)). R-OLDLIST.
```
old: PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`,
new: PR-35 returns only `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,
```

**`:49` — Material rescope.** Step 24, D23-C term. Heading KEEP; `v:57`, `v:74` KEEP.
```
old: Given evidence that implementation requires an approved-boundary change,
new: Given evidence that implementation requires a material change to the Epic-level commitment,
```

**`:57` — Approved rescope continuation.** Converged on `:141`'s wording (§12 §8a O15 (b)).
```
old: resume the recorded phase in the same PR session, workspace/worktree, branch, open PR and original Proceed.
new: resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR and original Proceed.
```

**`:87` — Merge readiness.** Step 40 (coverage:16). `v:82` KEEP. Glue as compiled (§12 §8a O22 (a)).
```
old: The conditional prompt separately requires
new: The conditional prompt, usable {FALLBACK}, separately requires
```

**Five new cases, appended after the file's last line** (one blank line before each heading), in this
order. The first is child C6's (glue as compiled, §12 §8a O22 (a)). The other four are §12 §8a O16 (b);
their wording is compiled from C-DEC, C-LAT, C-SUB and C-DISPATCH and listed in 8a.11 (U-8a-1). Each
avoids the literals it would otherwise mask ("An *In-flight decisions* section", "Decide it during
work", "Subscribing is not polling", "no session is created by an agent") and every forbidden entry.
```
insert:

## PR-40 rejection re-plan

Given a PR-40 `REJECT` (`reject_replan`) for this `WORK_UNIT_ID`, whose pull request merged under the earlier plan cycle, PR-20 plans that work unit again in a new top-level session that Nathan creates, and the new plan receives its own Proceed. PR-30 starts only from the Proceed of its own plan. {LANDED} PR-30 creates a new branch and a new pull request for the new plan. The earlier Proceed is spent and is never reused.

## In-flight decisions

Given a decision that is not material and is obvious, necessary to deliver the approved scope, and consistent with the Epic's objective and controlling constraints, PR-30 or PR-35 decides it, implements it, tests it, and records it under *In-flight decisions* in `PR_IMPLEMENTATION_RESULT`: what changed, why it was necessary to deliver the approved scope, and what was tested, by test identity and outcome. That holds even if the plan did not anticipate it; `NONE` is recorded when there were none.

## Implementor latitude

Given a planned approach found incomplete, impractical or inferior, that alone is not material. A change to the Epic-level commitment — its outcome or objective; approved acceptance criteria; a protected architectural, security, data-model or external-contract boundary; the scope of several planned work units; an accepted dependency or cross-team commitment; or budget, schedule or risk needing Product Owner direction — takes the formal rescope route. Anything that is neither material nor obvious and necessary is not done; it is recorded as a candidate for its owner.

## Pull request subscription

Given PR-35 entry, subscribe to the pull request's activity where the surface provides it, and record the subscription as active only when the tool result confirms that this session receives the pull request's events. Act on review, comment and check events as they arrive. Without an active subscription, `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. The subscription creates no session.

## Observed merge

Given `MERGE_PENDING` returned with the conditional PR-40 block and an active subscription, when the subscription delivers the merge of the identified PR — a merge Nathan performs — PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff and returns control. Nathan creates the PR-40 session and pastes it; PR-40 still verifies the merged state and landed lineage independently. The conditional PR-40 block stays usable only after Nathan merges and {FALLBACK}. No agent merges or creates a session.
```
- The re-plan case contains neither "receives its own PO Proceed" nor "normal Plan/instruction path"
  (existing forbidden entries; measured).

**`:53` KEEP verbatim.** "preserve the immutable base, decision, PR session, workspace/worktree, …"
names the recorded phase's session and restates no reversed rule (S-4; §E records it).

### 8a.3 `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py`

**`required` (`:25`–`:86`).** Existing labels unchanged (§12 §8a O22 (a)).

| `v:` | label | disposition | new value / note | regression |
|---|---|---|---|---|
| 26 | revision | REPLACE | `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0` | R-rev |
| 27–31 | stage availability; conditional remedy evidence; stage boundary; preserved local verification; PR-35 fit | KEEP | — | clean control |
| 32 | single session | REPLACE | `run in two dedicated sessions` (pr-relay-graph:2) | R-32 |
| 33–36 | PR-30 ownership; PR-35 ownership; PR-30 result; PR-30 complete result vocabulary | KEEP | — | clean control |
| 37 | PR-35 complete result vocabulary | REPLACE | `{V6}` (sweep:3, coverage:14) | R-37 |
| 38 | PR-30 to PR-35 | REPLACE | ``exactly one complete `PR-35` handoff to the dedicated PR-35 session`` (pr-relay-graph:0) | R-38 |
| 39–43 | workspace recovery … review-first behavior | KEEP | — | clean control |
| 44 | merge-ready ownership | REPLACE | `Continue in this phase's own dedicated session until all applicable predicates are true` (sweep:4, coverage:17) | R-44 |
| 45–54 | manual merge … paste-ready handoff | KEEP | `v:48`, `v:52`, `v:53`, `v:54` checked above | clean control |
| 55 | exact GCF-17 continuity list | REPLACE | `{NINE}` (pr-relay-graph:1) | R-55 |
| 56–62 | formal rescope … continuation prompt | KEEP | `v:58`, `v:61` survive `:133` | clean control |
| 63 | same PR continuation | REPLACE | `the recorded phase's own dedicated session, workspace/worktree, branch, open PR` (sweep:4, coverage:17) | R-63 |
| 64–85 | original Proceed … specification change terminal | KEEP | `v:83` kept deliberately (pr-relay-graph:8) | clean control |

**NEW required entries.** Eight label/literal pairs, inserted between `v:84` and `v:85`, in this order:
```
"artifact holds results": "never carries the only copy"
"in-flight decisions": "An *In-flight decisions* section"
"material latitude": "Decide it during work"
"one Proceed per plan": "One Proceed per approved per-PR plan"
"top-level PR-35 session": "never as a subagent, forked agent or workflow agent of PR-30"
"subscription is not polling": "Subscribing is not polling"
"no agent-created session": "no session is created by an agent"
"handoff carries no branch": "It carries no branch and no commit"
```
Sources and regressions:
- "artifact holds results": step 10, pr-relay-graph:11. R-CART.
- "in-flight decisions": step 20, pr-relay-graph:10, adversary:5. R-CDEC.
- "material latitude": step 24, pr-relay-graph:12. R-CLAT.
- "one Proceed per plan": child C6; §12 §8a O9 (a). R-CPROC.
- "top-level PR-35 session": A1-8 and the D23 clarification's *Guard*; W-1's guard phrase. It matches
  the C-SESSION clause and not C-TOP. R-TOP.
- the last three: §12 §8a O12 (b). R-SUB, R-DISP, R-NOBRANCH. Their labels are glue (U-8a-2).

**`forbidden` (`:91`–`:103`).** All 11 existing entries KEEP; none is narrowed (child C6,
pr-relay-graph:14). Nine entries are appended after `"[TODO"`, in this order:
```
one dedicated PR-development session
same-session `PR-35` handoff
{V5}
Continue in the same dedicated PR session until all applicable predicates are true
{TEN}
same dedicated PR session, workspace/worktree, branch, open PR
followed in the same session by PR-35
`MERGE_PENDING`, `RESCOPE_PENDING`
ten-field
```
- The first six are the old values of the REPLACE literals (R-32, R-38, R-37, R-44, R-55, R-63).
- The seventh is child C6's, also coverage:21's fix (R-C6-27).
- The last two are §12 §8a O10 (b): the old result lists and "ten-field" (R-OLDLIST, R-TENFIELD).
- **Measured:** on the edited package none of the 20 forbidden entries occurs, case-insensitively,
  anywhere in `SKILL.md + behavior-cases.md`. "exactly one same-session PR-35 re-entry handoff" does
  not contain "same-session `PR-35` handoff".

**`case_headings` (`:108`–`:130`).** Five headings are appended after `"## Not ready"`, in the order the
cases are appended (child C6; §12 §8a O16 (b)):
```
## PR-40 rejection re-plan
## In-flight decisions
## Implementor latitude
## Pull request subscription
## Observed merge
```
Regressions: R-heading, R-H-DEC, R-H-LAT, R-H-SUB, R-H-OBS.

### 8a.4 Must-fail regressions for `glow-hde-pr-development`

Each runs on a fresh scratch copy of the edited package with `PYTHONDONTWRITEBYTECODE=1`
(`/tmp/claude-0/v2work8/work/regress_8a.py`, sha256 `1e9c0b0e9423dbae…`). All 23 were measured and met
the criterion of 8a.0.

| id | serves | mutation | expected stdout (exit 1) | non-fail-fast set |
|---|---|---|---|---|
| R-rev | `v:26` | at `:8`, 1.3.0 → 1.2.5 | `FAIL: missing revision contract` | 1 |
| R-32 | `v:32` | inject the old `:53` first sentence | `FAIL: forbidden or unfinished content present: one dedicated PR-development session` | 1 |
| R-37 | `v:37` | inject `{V5}.` | `FAIL: forbidden or unfinished content present: {V5}` | **2**: `{V5}` and `` `MERGE_PENDING`, `RESCOPE_PENDING` `` |
| R-38 | `v:38` | inject "followed by exactly one complete same-session `PR-35` handoff." | `FAIL: forbidden or unfinished content present: same-session `PR-35` handoff` | 1 |
| R-44 | `v:44` | inject the old `:100` line | `FAIL: forbidden or unfinished content present: Continue in the same dedicated PR session until all applicable predicates are true` | 1 |
| R-55 | `v:55` | inject `{TEN}.` | `FAIL: forbidden or unfinished content present: {TEN}` | **2**: `{TEN}` and `ten-field` |
| R-63 | `v:63` | inject the old `:141` sentence | `FAIL: forbidden or unfinished content present: same dedicated PR session, workspace/worktree, branch, open PR` | 1 |
| R-C6-27 | child C6, coverage:21 | inject the whole old `:27` line | `FAIL: forbidden or unfinished content present: followed in the same session by PR-35` | 1 |
| R-OLDLIST | O10 (b) | inject the old cases `:21` list, "PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`, …" | `FAIL: forbidden or unfinished content present: `MERGE_PENDING`, `RESCOPE_PENDING`` | 1 |
| R-TENFIELD | O10 (b) | inject the old `:158` sentence ("…which the ten-field continuity list requires.") | `FAIL: forbidden or unfinished content present: ten-field` | 1 |
| R-CART | step 10 | delete `{C-ART}` | `FAIL: missing artifact holds results contract` | 1 |
| R-CDEC | step 20 | delete `{C-DEC}` | `FAIL: missing in-flight decisions contract` | 1 |
| R-CLAT | step 24 | delete `**Decide it during work:**` | `FAIL: missing material latitude contract` | 1 |
| R-CPROC | child C6 | delete `{C-PROCEED}` at `:27` | `FAIL: missing one Proceed per plan contract` | 1 |
| R-TOP | A1-8 | delete `{A18}` | `FAIL: missing top-level PR-35 session contract` | 1 |
| R-SUB | O12 (b) | delete "Subscribing is not polling, and it creates no session." | `FAIL: missing subscription is not polling contract` | 1 |
| R-DISP | O12 (b) | delete " No agent merges, and no session is created by an agent." | `FAIL: missing no agent-created session contract` | 1 |
| R-NOBRANCH | O12 (b) | delete "It carries no branch and no commit: " | `FAIL: missing handoff carries no branch contract` | 1 |
| R-heading | child C6 | rename `## PR-40 rejection re-plan` | `FAIL: missing behavior case: ## PR-40 rejection re-plan` | 1 |
| R-H-DEC | O16 (b) | rename `## In-flight decisions` | `FAIL: missing behavior case: ## In-flight decisions` | 1 |
| R-H-LAT | O16 (b) | rename `## Implementor latitude` | `FAIL: missing behavior case: ## Implementor latitude` | 1 |
| R-H-SUB | O16 (b) | rename `## Pull request subscription` | `FAIL: missing behavior case: ## Pull request subscription` | 1 |
| R-H-OBS | O16 (b) | rename `## Observed merge` | `FAIL: missing behavior case: ## Observed merge` | 1 |

**Why R-37 and R-55 expect two.** §12 §8a O10 (b) forbids the short substrings as well as the old
literals, and each old literal contains its short substring. The fail-fast line is the long entry,
because it sits earlier in `forbidden`. Both findings are that regression's own; the expected set is
stated exactly (U-8a-3 records this for E4).

**A limit, measured.** Reverting a line in place, instead of injecting, fires the missing new literal
and the forbidden old one. Only the injection form meets E4 item 9.

### 8a.5 The 1.3.0 revision and every pin of it

`1.2.5` → `1.3.0` (amendment, *New revisions*; pr-relay-graph:16, fv-main:25, fv-rest:26). Measured,
complete for the synced tree. Paths are written in full (verifier conflict 19).
```
glow-hde-pr-development/SKILL.md:8                                                            this section
glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:26                        this section
flowmaster-validate/scripts/validate_gcfpe_20260914.py:1722                                   contract subset primary_skill_revision (§8b)
flowmaster-validate/scripts/validate_gcfpe_20260914.py:2592                                   SKILL_CONTRACT marker (§8b)
flowmaster-validate/scripts/validate_gcfpe_current.py:651                                     PR_SKILL_CONTRACT marker (§8b; S-5, §12 §8b O14 (a))
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:28           installed_skill_revisions (§8b)
flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:3003    pr_development_contract.primary_skill_revision (§6 regenerator)
change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:3003            pr_development_contract.primary_skill_revision (§6 regenerator)
```
**Kept, not a pin of the installed revision:** `flowmaster-validate/scripts/validate_gcfpe_current.py:302`
(`1.2.0`) checks the historical 091326.2 contract; it stays (§12 §8a O25; S-5). The historical
contracts (`1.2.0`, `1.1.0`) keep their bytes (A1-1).

### 8a.6 Other packages' literals that read these bytes

Owned by §8b; listed so both sections use byte-identical values.
- `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2592`–`:2595` (case-insensitive
  `SKILL_CONTRACT`): revision → 1.3.0 (REPLACE); `:2594` → `{NINE}` (REPLACE; fv-main:24, fv-rest:18);
  `REMOTE_EVIDENCE_PENDING`, `PR_REMOTE_ACTION_LEDGER`, the no-merge marker (`:110`) and the
  handoff-shape marker (`:162`) KEEP.
- `flowmaster-validate/scripts/validate_gcfpe_current.py:651`–`:652`: `:651` → `1.3.0`; `:652`
  "one dedicated PR-development session" → `run in two dedicated sessions`, which this section places
  at `:3` and `:53` (S-5; §12 §8b O14 (a); verifier contradiction 7).
- `{NINE}` matches byte for byte at `change-flow/SKILL.md:303`,
  `change-flow/scripts/validate_gcfpe_20260914.py:1022`, `flowmaster-validate/SKILL.md:164`,
  `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594`, and the amthor sites in 8a.7–8a.9.
- **Measured** on a copy with both sections' skill-side edits applied (today's contract; §8b.12 copy A):
  `validate_gcfpe_current.py` (default and explicit alias) `ok: true`; `validate_gcfpe_20260914.py`
  `ok: true`; the default `validate_flowmaster.py` suite `FLOWMASTER_SUITE_PASS` after
  `SKILL_TREE_SHA256` was recomputed.

### 8a.7 `amthor-workspace-governance-audit/SKILL.md`

**`:10` — revision.** "Bumped one minor" → 1.12.0. Also pinned at `run_fixture_suite.py:307` (8a.9).
```
old: **WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3
new: **WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0
```

**`:32` — predecessor archive.** registry-audit:16; C-VERSION applies from the next release (A1-3).
```
old: After authorized selection, verify each predecessor prompt moved intact
new: After authorized selection, verify each predecessor prompt of a member that received a successor page moved intact
```

**`:38` — handoff invariant, plus the C-ART and C-PLACE invariants.** C-HANDOFF (registry-audit:13);
§12 §8a O21 (b).
- The first sentence stays: `run_fixture_suite.py:315` requires "exactly one fenced `text`
  `NEXT_PROMPT_HANDOFF` block" here. KEEP.
- The second sentence, including the Notion-resident clause, becomes C-HANDOFF. The terminal sentence
  stays.
- Two invariant bullets follow the `:38` bullet: C-ART, then C-PLACE, each verbatim behind a one-clause
  scope (glue: U-8a-4).
```
old: It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the receiving role/session and work identifiers; carries every already-existing required artifact by exact identity/version and its repository path, or its direct Notion URL for a Notion-resident artifact; carries status, decisions, constraints, unresolved items, next action, and expected output; and contains no blanks, menus, or alternative destinations. Terminal results identify completion and the native Product Owner return.
new: {C-HANDOFF} Terminal results identify completion and the native Product Owner return.
- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, as the first sentence of its output section: {C-ART}
- Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, after its handoff rule: {C-PLACE}
```
(The `old:` and `new:` spans each end with the line break that closes the bullet.)

**`:40` — primary-skill invariant.** C-SESSION (registry-audit:13), step 36's wording. The "adds no …
session … cross-session route" list takes the registry wording (§12 §8a O7 (b)).
```
old: - GCFPE PR-30, same-session PR-35, interrupted PR recovery,
new: - GCFPE PR-30, PR-35 in its own dedicated session, interrupted PR recovery,
```
```
old: Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session.
```

**`:41` — continuity list.** registry-audit:13 and :15. `{NINE}` only (§12 §8a O19 (a)). The
fixture-suite constant equals this text (8a.9).
```
old: - {TEN}. Require PR-30
new: - {NINE}. Require PR-30
```

**`:43` — PR-30 recovery.** Child C10, sweep:16, registry-audit:13.
```
old: or unsupported platform limitation. PR-30 owns
new: or unsupported platform limitation. {LANDED} PR-30 owns
```
```
old: ends with `PR_CANDIDATE_PUBLISHED` plus one complete same-session PR-35 handoff.
new: ends with `PR_CANDIDATE_PUBLISHED` plus one complete PR-35 handoff.
```

**`:44` — single Proceed.** Child C10. The child's words, then C-PROCEED's second and third sentences
verbatim (§12 §8a O18 (a)). The rest of `:44` stays.
```
old: - One Product Owner `Proceed` authorizes the single PR-30/PR-35 work unit through genuine merge readiness, not merge.
new: - One Product Owner `Proceed` per plan cycle authorizes the PR-30/PR-35 work unit through genuine merge readiness, not merge. A continuation — PR-30 to PR-35, a rescope return, a recovery — never requires or creates a second Proceed. Only a PR-40 `REJECT` re-plan creates a new plan, and that plan receives its own Proceed.
```

**`:47` — rescope resume.** registry-audit:13, "the recorded phase's own session".
```
old: phase in the same session/workspace/worktree/branch/open PR/original Proceed.
new: phase in the recorded phase's own session/workspace/worktree/branch/open PR/original Proceed.
```

**`:49` — merge chain.** registry-audit:13, adversary:9. C-DISPATCH verbatim after the first sentence;
the assertion sentence takes `{FALLBACK}` (glue as compiled, §12 §8a O22 (a)).
```
old: - PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only that Nathan manually merged the identified PR;
new: - PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only that Nathan manually merged the identified PR;
```

**New invariant bullet after `:49`.** A1-8 (the fifth package's semantic invariant); sweep:25 verbatim,
"launches" kept (§12 §8a O24 (a)).
```
old: Never treat `MERGE_PENDING` as a current post-merge fact.

new: Never treat `MERGE_PENDING` as a current post-merge fact.
- {INVARIANT}

```

**Lines kept verbatim (S-4; §E records each):** `:25` "Do not provision or message sessions" (a
prohibition). No other line restates a reversed rule.

### 8a.8 `amthor-workspace-governance-audit/references/`

**`interoperability-contracts.md`** (registry-audit:14)
- **`:13`**, step 35:
```
old: implementation/publication, same-session PR-35 review/readiness,
new: implementation/publication, PR-35 review/readiness,
```
- **`:18`**, step 35; the "adds no" list takes the registry wording (§12 §8a O7 (b)):
```
old: one selected PR-30 → PR-35 same-session phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: one selected PR-30 → PR-35 phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or any session beyond its own dedicated PR-35 session.
```
- **`:53`**: KEEP verbatim. `run_fixture_suite.py:316` requires "exactly one fenced `text`
  `NEXT_PROMPT_HANDOFF`" here, and the line states only the block's shape.
- **`:54`**, step 14 (C-HANDOFF):
```
old: - The handoff begins with the exact selected destination prompt name, version, and direct Notion URL and carries the actual receiving role/session, work identifiers, every already-existing required artifact by exact identity/version and its repository path or its direct Notion URL for a Notion-resident artifact, state, decisions, constraints, unresolved items, next action, and expected output.
new: - {C-HANDOFF}
```
- **`:68`**, step 35:
```
old: plus exactly one complete same-session PR-35 handoff.
new: plus exactly one complete PR-35 handoff.
```
```
old: {TEN}.
new: {NINE}.
```
- **`:74`**, step 40, as at SKILL.md `:49`:
```
old: PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only a manual merge;
new: PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only a manual merge;
```
- **`:96`**, step 35:
```
old: PR-30/PR-35 same-session skill/recovery
new: PR-30/PR-35 skill/recovery
```
- **Kept verbatim (S-4; §E records each):** `:16` "Session Branch and Session Relay may provision or
  contact independent sessions only in separately authorized work" — maintenance work, which the D23
  clarification does not bind; `:72` "preserve the same vehicle/original Proceed"; `:80`
  `DEDICATED_ONE_OFF` (S-9 records RS-40's class as pre-existing and out of scope).

**`behavioral-fixtures.md`** (registry-audit:14)
- **`:48`**:
```
old: {TEN}.
new: {NINE}.
```
- **`:49`**: KEEP verbatim (§12 §8a, "`behavioral-fixtures.md:49` stays verbatim"). PR-35 still creates
  no session under the D23 clarification.
- **`:50`**:
```
old: with one complete same-session PR-35 handoff.
new: with one complete PR-35 handoff.
```
- **`:52`**, step 40:
```
old: separately require Nathan's later manual-merge assertion and PR-40's
new: separately require Nathan's later manual-merge assertion, usable {FALLBACK}, and PR-40's
```
- **Two new fixture bullets before `:53`** (§12 §8a O21 (b): a `MERGE_OBSERVED` acceptance fixture and
  a re-plan fixture). Words from C-DISPATCH, C-PR20-ENTRY and child C8's three negatives (U-8a-4).
```
old: - Require exact rescope return phase
new: - Accept PR-40 entry on `MERGE_OBSERVED` only when the subscribed PR-35 session, or RS-40 resuming the PR-35 phase, observed through an active subscription the merge of the identified PR that Nathan performed, and Nathan pasted the handoff into a session he created; accept Nathan's manual-merge assertion {FALLBACK}. Reject an agent merge, automatic dispatch, an agent-created session, and PR-40 entry before any merge.
- Accept a PR-40 `REJECT` for a precise in-scope defect in landed work only as a re-plan through PR-20 in a new top-level session Nathan creates, with a new plan and its own Proceed; a pull request merged under an earlier plan cycle is landed history. Reject that `REJECT` routed to PR-30, a second Proceed for the same plan, and a Proceed between PR-30 and PR-35.
- Require exact rescope return phase
```

**`project-prompt-registry-schema.md:42` — the `session_class` enum.** S-8 (§12 §8a O20 (a);
registry-audit:20). The enum gains the value step 33 gives PR-35's row. Measured: the registry
validator (`scripts/validate_project_prompt_registry.py`) does not read this enum and still returns
`{"valid": true, "problems": []}`.
```
old:   session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN
new:   session_class: DEDICATED_ONE_OFF | CHANGE_LIFETIME | ROLE_CONTINUING | ORCHESTRATOR_RUN | DEDICATED_PR_REVIEW_SESSION
```

**Unchanged files:** `rule-catalog.md`, `report-contracts.md`, `workspace-skill-registry-schema.md`;
`epic-reengineering-interoperability.md` (historical provenance); every script except
`run_fixture_suite.py`; `assets/icon.svg`. A scan found no other statement of a reversed rule in them.

### 8a.9 `amthor-workspace-governance-audit/scripts/run_fixture_suite.py`

registry-audit:15: the constant is updated, not deleted, so the parity guard stays. §12 §8a O11 (b)
adds the forbidden assertion for all three files.
```
old: EXACT_GCF17_CONTINUITY = "{TEN}"
new: EXACT_GCF17_CONTINUITY = "{NINE}"
RETIRED_GCF17_CONTINUITY = "{TEN}"
```
```
old: self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", skill)
new: self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0", skill)
```
In `test_exact_gcf17_continuity_parity`, after its last `assertIn`:
```
old:         self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)

new:         self.assertIn(EXACT_GCF17_CONTINUITY, fixtures)
        for text in (skill, interoperability, fixtures):
            self.assertNotIn(RETIRED_GCF17_CONTINUITY, text)

```
Literal dispositions: `EXACT_GCF17_CONTINUITY` REPLACE (`{NINE}`); `RETIRED_GCF17_CONTINUITY` NEW,
FORBID `{TEN}` in all three files; the revision assertion REPLACE; `:315`–`:316` fenced-block
assertions KEEP.

**Must-fail regressions, measured** (`regress_8a.py`, with `TMPDIR` inside the scratch area). Pass =
`Ran 34 tests`, `FAILED (failures=1)`, exactly the named test failing.

| id | mutation | failing test |
|---|---|---|
| A-skill-list | `{NINE}` → `{TEN}` in `SKILL.md` | `test_exact_gcf17_continuity_parity` |
| A-interop-list | `{NINE}` → `{TEN}` in `interoperability-contracts.md` | `test_exact_gcf17_continuity_parity` |
| A-fixtures-list | `{NINE}` → `{TEN}` in `behavioral-fixtures.md` | `test_exact_gcf17_continuity_parity` |
| A-rev | revision 1.12.0 → 1.11.3 in `SKILL.md` | `test_exact_gcf17_continuity_parity` |
| A-handoff-kept | `:38`'s "exactly one fenced …" phrase damaged | `test_exact_fenced_text_handoff_parity` |
| A-inject-skill | `{TEN}` added beside `{NINE}` in `SKILL.md` | `test_exact_gcf17_continuity_parity` |
| A-inject-interop | the same in `interoperability-contracts.md` | `test_exact_gcf17_continuity_parity` |
| A-inject-fixtures | the same in `behavioral-fixtures.md` | `test_exact_gcf17_continuity_parity` |

The three injection rows close v1's measured limit (injection beside passed all 34 tests).

### 8a.10 What was measured (v2)

All runs used copies under `/tmp/claude-0/v2work8/` with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR`
inside the scratch area. Afterwards no `.pyc` or `__pycache__` existed there or in the drafters'
directories, the installed tree was only read, and `git status` in the repository was clean. No prompt
body was read.

- **Anchors.** Every `old:` span in 8a.1–8a.9 applied exactly once to a copy of the installed tree
  (`apply_skills.py`).
- **Edited copy, clean control:**
  - the PR skill validator prints `PASS: Glow HDE PR development skill structural contract`, and the
    non-fail-fast evaluation finds 0 failures;
  - the amthor suite runs 34 tests, OK;
  - `validate_project_prompt_registry.py` on
    `/home/user/glow-hdengine-v2/docs/prompt_ecosystem_management/project-prompt-contract-registry.md`
    returns `{"valid": true, "problems": []}`.
- **Regressions:** 23 of 23 PR-skill regressions exact (8a.4); 8 of 8 amthor regressions exact (8a.9).
- **Together with §8b's skill-side edits** (8b.12 copy A): the default `validate_flowmaster.py` suite
  returns `FLOWMASTER_SUITE_PASS` with no findings once `SKILL_TREE_SHA256` is recomputed.
- **No session creation.** A scan of the edited main-ecosystem skill text, outside the Flowmaster core,
  for create/spawn/launch/provision/start/open/schedule … session found only prohibitions, Nathan as
  the creator, the A1-6 override and the sweep:25 invariant.

### 8a.11 Unsettled

§12 settles every §8a question by option letter. These items are the words or consequences the
settled options still leave open. Each carries the compiled value that 8a.1–8a.9 place, so EXECUTE can
proceed if Nathan confirms it, and stops if he does not (§0).

- **U-8a-1 — Wording of the four O16 (b) behavior cases.** §12 §8a O16 (b) adds cases and headings for
  C-DEC, C-LAT, C-SUB and `MERGE_OBSERVED`; no source gives their headings or text. Compiled: the
  headings `## In-flight decisions`, `## Implementor latitude`, `## Pull request subscription`,
  `## Observed merge`, and the texts in 8a.2, built from the canonical texts' own words and written so
  they do not mask the required literals.
- **U-8a-2 — Labels of the three O12 (b) literals.** Compiled: "subscription is not polling",
  "no agent-created session", "handoff carries no branch". Labels appear only in failure messages.
- **U-8a-3 — Expected sets of R-37 and R-55.** Under §12 §8a O10 (b) each fires two forbidden entries.
  v1's criterion "the non-fail-fast count is exactly one" becomes "exactly the stated set". If E4 must
  see one finding each, the only way is to drop the two long entries, which the short ones subsume;
  §12 does not say which.
- **U-8a-4 — Wording and placement of the O21 (b) amthor additions.** Compiled: two invariant bullets
  after `SKILL.md:38` ("Every body whose registry row requires `NEXT_PROMPT_HANDOFF` carries, …:
  {C-ART}" / "…: {C-PLACE}") and two fixture bullets before `behavioral-fixtures.md:53` (8a.8). No
  source asks for fixture-suite assertions on them, and none is compiled.

## §8b Skill edits: change-flow, session-relay-flowmaster, tw-flowmaster, flowmaster-validate

**v2, consolidated.** This section replaces v1 §8b (v1 lines 4815–6236). Every §12 decision is applied
inline and cited (`§12 §8b Ox`, or the id: `S-5`, `W-9`, `V-6` …). v1's option lists and its 8b.14
are gone; the options §12 did not name are void (§0). What §12 does not settle is listed once, in 8b.14
*Unsettled*, with the compiled value placed here. Nothing in 8b.1–8b.13 is open.

It covers four of the six packages (A1-6): `change-flow`, `session-relay-flowmaster`, `tw-flowmaster`
and `flowmaster-validate`. Values owned elsewhere are cited, not repeated: §5 owns the R1 successor
files, digests, paths and the pin order; §6 owns every contract-only value; §4 owns the graph; §8a
owns `glow-hde-pr-development`, `amthor-workspace-governance-audit` and the tokens `{NINE}`, `{TEN}`,
`{V5}`, `{V6}`, `{FALLBACK}`, `{LANDED}`, `{A18}`. Where 8b.7 restates a §6 value as a validator
literal, it is §12's settled value (V-1 to V-8, W-1, W-2, W-8).

### 8b.0 Conventions

- **Line numbers** are those of the installed tree at
  `/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502`
  (read-only). On 2026-09-23 all four packages were byte-identical to the drafters' measurement copy
  (`diff -r` against `/tmp/claude-0/spec/s8b/skills`), so §2's digests hold: `change-flow` `80e877c2…`,
  `session-relay-flowmaster` `4ef8daa3…`, `tw-flowmaster` `fa3fac85…`, `flowmaster-validate`
  `b9ca212a…` (declared `SKILL_TREE_SHA256` `eb9634d6…`).
- **Every `old:` span was verified** to occur exactly once, by applying the edit set as scripted
  exact-substring replacements on a copy: skill text and skill-side literals by
  `/tmp/claude-0/v2work8/work/apply_8b.py` (sha256 `6988671a426e371a…`), the validator reversals by
  `patch_fv.py` (`5d03723189f4450c…`), the fixture deltas by `patch_fix_v2.py` (`7bce35b788bd6673…`).
  In `old:`/`new:` blocks, `\n` stands for a line break and `{TOKEN}` for its text.
- **Compile rule** is §8a.0's. S-4: every prose line that restates a reversed rule is converged; lines
  kept verbatim carry the reason §E records.
- **No session creation in skill text** (D23 clarification; D23 successor notes). The A1-6 override
  disables the core's fresh-session option in all three Flowmaster specializations; W-9 converts
  `change-flow:450`'s imperative and scopes the relay's provisioning route out of GCFPE main-ecosystem
  stages. No session-creation regex applies to skill text; `CONTRACT_FORBIDDEN` entries are exact
  phrases, each tested against the override and the invariant texts (§12 *Other settlements*).
- **Tokens.** `{C-SESSION}`, `{C-DISPATCH}`, `{C-HANDOFF}`, `{C-PLACE}`, `{C-PROCEED}`, `{C-D22}` are
  §3's texts, byte-exact (C-SESSION in W-6's form). `{OVERRIDE}` is §3's *GCFPE override*. `{STEP2}` is
  §3.5's step-2 literal. Three more, from §12:

```
{W9}
For a GCFPE main-ecosystem stage, return the paste-ready `NEXT_PROMPT_HANDOFF` and stop for Nathan; provisioning does not apply.

{S6}
A runtime handoff still names its destination by full name, version and direct Notion URL (C-HANDOFF); `NOTION_REFERENCE` stays versionless for reusable prompt text.

{S7}
`NOTION` means a maintenance surface that a destination rule names; live task, handoff and decision state lives in the repository.
```

- **How each check reads text:**

  | check | where | what it tests |
  |---|---|---|
  | `change-flow` validator skill clauses | `change-flow/scripts/validate_gcfpe_20260914.py:1020`–`:1031` | case-sensitive substring over the whole `SKILL.md`; fail-fast |
  | `change-flow` retired-phrase loop (new) | same file, after the clause block | case-**insensitive** substring (§12 §8b O15 (b)); fail-fast |
  | `CONTRACT_REQUIRED` | `flowmaster-validate/scripts/validate_flowmaster.py:113`, applied at `:1313`–`:1318` | case-sensitive substring over the whole `SKILL.md` |
  | `CONTRACT_FORBIDDEN` | `validate_flowmaster.py:304`, applied at `:1338`–`:1343` | case-insensitive substring over the whole `SKILL.md`, core included; never applied to `change-flow` (`:1340`) |
  | `CHANGE_FLOW_CONTRACT` | `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2580`–`:2586` | case-sensitive substring over `change-flow/SKILL.md` |
  | `SKILL_CONTRACT` | same file `:2590`–`:2606` | case-insensitive substring over the named skill's `SKILL.md` |
  | reference allowlist | `validate_flowmaster.py:1115`–`:1126` | every markdown link target `](references/…` must be in `OPTIONAL_REFERENCES`, and every listed path must be linked; plain-text filenames are not links |
- **Literal dispositions.** **KEEP** = verbatim, still present. **REPLACE** = a new value; the old one is
  guarded where a revert could come back. **FORBID** = the old text is put where a revert fails.
  **NEW** = a new check. Each REPLACE, FORBID and NEW entry names its must-fail regression (8b.10).
- **A regression passes** only when the findings on the mutated input, minus those on the clean input,
  are exactly the expected set (§9 item 9). For the fail-fast `change-flow` validator: exit 1 with
  exactly the expected line, and a non-fail-fast count of exactly one.

### 8b.1 The Flowmaster core and the GCFPE override (A1-6)

**Core boundaries.** No byte between the markers changes (A1-6). Measured on the edited copies: the
marker block, read as lines `BEGIN` through `END` with their newlines, is sha256 `4e565e40…` in all
three skills; the `change-flow` validator's `EXPECTED_CORE_SHA` `4d8bb9bf…` (`:26`, `:749`) KEEP.
```
change-flow/SKILL.md               :33 <!-- FLOWMASTER_CORE_BEGIN -->   :249 <!-- FLOWMASTER_CORE_END -->   specialization :250-:583
session-relay-flowmaster/SKILL.md  :23 <!-- FLOWMASTER_CORE_BEGIN -->   :239 <!-- FLOWMASTER_CORE_END -->   specialization :241-:724
tw-flowmaster/SKILL.md             :12 <!-- FLOWMASTER_CORE_BEGIN -->   :228 <!-- FLOWMASTER_CORE_END -->   specialization :230-:497
```
The core option the override disables sits at `change-flow:158`, `session-relay-flowmaster:148`,
`tw-flowmaster:137` ("3. a fresh spawned session in its own worktree only when no existing
authoritative session can do the work.").

**The override** goes in verbatim, once per skill, as its own paragraph in the specialization text, at
the positions simulated in v1 (§12 §8b O1 (a)):
- `change-flow`: a new paragraph after `:263`, in *Scope and endpoint*;
- `session-relay-flowmaster`: after `:255` (which W-9 also edits; 8b.4);
- `tw-flowmaster`: the first paragraph under `### GCFPE binding` (`:300`).
```
old: or manual PF controls.\n\n### Runtime entry gate
new: or manual PF controls.\n\n{OVERRIDE}\n\n### Runtime entry gate
```
```
old: ### GCFPE binding\n\n
new: ### GCFPE binding\n\n{OVERRIDE}\n\n
```
(The relay span is in 8b.4, combined with W-9.)

**Held in place** by one `CONTRACT_REQUIRED` entry per skill holding the whole override text (§12 §8b
O3 (a)). NEW; R-OV-1…3.

### 8b.2 `change-flow/SKILL.md`

**`:8` — revision.** 3.2.9 → 3.3.0. Pin sites: 8b.11. REPLACE; R-CF-REV.
```
old: CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9
new: CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0
```

**`:17`, `:19`, `:21` — R1 declarations.** `:17` (profile id) and `:19` (matrix digest) take §5's
values (A1-1; §12 *Successor oracle*). `:21` `R1_ROW_COVERAGE: 46/46` KEEP.

**Override** after `:263`: 8b.1.

**`:275` — entry-gate PR policy.** Step 35 (fv-rest:19, coverage:15). Glue as simulated (§12 §8b O5 (a)).
```
old: - The policy for one dedicated PR-development session per planned PR work unit, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, same-session PR-35 review/readiness,
new: - The policy for each planned PR work unit, run in two dedicated sessions, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, PR-35 review/readiness,
```

**`:277` — HDE execution handoff content.** The same artifact edit as relay `:273` (§12 §8b O18 (b)).
```
old: evidence destination, and cleanup/recovery owner in the handoff.
new: evidence destination, and cleanup/recovery owner in the output artifact that the handoff names.
```

**`:278` — manifest item.** fv-rest:19. Deletion only. The staging-boundary sentence on the line is
stale but no source touches it; it stays.
```
old: a selected PR-35 is lawful only as the same-session second phase of the existing GCF-17 PR work unit.
new: a selected PR-35 is lawful only as the second phase of the existing GCF-17 PR work unit.
```

**`:295` — the handoff rule.** Steps 14 and 19 (fv-rest:25). The first sentence stays: validator `:1024`
"exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block" KEEP. The field list becomes C-HANDOFF; C-PLACE
is appended at the end of the line (order C-HANDOFF then C-PLACE, as in the bodies; §12 §8b O19).
NEW literal `It carries no branch and no commit` (§12 §8b O16 (b)); R-CF-HND.
```
old: It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the actual receiving role/session and change/work identifiers; provides every required artifact repository path; and carries current status, decisions, constraints, unresolved items, next action, and expected output.
new: {C-HANDOFF}
```
```
old: Terminal results state completion and the native Product Owner return.
new: Terminal results state completion and the native Product Owner return. {C-PLACE}
```

**`:301` — the two-phase paragraph.** Step 35 and child C7.
- KEEP "PR-30 and PR-35 are two phases" — inside `{C-SESSION}` (W-6); validator `:1021` and
  `CHANGE_FLOW_CONTRACT` `:2581` (fv-main:26, fv-rest:17).
- REPLACE validator `:1023` "one dedicated PR-development session" → "run in two dedicated sessions";
  old FORBID (retired loop). R-CF-RP-1.
- NEW "never as a subagent, forked agent or workflow agent of PR-30" (A1-8; W-1's guard phrase). R-CF-A18.
- NEW "One Proceed per approved per-PR plan" (C-PROCEED; §12 §8b O16 (b), the literal §8a O9 (a)
  fixes; U-8b-7). R-CF-PROC.
- The first sentence ("Product Owner `Proceed` authorizes …") stays. C-PROCEED goes after the
  paragraph's last sentence (child C7; sweep:22).
```
old: PR-30 and PR-35 are two phases of that one work unit and retain one original Proceed, one dedicated PR-development session, one workspace/worktree, one branch, one pull request, one PR instruction and detailed Plan, one primary skill, and continuous recovery/artifact lineage.
new: {C-SESSION}
```
```
old: exactly one complete same-session PR-35 handoff;
new: exactly one complete PR-35 handoff to the dedicated PR-35 session;
```
```
old: coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness.\n
new: coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness. {C-PROCEED}\n
```

**`:303` — the continuity list.** Step 29, fv-rest:18. Validator `:1022` REPLACE `{TEN}` → `{NINE}`; old
FORBID (R-CF-RP-2); deletion R-CF-NINE.
```
old: {TEN}
new: {NINE}
```
```
old: same-session continuation cannot add, omit,
new: continuation cannot add, omit,
```

**`:305` — result vocabularies.** Step 38, A1-5. Only the PR-35 list changes; `{V5}` FORBID
(R-CF-RP-7). "exactly one same-session PR-35 re-entry handoff" stays (PR-35's own session; §8a keeps
the same phrase at PR skill `:112`).
```
old: {V5}
new: {V6}
```

**`:307` — the interoperability rule.** Steps 29–30 set `adds.session` and, per V-1,
`adds.cross_session_route` to 1. So "same-session", "session" and "cross-session route" leave the
"permits no extra …" list; the list's "or" moves to its new last item. Old phrase FORBID (R-CF-RP-3).
```
old: permits this one selected same-session PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: permits this one selected PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row.
```

**`:313`, `:323` — rescope sentences.** KEEP verbatim (child C7; §12 §8b O10). C-LAT and the step-14
field-list clause are not placed beside them in this skill; C-HANDOFF is placed at `:295`.

**`:321` — RS-40 resume.** sweep:20's wording (§12 §8b O34 (b)); "workspace/" is kept (U-8b-6).
```
old: it uses selected RS-40 to resume the recorded phase in the same session/workspace/worktree/branch/open PR under the original Proceed.
new: it uses selected RS-40 to resume the recorded phase in that phase's own session, workspace/worktree, branch and open PR under the original Proceed.
```

**`:331` — the merge boundary.** Step 40 (sweep:12, coverage:3). The three no-merge sentences KEEP; the
assertion clause takes `{FALLBACK}`; C-DISPATCH is appended; "Never present `MERGE_PENDING` as a current
post-merge fact." stays. Old phrase FORBID (R-CF-RP-8). NEW literal "no session is created by an agent"
(C-DISPATCH; §12 §8b O16 (b)); R-CF-DISP.
```
old: PR-35's `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only.
new: PR-35's `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}
```

**`:353` — runtime approval.** sweep:13's sentence with its predicate replaced by `{FALLBACK}`
(coverage:3). `PRODUCT_OWNER_RUNTIME_APPROVAL = PR Implementation Proceed invocation`
(`CONTRACT_REQUIRED['change-flow']`) KEEP. "PR-40 must independently verify …" stays. Old sentence
FORBID (R-CF-RP-9).
```
old: A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred; it is not a merge approval or merge instruction.
new: Where the subscribed PR-35 session observed the merge, that event is the fact PR-40 is entered on; {FALLBACK}, Nathan's later PR-40 invocation asserts the manual merge; neither is a merge approval or instruction.
```

**`:365` — actors table.** Step 35; C-SESSION's second and third sentences (§12 §8b O6 (a)). Old cell
FORBID (R-CF-RP-10).
```
old: | Per-PR planning and implementation | One dedicated session per planned PR work unit; the same session performs both |
new: | Per-PR planning and implementation | PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. |
```

**`:366` — PR merge row.** KEEP verbatim (S-4; §E records the reason): "no automatic dispatch or agent
merge from Proceed or PR-40" restates C-DISPATCH, under which dispatch is a paste and no agent creates
a session; the launch option it once contradicted is withdrawn (coverage:4; the `D23` clarification).

**`:411` — manual-control meaning.** fv-rest:19. Deletion (§12 §8b O7 (a)). Old phrase FORBID
(R-CF-RP-11).
```
old: has only the manual-merge-assertion meaning defined above;
new: has only the meaning defined above;
```

**`:450` — GCF-14.** W-9 (verifier contradiction 1). The old imperative joins the retired-phrase list
(R-CF-RP-14). "That session validates …" stays.
```
old: - GCF-14 — Create one dedicated PR session for one planned PR work unit.
new: - GCF-14 — Nathan creates one dedicated top-level PR session for one planned PR work unit.
```

**`:451`, `:452` — GCF-15, GCF-16.** KEEP (A1-1: GCF-15's session wording stays, read per plan cycle;
"that same session" is GCF-14's, PR-30's session). GCF-16 does not change (the `D23` correction).

**`:453` — GCF-17.** sweep:13, coverage:15, mirroring the successor row. A1-1's actor cell is the
subject, and A1-1's PR-35 session cell is appended (§12 §8b O8 (b)). Old phrase FORBID (R-CF-RP-12).
```
old: GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35, validates it, and creates exactly one active branch and pull request.
new: GCF-17 — The dedicated PR session (PR-30 phase) and the dedicated PR-35 session (PR-35 phase) implement only that work unit across selected PR-30 and PR-35, validate it, and create exactly one active branch and pull request. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session.
```

**`:455` — GCF-17.LINEAGE.** Child C7 and C-DISPATCH; words from `{FALLBACK}`, C-DISPATCH and A1-7's
`reject_replan` condition (§12 §8b O9 (a)). Old sentence FORBID (R-CF-RP-13).
```
old: Only after Nathan later asserts that the identified PR was manually merged may that invocation run.
new: Only after Nathan has manually merged the identified PR, and {FALLBACK}, may that invocation run; where the subscribed PR-35 session observed the merge, PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff.
```
```
old: This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only.
new: This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only. A precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed (GCF-14).
```

**`:557` — the runtime map.** The link target becomes the successor map only, and the SHA-256 its
digest (A1-1; §12 *Successor oracle*, OQ-7 (a)). The sentence describes it as the current projection
(§12 §8b O11 (a)); wording U-8b-4. Values from §5.
```
old: load the complete [bundled 46-row runtime map](references/glow-hde-canonical-change-flow-r1-runtime-map.json), SHA-256 `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`, as immutable historical baseline evidence. Preserve its original rows and source digests.
new: load the complete [bundled 46-row runtime map](references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json), SHA-256 `<successor runtime map sha256, §5>`, as the current runtime projection of the successor R1 oracle. Preserve its rows and source digests.
```

**`:559` — the current overlay.** A1-6 and S-5: re-pointed to the 091426.1 contract.
```
old: Load [GCFPE current direct-handoff contract](references/gcfpe-current-direct-handoff-contract.json) as the current specialization overlay.
new: Load [GCFPE current direct-handoff contract](references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json) as the current specialization overlay.
```

**`:561` — historical provenance.** The historical map is named here, as plain text, not as a link
(§12 §8b O11 (a); OQ-7 (a)); wording U-8b-4.
```
old: The older integrated-readiness, final-scan,
new: The historical 46-row runtime map `glow-hde-canonical-change-flow-r1-runtime-map.json` (SHA-256 `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`) remains immutable historical provenance, checked by its historical pins. The older integrated-readiness, final-scan,
```

**`:563` — the shared `contract_id`.** S-5 and §12 §8b O13 (a): the alias joins the superseded list, and
the current overlay is named by its own `contract_id`. Wording U-8b-5. No validator reads `:563`.
```
old: The bundled `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records
new: The bundled `gcfpe-current-direct-handoff-contract.json` alias (091326.2), `gcfpe-20260913.1-091326.2`, `gcfpe-20260913.1`, and `gcfpe-20260912.2` direct-handoff contracts are superseded candidate records
```
```
old: Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1` with the current contract above; that identifier resolves for current execution to `gcfpe-current-direct-handoff-contract.json` alone, which carries `status: SELECTED_PRODUCTION`.
new: Three of these files share `contract_id` `GCFPE-PF10-INTEGRITY-20260913.1`; that identifier no longer names the current overlay. The current overlay is the 091426.1 contract above, `contract_id` `GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED`, which carries `status: SELECTED_PRODUCTION`.
```
Measured: exactly three bundled files carry `GCFPE-PF10-INTEGRITY-20260913.1` (the alias,
`…-091326.2-…` and `gcfpe-20260913.1-…`), so "Three of these files" is exact once the alias is listed.
The alias file's bytes are unchanged (S-5).

**`:565`** KEEP (historical narrative; no source requires a note for 3.3.0).

**Lines that mention a session and stay verbatim (S-4; §E records each):** `:197` (core); `:263` ("a
dedicated PR session" as an actor the manager never substitutes for); `:305` "same-session PR-35
re-entry"; `:327`, `:383`, `:406`; `:451` (above).

### 8b.3 `change-flow/scripts/validate_gcfpe_20260914.py`

**Skill-clause literals, `:1020`–`:1031`.**
| line | literal | disposition | regression |
|---|---|---|---|
| `:1021` | "PR-30 and PR-35 are two phases" | KEEP (fv-main:26, fv-rest:17) | clean control |
| `:1022` | `{TEN}` → `{NINE}` | REPLACE; old in retired loop | R-CF-NINE, R-CF-RP-2 |
| `:1023` | "one dedicated PR-development session" → "run in two dedicated sessions" | REPLACE; old in retired loop | R-CF-RP-1 |
| new | "never as a subagent, forked agent or workflow agent of PR-30" | NEW (A1-8; W-1) | R-CF-A18 |
| new | "no session is created by an agent" | NEW (C-DISPATCH; §12 §8b O16 (b)) | R-CF-DISP |
| new | "One Proceed per approved per-PR plan" | NEW (C-PROCEED; §12 §8b O16 (b)) | R-CF-PROC |
| new | "It carries no branch and no commit" | NEW (C-HANDOFF; §12 §8b O16 (b)) | R-CF-HND |
| `:1024` | "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block" | KEEP (fv-rest:25) | clean control |
| `:1025`–`:1029` | `PR_RETURN_PHASE`, `PF10_BUILD_NOTES_ADDENDUM`, `SOURCE_RESOLUTION_ERROR`, the PR-50 sentence, `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` | KEEP | clean control |

The new block, in place of `:1020`–`:1031`:
```
    for text in (
        "PR-30 and PR-35 are two phases",
        "{NINE}",
        "run in two dedicated sessions",
        "never as a subagent, forked agent or workflow agent of PR-30",
        "no session is created by an agent",
        "One Proceed per approved per-PR plan",
        "It carries no branch and no commit",
        "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block",
        "PR_RETURN_PHASE",
        "PF10_BUILD_NOTES_ADDENDUM",
        "SOURCE_RESOLUTION_ERROR",
        "Only Nathan / Product Owner may manually invoke selected `PR-50",
        "ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR",
    ):
        require(text in skill, f"missing skill clause: {text}")
```

**The retired-phrase loop** (new, directly after the block). A1-6: "a check that fails if a retired
phrase comes back"; `CONTRACT_FORBIDDEN` never applies to `change-flow` (sweep:12). Each entry is the old
text of one 8b.2 edit that states a reversed rule; the fourteenth is `:450`'s old imperative (W-9).
Matching is case-insensitive (§12 §8b O15 (b)). Measured: none of the 14 occurs in the edited file,
case-insensitively.
```
    for text in (
        "one dedicated PR-development session",
        "{TEN}",
        "same-session PR-30 → PR-35 phase continuation",
        "same-session PR-35 handoff",
        "same-session PR-35 review/readiness",
        "same-session second phase",
        "{V5}",
        "historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged",
        "A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred",
        "One dedicated session per planned PR work unit; the same session performs both",
        "has only the manual-merge-assertion meaning",
        "The same dedicated PR session implements only that work unit",
        "Only after Nathan later asserts that the identified PR was manually merged may that invocation run",
        "GCF-14 — Create one dedicated PR session for one planned PR work unit",
    ):
        require(text.lower() not in skill.lower(), f"retired skill clause present: {text}")
```

**Revision literal.** `:746` REPLACE `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0` (R-CF-REV).

**Contract-side literals** (move with §6's regenerated contract, in §5's pin order):
- `:1007`–`:1010` `pr35_result_vocabulary`: REPLACE with
  `["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]`
  (sweep:3, adversary:9). Regression: §6 R9 (`FAIL PR-35 results`).
- `:751`: `contract_revision == "4.1.0"` (A1-2). Regression: §6 R1.
- `:806`: `len(graph["edges"]) == 229` (A1-7).
- `:76`–`:77`: `EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"`,
  `EXPECTED_ROUTING_SURFACE_ROWS = 284` (A1-7; final, since it reads only edges and state routes).
- `:21` `EXPECTED_GRAPH_SHA`: the final bundled-graph digest, in §5's pin order.
- **KEEP:** `:26` `EXPECTED_CORE_SHA` (A1-6); `:208` `EXPECTED_CONTRACT_TOP_LEVEL_KEYS`, because
  `observed_merge_edges` is recorded inside `post_merge_three_event_contract` (V-2), not as a top-level
  key; `:944` (`ordinary_pr_work_unit[2]` stays `NATHAN_PROCEED`); `:993`–`:1000`; `:1015`–`:1016`.

### 8b.4 `session-relay-flowmaster/SKILL.md`

**`:8` — revision.** 3.0.0 → 3.1.0. Pin: `validate_flowmaster.py:182`. R-REV-R.
```
old: `SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0`
new: `SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0`
```

**`:255` — provisioning, the W-9 sentence, and the override.** W-9 (§12 §8b O2 (b); verifier
contradiction 0): `:255` is scoped out of GCFPE main-ecosystem stages (scoping words: U-8b-1), the W-9
sentence follows it, and the override paragraph follows (§12 §8b O1 (a)).
```
old: When a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement.\n\n### Cross-skill contracts and shared state
new: Outside a GCFPE main-ecosystem stage, when a required participant does not exist or cannot be confirmed reachable, return `SESSION_PROVISIONING_REQUIRED` for Session Branch Flowmaster. Do not silently create a replacement. {W9}\n\n{OVERRIDE}\n\n### Cross-skill contracts and shared state
```

**`:259` — the prompt-locator rule.** Step 14. "/handoff" leaves the line's scope, and step 14's sentence
is appended (§12 §8b O17 (b)). `tw:304` takes the new line byte for byte (8b.5).
```
old: For every GCFPE reusable prompt and temporary repair/review/handoff prompt,
new: For every GCFPE reusable prompt and temporary repair/review prompt,
```
```
old: This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text.\n
new: This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text. Runtime handoffs may name versioned files; reusable prompt text stays versionless.\n
```

**`:266`** KEEP (S-4; §E records the reason): "Session Branch Flowmaster owns provisioning and provides a
stable `SessionEndpoint`" states ownership; the routes that send work there (`:255`, `:713`) are
scoped out of GCFPE main-ecosystem stages.

**`:268` — control plane.** Step 2. Bullet marker and final period stay. "preferred live control plane"
FORBID (8b.8; R-FB-R2). `:269` is out of scope (§P step 2).
```
old: - Notion is the preferred live control plane for current task, assignment, dependency, decision, and handoff state.
new: - {STEP2}.
```

**`:273` — HDE handoff content.** C-ART/C-HANDOFF; the same edit as `change-flow:277` (§12 §8b O18 (b)).
```
old: cleanup/recovery owner in the existing handoff.
new: cleanup/recovery owner in the output artifact that the handoff names.
```

**`:279` — handoff delivery.** Steps 14 and 19 (pr-relay-graph:18). The field list becomes C-HANDOFF,
then C-PLACE (§12 §8b O19). The versionless-invocation sentence contradicts C-HANDOFF and goes. "A
block only in a referenced artifact is insufficient." stays. `tw:315` takes the new line whole.
```
old: Deliver every concrete routed handoff in the final user-facing response itself: target actor and session continuity, exact task-bound advice or limitation, named file references the recipient can resolve itself, and a populated copyable invocation with the selected prompt's native inputs and actual prerequisites. For a Notion prompt use its versionless name and verified directory; approved runtime versions remain input lineage.
new: Deliver every concrete routed handoff in the final user-facing response itself. {C-HANDOFF} {C-PLACE}
```

**`:283` — the PR-lane paragraph.** Step 35 (C-SESSION), step 40 (C-DISPATCH), N4, sweep:5.
- C-SESSION is prepended (§12 §8b O20 (a)); NEW `CONTRACT_REQUIRED` literal `{A18}` (§12 §8b O16 (b));
  R-TOP-R.
- "PR-35 supplies the actual populated PR-40 handoff conditional on merge." becomes `{C-DISPATCH}`.
- "supplies merge approval" is reworded to "is not a merge approval or merge instruction", using
  `change-flow:353`'s words (§12 §8b O20 (b)). The old phrase is FORBIDDEN in both skills (R-FB-R4,
  R-FB-T4).
- KEEP: "…returns MERGE_PENDING with readiness for the Product Owner's manual merge, and returns control
  without polling for that action."; "Pending engineering remains with the same PR owner."; "PR-40
  stays read-only …"; "A prior MERGE_PENDING result …"; "Preserve this boundary … handoff."
- `tw:319` takes the new line byte for byte.
```
old: PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete same-session PR-35 handoff,
new: {C-SESSION} PR-30 finishes recovery, implementation, local testing and deliberate initial publication, returns PR_CANDIDATE_PUBLISHED with exactly one complete PR-35 handoff to the dedicated PR-35 session,
```
```
old: PR-35 supplies the actual populated PR-40 handoff conditional on merge.
new: {C-DISPATCH}
```
```
old: The Product Owner's PR-40 invocation supplies merge approval without a separate confirmation or approval artifact; it never authorizes an agent merge,
new: The Product Owner's PR-40 invocation is not a merge approval or merge instruction; it never authorizes an agent merge,
```

**`:285` — ordered PR units.** "same-session resume" converges on the recorded phase's own session
(§12 §8b O21 (b)); glue U-8b-2. The no-poll and no-early-PR-40 rules stay. `tw:321` takes the new line.
```
old: Return a populated same-session resume of the recorded PR phase after the actual merge,
new: Return a populated resume of the recorded PR phase in the recorded phase's own session after the actual merge,
```

**`:353`, `:372` — `CONTROL_PLANE`.** S-7 (§12 §8b O22): the enum `NOTION | NONE` is kept, and its
meaning is stated. `:353` is a line of the fenced manifest template, so the sentence is placed once, at
`:372`, directly after the sentence that binds `CONTROL_PLANE: NOTION` (placement: U-8b-3). The
`CONTRACT_REQUIRED` literal "Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION`" KEEP.
`scripts/validate_relay_manifest.py` is unchanged; its self-test stays 230 cases.
```
old: Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2.
new: Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE: NOTION` and an exact Notion page URL in `LEDGER_DESTINATION`; version 1 cannot represent that binding and must migrate to version 2. {S7}
```

**`:624` — `NOTION_REFERENCE`.** S-6 (§12 §8b O23). The `CONTRACT_REQUIRED` literal
"REFERENCE_METHOD: REPOSITORY_PATH | WORKTREE_PATH | DRIVE_LINK | NOTION_REFERENCE | INLINE_TEXT" (at
`:362`) KEEP.
```
old: 4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above.
new: 4. `NOTION_REFERENCE`: a versionless resource name plus its verified directory path, resolved by the recipient at execution under the prompt-locator rule above. {S6}
```

**`:713` — provisioning.** W-9: scoped as at `:255` (U-8b-1). The rest of the line stays.
```
old: This specialization cannot create a session. When a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:
new: This specialization cannot create a session. Outside a GCFPE main-ecosystem stage, when a required participant does not exist, return `SESSION_PROVISIONING_REQUIRED` and stop:
```

**`:723`** KEEP (the rule that requires the revision bump).

**Scripts.** `scripts/validate_relay_manifest.py` never reads `SKILL.md` and is unchanged (S-7).

### 8b.5 `tw-flowmaster/SKILL.md`

A1-6: this skill carries byte-identical copies of the relay's retired GCFPE lines. Measured today:
`tw:304` = relay `:259`; `:306` = `:261`; `:317` = `:281`; `:319` = `:283`; `:321` = `:285`; `:323` =
`:287`; `:315` ≠ relay `:279` ("named attachments", "an attached artifact").

- **`:8` — revision.** 1.1.6 → 1.2.0 (sweep:5 cites `:9`; the line is `:8`). R-REV-T.
  ```
  old: `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6`
  new: `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`
  ```
- **Override**, the first paragraph under `### GCFPE binding` (`:300`): 8b.1.
- **`:304` := the relay's new `:259`**, byte for byte (§12 §8b O17 (b); sweep:5).
- **`:311`** (sweep:5; §12 §8b O24 (a)):
  ```
  old: Add result artifact/PR/commit references when observed;
  new: Add result artifact/PR/commit references to the usage record when observed, never to the handoff;
  ```
- **`:315` := the relay's new `:279`**, the whole line (§12 §8b O19). This also changes "an attached
  artifact" to "a referenced artifact".
- **`:319` := the relay's new `:283`**, byte for byte (§12 §8b O20 (a), (b)). NEW `CONTRACT_REQUIRED`
  literal `{A18}`; R-TOP-T.
- **`:321` := the relay's new `:285`**, byte for byte (§12 §8b O21 (b)).
- **`CONTRACT_REQUIRED['tw-flowmaster']`:** existing entries KEEP; the revision entry
  (`validate_flowmaster.py:128`) REPLACE; `{OVERRIDE}` and `{A18}` NEW (8b.8).
- **Kept verbatim, out of scope:** `:281`, `:425`, `:427` instruct the TW flow to create and initialize
  TW Work sessions. The TW ecosystem is not the GCFPE main ecosystem, which the D23 clarification binds
  (and is outside D23-G); §E records it.

### 8b.6 `flowmaster-validate/SKILL.md`

No literal reads these lines; `SKILL_TREE_SHA256` reads them and moves last.

**`:8`, `:9` — identity.** `FLOWMASTER_VALIDATE_REVISION: 3.2.16` → `3.3.0`. `SKILL_TREE_SHA256` is
recomputed with `skill_tree_digest` over the final tree and written last (fv-main:23, fv-rest:9,
pr-relay-graph:32; §5 order).
```
old: FLOWMASTER_VALIDATE_REVISION: 3.2.16
new: FLOWMASTER_VALIDATE_REVISION: 3.3.0
```

**`:60` and `:231`–`:232` — C-D22.** Step 45 (fv-main:34). W-7: each site's reason clause is replaced by
C-D22's reason, verbatim (§12 §8b O26).
```
old: deliberately with no path option, because a file persists --
new: deliberately with no path option, because {C-D22} --
```
```
old: There is no path option and there will not be one: a file persists, and\na persisted corpus is what the policy forbids.
new: There is no path option and there will not be one: {C-D22}.
```

**`:145`, `:147`, `:149`, `:244`–`:249`** are §5's: the successor profile id, matrix, digest and
filename, and the "It pins:" list naming the successor matrix and digest and the kept historical oracle
digest (§12 *Successor oracle*, OQ-13 (a)). `:255`–`:257` KEEP.

**`:155` — contract revision** (A1-2):
```
old: The 20260914 candidate contract revision 4.0.6 binds
new: The 20260914 candidate contract revision 4.1.0 binds
```

**`:157` — the selected-alias description.** Follows S-5 (§12 §8b O12 (a)); wording U-8b-5.
```
old: The selected alias `references/gcfpe-current-direct-handoff-contract.json` must match that live binding.
new: The current overlay `references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json` must match that live binding; the `gcfpe-current-direct-handoff-contract.json` alias is historical provenance and no longer a validation default.
```

**`:164`–`:166` — the PR contract restatement.** fv-main:34, coverage:15, sweep:3, fv-rest:15.
```
old: - PR-30 and PR-35 are two phases of one GCF-17 PR work unit. {TEN}. Both phases share exactly one value for every field. PR-35 adds zero roles, sessions, approvals, gates, Proceeds, work units, R1 rows, merge authority, work vehicles, or cross-session routes.
new: - {C-SESSION} {NINE}. Both phases share exactly one value for every field. PR-35 adds zero roles, approvals, gates, Proceeds, work units, R1 rows, merge authority, or work vehicles.
```
```
old: coherent commits, deliberate initial publication, and its same-session PR-35 handoff.
new: coherent commits, deliberate initial publication, and its PR-35 handoff.
```
```
old: The exact PR-35 results are `MERGE_PENDING`, `RESCOPE_PENDING`,
new: The exact PR-35 results are `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,
```

**`:173` — merge boundary** (fv-main:34, coverage:15), as at `change-flow:331`:
```
old: PR-35 `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only.
new: PR-35 `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}
```

**`:176`, `:381`, `:383` — the fixture count** 33 → 37 (§12 §8b O29 (a); fv-rest:16):
```
old: The versioned 33-case section-13 fixture suite
new: The versioned 37-case section-13 fixture suite
```
```
old: and all 33 section-13 fixtures.
new: and all 37 section-13 fixtures.
```
```
old: The fixture report separates 33 required fixture IDs,
new: The fixture report separates 37 required fixture IDs,
```

**`:381` — the selected-alias description.** Follows S-5 (§12 §8b O12 (a)); wording U-8b-5.
```
old: During candidate staging, the suite validates the selected 54-member `GCFPE-20260913.1 / 091326.2` alias and its predecessor fixtures first.
new: By default the suite validates the 091426.1 current overlay and its schema-4 fixtures; the 54-member `GCFPE-20260913.1 / 091326.2` alias is validated only when passed explicitly.
```

**`:178`** KEEP (amendment, *Noticed, not in scope*).

**`:184` — TW revision** (the only prose pin of it):
```
old: the TW specialization revision is 1.1.6 (including
new: the TW specialization revision is 1.2.0 (including
```

**`:294` — Change check 12.** coverage:15; C-SESSION's second and third sentences (§12 §8b O25 (a)).
```
old: 12. One dedicated PR session plans and implements one work unit.
new: 12. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request.
```

**`:393` — rescope receiver compatibility.** sweep:20, verbatim:
```
old: resumes the recorded phase in the same session/worktree/branch/open PR under the original Proceed.
new: resumes the recorded phase in that phase's own session, worktree, branch and open PR under the original Proceed.
```

### 8b.7 `flowmaster-validate/scripts/validate_gcfpe_20260914.py` — the reversals

Error-code names are those simulated in v1 (§12 §8b O30 (a)); the three codes v1 had no name for are
compiled here and listed in U-8b-8. Each rule names its regressions (8b.10). New module constants go
directly before `EXPECTED_MERGE_PENDING_REQUIREMENTS` (`:881`).

**1. Header check → `PROMPT_BODY_RELEASE_HEADER`** (D23-G, step 42, fv-main:0, fv-rest:22; S-1: steps
41–43 run now).
- `prompt_identity_header_valid` (`:1046`–`:1078`) keeps the exact title, the `Prompt ID:` line and one
  neutral `Notion URL:` line in `nonblank[:12]`; it drops the `Prompt [Vv]ersion` and `Ecosystem
  release` requirements. The floor `len(nonblank) >= 7` becomes `>= 4` (§12 §8b O28 (a); §1 OQ-3).
- `:910` `PROMPT_VERSION_HEADER_RE` is REPLACED by the key tuple (nothing else imports it; measured).
- `validate_prompt_bodies` (`:2333`–`:2335`) emits `PROMPT_BODY_RELEASE_HEADER:<id>`.
- The `:904`–`:908` comment is rewritten to cite D23-G (text: U-8b-9).
```
RELEASE_HEADER_KEYS = ("Prompt Version:", "Prompt version:", "Set:", "Ecosystem release:")
```
```
    return bool(
        len(nonblank) >= 4
        and nonblank[0] == member.get("title")
        and any(line in header_value_lines("Prompt ID:", prompt_id) for line in nonblank[:8])
        and url_line_ok
    )


def prompt_body_release_header(nonblank: list[str]) -> bool:
    """True when the header window carries a release-bound line, which D23-G prohibits."""

    stripped = [governance_line_normalised(line) for line in nonblank[:8]]
    return any(line.startswith(key) for line in stripped for key in RELEASE_HEADER_KEYS)
```
```
        if prompt_body_release_header(nonblank):
            errors.append(f"PROMPT_BODY_RELEASE_HEADER:{prompt_id}")
```
An old seven-line header gives exactly `PROMPT_BODY_RELEASE_HEADER`, not also `PROMPT_BODY_IDENTITY`.
R-HDR-1…3.

**2. `PR35_ADDED_BOUNDARY` → exact map** (`:1742`–`:1743`). V-1: `session` 1 and `cross_session_route`
1, every other key 0 (fv-main:2 superseded in that part only). R-AB-1…3.
```
EXPECTED_PR35_ADDED_BOUNDARIES = {
    "approval": 0, "cross_session_route": 1, "duplicate_work_vehicle": 0, "merge_authority": 0,
    "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0,
    "work_vehicle": 0,
}
    if not isinstance(development, dict) or development.get("added_boundaries") != EXPECTED_PR35_ADDED_BOUNDARIES:
        errors.append("PR35_ADDED_BOUNDARY")
```

**3. `PR_PHASE_CONTINUITY`** (`:876`–`:880`, `:1744`–`:1745`; fv-main:3). Nine fields in order; exact
comparison KEEP; explicit absence test. R-PC.
```
EXPECTED_PHASE_CONTINUITY = [
    "WORK_UNIT_ID", "original Product Owner Proceed",
    "workspace/worktree", "branch", "pull request", "PR instruction", "detailed PR plan",
    "primary skill authority", "continuous recovery/artifact lineage",
]
    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY or "dedicated PR-development session" in development.get("shared_exactly_one", []):
        errors.append("PR_PHASE_CONTINUITY")
```

**4. `EXPECTED_PR35_RESULTS`** (`:853`–`:856`; used at `:1747` and `:1921`). R-V-1, R-V-2.
```
EXPECTED_PR35_RESULTS = [
    "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING",
    "PRODUCT_OWNER_DECISION_REQUIRED",
]
```

**5. `DIRECT_PR35_PR40_EDGE` and `GRAPH_DIRECT_PR40_EDGE` → one exact positive rule** (`:1837`–`:1838`,
`:1349`–`:1355`; fv-main:11, pr-relay-graph:22, fv-rest:20, coverage:19, adversary:9, sweep:0, A1-5,
A1-7, §4 E4–E5). Exactly PR-35 and RS-40, each with exactly one prompt edge to PR-40: `automatic:
false`, transport `COMPLETE_NEXT_PROMPT_HANDOFF`, sole state `MERGE_OBSERVED`, one `merge_observed`
branch whose condition equals A1-7's string exactly (§12 §8b O31 (a)).
- **The narrowing, stated as AF-001 requires.** `GRAPH_DIRECT_PR40_EDGE`'s prohibition set shrinks from
  `{"PR-30", "PR-35"}` to `{"PR-30"}`. PR-35 and RS-40 may route to PR-40 only on this exact edge.
- **Kept:** `DIRECT_PR30_PR40_EDGE` (`:1835`–`:1836`) and its fixture; "no agent merges"
  (`agent_merge_authorized`, `POST_MERGE_CONTRACT`); "no entry before Nathan merges" (R-DE-5).
```
OBSERVED_MERGE_EDGE_CONDITIONS = {
    "PR-35": "the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
    "RS-40": "resumed PR-35 phase; the subscribed PR-35 session observes the merge of the identified PR, performed by Nathan",
}


def observed_merge_edge_errors(edges) -> bool:
    """True unless PR-35 and RS-40 each have exactly one lawful MERGE_OBSERVED edge to PR-40."""

    found = [e for e in edges if isinstance(e, dict) and e.get("to") == "PR-40" and e.get("from") in OBSERVED_MERGE_EDGE_CONDITIONS]
    if sorted(e.get("from") for e in found) != ["PR-35", "RS-40"]:
        return True
    for e in found:
        branches = e.get("route_branches")
        if (
            e.get("from_kind") != "prompt" or e.get("to_kind") != "prompt" or e.get("automatic") is not False
            or e.get("transport") != "COMPLETE_NEXT_PROMPT_HANDOFF" or e.get("state_predicates") != ["MERGE_OBSERVED"]
            or not isinstance(branches, list) or len(branches) != 1 or not isinstance(branches[0], dict)
            or branches[0].get("branch_id") != "merge_observed" or branches[0].get("state") != "MERGE_OBSERVED"
            or branches[0].get("applicable_states") != ["MERGE_OBSERVED"]
            or branches[0].get("condition") != OBSERVED_MERGE_EDGE_CONDITIONS[e["from"]]
        ):
            return True
    return False
```
In `validate_contract`, in place of `:1837`–`:1838` (rule 9 follows it):
```
        if observed_merge_edge_errors(edges):
            errors.append("DIRECT_PR35_PR40_EDGE")
```
In `validate_graph_contract`, in place of `:1349`–`:1355`:
```
    if any(
        isinstance(edge, dict)
        and edge.get("from") in {"PR-30"}
        and edge.get("to") == "PR-40"
        for edge in edges
    ) or observed_merge_edge_errors(edges):
        errors.append("GRAPH_DIRECT_PR40_EDGE")
```
R-DE-1…8.

**6. `PR40_MANUAL_MERGE_BOUNDARY`** (`:1925`–`:1948`; fv-main:12). The boundary half and the DOC-20 half
KEEP; the two observed-merge edges leave the recovery list, so one defect fires one code. R-MB-1…4.
```
    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt" and edge.get("from") not in OBSERVED_MERGE_EDGE_CONDITIONS]
```

**7. `POST_MERGE_CONTRACT` and `POST_MERGE_THREE_EVENTS`** (`:1768`–`:1780`). V-2, V-3, and the literal
checks §12 §8b O33 (b) adds.
- `direct_PR35_to_PR40_automatic_edge: False` KEEP (A1-5; the D23 successor note).
  `agent_merge_authorized: False` KEEP. `event_1`, `event_3` KEEP.
- NEW: `observed_merge_edges` equals V-2's two summary objects exactly, checked inside
  `POST_MERGE_CONTRACT`. R-PM-5, R-PM-6.
- REPLACE: `event_2` equals V-3's object exactly (`actor`, `fact`, `time`, `value`), checked inside
  `POST_MERGE_THREE_EVENTS`. R-PM-2, R-PM-4.
```
EXPECTED_OBSERVED_MERGE_EDGES = [
    {"from": "PR-35", "to": "PR-40", "branch_id": "merge_observed", "state": "MERGE_OBSERVED", "automatic": False, "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"},
    {"from": "RS-40", "to": "PR-40", "branch_id": "merge_observed", "state": "MERGE_OBSERVED", "automatic": False, "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"},
]
EXPECTED_EVENT_2 = {
    "actor": "Nathan / Product Owner",
    "fact": "product_owner_manual_merge_observed_or_asserted",
    "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge",
    "value": True,
}
    errors += subset_errors(postmerge, {
        "agent_merge_authorized": False, "direct_PR35_to_PR40_automatic_edge": False,
        "observed_merge_edges": EXPECTED_OBSERVED_MERGE_EDGES,
    }, "POST_MERGE_CONTRACT")
    if not isinstance(postmerge, dict) or (
        (postmerge.get("event_1") or {}).get("value") != "MERGE_PENDING"
        or (postmerge.get("event_1") or {}).get("time") != "pre_merge_historical_evidence"
        or postmerge.get("event_2") != EXPECTED_EVENT_2
        or (postmerge.get("event_3") or {}).get("consumer") != "PR-40"
        or (postmerge.get("event_3") or {}).get("independent") is not True
    ):
        errors.append("POST_MERGE_THREE_EVENTS")
```
The graph carries the same record (mirrored); `GRAPH_POST_MERGE_CONTRACT_MISMATCH` (`:1256`) KEEP.

**8. `ROUTE_GRAPH_SHORTHAND`** (`:1782`–`:1798`). Exact equality KEEP. The literal equals §6's
`route_graph` with V-4's key: the three entries that change or are added are
```
        "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],
        "pr35_merge_pending_fallback": ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],
        "pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],
```
All other entries KEEP. R-RG-1…3.

**8a. `ROUTE_GRAPH_SEMANTICS`** (NEW, directly after rule 8). W-8: each changed contract-only value gets
an exact-value check (§6 Q6.18 (a)). The whole `route_graph_semantics` map must equal W-8's After value:
`same_session_phase_continuation` renamed `pr30_to_pr35_phase_continuation` with W-8's text,
`pr40_entry` = W-4's sentence, new `pr40_reject_replan`, and the four untouched keys byte-for-byte as
today. R-SEM-1…3.
```
EXPECTED_ROUTE_GRAPH_SEMANTICS = {
    "pr30_to_pr35_phase_continuation": "PR-30 to PR-35 is one lawful phase continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting PR-30's handoff; not a new work unit, and never a subagent.",
    "pr35_merge_pending": "Historical pre-merge evidence only; it does not assert that a merge occurred.",
    "pr40_entry": "PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.",
    "pr40_reject_replan": "A PR-40 REJECT for an in-scope defect in landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new Proceed for the new plan (D23-F).",
    "pr50": "Only the manual Product Owner boundary edge may invoke; no prompt, agent, skill, hub, automation, or automatic edge may route to PR-50.",
    "qa_pass_closure": "Verified EPIC PASS routes directly to CL-E-10; verified CRD PASS routes directly to CL-C-10. Both carry separate QA Report/RCA and the complete matching intake to continuing Isis. Unresolved class or receiver evidence returns terminally to Nathan with no handoff; QA never decides closure.",
    "rs40": "Internal same-open-PR continuation only after for PR-30_POSTPUBLICATION or PR-35.",
}
    if contract.get("route_graph_semantics") != EXPECTED_ROUTE_GRAPH_SEMANTICS:
        errors.append("ROUTE_GRAPH_SEMANTICS")
```
(`rs40`'s "only after for" is today's text, kept byte for byte.)

**8b. `PR35_TOP_LEVEL_ROLE`** (NEW, directly after 8a). W-1: the check on
`member_registry['PR-35'].receiving_role` that shares the registry's guard phrase (verifier unplaced 2).
R-ROLE.
```
PR35_TOP_LEVEL_ROLE_PHRASE = "never as a subagent, forked agent or workflow agent of PR-30"
    if PR35_TOP_LEVEL_ROLE_PHRASE not in str(((contract.get("member_registry") or {}).get("PR-35") or {}).get("receiving_role", "")):
        errors.append("PR35_TOP_LEVEL_ROLE")
```
The graph side is guarded by the existing `GRAPH_NODE_CONTRACT:PR-35` parity, which fires when the
graph and contract roles differ.

**9. The PR-40 re-plan route** (NEW, after rule 5 in `validate_contract`; child C8, fv-main:30).
`rescope_contract.new_proceed_required: False` KEEP (C8). R-RP-1, R-RP-2.
```
        replan = [e for e in edges if isinstance(e, dict) and e.get("from") == "PR-40" and any(isinstance(b, dict) and b.get("branch_id") in {"reject_replan", "reject_existing_pr_owner"} for b in e.get("route_branches", []))]
        if len(replan) != 1 or replan[0].get("to") != "PR-20" or any(isinstance(e, dict) and e.get("from") == "PR-40" and e.get("to") == "PR-30" for e in edges):
            errors.append("PR40_REJECT_REPLAN_ROUTE")
```

**10. `RECEIVER_CONTRACT:<id>`** (NEW, at the end of `validate_contract`). A1-6's `receiver_compatibility`
content check (adversary:10, fv-main:32, coverage:13, child C9, sweep:21). V-5: exact content of **all
seven** receivers; the code follows the v3 precedent (`validate_gcfpe_current.py:446`–`:448`). Its
negative control (C9): no entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` `REJECT` (R-RC-3,
R-RC-5). PR-30, RS-20, RS-30 and RS-40 are today's values; PR-20 is V-5's; PR-35 is sweep:10's; PR-40
takes V-4's `entry_fact` and loses `nathan_manual_merge_assertion_required`. R-RC-1…6.
```
EXPECTED_RECEIVERS = {
    "PR-20": {"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"], "earlier_cycle_pr_is_landed_history": True, "existing_work_unit_replan": True, "new_proceed_for_new_plan": True, "new_top_level_session_created_by_nathan": True},
    "PR-30": {"accepted_contexts": ["PROCEEDED_PREPUBLICATION", "OPEN_PR_POSTPUBLICATION_RECOVERY"], "accepted_final_replay": False, "delta_in_force_from_turn_after_addendum_created": True, "overlay_approvals": ["RS-20:APPROVE", "ESC-40:APPROVE", "IA-30:QUALIFYING_DELTA_APPROVE"]},
    "PR-35": {"context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION", "dedicated_top_level_pr35_session": True, "same_workspace_worktree_branch_open_pr_original_proceed": True},
    "PR-40": {"attribution_skill_read_only": True, "entry_fact": "MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED", "independent_actual_merged_state_and_landed_lineage_verification": True, "prior_merge_pending_is_historical_premerge_evidence": True},
    "RS-20": {"accepted_inputs": ["RESCOPE_REQUEST", "RESCOPE_PROPOSAL"], "bounded_implementation_delta_only": True, "decision_owner": "SAME_WHOLE_CHANGE_IA"},
    "RS-30": {"invented_ia_denial": False, "same_artifact_type_author_and_decision_owner": True},
    "RS-40": {"accepted_approval": "RS-20:RESCOPE_REVIEW:APPROVE", "contexts": ["PR-30_POSTPUBLICATION", "PR-35"], "delta_in_force_from_turn_after_addendum_created": True, "original_proceed": True, "requires_existing_open_pr": True},
}
    receivers = contract.get("receiver_compatibility")
    for receiver in sorted(set(EXPECTED_RECEIVERS) | set(receivers if isinstance(receivers, dict) else {})):
        if not isinstance(receivers, dict) or receivers.get(receiver) != EXPECTED_RECEIVERS.get(receiver):
            errors.append(f"RECEIVER_CONTRACT:{receiver}")
```

**11. `HANDOFF_CONTRACT` → exact keys and values; `HANDOFF_PROHIBITED_REFERENCES`; the subset check**
(`:1481`–`:1500`). A1-2, V-6 (verifier conflicts 4 and 17), fv-main:17, fv-rest:13, adversary:3,
coverage:12.
- `HANDOFF_CONTRACT`: `set(transition_contract) == set(After)`, and every value except
  `prohibited_references` equals After (V-6). After = today's keys minus the four V-6 deletes plus V-6's
  five `true` flags. `actual_pasteable_complete_prompt: True` KEEP (fixture
  `reject-incomplete-handoff`). R-HC-1, R-HC-2, R-HC-4, R-HC-5.
- `HANDOFF_PROHIBITED_REFERENCES` checks its own value: today's five plus V-6's seven, as a set
  (today's comparison form). R-HC-3, R-HC-7.
- NEW `GRAPH_HANDOFF_PROHIBITED_REFERENCES` in `validate_graph_contract`, after
  `GRAPH_HANDOFF_CONTRACT_MISMATCH` (`:1269`): graph `handoff_contract.prohibited` ⊆ contract
  `prohibited_references` (V-6; §12 §8b O32). R-HC-6, R-HC-7.
```
EXPECTED_TRANSITION_CONTRACT = {
    "actual_branch_only": True, "actual_pasteable_complete_prompt": True,
    "artifact_repository_paths_with_labels": True,
    "blank_form_menu_or_reconstruction_prohibited": True, "block": "NEXT_PROMPT_HANDOFF",
    "exact_destination_full_name_version_direct_notion_url": True,
    "exactly_one_per_nonterminal_result": True, "exceptional_context_only": True,
    "fence_language": "text", "first_line": "NEXT_PROMPT_HANDOFF",
    "metadata_only_or_routing_summary_prohibited": True, "no_branch_or_commit": True,
    "no_restated_artifact_content": True, "pr_reference_when_continuing": True,
    "receiving_role_and_exact_session": True, "terminal_has_no_handoff": True,
    "transport": "DIRECT_NATIVE_PROMPT_HANDOFF",
}
    if (
        not isinstance(transition, dict)
        or set(transition) != set(EXPECTED_TRANSITION_CONTRACT) | {"prohibited_references"}
        or any(transition.get(key) != value for key, value in EXPECTED_TRANSITION_CONTRACT.items())
    ):
        errors.append("HANDOFF_CONTRACT")
    prohibited_refs = set(transition.get("prohibited_references", [])) if isinstance(transition, dict) else set()
    if prohibited_refs != {
        "Library ID", "unlinked filename", "above", "conversation reconstruction",
        "model/strength/reasoning/eligibility/suitability/account/configuration route",
        "branch", "commit", "restated artifact content",
        "menu", "metadata-only summary", "blank form", "placeholder after publication",
    }:
        errors.append("HANDOFF_PROHIBITED_REFERENCES")
```
```
    if not isinstance(graph_handoff, dict) or not isinstance(transition, dict) or not set(graph_handoff.get("prohibited", [])) <= set(transition.get("prohibited_references", [])):
        errors.append("GRAPH_HANDOFF_PROHIBITED_REFERENCES")
```

**11a. W-8's other exact values, inside existing codes.**
- `PR_DEVELOPMENT_CONTRACT` subset (`:1720`–`:1741`) gains
  `"pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation", "deliberate initial publication", "complete PR-35 handoff to the dedicated PR-35 session"]`.
  R-OWN.
- `RESCOPE_CONTRACT` subset (`:1700`–`:1712`) gains §6's `preserved_lineage` (index 1
  `PR_PHASE_SESSION`; sweep:10). R-LIN.

**12. R1 identity claims** (`:1951`–`:1957`, `:1960`–`:1967`, `:1375`–`:1382`, `:1127`–`:1133`). V-7.
- `:1966` `r1_oracle_changed` → `True`. `:1956` `protected_r1_46_rows_unchanged` → `False` (§5's N9 is
  the replacement guard for the 43 unchanged rows).
- `:1964`, `:1379`, `:1130` `r1_oracle_sha256` and `:1131`, `:2611` `r1_runtime_map_sha256` and path: §5's
  successor values, in §5's pin order; §5's check ties these R1 literals to the successor oracle file's
  digest (§12 *Successor oracle*, OQ-10).
- KEEP: `r1_rows` 46, `r1_core_rows` 26, `r1_material_rows` 20; `pr35_adds_r1_row: False`;
  `flowmaster_primary_core_changed: False` and `4d8bb9bf…`; `pr35_same_r1_row_as_pr30: True` (`:1953`)
  and `PR-35_same_r1_row_as_PR-30` (`:1367`).

R-R1-1…3.

**13. Kept deliberately.** `PRESERVATION_CONTRACT` `versioned_sibling_successors: True` (`:1972`; A1-2,
A1-3; supersedes fv-main:31). `EXPECTED_CONTRACT_TOP_LEVEL_KEYS` (`:339`–`:398`) unchanged (V-2 adds no
top-level key).

**14. Other literals.**
- `:1390` `contract_revision` → `"4.1.0"` (A1-2; fv-main:35). R-ID.
- `:207`–`:208` → `fecc319bdd4ce7ee6201cb77d7231861` / `284` (A1-7). Every route-edge regression also
  shows `ROUTING_SURFACE_CHANGED`.
- `:1722` `primary_skill_revision` → `"1.3.0"` (§8a.5). R-PS.
- `:1090` `validator_revision` → `"3.3.0"` (§12 §8b O27 (a)).
- `:1118` `edge_count` → `229`; `:1123` `count` → `37` (§12 §8b O29 (a)).
- `:941`–`:945` byte pins (graph sha and bytes, contract sha and bytes, fixture sha): §5's order.
- `:2441`–`:2450` `exact_markers` (sweep:2, fv-rest:21, fv-main:33). PR-40's three markers KEEP (child
  C4). R-MK.
  ```
        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING", "MERGE_OBSERVED"),
        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES, "MERGE_OBSERVED"),
  ```
- `:2580`–`:2586` `CHANGE_FLOW_CONTRACT`: all markers KEEP; the revision marker reads profile
  `installed_skill_revisions['change-flow']`, which becomes `3.3.0`.
- `:2590`–`:2597` `SKILL_CONTRACT`: `:2592` → `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0`, `:2594` →
  `{NINE}` (REPLACE; fv-main:24); `:2593`, `:2595`, `:2596` KEEP (fv-main:25).
- `:2607`–`:2609` `PRIMARY_FILE_IDENTITY` `0665507…` KEEP.
- **Comments** (W-7; §12 §8b O26): the `:2657`–`:2658` comment's reason clause becomes C-D22's reason:
  ```
  old:     # option: a file would persist, and a persisted corpus is what the policy forbids.  Supply
  new:     # option: {C-D22}.  Supply
  ```
  The docstring at `:2287`–`:2291` states the policy but has no reason clause, so W-7 leaves it
  unchanged (U-8b-9).

### 8b.8 `validate_flowmaster.py`, `validate_gcfpe_current.py`, `run_gcfpe_current_fixtures.py`, the profile

**Revisions** (fv-rest:26, pr-relay-graph:16, sweep:5, adversary:17):
```
flowmaster-validate/scripts/validate_flowmaster.py:128        "TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0",
flowmaster-validate/scripts/validate_flowmaster.py:147        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",
flowmaster-validate/scripts/validate_flowmaster.py:182        "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",
flowmaster-validate/scripts/validate_flowmaster.py:686        "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",   (maintenance_metadata value; its key "…: 2.0.0" is the oracle's token and stays)
flowmaster-validate/scripts/validate_flowmaster.py:1221       "validator_revision": "3.3.0",
flowmaster-validate/scripts/validate_gcfpe_current.py:634-635 "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0" (both occurrences)
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:27   "change-flow": "3.3.0"
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:28   "glow-hde-pr-development": "1.3.0"
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:45   "validator_revision": "3.3.0"
```

**`CONTRACT_REQUIRED`** (A1-6; §12 §8b O3 (a), O16 (b)). Every existing entry KEEP.
- `tw-flowmaster` (after `:128`): NEW `{OVERRIDE}`, NEW `{A18}`.
- `change-flow` (after `:147`): NEW `{OVERRIDE}`. `:148`, the R1 profile id, is §5's.
- `session-relay-flowmaster` (after `:182`): NEW `{OVERRIDE}`, NEW `{A18}`.

**`CONTRACT_FORBIDDEN`** (append-only; no existing entry narrowed). Both skills take the same four
phrases (§12 §8b O4 (b)), appended after `"session_control_timeout_seconds = [["` (`tw-flowmaster`) and
after `"attach the file to the message"` (`session-relay-flowmaster`):
```
        "same-session PR-35 handoff",
        "preferred live control plane",
        "launched as a new session",
        "The Product Owner's PR-40 invocation supplies merge approval",
```
Measured: none occurs, case-insensitively, anywhere in either edited file, core included; none is a
substring of `{OVERRIDE}` or `{INVARIANT}` (§12 *Other settlements*). R-FB-R1…4, R-FB-T1…4.

**`OPTIONAL_REFERENCES['change-flow']`** (`:360`–`:364`). The allowlist equals the links in `SKILL.md`
(sweep:7, adversary:10). S-5: `references/gcfpe-current-direct-handoff-contract.json` is replaced by
`references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`, which `:559` now links. The
runtime-map entry is replaced by the successor path (§5; §12 *Successor oracle*, OQ-7 (a)).

**Default overlay path** (S-5; §12 §8b O12 (a)). Three defaults re-point to the 091426.1 contract; its
schema-4.0 dispatch (`validate_gcfpe_current.py:619`–`:622`, `run_gcfpe_current_fixtures.py:105`–`:109`)
then runs the v4 validator and fixtures in the default suite:
```
flowmaster-validate/scripts/validate_gcfpe_current.py:615        change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
flowmaster-validate/scripts/run_gcfpe_current_fixtures.py:104    change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
flowmaster-validate/scripts/validate_flowmaster.py:818           str(change_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),
```

**The v3 path** (reached only when the historical alias is passed explicitly). S-5 and §12 §8b O14 (a)
(verifier contradiction 7):
```
flowmaster-validate/scripts/validate_gcfpe_current.py:651   "GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0",
flowmaster-validate/scripts/validate_gcfpe_current.py:652   "## Recover before creating work", "run in two dedicated sessions", "RS-40", "PR-50",
```
Measured: the explicit alias run returns `ok: true` on the edited copy.

**Unchanged:**
- `validate_gcfpe_current.py:302` (`1.2.0`, the historical contract's pin; §12 §8a O25);
- `validate_gcfpe_current.py:80`–`:83` (historical; fv-main:21; §5);
- `validate_gcfpe_20260914.py:2557`–`:2575` (only for an `UNSELECTED_CANDIDATE` contract);
- `validate_gcfpe_current.py:602` (`NameError` on `--bodies-stdin`; out of scope, fv-rest:24).

**§5's sites, listed here, not changed by this section:** `validate_flowmaster.py:24`–`:42`, `:148`,
`:355` and `:360`–`:364` (runtime-map entry); `run_change_flow_fixtures.py:15`;
`validate_gcfpe_20260914.py:1130`–`:1131`, `:1379`, `:1964`, `:2610`–`:2612`; the validation profile at
`:35` and `:37`; `validate_gcfpe_current.py:81` and `:659`; the historical-layer pins, never edited:
`validate_strength_middleware.py:14`, `validate_integrated_readiness.py:8`/`:150`,
`validate_pre_guide_correction.py:9`/`:66`, `validate_final_scan.py:68` (sweep:8).

### 8b.9 Fixtures: `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` and `flowmaster-validate/fixtures/gcfpe-20260914.1-091426.1/scenarios.json`

Full paths throughout (verifier conflict 19). The R1 path fixture GCF-17.LINEAGE → GCF-14
(`GCF-LINEAGE-REPLAN-01`) is in `flowmaster-validate/fixtures/change-flow/scenarios.json`, which is §5's.

**Shape** (§12 §8b O29 (a)): four new scenario ids, HANDOFF-POS-03, HANDOFF-NEG-02, REPLAN-POS-01 and
REPLAN-NEG-01, giving 37 ids, 20 positive and 17 negative. The runner's case count is the one measured
at E4 (§12 *Other settlements*, §9); on the measurement candidate it was 228 (8b.12).

**Projection changes (`project_behavior`).**
- **`pr_split`** (fv-main:5, fv-main:6, fv-rest:16): `requests_new_session` leaves the failure test and
  `pr35_in_pr30_session` enters it; the positive requires `new_dedicated_pr35_session` and
  `added_boundaries == EXPECTED_PR35_ADDED_BOUNDARIES` and returns `PR30_TO_PR35_NEW_DEDICATED_SESSION`;
  the extra-Proceed failure KEEP.
- **`handoff`** (fv-main:7, fv-main:28, fv-rest:20, coverage:3, coverage:19, sweep:14, adversary:9):
  PR-30 → PR-35 accepted only with `same_session` false and `session_disposition: NEW_DEDICATED`; any
  PR-40 entry with `automatic_dispatch`, `session_created_by_agent` or `merge_performed_by: agent`
  fails; the fallback `PR40_CONDITIONAL_HANDOFF_ACCEPTED` KEEP and now also requires
  `not merge_observed_result_returned` (A1-5's predicate); the observed merge
  `PR40_OBSERVED_MERGE_HANDOFF_ACCEPTED` requires origin PR-35 or RS-40, `subscription_active`,
  `observed_merge_event`, `merge_performed_by: Nathan`, `three_events_separate`, and the contract's
  `direct_PR35_to_PR40_automatic_edge` false; the five runnable-prompt negatives KEEP.
- **`replan`** (new; child C8, fv-main:30): accepts (`REPLAN_NEW_PROCEED_ACCEPTED`) a `REJECT` for a
  precise in-scope defect only with receiver PR-20, `new_top_level_session_nathan_creates`, `new_plan`,
  `new_proceed_on_new_plan`, the contract's `reject_replan` edge(s) targeting exactly `["PR-20"]`, and
  `rescope_contract.new_proceed_required` false; `second_proceed_same_plan`,
  `proceed_between_pr30_and_pr35` or a receiver other than PR-20 fails.
- **`observation`** KEEP.

The projection code is the drafters' simulated code (`/tmp/claude-0/spec/s8b/B2/flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py`, as diffed against the installed runner), unchanged by §12.

**Scenario edits.** `scenarios.json` keeps its hand layout (pretty-printed header keys, one compact row
per line).
- PR-SPLIT-POS-01: input fact `same_session_pr35` → `new_dedicated_pr35_session`; expected
  `PR30_TO_PR35_NEW_DEDICATED_SESSION`.
- PR-SPLIT-NEG-01: input `{requests_additional_proceed, pr35_in_pr30_session}`; variant
  `new-session-only` → `pr35-in-pr30-session-only`; attribution `PR35_ADDED_BOUNDARY` KEEP.
- HANDOFF-POS-01, HANDOFF-NEG-01 and its five variants: `same_session` false,
  `session_disposition: NEW_DEDICATED`.
- HANDOFF-POS-02 kept for the fallback (coverage:19); gains variant `subscription-accepted-not-delivering`
  (`subscription_call_succeeded` true, `subscription_active` false; sweep:14, coverage:3).
- New HANDOFF-POS-03 (the `MERGE_OBSERVED` positive) with variant `rs40-resumed-pr35-phase` (sweep:0).
- New HANDOFF-NEG-02 with variants `before-any-merge`, `observed-without-active-subscription`,
  `agent-merge`, `automatic-dispatch`, `fallback-after-merge-observed`.
- New REPLAN-POS-01: `{decision: REJECT, precise_in_scope_defect, receiver: PR-20,
  new_top_level_session_nathan_creates, new_plan, new_proceed_on_new_plan}` →
  `REPLAN_NEW_PROCEED_ACCEPTED`.
- **New REPLAN-NEG-01 — each negative carries its own expected label** (child C8; §12 *Skill-edit
  decisions*, verifier contradiction 8). Each variant is REPLAN-POS-01's input plus exactly one defect:
  ```
  {"name":"second-proceed-same-plan","input":{…REPLAN-POS-01…,"second_proceed_same_plan":true},"expected":"VALIDATION_FAILURE","expected_rule":"PR40_REJECT_REPLAN_PROCEED"}
  {"name":"proceed-between-pr30-and-pr35","input":{…REPLAN-POS-01…,"proceed_between_pr30_and_pr35":true},"expected":"VALIDATION_FAILURE","expected_rule":"PR40_REJECT_REPLAN_PROCEED"}
  {"name":"reject-routed-to-pr30","input":{…REPLAN-POS-01…,"receiver":"PR-30"},"expected":"VALIDATION_FAILURE","expected_rule":"PR40_REJECT_REPLAN_ROUTE"}
  ```
  The row's own input carries all three defects.
- `required_fixture_ids` gains the four ids. `negative_rule_attribution` and `EXPECTED_NEGATIVE_RULES`
  (runner `:31`–`:47`) gain:
  ```
  "HANDOFF-NEG-02": "PR40_ENTRY_ON_OBSERVED_OR_ASSERTED_MERGE",
  "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED",
  ```
- Counts (runner `:258`, `:260`, `:267`): 37 ids; 20 positive, 17 negative.

**Runner support for per-variant labels** (verifier contradiction 8: "show that each variant fails for
its own reason"; U-8b-10):
```
REPLAN_DEFECT_REPAIR = {
    ("PR40_REJECT_REPLAN_PROCEED", "second-proceed-same-plan"): {"second_proceed_same_plan": False},
    ("PR40_REJECT_REPLAN_PROCEED", "proceed-between-pr30-and-pr35"): {"proceed_between_pr30_and_pr35": False},
    ("PR40_REJECT_REPLAN_ROUTE", "reject-routed-to-pr30"): {"receiver": "PR-20"},
}
EXPECTED_REPLAN_VARIANT_RULES = {name: rule for rule, name in REPLAN_DEFECT_REPAIR}
```
- a variant's `expected_rule` overrides the row label in its case record;
- `validate_fixture_document` emits `FIXTURE_REPLAN_VARIANT_RULES` unless REPLAN-NEG-01's variant labels
  equal `EXPECTED_REPLAN_VARIANT_RULES` exactly;
- for each REPLAN-NEG-01 variant the runner adds a case `REPLAN-NEG-01::<variant>::single-defect`, which
  passes only when reverting that one defect restores `REPLAN_NEW_PROCEED_ACCEPTED`.

**Runner-level cases.**
- Independent: `("requests_additional_proceed", "pr35_in_pr30_session")` (`:324`); the five
  `independent-handoff-*` cases take `same_session: False`, `session_disposition: NEW_DEDICATED` (`:332`).
- Mutation: `reject-pr35-direct-pr40` (`:361`) is reversed into `reject-second-pr35-pr40-edge` (same
  append, same expected set; fv-main:11, fv-rest:20, adversary:9). The counterparts of the 8b.10
  contract regressions are appended, each an exact error-set comparison, including nine for the checks
  §12 adds: `reject-no-subscription-fallback-shorthand` (`ROUTE_GRAPH_SHORTHAND`),
  `reject-same-session-phase-semantics` (`ROUTE_GRAPH_SEMANTICS`),
  `reject-pr35-role-without-top-level-clause` (`PR35_TOP_LEVEL_ROLE`),
  `reject-event-2-time-without-fallback-predicate` (`POST_MERGE_THREE_EVENTS`),
  `reject-missing-rs40-observed-merge-record` (`POST_MERGE_CONTRACT`),
  `reject-same-session-pr30-ownership` (`PR_DEVELOPMENT_CONTRACT`),
  `reject-shared-session-rescope-lineage` (`RESCOPE_CONTRACT`), `reject-receiver-pr20-removed`
  (`RECEIVER_CONTRACT:PR-20`), `reject-handoff-branch-flag-removed` (`HANDOFF_CONTRACT`).
- Kept mutation cases: `reject-new-proceed-boundary` (now proves the exact map),
  `reject-pr30-direct-pr40`, `reject-missing-pr35-result`, `reject-agent-merge`,
  `reject-incomplete-handoff`, `reject-primary-core-change`.
- Header cases (O28 (a)): `clean_header` = title, `Prompt ID: PR-35`, `Notion URL: …`,
  `## Native purpose` (4 lines, no padding); the two URL-label mutations re-index from 5 to 2; the four
  URL-label negatives KEEP; added `accept-header-free-of-release-lines` and ten
  `reject-release-header-*` cases (`Prompt Version:`, `Prompt version:`, `Set:`, `Ecosystem release:`
  plain, then bold, bullet, blockquote, bold-label-only, code-span, table-cell forms).
- Other literals: docstring `:2` "33" → "37"; `:702` `validator_revision` → `"3.3.0"`; the `:726`
  comment's reason clause (W-7):
  ```
  old: No path option: a file would persist.
  new: No path option: {C-D22}.
  ```

**Pins** (fv-main:29): `EXPECTED_FIXTURE_SHA256` (`validate_gcfpe_20260914.py:945`) and the profile's
`fixtures.sha256` and `count` (`:15`, `:12` → 37), set after `scenarios.json` is final, in §5's order.

### 8b.10 Must-fail regressions

Skill-text regressions run on a scratch copy of the edited tree
(`/tmp/claude-0/v2work8/work/regress_8b.py`, `dbc2e62587c98a57…`); contract and graph regressions on
the measurement candidate in memory (`run_contract.py`, `a357982d1d702f85…`); fixture-document
regressions through the runner (`reg_fix.py`, `65ee7a3872c019cb…`). `RS` = `ROUTING_SURFACE_CHANGED`.
Contract regressions are scored on `validate_contract`; a graph set is stated where the regression
targets `validate_graph_contract`.

**Skill text (36 regressions, all exact; plus the two clean controls, change-flow validator `PASS` and suite `FLOWMASTER_SUITE_PASS`):**
```
R-CF-RP-1…14   retired loop, one per entry      inject the phrase before <!-- FLOWMASTER_SPECIALIZATION_END -->   exit 1; "FAIL: retired skill clause present: <phrase>"; count 1
R-CF-CASE      retired loop is case-insensitive  inject "ONE DEDICATED PR-DEVELOPMENT SESSION"                     exit 1; "FAIL: retired skill clause present: one dedicated PR-development session"; count 1
R-CF-A18       NEW :301                          delete {A18}                                                     exit 1; "FAIL: missing skill clause: never as a subagent, forked agent or workflow agent of PR-30"
R-CF-NINE      :1022                             delete {NINE}.                                                   exit 1; "FAIL: missing skill clause: {NINE}"
R-CF-DISP      NEW (C-DISPATCH)                  delete " No agent merges, and no session is created by an agent."  exit 1; "FAIL: missing skill clause: no session is created by an agent"
R-CF-PROC      NEW (C-PROCEED)                   delete {C-PROCEED}                                               exit 1; "FAIL: missing skill clause: One Proceed per approved per-PR plan"
R-CF-HND       NEW (C-HANDOFF)                   delete "It carries no branch and no commit: "                    exit 1; "FAIL: missing skill clause: It carries no branch and no commit"
R-CF-REV       :746                              revision 3.3.0 → 3.2.9                                          exit 1; "FAIL: specialization revision"
R-OV-1…3       CONTRACT_REQUIRED override        replace {OVERRIDE} in change-flow / relay / tw                  FLOWMASTER_SUITE_FAIL; that skill only: "missing specialization contract: {OVERRIDE}"
R-TOP-R, -T    CONTRACT_REQUIRED {A18}           delete {A18} in relay / tw                                      that skill only: "missing specialization contract: {A18}"
R-FB-R1…4      relay CONTRACT_FORBIDDEN          inject each of the four phrases                                 relay only: "superseded contract present: <phrase>"
R-FB-T1…4      tw CONTRACT_FORBIDDEN             inject each of the four phrases                                 tw only: "superseded contract present: <phrase>"
R-REV-R        relay revision                    3.1.0 → 3.0.0                                                   relay only: "missing specialization contract: SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0"
R-REV-T        tw revision                       1.2.0 → 1.1.6                                                   tw only: "missing specialization contract: TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0"
```
The suite-level rows recompute `SKILL_TREE_SHA256` after the mutation, so only the named finding remains.

**Contract and graph (53, all exact):**
```
R-AB-1  added_boundaries.session 1→0                          {PR35_ADDED_BOUNDARY}
R-AB-2  added_boundaries.cross_session_route 1→0 (V-1)        {PR35_ADDED_BOUNDARY}
R-AB-3  added_boundaries.proceed 0→1                          {PR35_ADDED_BOUNDARY}
R-PC    shared_exactly_one re-gains the session field         {PR_PHASE_CONTINUITY}
R-V-1   pr35_result_vocabulary without MERGE_OBSERVED         {PR35_RESULT_VOCABULARY}
R-V-2   member_registry PR-35 result_states without it        {PR35_STATE_ROUTES, STATE_REGISTRY_MISMATCH:PR-35}
R-DE-1  second PR-35→PR-40 edge                               {DIRECT_PR35_PR40_EDGE, RS}
R-DE-2  PR-35→PR-40 automatic true                            {DIRECT_PR35_PR40_EDGE, RS}
R-DE-3  RS-40→PR-40 automatic true                            {DIRECT_PR35_PR40_EDGE, RS}
R-DE-4  PR-35→PR-40 merge condition missing                   {DIRECT_PR35_PR40_EDGE, RS}
R-DE-5  PR-40 entered before any merge (MERGE_PENDING)        {DIRECT_PR35_PR40_EDGE, RS}
R-DE-6  RS-40→PR-40 edge removed                              {DIRECT_PR35_PR40_EDGE, RS, STATE_EDGE_MISMATCH:RS-40:merge_observed}
R-DE-7  PR-30→PR-40 edge (kept prohibition)                   {DIRECT_PR30_PR40_EDGE, RS}
R-DE-8  graph and contract both gain a second PR-35 edge      contract {DIRECT_PR35_PR40_EDGE, RS}; graph {GRAPH_DIRECT_PR40_EDGE}
R-MB-1  merge-assertion boundary edge removed                 {PR40_MANUAL_MERGE_BOUNDARY, RS}
R-MB-2  boundary edge automatic true                          {PR40_MANUAL_MERGE_BOUNDARY, RS}
R-MB-3  DOC-20 condition loses its merge-assertion phrase     {PR40_MANUAL_MERGE_BOUNDARY, RS}
R-MB-4  a QA-10 prompt edge into PR-40                        {PR40_MANUAL_MERGE_BOUNDARY, RS}
R-PM-1  direct_PR35_to_PR40_automatic_edge true               {POST_MERGE_CONTRACT}
R-PM-2  event_2.fact → product_owner_manual_merge_assertion   {POST_MERGE_THREE_EVENTS}
R-PM-3  agent_merge_authorized true                           {POST_MERGE_CONTRACT}
R-PM-4  event_2.time → sweep:10's "…, else asserted …" (V-3)   {POST_MERGE_THREE_EVENTS}
R-PM-5  observed_merge_edges loses its RS-40 entry (V-2)      {POST_MERGE_CONTRACT}
R-PM-6  observed_merge_edges[0].automatic true (V-2)          {POST_MERGE_CONTRACT}
R-RG-1  ordinary_pr_work_unit re-gains the assertion node     {ROUTE_GRAPH_SHORTHAND}
R-RG-2  pr40_reject_replan removed                            {ROUTE_GRAPH_SHORTHAND}
R-RG-3  fallback key renamed pr35_no_subscription_fallback (V-4)  {ROUTE_GRAPH_SHORTHAND}
R-SEM-1 old key same_session_phase_continuation restored (W-8) {ROUTE_GRAPH_SEMANTICS}
R-SEM-2 pr40_entry back to today's text (W-8)                 {ROUTE_GRAPH_SEMANTICS}
R-SEM-3 pr40_reject_replan semantics removed (W-8)            {ROUTE_GRAPH_SEMANTICS}
R-ROLE  PR-35 receiving_role without the A1-8 clause (W-1)    {PR35_TOP_LEVEL_ROLE}
R-RP-1  PR-40 REJECT edge and state route → PR-30             {PR40_REJECT_REPLAN_ROUTE, RS}
R-RP-2  rescope new_proceed_required true                     {RESCOPE_CONTRACT}
R-RC-1  PR-35 old same-session flag                           {RECEIVER_CONTRACT:PR-35}
R-RC-2  PR-40 nathan_manual_merge_assertion_required true     {RECEIVER_CONTRACT:PR-40}
R-RC-3  PR-30 accepts a PR_WORK_UNIT_LINEAGE_REVIEW REJECT (C9 negative control)  {RECEIVER_CONTRACT:PR-30}
R-RC-4  PR-20 entry removed                                   {RECEIVER_CONTRACT:PR-20}
R-RC-5  RS-40 accepts a PR_WORK_UNIT_LINEAGE_REVIEW REJECT (C9 negative control)  {RECEIVER_CONTRACT:RS-40}
R-RC-6  PR-40 entry_fact → sweep:10's "…WHERE_NO_SUBSCRIPTION" (V-4)  {RECEIVER_CONTRACT:PR-40}
R-HC-1  re-insert status_completed_work_decisions_constraints_unresolved_authority  {HANDOFF_CONTRACT}
R-HC-2  actual_pasteable_complete_prompt false                {HANDOFF_CONTRACT}
R-HC-3  prohibited_references loses "branch"                  {HANDOFF_PROHIBITED_REFERENCES}
R-HC-4  no_branch_or_commit removed (V-6)                     {HANDOFF_CONTRACT}
R-HC-5  every_required_repository_and_pr_reference re-inserted (V-6)  {HANDOFF_CONTRACT}
R-HC-6  graph handoff_contract.prohibited gains an entry the contract lacks (V-6 subset)  contract {}; graph {GRAPH_HANDOFF_PROHIBITED_REFERENCES}
R-HC-7  prohibited_references loses "menu"                    contract {HANDOFF_PROHIBITED_REFERENCES}; graph {GRAPH_HANDOFF_PROHIBITED_REFERENCES}
R-R1-1  r1_oracle_changed false                               {PROTECTED_IDENTITIES}
R-R1-2  protected_r1_46_rows_unchanged true                   {GRAPH_PROOFS}
R-R1-3  pr35_adds_r1_row true                                 {PROTECTED_IDENTITIES}
R-ID    contract_revision 4.0.6                               {CONTRACT_IDENTITY}
R-PS    primary_skill_revision 1.2.5                          {PR_DEVELOPMENT_CONTRACT}
R-OWN   pr30_ownership[5] → "complete same-session PR-35 handoff" (W-8)  {PR_DEVELOPMENT_CONTRACT}
R-LIN   preserved_lineage[1] → PR_DEVELOPMENT_SESSION         {RESCOPE_CONTRACT}
```

**Header and body (carried from v1's measurement; the code is unchanged by §12, and the floor is 4):**
```
R-HDR-1  a body with "Prompt Version: 091426.1" after its Prompt ID: line   {PROMPT_BODY_RELEASE_HEADER:PR-35}
R-HDR-2  each of the 12 decorated header vectors in the header window        prompt_body_release_header true for all 12; identity stays valid
R-HDR-3  the four URL-label negatives                                        prompt_identity_header_valid false for all four
R-MK     a PR-35 body without MERGE_OBSERVED                                 {PROMPT_ROUTE_SEMANTICS:PR-35:MERGE_OBSERVED}
```

**Fixture document (measured):**
```
R-FX-1   REPLAN-NEG-01 reject-routed-to-pr30 relabelled PR40_REJECT_REPLAN_PROCEED   failing cases {section-13-fixture-document (FIXTURE_REPLAN_VARIANT_RULES), REPLAN-NEG-01::reject-routed-to-pr30::single-defect}
R-FX-2   reject-routed-to-pr30 also carries second_proceed_same_plan                failing cases {REPLAN-NEG-01::reject-routed-to-pr30::single-defect}
```

**Limits, measured.** Reverting `{NINE}` to `{TEN}` in place in `change-flow/SKILL.md` fires two checks
(the missing new literal and the retired old one); only the injection form meets "exactly its own
finding". `flowmaster-validate/SKILL.md` prose has no literal guard; only `SKILL_TREE_SHA256` reads it.

### 8b.11 Revisions and pin sites

Every revision pin moves in the same set (amendment, *New revisions*). Byte and identity pins are set
in §5's order: matrix → oracle → runtime map → graph → contract → profile → literals → fixtures →
`SKILL_TREE_SHA256` last.
```
change-flow 3.2.9 → 3.3.0
  change-flow/SKILL.md:8
  change-flow/scripts/validate_gcfpe_20260914.py:746
  flowmaster-validate/scripts/validate_flowmaster.py:147, :686
  flowmaster-validate/scripts/validate_gcfpe_current.py:634, :635
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:27
  (flowmaster-validate/SKILL.md:25 and :44 are history; kept)

session-relay-flowmaster 3.0.0 → 3.1.0
  session-relay-flowmaster/SKILL.md:8
  flowmaster-validate/scripts/validate_flowmaster.py:182

tw-flowmaster 1.1.6 → 1.2.0
  tw-flowmaster/SKILL.md:8
  flowmaster-validate/scripts/validate_flowmaster.py:128
  flowmaster-validate/SKILL.md:184

flowmaster-validate 3.2.16 → 3.3.0
  flowmaster-validate/SKILL.md:8

validator_revision 3.2.14 → 3.3.0   (§12 §8b O27 (a))
  flowmaster-validate/scripts/validate_flowmaster.py:1221
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1090
  flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:702
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:45

glow-hde-pr-development 1.2.5 → 1.3.0, sites in these packages (value §8a.5)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1722, :2592
  flowmaster-validate/scripts/validate_gcfpe_current.py:651          (S-5; §12 §8b O14 (a))
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:28

contract revision 4.0.6 → 4.1.0 (A1-2)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1390
  change-flow/scripts/validate_gcfpe_20260914.py:751
  flowmaster-validate/SKILL.md:155

routing surface 7380cd14…/282 → fecc319bdd4ce7ee6201cb77d7231861/284 (A1-7)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:207, :208
  change-flow/scripts/validate_gcfpe_20260914.py:76, :77

edge count 227 → 229 (A1-7)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1118
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:20
  change-flow/scripts/validate_gcfpe_20260914.py:806

bundled graph sha and bytes (value from the final build, §5 order)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:941, :942
  change-flow/scripts/validate_gcfpe_20260914.py:21
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:19, :24

contract sha and bytes (value from §6's regenerator, §5 order)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:943, :944
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:4, :8

fixtures sha and count 33 → 37 (§12 §8b O29 (a))
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:945, :1123
  flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:2, :258, :260, :267 (and :31-:47 attribution)
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:12, :15
  flowmaster-validate/SKILL.md:176, :381, :383

R1 identities and paths: §5 (listed in 8b.8)

SKILL_TREE_SHA256 (last)
  flowmaster-validate/SKILL.md:9
```

### 8b.12 Measured (v2)

All runs used copies under `/tmp/claude-0/v2work8/` with `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR`
inside the scratch area. Afterwards no `.pyc` or `__pycache__` existed there or in the drafters'
directories; the installed tree was only read; `git status` in the repository was clean. No prompt body
was read.

1. **Copy A — every skill-text and skill-side literal edit of §8a and §8b** (not the contract-side
   literals, which move with §6's contract), with today's contract, graph and R1 files, and
   `SKILL_TREE_SHA256` recomputed:
   - `validate_flowmaster.py --skills-root <copy>`: `FLOWMASTER_SUITE_PASS`, no findings (the default
     overlay now runs the v4 validator);
   - `change-flow/scripts/validate_gcfpe_20260914.py`: `PASS`;
   - `validate_gcfpe_20260914.py <cf> --contract <v4 contract>`: `ok: true`;
   - `validate_gcfpe_current.py <cf>` (default) and with the alias passed explicitly (v3 path):
     both `ok: true`;
   - `run_gcfpe_current_fixtures.py` and `run_change_flow_fixtures.py`: `fixture_suite_ok: true`;
   - relay self-test: `PASS`, 230 cases;
   - historical-layer spot checks (`validate_strength_middleware.py`, `validate_epic_alpha.py`): `ok: true`;
   - the embedded core measured `4e565e40…` in all three edited skills.
2. **Skill-text regressions on copy A:** 36 of 36 exact, and both clean controls pass (8b.10).
3. **Copy M — the 8b.7 reversals on a measurement candidate** (`cand.py`, `a5185c0f95b792d3…`): §6's
   prototype `/tmp/claude-0/spec/s6/after_contract.json` and `after_graph.json` with every §12 value
   applied: V-1 (`cross_session_route` 1 in the contract map, the graph `adds` and the PR-35 node, with
   `adds_session` true per §4 P35-8), V-2, V-3, V-4, V-5, V-6, V-7, V-8, W-1, W-2, W-8 and W-10. The
   R1 successor digest is §5's and is not stood in. Results:
   - `validate_contract` and `validate_graph_contract` both `[]`;
   - `routing_surface` = `('fecc319bdd4ce7ee6201cb77d7231861', 284)`, 229 edges;
   - 53 of 53 contract and graph regressions exact;
   - today's 091426.1 contract under the new validator returns 22 codes, and today's graph two, so every
     reversal rejects the old state:
   ```
   CONTRACT_IDENTITY DIRECT_PR35_PR40_EDGE GRAPH_PROOFS HANDOFF_CONTRACT HANDOFF_PROHIBITED_REFERENCES
   POST_MERGE_CONTRACT POST_MERGE_THREE_EVENTS PR35_ADDED_BOUNDARY PR35_RESULT_VOCABULARY PR35_STATE_ROUTES
   PR35_TOP_LEVEL_ROLE PR40_REJECT_REPLAN_ROUTE PROTECTED_IDENTITIES PR_DEVELOPMENT_CONTRACT PR_PHASE_CONTINUITY
   RECEIVER_CONTRACT:PR-20 RECEIVER_CONTRACT:PR-35 RECEIVER_CONTRACT:PR-40 RESCOPE_CONTRACT ROUTE_GRAPH_SEMANTICS
   ROUTE_GRAPH_SHORTHAND ROUTING_SURFACE_CHANGED
   graph: GRAPH_DIRECT_PR40_EDGE GRAPH_HANDOFF_PROHIBITED_REFERENCES
   ```
4. **The fixture runner on copy M** with the candidate contract: 228 cases, 0 failed. `profile_errors`
   were `PROFILE_FIXTURE_HASH`, `PROFILE_GRAPH_PIN` and `PROFILE_IDENTITY`, as expected before the pins
   move. R-FX-1 and R-FX-2 as stated.
5. **Not re-measured in v2** (carried from v1 8b.12, unchanged by §12): the header vectors (R-HDR-1…3,
   R-MK), and the strict candidate suite over both 216-case runs with every pin moved (v1 copy B2).
   E4 re-runs both on the final bytes.
6. **Session-creation scan.** The edited `change-flow`, relay, `tw-flowmaster`, PR and amthor skill
   text outside the core was scanned for create/spawn/launch/provision/start/open/schedule … session.
   Every GCFPE hit is a prohibition, names Nathan as the creator, or is the override; the only
   instructions to create sessions are `tw-flowmaster:281`, `:425`, `:427` (the TW flow; out of scope,
   8b.5).

### 8b.13 Findings placed, and rows superseded

**Placed here.** Where the value belongs to §5 or §6, the site is placed here and the value is cited.
- Preflight: fv-main:0–3, 5–7, 9, 11–17, 19, 23–35 (18, 20, 21 as §5 pin sites); fv-rest:3, 9–26, 28
  (0–2, 4–8, 27 as §5 sites; 29 as §9's command); pr-relay-graph:16–22, 32.
- Critics: coverage:3, 4, 7–9, 12–15, 19, 23; sweep:0, 2, 3, 5–8, 10–14, 20–22; adversary:1, 3, 7, 9,
  10, 13, 16, 17.
- Verifier items resolved here: contradictions 0, 1, 7 and 8; conflicts 0, 2, 3, 4, 10, 17 and 19
  (full paths); unplaced 2 (rule 8b).

**Superseded, recorded so §E can cite them** (coverage:7, sweep:11), reconciled with §1 (§12 *Other
settlements*):

| row | superseded part | governed by |
|---|---|---|
| fv-main:2 | the map with `cross_session_route` 0, and its fixture "reject-cross-session-route=1" | V-1: the negative sets it to 0 (R-AB-2) |
| fv-main:9 | 281/282 rows | A1-7: 284 |
| fv-main:13 | `direct_PR35_to_PR40_automatic_edge` true | A1-5; D23 successor note: stays false |
| fv-main:15 | edge count 226 | A1-7: 229 |
| fv-main:20, fv-rest:1, fv-rest:2 | in-place re-pin of the historical map and alias | A1-1 (§5); S-5 |
| fv-main:31 | change `versioned_sibling_successors` | A1-2, A1-3: kept |
| fv-rest:20 | rewrite HANDOFF-POS-02 | A1-5, coverage:19: kept for the fallback |
| fv-rest:23 | "record the alias as a known contradiction" | S-5: re-pointed |
| sweep:10 | the names `pr35_no_subscription_fallback`, `OBSERVED_MERGE_EVENT_OR_NATHAN_ASSERTION_WHERE_NO_SUBSCRIPTION`, and `event_2.time` "…, else asserted …" | V-3, V-4 (A1-5's single predicate) |
| sweep:13 | predicate "where no subscription existed" | A1-5's single predicate |

**Anchor corrections:** sweep:5 cites `tw-flowmaster:9` (the revision is on `:8`); step 45's old string
is at `flowmaster-validate/SKILL.md:231`–`:232`, not `:55`–`:60`.

### 8b.14 Unsettled

§12 settles every §8b question by option letter. These are the words, names and placements the
settled options still leave open. Each carries the compiled value placed above; EXECUTE uses it only if
Nathan confirms it, and otherwise stops (§0).

- **U-8b-1 — W-9's scoping words at relay `:255` and `:713`.** W-9 says "scoped to non-GCFPE
  exchanges". Compiled: "Outside a GCFPE main-ecosystem stage, …", the complement of W-9's own added
  sentence. The difference is `GCFPE-MGMT-10` work, which the D23 clarification does not bind: under the
  compiled words it may still return `SESSION_PROVISIONING_REQUIRED`; under a literal "non-GCFPE" it
  could not.
- **U-8b-2 — Glue at relay `:285` / `tw:321`.** Compiled: "Return a populated resume of the recorded PR
  phase in the recorded phase's own session after the actual merge, …" (§12 §8b O21 (b) gives the
  phrase, not the sentence).
- **U-8b-3 — S-7's placement.** S-7 names `:353` and `:372`; `:353` is a line inside the fenced manifest
  template, where a prose sentence would corrupt the template. Compiled: the sentence once, at `:372`,
  after the `CONTROL_PLANE: NOTION` binding sentence; `:353` unchanged.
- **U-8b-4 — `change-flow:557` and `:561` wording.** §12 §8b O11 (a) and OQ-7 (a) fix the intent (link
  the successor only; describe it as the current projection; name the historical map as provenance).
  Compiled texts in 8b.2.
- **U-8b-5 — Wording for `change-flow:563`, `flowmaster-validate/SKILL.md:157` and `:381`.** S-5 and
  §12 §8b O12 (a), O13 (a) fix the facts, not the words. Compiled texts in 8b.2 and 8b.6.
- **U-8b-6 — `change-flow:321`.** sweep:20's wording ("in that phase's own session, worktree, branch
  and open PR") drops "workspace/" from this line. Compiled: sweep:20's phrase with "workspace/" kept.
- **U-8b-7 — The C-PROCEED literal in the `change-flow` validator.** §12 §8b O16 (b) names C-PROCEED but
  no substring. Compiled: "One Proceed per approved per-PR plan", the literal §12 §8a O9 (a) fixes for
  the PR skill.
- **U-8b-8 — Three new error-code names**, which v1 never simulated (so O30 (a) does not cover them):
  `ROUTE_GRAPH_SEMANTICS` (W-8), `PR35_TOP_LEVEL_ROLE` (W-1), `GRAPH_HANDOFF_PROHIBITED_REFERENCES`
  (V-6's subset check; O32 (b) asked for "a new graph-parity code"). Also a placement choice: V-2 and
  V-3's literal checks, and W-8's `pr30_ownership` and `preserved_lineage` checks, sit inside the
  existing codes `POST_MERGE_CONTRACT`, `POST_MERGE_THREE_EVENTS`, `PR_DEVELOPMENT_CONTRACT` and
  `RESCOPE_CONTRACT` rather than under new names.
- **U-8b-9 — The comment and docstring texts.** The `validate_gcfpe_20260914.py:904`–`:908` comment is
  rewritten to cite D23-G; compiled: `# D23-G: a body carries no release-bound header line
  (Prompt version, Set, Ecosystem release); prompt_body_release_header rejects one in the header
  window.` The `:2287`–`:2291` docstring has no reason clause, so W-7 changes nothing there. Neither is
  a check.
- **U-8b-10 — REPLAN-NEG-01's labels and proof.** §12 reads "a Proceed label for each Proceed case";
  compiled as the one simulated label `PR40_REJECT_REPLAN_PROCEED` on both Proceed variants (O30 (a)),
  and `PR40_REJECT_REPLAN_ROUTE` on the route variant. To show each variant fails for its own reason, the
  runner gains the `::single-defect` cases and `FIXTURE_REPLAN_VARIANT_RULES`; this is runner code no
  source words.
- **U-8b-11 — Nine new fixture mutation counterparts** (8b.9) for the checks §12 adds, beyond v1's
  list. They take the measured runner count to 228 on the candidate; §9 uses the count measured at E4.

## §9 The gate, E4 — commands and pass criteria

The gate runs once, after E1–E3, on a scratch copy of the synced tree with the six edited packages
laid over it. Every command runs with `PYTHONDONTWRITEBYTECODE=1`, and each tool's own top-level
flag is read by name. **A green section count beside a false suite flag is a failure.**

1. **Graph.** `graph_parts.py build` must give 55 nodes, 229 edges and 55 state routes. Its embedded
   JSON, plus one newline, must be byte-identical to both bundled graph copies. (The builder's own
   endpoint check always passes, so it proves assembly only.)
2. **Parity and routing.** `validate_graph_contract(contract, graph)` must return `[]` for both
   contract copies. `routing_surface(contract)` must equal
   `('fecc319bdd4ce7ee6201cb77d7231861', 284)`.
3. **Live suites** (§2) all pass, run on the edited copy.
4. **Historical layer** (§2): every result equals its baseline.
5. **The v4 fixtures** pass (`fixture_suite_ok: true`). The case counts are recorded, with every new
   case named.
6. **The other packages' validators** pass: the PR skill, the relay self-test, the audit skill's
   fixture suite, and the registry structure check.
7. **Bodies.**
   - The 55 edited bodies from E3 are piped as `{id: text}` to the edited validator with
     `--bodies-stdin`.
   - `prompt_bodies_validated` must list all 55, and `prompt_body_checks_not_evaluated` must be empty.
   - **No body text is written anywhere.**
8. **Registry assertions, in memory.**
   - For each registry row, call `_evaluate_assertions(row, bodies[row["prompt_key"]], ref)`,
     imported from a scratch copy of the audit skill. The registry is loaded with `load_data` from
     the execution branch.
   - **Pass means zero findings on every row.** Nothing is snapshotted or hashed, and no evidence
     file holds a body digest.
9. **Must-fail regressions.**
   - **Which:** every new guard, every reversed validator literal and every new check (§5–§8).
   - **How:** each mutates one thing in memory or in a scratch copy.
   - **Pass:** the findings on the mutated input, minus those on the clean input, equal exactly the
     one expected finding. For registry guards the key is `(f["rule_id"], f["observed"]["summary"])`;
     for validators it is the named error code.
10. **Closure and records.** `closure.py` over PR-10, PR-20, PR-30, PR-35, PR-40, RS-40, DOC-10 and
    DOC-20 must match the expected new closure. `modification_validate.py` must pass both records.

§E records every command, its flag values and its counts.

## §10 The review, E5

Per `D24` and `reviewer-prompt-template.md` v1.1.

1. **The brief comes first.** Fill the template once for the whole set, and commit it under
   `docs/ephemeral/modifications/evidence/` before any reviewer is spawned. The reviewers are
   maintenance subagents, which the `D23` clarification allows.
2. **The set under review:**
   - the six `.skill` packages, each with file count, bytes and sha256;
   - the contract regenerator and the registry deriver;
   - `route_sim_final.py` and the body rules script;
   - the successor source matrix;
   - this specification, and the E4 results.
3. **What the brief tells reviewers to attack, weakest first:**
   - the successor oracle's provenance;
   - the regenerator's contract-only value table;
   - each reversed literal, and whether its replacement still guards what is kept;
   - the guard patterns;
   - the body rules script's anchors;
   - the fallback path in PART-11.
4. **Two fresh reviewer subagents**, never forked, each briefed only by the committed brief. Each
   writes `SECTION-10-REVIEW-a1-<id>.md`.
5. **Approval** needs both verdicts to be `SKILL_FIT_CONFIRMED` against the same digests. Any
   `SKILL_REPAIR_REQUIRED` finding is repaired and re-reviewed on the new bytes, by fresh reviewers.

## §11 The cut-over, E6 — runbook

**Held until:** both verdicts confirm, and Nathan has received the six packages, the six rollback
packages, the brief and both verdicts.

| # | who | action | stop if |
|---|---|---|---|
| 0 | Nathan | Confirm no GCFPE lifecycle session is in flight, then merge the execution PR. **The freeze starts** | a session is in flight |
| 1 | Nathan | Install all six packages together | — |
| 2 | session | `freeze.py` on each installed tree must equal its reviewed digest | any digest differs |
| 3 | session | Installed suite (§2 live suites) passes on the installed tree, run with `PYTHONDONTWRITEBYTECODE=1` from a scratch copy | any failure |
| 4 | session | Land the body edits: for each of the 55 pages, fetch, derive the edits with the reviewed rules script, `update_content`, and read back. The readback is checked the way the E3 form was: the edited validator and the page's registry assertions must pass on it. It is never byte-compared or hashed (`prompt-corpus-policy.md`) | any check fails |
| 5 | session | Re-scan all 55 live bodies: the installed validator with `--bodies-stdin`, plus registry assertions from the registry at the merge commit | any finding |
| 6 | session | Notion control edits with readback: steps 6, 9, 16, 36 and 44, and child C11 | any readback differs |
| 7 | session | Report to Nathan: every step's result, with the digests | — |
| 8 | Nathan | **Lift the freeze** | — |

**On any stop:**
- The freeze stays, and the session reports exactly where it stopped.
- Bodies already landed are **not** rolled back automatically. Nathan decides.
- Nathan can reinstall the rollback packages, whose digests §2 records.
- A partial body landing is repaired forward with the reviewed rules script, never by hand.

## §12 Decisions the plan's author settles

The section drafters were told to compile and never to decide. They left 157 open questions, and the
verifier found 10 contradictions, 20 conflicts, 6 regex errors and 7 unplaced findings. This log
settles each one, cited by **the section's own question id**; option letters are the section's own.
Each decision follows these principles, in order:
1. Nathan's rulings.
2. Never weaken a check (`AF-001`): take the option that keeps or adds a guard.
3. Historical bytes never change.
4. A1-5's single fallback condition, "only where no `MERGE_OBSERVED` result was returned for this
   merge", everywhere.
5. The smallest edit that satisfies the ruling.

The E5 reviewers are pointed at this log first.

### Scope decisions

- **S-1 — Steps 41–43 run in this cut-over.** This settles §1 OQ-2, §7 OQ-12 and verifier conflict 12.
  - **Why:** Nathan's PART-12 ruling says bodies drop their release-bound header lines, and A1-3 only
    defers C-VERSION's successor-page rule.
  - **C-VERSION** is placed with this qualifier: *"It applies from the release after 091426.1;
    091426.1's bodies were edited in place by `MODIFICATION-20260923-alpha-feedback-open-entries`
    (`D23-G`)."*
  - **Step 41** also covers `prompt-body-content-policy.md:88` (sweep:17).
- **S-2 — The small documentation corrections are compiled as E1 edits.** This settles §1 OQ-1,
  §7 OQ-10 and OQ-11, and verifier contradiction 9.
  - **N1.** A new key, `body_identity_disposition`, under `body_extraction_convention` in the
    registry. It states that the `evidence_contract` and `source_snapshot` identities describe the
    bodies before `D23` and no longer identify them.
  - **`authoritative-surfaces.md:59`** is corrected to match. Its token lines `:29` and `:45-46`, and
    `ecosystem-change-management.md:143`, are labelled *"as measured before `D23`"*, not restated.
  - **N2.** `ecosystem-change-management.md:141` becomes *"`required_regex` binds the Canon source and
    the `D23` canonical wordings; `forbidden_regex` guards `D7`, the `D23` reversals and session
    creation."* No count.
  - **`ecosystem-change-management.md:176`** becomes "carried, until `D23-G` removed them,".
  - **`execution-and-delegation-model.md`** gains the scope line in the `D23` clarification's words
    (§3 open question 13).
- **S-3 — The skill-bundled graph copies are validator fixtures built from the parts.** They are not
  the Drive or repository copies of an assembled graph that `glow-graph-contract/SKILL.md:59`
  forbids, so writing them breaks no rule. This settles §1 OQ-6. Making that skill say so explicitly
  is added to *Noticed, not in scope*.
- **S-4 — Every prose line that restates a reversed rule is converged.** None is left untouched. This
  settles §1 OQ-7, verifier conflicts 10 and 13, and sweep:13.
  - **`change-flow:366` and `glow-hde-pr-development:135`:** each is kept verbatim only if §E records
    that the line restates no reversed rule. Otherwise it is converged.
- **S-5 — The alias is re-pointed** (§1 OQ-19, §8b O12 (a), verifier note 4).
  - **Unlinked:** the 091326.2 alias leaves `change-flow/SKILL.md` and `OPTIONAL_REFERENCES`. Its
    file is unchanged, as a historical record.
  - **Re-pointed to the 091426.1 contract:** the defaults at `validate_gcfpe_current.py:615`,
    `run_gcfpe_current_fixtures.py:104` and `validate_flowmaster.py:818`.
  - **`change-flow:563`** lists the alias as superseded and names the 091426.1 contract by its own
    `contract_id` (§8b O13 (a)).
  - **The v3 path:** `validate_gcfpe_current.py:651` moves to 1.3.0, and `:652` is replaced by "run in
    two dedicated sessions" (§8b O14 (a); verifier contradiction 7). The v3-path pin at `:302` stays,
    because it is historical (§8a O25).
- **S-6 — Relay `:624`** gains *"A runtime handoff still names its destination by full name, version
  and direct Notion URL (C-HANDOFF); `NOTION_REFERENCE` stays versionless for reusable prompt
  text."* This settles §1 OQ-12, §3 open question 13 and §8b O23.
- **S-7 — `CONTROL_PLANE` keeps its enum.** This settles §1 OQ-11 and §8b O22 (a). At relay `:353` and
  `:372`: *"`NOTION` means a maintenance surface that a destination rule names; live task, handoff and
  decision state lives in the repository."*
- **S-8 — The schema enum doc gains `DEDICATED_PR_REVIEW_SESSION`,** in the fifth package. This
  settles §1 OQ-15 and §8a O20 (a).
- **S-9 — `RS-40`'s `session_class DEDICATED_ONE_OFF` is left unchanged,** and §E records it as a
  pre-existing inaccuracy out of scope (verifier unplaced 6).

### Wording decisions

- **W-1 — The PR-35 role.** This settles §1 OQ-8, §3 open question 3, §4 OQ-6, §6 Q6.15, §7 OQ-5 and
  verifier contradiction 4. Step 30's sentence is followed by the A1-8 clause, verbatim. It is the
  same string in `PR-35.json` `receiving_role`, the contract `member_registry`, and the registry
  `session_role`, single-quoted in YAML if needed:
  ```text
  You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
  ```
  Its guard phrase, which the registry and the new `flowmaster-validate` check on
  `member_registry['PR-35'].receiving_role` share (verifier unplaced 2), is `never as a subagent,
  forked agent or workflow agent of PR-30`. coverage:6's phrase is superseded.
- **W-2 — The RS-40 role.** This settles §1 OQ-9, §3 open question 4, §4 OQ-8 and §7 OQ-6.
  - **Graph `receiving_role` and registry `session_role`:** *"You resume the recorded phase in its own
    dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE
    PR-35."*
  - **Registry `creator_role`:** *"the recorded phase's own dedicated session for the exact suspended
    work unit."*
  - **Mirrored** into `member_registry['RS-40'].receiving_role` (verifier conflict 16).
- **W-3 — The PR-20 and PR-40 roles stay.** This settles §1 OQ-10, §3 open question 5, §4 OQ-9, §6
  Q6.16 and §7 OQ-7, option (b). Body-level C-TOP and its guards carry the rule for them. The `D23`
  clarification's *Guard* paragraph is corrected to say: *"PR-35's graph, contract and registry role,
  and every main-ecosystem body (C-TOP)."*
- **W-4 — PR-40's entry wording**, in the body and in the registry input at `:3710`. This settles §1
  OQ-23, §3 open question 6 and §7 OQ-8:
  ```text
  PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on Nathan's assertion that he manually merged it.
  ```
  PR-40's PR-35-result input at `:3705` becomes:
  ```text
  The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical pre-merge evidence.
  ```
- **W-5 — The ASK OK? variant** (§1 OQ-16, §3 open question 1, §7 OQ-3). The text is C-PLACE verbatim,
  then *"`ASK OK?` is the line immediately before the block."* The guard is option (c), both parts:
  - a required pattern on that sentence, with a deletion regression;
  - G08's forbidden old wording.

  §E records that ordering in the *output* can be checked only on outputs.
- **W-6 — C-SESSION in skill text.** The backticks are dropped, and A1-8's sentence goes last. This
  settles §1 OQ-5 and §3 open question 2, option (a) in both.
- **W-7 — C-D22** replaces each site's reason clause with the C-D22 reason, verbatim (§3 open question
  8, §8b O26 (a)).
- **W-8 — Contract-only texts** (§1 OQ-18, §6 Q6.8–Q6.10):
  - **`route_graph_semantics.same_session_phase_continuation` is renamed
    `pr30_to_pr35_phase_continuation`,** with the value *"PR-30 to PR-35 is one lawful phase
    continuation inside GCF-17 into PR-35's own top-level session, which Nathan creates by pasting
    PR-30's handoff; not a new work unit, and never a subagent."*
  - **`route_graph_semantics.pr40_entry`** becomes the W-4 sentence.
  - **New key `route_graph_semantics.pr40_reject_replan`:** *"A PR-40 REJECT for an in-scope defect in
    landed work re-plans through PR-20 in a new top-level session that Nathan creates, with a new
    Proceed for the new plan (D23-F)."*
  - **`pr_development_contract.pr30_ownership[5]`** becomes *"complete PR-35 handoff to the dedicated
    PR-35 session"*.
  - **Each changed value gets an exact-value check,** with a must-fail regression (§6 Q6.18, option
    (a)).
- **W-9 — The change-flow and relay session-creation lines** (verifier contradictions 0–2):
  - **`change-flow:450`** becomes *"GCF-14 — Nathan creates one dedicated top-level PR session for one
    planned PR work unit."* The old imperative joins the retired-phrase list.
  - **Relay `:255` and `:713`** are scoped to non-GCFPE exchanges, and gain after `:255`: *"For a GCFPE
    main-ecosystem stage, return the paste-ready `NEXT_PROMPT_HANDOFF` and stop for Nathan;
    provisioning does not apply."* (§8b O2 (b)).
  - **`glow-hde-pr-development:173`** drops "hidden " (§8a O14 (b)).
- **W-10 — Handoff contract lists** (§4 OQ-4, option (c)):
  - **`required`** keeps the two surviving strings, "exact selected prompt full name/version/direct
    Notion URL" and "receiving role and exact session", and adds three: "input artifact repository
    paths with one-line labels", "pull request reference when the receiver continues an existing PR"
    and "minimum exceptional context only for a condition the artifacts do not record".
  - **`prohibited`** gains "branch", "commit" and "restated artifact content", appended in that order.

### Contract and graph values

- **V-1 — `cross_session_route` is 1** (§1 OQ-4, §6 Q6.12, verifier conflict 0). The PR-30 → PR-35
  handoff now crosses sessions, so the graph `adds`, the PR-35 node and the contract's
  `added_boundaries` all carry 1. `PR35_ADDED_BOUNDARY` is the exact map {`session`: 1,
  `cross_session_route`: 1, every other key 0}. The negative fixture sets `cross_session_route` to 0.
  fv-main:2 is superseded in that part only.
- **V-2 — The observed-merge record** (§4 OQ-5, §6 Q6.11a). A key `observed_merge_edges` goes inside
  `post_merge_three_event_contract`, in the graph and the contract. It is a list of two summary
  objects, `{from, to: "PR-40", branch_id: "merge_observed", state: "MERGE_OBSERVED", automatic:
  false, transport: "COMPLETE_NEXT_PROMPT_HANDOFF"}`, for PR-35 and RS-40, in that order. A literal
  check with a regression guards it (§8b O33 (b)).
- **V-3 — `event_2`** (§6 Q6.11b, verifier conflict 1 and contradiction 6):
  - **`actor`:** "Nathan / Product Owner".
  - **`fact`:** "product_owner_manual_merge_observed_or_asserted".
  - **`time`:** *"observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only
    where no MERGE_OBSERVED result was returned for this merge"*.
  - **`value`:** `true`.
- **V-4 — Names worded on A1-5's condition** (§6 Q6.6, Q6.7; §8b rule 8):
  - `receiver_compatibility.PR-40.entry_fact` = `"MERGE_OBSERVED_OR_NATHAN_ASSERTION_WHERE_NO_MERGE_OBSERVED"`,
    and `nathan_manual_merge_assertion_required` is deleted;
  - the route shorthand for the fallback is `pr35_merge_pending_fallback` = [PR-35,
    NATHAN_MANUAL_MERGE_ASSERTION, PR-40];
  - no other new shorthands, apart from the child's `pr40_reject_replan`.
- **V-5 — `receiver_compatibility`** (§6 Q6.5, Q6.21, verifier conflict 3):
  - **PR-20** = `{"accepted_inputs": ["PR_INSTRUCTION", "PR-40:PR_WORK_UNIT_LINEAGE_REVIEW:REJECT"],
    "earlier_cycle_pr_is_landed_history": true, "existing_work_unit_replan": true,
    "new_proceed_for_new_plan": true, "new_top_level_session_created_by_nathan": true}`.
  - **The new check `RECEIVER_CONTRACT:<id>`** asserts the exact content of **all seven** receivers.
    Its negative control: no entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` REJECT.
- **V-6 — `transition_contract`** (§6 Q6.1–Q6.4, §1 OQ-17, §8b O32, verifier conflicts 4 and 17):
  - **Deleted:** `status_completed_work_decisions_constraints_unresolved_authority`,
    `epic_change_and_work_unit`, `next_action_and_expected_output` and
    `every_required_repository_and_pr_reference`.
  - **Added, each `true`:** `artifact_repository_paths_with_labels`, `pr_reference_when_continuing`,
    `exceptional_context_only`, `no_branch_or_commit` and `no_restated_artifact_content`.
  - **`prohibited_references` gains,** in this order: "branch", "commit", "restated artifact
    content", "menu", "metadata-only summary", "blank form" and "placeholder after publication".
  - **`HANDOFF_CONTRACT`:** `set(transition_contract) == set(After)`, and every value except
    `prohibited_references` equals After.
  - **`HANDOFF_PROHIBITED_REFERENCES`** checks its own value.
  - **The subset check** (graph `handoff_contract.prohibited` ⊆ `prohibited_references`) is adopted,
    with a must-fail regression.
- **V-7 — The R1 identity flags** (§5 OQ-8, §6 Q6.13, Q6.14): `r1_oracle_changed: true` and
  `protected_r1_46_rows_unchanged: false`. §5's check N9 (the 43 unchanged rows equal the historical
  rows, in the same order) is the replacement guard. No new pointer key is added; the oracle's
  authority block carries `D23`.
- **V-8 — PR-35's `native_function`** gains *"; return MERGE_OBSERVED when an active subscription
  observes Nathan's merge"* before its final period (§4 OQ-7, §6 Q6.17, option (b)).
- **V-9 — `merge_pending_requirements`** keeps "no unresolved material boundary" (§6 Q6.19). PART-07
  converges routing sentences only. §E records it.
- **V-10 — Graph identity** (§4 OQ-3, option (a)). EXECUTE applies the routing transform first and
  checks it against the A1-7 checkpoint: 574 175 bytes, `b1911cf5…`, `fecc319b…`/284. It then applies
  the non-routing edits and re-checks `fecc319b…`/284 and 229 edges. The final bytes are measured and
  recorded.
- **V-11 — The A1-7 row count is 15:** 13 changed and 2 new edge rows, plus 7 state-route rows (§4
  OQ-2, option (a); verifier conflict 8). The amendment's "16" is corrected to 15.
- **V-12 — MERGE_OBSERVED in the registry's `outputs[].states`** goes in ASCII order, since those
  lists are sorted (§7 OQ-4 (a)). Everywhere else it goes in A1-5's order.

### Successor oracle

Settles §5 OQ-1 to OQ-14.
- **Error codes** extend the existing series: `FMV-ORACLE-008` onward for the oracle and matrix, and
  `FMV-GCF-MAP-007` for the historical map's digest (OQ-1 (a)).
- **`required_global_tokens`:** the old profile id is replaced by the new one in the successor oracle
  (OQ-2 (a)).
- **Authority block** (OQ-3). The existing keys stay, and three are appended:
  - `successor_source_matrix_sha256`;
  - `successor_rows` = [`GCF-14`, `GCF-17`, `GCF-17.LINEAGE`], in oracle order and compared as a set;
  - `successor_authority` = "D23-D, D23-F; Product Owner 2026-09-23".

  The original matrix digest attests the rows not listed in `successor_rows`. A new check pins
  `r1_frozen_snapshot_sha256`, `r1_verdict` and the two library ids to their historical values, and
  it states that they attest the original matrix only.
- **Readings of the A1-1 table** (OQ-4): an ellipsis keeps today's prefix, and GCF-14's
  `pr_work_unit_lineage_review` is appended at the end of `consumes`. Both are confirmed.
- **Matrix layout** (OQ-5):
  - a short prose header;
  - a ```` ```json ```` fence per changed row, holding `json.dumps(indent=2, ensure_ascii=False)` of the
    row plus `supersedes_source_row_sha256`, in oracle key order;
  - after each block, a line `source_row_sha256: <hex>`.

  The matrix digest is the sha256 of the file's bytes.
- **Where the matrix lives** (OQ-6): the repository copy is at
  `docs/prompt_ecosystem_management/r1-successor-source-20260923.md`, because it is an authority
  source, not a Modification's evidence.
- **Links** (OQ-7 (a)): `change-flow:557` links the successor map only, and `OPTIONAL_REFERENCES`
  replaces the historical path with the successor path. The historical map stays as a file checked by
  its historical pins.
- **Fixture** (OQ-9): id `GCF-LINEAGE-REPLAN-01`, appended at the end. The file's `oracle_profile`
  moves to the new id.
- **R1 literals** (OQ-10): a check ties `validate_gcfpe_20260914.py`'s R1 literals to the successor
  oracle file's digest, so they cannot fall stale.
- **A builder script** for the matrix, the oracle and the map is committed with the evidence and
  reviewed in E5 (OQ-11 (a)).
- **Missing files** (OQ-12): N1 and N3 skip when their file is absent, and the structure check reports
  it, so each regression still yields exactly one finding.
- **`flowmaster-validate` SKILL.md's "It pins:" list** names the successor matrix and its digest, and
  the kept historical oracle digest (OQ-13 (a)).
- **Two further choices** (OQ-14):
  - N9 also requires the historical row order;
  - `historical_non_executable_references` gains the historical oracle and map filenames.
- **Expected findings:** G11's expected set is its two wrapper codes (verifier conflict 18). Paths
  are always written in full (verifier conflict 19).

### Registry guards

Settles §7 OQ-1 to OQ-15 and verifier regex errors 0–3.
- **G04 (Notion-resident)** applies to the 10 step-5 rows (OQ-1 (a); §1 OQ-22 (a)).
- **G15 (old continuity list)** applies to all 54 main-ecosystem rows, cleared by E4's clean control
  (OQ-2 (b)).
- **ASK OK?:** see W-5 (OQ-3).
- **G06:** the window widens to `{0,1500}?`, the value the verifier measured (OQ-13 (b)).
- **G19 and G20:** the verifier's corrected values are adopted (OQ-14):
  - G19 gains the possessive exclusion `(?!['’]s\b)` after the prompt id, so "Run PR-35's tests in a
    subagent" is not caught;
  - G20 gains `(?<!Nathan )`, so "Nathan creates a new session for PR-40" is not caught.

  Their stated limits are recorded in §E. E4's clean control runs over the 54 edited bodies, and any
  hit goes to Nathan, never exempted.
- **Header guards G12–G14** use the verifier's decorated-header prefix (regex error 2). It catches
  all 12 forms of each key and stays silent on "Settings:" and "Setup:" lines.
- **Masking** (OQ-15, option (b)). The required guards anchor on sentences found only in the
  canonical texts:
  - G07: "The final response ends with the `NEXT_PROMPT_HANDOFF` block.";
  - G24: "stay subscribed and do not poll";
  - G25: "The observed merge event is the fact PR-40 is entered on".

  Each regression deletes that sentence.
- **The PR-20 input** drops its backticks, following the registry's convention (OQ-9 (b)).

### Skill-edit decisions

**§8a** settles O1 to O25:
- C-ART goes after `:158`, and C-LAT per O2 (a). `:17` loses "original" (O3 (a)). The tail of `:22`
  is deleted, because recovery covers it (O4 (a)).
- Recovery step 3 uses the child's words (O5 (a)). `:82` per O6 (b), and `:77` repeats the
  landed-history rule.
- The "adds no … session" lists use the registry wording "any session beyond its own dedicated PR-35
  session" (O7 (b)). `behavioral-fixtures.md:49` stays verbatim.
- `:133` drops its branch-state clause (O8 (b)).
- C-PROCEED's literal is O9 (a). The old lists and "ten-field" are also forbidden, each with a
  regression (O10 (b)).
- `amthor`'s fixture suite gains its forbidden assertion (O11 (b)).
- New literals: "Subscribing is not polling", "no session is created by an agent" and "It carries no
  branch and no commit", each with a deletion regression (O12 (b)).
- No C-TOP in the skill (O13 (a)). `:173` per W-9. `behavior-cases.md:57` converges (O15 (b)).
- Headings are added for C-DEC, C-LAT, C-SUB and MERGE_OBSERVED (O16 (b)).
- O17 (a), O18 (a) and O19 (a) as compiled.
- `amthor` gains invariants for C-ART and C-PLACE, a MERGE_OBSERVED acceptance fixture and a re-plan
  fixture (O21 (b)).
- Glue as compiled (O22 (a)). `:162`'s second sentence is replaced whole by C-HANDOFF (O23 (a)).
  C-PLACE goes at the end of `:162` (verifier conflict 15).
- The historical pin stays (O25).

**§8b** settles O1 to O34:
- Override positions as simulated (O1 (a)). Provisioning per W-9 (O2 (b)). `CONTRACT_REQUIRED` holds
  the whole override text (O3 (a)).
- `CONTRACT_FORBIDDEN` gets the same four phrases for both the relay and `tw-flowmaster` (O4 (b)).
- O5 (a), O6 (a) and O7 (a) as simulated. `:453` also takes A1-1's PR-35 session cell (O8 (b)). O9 (a).
  `:313` and `:323` stay verbatim, per child C7 (O10).
- O11 (a). The alias per S-5 (O12 (a), O13 (a), O14 (a)).
- The retired-phrase loop is case-insensitive (O15 (b)). It includes the old `:450` imperative.
- Required literals are added for C-DISPATCH ("no session is created by an agent"), C-PROCEED and
  C-HANDOFF ("It carries no branch and no commit") in `change-flow`'s validator, and for C-SESSION's
  top-level sentence in `CONTRACT_REQUIRED` for the relay and `tw-flowmaster`. Each has a deletion
  regression (O16 (b)).
- `:259`, and `tw:304`, drop "/handoff" from their scope (O17 (b)).
- The artifact edit is made at relay `:273` **and** `change-flow:277` (O18 (b)).
- At relay `:279` the order is **C-HANDOFF, then C-PLACE**, as in the bodies. `tw:315` equals the new
  relay `:279` (O19).
- `:283` and `tw:319`: C-SESSION is prepended, and "supplies merge approval" is reworded to "is not a
  merge approval or merge instruction" (O20 (a) and (b)).
- `:285` and `tw:321` converge to "resume in the recorded phase's own session" (O21 (b)).
- O22 per S-7, and O23 per S-6. O24 (a) and O25 (a). O26 per W-7.
- `validator_revision` becomes 3.3.0 (O27 (a)). The header floor is 4 (O28 (a); §1 OQ-3).
- Four new scenario ids: 37 ids, split 20/17, with the runner count measured at E4 (O29 (a)). Error
  names as simulated (O30 (a)). The positive rule compares exact strings (O31 (a)). The subset check
  is added (O32, per V-6). Literal checks for V-2 and V-3 are added (O33 (b)).
- `change-flow:321` takes sweep:20's wording (O34 (b)).
- **Child C8's three negatives** each carry their own expected label: `PR40_REJECT_REPLAN_ROUTE` for
  the route, and a Proceed label for each Proceed case (verifier contradiction 8).

### Other settlements

**§3 remaining open questions:**
- C-PLACE goes in 53 bodies (option (a)).
- C-HANDOFF's "an issued version is never edited" covers the handoff's input artifacts, so its text
  stays.
- C-PROCEED's body set: the rules script anchors on the sentence and reports every body it edits, §E
  lists them, and E4 checks them.
- No session-creation regex applies to skill text. `CONTRACT_FORBIDDEN` entries are exact phrases,
  and each is tested against the override and the invariant texts.

**§4:**
- OQ-1: the stages are in §0, with two commits.
- OQ-10: the amendment's edge-index bullet is corrected to what was measured. New edges take indices
  128 and 129, which match `_other_edge_indices` entries that no edge carries. No two placed edges
  share an index.

**§1:**
- Its table is reconciled with these decisions, so each finding has exactly one disposition, and
  partial supersessions are listed (verifier conflict 11).
- coverage:21 is cited to its fix (verifier unplaced 5).
- registry-audit:11's postflight note is recorded in §E.

**§6:** Q6.20 is settled on approval. A `D23` successor note then records A1-3 and A1-5, and corrects
`D23-E`'s parenthetical: `direct_PR35_to_PR40_automatic_edge` stays `false`.

**§9:** the fixture count is the one measured at E4, not 172 (verifier note 3).


### Addendum, v2 — the questions the v2 rewrite left open

The v2 rewrite applied §12 inline and left these questions open. Each is settled here. Where a worker
placed a value in the text, that value is adopted unless the line says otherwise. The E5 reviewers
attack these next after §12 itself.

**§1 and §3:**
- **U-1.** `glow-hde-pr-development:121` takes sweep:19's qualifier (S-4).
- **U-2.** In `change-flow`, C-LAT and the step-14 clause each go in a new sentence directly after
  `:323`. `:453`–`:454` take C-LAT's definition by reference ("material change, as defined above").
- **U-3.** The docstring at `validate_gcfpe_20260914.py:2288`–`:2291` is left unchanged, because it
  has no reason clause.
- **U-4.** N1's text is *"The `evidence_contract` and `source_snapshot` identities on every row
  describe the bodies before `D23` (2026-09-23) and no longer identify them. They are not regenerated,
  because hashing bodies is prohibited (`prompt-corpus-policy.md`)."*
  `authoritative-surfaces.md:59` states the same fact in one sentence.
- **U-5.** The scope line is a new paragraph at the end of `execution-and-delegation-model.md` §1,
  headed "**Scope (`D23`, 2026-09-23).**", followed by the `D23` clarification's sentence.
- **U-6.** After relay `:255`, the GCFPE override comes first and W-9's sentence second.
- **§12 S-2's citation** means v1 §3 question 9, not 13.

**§5:**
- **The matrix bytes.** The prose header is exactly:
  *"# R1 successor source matrix — 2026-09-23\n\nAuthority: D23-D, D23-F; Product Owner 2026-09-23.
  One block per changed row.\n"*
  - One blank line separates each block from the next.
  - The file ends with one newline.
  - A check reads each `source_row_sha256:` line and compares it with the oracle's digest.
- **The builder** is `docs/ephemeral/modifications/evidence/build_r1_successor.py`.
- **The new checks** are coded `FMV-ORACLE-008` to `016`, in N order, and `FMV-GCF-MAP-007`, as the
  worker placed them.
- **The R1-literal tie check** runs in `validate_flowmaster.py`, with code `FMV-ORACLE-017`.
- **The two added regressions** are adopted. The tie-check regression's expected set is measured at
  E4.
- **The "It pins:" bullets** are adopted as the worker wrote them.
- **`handoff_contract.required` order:** the two kept strings first, then the three new ones (§4).

**§6 and §7:**
- **`route_graph_semantics` exact-value check:** `ROUTE_GRAPH_SEMANTICS`.
- **The prohibited-references subset check:** `GRAPH_HANDOFF_PROHIBITED_REFERENCES`.
- **The three checks placed in existing codes** stay where the worker put them.
- **PR-40's `D23-E` guard** is `G25B`, `CTR-002`, required on PR-40 only:
  ```text
  PR-40 is entered on the observed merge event
  ```
  G25 stays on PR-35 and RS-40.
- **G08A** keeps its id, with rule `TOP-001`.
- **`:3705` keeps PR-40's PR-30-result input.** The W-4 sentence is added as its own input line
  alongside it, and replaces only the clause about the PR-35 result.

**§8a and §8b:**
- **U-8a-1, U-8a-2 and U-8a-4:** the worker's wording is adopted.
- **U-8a-3:** the two-finding sets for R-37 and R-55 are accepted and recorded as their expected
  sets. Both forbidden entries are kept, and none is dropped.
- **U-8b-1:** "Outside a GCFPE main-ecosystem stage" is adopted. It is correct, because
  `GCFPE-MGMT-10` and the triage prompt are excepted by `D23`.
- **U-8b-2 and U-8b-4 to U-8b-7:** the worker's wording is adopted.
- **U-8b-3:** the S-7 sentence goes once, at `:372`, because `:353` is inside a code fence.
- **U-8b-8:** the error-code names are adopted: `ROUTE_GRAPH_SEMANTICS`, `PR35_TOP_LEVEL_ROLE` and
  `GRAPH_HANDOFF_PROHIBITED_REFERENCES`.
- **U-8b-9:** the comment at `:904`–`:908` cites `D23-G` and `PROMPT_BODY_RELEASE_HEADER`.
- **U-8b-10 and U-8b-11:** the worker's runner code and nine mutation cases are adopted.
- **The TW flow's own session-creation instructions** (`tw-flowmaster:281`, `:425` and `:427`) are
  outside the main ecosystem. §E records them, and they are not edited.
