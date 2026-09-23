---
artifact_type: GCFPE_MODIFICATION_EXECUTION_SPECIFICATION
modification_id: MODIFICATION-20260923-alpha-feedback-open-entries
also_serves: MODIFICATION-20260923-pr40-reject-replans
version: v1
written: 2026-09-23
status: PART OF AMENDMENT 1, awaiting Nathan's approval with it
compiled_by: workflow wf_6c82e4c3-777 (8 section drafters, 1 verifier); sections 0, 2, 9-12 by the plan's author
---

# Execution specification — Amendment 1

This file holds the exhaustive detail behind `Amendment 1` in the Modification's §P. It gives:
- every edit, literal and guard value;
- every pin site;
- every command, with its arguments and baseline result;
- the disposition of every finding.

**How to read it:**
- **§0** defines the stages and the order of precedence.
- **§1 and §3–§8** were compiled by eight drafters who were told to compile and never to decide. They
  therefore list open questions and options.
- **§12 settles every one of those questions**, by each section's own question id. Read every section
  with §12 applied. An option §12 does not name is void.
- **Wherever a section and §12 disagree, §12 governs.** A choice that would contradict one of the
  amendment's rulings is not settled anywhere in this file: EXECUTE stops and brings it to Nathan.

**What comes next.** Before E1 starts, a consolidated `v2` of this file, with §12 applied inline and
the options removed, replaces it as `EXECUTION-SPEC-20260923-alpha-feedback-open-entries-v2.md`. The v2 is checked against this v1 and §12, and EXECUTE runs from it.

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

This section gives every preflight row (121) and every critic finding (77) exactly one disposition, and says where each one is carried. It decides nothing. Where the amendment, the child plan and the findings leave a choice, the row points to an open question in §1.6.

### 1.1 Precedence

1. **Amendment 1 governs.** Its *Precedence* paragraph: wherever it changes a step, a ruling or a canonical wording, it governs, and "the same holds against any preflight row or critic finding that disagrees with it". The decision record's two `D23` successor sections, the *Correction* (GCF-17.LINEAGE, not GCF-15) and the *Clarification* (top-level sessions only; nothing creates a session), are rulings the amendment cites; they rank with it. The follow-up's §P (child steps C1–C11) governs its own steps and shares the parent's package, gate, review and cut-over.
2. **The original §P governs where the amendment is silent:** its rulings table, canonical wording (C-*) and steps 0–48.
3. **Findings come last.** A finding supplies a value only where neither the amendment nor §P speaks, and never against either. Where two findings disagree and the amendment is silent, neither governs; the point is an open question.

**What the amendment changes in §P**, and so what every finding is read against:
- Steps 0 and 1 stand; they ran under the original approval.
- §P's PART-11 ruling row (the session-launch option), §P's C-SUB and §P's C-DISPATCH are superseded by A1-5's C-SUB and C-DISPATCH.
- Step 15 runs only through A1-2's contract regenerator (defect 1).
- Step 34's in-place re-pin is replaced by A1-1's successor oracle (defect 3). Historical oracle, runtime map, correction layers and historical contracts keep their bytes; their validators and pins are never edited.
- Step 38: the flag below stays false, the merge-assertion boundary stays as the fallback, and the observed-merge edge is recorded inside `post_merge_three_event_contract` (A1-5). PR-35 → PR-40 and RS-40 → PR-40 are paste edges (A1-7).

```
"direct_PR35_to_PR40_automatic_edge": false
```

- Every fallback condition, including step 39's "where no subscription existed", is worded as A1-5's single predicate:

```
only where no `MERGE_OBSERVED` result was returned for this merge
```

- C-VERSION applies from the next release, and 091426.1 is edited in place (A1-3).
- Step 46 is replaced by E4, and step 47 by E5 (`D24`): six packages (A1-6), one cut-over under a freeze (A1-4), new revisions with every pin moving.
- C-TOP is new, and C-SESSION gains its PR-35 clause (A1-8).
- The routing surface moves only as A1-7's table says. Its identities, and the simulation that is their authority:

```
routing surface   fecc319bdd4ce7ee6201cb77d7231861 / 284 rows
graph             229 edges
simulation        route_sim_final.py  sha256 e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26
```

**The first draft.** The critics worked against the first draft of the amendment, so their targets cite its numbering (N3, N7, the step-changes table). Where Amendment 1 carries the same content (N3 and N7 are A1-8 and spec §7; the first draft's A1-1 to A1-7 keep their numbers), the finding is placed there. Amendment 1 carries none of the first draft's step-changes table or its N1, N2, N4, N5 and N6. A finding whose only home was one of those is UNPLACED (OQ-1, OQ-13).

### 1.2 Superseded findings

**Superseded in full (6).**
- **fv-main:13** — A1-5 keeps `direct_PR35_to_PR40_automatic_edge` false. The `event_2` update it also asks for is carried by A1-2 ("observed or asserted").
- **fv-main:20** — A1-1: a successor runtime map, not an in-place edit. The historical-layer pins it lists are never edited; the live sites re-point to the successor.
- **fv-main:28** — A1-5: `MERGE_PENDING` always carries the conditional PR-40 block as the fallback, so HANDOFF-POS-02 stays (coverage:19) rather than being inverted.
- **fv-main:31** — A1-2 with A1-3: `versioned_sibling_successors` is kept, because it is true of how 091426.1 was made.
- **fv-rest:1** — A1-1: no in-place runtime-map edit; the historical map and the 091326.2 alias keep their bytes. Its list of child rows (GCF-15, GCF-16, GCF-14) is replaced by the `D23` correction and A1-1 (GCF-17.LINEAGE, and GCF-14's `consumes`).
- **coverage:0** — A1-8: C-TOP says "starts", and the guards forbid creating a session to run a named prompt. Its unnamed-object pattern is not adopted.

**Superseded in one value; the rest of the row is placed.**
- fv-main:9 — its 281/282-row figures; A1-7's 284 rows govern.
- fv-main:15 — its 226-edge figure; A1-5 keeps the boundary, and A1-7 gives 229.
- fv-main:22, fv-rest:27 — re-pinning GCF-14 and GCF-15; A1-1 keeps their session wording, read per plan cycle.
- pr-relay-graph:30 — the GCF-15 row; the `D23` correction names GCF-17.LINEAGE.
- fv-rest:2 — re-pinning the alias contract; A1-6 takes the finding's other route and re-points the overlay.
- fv-rest:20 — its DOC-20 phrase edit and its HANDOFF-POS-02 rewrite; A1-5 leaves DOC-20 → PR-40 unchanged and keeps the fallback block.
- fv-rest:28 — its `global.json:48` wording; A1-7's wording governs (child C2).
- pr-relay-graph:8 — deleting the manual-merge clause at `glow-hde-pr-development/SKILL.md:164`; under A1-5 it is rewritten to the fallback predicate (coverage:16).
- pr-relay-graph:25 — new edges "at 235 and above"; A1-7's simulation places them.
- pr-relay-graph:27, registry-audit:10 — the premise that the automatic-edge flag becomes true, and pr-relay-graph:27's `DOC-20.json:151` edit; A1-5.
- sweep:0 — its illustrative digest; A1-7.
- sweep:1 — keeping the broad session pattern; A1-8 adopts named-prompt guards and states the narrowing.
- adversary:1 — its interim digest; A1-7.

### 1.3 How to read the table

- **Order.** Preflight readers `fv-main`, `fv-rest`, `pr-relay-graph`, `registry-audit`, then critics `sweep`, `coverage`, `adversary`; each by number. This is the order of the rendered evidence file.
- **PLACED** — a home exists and the action is determinate. A PLACED row that names an OQ has its action placed but one named value open.
- **SUPERSEDED** — the amendment overrides the finding's required action (§1.2).
- **OUT_OF_SCOPE** — the amendment's *Noticed, not in scope* list carries it. Its items in order: 1 `validate_gcfpe_current.py:602` NameError; 2 the audit skill's snapshot procedure; 3 `flowmaster-validate/SKILL.md:178`; 4 `glow-graph-contract/SKILL.md:13`, `:134`; 5 per-part `edge_indices` and the builder's index collision; 6 the derivation scripts' home.
- **DOCUMENTATION_ONLY** — no action needed. No finding qualifies.
- **UNPLACED** — no home, or the finding's own action is a choice that no source makes.
- **Citations.** A1-1 to A1-8, E4 and E5 are Amendment 1's rulings. "Defect N" is row N of its defect table, which names its answer. "New revisions" is its revision list. "Precedence clause" is its *Precedence* paragraph. "D23 correction" and "D23 clarification" are the decision record's two successor sections. "Step N" is original §P. "Cn" is a child step. Spec sections, of which the amendment itself names §6 to §9: §2 baseline, §3 canonical wording, §4 graph transforms, §5 R1 successor, pin sites and pin order, §6 contract regenerator, §7 registry, §8 skill edits, §9 gate, §10 review, §11 cut-over.

### 1.4 Disposition of every finding

| id | effect or severity | disposition | where |
|---|---|---|---|
| fv-main:0 | WOULD_FAIL | PLACED | step 42 (D23-G); spec §8 header check inverted; OQ-2, OQ-3 |
| fv-main:1 | WOULD_FAIL | PLACED | step 42; spec §8 fixtures (header rebuilt, three-key negatives, URL-label negatives kept); OQ-2, OQ-3 |
| fv-main:2 | WOULD_FAIL | PLACED | step 29 (graph key is `pr_continuity_contract.adds`); A1-2 mirror; spec §4, §8 exact map; OQ-4 |
| fv-main:3 | WOULD_FAIL | PLACED | step 29; A1-2 (`shared_exactly_one` copied); spec §8 nine-field literal |
| fv-main:4 | WOULD_FAIL | PLACED | A1-2 regenerator (defect 1); spec §6 |
| fv-main:5 | WOULD_FAIL | PLACED | steps 29–30; spec §8 fixture and fixture pin |
| fv-main:6 | WOULD_PASS | PLACED | steps 29–30; spec §8 (new-session case inverted per fv-rest:16; extra-Proceed kept) |
| fv-main:7 | WOULD_PASS | PLACED | steps 13, 29–31; spec §8 fixtures |
| fv-main:8 | WOULD_FAIL | PLACED | A1-2 (member_registry pairs); A1-8 (PR-35 role clause); OQ-8, OQ-10 |
| fv-main:9 | WOULD_FAIL | PLACED | A1-7 (approving is the reading; its digest, 284 rows); the finding's 281/282-row figures superseded |
| fv-main:10 | WOULD_FAIL | PLACED | A1-2 regenerator; spec §6 |
| fv-main:11 | WOULD_FAIL | PLACED | A1-5, A1-7 (PR-35 and RS-40 paste edges); spec §8 |
| fv-main:12 | WOULD_FAIL | PLACED | A1-5 (fallback boundary kept; DOC-20 edge unchanged); spec §8 |
| fv-main:13 | WOULD_FAIL | SUPERSEDED | A1-5: `direct_PR35_to_PR40_automatic_edge` stays false; its event_2 update is carried by A1-2 |
| fv-main:14 | WOULD_FAIL | PLACED | A1-2 (shorthands revised, re-plan shorthand); C8; spec §6, §8 |
| fv-main:15 | WOULD_FAIL | PLACED | A1-7 (229 edges); its 226 figure superseded because A1-5 keeps the boundary; spec §5 |
| fv-main:16 | WOULD_FAIL | PLACED | E4 (spec §9 items 1–3); spec §5 pin order; OQ-6 |
| fv-main:17 | WOULD_FAIL | PLACED | A1-2 (flags follow C-HANDOFF; exact-key check); spec §6, §8; OQ-17 |
| fv-main:18 | WOULD_FAIL | PLACED | A1-1 (live pins move to the successor); spec §5 pin sites |
| fv-main:19 | WOULD_PASS | PLACED | A1-2 (R1 flags tell the truth); A1-1 (46 rows; 43-row check) |
| fv-main:20 | WOULD_FAIL | SUPERSEDED | A1-1: successor runtime map; historical map, validators and pins are never edited |
| fv-main:21 | WOULD_FAIL | PLACED | A1-1 (historical files and pins kept, live sites re-pointed; step 34 superseded) |
| fv-main:22 | UNCERTAIN | PLACED | D23 correction; A1-1 (GCF-17, GCF-17.LINEAGE, GCF-14; GCF-14/15 session wording stays) |
| fv-main:23 | WOULD_FAIL | PLACED | spec §5 pin order (`SKILL_TREE_SHA256` last); E4 |
| fv-main:24 | WOULD_FAIL | PLACED | step 35; defect 12, spec §8 (replace) |
| fv-main:25 | UNCERTAIN | PLACED | defect 12, spec §8 (keep); New revisions (every pin moves) |
| fv-main:26 | WOULD_FAIL | UNPLACED | home is step 35 and spec §8, but the backtick choice is not made; OQ-5 |
| fv-main:27 | WOULD_FAIL | PLACED | E4 (edited copy; one must-fail regression per reversed literal); E5 |
| fv-main:28 | WOULD_PASS | SUPERSEDED | A1-5: MERGE_PENDING keeps the conditional PR-40 block, so HANDOFF-POS-02 stays (coverage:19) |
| fv-main:29 | WOULD_FAIL | PLACED | spec §5 pin chain (fixture sha, profile count, id literals); spec §8 |
| fv-main:30 | UNCERTAIN | PLACED | child C8 |
| fv-main:31 | WOULD_PASS | SUPERSEDED | A1-2 with A1-3: `versioned_sibling_successors` is kept, being true of 091426.1 |
| fv-main:32 | WOULD_PASS | PLACED | A1-2 value table (spec §6); A1-6 receiver check; C9 (PR-30 unchanged, sweep:21); OQ-18 |
| fv-main:33 | UNCERTAIN | PLACED | E4 (55 edited bodies through the edited validator); A1-4 readback; C4 |
| fv-main:34 | WOULD_PASS | PLACED | step 45 (C-D22, code sites added); steps 35, 40 (`SKILL.md:164-165`, `:173`); spec §8 |
| fv-main:35 | UNCERTAIN | PLACED | A1-2 (4.1.0); A1-5 (edge recorded inside `post_merge_three_event_contract`, no new top-level key) |
| fv-rest:0 | WOULD_FAIL | PLACED | A1-1 (oracle pin moves to the successor; historical digest still verified); spec §5 |
| fv-rest:1 | WOULD_FAIL | SUPERSEDED | A1-1: no in-place map edit, historical map and alias keep their bytes; rows per D23 correction |
| fv-rest:2 | WOULD_FAIL | PLACED | A1-6 (overlay re-pointed, the finding's second route); A1-1 (alias bytes kept); OQ-19 |
| fv-rest:3 | WOULD_PASS | PLACED | A1-2 (flags truthful); A1-1 (43 unchanged rows; re-stamp regression) |
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
| fv-rest:15 | WOULD_FAIL | PLACED | steps 29–30; spec §4, §8 exact map; OQ-4 |
| fv-rest:16 | WOULD_FAIL | PLACED | steps 29–31; spec §8 fixtures and pins |
| fv-rest:17 | WOULD_FAIL | UNPLACED | home is step 35 and spec §8, but the backtick choice is not made; OQ-5 |
| fv-rest:18 | WOULD_FAIL | PLACED | step 35; spec §8 (cross-skill nine-field pins; `:10` added) |
| fv-rest:19 | UNCERTAIN | UNPLACED | offers edit or record untouched; coverage:15 and sweep:13 disagree; OQ-7 |
| fv-rest:20 | WOULD_FAIL | PLACED | A1-5 (positive PR-35/RS-40 rule, PR-30 ban kept); spec §8; its DOC-20 and POS-02 parts superseded by A1-5 |
| fv-rest:21 | UNCERTAIN | PLACED | A1-5 (MERGE_OBSERVED, ordered vocabulary); C4 (PR-40 keeps "historical pre-merge") |
| fv-rest:22 | WOULD_FAIL | PLACED | steps 42–43; spec §8 fixtures; OQ-2, OQ-3 |
| fv-rest:23 | WOULD_PASS | PLACED | A1-6 (overlay re-pointed to 091426.1); spec §8 |
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
| pr-relay-graph:5 | UNCERTAIN | PLACED | step 14; defect 12, spec §8 (clause only; RS-40 qualification kept) |
| pr-relay-graph:6 | WOULD_FAIL | PLACED | steps 14, 19; defect 12, spec §8 (first sentence kept; `:133` added) |
| pr-relay-graph:7 | UNCERTAIN | PLACED | step 40; defect 12, spec §8 (C-DISPATCH appended; four literals kept) |
| pr-relay-graph:8 | WOULD_FAIL | PLACED | step 40; spec §8; clause rewritten to A1-5's fallback predicate, not deleted (coverage:16) |
| pr-relay-graph:9 | UNCERTAIN | PLACED | step 37; defect 12, spec §8 (C-SUB before `:112`) |
| pr-relay-graph:10 | WOULD_PASS | PLACED | step 20; spec §8 (anchor `:108`; literal made distinct per adversary:5) |
| pr-relay-graph:11 | WOULD_PASS | PLACED | step 10; spec §8 (C-ART after the path; literal added); OQ-21 |
| pr-relay-graph:12 | WOULD_PASS | PLACED | step 24; spec §8 (procedure kept; literal; cases `:49`) |
| pr-relay-graph:13 | WOULD_PASS | PLACED | step 27; defect 12 (sentence kept) |
| pr-relay-graph:14 | UNCERTAIN | PLACED | child C6 |
| pr-relay-graph:15 | WOULD_PASS | PLACED | steps 35, 40; C6 heading; spec §8; OQ-21 |
| pr-relay-graph:16 | UNCERTAIN | PLACED | New revisions (1.3.0, 3.1.0; every pin moves) |
| pr-relay-graph:17 | WOULD_PASS | UNPLACED | offers two enum dispositions; the amendment picks neither; OQ-11 |
| pr-relay-graph:18 | WOULD_PASS | PLACED | step 14 (`:273`, `:279`); spec §8; OQ-12 |
| pr-relay-graph:19 | WOULD_PASS | UNPLACED | conditional relay guard; A1-6 names none for the relay; OQ-13 |
| pr-relay-graph:20 | WOULD_FAIL | PLACED | E4 (spec §9 item 1); spec §5 pin chain |
| pr-relay-graph:21 | WOULD_FAIL | PLACED | A1-2 regenerator; spec §6 |
| pr-relay-graph:22 | WOULD_FAIL | PLACED | A1-5, A1-7; spec §8 (narrowing stated) |
| pr-relay-graph:23 | WOULD_PASS | PLACED | E4 (spec §9 item 1 proves assembly only; item 2 parity) |
| pr-relay-graph:24 | WOULD_FAIL | PLACED | child C1 |
| pr-relay-graph:25 | UNCERTAIN | PLACED | C1 (index 172 kept); A1-7 simulation is the authority; index collision is Noticed, item 5 |
| pr-relay-graph:26 | WOULD_FAIL | PLACED | child C2 |
| pr-relay-graph:27 | UNCERTAIN | PLACED | A1-5 (fallback kept, automatic false, launch withdrawn, DOC-20 unchanged); A1-7 (229) |
| pr-relay-graph:28 | UNCERTAIN | PLACED | steps 29–30 field names; A1-2 mirror; spec §4; OQ-4 |
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
| registry-audit:5 | WOULD_FAIL | PLACED | step 43; spec §7 (header-window guards incl. `Set:`); OQ-2 |
| registry-audit:6 | WOULD_PASS | PLACED | steps 4, 5, 7; spec §7 (companion per adversary:6); OQ-22 |
| registry-audit:7 | UNCERTAIN | PLACED | step 33; spec §7 (quoted input; role parity); OQ-8 |
| registry-audit:8 | WOULD_PASS | PLACED | step 33; spec §7 (forbidden line text) |
| registry-audit:9 | UNCERTAIN | UNPLACED | the RS-40 role text is only an example; its `:3708` edit is placed (spec §7); OQ-9 |
| registry-audit:10 | WOULD_FAIL | PLACED | A1-2 deriver (PR-35, PR-40, RS-40); spec §7; automatic-edge premise superseded by A1-5 |
| registry-audit:11 | WOULD_FAIL | PLACED | child C5 (deriver; PR-20 input); postflight note: OQ-21 |
| registry-audit:12 | WOULD_FAIL | PLACED | defect 10, spec §7; A1-8 guards; OQ-16, OQ-23 |
| registry-audit:13 | WOULD_FAIL | PLACED | A1-6 (fifth package); C10; spec §8 |
| registry-audit:14 | WOULD_FAIL | PLACED | A1-6; spec §8 |
| registry-audit:15 | WOULD_FAIL | PLACED | A1-6; spec §8 (nine-field constant; revision pin) |
| registry-audit:16 | UNCERTAIN | PLACED | A1-6; A1-3 (C-VERSION prospective); spec §8 |
| registry-audit:17 | WOULD_PASS | UNPLACED | no step; the first draft's N1 is not in Amendment 1; OQ-1 |
| registry-audit:18 | WOULD_PASS | UNPLACED | no step; the first draft's N2 is not in Amendment 1; OQ-1 |
| registry-audit:19 | WOULD_PASS | PLACED | A1-2 (line-anchored insertion; `load_data` diff); E4 |
| registry-audit:20 | WOULD_PASS | UNPLACED | optional edit; the amendment is silent; OQ-15 |
| sweep:0 | BLOCKER | PLACED | A1-5, A1-7 (RS-40 edge; A1-7 digest, 284 rows, 229 edges); A1-2 deriver; spec §8; its illustrative digest superseded |
| sweep:1 | GAP | PLACED | A1-8 (C-TOP says "starts"); its keep-the-broad-pattern advice superseded by A1-8's guards |
| sweep:2 | GAP | PLACED | defect 10, spec §7 (D23-E guards); spec §8 (`exact_markers`); OQ-23 |
| sweep:3 | GAP | PLACED | A1-5 (one ordered vocabulary); spec §4, §6, §8 |
| sweep:4 | GAP | PLACED | step 35; defect 12, spec §8; C6 combined lines |
| sweep:5 | GAP | PLACED | A1-6 (sixth package, relay bytes); New revisions (1.2.0); E5; A1-4; OQ-13 |
| sweep:6 | GAP | PLACED | A1-6 (GCFPE override outside the core; `CONTRACT_REQUIRED`) |
| sweep:7 | GAP | PLACED | A1-1 (successor files; historical digests still verified); C3; spec §5 |
| sweep:8 | GAP | PLACED | A1-1 (historical pins never edited); E4 (twelve commands); spec §2, §9 |
| sweep:9 | GAP | PLACED | this section (every row, WOULD_PASS included) |
| sweep:10 | GAP | PLACED | A1-2 (value table; event_2; `versioned_sibling_successors` kept); A1-5; spec §6 |
| sweep:11 | GAP | PLACED | Precedence clause; this section; its fv-main:2 part is OQ-4 |
| sweep:12 | GAP | PLACED | A1-6 (change-flow retired-phrase check); OQ-14 |
| sweep:13 | GAP | PLACED | steps 35, 40; spec §8 (`:353`, `:453`); its no-"untouched" rule is OQ-7 |
| sweep:14 | GAP | PLACED | A1-5 (active only on confirmed delivery; fallback always carried) |
| sweep:15 | GAP | UNPLACED | two options; the amendment picks neither; OQ-10 |
| sweep:16 | GAP | PLACED | child C6; C10 |
| sweep:17 | MINOR | PLACED | step 41 (its no-conflicting-line check); OQ-2 |
| sweep:18 | MINOR | UNPLACED | no step; the first draft's N1 and N2 are not in Amendment 1; OQ-1 |
| sweep:19 | MINOR | UNPLACED | home is step 37, but reword-or-keep is not decided; OQ-20 |
| sweep:20 | MINOR | PLACED | step 35; spec §8 (flowmaster-validate `SKILL.md:393`) |
| sweep:21 | MINOR | PLACED | child C9 |
| sweep:22 | MINOR | PLACED | child C7 |
| sweep:23 | MINOR | UNPLACED | no step; extends the first draft's N1; OQ-1 |
| sweep:24 | MINOR | PLACED | A1-1 (GCF-14 `consumes`; three rows change) |
| sweep:25 | MINOR | PLACED | A1-8 (semantic invariant in the fifth package); spec §8 |
| sweep:26 | MINOR | UNPLACED | the amendment is silent on the no-replacement rule; OQ-6 |
| sweep:27 | MINOR | PLACED | A1-3 (the date is informational) |
| coverage:0 | BLOCKER | SUPERSEDED | A1-8: C-TOP reworded, and guards forbid a session for a named prompt; its pattern not adopted |
| coverage:1 | BLOCKER | PLACED | defect 10, spec §7 (D23-E guards and regressions); OQ-23 |
| coverage:2 | GAP | PLACED | A1-5, its option (b); A1-7; A1-2 deriver (RS-40) |
| coverage:3 | GAP | PLACED | A1-5 (one fallback predicate, in C-DISPATCH and the A1-7 rows); spec §8 fixture |
| coverage:4 | GAP | PLACED | Precedence clause (supersedes the §P PART-11 row and C-DISPATCH) |
| coverage:5 | GAP | PLACED | A1-8 (distinct patterns); spec §7 |
| coverage:6 | GAP | PLACED | D23 clarification, *Guard*; A1-8; spec §7, §8; OQ-8 |
| coverage:7 | GAP | PLACED | Precedence clause; this section |
| coverage:8 | GAP | PLACED | this section |
| coverage:9 | GAP | PLACED | A1-1 (successor files; live versus historical); spec §5 |
| coverage:10 | GAP | PLACED | A1-1 (matrix format, formula, authority block) |
| coverage:11 | GAP | PLACED | A1-1 (43 unchanged rows field for field; re-stamp regression) |
| coverage:12 | GAP | PLACED | A1-2 (handoff flags; exact-key check); spec §6; OQ-17 |
| coverage:13 | GAP | PLACED | A1-2 value table; A1-6 receiver check; OQ-18 |
| coverage:14 | GAP | PLACED | A1-5; spec §8 (every site; `:37` reversal) |
| coverage:15 | GAP | UNPLACED | offers edit or record untouched; sweep:13 disagrees; OQ-7 |
| coverage:16 | GAP | PLACED | A1-5; step 40; spec §8 (`:164`, cases `:87`) |
| coverage:17 | GAP | PLACED | defect 12, spec §8 (per-literal treatment at `:100`, `:141`) |
| coverage:18 | GAP | UNPLACED | the RS-40 role and PR-40 input texts are not given; OQ-9 |
| coverage:19 | MINOR | PLACED | A1-5, A1-7; spec §8 (assertions, fixtures, narrowing) |
| coverage:20 | MINOR | PLACED | A1-1 (GCF-14/15 read per plan cycle); C3 |
| coverage:21 | MINOR | PLACED | child C6 |
| coverage:22 | MINOR | UNPLACED | the amendment is silent on the no-replacement rule; OQ-6 |
| coverage:23 | MINOR | UNPLACED | the amendment is silent on relay `:624`; OQ-12 |
| coverage:24 | MINOR | PLACED | A1-2 (line-anchored; `load_data` diff); its registry-audit:20 part is OQ-15 |
| coverage:25 | MINOR | PLACED | A1-7 (16 route rows plus the 7 state-route rows) |
| coverage:26 | MINOR | PLACED | amendment, *How it was found* (the critic returned nothing) |
| coverage:27 | MINOR | PLACED | A1-8 (PR-50 is a separate edit) |
| adversary:0 | BLOCKER | PLACED | A1-8 (named-prompt guards; narrowing stated); spec §7 |
| adversary:1 | BLOCKER | PLACED | A1-5 (RS-40 included); A1-7 (digest, 284 rows, 229 edges; simulation sha256 recorded); its interim digest superseded |
| adversary:2 | GAP | PLACED | A1-2 (recipe; full compared-pair set; strip-and-regenerate test; negative control) |
| adversary:3 | GAP | PLACED | A1-2 (exact-key handoff check); spec §6 |
| adversary:4 | GAP | PLACED | defect 10, spec §7; OQ-23 |
| adversary:5 | GAP | PLACED | A1-8 (distinct patterns); spec §7 (C-DEC pattern) |
| adversary:6 | GAP | PLACED | spec §7 (fenced values; case-insensitive companion; own regression) |
| adversary:7 | GAP | PLACED | A1-1 (sites, kept checks, regressions); spec §5 pin order |
| adversary:8 | GAP | PLACED | A1-1 (matrix format, digest formula) |
| adversary:9 | GAP | PLACED | A1-5; spec §8 (vocabulary sites; `:361` reversed; fixtures) |
| adversary:10 | GAP | PLACED | A1-6 (re-point; receiver content check); C9; OQ-19 |
| adversary:11 | GAP | PLACED | A1-4 (freeze, stop rule, rollback, rules script in E5, bytecode, merge commit); N-step part is OQ-1 |
| adversary:12 | GAP | PLACED | A1-7 (the committed simulation and its sha256 are the authority); collision is Noticed, item 5 |
| adversary:13 | GAP | PLACED | E4 (twelve historical commands equal baseline); spec §2, §9 |
| adversary:14 | GAP | UNPLACED | the `ASK OK?` variant has no canonical text; child half placed (C-PR20-ENTRY, C-PR30-ENTRY); OQ-16 |
| adversary:15 | MINOR | PLACED | spec §9 items 8–9 (real interface) |
| adversary:16 | MINOR | PLACED | spec §2, §9 (`<root>` defined) |
| adversary:17 | MINOR | PLACED | New revisions (validator revision moves alongside) |
| adversary:18 | MINOR | OUT_OF_SCOPE | Noticed, item 6: the scripts ship in `glow-graph-contract` (A1-2) |
| adversary:19 | MINOR | PLACED | spec §7 (limit recorded; value fenced) |
| adversary:20 | MINOR | PLACED | child C5 (clean control on today's PR-20 body) |

### 1.5 Counts

| disposition | preflight | critic | total |
|---|---|---|---|
| PLACED | 105 | 65 | 170 |
| SUPERSEDED | 5 | 1 | 6 |
| OUT_OF_SCOPE | 2 | 1 | 3 |
| DOCUMENTATION_ONLY | 0 | 0 | 0 |
| UNPLACED | 9 | 10 | 19 |
| **total** | **121** | **77** | **198** |

- **198 rows, confirmed.** A script checked that the table holds every key of `raw_findings.json` exactly once: 121 preflight rows and 77 critic findings, and no others.
- 33 of the 170 PLACED rows name an open question.
- **The five blockers** (sweep:0, coverage:0, coverage:1, adversary:0, adversary:1) match the amendment's count. Four are placed, and coverage:0 is superseded by A1-8.

### 1.6 Open questions

None is decided here. Each lists its options and the rows that depend on it.

- **OQ-1. First-draft items with no home.** Amendment 1 has no step for:
  - N1, the registry's stale `evidence_contract` body identities and `authoritative-surfaces.md:59` (registry-audit:17), extended to each row's `source_snapshot` (sweep:23);
  - N2, `ecosystem-change-management.md:141` (registry-audit:18);
  - the dated token and header lines of sweep:18;
  - adversary:11's assignment of N1, N2 and N5 to E1 and of N4 and N6 to E2.

  The `D23` clarification also says `execution-and-delegation-model.md` gains a scope line (the first draft's N5), with no step or wording. Options:
  - (a) compile them from the findings as E1 repository edits;
  - (b) record each in §E as a known stale statement for a follow-up Modification;
  - (c) Nathan adds them to the amendment.

  `D23`'s "It authorizes only what the plans say" bears on (a).
- **OQ-2. Steps 41–43 in this run.** A1-3 applies C-VERSION "from the next release". C-VERSION's last sentence is the header rule that steps 41–43 implement. But A1-3's stated reason concerns successor pages only, and the amendment does not amend steps 41–43. Options: (a) they run at this cut-over; (b) they are deferred with C-VERSION. Rows: fv-main:0, fv-main:1, fv-rest:22, registry-audit:5, sweep:17.
- **OQ-3. The header check's floor of seven nonblank lines.** fv-main:0 says to re-derive it and gives no value. fv-rest:22 keeps it and pads the fixture header to seven or more. Options: (a) keep seven and pad the fixture; (b) re-derive it, with the measured value brought to Nathan. Rows: fv-main:0, fv-main:1, fv-rest:22.
- **OQ-4. `cross_session_route`.** Neither the amendment nor `route_sim_final.py` sets it. Options:
  - (a) 1 in the graph's `adds` and on the PR-35 node, with a negative fixture for 0 (fv-rest:15, pr-relay-graph:28, sweep:11);
  - (b) 0, with fv-main:2's negative fixture for 1.

  Rows: fv-main:2, fv-rest:15, pr-relay-graph:28, sweep:11.
- **OQ-5. C-SESSION's backticks in skill text.** §P's C-SESSION puts the two prompt ids in backticks. The kept markers are unbackticked: `change-flow/scripts/validate_gcfpe_20260914.py:1020-1021` and `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2580-2586`. Amendment 1 is silent; the first draft dropped the backticks. Options:
  - (a) place the skill sentence without backticks;
  - (b) keep the backticks and replace both markers, each with a must-fail regression.

  Rows: fv-main:26, fv-rest:17.
- **OQ-6. `glow-graph-contract/SKILL.md:59`** forbids minting a replacement assembled graph, and E4 needs new bundled graph copies in two skills. Options:
  - (a) a statement in E2, or a `D23` successor note, that skill-bundled references are validator fixtures built from the parts (sweep:26);
  - (b) amend the rule, which makes `glow-graph-contract` a seventh package (coverage:22);
  - (c) record the conflict for a follow-up Modification.

  Rows: fv-main:16, sweep:26, coverage:22.
- **OQ-7. Lines no finding words or assigns.** `change-flow/SKILL.md:275`, `:278`, `:411` and `:450`–`:455`, less `:453` (sweep:13) and `:455` (C7). Also `flowmaster-validate/SKILL.md:294`. A1-1 keeps the GCF-14/15 wording that `:450`–`:451` restate. fv-rest:19 and coverage:15 allow recording a line as untouched; sweep:13 forbids that for a line that restates a reversed rule. Options:
  - (a) converge each under steps 35 and 40 in spec §8;
  - (b) record each in §E as intentionally untouched, with a reason.

  Rows: fv-rest:19, coverage:15, sweep:13.
- **OQ-8. The PR-35 role string.** A1-8 says the role in the graph, contract and registry "carries the same clause". Step 30 gives a `receiving_role` without the clause. Options: (a) step 30's string followed by A1-8's clause verbatim; (b) the first draft's combined string. The phrase coverage:6's role guard checks follows the choice. Rows: fv-main:8, registry-audit:7, coverage:6.
- **OQ-9. The RS-40 role and PR-40's inputs.** Two texts are missing:
  - an RS-40 role (registry-audit:9 offers only an example; coverage:18 asks for one);
  - wording for PR-40's PR-35-result input to accept `MERGE_OBSERVED`.

  Options: (a) registry-audit:9's example, identical in graph and registry, plus an input sentence compiled from A1-5; (b) wording Nathan gives. Rows: registry-audit:9, coverage:18.
- **OQ-10. The PR-20 and PR-40 roles.** The `D23` clarification's *Guard* names "the graph role and the registry role for each affected prompt", but A1-8 carries the clause into PR-35's role only. Options:
  - (a) append C-TOP's top-level clause to both prompts' graph and registry roles as identical strings, with a parity regression;
  - (b) a `D23` successor note that body-level C-TOP and its spec §7 guards carry the rule, and the roles stay.

  fv-main:8's conditional PR-20 update follows the choice. Rows: sweep:15, fv-main:8.
- **OQ-11. The relay's `CONTROL_PLANE` enum.** Options:
  - (a) keep it, and state at `session-relay-flowmaster/SKILL.md:353` and `:372` that Notion means a maintenance surface a destination rule names;
  - (b) add a repository value, changing the relay validator, its fixtures, `manifest-v2-examples.md:51` and `validate_flowmaster.py:232` together.

  Row: pr-relay-graph:17.
- **OQ-12. `session-relay-flowmaster/SKILL.md:624`** calls `NOTION_REFERENCE` versionless, against C-HANDOFF. Options: (a) add it to step 14; (b) record it in §E as out of scope, with a reason. Rows: pr-relay-graph:18, coverage:23.
- **OQ-13. Retired-phrase guards for the relay and `tw-flowmaster`.** A1-6 gives `tw-flowmaster` the relay's new bytes and the override, held by `CONTRACT_REQUIRED`, but names no `CONTRACT_FORBIDDEN` entries. The relay's own validator never reads its `SKILL.md`. Options:
  - (a) add to `flowmaster-validate`'s `CONTRACT_FORBIDDEN` the relay's two retired phrases (pr-relay-graph:19) and the three phrases sweep:5 names for `tw-flowmaster`, each with a must-fail regression;
  - (b) no entries, recording under AF-001 that these reversals have no mechanical regression.

  Rows: pr-relay-graph:19, sweep:5.
- **OQ-14. How `change-flow`'s retired-phrase check works.** A1-6 decides that the check exists but names no mechanism or phrase list. Options (sweep:12):
  - (a) new obsolete-phrase rules in the successor oracle's `prohibited_active_patterns`;
  - (b) a forbidden-phrase loop in `change-flow/scripts/validate_gcfpe_20260914.py`.

  Row: sweep:12.
- **OQ-15. The `session_class` enum at `project-prompt-registry-schema.md:42`.** The finding marks this edit optional. Options: (a) add the new class in the fifth package; (b) leave it and record the drift. Rows: registry-audit:20, coverage:24.
- **OQ-16. The `ASK OK?` variant of C-PLACE.** Step 18 says where `ASK OK?` goes but gives no text, so the ordering guard of registry-audit:12 cannot be written or regressed (adversary:14). Options:
  - (a) a derived sentence stating that `ASK OK?` is the line immediately before the block, with a required guard and a line-reorder regression;
  - (b) wording Nathan gives;
  - (c) a forbidden-wording guard only, recording that order is unchecked.

  Rows: adversary:14, registry-audit:12.
- **OQ-17. A graph-to-contract subset check** on prohibited handoff references (fv-main:17, coverage:12). A1-2 adopts only the exact-key `HANDOFF_CONTRACT` check. Options: (a) add the subset check with a must-fail regression; (b) the exact-key check alone.
- **OQ-18. Contract-only texts with no source.** The `pr30_ownership` item that names a same-session PR-35 handoff has no replacement text. Nor do the `route_graph_semantics` entries `same_session_phase_continuation` and `pr40_entry`: coverage:13 offers "false or renamed" for the first, and sweep:10 says only "per C-SESSION and C-DISPATCH". Options: (a) texts compiled from C-SESSION and C-DISPATCH in spec §6 and reviewed in E5; (b) wording Nathan gives. Rows: fv-main:32, coverage:13.
- **OQ-19. The 091326.2 alias after the re-point.** A1-6 re-points the overlay, and A1-1 keeps the alias's bytes. Neither says whether `gcfpe-current-direct-handoff-contract.json` stays linked from `change-flow/SKILL.md` and listed in `OPTIONAL_REFERENCES`, or what `validate_gcfpe_current.py` then validates by default. Options:
  - (a) keep it linked as a historical reference, validated by its own pins;
  - (b) unlink it and drop it from `OPTIONAL_REFERENCES`, leaving the file unchanged.

  Rows: fv-rest:2, adversary:10.
- **OQ-20. `glow-hde-pr-development/SKILL.md:121`,** the polling rule. Step 37 targets it, and C-SUB goes before `:112` (pr-relay-graph:9). Options (sweep:19): (a) qualify it to apply only where no subscription delivers the result; (b) keep it verbatim, recorded as deliberate.
- **OQ-21. Secondary asks left open.** Each is adopted or not:
  - C-ART after `:158` or after `:160` (pr-relay-graph:11);
  - the behaviour-case headings for C-DEC, C-LAT and C-SUB that pr-relay-graph:15 says to "consider";
  - registry-audit:11's note that the next postflight restate its check (f).
- **OQ-22. The rows for the `Notion-resident artifact` guard** (registry-audit:6). Options: (a) the 10 step-5 rows; (b) all 55.
- **OQ-23. PR-40's body wording for `D23-E`.** Step 39 gives only PR-40's registry input, and A1-5 rewords its fallback clause. The `D23-E` guard on PR-40 needs the body to carry the observed-merge wording. Options: (a) step 39's sentence with A1-5's predicate substituted, used in both body and registry; (b) wording Nathan gives. Rows: coverage:1, sweep:2, adversary:4, registry-audit:12.

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

Every fixed text that EXECUTE places, in its final form. Precedence: the amendment governs §P's canonical wording and steps where they differ (amendment, *Precedence*); A1-5's C-SUB and C-DISPATCH supersede §P's C-SUB, C-DISPATCH and PART-11 ruling row; the follow-up's texts are its §P *Canonical wording*. A worker who cannot place a text reports it and does not improvise (§P *Canonical wording*). Nothing here is re-authored per prompt.

**Conventions.**
- A code block is the exact string. Hard wraps in the source files are not part of a text: a wrapped line joins the next with one space. C-LAT keeps its blank line and its numbered items on their own lines. Asterisks and backticks are part of the text.
- Phases are the follow-up's *Order* and A1-4: **E1** repository work on the execution branch (graph parts, registry, policy files); **E2** skill work in scratch copies; **E3** bodies computed in memory by the body rules script, which holds these texts and anchor patterns, never body text (A1-4 item 2); **cut-over** lands bodies and Notion control edits after the six packages are installed (A1-4 item 5).
- "Converges on" for a skill line means the text is placed while every kept validator literal on that line stays. The keep/replace/forbid marking per literal is spec §8 (amendment defect 12).
- Line numbers are those of today's installed trees and repository, as the plan and findings cite them.

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

- **Goes:** as the first sentence of the result or output section (the section naming the output artifact) of the 53 bodies whose registry row's `required_literals` contain `NEXT_PROMPT_HANDOFF` (step 8; selector registry-audit:2: PR-35 in, GCFPE-MGMT-10 and PR-50 out; measured 53). In `glow-hde-pr-development`, after SKILL.md:158, not mid-sentence at :155 as step 10 says (pr-relay-graph:11).
- **Placed by:** step 8 (E3, cut-over); step 10 (E2). The step-9 Hub sentence is a separate literal (3.5).
- **Note:** the §P source wraps between "never" and "carries"; the placed text has one space there (registry-audit:4).

**C-HANDOFF** (PART-04; replaces each body's handoff field list).

```text
The block names the exact destination prompt by full name, version and direct Notion URL; the receiving role and session; each input artifact by repository path, with a one-line label; the pull request reference when the receiver continues an existing PR; and, only for a condition those artifacts do not already record, the minimum context it needs. It carries no branch and no commit: an artifact is identified by its versioned filename, and an issued version is never edited. It does not restate history, architecture, decisions, scope, acceptance criteria, workflow rules or artifact contents that the named prompt, canon or files hold. No placeholders, menus, alternate destinations, "above", prior-chat reconstruction or unlinked filenames.
```

- **Goes, bodies:** the same 53 bodies, replacing the handoff field-list paragraph anchored on the sentence containing `NEXT_PROMPT_HANDOFF` (step 13). The replacement keeps the `NEXT_PROMPT_HANDOFF` literal and is made in the same page edit as C-PLACE (fv-main:33). PR-30 step 6 and PR-35's *Required inputs* drop branch, worktree, commit and head as handoff content and keep them as entry-recovery checks (step 13).
- **Goes, skills (field-list clauses only, never whole lines):** `glow-hde-pr-development` SKILL.md:22 (its postpublication-qualification literal stays; pr-relay-graph:5), :82, :133 (pr-relay-graph:6), :162 (its first sentence stays verbatim; pr-relay-graph:6, fv-rest:25); `change-flow` :295, :313; `session-relay-flowmaster` :259, :273, :279 (pr-relay-graph:18); `amthor-workspace-governance-audit` SKILL.md:38, dropping the Notion-resident clause, and `references/interoperability-contracts.md` (registry-audit:13, :14); `tw-flowmaster` :304 and :315 take the relay's new text (sweep:5, A1-6). Step 14.
- **Goes, Notion:** Hub § *Handoff format — required structure*, replacing the 16-section list with C-HANDOFF followed by the step-16 sentence in 3.5 (step 16).
- **Carried as fields, not text:** graph `handoff_contract.required` and `.prohibited` (step 12, E1); contract `transition_contract` flags, set by the regenerator, with `HANDOFF_CONTRACT` becoming an exact-key check (A1-2, E1).
- **Placed by:** 13 (E3, cut-over), 14 (E2), 16 (cut-over), 12 and A1-2 (E1).

**C-PLACE** (PART-05).

```text
The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a few lines naming what was produced and where; the artifact holds the rest.
```

- **Goes:** after the handoff rule in the 53 handoff-roster bodies; the 16 bodies that say the response "contains" the block now say "ends with" (step 18, whose verification counts 53). Skills: `glow-hde-pr-development` :162, appended after the C-HANDOFF clause (pr-relay-graph:6); `change-flow` :295; `session-relay-flowmaster` :279 (step 19). The existing block-shape sentences (one fenced `text` block whose first line is `NEXT_PROMPT_HANDOFF`) stay verbatim (fv-rest:25).
- **Placed by:** 18 (E3, cut-over, same page edit as step 13), 19 (E2). The four `ASK OK?` bodies take the variant in 3.2.

**C-DEC** (PART-06, added to `PR_IMPLEMENTATION_RESULT`).

```text
An *In-flight decisions* section, one row per decision taken without a rescope: what changed, why it was necessary to deliver the approved scope, and what was tested, by test identity and outcome. `NONE` when there were none.
```

- **Goes:** the `PR_IMPLEMENTATION_RESULT` section of PR-30, PR-35 and RS-40 (step 20). In `glow-hde-pr-development`, at SKILL.md:108, which names the result artifact, not at :59 as step 20 says (pr-relay-graph:10).
- **Placed by:** step 20 (bodies E3, cut-over; skill E2).

**C-LAT** (PART-07; PR lane only).

```text
**Material** means a change to the Epic-level commitment: its outcome or objective; approved acceptance criteria; a protected architectural, security, data-model or external-contract boundary; the scope of several planned work units; an accepted dependency or cross-team commitment; or budget, schedule or risk needing Product Owner direction. A planned approach found incomplete, impractical or inferior is not by itself material.

**Decide it during work:**
1. Is it material, as above? Then take the formal rescope route.
2. Otherwise, is it obvious, necessary to deliver the approved scope, and consistent with the Epic's objective and controlling constraints? Then decide it, implement it, test it, and record it under *In-flight decisions*. That holds even if the plan did not anticipate it.
3. Otherwise, do not do it. Record it as a candidate for its owner.
```

- **Goes:** once, in the section that sends findings to RS, in PR-10, PR-20, PR-30, PR-35, PR-40, RS-10, RS-20, DOC-10, DOC-20 and IA-30; in those routing sentences "material boundary" becomes the step-22 literal in 3.5 (step 22). Skills: `glow-hde-pr-development` :65, :128, :135, with the numbered procedure :130-133 intact and `behavior-cases.md`:49 converged (pr-relay-graph:12); `change-flow` :313, :323, :453-454 (step 24; see open question on :313 and :323). OPS-*, QA-*, CL-* and ESC-* are out of scope (step 22).
- **Graph:** step 23's condition wording is superseded by the A1-7 conditions in 3.6.
- **Placed by:** 22 (E3, cut-over), 24 (E2).

**C-VERSION** (PART-12, the release rule). Text unchanged.

```text
A release's membership and each member's current version live in the register and the complete-prompt-set catalog. A member whose body changes gets a successor page at the new version; a member whose body does not change keeps its page, and the register records it in the new release. Bodies carry no release-bound header line.
```

- **Applies from the next release, not to this run** (A1-3). This run edits the 091426.1 bodies in place. The register records each changed member's revision date, which is informational: nothing reads it and it identifies nothing. The contract and skill revisions move, so the bytes stay distinguishable. The contract's `versioned_sibling_successors` stays `true`, because it is true of how 091426.1 was made (A1-2).
- **Goes:** `prompt-body-content-policy.md` :33-34, where `Prompt version:` and `Ecosystem release:` leave the legitimate list and C-VERSION is added (step 41); the Notion register and complete-prompt-set catalog, as the release rule, with a per-member `current_version` column, all `091426.1` (step 44). A related skill literal, `amthor-workspace-governance-audit` SKILL.md:32 narrowed to "each member that received a successor page", is spec §8 (registry-audit:16).
- **Placed by:** 41 (E1), 44 (cut-over).

**C-D22** (PART-13). §P defines it as the `D22` wording of `prompt-corpus-policy.md`, *Amendment*. The text EXECUTE places is step 45's reason:

```text
a path option invites a standing directory; a transient read file is allowed under `D22`
```

- **Goes:** `flowmaster-validate` SKILL.md:55-60 and :231-232, replacing "a file persists, and a persisted corpus is what the policy forbids" (step 45); also `scripts/validate_gcfpe_20260914.py` docstring :2288-2291 and comment :2657-2659, and `scripts/run_gcfpe_20260914_fixtures.py`:726 (fv-main:34). The no-path-option behaviour is kept; only its stated reason changes (fv-main:34).
- **Placed by:** step 45 (E2).

### 3.2 Texts added or amended by Amendment 1

**C-SESSION** (PART-09), amended.

```text
PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. The phases share one `WORK_UNIT_ID`, original Proceed, workspace/worktree, branch, pull request, PR instruction, detailed plan, primary skill authority and recovery lineage; they do not share a session. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
```

- **Changes from §P:** the backticks around PR-30 and PR-35 in the first sentence are dropped, so the kept literal "PR-30 and PR-35 are two phases" matches `change-flow`'s validator (:1020-1021) and `flowmaster-validate`'s `CHANGE_FLOW_CONTRACT` (:2580-2586), which §P's text fails (fv-main:26, fv-rest:17; measured). The last sentence is A1-8's addition, appended.
- **Goes, bodies:** the ~17 bodies stating one shared session, replacing the continuity-list paragraph; readback: "dedicated PR-development session" is absent from every continuity list (step 32).
- **Goes, skills (step 35, sites extended by findings):** `glow-hde-pr-development` description :3, and :10, :22, :27 (pr-relay-graph:2, :4), :53, :55 (pr-relay-graph:1), :82, :100, :141 (sweep:4, coverage:17), :158 (pr-relay-graph:1), :164, and `behavior-cases.md` :7, :11, :13, :17 (pr-relay-graph:15); `change-flow` :275, :301, :303, :307, :365, :453 (fv-rest:19, coverage:15); `session-relay-flowmaster` :283; `flowmaster-validate` SKILL.md :164-165 and :294 (fv-main:34, coverage:15); `amthor-workspace-governance-audit` SKILL.md :40, :41, :43, :47 and `interoperability-contracts.md` :13, :18, :53-54, :68, :96 (registry-audit:13, :14); `tw-flowmaster` :319 and :321, byte-identical to the relay's new lines (sweep:5, A1-6).
- **Also carried by:** PR-35's role in the graph, the contract and the registry (A1-8; 3.4); the GCF-17 successor row, in its own A1-1 wording.
- **Placed by:** 32 (E3, cut-over), 35 (E2).

**C-SUB** (PART-10), A1-5; supersedes §P's C-SUB.

```text
At entry, subscribe to the pull request's activity where the surface provides it, and record the subscription as active only when the tool result confirms that this session receives the pull request's events. Act on review, comment and check events as they arrive. Without an active subscription, `REMOTE_EVIDENCE_PENDING` and its re-entry handoff apply as before. Subscribing is not polling, and it creates no session.
```

- **Goes:** the PR-35 body; RS-40's PR-35 phase (step 37). `glow-hde-pr-development`: its own sentence before SKILL.md:112, which stays verbatim (pr-relay-graph:9); :121 is also in step 37, and its literal is spec §8 (sweep:19).
- **Why it differs from §P:** a subscription counts as active only when the tool confirms this session receives the PR's events (A1-5; sweep:14).
- **Placed by:** 37 (bodies E3, cut-over; skill E2).

**C-DISPATCH** (PART-11), A1-5; supersedes §P's C-DISPATCH and the PART-11 ruling row's launch option.

```text
At `MERGE_PENDING`, return control with the result, including the conditional `PR-40` block for Nathan, which is usable only after he merges and only where no `MERGE_OBSERVED` result was returned for this merge; stay subscribed and do not poll. When the active subscription delivers the merge of the identified PR — a merge Nathan performs — return `MERGE_OBSERVED` with the paste-ready `PR-40` handoff and return control. Nathan creates the PR-40 session and pastes it. The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently. No agent merges, and no session is created by an agent.
```

- **Goes, bodies:** PR-35 and RS-40 (step 39). RS-40 carries it because it resumes the PR-35 phase in the same subscribed PR-35 session and gains `MERGE_OBSERVED` (A1-5).
- **Goes, skills (step 40, sites extended by findings):** `glow-hde-pr-development` :110, appended after the existing sentences, never replacing them (pr-relay-graph:7); :164, removing only the manual-assertion clause and keeping the rescope sentence and PR-40's independent-verification literal (pr-relay-graph:8, coverage:16); `behavior-cases.md`:87 (pr-relay-graph:15, coverage:16); `change-flow` :331, :366, and :455 through the successor GCF-17.LINEAGE row (child C7); `session-relay-flowmaster` :283-285; `tw-flowmaster` :319-321 (sweep:5); `flowmaster-validate` SKILL.md:173 (fv-main:34, coverage:15); `amthor-workspace-governance-audit` SKILL.md:49 and `interoperability-contracts.md`:74, keeping "MERGE_PENDING is historical", PR-40's independent verification and no-merge (registry-audit:13, :14).
- **Placed by:** 39 (E3, cut-over), 40 (E2).

**C-TOP** (A1-8), new.

```text
This prompt runs in a top-level session that Nathan creates, or re-enters by pasting a handoff, and never as a subagent of another session. It may use subagents as workers within its own task. It never creates, starts or schedules another session; it returns control, with the handoff where there is one.
```

- **Goes:** the 54 main-ecosystem bodies, every GCFPE body except GCFPE-MGMT-10, beside the handoff or return rule. For the 53 handoff-roster bodies it is placed with the step-18 edit; PR-50 has no handoff, so it gets a separate edit beside its return rule (A1-8, coverage:27).
- **Wording note:** the last sentence says "starts", not "launches", so the forbidden session-creation guard does not match the canonical text itself (sweep:1; coverage:0; measured below).
- **Placed by:** A1-8, computed at E3, landed at cut-over.

**GCFPE override** (A1-6), new.

```text
For every GCFPE main-ecosystem stage, the core's option to create a fresh session does not apply: this skill never creates, spawns, launches or schedules a session; when no existing authoritative session can do the work, it returns the paste-ready `NEXT_PROMPT_HANDOFF` and stops for Nathan.
```

- **Goes:** `change-flow`, `session-relay-flowmaster` and `tw-flowmaster`, each in its specialization text outside the byte-identical Flowmaster core, which is left unchanged (A1-6; sweep:6). Held in place by `CONTRACT_REQUIRED` entries (A1-6).
- **Placed by:** A1-6, at E2.

**C-PLACE, `ASK OK?` variant** — derived; see open questions. §P gives an instruction, not a text: "In the four bodies that also 'end `ASK OK?`', `ASK OK?` moves to the line immediately before the block." The amendment gives no wording (adversary:14). The derivation keeps C-PLACE verbatim and adds one sentence restating that instruction:

```text
The final response ends with the `NEXT_PROMPT_HANDOFF` block. Anything before it is at most a few lines naming what was produced and where; the artifact holds the rest. `ASK OK?` is the line immediately before the block.
```

- **Goes:** QA-60, QA-80, RS-10 and RS-30, in place of C-PLACE, with the body's `ASK OK?` line moved to the line immediately before the block (step 18).
- **Constraints it meets (measured):** it still matches the proposed placement guard (first pattern below), and it does not reuse "end `ASK OK?`", so the proposed forbidden pattern (second) stays silent (registry-audit:12 and its notes):

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

- **Goes:** every body that carries the single-Proceed sentence, replacing it (C4, which does not enumerate them); `glow-hde-pr-development` :10, :17-18, :27, one combined replacement per line with step 35 at :10 and :27, plus a new required literal taken from it (C6); `change-flow`, as its own sentence after :301, with :313 and :323 verbatim (C7; sweep:22); `amthor-workspace-governance-audit` SKILL.md:44, "one Proceed per plan cycle" (C10).
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

**PR-35 role — not fixed; see open questions.** A1-8: "The role of PR-35 in the graph, the contract and the registry carries the same clause" as C-SESSION's added sentence. One string goes to four places: graph `PR-35.json` `node.receiving_role` (step 30, E1), contract `member_registry['PR-35'].receiving_role` in both copies, set by the regenerator from the graph (A1-2; fv-main:8), and registry PR-35 `session_role`, equal to the graph string verbatim (registry-audit:7). The amendment gives no string. The candidates on record are:

Option (a), the first draft of this amendment, which uses the GCF-17 successor row's phrase "never a subagent of another session" (the phrase coverage:6's proposed role literal requires):

```text
You are the dedicated PR-35 session for one work unit: a top-level session entered from PR-30's handoff, never a subagent of another session. You continue its existing pull request.
```

Option (b), step 30's string followed by A1-8's clause verbatim:

```text
You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
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

**RS-40 role — see open questions.** Graph `RS-40.json` `node.receiving_role` and registry `session_role` (today both "You are the same dedicated PR engineering session for the exact suspended work unit.") must change together (registry-audit:9, coverage:18). The only text on record is registry-audit:9's, offered as an example:

```text
You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.
```

**PR-20 registry input** (C5), as a quoted string:

```text
`PR_WORK_UNIT_LINEAGE_REVIEW` with `REJECT` (`reject_replan`) and its in-scope finding, for a re-plan of the same `WORK_UNIT_ID` in a new dedicated session Nathan seeds
```

**PR-40 registry inputs.** At :3708, "the dedicated PR session identity" becomes (registry-audit:9, coverage:18):

```text
the PR-30 and PR-35 session identities
```

The :3710 input (step 39) and PR-40's PR-35-result input have no final wording; see open questions.

**Governance-audit invariant** (A1-8's semantic invariant, added to the fifth package; wording sweep:25). A bullet in `amthor-workspace-governance-audit` SKILL.md's Alpha-feedback invariants list (:36):

```text
Every main-ecosystem prompt (all but GCFPE-MGMT-10) runs as its own top-level session Nathan creates; none runs as a subagent, forked or workflow agent; none creates, launches or schedules a session; workers within a task are allowed.
```

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

### 3.6 Graph conditions (A1-7, including the follow-up's three rows)

The authority for the full edge objects and insertion positions is `route_sim_final.py`, sha256 `e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26` (A1-7). The 15 condition strings, read from its constants, each equal the A1-7 table's *after* cell verbatim (measured). Keys name the part and branch:

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

Placed by: steps 23, 31 and 38 as amended by A1-7, and child C1 and C2, at E1. The `NATHAN_PROCEED` condition exists in two copies in `global.json`, `_other_edges` and `boundary_transitions`, and both take the same string (child C2). The GCF-17, GCF-17.LINEAGE and GCF-14 successor text is A1-1's table and is not repeated here.

### 3.7 Check

A scratch script (`/tmp/claude-0/spec/section3/check.py`, run with `PYTHONDONTWRITEBYTECODE=1`) read the texts out of the plan, amendment and follow-up copies (`extract.py`), not from this section. It read the forbidden list from the installed `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py` (:91-103, 11 entries) and applied it as that validator does: a case-insensitive substring test.

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

Informative, since spec §7 governs the adopted guard values: each guard pattern the findings propose was run against these texts. Every required pattern matched its home text and no other canonical text: C-ART, C-DEC, C-LAT (two patterns), C-PLACE and its variant, C-SESSION (two), C-TOP, C-SUB, C-DISPATCH (two) and C-PR20-ENTRY. Every proposed forbidden pattern was silent on all 59 texts and on the C-PLACE + C-HANDOFF, C-PLACE + C-SESSION and C-PLACE + C-HANDOFF + C-SESSION + C-TOP combinations. The only matches came from the first draft's withdrawn session-creation pattern, below, on two skill texts: the A1-6 override and the governance-audit invariant. Neither is body text; see open question 15.

```text
\b(?:launch|spawn|auto-?start)\w*\b[^.\n]{0,60}\bsession\b
```

### 3.8 Open questions

Each is left open here. The compiled value, where one is shown, is marked.

1. **ASK OK? variant wording.** §P step 18 gives an instruction, not a text, and the amendment gives none (adversary:14). Options: (a) the derived text in 3.2, which is C-PLACE verbatim plus "`ASK OK?` is the line immediately before the block."; (b) wording Nathan gives. The ordering guard and its must-fail regression derive from whichever is chosen (adversary:14).
2. **C-SESSION provenance.** Amendment 1 does not itself state the backtick drop or where A1-8's sentence goes. The drop is option (a) of fv-main:26 and fv-rest:17, which the superseded first draft adopted at step 32; "gains" is read as appended. Backticks: (a) drop them (compiled); (b) keep §P's backticks and change both validator markers (`change-flow` validator :1020-1021, `flowmaster-validate` :2580-2586). Position: (a) last sentence (compiled); (b) after the third sentence.
3. **PR-35 role string** (A1-8, steps 30 and 33). A1-8 says the role "carries the same clause" but gives no string. Options: (a) the first-draft string in 3.4; (b) step 30's string followed by the A1-8 clause verbatim; (c) another. Only (a) contains coverage:6's proposed role literal "never a subagent of another session"; only (b) carries the clause verbatim.
4. **RS-40 role** (registry-audit:9, coverage:18). The only text on record is registry-audit:9's example. Options: (a) adopt it verbatim for graph and registry; (b) another. Also open: whether RS-40's registry `creator_role`, today "the same dedicated PR engineering session for the exact suspended work unit.", changes with it. No finding covers it.
5. **PR-20 and PR-40 roles** (sweep:15; the D23 clarification's *Guard* names "the graph role and the registry role for each affected prompt"). Options: (a) append C-TOP's top-level clause to both prompts' graph `receiving_role` and registry `session_role` as identical strings; (b) a D23 successor note saying body-level C-TOP carries the rule and those roles stay. The amendment is silent.
6. **PR-40 registry input :3710 and the PR-40 body's entry wording** (step 39, A1-5, coverage:3, coverage:18). Step 39's "the observed merge event, or Nathan's assertion where no subscription existed" and the preflight's longer form both use "where no subscription existed". That conflicts with A1-5's single predicate, "only where no `MERGE_OBSERVED` result was returned for this merge". PR-40's PR-35-result input ("The complete PR-35 result whose earlier MERGE_PENDING is historical pre-merge evidence") has no wording for accepting `MERGE_OBSERVED`. No text is given for the PR-40 body's entry either, although the proposed D23-E guard requires it to contain "observed merge event" (registry-audit:12). Options: (a) substitute A1-5's predicate into step 39's sentence and reuse that sentence in the body; (b) wording Nathan gives.
7. **C-VERSION's effective date at its sites** (A1-3; steps 41 and 44). A1-3 applies C-VERSION from the next release, but gives no qualifier for the placed text. Options: (a) place it verbatim and record "from the next release" only in `D23` and §E; (b) add a qualifier sentence at both sites (no wording given).
8. **C-D22 at the other sites** (step 45, fv-main:34). Step 45 gives one old-to-new pair. The other sites word the reason differently: "because a file persists" at SKILL.md:59; "a file would persist, and a persisted corpus is what the policy forbids" at `validate_gcfpe_20260914.py`:2658; "No path option: a file would persist." at the runner's :726. The docstring at :2288-2291 has no persistence clause. Options: (a) the C-D22 reason verbatim in place of each site's reason clause; (b) per-site wording in §8.
9. **`execution-and-delegation-model.md` scope line.** The `D23` clarification says the file "gains a scope line: its subagents are maintenance workers, and never a way to run a main-ecosystem prompt". Amendment 1 names no step or wording for it; the superseded first draft had one (N5). Options: (a) place `D23`'s phrase; (b) the first draft's N5 text; (c) leave it for a later Modification and record that in §E.
10. **C-PLACE body count** (step 18). The target column says "55 bodies (block present)"; the verification says 53. The registry roster measures 53: PR-35 in, GCFPE-MGMT-10 and PR-50 out. GCFPE-MGMT-10 has handoff branches (registry-audit:2) but is outside the main ecosystem. Options: (a) 53 (compiled); (b) 54 with GCFPE-MGMT-10.
11. **C-HANDOFF's "an issued version is never edited"** against A1-3's in-place edit of 091426.1. The registry-audit notes raise the two together; A1-3 answers only C-VERSION. Options: (a) read it as scoped to the handoff's input artifacts and keep the text (compiled unchanged); (b) qualify the sentence.
12. **`change-flow` :313 and :323.** Step 14 (C-HANDOFF, :313) and step 24 (C-LAT, :313 and :323) converge on these lines, but child C7 and sweep:22 keep them verbatim. Options: (a) keep both lines verbatim and place C-LAT and C-HANDOFF beside them; (b) edit only their field-list and threshold clauses, keeping the Proceed, accepted-final and PR-50 prohibitions.
13. **Relay :624** (`NOTION_REFERENCE` is versionless; coverage:23, pr-relay-graph:18). Options: (a) add it to step 14 under C-HANDOFF; (b) record it in §E as out of scope, with a reason. The amendment is silent.
14. **C-PROCEED's body set** (C4). C4 replaces "the single-Proceed sentence in the bodies that carry it" but does not enumerate them, since the bodies were not read. Options: (a) the rules script anchors on that sentence and reports every body it edits; (b) a list is added to the spec before E3.
15. **Skill texts and session-creation guards.** The A1-6 override says "spawns, launches or schedules a session", and the governance-audit invariant (sweep:25) says "creates, launches or schedules a session". C-TOP was reworded from "launches" to "starts" so that a session-creation guard would not match it (sweep:1). The withdrawn broad pattern matches both skill texts (3.7). Options: (a) no session-creation pattern applies to skill text, so no change; (b) if spec §7 applies one to skill text (for example `CONTRACT_FORBIDDEN` for the relay or `tw-flowmaster`), test it against both texts, or reword them as C-TOP was.

## §4 Graph transforms

This section lists every edit EXECUTE makes in `/home/user/glow-hdengine-v2/docs/graph/parts`. It compiles:
- original steps 12, 23, 29, 30, 31, 34 and 38 (§P);
- amendment rulings A1-1, A1-2, A1-5, A1-7 and A1-8;
- the follow-up plan's C1 and C2;
- the findings cited on each item.

It makes no decision. Where no source gives a literal, the item says so and points to an open question, numbered OQ-n in §4.12.

**Files edited:** `global.json` and seven prompt parts, `PR-35.json`, `RS-40.json`, `PR-40.json`, `PR-20.json`, `PR-30.json`, `PR-10.json` and `DOC-10.json`. The other 48 prompt parts are not edited.

### 4.1 Rules for the transform

1. **Scripted, never by hand.** Every edit is made by a scripted JSON transform (§P step conventions).
2. **Serialization.** Every file the transform writes is UTF-8, in exactly this form:
   ```
   json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
   ```
   Measured: this is the simulation's `save()`, and `graph_parts.py split` uses the same writer. It reproduces all 56 current part files byte for byte.
3. **Authority.** A1-7 makes the simulation's sha256 "the authority for the full edge objects and insertion positions". So the routing portion of the final parts must equal the simulation's `parts_new` output exactly. V3 in §4.10 checks this. The routing digest alone does not, as the negative controls in §4.10 show.
4. **Completeness.** A1-7 calls its table "the complete diff" of routing, so no route condition outside §4.6 changes. §4.5 lists the conditions and roles that stay for that reason.
5. **Where the parts land.** Repository work goes on the execution branch (A1-4, step 1). For the stage, see OQ-1.

### 4.2 The simulation, reproduced

The authority file is `/tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/route_sim_final.py`. Measured sha256:
```
e0854a5561758d9c89f43beedde902c325332bcb6b90e2feea002c65b1c3ab26
```
What it does:
1. It copies the parts.
2. It applies the A1-7 conditions, the child's in-place re-target and both `MERGE_OBSERVED` additions.
3. It builds base and new graphs with `glow-graph-contract/scripts/graph_parts.py build`.
4. It computes `routing_surface` with `flowmaster-validate/scripts/validate_gcfpe_20260914.py`.

It was rerun on a copy. The copy differs only at line 10, the `W` path:
```
cp /tmp/claude-0/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/scratchpad/exec/route_sim_final.py /tmp/claude-0/spec/s4-graph/route_sim_final.copy.py
sed -i 's#^W = ".*"$#W = "/tmp/claude-0/spec/s4-graph/routesim"#' /tmp/claude-0/spec/s4-graph/route_sim_final.copy.py
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/claude-0/spec/s4-graph/route_sim_final.copy.py
```
Output, measured 2026-09-23, with exit 0 and no builder `WARNING` lines:
```
BASE build: 55 nodes, 227 edges, 55 state_routes | embedded JSON 569835 bytes  sha256 90021eb7a38c852b0cd9d78b879e4ce991048581acf7c1d92967644335079223 | validation PASS -> ('7380cd14430777675f1e8b2cdfa4a0da', 282)
NEW  build: 55 nodes, 229 edges, 55 state_routes | embedded JSON 574175 bytes  sha256 b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7 | validation PASS -> ('fecc319bdd4ce7ee6201cb77d7231861', 284)
state_routes keys changed: ['DOC-10', 'PR-10', 'PR-20', 'PR-30', 'PR-35', 'PR-40', 'RS-40']
edge count 227 -> 229
```
**Reproduced exactly:** routing surface `fecc319bdd4ce7ee6201cb77d7231861` over 284 rows, 229 edges, and an embedded graph of 574175 bytes with sha256 `b1911cf5…`.

**Row accounting.** This was measured by recomputing the `routing_surface` rows of both builds. There are 282 rows before and 284 after:
- 20 rows exist only before: 13 edge rows and 7 state-route rows.
- 22 rows exist only after: 15 edge rows (13 changed edges and 2 new ones) and 7 state-route rows.
- The 7 state-route rows belong to DOC-10, PR-10, PR-20, PR-30, PR-35, PR-40 and RS-40.

A1-7's prose says "16 route rows change or are added", but its own table has 15 rows and the measurement gives 15 (OQ-2). The digest reproduces, so A1-7's stop rule is not triggered.

**What 574 175 bytes / `b1911cf5…` identifies.** It is the routing-only build. The simulation applies none of the non-routing edits: G5–G16 in §4.3, and P35-6 to P35-9 and R40-8 in §4.4. Those edits leave the digest and the edge count unchanged but change the embedded bytes, for two reasons:
- `routing_surface` reads only `edges` and `state_routes`;
- the builder derives `state_routes` only from the edges, `state_route_order` and `state_routes_extra`, which is empty in every part.

Measured: adding only the fixed-value PART-09 edits (G8–G10, P35-6, P35-8 and P35-9) gives 229 edges and 574112 bytes, with sha256 `26093c3a41581979f5b4fc617a8e72d05ca6873997e47fb63bebed3b6189078c`. The digest stays `fecc319b…`/284. The final graph's bytes and sha256 are therefore measured from the final build and enter the pin chain (another section). They will not be 574175 / `b1911cf5…` (OQ-3).

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

**G5. `handoff_contract.required`.** Source: step 12. A1-2 governs the contract's `transition_contract`, not this list, so step 12 stands for it. Step 12 replaces the whole list:
> `required` becomes: prompt full name/version/URL; receiving role and session; artifact repository paths with labels; PR reference when continuing a PR; exceptional context only.

So the three items "Epic/change and work unit", "status, completed work, …" and "next action and expected output" leave the list (pr-relay-graph:31). No source fixes the five exact strings (OQ-4). The current value, for reference:
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

**G6. `handoff_contract.prohibited`.** Source: step 12, which adds these three literals and keeps the nine current entries:
```
branch
commit
restated artifact content
```
No source states their position in the list (OQ-4).

**G7. The other `handoff_contract` keys stay unchanged:**
- `complete_paste_ready_prompt` stays `true` (step 12).
- `actual_branch_only` `true`, `fence_language` `"text"`, `first_line` `"NEXT_PROMPT_HANDOFF"` and both block counts are kept (pr-relay-graph:31).

`GRAPH_HANDOFF_CONTRACT_MISMATCH` reads only these keys, so G5 and G6 do not affect graph–contract parity. The contract side belongs to A1-2 and another section (fv-main:17, fv-rest:13, coverage:12, adversary:3).

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
- **G10:** `cross_session_route` goes from 0 to 1 (fv-rest:15, pr-relay-graph:28). sweep:11 retires fv-main:2's opposite fixture.
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

**G11. `proofs["PR-35_same_r1_row_as_PR-30"]` stays `true`** (step 29: "same R1 row, new session"). `pr_continuity_contract.r1_row` stays `"GCF-17"`.

**G12. `post_merge_three_event_contract.direct_PR35_to_PR40_automatic_edge` stays `false`** (A1-5). This supersedes step 38's "= true" and the findings that followed it: fv-main:13, registry-audit:10 and pr-relay-graph:27 (sweep:11).

**G13. The rest of the post-merge contract stays unchanged:**
- `agent_merge_authorized` stays `false`;
- `event_1` and `event_3` are unchanged (fv-main:13; A1-5 C-DISPATCH: "No agent merges", and "`PR-40` still verifies the merged state and landed lineage independently").

**G14. `post_merge_three_event_contract.event_2`.** A1-2: "`event_2` becomes 'observed or asserted'".
- The `fact` and `time` literals are sweep:10's, the only ones the record gives.
- `actor` is unchanged (fv-main:13).
- `value` is unchanged; no source changes it.

Final object:
```json
{
  "actor": "Nathan / Product Owner",
  "fact": "product_owner_manual_merge_observed_or_asserted",
  "time": "observed by the subscribed PR-35 session, else asserted at the later PR-40 invocation",
  "value": true
}
```
The A1-2 regenerator copies the whole `post_merge_three_event_contract` into the contract (fv-main:10; `GRAPH_POST_MERGE_CONTRACT_MISMATCH`). The validator literal for `event_2.fact` belongs to another section (fv-main:13).

**G15. The observed-merge edge record.** A1-5: "The observed-merge edge is recorded inside `post_merge_three_event_contract`." sweep:10 names the key `pr35_observed_merge_edge` and places it in both the graph and the contract. Nothing more is specified:
- no source gives its content;
- A1-5 says "edge", singular, while the graph gains two observed-merge edges (E4 and E5).

See OQ-5. The record is outside the routing digest.

**G16. `protected_identities.r1_oracle_sha256`.** Source: A1-1, under which the live surfaces re-point to the successor; also fv-main:18, pr-relay-graph:30 and adversary:7.
- **Value:** the sha256 of the successor oracle file `flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json`, as finally written.
- **When:** it cannot be computed until that file exists. It is taken in the pin order matrix → oracle → runtime map → graph → contract → profile → literals → fixtures → `SKILL_TREE_SHA256` (adversary:7 (d)).
- **The oracle is computed once,** with all three changed rows: GCF-17, GCF-17.LINEAGE and GCF-14 (A1-1, child C3). The GCF-15 in pr-relay-graph:30 is the error the decision record's `D23` correction fixes.

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
- `_other_state_vocabularies`, including `PR_RETURN_PHASE`. Step 31's "RS-40's `PR_RETURN_PHASE: PR-35` resumes in the PR-35 session" is carried by the RS-40 conditions in E14 and E15.
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
- **P35-7. `node.receiving_role`.** Step 30 gives:
  ```
  You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request.
  ```
  A1-8 adds: "The role of PR-35 in the graph, the contract and the registry carries the same clause", that is, C-SESSION's added clause:
  ```
  PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.
  ```
  No source gives the combined string (OQ-6). Whatever it is:
  - the registry's PR-35 `session_role` must equal it verbatim (registry-audit:7);
  - the contract's `member_registry["PR-35"].receiving_role` is copied from it (fv-main:8).
- **P35-8.** `node.adds_session` goes from `false` to `true` (step 30).
- **P35-9.** `node.cross_session_route` goes from `false` to `true` (fv-rest:15, pr-relay-graph:28).
- **Unchanged:**
  - `r1_mapping` stays `"GCF-17"`;
  - the other `adds_*` flags stay `false`;
  - `title`, `candidate_url` and `output_artifacts`;
  - `native_function` (OQ-7).

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
- **R40-8. `node.receiving_role`.** Its value today, which C-SESSION makes untrue for the PR-35 phase:
  ```
  You are the same dedicated PR engineering session for the exact suspended work unit.
  ```
  Step 31 targets RS-40's PR-35 phase. registry-audit:9 asks for identical graph and registry strings and proposes, "for example":
  ```
  You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35.
  ```
  The amendment gives no text (coverage:18). See OQ-8.
- **Unchanged:** `session_class` `"DEDICATED_ONE_OFF"`, `predecessor_union_destinations`, and every other branch.

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
  - `node.receiving_role` (OQ-9);
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
- **Unchanged:** `node.receiving_role` (OQ-9).

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
- The `MERGE_OBSERVED` vocabulary order is A1-5's single ordered vocabulary (sweep:3, adversary:9).
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
- **What the collision is.** 128 and 129 are also entries of `_other_edge_indices`, which no edge carries. That is the collision: with the declared list, not with a placed edge. In the new build all 229 placed edges have distinct indices. adversary:12 reports 135, which `OPS-10`'s first edge carries. The builder never assigns 135, because its counter does not start at max(`_other_edge_indices`)+1 (OQ-10).
- **The digest is unaffected either way,** because `routing_surface` sorts its rows.
- **Placement still matters.** It changes the embedded bytes, and the order of the contract's `route_edges`, which the regenerator copies. Measured: giving the PR-35 edge an explicit index of 235 (N3), or inserting it at `edges[0]` (N4), leaves the digest at `fecc319b…`/284 but changes the graph sha256. This is why V3 compares the parts with the simulation.
- **Fixing the builder is out of scope** (amendment, "Noticed, not in scope").

### 4.9 Order of operations

1. **One transform makes the independent edits,** in any order: G1–G14 and G17, and every item in §4.4 except P35-7 and R40-8. G15, P35-7 and R40-8 follow once their literals are settled (OQ-5, OQ-6, OQ-8).
2. **G16 waits for the successor oracle file** and follows the pin order (adversary:7).
3. **One final build.** Its embedded JSON block plus one LF becomes the bundled graph in both skills, and the pin chain continues from it (fv-main:16, fv-rest:10, pr-relay-graph:20; the pin-chain section). The A1-2 contract regenerator reads the same build, and the A1-2 registry deriver reads the same parts.

### 4.10 Verification

**V1. Build to scratch, never into the repository.**
```
PYTHONDONTWRITEBYTECODE=1 python3 /root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502/glow-graph-contract/scripts/graph_parts.py build <execution-worktree>/docs/graph/parts <scratch>/graph.md
```
It must print `55 nodes, 229 edges, 55 state_routes`, no `WARNING` line and `validation PASS`. The builder's endpoint check always passes, so this shows only that the parts assemble (pr-relay-graph:23). Parity with the contract is an E4 item (another section).

**V2. Routing digest.** Take the embedded JSON block of the V1 build and run `routing_surface({"route_edges": edges, "state_routes": state_routes})` from a scratch copy of `flowmaster-validate/scripts`. It must return:
```
('fecc319bdd4ce7ee6201cb77d7231861', 284)
```

**V3. Equality with the simulation.** Rerun the simulation copy as in §4.2. Every final part file must equal the simulation's `parts_new` file, except at exactly the JSON paths below. After only the routing transform, the eight changed files hash to the checkpoint values that follow.
```
global.json
  $.handoff_contract.required
  $.handoff_contract.prohibited
  $.pr_continuity_contract.shared_exactly_one
  $.pr_continuity_contract.adds.session
  $.pr_continuity_contract.adds.cross_session_route
  $.post_merge_three_event_contract.event_2.fact
  $.post_merge_three_event_contract.event_2.time
  $.post_merge_three_event_contract.<observed-merge record key>   (OQ-5)
  $.protected_identities.r1_oracle_sha256
prompts/PR-35.json
  $.node.session_class
  $.node.receiving_role
  $.node.adds_session
  $.node.cross_session_route
  $.node.native_function          (only if OQ-7 is answered "edit")
prompts/RS-40.json
  $.node.receiving_role           (only if OQ-8 is answered "edit")
prompts/PR-20.json, prompts/PR-40.json
  $.node.receiving_role           (only if OQ-9 is answered (a))
every other path of all 56 files: equal to parts_new
```
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
DOC-10, PR-10 and PR-30 keep these simulation hashes in the final parts. PR-20 and PR-40 keep them too, unless OQ-9 is answered (a).

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
Step 12's "`closure.py` unchanged for all prompts" holds for step 12 alone, because `closure.py` reads no `global.json` key. It does not hold for the whole transform.

**Negative controls, measured on copies of the simulation's `parts_new`.** Each shows which check catches which omission:
```
N1  PR-40 state_route_order entry not renamed     digest 70c9189ceadedf1f4f60a61a38906924/284, no builder warning   -> caught by V2
N2  boundary_transitions copies left unedited     digest fecc319b.../284 unchanged; 574093 bytes                    -> caught by V3 and V4, not by V1 or V2
N3  new PR-35 edge given edge_indices entry 235   digest unchanged; sha256 c1fbb70023742abe...                      -> caught by V3, not by V1 or V2
N4  new PR-35 edge inserted at edges[0]           digest unchanged; sha256 8c6f4f468ed9745b...                      -> caught by V3, not by V1 or V2
```

### 4.11 Findings placed in this section

- **Applied here.**
  - Field names and values: fv-main:2 (graph half), fv-rest:15, pr-relay-graph:28.
  - The PR-35 node's graph half: fv-main:8.
  - Rename and placement: pr-relay-graph:24, pr-relay-graph:25 (in-place re-target; "235 and above" superseded by the simulation).
  - The two copies and PR-20: pr-relay-graph:26, fv-rest:28.
  - The added PART-07 conditions, with DOC-20 unchanged: pr-relay-graph:29.
  - The graph's pin site, computed once after the oracle, with GCF-15 corrected to GCF-17.LINEAGE and GCF-14: fv-main:18, pr-relay-graph:30, adversary:7.
  - The ordered vocabulary: sweep:3, adversary:9.
  - RS-40 mirrored: sweep:0, coverage:2.
  - `event_2` and the record's key: sweep:10.
  - The simulation as authority, and the placement note: adversary:12.
  - Row accounting: coverage:25.
  - Step 12's graph half: pr-relay-graph:31.
- **Superseded, with the ruling that governs.**
  - `direct_PR35_to_PR40_automatic_edge` becoming `true` in fv-main:13, pr-relay-graph:27 and registry-audit:10: A1-5, via sweep:11.
  - The 281/282-row and 283-row figures in fv-main:9 and sweep:0: A1-7's `fecc319b…`/284.
  - pr-relay-graph:27's DOC-20.json:151 edit: A1-5.
- **Human re-pin.** fv-rest:14 and fv-main:9 (by the pin's own rule, a human re-pins it after reading the diff): the diff is A1-7, reproduced in §4.2.
- **Scoped here.** The grep-scope part of fv-main:21: the graph's single pin site moves, and historical files keep `52807e58…`.
- **Weak gate recorded.** pr-relay-graph:23: V1 counts as assembly only.
- **Left open.** Role text: registry-audit:7 and coverage:6 (OQ-6), registry-audit:9 and coverage:18 (OQ-8), sweep:15 (OQ-9).
- **Cross-referenced to other sections, not placed here.**
  - Contract regeneration and parity: fv-main:4, fv-main:10, fv-main:17, fv-rest:12, fv-rest:13, pr-relay-graph:21, coverage:12, adversary:2, adversary:3.
  - Bundled graph and pin chain: fv-main:16, fv-rest:10, pr-relay-graph:20.
  - Validator literals: fv-main:3, fv-main:11, fv-main:12, fv-main:19, fv-rest:20, fv-rest:21.
  - Registry: registry-audit:10, registry-audit:12.

### 4.12 Open questions

These are listed in full in this section's `open_questions`. In short:
- **OQ-1:** the stage for the graph edits.
- **OQ-2:** the row count, 16 or 15.
- **OQ-3:** the final graph identity against `b1911cf5…`.
- **OQ-4:** the `handoff_contract` literals.
- **OQ-5:** the observed-merge record.
- **OQ-6:** the PR-35 role string.
- **OQ-7:** PR-35's `native_function`.
- **OQ-8:** the RS-40 role.
- **OQ-9:** the PR-20 and PR-40 roles.
- **OQ-10:** the amendment's collision wording.

## §5 Successor R1 oracle

This section compiles A1-1 together with child step C3 and the `D23` correction ("D23-F names the wrong R1 row"). It makes no decision of its own. Where A1-1 is silent, the section points to an open question (OQ-n in this section's record). Line numbers refer to today's installed tree, the §2 baseline. Values marked **PROTOTYPE** were produced on scratch copies under `/tmp/claude-0/spec/s5/`. EXECUTE recomputes every one of them.

### 5.1 The three files (A1-1)

```
flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json        successor oracle
change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json    successor runtime map
flowmaster-validate/references/r1-successor-source-20260923.md                         successor source matrix
```

- The matrix ships in the `flowmaster-validate` package, so `SKILL_TREE_SHA256` covers it. The repository keeps a byte-identical copy (A1-1). Where that copy lives is OQ-6.
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
   - `authority`, by additions only (§5.5);
   - the ten row fields below;
   - then `source_row_sha256` of the three changed rows (§5.4).
3. Copy everything else verbatim:
   - the top-level keys `schema_version`, `generated_for_run`, `coverage`, `special_destinations`, `external_inputs`, `terminal_outputs`, `prohibited_active_patterns` and `required_global_tokens` (but see OQ-2);
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

Two readings of the A1-1 table are applied here. Both are listed as OQ-4 because each fixes a digest:
- **The "…" in the two `failure_stop_condition` cells stands for today's unchanged prefix.** The table's "today" column uses the same "…" in front of the exact tail of today's value.
- **GCF-14's "… plus" appends `pr_work_unit_lineage_review` as the last item.**

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

**Measured result (prototype).**
- 46 rows: 26 CORE and 20 MATERIAL. Every row has exactly the 12 fields that FMV-ORACLE-006 requires.
- The only differences from the historical oracle are `profile_id`, `authority`, and these ten row fields:
  - GCF-14: `consumes`, `source_row_sha256`;
  - GCF-17: `name`, `actor`, `session`, `failure_stop_condition`, `source_row_sha256`;
  - GCF-17.LINEAGE: `next`, `failure_stop_condition`, `source_row_sha256`.

### 5.4 The successor source matrix and its digest formula (A1-1; adversary:8; coverage:10)

**Format.**
- The matrix holds one fenced JSON block for each successor row, three in all: GCF-14, GCF-17 and GCF-17.LINEAGE.
- **Each block has exactly 12 keys:**
  - the row's 11 content fields, which are the 12 row fields minus `source_row_sha256` (`id` is one of the 11);
  - `supersedes_source_row_sha256`, the historical row's digest.
- The file has no other JSON fence.
- The prose, the fence delimiter and the block serialization affect only the matrix digest and are open (OQ-5). So is whether the matrix also displays each computed row digest.

**Row digest formula (A1-1).** Its value is written into the successor oracle row's `source_row_sha256`:

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

**The three blocks.** Their content is compiled. Each `supersedes_source_row_sha256` is the historical digest. Only the layout is PROTOTYPE.

```json
{
  "id": "GCF-14",
  "partition": "CORE",
  "name": "Dedicated PR session creates the per-PR Implementation Plan",
  "change_class": "PR",
  "actor": "Dedicated PR session",
  "session": "One new work-unit session bound to one planned PR work unit; it must later implement that same unit.",
  "consumes": ["pr_instruction", "approved_implementation_plan_lineage", "current_repository", "pr_work_unit_lineage_review"],
  "produces": ["per_pr_implementation_plan"],
  "next": ["GCF-15"],
  "approval_contract": "The PR session authors; the Product Owner later approves only by running Proceed.",
  "failure_stop_condition": "STOP_PR_INSTRUCTION_OR_REPOSITORY_CONFLICT, STOP_SCOPE_EXPANSION, or STOP_PLAN_INCOMPLETE; recovery owner: same PR session/IA for upstream scope.",
  "supersedes_source_row_sha256": "4f033c4b644dedc5589bcb3fb2a7bdec67e9ff457907f3733c101db2168f2767"
}
```

```json
{
  "id": "GCF-17",
  "partition": "CORE",
  "name": "Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session",
  "change_class": "PR",
  "actor": "Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)",
  "session": "PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session.",
  "consumes": ["per_pr_authorized_execution_state", "pr_implementation_proceed_invocation", "pr_instruction", "current_repository"],
  "produces": ["pr_or_ordered_lineage", "implementation_result_evidence"],
  "next": ["GCF-17.LINEAGE", "GCF-17.RESCOPE", "GCF-19", "GCF-20"],
  "approval_contract": "Proceed already supplied PO runtime approval. Normal repository review/evidence follows; no new PO approval binding is created.",
  "failure_stop_condition": "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: the phase's own PR session/IA rescope.",
  "supersedes_source_row_sha256": "a2b761a9bf4328cbac51afd5312fcc13b55178ea5c52d6a213678396269e8043"
}
```

```json
{
  "id": "GCF-17.LINEAGE",
  "partition": "MATERIAL_BRANCH_LOOP_OR_UTILITY",
  "name": "PR Work-Unit Lineage Review",
  "change_class": "PR",
  "actor": "Responsible PR review chain",
  "session": "Review context bound to one planned work unit and its complete ordered PR lineage.",
  "consumes": ["pr_instruction", "per_pr_implementation_plan", "pr_implementation_proceed_invocation", "pr_or_ordered_lineage", "implementation_result_evidence"],
  "produces": ["pr_work_unit_lineage_review"],
  "next": ["GCF-14", "GCF-19", "GCF-20"],
  "approval_contract": "Review/acceptance is evidence-based and not a new Product Owner implementation approval.",
  "failure_stop_condition": "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA.",
  "supersedes_source_row_sha256": "46e1c8d0a127afb4851f9945afd4f7d6c607e48936ea1206ef27ca9e8b1c2061"
}
```

### 5.5 The authority block (A1-1; adversary:7(b); coverage:10; fv-rest:6)

**Kept verbatim** under the copy rule:

```json
"r1_source_manifest_library_id": "libfile_e66c0851b3d88191a6d3e39e34e987c6",
"r1_contract_matrix_library_id": "libfile_9caa654f4a648191bb970b2f32970f22",
"r1_contract_matrix_sha256": "faa7fb7d77066cc491bde957b6d2f7d3255c74833936e3952f97873da27ea2f1",
"r1_frozen_snapshot_sha256": "5a6d89ed366f467ee75a5c71d23bf1a613dc79bb4d56791e812e20d53e53db67",
"r1_verdict": "R1_CANONICAL_TRUTH_LOCK_PASS"
```

The original matrix digest `faa7fb7d…` is kept, scoped to the 43 unchanged rows (A1-1). So `EXPECTED_R1_MATRIX_SHA256` and FMV-ORACLE-003 do not move. How the scope is expressed is OQ-3.

**Added** (A1-1). The first two key names come from adversary:7. The third key is unnamed (OQ-3). The prototype appends all three after the kept keys.

```json
"successor_source_matrix_sha256": "<sha256 of the bytes of r1-successor-source-20260923.md>",
"successor_rows": ["GCF-14", "GCF-17", "GCF-17.LINEAGE"],
"<OQ-3 key>": "D23-D, D23-F, Product Owner 2026-09-23"
```

The row binding lives at authority level because FMV-ORACLE-006 forbids a 13th row field (coverage:10; fv-rest:6). Because the runtime map projects `authority`, the map carries these keys too.

### 5.6 The runtime-map successor (A1-1; fv-rest:1; fv-main:20)

**The map is the oracle projection** that FMV-GCF-ROW-001 and FMV-GCF-MAP-005 compare against (`validate_flowmaster.py:732-760`). It is built in this key order and serialized with the §5.3 recipe:

```python
{key: oracle[key] for key in ("profile_id", "authority", "coverage", "runtime_rows")}
```

- **Measured:** today's map bytes equal this projection of today's oracle, serialized with the §5.3 recipe.
- **It is always regenerated from the successor oracle,** never edited by hand.
- **Enforcement:** FMV-GCF-ROW-001 covers the rows, FMV-GCF-MAP-005 covers `profile_id`, `authority` and `coverage`, and FMV-GCF-MAP-006 covers the digest.
- **Its digest does not depend on OQ-2,** because `required_global_tokens` is not projected (measured).

### 5.7 Checks

**Existing checks whose value moves and whose meaning stays** (fv-rest:0; fv-rest:4; fv-main:18):
- FMV-ORACLE-007, the successor oracle digest;
- FMV-ORACLE-002, the profile id;
- FMV-ORACLE-003, `faa7fb7d…`, which does not change;
- FMV-ORACLE-004 and -005, 46/26/20;
- FMV-ORACLE-006, the 12 fields;
- FMV-GCF-MAP-006, FMV-GCF-ROW-001, FMV-GCF-MAP-005 and FMV-GCF-INTERFACE-001 (see OQ-2);
- PROFILE_PROTECTED_IDENTITIES, GRAPH_PROTECTED_IDENTITIES and PROTECTED_IDENTITIES;
- R1_RUNTIME_MAP_IDENTITY, in both `validate_gcfpe_20260914.py` and `validate_gcfpe_current.py`.

**New checks**, in `validate_flowmaster.py` and run by the default suite (A1-1: "the suite goes on verifying the historical files' digests"; adversary:7(b); sweep:7).
- N2 needs the change-flow directory, which `validate_change_flow_contract` has.
- The others need the flowmaster-validate directory, which `load_change_oracle` has.
- **Codes are open (OQ-1).** N1–N9 are placeholders.

- **N1 — historical oracle digest** (A1-1; sweep:7, which names the constant `HISTORICAL_ORACLE_SHA256`). The file `flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json` must hash to `52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e`.
- **N2 — historical runtime-map digest** (A1-1; adversary:7(b)). The file `change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json` must hash to `5574666e5975c104ccf13e77a13d94e0d16f37af37de7eb26d7e0f7b00f45b0e`.
- **N3 — matrix digest** (A1-1; adversary:8). The sha256 of the matrix file's bytes must equal `authority.successor_source_matrix_sha256`.
- **N4 — successor row list** (coverage:10; adversary:7(b)). `authority.successor_rows` must equal the set pinned in the validator, `GCF-14`, `GCF-17` and `GCF-17.LINEAGE`, with no duplicates. This pinned set is what makes the count of kept rows exactly 43. Whether list order is compared is part of OQ-3.
- **N5 — matrix shape** (adversary:8). The file must hold exactly three JSON blocks, whose `id`s equal the pinned set, each with exactly the 12 keys of §5.4.
- **N6 — changed rows equal the matrix** (A1-1). For each pinned row, the oracle row's 11 content fields must equal its block's.
- **N7 — digests follow the formula** (A1-1). For each pinned row, `source_row_sha256` must equal the §5.4 formula applied to the row.
- **N8 — supersedes the right digest** (adversary:8). Each block's `supersedes_source_row_sha256` must equal the historical row's `source_row_sha256`.
- **N9 — the 43 unchanged rows** (A1-1; coverage:11; adversary:7(b)). Every oracle row outside the pinned set must equal the historical row with the same `id` in all 12 fields.

**Must-fail regressions.** Each one mutates one thing in a scratch copy or in memory. Under §9 item 9, each must yield exactly its own finding. A regression marked "re-stamped" first applies this set, so that only the new check can catch it:

```
re-serialize the successor oracle (5.3) and re-derive the successor map (5.6)
validate_flowmaster.py   EXPECTED_ORACLE_SHA256, EXPECTED_CHANGE_RUNTIME_MAP_SHA256
validate_gcfpe_current.py   the installed successor-map constant (5.8)
authority.successor_source_matrix_sha256   (only when the matrix bytes change)
flowmaster-validate/SKILL.md   SKILL_TREE_SHA256
candidate-suite runs also: validation-profile :35/:37 and the validate_gcfpe_20260914.py R1 literals (5.8)
```

- **G1** (A1-1; adversary:7(c); coverage:11): edit GCF-16 `session`, set its `source_row_sha256` by the formula, and re-stamp. Expected: N9 on GCF-16 only.
- **G2** (adversary:7(c); coverage:10): edit GCF-17 `session` in the oracle only, set its digest by the formula, and re-stamp, leaving the matrix untouched. Expected: N6 on GCF-17 only.
- **G3** (A1-1): replace GCF-14's `source_row_sha256` with another 64-hex value and re-stamp. Expected: N7 on GCF-14 only.
- **G4** (A1-1; adversary:7(c)): flip one byte in the matrix prose, outside the JSON blocks. Expected: N3 only.
- **G5** (A1-1; sweep:7): flip one byte of the historical oracle inside `generated_for_run`. Expected: N1 only. A flip inside a historical row also fires N9 for that row (measured), which is why the location is fixed.
- **G6** (A1-1): flip one byte of the historical map. Expected: N2 only.
- **G7** (coverage:10): add GCF-16 to `authority.successor_rows` and re-stamp. Expected: N4 only.
- **G8** (adversary:8): alter one block's `supersedes_source_row_sha256`, write the new matrix digest into `authority`, and re-stamp. Expected: N8 only.
- **G9** (C3): evaluate the §5.10 fixture against the historical oracle. Expected: FMV-GCF-EDGE-003 only.
- **G10** (A1-2; fv-rest:2; fv-rest:3): a scratch contract with `r1_oracle_changed` false and every other pin re-stamped. Expected: PROTECTED_IDENTITIES.
- **G11** (fv-rest:4; fv-main:18): leave the profile's `r1_oracle_sha256` at `52807e58…`. Expected: PROFILE_PROTECTED_IDENTITIES. Measured on the prototype, it appears under FMV-GCF-CANDIDATE-CONTRACT-001 and FMV-GCF-CANDIDATE-FIXTURE-PROFILE-001.
- **G12** (coverage:9; sweep:7): add a link to the historical map in `change-flow/SKILL.md`. This is valid only if OQ-7 resolves to "successor link only". Expected (measured):
  ```
  FMV-SKILL-STRUCTURE-001  unapproved reference-file dependency: references/glow-hde-canonical-change-flow-r1-runtime-map.json
  ```
- **G13** (coverage:9): delete the matrix file. Expected (measured without N3):
  ```
  FMV-SKILL-STRUCTURE-001  missing bundled script: references/r1-successor-source-20260923.md
  ```
  With N3 present, N3 fires as well (OQ-12).

**Measured (prototype harness, placeholder codes).** G1 to G8 each produced exactly its one expected finding. With no mutation, the checks produced no findings on the prototype files.

### 5.8 Live pin and path sites to re-point

These are the sites A1-1 calls "the live validators are re-pointed". `<SUCC_ORACLE>` and `<SUCC_MAP>` stand for the §5.11 digests.

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
:361-364 OPTIONAL_REFERENCES["change-flow"]: the successor map path
           "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
         (replace or add: OQ-7; A1-6's overlay entry is §8's)
:684-689 maintenance_metadata: "CHANGE_FLOW_SPECIALIZATION_REVISION: 2.0.0" -> "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0"
         (adversary:7; plus OQ-2 option b)
new      the historical oracle and historical map paths and digests (N1, N2); the matrix path; the pinned successor set (N4)
```

- The `validator_revision` at `:1221` moves under §8.
- **`flowmaster-validate/SKILL.md` must not link to the matrix** as `](references/...)`. `OPTIONAL_REFERENCES` has no `flowmaster-validate` entry, so any such link fails as an unapproved reference-file dependency.

**`flowmaster-validate/scripts/validate_gcfpe_20260914.py`** (fv-main:18; fv-main:19; fv-main:20; fv-rest:3; pr-relay-graph:30; sweep:7):

```
:1130   "r1_oracle_sha256": "<SUCC_ORACLE>"          (PROFILE_PROTECTED_IDENTITIES; :1132 r1_rows 46 kept)
:1131   "r1_runtime_map_sha256": "<SUCC_MAP>"
:1379   "r1_oracle_sha256": "<SUCC_ORACLE>"          (GRAPH_PROTECTED_IDENTITIES; r1_rows 46, r1_core_rows 26, r1_material_rows 20 kept)
:1956   "protected_r1_46_rows_unchanged": OQ-8
:1964   "r1_oracle_sha256": "<SUCC_ORACLE>"          (PROTECTED_IDENTITIES)
:1965   "r1_rows": 46, "flowmaster_primary_core_changed": False      kept
:1966   "r1_oracle_changed": True, "pr35_adds_r1_row": False          (A1-2 "flags tell the truth"; pr35_adds_r1_row kept)
:2610   runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
:2611   ... sha256(runtime_map) != "<SUCC_MAP>"
```

**`flowmaster-validate/scripts/validate_gcfpe_current.py`** (fv-main:21; sweep:7):

```
:80     EXPECTED_R1_SHA256           kept (52807e58...; the alias's recorded value, used at :376)
:81     EXPECTED_RUNTIME_MAP_SHA256  kept (5574666e...; the alias's recorded value, used at :376)
new     a separate installed-map constant = "<SUCC_MAP>"
:659    runtime_map = change_skill_dir / "references" / "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
:660    compare to the new installed-map constant
```

**The other sites:**

```
flowmaster-validate/scripts/run_change_flow_fixtures.py:15
        ORACLE_PATH = SKILL_DIR / "references" / "glow-hde-canonical-change-flow-r1-20260923.json"
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json
        :35 "r1_oracle_sha256": "<SUCC_ORACLE>"    :36 "r1_rows": 46 kept    :37 "r1_runtime_map_sha256": "<SUCC_MAP>"
both 091426.1 direct-handoff contract copies (change-flow/references and flowmaster-validate/references), protected_identities:
        :3114 "r1_oracle_sha256": "<SUCC_ORACLE>"    :3113 "r1_oracle_changed": true
        r1_rows 46, r1_core_rows 26, r1_material_rows 20, pr35_adds_r1_row false, flowmaster_primary_core_changed false kept
        written by the regenerator (A1-2, §6); graph_proofs.protected_r1_46_rows_unchanged (:390): OQ-8
docs/graph/parts/global.json:555
        "r1_oracle_sha256": "<SUCC_ORACLE>"        (:551-557 otherwise kept; rebuilt per §6)
change-flow/SKILL.md
        :17   R1_CONTRACT_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1
        :19   R1_CONTRACT_MATRIX_SHA256 kept (faa7fb7d...)      :21 R1_ROW_COVERAGE: 46/46 kept
        :557  link target references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json and SHA-256 `<SUCC_MAP>`
              (its "immutable historical baseline" prose is §8's; fv-rest:1)
flowmaster-validate/SKILL.md
        :145  R1_ORACLE_PROFILE: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1
        :147  kept    :149  R1_ORACLE_SHA256: <SUCC_ORACLE>
        :244  The Change oracle is the bundled file references/glow-hde-canonical-change-flow-r1-20260923.json. It pins:
        :246  - projection SHA-256 <SUCC_ORACLE>;
        :248, :249 kept (OQ-13)
        :9    SKILL_TREE_SHA256, last (5.11)
flowmaster-validate/fixtures/change-flow/scenarios.json
        the new scenario (5.10); :3 "oracle_profile": OQ-9
```

**Measured, default suite.** On a copy with only the `validate_flowmaster.py` constants and allowlists, `run_change_flow_fixtures.py:15`, `change-flow/SKILL.md:17` and `:557`, and `validate_gcfpe_current.py:659-660` re-pointed, the default suite returned two findings:
- FMV-GCF-INTERFACE-001, "missing mandatory interface token: GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1", which is OQ-2;
- SKILL_SELF_IDENTITY.

With either OQ-2 option plus a re-stamped tree it returned FLOWMASTER_SUITE_PASS, `rows_exact` true, `interfaces_closed` true, and 31/31 change-flow fixtures.

**Measured, candidate suite.** The suite (`--gcfpe-contract` with `--gcfpe-candidate-root`) also passed with `validate_gcfpe_20260914.py`, the profile, the graph and the contract still pinning `52807e58…` and `5574666e…`. It passes because the historical files still hash to those values. Nothing but the E4 residual-hit list (§5.12) would notice a site left unmoved (OQ-10).

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
flowmaster-validate/SKILL.md:147, :248, :249
```

**Measured:** on the re-pointed prototype copies, all 12 historical-layer commands from §2 exited 0, and each one's output hashed the same as its baseline.

**Superseded.**
- **Step 34's verification is replaced by §5.12's residual-hit list.** That verification was "`grep -rc 52807e58` = 0" (fv-main:21; fv-rest:8; pr-relay-graph:30).
- **fv-main:20's re-pins at these sites are dropped:** `validate_strength_middleware.py:14`, `validate_integrated_readiness.py:8`/`:151`, `validate_pre_guide_correction.py:9`/`:67` and `validate_gcfpe_current.py:81` (sweep:8).
- **So are fv-rest:1's in-place map edit and alias `:806` re-pin, and fv-rest:2's alias re-pin** (sweep:11).
- **pr-relay-graph:30's "after the child's GCF-15 row change" does not apply:** GCF-15 does not change (D23 correction).

### 5.10 The R1 path fixture (child C3; fv-rest:27; coverage:20; sweep:7)

It is added to `flowmaster-validate/fixtures/change-flow/scenarios.json`. That file is hand-formatted, and no `json.dumps` variant reproduces it, so the scenario is inserted as text in the file's existing style. The file has no hash pin; only `SKILL_TREE_SHA256` covers it. Its `id` and position are OQ-9. The content:

```json
{
  "id": "<OQ-9>",
  "expected_pass": true,
  "expected_rule_ids": [],
  "coverage_mode": "COMPLETE",
  "events": [{"row": "GCF-17.LINEAGE"}, {"row": "GCF-14"}]
}
```

**Measured** with `validate_fixture_payload`:
- against the historical oracle, exactly `["FMV-GCF-EDGE-003"]`;
- against the successor oracle, `[]`.

Against the successor oracle, the existing 31 change-flow fixtures keep their expectations, and `graph_findings` over the successor rows is `[]`. GCF-14's new input has one producer, GCF-17.LINEAGE, and is already a declared terminal output.

### 5.11 Pin order (adversary:7(d); fv-main:16; fv-main:23; fv-rest:9; pr-relay-graph:30)

Each step writes a pin only after the bytes it pins are final. No step pins a later step's output.

1. **Matrix.** Write the three blocks. `sha256(matrix bytes)` is the matrix digest. Copy the file to the repository (OQ-6).
2. **Oracle.** Build it by §5.3, writing the step-1 digest into `authority.successor_source_matrix_sha256`. The result is `<SUCC_ORACLE>`.
3. **Map.** Derive it by §5.6. The result is `<SUCC_MAP>`.
4. **Graph.** Write `<SUCC_ORACLE>` at `global.json:555`, rebuild, and write both bundled copies (§6).
   - Measured with a copy of `route_sim_final.py` and the prototype digest: 229 edges, 574 175 B, routing surface still `fecc319bdd4ce7ee6201cb77d7231861`/284. Only the graph digest changes, so §2's `b1911cf5…` is not final.
5. **Contract, both copies.** `protected_identities.r1_oracle_sha256` becomes `<SUCC_ORACLE>`, `r1_oracle_changed` becomes true, and the step-4 graph digest goes into `source_snapshot` (regenerator, §6).
6. **Profile.** `:35` becomes `<SUCC_ORACLE>` and `:37` becomes `<SUCC_MAP>`, alongside the graph and contract pins (§6).
7. **Literals.** Every §5.8 validator constant, path and SKILL.md line except `:9`.
8. **Fixtures pin.**
   - The §5.10 scenario, which has no hash pin.
   - The 091426.1 fixture pin: `EXPECTED_FIXTURE_SHA256` at `validate_gcfpe_20260914.py:945`, plus the profile's `fixtures.sha256`/`count`, for C8's edits (fv-main:29, §8). The profile is written a second time here.
9. **`SKILL_TREE_SHA256`** at `flowmaster-validate/SKILL.md:9`, last. The change-flow package has no tree digest.

### 5.12 Prototype values and E4 items

**Determined** by the §5.3 content and the §5.4 formula, subject only to OQ-4:

```
GCF-14          source_row_sha256 42db7a9e614ecf943f042a9c012112fd3934f12e504cd4b980f404735b9cfe6b
GCF-17          source_row_sha256 6774529046ba5050b2e62b8cf01b024766c5e99d343d0fcfdd32b0367fb99602
GCF-17.LINEAGE  source_row_sha256 73a133c18b13682cbc57d813b37caacda7ed15b183437515867166bcda70e83e
```

**PROTOTYPE.** These depend on OQ-2, OQ-3 and OQ-5:

```
matrix       3 695 B  d546dac141e31c8b1d32a694a86b6b7ecc9789fedd5f705673e7165822b1484b
oracle      53 402 B  afb439b187b50a27937bcb238c65fb206cac53dd5a1ac4023549c1f552d12c46   OQ-2 option b (tokens copied)
oracle      53 402 B  c3861f40ae5dbeab4eb61e1a70ad730fbb453c7bc7f9dd73a4af611cb53fec77   OQ-2 option a (token replaced)
runtime map 46 326 B  c02d3d1924ab491c336675470e38ca514b6194eb3832c6f5eb1ac58b4b45f7f0   either option
graph      574 175 B  7c51ed4cb975fdab7401ea93dc5a60d1e16cfee0c1a193c746f4007b310808f6   route_sim_final.py copy + oracle afb439b1... at global.json:555
```

**The E4 items this section owns** are in §9: item 3, the live suites; item 4, the historical layer, which must equal its baseline; and item 9, regressions G1 to G13.

The residual-hit check below replaces step 34's grep:

```
grep -rn -e 52807e58 -e 5574666e <copy>/flowmaster-validate <copy>/change-flow <repo>/docs/graph/parts
```

It must return exactly these hits:
- the §5.9 sites that carry these digests;
- `validate_gcfpe_current.py:80`/`:81`;
- the two new historical constants in `validate_flowmaster.py`.

It must return no hit in:
- the successor oracle, the successor map or the matrix;
- the profile;
- the 091426.1 contracts or bundled graphs;
- `global.json`;
- either SKILL.md, unless OQ-13 adds a mention.

For the old profile id, the check is:

```
grep -rn GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1 <copy>/flowmaster-validate <copy>/change-flow
```

It must hit only the two historical files, plus the OQ-2 and OQ-9 sites, depending on how those resolve.

### 5.13 Placement of findings

| finding | placed in |
|---|---|
| adversary:7 | §5.8 sites, §5.7 N1–N9, G1/G2/G4, §5.11 order |
| adversary:8 | §5.3 serialization, §5.4 format and formula, N5–N8, G8 |
| coverage:9 | §5.8/§5.9 live-versus-historical split; allowlists, G12/G13 |
| coverage:10 | §5.5 authority binding, N4/N5, G2/G7; verdict/snapshot scope OQ-3 |
| coverage:11 | N9, G1 |
| coverage:20 | §5.3 GCF-14/15 disposition, §5.10 |
| sweep:7 | §5.8 path sites, N1, §5.10 |
| sweep:8 | §5.9; fv-main:20 historical sites superseded |
| sweep:11 | only its fv-rest:1/fv-rest:2 part: superseded (§5.9) |
| sweep:24 | GCF-14 `consumes` (third changed row) |
| fv-main:18, fv-rest:4, fv-rest:5 | §5.8 profile, contracts, SKILL.md `:149`/`:246` |
| fv-main:19, fv-rest:3 | §5.8 `:1964-1966` (A1-2), N9 as the kept-invariant guard; `:1956` OQ-8 |
| fv-main:20, fv-rest:1 | §5.6 successor map and its pins; in-place edit superseded |
| fv-main:21, fv-rest:2 | §5.8 `validate_gcfpe_current.py` split; alias kept; grep replaced (§5.12) |
| fv-main:22, fv-rest:27 | §5.3 rows, §5.10 fixture |
| fv-rest:0, fv-rest:7 | §5.2, §5.8 |
| fv-rest:6 | §5.4/§5.5; FMV-ORACLE-003 unchanged |
| fv-rest:8 | §5.1, §5.9 |
| pr-relay-graph:30 | §5.11 step 4 |
| fv-main:23, fv-rest:9 | §5.11 step 9 |

Cross-references only, placed elsewhere: fv-main:16, fv-main:29, pr-relay-graph:20, pr-relay-graph:21 and adversary:2 (§6); coverage:15, sweep:12 and sweep:13 (§8: the prose at `change-flow/SKILL.md:453-455` and `flowmaster-validate/SKILL.md:294` that restates GCF-17).

## §6 Contract regenerator and value table

This section compiles A1-2 (the contract regenerator), the contract-only values that A1-2, A1-3, A1-5, A1-6 and the child's C8–C9 change, and the validator checks those values move. It replaces step 15 ("Regenerate from the graph parts; never hand-edit"), which had no tool (fv-main:17, fv-rest:12, pr-relay-graph:21). Every value cites its source. **A value written `«Q6.n»` has not been decided.** It stays open until open question Q6.n (§6.7) is ruled, and the value table is not complete until then.

Abbreviations: `fv` is `flowmaster-validate/scripts/validate_gcfpe_20260914.py`, `cf` is `change-flow/scripts/validate_gcfpe_20260914.py`, and `global.json` is `docs/graph/parts/global.json`.

### 6.1 Recipe (A1-2)

**Inputs**
1. **G**, the graph build. Run `graph_parts.py build` over the edited parts into scratch. Take the lines between the first line equal to ` ```json ` and the last line equal to ` ``` `, join them with `\n`, and append one `\n`. The resulting bytes are the bundled graph that §5 writes to both skills (preflight_notes fv-main tooling). Today they are 569 835 B, `90021eb7…`.
2. **T**, the template: the current 091426.1 direct-handoff contract, today `2b78f877…`, 606 657 B, byte-identical in both skills.
3. **The value table** (§6.3), held as an explicit `{key path: value}` map inside the script. It is never read from the graph.

**Steps**
1. Deep-copy T.
2. Write every mirrored path in §6.2 from G. There are 42 contract paths, plus 12 fields for each of the 55 members, 702 paths in all.
3. Write each value-table entry at its path. A removal listed in §6.3 deletes the key.
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

**No value-table entry may target a mirrored path.** Mirrored values are authored in the graph parts and reach the contract only through step 2. That applies to four of the keys the task lists under the value table:
- `post_merge_three_event_contract`;
- `pr_development_contract.pr35_result_vocabulary`, `.added_boundaries` and `.shared_exactly_one`;
- the `member_registry` fields;
- the routing surfaces.

§6.3 shows their before and after values so the whole contract delta can be reviewed. Their source of truth is `global.json` and the prompt parts.

**Pin order.** `protected_identities.r1_oracle_sha256` (§6.3) and the graph's own `protected_identities` both need the successor oracle's digest. The regenerator therefore runs after the oracle is final and after the last graph build. Its output feeds the profile and literal re-pins (§5, pin order from adversary:7(d)).

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
- These checks constrain the graph alone:
  - `GRAPH_IDENTITY`, `GRAPH_CANDIDATE_PROFILE`, `GRAPH_BASELINE_PROFILE` and `GRAPH_NODE_SET`;
  - the handoff constants (block counts 1 and 0, and `complete_paste_ready_prompt`);
  - `GRAPH_UNRESOLVED_EDGE`, `GRAPH_PR50_INBOUND_CARDINALITY`, `GRAPH_DIRECT_PR40_EDGE`, `GRAPH_UNRESOLVED_PREDICATES`, `GRAPH_PROOFS` and `GRAPH_PROTECTED_IDENTITIES` (fv:1176-1199, :1330-1382).

  Of these, `GRAPH_DIRECT_PR40_EDGE` moves with step 38 and `GRAPH_PROTECTED_IDENTITIES` moves with §5.

This set is complete for the two functions. The prototype's leave-one-out run confirms that none of the 54 entries is surplus (§6.4).

### 6.3 Value table (before → after)

Before values are dumped from today's bundled contract (`2b78f877…`). After values are sorted-key JSON, as serialised.

#### Contract-only keys (the regenerator's value table)

**`contract_revision`**. Source: A1-2 ("moves from 4.0.6 to 4.1.0"). Settles fv-main:35 and fv-rest:11.
```json
"4.0.6"
```
```json
"4.1.0"
```

**`transition_contract`**. Sources: A1-2 ("the handoff flags follow C-HANDOFF, and `HANDOFF_CONTRACT` becomes an exact-key check"); §P C-HANDOFF; step 12; D23-B; fv-main:17, fv-rest:13, pr-relay-graph:31, adversary:3 and coverage:12.

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
After:
```
{
  "actual_branch_only": true,
  "actual_pasteable_complete_prompt": true,
  "blank_form_menu_or_reconstruction_prohibited": true,
  "block": "NEXT_PROMPT_HANDOFF",
  "every_required_repository_and_pr_reference": «Q6.3»,
  "exact_destination_full_name_version_direct_notion_url": true,
  "exactly_one_per_nonterminal_result": true,
  "fence_language": "text",
  "first_line": "NEXT_PROMPT_HANDOFF",
  "metadata_only_or_routing_summary_prohibited": true,
  "prohibited_references": [
    "Library ID",
    "unlinked filename",
    "above",
    "conversation reconstruction",
    "model/strength/reasoning/eligibility/suitability/account/configuration route",
    "branch",
    "commit",
    "restated artifact content"
  ],
  "receiving_role_and_exact_session": true,
  "terminal_has_no_handoff": true,
  "transport": "DIRECT_NATIVE_PROMPT_HANDOFF"
  «Q6.2: any added C-HANDOFF flags»
}
```
- **Retired.** The flags `status_completed_work_decisions_constraints_unresolved_authority`, `epic_change_and_work_unit` and `next_action_and_expected_output` are retired: D23-B reverses the first, and step 12's required list drops the other two. Whether each key is deleted or kept with `false` is Q6.1.
- **Kept.** Destination, receiving role and session, paste-ready completeness, one block per nonterminal result, and the ban on menus, "above" and reconstruction are kept, as C-HANDOFF requires and step 12 keeps `complete_paste_ready_prompt`. No source changes the metadata-only prohibition, the transport or the terminal rule.
- **Mirrored.** `first_line`, `fence_language` and `actual_branch_only` are mirrored (§6.2) and do not change.

**`receiver_compatibility`**. Sources: A1-2 ("PR-35's receiver entry is a dedicated top-level session; PR-40 is entered on `MERGE_OBSERVED` or, as the fallback, on Nathan's assertion"); A1-5; C9; sweep:10, sweep:21, fv-main:32 and adversary:10. `PR-30`, `RS-20`, `RS-30` and `RS-40` are unchanged (C9, sweep:21).

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
After:
```
{
  "PR-20": «Q6.5»,
  "PR-35": {
    "context": "SAME_PR_WORK_UNIT_AFTER_INITIAL_PUBLICATION",
    "dedicated_top_level_pr35_session": true,
    "same_workspace_worktree_branch_open_pr_original_proceed": true
  },
  "PR-40": {
    "attribution_skill_read_only": true,
    "entry_fact": «Q6.6»,
    "independent_actual_merged_state_and_landed_lineage_verification": true,
    "prior_merge_pending_is_historical_premerge_evidence": true
  }
}
```
- **PR-20** must, per C9, accept a PR-40 `REJECT` finding (`reject_replan`) for an existing `WORK_UNIT_ID`, in a new top-level session Nathan creates, with a new Proceed. Its literal shape is Q6.5.
- **PR-35** takes sweep:10's two keys in place of the same-session key.
- **PR-40** keeps its three verification flags (sweep:10; A1-5 "PR-40 still verifies … independently"). `nathan_manual_merge_assertion_required` is replaced by `entry_fact` (sweep:10). The value of `entry_fact` is Q6.6.

**`route_graph`**. Sources: A1-2 ("the route shorthands are revised, and the re-plan gets one"); C8 (`pr40_reject_replan`); sweep:10. The three rescope sequences are mirrored and unchanged.

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
After (only the entries that change or are added):
```
"ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],
"pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],
«Q6.7 key name»: ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"]
```
Both ordinary sequences keep `NATHAN_PROCEED` at index 2 (cf:944-945). No new value contains a `RETIRED_DRAIN_TOKENS` entry (fv:1628-1629).

**`route_graph_semantics`**. Sources: fv-main:32, coverage:13 and sweep:10 ("per C-SESSION and C-DISPATCH"). `pr35_merge_pending` is unchanged, because `MERGE_PENDING` stays pre-merge evidence (A1-5). `pr50`, `qa_pass_closure` and `rs40` are unchanged.

Before (the entries that change):
```json
{
  "pr40_entry": "Requires Nathan's later manual-merge assertion and PR-40's independent read-only verification.",
  "same_session_phase_continuation": "PR-30 to PR-35 is one lawful same-session phase continuation inside GCF-17, not a new work unit or cross-session route."
}
```
After:
```
{
  "pr40_entry": «Q6.9»,
  «Q6.8 key»: «Q6.8 text»
}
```

**`pr_development_contract` (its contract-only fields)**. Sources:
- `primary_skill_revision`: A1-6 ("`glow-hde-pr-development` 1.3.0"); fv-main:25, fv-rest:26 and pr-relay-graph:16.
- `pr30_ownership`: fv-main:32; C-SESSION.

Before:
```json
{
  "pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation", "deliberate initial publication", "complete same-session PR-35 handoff"],
  "primary_skill_revision": "1.2.5"
}
```
After:
```
{
  "pr30_ownership": ["recovery", "implementation", "local testing", "coherent commit creation", "deliberate initial publication", «Q6.10»],
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
- A1-2 ("the R1 identity flags tell the truth: `r1_oracle_changed: true`");
- A1-1 (46 rows, 26 core and 20 material; the live validators are re-pointed to the successor);
- A1-6 (the Flowmaster core stays byte-identical);
- fv-main:18, fv-main:19, fv-rest:3 and adversary:7(a).

The successor digest is written in pin order (§5).

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
After:
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
Whether a `D23` pointer is added is Q6.14.

**`graph_proofs.protected_r1_46_rows_unchanged`**. Sources: A1-2 ("the R1 identity flags tell the truth"); A1-1 (three rows change); fv-main:19 and fv-rest:3. `pr35_same_r1_row_as_pr30` stays `true` (step 29), and `route_edge_count` is mirrored.

Before:
```json
{"pr35_same_r1_row_as_pr30": true, "protected_r1_46_rows_unchanged": true, "route_edge_count": 227}
```
After (`false` or a rename is Q6.13; the prototype used `false`):
```
{"pr35_same_r1_row_as_pr30": true, "protected_r1_46_rows_unchanged": false, "route_edge_count": 229}
```

#### Mirrored keys the amendment changes (authored in the graph parts, then copied)

**`post_merge_three_event_contract`** (`global.json`). Sources:
- A1-5: `direct_PR35_to_PR40_automatic_edge` stays `false`; "the observed-merge edge is recorded inside `post_merge_three_event_contract`"; no agent merges.
- A1-2: "`event_2` becomes 'observed or asserted'".
- sweep:10 and fv-main:13 keep `event_2.actor`, `event_1` and `event_3`.

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
```
{
  "agent_merge_authorized": false,
  "direct_PR35_to_PR40_automatic_edge": false,
  "event_1": {"fact": "prior_pr35_result", "producer": "PR-35", "time": "pre_merge_historical_evidence", "value": "MERGE_PENDING"},
  "event_2": {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted", "time": «Q6.11b», "value": true},
  "event_3": {"consumer": "PR-40", "fact": "pr40_actual_merge_verification", "independent": true, "values": ["VERIFIED", "PENDING"]},
  «Q6.11a: the observed-merge edge record»
}
```

**`pr_development_contract`, mirrored fields** (`global.json` `pr_continuity_contract` and `state_vocabularies`). Sources:
- `pr35_result_vocabulary`: A1-5's ordered vocabulary; sweep:3, adversary:9 and route_sim_final.py.
- `added_boundaries.session`: step 29, fv-main:2 and fv-rest:15.
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
```
{
  "added_boundaries": {"approval": 0, "cross_session_route": «Q6.12», "duplicate_work_vehicle": 0, "merge_authority": 0, "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0, "work_vehicle": 0},
  "pr35_result_vocabulary": ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
  "shared_exactly_one": ["WORK_UNIT_ID", "original Product Owner Proceed", "workspace/worktree", "branch", "pull request", "PR instruction", "detailed PR plan", "primary skill authority", "continuous recovery/artifact lineage"]
}
```
`pr30_result_vocabulary` is unchanged.

**`member_registry` mirrored fields** (the `PR-35.json` and `RS-40.json` nodes). Sources:
- `session_class` and `receiving_role`: step 30, A1-8 and fv-main:8.
- `result_states`: A1-5 ("Both PR-35 and RS-40 gain it") and route_sim_final.py, which measured exactly these two node changes.

`version`, `title` and `notion_url` are unchanged (A1-3). No other member's mirrored field changes unless Q6.16 or Q6.17 rules otherwise.

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
    "result_states": ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  }
}
```
After:
```
{
  "PR-35": {
    "native_function": «Q6.17»,
    "receiving_role": «Q6.15; step 30's base text: "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request."»,
    "result_states": ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"],
    "session_class": "DEDICATED_PR_REVIEW_SESSION"
  },
  "RS-40": {
    "result_states": ["SOURCE_RESOLUTION_ERROR", "PR_CANDIDATE_PUBLISHED", "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  }
}
```

**The routing surfaces and derived pins.**
- `route_edges`, `state_routes` and `boundary_transitions` follow A1-7. route_sim_final.py (`e0854a55…`) is the authority for the full edge objects and their positions, so they are not restated here.
- `graph_proofs.route_edge_count` goes from 227 to 229.
- `source_snapshot.frozen_candidate_graph.sha256` becomes the sha256 of the final bundled graph. That is not route-sim's `b1911cf5…`: steps 29–30 and the successor oracle digest move the bytes again (§5).

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
1. Strip every §6.2 path from today's contract.
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

**After-state measurement.** This is a measurement, not a decision. The graph is route_sim_final.py's parts, with step 29–30 values and sweep:10's `event_2.fact` added. The contract is regenerated with only the determinable values of §6.3, and every `«Q»` value is left at today's value.
```
route-sim parts rebuilt            574175 B sha256 b1911cf54d2af9ae889153b619d39c9deac9b3089b45262770fe7508dff96ee7 (matches A1-7)
routing_surface(regenerated)       fecc319bdd4ce7ee6201cb77d7231861 / 284   (matches A1-7)
validate_graph_contract            ["GRAPH_DIRECT_PR40_EDGE"]   (graph-only check; step 38 narrows it)
validate_contract, today's fv      CONTRACT_IDENTITY, DIRECT_PR35_PR40_EDGE, GRAPH_PROOFS, HANDOFF_CONTRACT,
                                   HANDOFF_PROHIBITED_REFERENCES, POST_MERGE_THREE_EVENTS, PR35_ADDED_BOUNDARY,
                                   PR35_RESULT_VOCABULARY, PR35_STATE_ROUTES, PR40_MANUAL_MERGE_BOUNDARY,
                                   PROTECTED_IDENTITIES, PR_DEVELOPMENT_CONTRACT, PR_PHASE_CONTINUITY,
                                   ROUTE_GRAPH_SHORTHAND, ROUTING_SURFACE_CHANGED
validate_contract, scratch fv with the §6.5 expectations
                                   DIRECT_PR35_PR40_EDGE, PR40_MANUAL_MERGE_BOUNDARY   (step 38's rewrites)
```
**E4 item 2 (`validate_graph_contract == []`) cannot pass** until step 38 narrows `GRAPH_DIRECT_PR40_EDGE` to PR-30 (coverage:19, adversary:9).

### 6.5 Validator checks whose expectations move

Each moved literal gets a must-fail regression that must add exactly its own code over the clean after-state (§9 item 9). The run marked "measured" used a scratch copy of `fv` patched with the expectations below: 19 regressions, each adding exactly its code.

| check | where | what moves | regression |
|---|---|---|---|
| `CONTRACT_IDENTITY` | fv:1386-1400; cf:751 | `contract_revision` | R1 |
| `HANDOFF_CONTRACT` | fv:1482-1494 | from a subset check to an exact-key, exact-value check on the §6.3 `transition_contract`, excluding `prohibited_references` (A1-2) | R2a, R2b, R2c |
| `HANDOFF_PROHIBITED_REFERENCES` | fv:1495-1500 | the set gains three entries | R3 |
| `POST_MERGE_CONTRACT` | fv:1769-1771 | unchanged (both flags stay `false`, A1-5); kept guarding | R4 |
| `POST_MERGE_THREE_EVENTS` | fv:1772-1780 | `event_2.fact`; plus an assertion on the observed-merge record once Q6.11 is ruled | R5 |
| `ROUTE_GRAPH_SHORTHAND` | fv:1782-1798 | the exact dict becomes §6.3's `route_graph` | R6a, R6b |
| `PR35_ADDED_BOUNDARY` | fv:1742-1743 | from "all zero" to an exact map (fv-main:2, fv-rest:15) | R7a, R7b |
| `PR_PHASE_CONTINUITY` | fv:876-880, :1744-1745 | nine fields | R8 |
| `PR35_RESULT_VOCABULARY` / `PR35_STATE_ROUTES` | fv:853-856, :1747, :1921-1922; cf:1006-1011 | six values | R9 |
| `PR_DEVELOPMENT_CONTRACT` | fv:1714-1741 | `primary_skill_revision` | R10 |
| `PROTECTED_IDENTITIES` | fv:1959-1967 | `r1_oracle_changed`, `r1_oracle_sha256` | R11a, R11b |
| `GRAPH_PROOFS` (contract) | fv:1950-1957 | `protected_r1_46_rows_unchanged` (Q6.13) | R12 |
| new receiver-compatibility check | the v4 `validate_contract` in fv, reached for schema 4.0 through `validate_gcfpe_current.py:401-405` and `:619-622` (A1-6) | exact content of `PR-20`, `PR-30`, `PR-35` and `PR-40`; no entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` `REJECT` (C9). Code name and scope are Q6.21 | R13a–R13d |
| `ROUTING_SURFACE_CHANGED` | fv:207-208, :1673-1675; cf:76-77, :919-921 | the pin | R14 |
| `PRESERVATION_CONTRACT` | fv:1968-1977 | unchanged (A1-3); kept guarding | R15 |

New expectations:
```
CONTRACT_IDENTITY / cf:751     "contract_revision": "4.1.0"
HANDOFF_CONTRACT               {k: v for k, v in transition_contract.items() if k != "prohibited_references"} == §6.3 after value, keys and values exactly
HANDOFF_PROHIBITED_REFERENCES  {"Library ID", "unlinked filename", "above", "conversation reconstruction",
                                "model/strength/reasoning/eligibility/suitability/account/configuration route",
                                "branch", "commit", "restated artifact content"}
POST_MERGE_THREE_EVENTS        event_2.fact == "product_owner_manual_merge_observed_or_asserted"; event_2.actor, event_1 and event_3 unchanged
PR35_ADDED_BOUNDARY            added_boundaries == {"approval": 0, "cross_session_route": «Q6.12», "duplicate_work_vehicle": 0, "merge_authority": 0,
                                "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0, "work_vehicle": 0}
EXPECTED_PHASE_CONTINUITY      ["WORK_UNIT_ID", "original Product Owner Proceed", "workspace/worktree", "branch", "pull request",
                                "PR instruction", "detailed PR plan", "primary skill authority", "continuous recovery/artifact lineage"]
EXPECTED_PR35_RESULTS / cf     ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
PR_DEVELOPMENT_CONTRACT        "primary_skill_revision": "1.3.0"
PROTECTED_IDENTITIES           "r1_oracle_changed": True, "r1_oracle_sha256": <successor oracle sha256>; all other values unchanged
GRAPH_PROOFS                   "protected_r1_46_rows_unchanged": False   (Q6.13)
EXPECTED_ROUTING_SURFACE       "fecc319bdd4ce7ee6201cb77d7231861", EXPECTED_ROUTING_SURFACE_ROWS = 284   (fv and cf)
```
Must-fail regressions. Each mutates the clean after-state contract in memory and must add exactly the named code:
```
R1   contract_revision = "4.0.6"                                              -> CONTRACT_IDENTITY; cf: FAIL corrected-source contract revision   (measured)
R2a  transition_contract["status_completed_work_decisions_constraints_unresolved_authority"] = True  -> HANDOFF_CONTRACT   (measured)
R2b  transition_contract["epic_change_and_work_unit"] = True                  -> HANDOFF_CONTRACT   (measured)
R2c  transition_contract["actual_pasteable_complete_prompt"] = False          -> HANDOFF_CONTRACT   (existing fixture reject-incomplete-handoff; measured)
R3   transition_contract["prohibited_references"].remove("branch")            -> HANDOFF_PROHIBITED_REFERENCES   (measured)
R4   post_merge_three_event_contract["direct_PR35_to_PR40_automatic_edge"] = True  -> POST_MERGE_CONTRACT   (measured)
R5   post_merge_three_event_contract["event_2"]["fact"] = "product_owner_manual_merge_assertion"  -> POST_MERGE_THREE_EVENTS   (measured)
R6a  route_graph["ordinary_pr_work_unit"] = ["PR-10","PR-20","NATHAN_PROCEED","PR-30","PR-35","NATHAN_MANUAL_MERGE_ASSERTION","PR-40"]  -> ROUTE_GRAPH_SHORTHAND   (measured)
R6b  del route_graph["pr40_reject_replan"]                                    -> ROUTE_GRAPH_SHORTHAND   (measured)
R7a  added_boundaries["session"] = 0                                          -> PR35_ADDED_BOUNDARY   (measured)
R7b  added_boundaries["proceed"] = 1                                          -> PR35_ADDED_BOUNDARY   (existing fixture reject-new-proceed-boundary; measured)
R8   shared_exactly_one.insert(2, "dedicated PR-development session")         -> PR_PHASE_CONTINUITY   (measured)
R9   pr35_result_vocabulary.remove("MERGE_OBSERVED")                          -> PR35_RESULT_VOCABULARY; cf: FAIL PR-35 results   (measured)
R10  primary_skill_revision = "1.2.5"                                         -> PR_DEVELOPMENT_CONTRACT   (measured)
R11a protected_identities["r1_oracle_changed"] = False                        -> PROTECTED_IDENTITIES   (measured)
R11b protected_identities["r1_oracle_sha256"] = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"  -> PROTECTED_IDENTITIES   (measured with an all-zero digest; exact once the successor exists)
R12  graph_proofs["protected_r1_46_rows_unchanged"] = True                    -> GRAPH_PROOFS   (measured)
R13a receiver_compatibility["PR-30"] gains acceptance of a PR_WORK_UNIT_LINEAGE_REVIEW REJECT   -> new receiver check (C9)
R13b receiver_compatibility["PR-35"]["same_session_workspace_worktree_branch_open_pr_original_proceed"] = True  -> new receiver check
R13c receiver_compatibility["PR-40"]["nathan_manual_merge_assertion_required"] = True  -> new receiver check
R13d del receiver_compatibility["PR-20"]                                      -> new receiver check
R14  route_edges[0]["route_branches"][0]["condition"] += " x"                 -> ROUTING_SURFACE_CHANGED   (measured)
R15  preservation["versioned_sibling_successors"] = False                     -> PRESERVATION_CONTRACT   (measured)
```
R13a–R13d are not measured, because the entry shapes are open (Q6.5, Q6.6).

**Checks the mirrored values move, specified elsewhere.** They are listed here so that no moved literal goes unowned.
- **Step 38** (coverage:19, adversary:9, fv-rest:20):
  - `DIRECT_PR35_PR40_EDGE` (fv:1837-1838);
  - `GRAPH_DIRECT_PR40_EDGE` (fv:1349-1355);
  - `PR40_MANUAL_MERGE_BOUNDARY` (fv:1924-1948), which rejects the new PR-35 → PR-40 and RS-40 → PR-40 prompt edges.
- **Pin chain, §5:**
  - cf:806's edge count of 227 becomes 229;
  - the bundled-graph pins (cf:21, :777, :781; fv:941-942);
  - the contract byte pins (fv:943-944; profile);
  - the graph's `GRAPH_PROTECTED_IDENTITIES` (fv:1375-1382).
- **§8:**
  - the skill-text literals at cf:1020-1023;
  - the fixture runner's `pr_split` positive case, which requires every `added_boundaries` value to be zero (runner:66-70; fv-main:6);
  - `reject-pr35-direct-pr40` (runner:361).

### 6.6 Finding dispositions placed here

- **Placed fully:**
  - fv-main:2, :3, :4, :8, :10, :13, :14, :17, :19, :32, :35;
  - fv-rest:3, :12, :13, :15;
  - pr-relay-graph:21, :28, :31;
  - coverage:12, :13; sweep:10, :21; adversary:2, :3, :10.
- **Superseded by A1-2/A1-3:** fv-main:31 (`preservation` is kept).
- **Placed for the contract part only, with the rest in §5 or §8:**
  - fv-main:18 and fv-rest:11 (contract pins);
  - fv-main:25, fv-rest:26 and pr-relay-graph:16 (`primary_skill_revision`);
  - fv-rest:21, sweep:3 and adversary:9 (the vocabulary mirror);
  - fv-rest:20 (the `POST_MERGE_*` half).

### 6.7 Open questions (not decided here)

Q6.1–Q6.21 are listed in this section's `open_questions`. Each one blocks only the value it marks.

The following hold whichever way the questions are ruled:
- the recipe;
- the mirrored key set;
- the acceptance test and its measured PASS;
- the negative control;
- every value not marked `«Q»`.

## §7 Registry: guards, derived fields, dispositions

This section compiles every change to `docs/prompt_ecosystem_management/project-prompt-contract-registry.md` in this run:
- the guards, which are the `D14` tested guards that `D23` requires for each ruling ("Until those land, `D23` is ruled but not applied");
- the `D13` fields the registry deriver rewrites;
- the authored row edits;
- the N1 and N2 dispositions;
- the edit method.

The registry is repository work, so it goes on the execution branch in E1 (A1-4 item 1; child *Order*, "C5 with E1"). The section decides nothing. Where the sources are silent or disagree, it names the item and points to §7.12.

**Baseline, measured today.**
- 5301 lines, sha256 `c5ae188834d5154826b1bc723a89712cebe4631bee296c56ec856b3947e1d1f7`.
- 55 rows and 831 assertions.
- `validate_project_prompt_registry.py` returns `{"valid": true, "problems": []}`, exit 0.

**Precedence.** The amendment governs §P, and it also governs the preflight rows and critic findings. Two consequences:
- **Superseded premise.** Wherever a finding assumes that `direct_PR35_to_PR40_automatic_edge` becomes `true` (registry-audit:10, :12), A1-5 supersedes that premise. The derived values below follow from the graph edges only.
- **Superseded C-SUB and C-DISPATCH.** §P's C-SUB and C-DISPATCH are superseded by A1-5's versions. Where they are tested below, it is only as retired text.

### 7.1 Conventions

**The evaluator.** Every guard below is evaluated by the audit skill's own function, imported from a scratch copy of `amthor-workspace-governance-audit` (registry-audit notes; adversary:15; `audit_workspace_governance.py:520-545`):

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

Every value in §7.3 was checked in this form: `yaml.safe_load` returns exactly `[{"value": <value>, "rule_id": <RULE_ID>}]`.

**Row selectors.**
- **ALL55.** Every row.
- **MAIN54.** Every row except `GCFPE-MGMT-10` (A1-8; the `D23` clarification).
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

**Must-fail regression criterion** (E4 item 9; registry-audit:1; spec §9). `F` evaluates the whole edited row, which carries several assertions under one `rule_id`. So the value, not the `rule_id` alone, identifies the guard.

```
set(F(row, mutated)) - set(F(row, clean)) == {(rule_id, "Required pattern absent: " + value)}     # required guard
set(F(row, mutated)) - set(F(row, clean)) == {(rule_id, "Forbidden pattern matched: " + value)}   # forbidden guard
```

**Canonical texts used for testing.** They were read from the three sources, with hard wraps joined by one space, and they equal spec §3's strings:
- §P: C-NOTION, C-ART, C-HANDOFF, C-PLACE, C-DEC, C-LAT and C-VERSION;
- A1-5: C-SUB and C-DISPATCH;
- A1-8: C-TOP, and C-SESSION with the A1-8 sentence appended, tested in both backtick variants (spec §3 OQ-2);
- A1-6: the GCFPE override;
- the child: C-REPLAN, C-PROCEED, C-PR20-ENTRY and C-PR30-ENTRY;
- the literals of steps 4 and 22;
- three candidate wordings of PR-40's step-39 input.

Every text was also tested in its wrapped source form.

### 7.2 Step 43, first half: the release-identity requirements are removed from all 55 rows

These two entries are deleted from every row's `required_regex`. Each is an exact two-line pair (registry-audit:5; `D23-G`):

```
    - value: 'Prompt [Vv]ersion: `?091426\.1`?'
      rule_id: SRC-001
    - value: 'Ecosystem release: `?GCFPE-20260914\.1`?'
      rule_id: INV-003
```

§E records this as moving the release binding to the register (step 44), not as keeping it. Afterwards, the only release binding inside the audit is `expected_title` "— 091426.1", checked by `NAM-001` at WARNING severity and only when a title is supplied (registry-audit:5, invariant note). This half, and G12–G14 below, assume that steps 42–43 run in this run; see OQ-12.

### 7.3 The guards

Every value below was tested on a scratch copy:
- It compiles.
- It round-trips through YAML single quotes.
- A required value matches its home text, in both the joined and the wrapped form, and matches no other canonical text.
- A forbidden value matches no canonical text in either form. It also matches none of the four combined paragraphs below and none of the 16 worker or negated phrasings, which include the two named in the brief.
  - The combined paragraphs are C-PLACE + C-HANDOFF + C-SESSION + C-TOP; a handoff rule + C-HANDOFF + C-PLACE + C-TOP; C-PLACE + C-SESSION; and C-DISPATCH + C-SUB + C-TOP.
- Every regression gives exactly its own finding from the real evaluator (§7.10).

| id | ruling | step or item | list | rule_id | rows | source |
|---|---|---|---|---|---|---|
| G01 | Notion policy (Class B) | 7 | forbidden_regex | CTR-001 | ALL55 | step 7; registry-audit:6 |
| G02 | Notion policy | 7, functional companion | forbidden_regex | CTR-001 | ALL55 | registry-audit:6 as corrected by adversary:6 |
| G03 | Notion policy | 4 | forbidden_regex | CTR-001 | QA-10 | registry-audit:6 |
| G04 | Notion policy | 5 | forbidden_regex | CTR-001 | STEP5 (OQ-1) | registry-audit:6 |
| G05 | D23-A | 11 | required_regex | CTR-002 | NPH53 | step 11; registry-audit:2, :4 |
| G06 | D23-B content | 17 | forbidden_regex | TOP-001 | NPH53 | registry-audit:3 and notes; adversary:19 |
| G07 | D23-B placement | 18–19 | required_regex | TOP-001 | NPH53 | registry-audit:12 notes |
| G08 | D23-B, `ASK OK?` | 18–19 | forbidden_regex | CTR-002 | QA-60, QA-80, RS-10, RS-30 (OQ-3) | registry-audit:12 notes; adversary:14 |
| G09 | D23-C | 21 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | step 21 as corrected by adversary:5 |
| G10 | D23-C | 25 | required_regex | CTR-002 | LAT10 | step 25; registry-audit:12 notes |
| G11 | D23-C definition | 25 | required_regex | CTR-002 | LAT10 | registry-audit notes |
| G12 | D23-G | 43 | forbidden_regex | SRC-001 | ALL55 | registry-audit:5 and notes |
| G13 | D23-G | 43 | forbidden_regex | INV-003 | ALL55 | registry-audit:5 and notes |
| G14 | D23-G (`Set:`) | 43 | forbidden_regex | SRC-001 | ALL55 | registry-audit:5 and notes |
| G15 | D23-D, old continuity list | N3 | forbidden_regex | CTR-001 | step-32 rows (OQ-2) | registry-audit:12 notes |
| G16 | D23-D | N3 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | registry-audit:12 notes |
| G17 | D23-D, A1-8 clause | N3 | required_regex | CTR-002 | PR-30, PR-35, RS-40 | A1-8; coverage:5; adversary:5 |
| G18 | C-TOP required | N3 | required_regex | CTR-002 | MAIN54 | A1-8; coverage:5; adversary:5 |
| G19 | C-TOP forbidden F1 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0 |
| G20 | C-TOP forbidden F2 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0 |
| G21 | C-TOP forbidden F3 | N3 | forbidden_regex | CTR-001 | MAIN54 | A1-8; adversary:0, without `send_later` |
| G22 | D23-E, withdrawn launch | N3 | forbidden_regex | CTR-001 | PR-35, RS-40 | coverage:1 |
| G23 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40 | registry-audit:12 notes; adversary:4 |
| G24 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40 | registry-audit:12 notes; adversary:4 |
| G25 | D23-E | N3 | required_regex | CTR-002 | PR-35, RS-40, PR-40 | registry-audit:12 notes; adversary:4 |
| G26 | D23-F | child C5 | forbidden_regex | CTR-001 | PR-40 | child C5 |
| G27 | D23-F | child C5 | required_regex | CTR-002 | PR-20 | child C5 |

Each value below is quoted verbatim from its source; the table gives the source. Two values differ from the text of their finding:
- **G02** is adversary:6's corrected form, with `(?i)`.
- **G21** drops `send_later` from adversary:0's F3. A1-8 forbids "naming a session-creating tool", and `send_later` schedules a message into the same session and creates nothing.

G19 and G20 are adversary:0's F1 and F2 with `<PID>` expanded:

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

```
Concise authorized operational state and pointers remain `CONTROL_NOTION`.
```

- **G02 regression**, on PR-10 (adversary:6). Append:

```
Operational state and pointers stay in Notion.
```

G03 goes on QA-10 only:

```
    - value: 'Notion and repository persistence'
      rule_id: CTR-001
```

- G03 is silent on step 4's replacement, "repository persistence, Notion read-only unless a destination rule names the page".
- **G03 regression**, on QA-10. Append:

```
Use Notion and repository persistence for results.
```

G04 goes on the STEP5 rows (OQ-1):

```
    - value: 'Notion-resident artifact'
      rule_id: CTR-001
```

- **G04 regression**, on CF-C-10. Insert this sentence after the handoff sentence:

```
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

#### D23-B: G06 (step 17), G07 and G08 (steps 18–19)

G06 goes on NPH53:

```
    - value: 'NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,600}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)'
      rule_id: TOP-001
```

- **Clean.** G06 is silent on every canonical text and on the combined paragraphs. It is silent on C-HANDOFF's "It carries no branch and no commit" and on C-SESSION's "workspace/worktree".
- **Regression**, on PR-35. Insert the sentence below immediately after the sentence that contains `NEXT_PROMPT_HANDOFF`, in the same paragraph. The limit is in §7.4.

```
 It carries the same session, worktree, branch, PR and head commit.
```

G07 goes on NPH53:

```
    - value: 'ends with the `?NEXT_PROMPT_HANDOFF`? block'
      rule_id: TOP-001
```

- **Home: C-PLACE.** The pattern also matches spec §3's derived `ASK OK?` variant.
- **Regression**, on PR-35. Delete C-PLACE.

G08 goes on QA-60, QA-80, RS-10 and RS-30. Its adoption is open (OQ-3):

```
    - value: '\bends? `ASK OK\?`'
      rule_id: CTR-002
```

- **Clean.** G08 is silent on C-PLACE and on spec §3's derived variant ("`ASK OK?` is the line immediately before the block.").
- **Regression**, on QA-60. Append:

```
The final response must end `ASK OK?`.
```

#### D23-C: G09 (step 21), G10 and G11 (step 25)

G09 goes on PR-30, PR-35 and RS-40:

```
    - value: 'An\s+\*?In-flight decisions\*?\s+section'
      rule_id: CTR-002
```

- **Home: C-DEC.** It does not match C-LAT's "record it under *In-flight decisions*". That is why the literal `In-flight decisions` from step 21 is not used: C-LAT masks it on PR-30 and PR-35 (adversary:5).
- **Regression.** Delete C-DEC. It passes on PR-35, where C-LAT is also present, and on RS-40.

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

Each pattern is windowed to the first 8 nonblank lines of the body. That is `flowmaster-validate`'s header window, and it is where step 42 deletes the lines.

```
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_-]*(?:\*\*)?Prompt [Vv]ersion:'
      rule_id: SRC-001
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_-]*(?:\*\*)?Ecosystem release:'
      rule_id: INV-003
    - value: '\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_-]*(?:\*\*)?Set:'
      rule_id: SRC-001
```

- **Clean.** The patterns are silent on a header of the title, `Prompt ID:` and `Notion URL:`, and on C-HANDOFF's "full name, version and direct Notion URL".
- **Regressions**, on PR-35. Insert one line directly after the `Prompt ID:` line, once per guard. G12 and G14 share `SRC-001`, and their summaries differ by value.

```
Prompt Version: 091426.1
```
```
Ecosystem release: GCFPE-20260914.1
```
```
Set: GCFPE-20260914.1 / 091426.1
```

#### D23-D: G15, G16 and G17

G15 goes on the rows whose continuity-list paragraph step 32 replaces (OQ-2):

```
    - value: 'Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session'
      rule_id: CTR-001
```

- **Clean.** G15 is silent on C-SESSION ("original Proceed, workspace/worktree"). Do not forbid "same-session" broadly: PR-35's own `RECOVERY_PENDING` re-entry is legitimate (registry-audit notes).
- **Regression**, on PR-35. Append the old list. It is `EXACT_GCF17_CONTINUITY` from `amthor-workspace-governance-audit/scripts/run_fixture_suite.py:24`, and the same text sits at `glow-hde-pr-development/SKILL.md:55`:

```
The exact ordered ten-field GCF-17 continuity list is: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree; branch; pull request; PR instruction; detailed PR plan; primary skill authority; continuous recovery/artifact lineage.
```

G16 and G17 go on PR-30, PR-35 and RS-40, each with its own distinct pattern (A1-8; coverage:5):

```
    - value: 'they do not share a session'
      rule_id: CTR-002
    - value: 'never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30'
      rule_id: CTR-002
```

- **Homes.** G16's home is C-SESSION, in both backtick variants. G17's home is A1-8's C-SESSION sentence, and G17 does not match C-TOP.
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

```
    - value: '(?i)(?<!never )(?<!not )(?<!n''t )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b'
      rule_id: CTR-001
    - value: '(?i)(?<!never )(?<!not )(?<!no )(?<!n''t )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|the next prompt|the destination prompt|a main-ecosystem prompt)'
      rule_id: CTR-001
    - value: '(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b'
      rule_id: CTR-001
```

The `n''t` in G19 and G20 is the YAML escape for `n't`.

**Clean.** All three are silent on:
- C-TOP, including its word "starts". The first draft's C-TOP said "launches", and the withdrawn broad pattern matched C-TOP itself (coverage:0; sweep:1).
- The A1-6 override and the other canonical texts, and the four combined paragraphs.
- The worker phrasings `use subagents as workers within this task` and `spawn worker subagents for parallel reads within this session`, and 14 further worker or negated phrasings.
- `mcp__Claude_Code_Remote__send_later`.

**What they catch, measured:**
- **G19** catches 8 of 8 injections, capitalised forms included, such as "Run PR-35 as a subagent." and "dispatch PR-40 to a workflow agent".
- **G20** catches 7 of 7, such as "Launch a new session for PR-40." and "spawn a session to run PR-40".
- **G21** catches 5 of 5, such as the fully qualified `mcp__Claude_Code_Remote__create_session`, which has no leading word boundary.

**Regressions**, on PR-35. Append one line per guard:

```
Run PR-35 as a subagent.
```
```
Launch a new session for PR-40.
```
```
Use mcp__Claude_Code_Remote__create_session to open it.
```

#### D23-E: G22–G25

G22 goes on PR-35 and RS-40, and guards the launch option the `D23` clarification withdrew (coverage:1):

```
    - value: 'launched as a new session'
      rule_id: CTR-001
```

- **Clean.** G22 is silent on every canonical text. It matches the superseded §P C-DISPATCH, whose wording G20 does not catch.
- **Regression**, on PR-35. Append:

```
Emit the PR-40 handoff: paste-ready, or launched as a new session where the surface provides one.
```

G23 and G24 go on PR-35 and RS-40, and G25 goes on PR-35, RS-40 and PR-40 (registry-audit:12 notes; adversary:4):

```
    - value: '[Ss]ubscribe to the pull request'
      rule_id: CTR-002
    - value: 'do not poll'
      rule_id: CTR-002
    - value: 'observed merge event'
      rule_id: CTR-002
```

- **G23's value must stay quoted.** As a plain scalar it raises a `ParserError` (adversary:4).
- **Homes:**
  - G23 matches A1-5's C-SUB;
  - G24 matches A1-5's C-DISPATCH;
  - G25 matches A1-5's C-DISPATCH on PR-35 and RS-40. On PR-40 it matches PR-40's step-39 input text in all three candidate wordings (OQ-8).
- **Regressions**, each yielding only its own finding. On PR-35:
  - **G23:** delete C-SUB;
  - **G24:** delete ` and do not poll`;
  - **G25:** delete the sentence "The observed merge event is the fact PR-40 is entered on; `PR-40` still verifies the merged state and landed lineage independently."

  On PR-40, delete the step-39 input sentence (G25). Deleting all of C-DISPATCH yields two findings, so it is not a valid regression.

#### D23-F: G26 and G27 (child C5)

G26 goes on PR-40:

```
    - value: 'original Proceed and a suitable actual authorized implementation vehicle'
      rule_id: CTR-001
```

- **Clean.** G26 is silent on C-REPLAN.
- **Regression**, on PR-40. Append:

```
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
- The window is 600 characters from the last `NEXT_PROMPT_HANDOFF` in the same paragraph. C-HANDOFF alone is 746 characters.
- Measured: the regression sentence appended at the end of the C-HANDOFF paragraph, 785 characters from the token, is **not** caught. The same sentence 450 characters away is caught.
- A bare "names the branch and the commit" is not caught (adversary:19).
- In DOC-20 and PR-40, "commit identity" text may sit near a handoff. Any such hit at E4 is settled by reading the body back, never by exemption (registry-audit:3). See OQ-13.

**G19 (F1).**
- It misses "running", "executed", "invoked" and "executing" before a prompt id. It misses the passive "PR-35 is run as a subagent" and a pronoun such as "run it as a subagent".
- It fires on prohibitions that are not negated immediately before the verb:
  - "It is forbidden to run PR-35 as a subagent.";
  - "Do not ever run PR-35 as a subagent.";
  - "PR-35 must never be used to run PR-40 as a subagent.".
- It also fires on "subagents run PR-35's tests in a subagent".

**G20 (F2).**
- It misses a bare "launch a new session." that names no prompt. A1-8 states this itself and assigns it to the governance audit's semantic invariant.
- It also misses "created a session for PR-40".
- It fires on "No agent may launch a new session for PR-40.", on "without launching a new session for PR-40" and on "Nathan, not the agent, may open a new session for PR-40." The last is a sentence the new model permits (OQ-14).

**G21 (F3).** It catches only the four tool names. `send_later` is excluded deliberately.

**Masking on real bodies.**
- A required guard's deletion regression fails if the edited body carries the pattern in a second place. For example:
  - an existing "do not poll" in PR-35 or RS-40 (G24);
  - "ends with the `NEXT_PROMPT_HANDOFF` block" in one of the 16 formerly "contain" bodies (G07);
  - a second "observed merge event" (G25).
- Bodies were not read, so this is known only at E4. There, E4 item 9 fails for that guard and EXECUTE stops (OQ-15).

**Other windows and forms.**
- G12–G14 do not look past the first 8 nonblank lines.
- G15 catches only the "Proceed; dedicated PR-development session" form.

### 7.5 `D13`-derived fields: the registry deriver

**The rule.** It reproduces all 55 rows today with 0 drift (registry-audit notes, measured again here). It uses union semantics over `outputs[]`: IA-40 has two outputs, and a per-list comparison reports false drift there.

```
for each row r, with P = the E1-built part docs/graph/parts/prompts/<r.prompt_key>.json:
  derived = sorted({e["to"] for e in P["edges"] if e["to_kind"] == "prompt" and e["to"] != P["id"]})
  r["required_interfaces"] == derived                                    # list equality; always sorted today
  set().union(*(o.get("consumers") or [] for o in r["outputs"])) == set(derived)
  set().union(*(o.get("states") or [] for o in r["outputs"])) == set(P["node"]["result_states"])
```

**What the deriver rewrites.** It rewrites only the rows whose derived sets change, and in those rows only `outputs[].consumers`, `outputs[].states` and `required_interfaces`. Against the simulated parts (`route_sim_final.py`, sha256 `e0854a55…`, reproduced here), exactly three rows change: `PR-35`, `PR-40` and `RS-40` (A1-2).
- Consumers are written sorted. Ten other rows keep today's unsorted consumer order untouched.
- `session_class`, `session_role` and `creator_role` are authored, not derived (registry-audit notes). They are in §7.6.

PR-35 (`:3616-3624`, `:3682-3683`):

```
  outputs:
  - artifact: PR_IMPLEMENTATION_RESULT
    states:            # set: {MERGE_PENDING, MERGE_OBSERVED, PRODUCT_OWNER_DECISION_REQUIRED, RECOVERY_PENDING, REMOTE_EVIDENCE_PENDING, RESCOPE_PENDING}
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
    states:            # set: today's seven plus MERGE_OBSERVED
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

Where `MERGE_OBSERVED` sits inside the two `states` lists is open (OQ-4). Either position passes the drift check and the semantic diff, because both compare sets.

**Checks.** Run in E1 after the graph build, and again in E4.
- **Acceptance.** Today's registry against today's parts gives drift `[]`.
- **Post-edit.** The edited registry against the E1 parts gives drift `[]`.
- **Must-fail.** Each negative control reports exactly the listed rows:
  - the unedited registry against the E1 parts gives `['PR-35', 'PR-40', 'RS-40']`;
  - re-injecting `PR-30` into PR-40's consumers gives `['PR-40']`;
  - removing `MERGE_OBSERVED` from RS-40's states gives `['RS-40']`.

### 7.6 Authored row edits

Each edit replaces one exact line, or inserts after one. A new string is written single-quoted whenever its plain form does not round-trip. Measured:
- the plain form fails for PR-35 role option (a), RS-40's example role, the PR-35 input and the PR-20 input;
- `- session_disposition: NEW_DEDICATED …` unquoted parses as a mapping (registry-audit:7).

**Step 26 — PR-30, `:3531`**, `mutations.allowed`. Old:

```
    - Implement, test, commit, publish, and review-correct the exact proceeded PR work unit
```

New:

```
    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35
```

The verification is `grep -c review-correct` = 0, measured 0.

**Step 33 — PR-35** (registry-audit:7, :8 and notes; A1-8).
- `:3604`: `  session_class: DEDICATED_PR_REVIEW_SESSION`.
- `:3605` `session_role`. It equals the graph's `PR-35.json` `node.receiving_role` verbatim, and it carries the A1-8 clause. The string is open (OQ-5; spec §4 OQ-6). Option (a) must be single-quoted; option (b) round-trips plain.
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

**Step 39, and the other PR-40 inputs** (registry-audit:9; coverage:3, :18).
- `:3708` replaces "the dedicated PR session identity" with "the PR-30 and PR-35 session identities":

```
  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change IA context and exact return owner
```

- `:3710`, today "Nathan's later invocation asserting the identified PR was manually merged after PR-35 produced MERGE_PENDING". Its wording is open (OQ-8). The only candidate that uses A1-5's single fallback predicate is the registry-audit notes' sentence with its predicate replaced, as coverage:3 directs:

```
  - The observed merge event for the identified PR, delivered to the subscribed PR-35 session, or Nathan's assertion that he manually merged it only where no MERGE_OBSERVED result was returned for this merge
```

- `:3705`, the PR-35-result input, must accept `MERGE_OBSERVED` (coverage:18). No wording is given (OQ-8).

**Child C5 — PR-20.** Insert after `  - PR_INSTRUCTION_ID` (`:3429`), as a quoted string. Whether the backticks are literal is open (OQ-9):

```
  - '`PR_WORK_UNIT_LINEAGE_REVIEW` with `REJECT` (`reject_replan`) and its in-scope finding, for a re-plan of the same `WORK_UNIT_ID` in a new dedicated session Nathan seeds'
```

The next postflight should restate check (f) by its real criterion, "no QA Guide or QA Plan", and not as "exactly `[PR_INSTRUCTION_ID]`" (registry-audit:11). That is a note for the postflight, not a registry edit.

**RS-40 `session_role`, `:5108`.** Today it reads "You are the same dedicated PR engineering session for the exact suspended work unit." It changes together with the graph's `RS-40.json` `node.receiving_role` to one identical string (registry-audit:9; coverage:18).
- The only text on record is registry-audit:9's example. It contains ": ", so it must be single-quoted. The string is open (OQ-6; spec §4 OQ-8).
- Whether `creator_role` (`:5109`) also changes is open too.

**PR-20 and PR-40 roles.** Their changes are open (OQ-7; sweep:15; spec §4 OQ-9).

### 7.7 Role parity check for the D23 clarification (coverage:6)

The `D23` clarification requires a guard on "the graph role and the registry role for each affected prompt". No registry assertion reads `session_role`, so E4 item 8 adds this check, in memory:

```
registry["PR-35"]["session_role"] == graph PR-35.json ["node"]["receiving_role"]     -> else ROLE_PARITY
<clause phrase> in graph PR-35.json ["node"]["receiving_role"]                        -> else ROLE_CLAUSE
```

- **The clause phrase follows OQ-5:**
  - under option (a) it is `never a subagent of another session`, coverage:6's phrase;
  - under option (b) it is `never as a subagent, forked agent or workflow agent of PR-30`.
- **Must-fail regressions**, measured for both options:
  - removing the clause from the registry role only yields `ROLE_PARITY` alone;
  - removing it from both yields `ROLE_CLAUSE` alone.
- **The contract side** is §5/§8. It is `flowmaster-validate`'s literal on `member_registry['PR-35'].receiving_role`, and the regenerator copies that role from the graph.

### 7.8 N1 and N2

These come from the first draft's N1 and N2, carried by registry-audit:17, :18, sweep:18 and :23. The amendment does not contradict them. Their wording and placement are open (OQ-10, OQ-11).

**N1, in the registry.** A dated disposition. It is inserted, and no existing dated statement is edited (`AUTH-001`). It states:
- **Which identities are stale.** Both identities on all 55 rows describe the pre-`D23` (pre-2026-09-23) bodies and no longer identify the live bodies:
  - the `evidence_contract` byte counts and SHA-256;
  - the `source_snapshot` `sha256`, `bytes` and `completeness` (sweep:23). `applies_to` (`:80-82`) already records these as the 2026-09-17 pre-merge extraction. N1 adds that they do not identify the edited bodies either.
- **Why they are not regenerated.** Hashing bodies is prohibited: `prompt-corpus-policy.md:104` says "Never an identity. Not hashed, not byte-compared", and `:110` lists "body hashes" among what is still prohibited.
- **Which claims it supersedes.** The identity claims at registry `:39` (the `authority_sources` note, "…are the reproducible identity"), `:55-56` (`row_wording_disposition`) and `:79-80` (`body_extraction_convention.applies_to`, "…which are the body identity for validation").
- **Nothing breaks.** No live check consumes these values: the SF10-12 pins are retired. The retired bench `docs/ephemeral/gcfpe.round20.sf10-bench/bench.py` would report a mismatch on every edited body (registry-audit live-window notes).

**N1, outside the registry.**
- `authoritative-surfaces.md:59` is corrected to match: its description still says "with `evidence_contract` byte count and SHA-256 per prompt".
- `authoritative-surfaces.md:29` and `:45-46`, and `ecosystem-change-management.md:143`, still state the old graph token "55 nodes · 227 edges · 55 state_routes · 569,902 bytes · sha256 1d0b7258…". Today's build is 569835 B / `90021eb7…`. Each is either restated with the E4 item-1 token after the merge, or labelled as dated (sweep:18).
- `ecosystem-change-management.md:176` changes "carries" to "carried, until D23-G removed them," (sweep:18).

**N2, at `ecosystem-change-management.md:141`.** Today it reads: "499 assertions across 55 prompts, 0 failing. `required_regex` binds release identity and Canon source; `forbidden_regex` guards D7 against Drive reintroduction in any of its four forms."
- After §7.2 and §7.3 the sentence must not claim the release-identity binding, and it drops the count rather than pinning it again (registry-audit:18; r27 W2).
- The count was 831 today. It is 1429 on the prototype, and it varies with OQ-1 and OQ-2.
- The replacement wording is open (OQ-11).

### 7.9 Method: line-anchored insertion and a `load_data` semantic diff (A1-2; registry-audit:19; coverage:24)

**How the script edits the file.**
- It edits the Markdown file's lines, and never round-trips YAML: `yaml.safe_dump` would reflow and requote the whole 5301-line file.
- A row's range runs from the line `- prompt_key: <KEY>` to the next line `- prompt_key: ` or `global_literals:`.
- Every operation names its row and an exact anchor line. Within the row, that anchor occurs exactly once, or first after a named sub-anchor such as `    consumers:` or `  required_interfaces:`. Otherwise the script stops.
- Removals delete an exact two-line pair.
- Appends go after the last item of the named list.

**Order within E1:**
1. graph parts, then the build (spec §4);
2. the deriver (§7.5);
3. §7.2, §7.3 and §7.6;
4. N1;
5. the checks below.

**Checks after the edit.** Each must hold.
1. **`load_data(old)` against `load_data(new)`.**
   - Top-level keys other than `prompts` are unchanged, except N1's new key.
   - The 55 rows keep their set and order.
   - Per row, the multiset difference of `(value, rule_id)` in each assertion list is exactly the two §7.2 removals plus the guards §7.3 selects for that row.
   - Kept entries keep their order.
   - The non-assertion fields that change are exactly: PR-20 `inputs`; PR-30 `mutations`; PR-35 `creator_role`, `inputs`, `mutations`, `outputs`, `required_interfaces`, `session_class` and `session_role`; PR-40 `inputs`, `outputs` and `required_interfaces`; RS-40 `outputs`, `required_interfaces` and `session_role`. RS-40 `creator_role` joins the list if OQ-6 changes it.
2. **Every item of every `inputs` list is a `str`.**
3. **The structure check.** From a scratch copy of the skill, run the command below. It must return `{"valid": true, "problems": []}`.

```
PYTHONDONTWRITEBYTECODE=1 python3 <scratch>/wga/scripts/validate_project_prompt_registry.py <branch>/docs/prompt_ecosystem_management/project-prompt-contract-registry.md
```

4. **The §7.5 drift checks and their negative controls.**
5. **The §7.3 and §7.7 evaluations, at E4 on the E3 bodies.** No snapshot is taken, no hash is computed, and nothing is written that embeds a body digest (E4; registry-audit:0).

**Live window** (registry-audit, live-window notes).
- From the merge until the cut-over lands the bodies, `main`'s registry fails against the unedited live bodies: the new required guards are absent from them. That falls inside the A1-4 freeze.
- The cut-over re-scan uses the registry at the merge commit (A1-4 item 5).
- The registry path is CI-exempt (`_DOCUMENTATION_PREFIXES`), so every check here is run by the agent.

### 7.10 Measured, on scratch copies under `/tmp/claude-0/spec/s7-registry/`

Every run used `PYTHONDONTWRITEBYTECODE=1`. The scripts:

```
2a8b5b683a85663b54ce3e72b0f29dc34880d7b230473e9b6fdc6bc0270dc7a0  texts.py
93d910e89e0d6a30a1d16027085bffa3737af596ea1598c43bc01b9d606b4db6  guards.py
2c93c6f8ffb00d25cf002c30f0ff31beb33eb09c495632e95799eeecef2c8c93  test_static.py
ba7be6521b7c5f011c669fc51a8b0948b079fe9e9c9515d55c40c62f79b900ff  test_dynamic.py
caad960c7b8249f9840a9818a39c98cd316051399653f03b6c7092c6717062d9  apply_registry.py
0883de989f1c7ff4c41927d68d3bdf3cee55fc4507c9ee892c38b6f469981ceb  semdiff.py
```

**Canonical texts.**
- The extracted texts equal spec §3's strings, all 16 compared.

**Static tests:**
- All 27 guards compile and round-trip through YAML single quotes.
- The 12 required guards each match their home texts, joined and wrapped, and match no other canonical text.
- The 15 forbidden guards each match no canonical text, no combined paragraph and no worker or negated phrasing.
- `STATIC FAILURES: 0`.

**Registry prototype, 5301 → 6504 lines:**
- The semantic diff is exactly as §7.9 lists.
- Guard row counts: G01 55, G02 55, G03 1, G04 10, G05 53, G06 53, G07 53, G08 4, G09 3, G10 10, G11 10, G12 55, G13 55, G14 55, G15 3, G16 3, G17 3, G18 54, G19 54, G20 54, G21 54, G22 2, G23 2, G24 2, G25 3, G26 1, G27 1.
- Assertions go from 831 to 1429.
- The structure check returns valid true with no problems, exit 0.
- Both `MERGE_OBSERVED` positions pass.

**Deriver:**
- `route_sim_final.py` (copy) reproduces `('fecc319bdd4ce7ee6201cb77d7231861', 284)`, 229 edges, 574175 B, `b1911cf5…`.
- The drift checks give the results in §7.5, including all three negative controls.

**Regressions, real evaluator:**
- Synthetic bodies are built only from canonical texts, in two handoff layouts.
- Clean: 0 new-guard findings on 55 rows × 2 layouts.
- 32 regression cases × 2 layouts: all yield exactly their own `(rule_id, observed.summary)`. `REGRESSION FAILURES: 0`.

### 7.11 Dispositions of the registry findings

| finding | disposition |
|---|---|
| registry-audit:0, :1 | the gate method and its pass criteria are spec §9 items 8–9; §7.1 uses them |
| registry-audit:2 | NPH53 selector, §7.1; G05–G07 |
| registry-audit:3 | G06; limits in §7.4 |
| registry-audit:4 | G05 |
| registry-audit:5 | §7.2; G12–G14; the NAM-001 note goes to §E |
| registry-audit:6 | G01–G04 (G02 as corrected by adversary:6); G04's rows are OQ-1 |
| registry-audit:7, :8 | PR-35 edits, §7.6; the role is OQ-5 |
| registry-audit:9 | PR-40 `:3708`, §7.6; the RS-40 role is OQ-6 |
| registry-audit:10 | deriver, §7.5 (PR-35, RS-40); its "automatic edge becomes true" premise is superseded by A1-5 |
| registry-audit:11 | deriver (PR-40), PR-20 input, §7.6; the postflight check (f) note |
| registry-audit:12 | G07, G08, G15–G17, G23–G27; G08 is OQ-3 |
| registry-audit:13–16 | skill text in `amthor-workspace-governance-audit`, the fifth package: spec §8, not the registry |
| registry-audit:17 | N1, §7.8 |
| registry-audit:18 | N2, §7.8 |
| registry-audit:19 | §7.9 |
| registry-audit:20 | the `session_class` enum doc is skill text, spec §8; no registry change |
| coverage:0; sweep:1 | resolved by A1-8's C-TOP ("starts") and adversary:0's F2 (G20); coverage:0's unnamed-object pattern is not adopted, because A1-8 forbids "creating a session to run a named prompt" |
| coverage:1; sweep:2; adversary:4 | G22–G25 (the `exact_markers` literal in sweep:2 is spec §8) |
| coverage:2; sweep:0; adversary:1 | RS-40 in the deriver's row set, §7.5 |
| coverage:3, :18 | PR-40 inputs, §7.6; OQ-8 |
| coverage:5; adversary:5 | G09, G17, G18 |
| coverage:6 | §7.7 |
| coverage:24 | §7.9; registry-audit:20 goes to spec §8 |
| coverage:27 | G18 on PR-50, with its regression |
| sweep:15 | OQ-7 |
| sweep:18, :23 | N1, §7.8 |
| adversary:0 | G19–G21; `send_later` excluded under A1-8 |
| adversary:6 | G02; every value is in a code block |
| adversary:14 | OQ-3 |
| adversary:15 | §7.1 |
| adversary:19 | §7.4 |
| adversary:20 | G27's clean control |

### 7.12 Open questions

1. **OQ-1, G04's rows.** Options: (a) the 10 step-5 rows; (b) all 55. Registry-audit:6 offers both, and the prototype used (a).
2. **OQ-2, G15's rows.** Step 32's body set (~17) is known only at E3, after E1's registry edit. G16 and G17 also assume that PR-30, PR-35 and RS-40 carry C-SESSION. Options:
   - (a) land G15 on PR-30, PR-35 and RS-40 in E1, then amend the registry on the branch after E3 with the full step-32 set, before E4;
   - (b) all 54 main rows, with E4's clean control;
   - (c) PR-30, PR-35 and RS-40 only.
3. **OQ-3, the `ASK OK?` ordering guard.** G08 bans a wording and does not check order (adversary:14), and the `ASK OK?` variant of C-PLACE has no canonical wording (spec §3 OQ-1). Options:
   - (a) G08 alone, recording that order is unchecked;
   - (b) a required pattern derived from the variant once it is worded, with a line-reorder regression;
   - (c) both.
4. **OQ-4, where `MERGE_OBSERVED` sits in PR-35 and RS-40 `outputs[].states`.** Options: (a) ASCII order, as both lists are sorted today, which puts it before `MERGE_PENDING`; (b) A1-5's vocabulary order, which puts it after `MERGE_PENDING`.
5. **OQ-5, the PR-35 role string** (spec §3 OQ-3, §4 OQ-6), which sets the §7.7 phrase. Options: (a) the first draft's string, which needs single quotes; (b) step 30's string followed by the A1-8 clause.
6. **OQ-6, the RS-40 role** (spec §4 OQ-8). Options: (a) registry-audit:9's example; (b) another string. Also open: whether RS-40's `creator_role` changes with it.
7. **OQ-7, the PR-20 and PR-40 roles** (sweep:15; spec §4 OQ-9). Options: (a) append C-TOP's top-level clause to both, as identical graph and registry strings; (b) a `D23` successor note saying that body-level C-TOP and G18–G21 carry the rule.
8. **OQ-8, PR-40's inputs.** `:3710`: (a) the A1-5-substituted sentence in §7.6; (b) wording Nathan gives. `:3705` has no wording for accepting `MERGE_OBSERVED`.
9. **OQ-9, backticks in the PR-20 input.** Options: (a) literal, as child C5 prints them; (b) none, as in registry-audit:11 and in all 182 of the registry's inputs today.
10. **OQ-10, N1's wording and position.** Options: (a) a new key under `body_extraction_convention`; (b) a top-level key. Also open: the `authoritative-surfaces.md:59` wording, and whether the token lines are restated with the post-merge token or labelled dated.
11. **OQ-11, N2's sentence.** Registry-audit:18's "`required_regex` now binds only the Canon source" becomes false once G05, G07, G09–G11, G16–G18, G23–G25 and G27 land. The `forbidden_regex` clause also becomes incomplete. Options: (a) registry-audit:18's wording as it stands; (b) a sentence naming the Canon source and the `D23` wordings, without a count. No text is given for (b).
12. **OQ-12, steps 42–43 in this run.** The amendment does not amend them, but A1-3 applies C-VERSION, whose last sentence they implement, "from the next release". Options:
    - (a) they run now, as compiled here;
    - (b) they are deferred: §7.2 and G12–G14 drop out, and the two required entries stay.
13. **OQ-13, G06's 600-character window.** It cannot reach past C-HANDOFF, which is 746 characters. Options: (a) keep it and record the limit; (b) widen it. No finding gives a value for (b).
14. **OQ-14, G19 and G20.** They miss several inflections and fire on some prohibitions and on "Nathan, not the agent, may open a new session for PR-40." Options:
    - (a) adopt them as tested; E4's clean control over the 54 edited bodies decides, and any hit goes to Nathan, never exempted (registry-audit:3);
    - (b) revise the patterns. No finding gives values.
15. **OQ-15, masking on real bodies** (G07, G24, G25). If an E3 body carries the pattern twice, the regression cannot fire. Options: (a) stop at E4 and bring it to Nathan; (b) move to a C-DISPATCH-anchored value. No finding gives one.

## §8a Skill edits: glow-hde-pr-development and amthor-workspace-governance-audit

This section compiles every edit EXECUTE makes, at E2, to two of the six packages (A1-6):
`glow-hde-pr-development` (4 files) and `amthor-workspace-governance-audit` (15 files). It decides
nothing. Where the amendment, the child plan and the findings leave more than one result, the line
carries an `O`-number, and the options are listed under this section's open questions.

### 8a.0 Conventions

- **Line numbers** are those of the installed files whose digests §2 records
  (`glow-hde-pr-development` `e109d47a…`, `amthor-workspace-governance-audit` `6cd088a0…`). E2
  applies each edit by its `old:` span, on a scratch copy, as a scripted exact-substring
  replacement that asserts the span occurs exactly once. Insertions shift later lines, so line
  numbers identify, and spans locate.
- **No whole-line replacement** where a kept literal sits on the line (amendment defect 12). Every
  `old:` span below either stops short of a kept literal or carries it into `new:` unchanged
  (`:22`'s second span restores `v:52`'s tail).
- **The compile rule.** Canonical texts go in verbatim (§P: "written once … never re-authored per
  prompt"). Words that state a reversed rule are deleted; they are replaced only by words taken
  from a canonical text, the A1-7 table or a finding. Everything else on the line is untouched.
  Where that rule still leaves a choice, the line is marked `O`.
- **Tokens in code blocks.** `{C-X}` stands for §3's text of C-X, byte-exact; `{C-SESSION}` is §3's
  compiled form (backticks dropped, A1-8's sentence appended; §3 open question 2). The other tokens
  are defined here:

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
```

  - `{NINE}` is `{TEN}` without "dedicated PR-development session;", as step 29 removes it from
    `pr_continuity_contract.shared_exactly_one`, with "ten-field" read as "nine-field"
    (pr-relay-graph:1, fv-main:24, fv-rest:18, registry-audit:15).
  - `{V6}` is A1-5's ordered vocabulary (sweep:3, adversary:9, coverage:14).
  - `{FALLBACK}` is A1-5's single fallback predicate, "worded one way everywhere" (coverage:3,
    coverage:16).
  - `{LANDED}` is C-PR20-ENTRY's last sentence (child C6, sweep:16).
- **How the PR skill's validator reads.** `required` is a case-sensitive substring test on
  `SKILL.md + "\n" + behavior-cases.md`. `forbidden` is case-insensitive on the same text.
  `case_headings` are tested in `behavior-cases.md` only. The script is fail-fast: it prints the
  first failure and exits 1. So a forbid regression is written in **injection form** (the old text
  is added and the new text is left in place), which makes exactly one check fire.
- **Literal dispositions.** `v:N` is `validate_glow_hde_pr_development.py` line N. **KEEP** means
  verbatim and still present after the edit. **REPLACE** gives a new literal. **FORBID** adds the old
  text to `forbidden`. **NEW** adds a required literal.
- **Literal map.** A script run on a copy
  (`/tmp/claude-0/spec/s8a/work/litmap.py`, sha256 `4ab18ac9…`) parsed the validator's AST and
  located each literal. All 60 required literals occur today; none of the 11 forbidden ones does.
  Every heading in `case_headings` is present. The occurrences that matter here:
  - `v:32` at `:10` and `:53`;
  - `v:35` at `:22`, `:53`, `:57`, `:82`, `:164`, cases `:7`, `:11`, `:21`;
  - `v:53` at nine sites;
  - `v:57` and `v:74` at `:132` and cases `:49`;
  - `v:64` at `:10`, `:55`, `:141` and cases `:13`;
  - `v:82` at `:110` and cases `:87`;
  - every other literal on exactly one line, named below.

### 8a.1 `glow-hde-pr-development/SKILL.md`

**`:3` — description, the trigger surface.** Step 35 ("the description changes"). No literal sits
on this line. Glue: O22.
```
old: Glow HDE PR work unit in its single dedicated development session across
new: Glow HDE PR work unit, run in two dedicated sessions, across
```

**`:8` — revision.** From the amendment's *New revisions* (1.3.0); the pins are in 8a.5.
`v:26` REPLACE.
```
old: `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5`
new: `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0`
```

**`:10` — "Complete one approved PR work unit…".** Step 35 and child C6 ("C-PROCEED at `:10`"),
as one combined edit. Its session element is deleted: C-SESSION goes in at `:53`. Its Proceed
element takes C-PROCEED's first-sentence words.
- `v:31` "PR-30 and PR-35 are two phases of the same native PR-execution authority": KEEP. The
  sentence is untouched (pr-relay-graph:4).
- `v:32`: REPLACE and FORBID (8a.3). This is one of its two occurrences.
- `v:64`: KEEP. It still occurs at `:55` and `:141`.
- Cross-surface: `validate_gcfpe_current.py:652` reads this phrase (8a.6).
```
old: Keep the existing GCFPE actor, one dedicated PR-development session, one original Product Owner Proceed, scope, and manual-merge boundaries intact.
new: Keep the existing GCFPE actor, one Proceed per approved per-PR plan, scope, and manual-merge boundaries intact.
```

**`:17`–`:18` — Proceed intake items.** Child C6 ("C-PROCEED at `:17-18`"). O3. The simulated
option (a), shown below, leaves `:18` unchanged.
```
old: detailed PR implementation Plan covered by the original Proceed, with
new: detailed PR implementation Plan covered by the Proceed, with
```

**`:22` — PR-35 / RS-40 intake item.** Step 14 (C-HANDOFF) and step 35 (pr-relay-graph:5).
"same-session" is deleted. The trailing lineage clause is O4.
- `v:52` "only when `PR_RETURN_PHASE: PR-35`, the PR-35 handoff": KEEP.
- `v:35`: KEEP.
```
old: the complete `PR_CANDIDATE_PUBLISHED` result and same-session PR-35 handoff;
new: the complete `PR_CANDIDATE_PUBLISHED` result and PR-35 handoff;
```
O4, option (a), simulated:
```
old: , the PR-35 handoff; in either case require the exact workspace/worktree, branch, open PR and remote-head lineage;
new: , the PR-35 handoff;
```

**`:27` — "Proceed authorizes the bounded engineering lifecycle…".** Step 35 and child C6, as one
combined edit (sweep:4, pr-relay-graph:14).
- No literal sits on this line today.
- **FORBID** `followed in the same session by PR-35` (child C6).
- **NEW** the C-PROCEED literal (8a.3, O9).
```
old: coherent initial publication followed in the same session by PR-35 review remediation
new: coherent initial publication followed by PR-35 review remediation
```
```
old: only for its explicit scope; continuation preserves the original Proceed and never requires or creates a second Proceed.
new: only for its explicit scope. {C-PROCEED}
```

**`:43`–`:44` — recovery steps 3 and 4.** Child C6 names them "`:41` (recovery steps 3 and 4)".
The numbered list starts at `:41`, so steps 3 and 4 are `:43` and `:44` (sweep:16). This compile
corrects the anchor; the steps it names are unambiguous.
- `:43`: O5. Simulated option (a):
```
old: 3. Match prior work using evidence such as
new: 3. Match prior work of the current plan cycle using evidence such as
```
- `:44`: `{LANDED}` is appended after one space (child C6, sweep:16).
```
old: Reconcile partial or ambiguous external effects before retrying them.
new: Reconcile partial or ambiguous external effects before retrying them. {LANDED}
```
- `v:39` "Recover before creating work" (the heading at `:37`): KEEP.

**`:53` — the two-phase paragraph.** Step 35, with A1-8's clause carried inside `{C-SESSION}`.
- `v:32`: REPLACE and FORBID (second occurrence).
- `v:33`, `v:34`: KEEP (pr-relay-graph:3).
- `v:35`: KEEP.
- `v:38`: REPLACE and FORBID (pr-relay-graph:0).
- **NEW** the literal `run in two dedicated sessions`, which is `v:32`'s new value.
- **NEW** the top-level literal (A1-8).
```
old: Remain in the one dedicated PR-development session across both phases.
new: {C-SESSION}
```
```
old: followed by exactly one complete same-session `PR-35` handoff.
new: followed by exactly one complete `PR-35` handoff to the dedicated PR-35 session.
```
The "adds no … session" list is O7. Option (a), simulated:
```
old: The phase boundary adds no actor, session, work unit,
new: The phase boundary adds no actor, work unit,
```

**`:55` — the continuity list.** Step 35 (pr-relay-graph:1).
- `v:55`: REPLACE and FORBID.
- `v:64`: KEEP.
- The sentence after the list is untouched.
- Cross-surface: `flowmaster-validate` `:2594` (8a.6).
```
old: {TEN}.
new: {NINE}.
```

**`:57` — result vocabularies.** Step 38 and A1-5 (coverage:14, sweep:3). Only the PR-35 list
changes.
- `v:36` (the PR-30 vocabulary, on the same line): KEEP.
- `v:37`: REPLACE and FORBID.
- The RS-40 sentence stays: RS-40 "returns only that phase's lawful result", and that result now
  includes `MERGE_OBSERVED` (A1-5).
```
old: The PR-35 result vocabulary is exactly `MERGE_PENDING`, `RESCOPE_PENDING`,
new: The PR-35 result vocabulary is exactly `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,
```

**`:59` — not edited.** Step 20's anchor moves to `:108`, because `:59` never names
`PR_IMPLEMENTATION_RESULT` (pr-relay-graph:10).
- `v:49`, `v:50`, `v:51`: KEEP.
- The `flowmaster-validate` marker `PR_REMOTE_ACTION_LEDGER` at `:2592`: KEEP (fv-main:25).

**`:65`, `:126`–`:135` — C-LAT.** Step 24 (pr-relay-graph:12). Placement is O2.
- The numbered procedure at `:130`–`:133` stays intact. `v:56`, `v:57`, `v:58`, `v:61` and `v:74`
  sit there: KEEP.
- **NEW** `Decide it during work`.

Simulated option (a): C-LAT goes after the `:126` heading, and `:128`'s threshold takes the D23-C
term that the A1-7 rows use.
```
old: ## Route a real material boundary

When repository evidence proves that the approved work unit cannot be completed without changing approved scope, architecture, requirements, or Plan authority:
new: ## Route a real material boundary

{C-LAT}

When repository evidence proves a material change, as defined above:
```
```
old: route a substantiated material boundary through the existing rescope path.
new: route a substantiated material change (as defined below) through the existing rescope path.
```
- `{C-LAT}` is §3's two paragraphs plus the numbered list, with each item on its own line.
- `:135` is compiled unchanged. It holds no words C-LAT reverses: "Ordinary in-scope difficulty or
  review correction is not rescope" agrees with C-LAT.

**`:77` — PR reuse.** Child C6 ("one branch and one PR per plan cycle at `:77`"). Whether `:77`
also repeats `{LANDED}` is O6.
```
old: Reuse an existing PR for the same branch/work unit instead of creating another.
new: Reuse an existing PR for the same branch/work unit in the current plan cycle instead of creating another.
```

**`:79` — push bundling.** Step 27. The second sentence, "Never push merely to trigger another
remote run.", is kept. pr-relay-graph:13 records that "the change keeps this rule", and no ruling
removes it. No literal sits on this line.
```
old: - Bundle related implementation or review corrections into one locally verified push when practical.
new: - Bundle related implementation changes into one locally verified push when practical.
```

**`:82` — PR-30's stop and handoff.** Step 14 (C-HANDOFF: the field list goes), step 35 (the PR-35
session) and child C6 (per plan cycle).
- `v:35`: KEEP.
- The last sentence is O6. Option (a) is simulated below.
```
old: that invokes the exact selected PR-35 in this same dedicated session with all repository, worktree, branch, PR, remote-head, artifact, test, constraint, unresolved-item, and original-Proceed lineage.
new: that invokes the exact selected PR-35 in the dedicated PR-35 session.
```
```
old: or create another PR/session/Proceed.
new: or create another PR/Proceed in this plan cycle, or any session.
```

**`:100` — merge-readiness loop.** Step 35 (sweep:4, coverage:17). `v:44`: REPLACE and FORBID.
```
old: Continue in the same dedicated PR session until all applicable predicates are true:
new: Continue in this phase's own dedicated session until all applicable predicates are true:
```

**`:108` — the result artifact.** Step 20, re-anchored here (pr-relay-graph:10). The artifact is
named here, and C-DEC is added verbatim as a nested item. C-DEC opens with "An", so it cannot run
on inside the sentence. Glue: O22.
- **NEW** `An *In-flight decisions* section` (adversary:5). The bare `In-flight decisions` is not
  used: C-LAT's "record it under *In-flight decisions*" would mask its deletion regression.
```
old: - the complete PR implementation result and handoff artifacts are saved and read back.
new: - the complete PR implementation result (`PR_IMPLEMENTATION_RESULT`) and handoff artifacts are saved and read back; `PR_IMPLEMENTATION_RESULT` includes:
  - {C-DEC}
```

**`:110` — `MERGE_PENDING`.** Step 40: C-DISPATCH is appended after the existing sentences, which
stay (pr-relay-graph:7).
- `v:45`, `v:46`, `v:81`, `v:82`: KEEP.
- The `flowmaster-validate` marker at `:2593`: KEEP.
```
old: or keep polling for that manual action.
new: or keep polling for that manual action. {C-DISPATCH}
```

**New paragraph before `:112`.** Step 37: C-SUB goes in its own paragraph immediately before
`:112`, and `:112` stays verbatim (pr-relay-graph:9).
- `v:47`, `v:48`: KEEP. "exactly one same-session PR-35 re-entry handoff" stays correct, because
  PR-35 re-enters its own session.
```
old: 
Use `REMOTE_EVIDENCE_PENDING` only in PR-35 when
new: 
{C-SUB}

Use `REMOTE_EVIDENCE_PENDING` only in PR-35 when
```

**`:121` — polling.** Step 37 names `:121` (sweep:19). The only edit text on record is sweep:19's.
The finding's alternative, "kept deliberately", would drop a line the original step targets. No
literal sits on this line.
```
old: - poll only when a pending remote result can change the next action;
new: - where no subscription delivers it, poll only when a pending remote result can change the next action;
```

**`:133` — the RS-20 package.** Step 14 (pr-relay-graph:6): O8. Whichever option is taken,
`v:58` and `v:61` stay verbatim.

**`:141` — approved open-PR rescope.** Step 35 (sweep:4, coverage:17).
- `v:63`: REPLACE and FORBID.
- `v:62`, `v:64`, `v:71`, `v:76`: KEEP.
```
old: Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR,
new: Resume the recorded phase in the recorded phase's own dedicated session, workspace/worktree, branch, open PR,
```

**`:158` — one branch and one PR.** Step 35 ("ten-field", pr-relay-graph:1) and child C6 ("per
plan cycle"). `v:53` on `:157` (`` `docs/ephemeral` `` plus its two trailing spaces): KEEP.
```
old: The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires;
new: The work unit keeps exactly one branch and one pull request per plan cycle, which the nine-field continuity list requires;
```

**C-ART — new paragraph.** Step 10. Its position (after `:158` or after `:160`) is O1. Option (a),
after `:158`, is simulated.
- **NEW** `never carries the only copy` (pr-relay-graph:11; the same string as registry step 11).
```
old: for artifacts. The Product Owner merges.

new: for artifacts. The Product Owner merges.

{C-ART}

```

**`:162` — the handoff rule.** Steps 14 and 19 (pr-relay-graph:6, fv-rest:25).
- The first sentence stays verbatim: `v:54` KEEP, and the `flowmaster-validate` marker at `:2595`
  KEEP.
- The second sentence, the field list, is replaced by C-HANDOFF (O23). "Populate only the actual
  branch.", the not-runnable sentence and the terminal-return sentence stay.
- C-PLACE is appended at the end of the line.
```
old: It must instruct the receiver to run the exact selected Notion prompt by full name, version, and direct Notion URL; identify the receiving role and exact continuing/dedicated session; identify the change/Epic and work unit; supply every required repository path and repository/PR reference; state current status, completed work, decisions, constraints, unresolved items, and preserved authority; and state the next required action and expected output.
new: {C-HANDOFF}
```
```
old: or unrecoverable work.
new: or unrecoverable work. {C-PLACE}
```

**`:164` — returns by result.** Step 35 (the first sentence) and step 40, applied partially
(coverage:16, pr-relay-graph:8, coverage:3).
- The fallback clause is rewritten to the single predicate, not deleted.
- "Nathan's later merge assertion" stays: it is the fact on the fallback path.
- `v:83` "PR-40's duty to independently verify actual merged state and landed lineage": KEEP.
- `v:59` (the rescope sentence): KEEP.
- The interruption sentence ("exact same-session same-phase continuation") stays: it names the
  phase's own session.
- Whether a `MERGE_OBSERVED` return sentence is added here is O17.
```
old: At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact same-session PR-35 continuation.
new: At PR-30 `PR_CANDIDATE_PUBLISHED`, return the exact PR-35 continuation.
```
```
old: to use it only after Nathan has manually merged the identified PR;
new: to use it only after Nathan has manually merged the identified PR and {FALLBACK};
```

**Lines that mention sessions and stay unchanged.** None states the shared session that D23-D
reverses.
- `:21` "the dedicated PR-session identity";
- `:112` "same-session PR-35 re-entry" and "same-session repository/artifact inconsistency";
- `:147` "that same native PR-30 session";
- `:151` "work for the same session".

**Not flagged by any finding:**
- `:173`, "Do not create hidden sessions", which is O14;
- cases `:57`, which is O15.

### 8a.2 `glow-hde-pr-development/references/behavior-cases.md`

Only the headings are validated, so each content edit is listed for completeness
(pr-relay-graph:15).

**`:7` — Fresh work unit.** Step 35. `v:35`: KEEP. The "creates no new … session" list is O7;
option (a) is shown.
```
old: with exactly one complete same-session PR-35 handoff.
new: with exactly one complete PR-35 handoff.
```
```
old: The phase split creates no new role, session, Proceed,
new: The phase split creates no new role, Proceed,
```

**`:11` — PR-30 phase boundary.** Steps 35 and 14, by the same rule as `:82`. `v:35`: KEEP.
```
old: invokes the exact selected PR-35 in the same dedicated PR-development session with complete lineage.
new: invokes the exact selected PR-35 in the dedicated PR-35 session.
```

**`:13` — the continuity list.** Step 35 (pr-relay-graph:1). `v:64`: KEEP.
```
old: The shared phase identity preserves the exact ordered ten-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; dedicated PR-development session; workspace/worktree;
new: The shared phase identity preserves the exact ordered nine-field GCF-17 continuity list: `WORK_UNIT_ID`; original Product Owner Proceed; workspace/worktree;
```

**`:17` — PR-35 review phase.** Step 35.
```
old: Given the complete same-session PR-35 handoff,
new: Given the complete PR-35 handoff,
```

**`:21` — exact phase results.** Step 38 (sweep:3). `v:35`: KEEP. Guarding this old form is O10.
```
old: PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`,
new: PR-35 returns only `MERGE_PENDING`, `MERGE_OBSERVED`, `RESCOPE_PENDING`,
```

**`:49` — Material rescope.** Step 24 (pr-relay-graph:12), using the D23-C term from C-LAT and
A1-7.
- The heading `## Material rescope`: KEEP.
- `v:57`, `v:74` on this line: KEEP.
```
old: Given evidence that implementation requires an approved-boundary change,
new: Given evidence that implementation requires a material change to the Epic-level commitment,
```

**`:87` — Merge readiness.** Step 40 (coverage:16: "the same wording"). `v:82`: KEEP.
```
old: The conditional prompt separately requires
new: The conditional prompt, usable {FALLBACK}, separately requires
```

**New case, appended at the end of the file.** Child C6. It is built from C-PR20-ENTRY,
C-PROCEED, C-PR30-ENTRY, `{LANDED}` and C-REPLAN's last sentence, plus the child's own words: "a
new branch and PR are created". It avoids both forbidden strings the child names. Glue: O22.
```
insert (after the file's last line, one blank line before the heading):
## PR-40 rejection re-plan

Given a PR-40 `REJECT` (`reject_replan`) for this `WORK_UNIT_ID`, whose pull request merged under the earlier plan cycle, PR-20 plans that work unit again in a new top-level session that Nathan creates, and the new plan receives its own Proceed. PR-30 starts only from the Proceed of its own plan. {LANDED} PR-30 creates a new branch and a new pull request for the new plan. The earlier Proceed is spent and is never reused.
```

### 8a.3 `glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py`

**`required` (`:25`–`:86`).** Labels are unchanged (O22).

- **KEEP**, verbatim: `v:27`–`v:31`, `v:33`–`v:36`, `v:39`–`v:43`, `v:45`–`v:54`, `v:56`–`v:62`,
  `v:64`–`v:85`. `v:48` and `v:83` are kept deliberately (pr-relay-graph:9 and :8).
- **REPLACE**, each new value in place of the old one:

```
v:26  "revision"
GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0

v:32  "single session"
run in two dedicated sessions

v:37  "PR-35 complete result vocabulary"
{V6}

v:38  "PR-30 to PR-35"
exactly one complete `PR-35` handoff to the dedicated PR-35 session

v:44  "merge-ready ownership"
Continue in this phase's own dedicated session until all applicable predicates are true

v:55  "exact GCF-17 continuity list"
{NINE}

v:63  "same PR continuation"
the recorded phase's own dedicated session, workspace/worktree, branch, open PR
```

Sources:
- `v:26`: *New revisions*.
- `v:32`: pr-relay-graph:2; the value is C-SESSION's words.
- `v:37`: sweep:3 and coverage:14.
- `v:38`: pr-relay-graph:0.
- `v:44` and `v:63`: sweep:4 and coverage:17.
- `v:55`: pr-relay-graph:1.

**NEW entries.** Five label/literal pairs, inserted between `v:84` and `v:85`. The C-PROCEED
literal is O9.

```
"artifact holds results": "never carries the only copy"
"in-flight decisions": "An *In-flight decisions* section"
"material latitude": "Decide it during work"
"one Proceed per plan": "One Proceed per approved per-PR plan"
"top-level PR-35 session": "never as a subagent, forked agent or workflow agent of PR-30"
```

Sources:
- "artifact holds results": step 10, pr-relay-graph:11.
- "in-flight decisions": step 20, pr-relay-graph:10, adversary:5.
- "material latitude": step 24, pr-relay-graph:12.
- "one Proceed per plan": child C6.
- "top-level PR-35 session": A1-8 and the D23 clarification's *Guard* ("the skills"). Its value is
  the plain-substring form of the pattern that A1-8 and §7 give the C-SESSION clause
  (`never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30`;
  coverage:5, adversary:5). It matches the C-SESSION clause and not C-TOP.

**`forbidden` (`:91`–`:103`).** All 11 existing entries stay; none is narrowed (child C6,
pr-relay-graph:14). Seven entries are appended after `"[TODO"`, in this order:

```
one dedicated PR-development session
same-session `PR-35` handoff
{V5}
Continue in the same dedicated PR session until all applicable predicates are true
{TEN}
same dedicated PR session, workspace/worktree, branch, open PR
followed in the same session by PR-35
```

- Each of the first six is the old value of a REPLACE literal above. It is forbidden so that
  reinjecting it fails (pr-relay-graph:0 and :2, sweep:3 and :4, coverage:17).
- The seventh is from child C6.
- Measured on the edited copy: none of the seven occurs, case-insensitively, anywhere in the new
  text. Among the text that must stay, "exactly one same-session PR-35 re-entry handoff" does not
  contain "same-session `PR-35` handoff".
- The C-REPLAN, C-PROCEED and re-plan case texts contain neither "receives its own PO Proceed" nor
  "normal Plan/instruction path".

**`case_headings` (`:108`–`:130`).** Append after `"## Not ready"`:
```
## PR-40 rejection re-plan
```

**Guards no source requests.** No finding asks for a required literal for C-SUB, C-DISPATCH, C-HANDOFF
or C-PLACE in this validator, nor for C-TOP in this skill (O12, O13). Case headings for C-DEC,
C-LAT, C-SUB and `MERGE_OBSERVED` are also unrequested: pr-relay-graph:15 only says to "consider"
them (O16).

### 8a.4 Must-fail regressions for `glow-hde-pr-development`

Each regression is run on a scratch copy of the edited package, with `PYTHONDONTWRITEBYTECODE=1`.
**Pass** means exit 1 and stdout equal to the expected line. A second, non-fail-fast evaluation
(`allfail.py`) must also find exactly one failure. All 14 were measured and met both conditions.

| id | serves | mutation |
|---|---|---|
| R-rev | revision | at `:8`, 1.3.0 → 1.2.5 |
| R-32 | `v:32` | inject the old `:53` first sentence |
| R-37 | `v:37` | inject `{V5}.` |
| R-38 | `v:38` | inject "followed by exactly one complete same-session `PR-35` handoff." |
| R-44 | `v:44` | inject the old `:100` line |
| R-55 | `v:55` | inject `{TEN}.` |
| R-63 | `v:63` | inject the old `:141` sentence |
| R-C6-27 | child C6 | inject the whole old `:27` line |
| R-CART | step 10 | delete `{C-ART}` |
| R-CDEC | step 20 | delete `{C-DEC}` |
| R-CLAT | step 24 | delete `**Decide it during work:**` |
| R-CPROC | child C6 | delete `{C-PROCEED}` at `:27` |
| R-TOP | A1-8 | delete C-SESSION's A1-8 sentence |
| R-heading | child C6 | rename the new heading |

Expected stdout, in table order:
```
FAIL: missing revision contract
FAIL: forbidden or unfinished content present: one dedicated PR-development session
FAIL: forbidden or unfinished content present: {V5}
FAIL: forbidden or unfinished content present: same-session `PR-35` handoff
FAIL: forbidden or unfinished content present: Continue in the same dedicated PR session until all applicable predicates are true
FAIL: forbidden or unfinished content present: {TEN}
FAIL: forbidden or unfinished content present: same dedicated PR session, workspace/worktree, branch, open PR
FAIL: forbidden or unfinished content present: followed in the same session by PR-35
FAIL: missing artifact holds results contract
FAIL: missing in-flight decisions contract
FAIL: missing material latitude contract
FAIL: missing one Proceed per plan contract
FAIL: missing top-level PR-35 session contract
FAIL: missing behavior case: ## PR-40 rejection re-plan
```

**A limit, measured.** Reverting a line in place, instead of injecting, fires two checks: the new
literal goes missing, and the old one is forbidden. For example, `{V6}` → `{V5}` at `:57` prints
`FAIL: missing PR-35 complete result vocabulary contract`, and `allfail.py` counts 2. So only the
injection form meets E4 item 9's "exactly its own finding".

### 8a.5 The 1.3.0 revision and every pin of it

`1.2.5` → `1.3.0` (amendment, *New revisions*: "every revision pin moves in the same set";
pr-relay-graph:16, fv-main:25, fv-rest:26). This measured list is complete for the synced tree:

```
glow-hde-pr-development/SKILL.md:8                                         this section
glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py:26     this section
flowmaster-validate/scripts/validate_gcfpe_20260914.py:1722                contract subset primary_skill_revision
flowmaster-validate/scripts/validate_gcfpe_20260914.py:2592                SKILL_CONTRACT marker
flowmaster-validate/scripts/validate_gcfpe_current.py:651                  PR_SKILL_CONTRACT marker
flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:28      installed_skill_revisions
flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:3003   pr_development_contract.primary_skill_revision
change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json:3003           pr_development_contract.primary_skill_revision
```

- **Ownership.** The four `flowmaster-validate` sites belong to that package's section. The two
  contract sites are set by the regenerator's value table (§6).
- **Not pins of the installed revision, and kept.** `validate_gcfpe_current.py:302` (`1.2.0`)
  checks the historical 091326.2 contract. Today it passes while the skill is at 1.2.5, which
  proves it pins the contract, not the skill. The historical contracts (`1.2.0`, `1.1.0`) keep their
  bytes (A1-1). O25 covers `:302` if the current-overlay alias is re-pointed.

### 8a.6 Other packages' literals that read these bytes

Owned by the `flowmaster-validate` and `change-flow` sections. They are listed so that those
sections use byte-identical values.

- **`validate_gcfpe_20260914.py:2592`–`:2595`** (case-insensitive):
  - revision → 1.3.0;
  - `:2594` → `{NINE}` (fv-main:24, fv-rest:18);
  - `REMOTE_EVIDENCE_PENDING`, `PR_REMOTE_ACTION_LEDGER`, the no-merge marker (`:110`) and the
    handoff-shape marker (`:162`) all KEEP.
- **`validate_gcfpe_current.py:651`–`:652`:** revision → 1.3.0. "one dedicated PR-development
  session" must become a substring of the new `SKILL.md` (pr-relay-graph:2). This section's text
  supplies `run in two dedicated sessions` at `:3` and `:53`, but the choice belongs to that
  section.
- **Measured on the edited copy.**
  - `validate_gcfpe_current.py` returns exactly two errors:
    `PR_SKILL_CONTRACT_MISSING:GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.2.5` and
    `PR_SKILL_CONTRACT_MISSING:one dedicated PR-development session`.
  - `validate_gcfpe_20260914.py` returns exactly two `SKILL_CONTRACT:glow-hde-pr-development:`
    errors, for the revision and `{TEN}`.
  - With those four markers changed as above, both return only
    `SKILL_SELF_IDENTITY:DECLARED_eb9634d60a65_MEASURED_9ff9168fdbf3`. That is
    `flowmaster-validate`'s own tree digest, which moves last (§5).
- **`{NINE}` must match, byte for byte,** at:
  - `change-flow/SKILL.md:303`;
  - `change-flow/scripts/validate_gcfpe_20260914.py:1022`;
  - `flowmaster-validate/SKILL.md:164`;
  - `flowmaster-validate/scripts/validate_gcfpe_20260914.py:2594`;
  - the amthor sites in 8a.7 to 8a.9.

### 8a.7 `amthor-workspace-governance-audit/SKILL.md`

**`:10` — revision.** The amendment says "bumped one minor", which is 1.12.0 under the patch reset
that every other bump in the amendment uses. Pinned also at `run_fixture_suite.py:307` (8a.9).
```
old: **WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3
new: **WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0
```

**`:32` — predecessor archive.** registry-audit:16, which narrows the check to members that
received a successor page. C-VERSION applies from the next release (A1-3).
```
old: After authorized selection, verify each predecessor prompt moved intact
new: After authorized selection, verify each predecessor prompt of a member that received a successor page moved intact
```

**`:38` — handoff invariant.** C-HANDOFF (registry-audit:13).
- The first sentence stays: `run_fixture_suite.py:315` requires "exactly one fenced `text`
  `NEXT_PROMPT_HANDOFF` block" in this file. KEEP.
- The second sentence, including the Notion-resident clause, becomes C-HANDOFF, as at `:162`.
- The terminal sentence stays.
- The kept invariants (destination by name, version and URL; no blanks, menus or alternates) are
  all carried by C-HANDOFF.
```
old: It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the receiving role/session and work identifiers; carries every already-existing required artifact by exact identity/version and its repository path, or its direct Notion URL for a Notion-resident artifact; carries status, decisions, constraints, unresolved items, next action, and expected output; and contains no blanks, menus, or alternative destinations.
new: {C-HANDOFF}
```

**`:40` — primary-skill invariant.** C-SESSION (registry-audit:13), in step 36's wording. The
"adds no … session … cross-session route" list is O7. Option (a) is shown.
```
old: - GCFPE PR-30, same-session PR-35, interrupted PR recovery,
new: - GCFPE PR-30, PR-35 in its own dedicated session, interrupted PR recovery,
```
```
old: Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row.
```

**`:41` — continuity list.** registry-audit:13 and :15. Whether C-SESSION is prefixed here is O19.
The fixture-suite constant must equal this text (8a.9).
```
old: - {TEN}. Require PR-30
new: - {NINE}. Require PR-30
```

**`:43` — PR-30 recovery.** Child C10 ("gains the plan-cycle recovery rule"), sweep:16 (mirror)
and registry-audit:13.
```
old: or unsupported platform limitation. PR-30 owns
new: or unsupported platform limitation. {LANDED} PR-30 owns
```
```
old: ends with `PR_CANDIDATE_PUBLISHED` plus one complete same-session PR-35 handoff.
new: ends with `PR_CANDIDATE_PUBLISHED` plus one complete PR-35 handoff.
```

**`:44` — single Proceed.** Child C10 ("becomes 'one Proceed per plan cycle' under C-PROCEED").
The wording is O18. Option (a), simulated, keeps the child's quoted words and adds C-PROCEED's
second and third sentences verbatim. The rest of `:44` (CI economy, `MERGE_PENDING` predicates,
manual merge) is kept.
```
old: - One Product Owner `Proceed` authorizes the single PR-30/PR-35 work unit through genuine merge readiness, not merge.
new: - One Product Owner `Proceed` per plan cycle authorizes the PR-30/PR-35 work unit through genuine merge readiness, not merge. A continuation — PR-30 to PR-35, a rescope return, a recovery — never requires or creates a second Proceed. Only a PR-40 `REJECT` re-plan creates a new plan, and that plan receives its own Proceed.
```

**`:47` — rescope resume.** registry-audit:13, in its exact words, "the recorded phase's own
session".
```
old: phase in the same session/workspace/worktree/branch/open PR/original Proceed.
new: phase in the recorded phase's own session/workspace/worktree/branch/open PR/original Proceed.
```

**`:49` — merge chain.** registry-audit:13 and adversary:9 converge it on C-DISPATCH, keeping
three things: "MERGE_PENDING is historical", "PR-40 independently verifies" and no-merge.
- C-DISPATCH goes in verbatim after the first sentence.
- The assertion sentence takes `{FALLBACK}`. Glue: O22.
```
old: - PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only that Nathan manually merged the identified PR;
new: - PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only that Nathan manually merged the identified PR;
```

**New invariant bullet after `:49`.** A1-8 ("the governance audit's semantic invariant … is
added to the fifth package"). The text is sweep:25's, verbatim. It says "launches"; see O24.
```
insert (as the line after :49):
- Every main-ecosystem prompt (all but GCFPE-MGMT-10) runs as its own top-level session Nathan creates; none runs as a subagent, forked or workflow agent; none creates, launches or schedules a session; workers within a task are allowed.
```

### 8a.8 `amthor-workspace-governance-audit/references/`

**`interoperability-contracts.md`** (registry-audit:14)

- **`:13`**, step 35, deletion only:
```
old: implementation/publication, same-session PR-35 review/readiness,
new: implementation/publication, PR-35 review/readiness,
```
- **`:18`**, step 35. The "adds no" list is O7; option (a) is shown.
```
old: one selected PR-30 → PR-35 same-session phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: one selected PR-30 → PR-35 phase continuation inside existing R1 row GCF-17; it adds no role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row.
```
- **`:53`**: KEEP verbatim. `run_fixture_suite.py:316` requires "exactly one fenced `text`
  `NEXT_PROMPT_HANDOFF`" here, and the line states only the block's shape.
- **`:54`**, step 14 (C-HANDOFF):
```
old: - The handoff begins with the exact selected destination prompt name, version, and direct Notion URL and carries the actual receiving role/session, work identifiers, every already-existing required artifact by exact identity/version and its repository path or its direct Notion URL for a Notion-resident artifact, state, decisions, constraints, unresolved items, next action, and expected output.
new: - {C-HANDOFF}
```
- **`:68`**, step 35: the handoff and the continuity list.
```
old: plus exactly one complete same-session PR-35 handoff.
new: plus exactly one complete PR-35 handoff.
```
```
old: {TEN}.
new: {NINE}.
```
- **`:74`**, step 40, handled as at SKILL.md `:49`:
```
old: PR-35's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later invocation asserts only a manual merge;
new: PR-35's `MERGE_PENDING` is historical pre-merge evidence. {C-DISPATCH} Nathan's later invocation, usable {FALLBACK}, asserts only a manual merge;
```
- **`:96`**, step 35, deletion only:
```
old: PR-30/PR-35 same-session skill/recovery
new: PR-30/PR-35 skill/recovery
```

**`behavioral-fixtures.md`** (registry-audit:14)

- **`:48`**:
```
old: {TEN}.
new: {NINE}.
```
- **`:49`**: O7(b). Option (a), keep verbatim, is simulated. PR-35 still creates no session under
  the D23 clarification.
- **`:50`**:
```
old: with one complete same-session PR-35 handoff.
new: with one complete PR-35 handoff.
```
- **`:52`**, step 40 with `{FALLBACK}`:
```
old: separately require Nathan's later manual-merge assertion and PR-40's
new: separately require Nathan's later manual-merge assertion, usable {FALLBACK}, and PR-40's
```

**`project-prompt-registry-schema.md:42`** — the `session_class` enum (registry-audit:20). The
finding calls this edit "optional", so it is O20. Measured: `SAME_SESSION_CONTINUATION` is used by
one registry row today (PR-35), and step 33 moves that row to `DEDICATED_PR_REVIEW_SESSION`.

**Unchanged files:**
- `rule-catalog.md`, `report-contracts.md`, `workspace-skill-registry-schema.md`;
- `epic-reengineering-interoperability.md`, which is historical provenance (registry-audit notes);
- every script except `run_fixture_suite.py`;
- `assets/icon.svg`.

A scan found no other statement of the reversed rules in them. No source asks for amthor
invariants on C-ART or C-PLACE, or for `MERGE_OBSERVED` or re-plan fixture lines (O21).

### 8a.9 `amthor-workspace-governance-audit/scripts/run_fixture_suite.py`

registry-audit:15: the constant is updated, not deleted, so the parity guard stays.
```
old: EXACT_GCF17_CONTINUITY = "{TEN}"
new: EXACT_GCF17_CONTINUITY = "{NINE}"
```
```
old: self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.11.3", skill)
new: self.assertIn("WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** 1.12.0", skill)
```

**Must-fail regressions, measured** on the edited copy with `TMPDIR` inside the scratch copy.
**Pass** means `Ran 34 tests`, `FAILED (failures=1)`, and exactly the named test failing.

| mutation | failing test |
|---|---|
| `{NINE}` → `{TEN}` in `SKILL.md` | `test_exact_gcf17_continuity_parity` |
| `{NINE}` → `{TEN}` in `interoperability-contracts.md` | `test_exact_gcf17_continuity_parity` |
| `{NINE}` → `{TEN}` in `behavioral-fixtures.md` | `test_exact_gcf17_continuity_parity` |
| revision 1.12.0 → 1.11.3 in `SKILL.md` | `test_exact_gcf17_continuity_parity` |
| `:38`'s kept "exactly one fenced …" phrase damaged | `test_exact_fenced_text_handoff_parity` |

**A limit, measured:** adding `{TEN}` beside `{NINE}` passes all 34 tests, because the suite has no
forbidden check. See O11.

### 8a.10 What was measured

All runs used a copy of the synced tree under `/tmp/claude-0/spec/s8a/`, with
`PYTHONDONTWRITEBYTECODE=1`.

**Baseline:**
- the PR skill validator prints `PASS`;
- the amthor suite runs 34 tests, OK;
- `validate_project_prompt_registry.py` returns `{"valid": true, "problems": []}`.

**The edits, simulated** (`work/apply.py`, sha256 `2114f9ce…`, under both option sets A and B):
- the PR skill validator prints `PASS`, and the non-fail-fast evaluation finds 0 failures;
- the amthor suite runs 34 tests, OK;
- the registry check is unchanged.

**Regressions:**
- 14 of 14 PR-skill regressions are exact (`work/regress.py`, `6d64146c…`);
- the 5 amthor regressions fail as specified, and the injection-beside case passes, as
  8a.9 records (`work/regress_amthor.py`, `ea2c4f42…`).

**Default `validate_flowmaster.py` suite on the edited copy.** It fails only in
`gcfpe_current_direct_handoff`, with the two markers of 8a.6. The fixture cases that report errors
are the expected-negative cases, identical to the baseline's.

## §8b Skill edits: change-flow, session-relay-flowmaster, tw-flowmaster, flowmaster-validate

This section compiles every edit EXECUTE makes at E2 to four of the six packages (A1-6):
`change-flow`, `session-relay-flowmaster`, `tw-flowmaster` and `flowmaster-validate`. It decides
nothing. Where the amendment, the child plan and the findings leave more than one result, the item
carries an `O`-number. Its options are in 8b.14. The value marked *simulated* is the one the
measurements in 8b.12 used. It is not a ruling.

Values owned elsewhere are cited, not repeated:
- **§5** owns the R1 successor files, their digests and paths, and the pin order.
- **§6** owns every contract-only value: `transition_contract`, `receiver_compatibility`,
  `route_graph`, `graph_proofs` and `protected_identities`.
- **§4** owns the graph.
- **§8a** owns `glow-hde-pr-development` and the tokens `{NINE}`, `{TEN}`, `{V5}`, `{V6}` and
  `{FALLBACK}`.

### 8b.0 Conventions

- **Line numbers** are those of the installed files whose digests §2 records:
  - `change-flow` `80e877c2…`;
  - `session-relay-flowmaster` `4ef8daa3…`;
  - `tw-flowmaster` `fa3fac85…`;
  - `flowmaster-validate` `b9ca212a…`.

  E2 applies each edit by its `old:` span, on a scratch copy, as a scripted exact-substring
  replacement that asserts the span occurs exactly once. Line numbers identify a site; spans locate
  it. In `old:`/`new:` blocks, `\n` stands for a line break and a `{TOKEN}` for its text;
  everything else is literal.
- **The compile rule is §8a.0's.**
  - Canonical texts go in verbatim.
  - Words that state a reversed rule are deleted, and are replaced only by words from a canonical
    text, the A1-7 table or a finding.
  - Everything else on the line stays. No whole-line replacement is made where a kept literal sits
    (amendment defect 12).
- **Tokens.**
  - `{C-SESSION}`, `{C-DISPATCH}`, `{C-HANDOFF}`, `{C-PLACE}`, `{C-PROCEED}` and `{C-D22}` are §3's
    texts, byte-exact.
  - `{OVERRIDE}` is §3's *GCFPE override* (A1-6).
  - `{STEP2}` is §3.5's step-2 literal.
  - `{NINE}`, `{TEN}`, `{V5}`, `{V6}` and `{FALLBACK}` are §8a.0's.
- **How each check reads text** (read from the code):

  | check | where | what it tests |
  |---|---|---|
  | `change-flow` validator skill clauses | change-flow `scripts/validate_gcfpe_20260914.py:1020-1031` | case-sensitive substring over the whole `SKILL.md`; fail-fast |
  | `CONTRACT_REQUIRED` | `validate_flowmaster.py:113`, applied at `:1313-1318` | case-sensitive substring over the whole `SKILL.md` |
  | `CONTRACT_FORBIDDEN` | `validate_flowmaster.py:304`, applied at `:1338-1343` | case-insensitive substring over the whole `SKILL.md`, the embedded core included; **never applied to `change-flow`** (`:1340`, sweep:12) |
  | `CHANGE_FLOW_CONTRACT` | flowmaster-validate `validate_gcfpe_20260914.py:2580-2586` | case-sensitive substring over change-flow `SKILL.md` |
  | `SKILL_CONTRACT` | same file `:2590-2606` | case-insensitive substring over the named skill's `SKILL.md` |
  | reference allowlist | `validate_flowmaster.py:1115-1126` | every linked `references/…` path must be in `OPTIONAL_REFERENCES`, and every listed path must be linked |
- **Literal dispositions.** **KEEP** means verbatim and still present. **REPLACE** gives a new
  value. **FORBID** puts the old text where a revert fails. **NEW** adds a check.
- **A regression passes** only when the findings on the mutated input, minus those on the clean
  input, are exactly the expected set (§9 item 9). For the fail-fast `change-flow` validator this
  means exit 1 with exactly the expected line. A second, non-fail-fast count must also find exactly
  one failure.

### 8b.1 The Flowmaster core and the GCFPE override (A1-6)

**Core boundaries.** The core is byte-identical in all five skills that embed it. The marker block,
read as lines `BEGIN` through `END` with their newlines, measures sha256 `4e565e40…` in each
(sweep:6 cites the same prefix), and the `change-flow` validator's
`EXPECTED_CORE_SHA` `4d8bb9bf…` pins it (`:26`, `:749`). **No byte inside these markers changes**
(A1-6):

```
change-flow/SKILL.md               :33 <!-- FLOWMASTER_CORE_BEGIN -->   :249 <!-- FLOWMASTER_CORE_END -->   specialization :250-:583
session-relay-flowmaster/SKILL.md  :23 <!-- FLOWMASTER_CORE_BEGIN -->   :239 <!-- FLOWMASTER_CORE_END -->   specialization :241-:724
tw-flowmaster/SKILL.md             :12 <!-- FLOWMASTER_CORE_BEGIN -->   :228 <!-- FLOWMASTER_CORE_END -->   specialization :230-:497
```

The core option that the override disables is `change-flow:158`, `session-relay-flowmaster:148` and
`tw-flowmaster:137`:

```
3. a fresh spawned session in its own worktree only when no existing authoritative session can do the work.
```

**The override.** `{OVERRIDE}` goes in verbatim, once per skill, as its own paragraph inside the
specialization markers (A1-6; sweep:6). Its position is **O1**. The simulated positions:
- `change-flow`: a new paragraph after `:263`, in *Scope and endpoint*;
- `session-relay-flowmaster`: after `:255`, in *Endpoint and boundaries*;
- `tw-flowmaster`: the first paragraph under `### GCFPE binding` (`:300`).

```
old: or manual PF controls.\n\n### Runtime entry gate
new: or manual PF controls.\n\n{OVERRIDE}\n\n### Runtime entry gate
```
```
old: Do not silently create a replacement.\n\n### Cross-skill contracts and shared state
new: Do not silently create a replacement.\n\n{OVERRIDE}\n\n### Cross-skill contracts and shared state
```
```
old: ### GCFPE binding\n\n
new: ### GCFPE binding\n\n{OVERRIDE}\n\n
```

**Held in place** by one `CONTRACT_REQUIRED` entry per skill: `{OVERRIDE}` as a whole string (A1-6;
granularity **O3**; see 8b.8). Deleting it in any one skill must produce exactly that skill's
`missing specialization contract: {OVERRIDE}` (measured, 8b.12).

### 8b.2 `change-flow/SKILL.md`

**`:8` — revision.** 3.2.9 → 3.3.0 (amendment, *New revisions*). Pin sites are in 8b.11.
```
old: CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9
new: CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0
```

**`:17`, `:19`, `:21` — R1 declarations.** `:17` (the profile id) and `:19` (the matrix digest) are
§5's (A1-1; adversary:7). `:21` `R1_ROW_COVERAGE: 46/46` is KEEP (A1-1: 46 rows).

**Override** after `:263`: 8b.1.

**`:275` — the entry-gate PR policy.** Step 35 (C-SESSION; fv-rest:19, coverage:15). The phrases
"one dedicated PR-development session" and "same-session" go, and C-SESSION's words take their
place. Glue: **O5**. Simulated:
```
old: - The policy for one dedicated PR-development session per planned PR work unit, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, same-session PR-35 review/readiness,
new: - The policy for each planned PR work unit, run in two dedicated sessions, using `glow-hde-pr-development` as the sole primary skill across PR-30 implementation/publication, PR-35 review/readiness,
```

**`:278` — manifest item.** fv-rest:19. Deletion only.
```
old: a selected PR-35 is lawful only as the same-session second phase of the existing GCF-17 PR work unit.
new: a selected PR-35 is lawful only as the second phase of the existing GCF-17 PR work unit.
```
The staging-boundary sentence on the same line is stale, but no source touches it, so it stays.

**`:295` — the handoff rule.** Steps 14 and 19 (fv-rest:25).
- The first sentence stays verbatim. Validator literal `:1024`, "exactly one fenced `text`
  `NEXT_PROMPT_HANDOFF` block", is KEEP.
- The field-list sentence becomes `{C-HANDOFF}`.
- `{C-PLACE}` is appended at the end of the line, following §8a's placement at PR skill `:162`.
```
old: It begins by directing the receiver to the exact selected destination prompt by name, version, and direct Notion URL; names the actual receiving role/session and change/work identifiers; provides every required artifact repository path; and carries current status, decisions, constraints, unresolved items, next action, and expected output.
new: {C-HANDOFF}
```
```
old: Terminal results state completion and the native Product Owner return.
new: Terminal results state completion and the native Product Owner return. {C-PLACE}
```

**`:301` — the two-phase paragraph.** Step 35 (C-SESSION) and child C7 (C-PROCEED).
- KEEP: "PR-30 and PR-35 are two phases", which lies inside `{C-SESSION}` because §3 drops C-SESSION's
  backticks. It is change-flow validator `:1021` and flowmaster-validate `CHANGE_FLOW_CONTRACT`
  `:2581` (fv-main:26, fv-rest:17).
- REPLACE and FORBID: "one dedicated PR-development session" (`:1023`; 8b.3).
- NEW: "never as a subagent, forked agent or workflow agent of PR-30", from A1-8's clause inside
  `{C-SESSION}`.
- The first sentence ("Product Owner `Proceed` authorizes …") stays.
```
old: PR-30 and PR-35 are two phases of that one work unit and retain one original Proceed, one dedicated PR-development session, one workspace/worktree, one branch, one pull request, one PR instruction and detailed Plan, one primary skill, and continuous recovery/artifact lineage.
new: {C-SESSION}
```
```
old: exactly one complete same-session PR-35 handoff;
new: exactly one complete PR-35 handoff to the dedicated PR-35 session;
```
C-PROCEED "is appended as its own sentence after `:301`" (child C7; sweep:22):
```
old: coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness.\n
new: coherent corrective commits and pushes, CI economy, remote-head proof, and genuine merge readiness. {C-PROCEED}\n
```

**`:303` — the continuity list.** Step 29 and fv-rest:18. The list becomes `{NINE}`, and
"same-session " is deleted from the second sentence.
- `:1022`: REPLACE with `{NINE}` and FORBID `{TEN}`.
- The same `{NINE}` bytes must match `change-flow` validator `:1022`, flowmaster-validate `SKILL.md:164`,
  `validate_gcfpe_20260914.py:2594` and the §8a sites (§8a.6).
```
old: {TEN}
new: {NINE}
```
```
old: same-session continuation cannot add, omit,
new: continuation cannot add, omit,
```

**`:305` — result vocabularies.** Step 38 and A1-5 (sweep:3, coverage:14). Only the PR-35 list
changes. "exactly one same-session PR-35 re-entry handoff" stays: PR-35 re-enters its own session,
and §8a keeps the same phrase at PR skill `:112`.
```
old: {V5}
new: {V6}
```

**`:307` — the interoperability rule.** Steps 29–30 set `adds.session` and
`adds.cross_session_route` to 1 (§4 G9–G10; fv-rest:15). So "same-session", "session" and
"cross-session route" leave the "permits no extra …" list. This is deletion only, with the list's
"or" moved to its new last item.
```
old: permits this one selected same-session PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, session, work unit, duplicate branch/PR/work vehicle, merge authority, R1 row, or cross-session route.
new: permits this one selected PR-30 → PR-35 phase continuation inside GCF-17. It permits no extra role, approval, authority transfer, Product Owner gate, Proceed, work unit, duplicate branch/PR/work vehicle, merge authority, or R1 row.
```

**`:313`, `:323` — rescope sentences.** KEEP verbatim (child C7; sweep:22). Where C-LAT and the
step-14 field-list clause are placed beside them is §3 open question 12. It is **O10** here only by
reference.

**`:331` — the merge boundary.** Step 40 (sweep:12, coverage:3).
- The three no-merge sentences are KEEP (step 40: "keep every no-merge … sentence").
- The assertion clause takes `{FALLBACK}` (A1-5: "worded one way everywhere").
- `{C-DISPATCH}` is appended after the clause.
- "Never present `MERGE_PENDING` as a current post-merge fact." stays.
```
old: PR-35's `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only.
new: PR-35's `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts that Nathan manually merged; PR-40 then independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}
```

**`:353` — runtime approval.** sweep:13's replacement sentence, with its predicate "where no
subscription existed" replaced by `{FALLBACK}`, as A1-5 requires (coverage:3).
- The `PRODUCT_OWNER_RUNTIME_APPROVAL = PR Implementation Proceed invocation` literal on this line
  is KEEP. It is `CONTRACT_REQUIRED['change-flow']`.
- "PR-40 must independently verify …" stays.
```
old: A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred; it is not a merge approval or merge instruction.
new: Where the subscribed PR-35 session observed the merge, that event is the fact PR-40 is entered on; {FALLBACK}, Nathan's later PR-40 invocation asserts the manual merge; neither is a merge approval or instruction.
```

**`:365` — actors table.** Step 35. The cell states one session for the work unit. **O6**.
Simulated option (a), C-SESSION's second and third sentences:
```
old: | Per-PR planning and implementation | One dedicated session per planned PR work unit; the same session performs both |
new: | Per-PR planning and implementation | PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request. |
```

**`:366` — PR merge row.** Step 40 names it. KEEP verbatim: "no automatic dispatch or agent merge
from Proceed or PR-40" restates A1-5's C-DISPATCH, under which dispatch is a paste and no agent
creates a session. §P's launch option, which the row once contradicted, is withdrawn (coverage:4;
the `D23` clarification).

**`:411` — manual-control meaning.** fv-rest:19. "manual-merge-assertion " is deleted. **O7**.
```
old: has only the manual-merge-assertion meaning defined above;
new: has only the meaning defined above;
```

**`:450`–`:452` — GCF-14, GCF-15, GCF-16.** KEEP. A1-1: "GCF-14 and GCF-15's session wording
stays", read per plan cycle. GCF-16 does not change (the `D23` correction).

**`:453` — GCF-17.** sweep:13 and coverage:15, mirroring the successor row. The subject takes
A1-1's actor cell. Whether the session cell is also placed is **O8**. Simulated:
```
old: GCF-17 — The same dedicated PR session implements only that work unit across selected PR-30 and PR-35, validates it, and creates exactly one active branch and pull request.
new: GCF-17 — The dedicated PR session (PR-30 phase) and the dedicated PR-35 session (PR-35 phase) implement only that work unit across selected PR-30 and PR-35, validate it, and create exactly one active branch and pull request.
```
C-LAT at `:453`–`:454` (step 24) falls under O10.

**`:455` — GCF-17.LINEAGE.** Child C7 ("follows the successor row") and C-DISPATCH (§3).
- Its merge-entry sentence takes the fallback predicate.
- The successor row's new `next` (GCF-14) needs a re-plan statement.

No source gives the words: **O9**. The simulated option takes its words from `{FALLBACK}`,
C-DISPATCH and the A1-7 `reject_replan` condition:
```
old: Only after Nathan later asserts that the identified PR was manually merged may that invocation run.
new: Only after Nathan has manually merged the identified PR, and {FALLBACK}, may that invocation run; where the subscribed PR-35 session observed the merge, PR-35 returns `MERGE_OBSERVED` with the paste-ready PR-40 handoff.
```
```
old: This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only.
new: This is the single authoritative work-unit acceptance route; an attribution bundle is evidence only. A precise in-scope implementation/review/corrected-code/PR-lineage defect in landed work requires a new per-PR plan for the same work unit, in a new top-level session Nathan creates, with a new Proceed (GCF-14).
```

**`:557` — the runtime map.**
- The link target and SHA-256 become the successor runtime map,
  `references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json`, with its digest. That is
  A1-1; the value and the order are §5's (fv-rest:1, sweep:7).
- The sentence calls the map "immutable historical baseline evidence". Whether the historical map
  is still named here is **O11**.

**`:559` — the current overlay.** A1-6 re-points it from 091326.2 to the 091426.1 contract. The
`validate_flowmaster.py` `OPTIONAL_REFERENCES` change is in 8b.8.
```
old: Load [GCFPE current direct-handoff contract](references/gcfpe-current-direct-handoff-contract.json) as the current specialization overlay.
new: Load [GCFPE current direct-handoff contract](references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json) as the current specialization overlay.
```

**`:561`** is KEEP.

**`:563`** says the shared `contract_id` "resolves for current execution to
`gcfpe-current-direct-handoff-contract.json` alone". That stops being true once `:559` is
re-pointed. The 091426.1 contract's id is `GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED`. No
source words the change: **O13**, tied to **O12**. No validator reads `:563`.

**`:565`** is KEEP. No source requires a narrative note for 3.3.0.

**Lines that mention a session and stay unchanged.** None states the reversed shared-session rule:
- `:197` (core);
- `:263`;
- `:305`, "same-session PR-35 re-entry";
- `:327`, `:383` and `:406`.

`:277` and `:321` repeat rules that findings converge elsewhere. No finding names them here: **O18**
and **O34**.

### 8b.3 `change-flow/scripts/validate_gcfpe_20260914.py`

**Skill-clause literals, `:1020`–`:1031`.**
- KEEP: `:1021`, "PR-30 and PR-35 are two phases" (fv-main:26, fv-rest:17).
- REPLACE `:1022`: `{TEN}` → `{NINE}` (fv-rest:18).
- REPLACE `:1023`: "one dedicated PR-development session" → "run in two dedicated sessions". These are
  C-SESSION's words, the same value §8a gives PR validator `v:32` (pr-relay-graph:2, sweep:12).
- KEEP: `:1024`, "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block" (fv-rest:25).
- KEEP: `:1025`–`:1029`.
- NEW, after `:1023`: "never as a subagent, forked agent or workflow agent of PR-30". Sources: A1-8,
  the `D23` clarification's *Guard* ("the skills"), and §8a's identical literal.

Further required literals, for C-DISPATCH, C-PROCEED or C-HANDOFF, are unrequested: **O16**.

The new block, in place of `:1020`–`:1031`:
```
    for text in (
        "PR-30 and PR-35 are two phases",
        "{NINE}",
        "run in two dedicated sessions",
        "never as a subagent, forked agent or workflow agent of PR-30",
        "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block",
        "PR_RETURN_PHASE",
        "PF10_BUILD_NOTES_ADDENDUM",
        "SOURCE_RESOLUTION_ERROR",
        "Only Nathan / Product Owner may manually invoke selected `PR-50",
        "ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR",
    ):
        require(text in skill, f"missing skill clause: {text}")
```

**The retired-phrase loop.** This is new, placed directly after the block above. A1-6: "a check that
fails if a retired phrase comes back"; `CONTRACT_FORBIDDEN` is never applied to `change-flow`
(sweep:12).
- Each entry is the old text of one 8b.2 edit that states a reversed rule. sweep:12 names the first
  four sites (`:301`, `:307`, `:331`, `:353`). The rest are the same class, from `:275`, `:278`,
  `:303`, `:305`, `:365`, `:411`, `:453` and `:455`.
- Matching mirrors the required loop: case-sensitive substring over the whole `SKILL.md`. **O15**.
- Measured: none of the 13 occurs in the edited file, case-sensitively or not.
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
    ):
        require(text not in skill, f"retired skill clause present: {text}")
```
If O6, O7, O8 or O9 takes another option, the entry for that line still holds: each entry is only
the old text.

**Contract-side literals.** These move together with the contract §6 regenerates.
- `:1007`–`:1010`, `pr35_result_vocabulary`: REPLACE with the `{V6}` list (sweep:3, adversary:9):
  ```
  ["MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING", "PRODUCT_OWNER_DECISION_REQUIRED"]
  ```
- `:746`: `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0`.
- `:751`: `contract_revision == "4.1.0"` (A1-2; fv-rest:11).
- `:806`: `len(graph["edges"]) == 229` (A1-7; fv-rest:10).
- `:76`–`:77`: `EXPECTED_ROUTING_SURFACE = "fecc319bdd4ce7ee6201cb77d7231861"`,
  `EXPECTED_ROUTING_SURFACE_ROWS = 284` (A1-7; fv-rest:14). The digest is final: it reads only edges
  and state routes (§2).
- `:21`: `EXPECTED_GRAPH_SHA` takes the final bundled-graph digest, in §5's pin order (fv-rest:10).
- **Unchanged:**
  - `:26` `EXPECTED_CORE_SHA` (A1-6);
  - `:208` `EXPECTED_CONTRACT_TOP_LEVEL_KEYS`, because A1-5 records the observed-merge edge inside
    `post_merge_three_event_contract`, not as a new top-level key (sweep:10);
  - `:944`, since `ordinary_pr_work_unit[2]` stays `NATHAN_PROCEED`;
  - `:993`–`:1000`;
  - `:1015`–`:1016`.

### 8b.4 `session-relay-flowmaster/SKILL.md`

**`:8` — revision.** 3.0.0 → 3.1.0 (amendment; pr-relay-graph:16). The pin is `validate_flowmaster.py:182`.
```
old: `SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.0.0`
new: `SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0`
```

**Override** after `:255`: 8b.1.
- `:255` and `:713` send a missing participant to Session Branch Flowmaster as
  `SESSION_PROVISIONING_REQUIRED`.
- That provisions sessions, which the override and the `D23` clarification rule out for GCFPE stages.

**O2**.

**`:259` — the prompt-locator rule.** Step 14's parenthetical: "runtime handoffs may name versioned
files; reusable prompt text stays versionless".
- The rest of the line forbids a direct URL in "temporary … handoff prompt" text.
- C-HANDOFF requires the destination's direct Notion URL (pr-relay-graph:18).

The carve-out's wording is **O17**. Simulated option (a) appends the parenthetical as a sentence and
changes nothing else:
```
old: This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text.\n
new: This prompt-locator rule does not ban API URLs, tool parameters or actual identity evidence outside prompt text. Runtime handoffs may name versioned files; reusable prompt text stays versionless.\n
```

**`:268` — control plane.** Step 2. The bullet marker and the final period stay.
- FORBID "preferred live control plane" (8b.8).
- **`:269` is out of scope** (§P step 2, *Explicitly not in scope*).
```
old: - Notion is the preferred live control plane for current task, assignment, dependency, decision, and handoff state.
new: - {STEP2}.
```

**`:273` — HDE handoff content.** First-draft step 14 and pr-relay-graph:18.
- The line puts "verified results and material gaps …" "in the existing handoff".
- C-HANDOFF forbids restated artifact content, and C-ART puts results in the artifact.
- No finding words the change: **O18**.

Simulated:
```
old: cleanup/recovery owner in the existing handoff.
new: cleanup/recovery owner in the output artifact that the handoff names.
```

**`:279` — handoff delivery.** Steps 14 and 19 (pr-relay-graph:18).
- The field list becomes `{C-PLACE} {C-HANDOFF}`.
- The sentence that makes Notion prompts versionless in the invocation contradicts C-HANDOFF and is
  deleted.
- "A block only in a referenced artifact is insufficient." stays.
- The order of the two texts is **O19**.
```
old: Deliver every concrete routed handoff in the final user-facing response itself: target actor and session continuity, exact task-bound advice or limitation, named file references the recipient can resolve itself, and a populated copyable invocation with the selected prompt's native inputs and actual prerequisites. For a Notion prompt use its versionless name and verified directory; approved runtime versions remain input lineage.
new: Deliver every concrete routed handoff in the final user-facing response itself. {C-PLACE} {C-HANDOFF}
```

**`:283` — the PR-lane paragraph.** Step 35 (C-SESSION), step 40 (C-DISPATCH; keep every no-merge
and no-polling sentence), N4 and sweep:5.
- **KEEP** these sentences:
  - "…returns MERGE_PENDING with readiness for the Product Owner's manual merge, and returns control
    without polling for that action.";
  - "Pending engineering remains with the same PR owner.";
  - "PR-40 stays read-only …";
  - "A prior MERGE_PENDING result …";
  - "Preserve this boundary … handoff."
- **`{C-SESSION}`** is placed at the start of the line (**O20**, simulated), and "same-session" goes
  from PR-30's handoff. The replacement words are A1-7's PR-30 → PR-35 condition, as §8a used at PR
  skill `:53`.
- **"PR-35 supplies the actual populated PR-40 handoff conditional on merge."** becomes
  `{C-DISPATCH}`.
- **"The Product Owner's PR-40 invocation supplies merge approval …"**: the approval clause is
  deleted. It contradicts `change-flow:353` ("not a merge approval") and sweep:5 forbids it. What
  remains keeps the no-agent-merge and PR-40-verifies clauses. Deletion rather than rewording is
  O20.
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
new: The Product Owner's PR-40 invocation never authorizes an agent merge,
```

**`:285` — ordered PR units.** KEEP verbatim (simulated, **O21**). Its "same-session resume of the
recorded PR phase" names the recorded phase's own session, which C-SESSION keeps. Its no-poll and
no-early-PR-40 rules are the ones step 40 keeps.

**`:353`, `:372` — `CONTROL_PLANE: NOTION | NONE`.** pr-relay-graph:17 offers two options, and the
amendment is silent: **O22**.
- Simulated: unchanged.
- The `CONTRACT_REQUIRED` literal "Bind `update_control_record` to `SHARED_STATE.CONTROL_PLANE:
  NOTION`" on `:372` is KEEP.

**`:624` — `NOTION_REFERENCE`.** §3 open question 13 (coverage:23): **O23**. Simulated: unchanged.
The `CONTRACT_REQUIRED` literal "REFERENCE_METHOD: REPOSITORY_PATH | WORKTREE_PATH | DRIVE_LINK |
NOTION_REFERENCE | INLINE_TEXT" is KEEP.

**`:713`.** KEEP (first-draft N6). The override states the explicit rule. See O2.

**`:723`.** KEEP. It is the rule that requires the revision bump.

**Scripts.** `scripts/validate_relay_manifest.py` never reads `SKILL.md` (pr-relay-graph:19). It
changes only under O22's option (b). The self-test stays 230 cases.

### 8b.5 `tw-flowmaster/SKILL.md`

A1-6: this skill "carries byte-identical copies of the relay's retired GCFPE lines". Measured today:
- `:304` = relay `:259`;
- `:319` = relay `:283`;
- `:321` = relay `:285`;
- `:317` = relay `:281`;
- `:306` = relay `:261`;
- `:323` = relay `:287`;
- `:315` ≠ relay `:279`. It differs in "named attachments" and "an attached artifact".

The edits:
- **`:8` — revision.** 1.1.6 → 1.2.0 (amendment; sweep:5, which cites `:9`; the line is `:8`).
  ```
  old: `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.1.6`
  new: `TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0`
  ```
- **Override**, under `### GCFPE binding` (`:300`): 8b.1.
- **`:304` := the relay's new `:259`,** byte for byte, under whichever O17 option is taken (sweep:5).
- **`:311`.** sweep:5: "Drop 'PR/commit references' from :311's handoff metadata and keep them in the
  usage record". No words are given: **O24**. Simulated:
  ```
  old: Add result artifact/PR/commit references when observed;
  new: Add result artifact/PR/commit references to the usage record when observed, never to the handoff;
  ```
- **`:315` takes the relay's step-14/19 text** (sweep:5). Whole line, or edited span only, is
  **O19**. Simulated: the whole line, equal to the relay's new `:279`.
- **`:319` := the relay's new `:283`,** byte for byte (sweep:5).
- **`:321` := the relay's `:285`,** today's bytes under O21 (a).
- **`CONTRACT_REQUIRED['tw-flowmaster']`:** all existing entries are KEEP. The revision entry
  (`validate_flowmaster.py:128`) and `{OVERRIDE}` move (8b.8).

### 8b.6 `flowmaster-validate/SKILL.md`

**`:8`, `:9` — identity.**
- `FLOWMASTER_VALIDATE_REVISION: 3.2.16` → `3.3.0` (amendment).
- `SKILL_TREE_SHA256` is recomputed with `skill_tree_digest` over the final tree and written **last**
  (fv-main:23, fv-rest:9, pr-relay-graph:32; §5 order).

**`:60` and `:231`–`:232` — C-D22** (step 45; fv-main:34). Step 45's old string is at `:231`–`:232`,
not at `:55`–`:60`; `:60` carries the shorter reason "because a file persists". Per-site wording is
§3 open question 8. Simulated option (a):
```
old: deliberately with no path option, because a file persists --
new: deliberately with no path option, because {C-D22} --
```
```
old: There is no path option and there will not be one: a file persists, and\na persisted corpus is what the policy forbids.
new: There is no path option and there will not be one: {C-D22}.
```

**`:145`, `:147`, `:149`, `:244`–`:249`** are §5's: the successor oracle's profile id, matrix,
digest and filename (A1-1; fv-rest:5, fv-main:18, adversary:7). `:255`–`:257` are KEEP, since the
successor is the "successor canonical source" route they already allow.

**`:155`** — the contract revision, from A1-2:
```
old: The 20260914 candidate contract revision 4.0.6 binds
new: The 20260914 candidate contract revision 4.1.0 binds
```

**`:164`–`:166` — the PR contract restatement.** fv-main:34, coverage:15, sweep:3 and fv-rest:15.
- In `:164`:
  - the first sentence becomes `{C-SESSION}`;
  - the list becomes `{NINE}`;
  - "sessions" and "cross-session routes" leave the "adds zero" list, matching `:307` above.
- In `:165`, "same-session " is deleted.
- In `:166`, `MERGE_OBSERVED` is inserted after `MERGE_PENDING`.
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

**`:173` — merge boundary.** fv-main:34, coverage:15; the same treatment as `change-flow:331`.
```
old: PR-35 `MERGE_PENDING` is historical pre-merge evidence; Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only.
new: PR-35 `MERGE_PENDING` is historical pre-merge evidence; {FALLBACK}, Nathan's later invocation asserts the manual merge; PR-40 independently verifies actual merged state and landed lineage read-only. {C-DISPATCH}
```

**`:176`, `:381`, `:383` — the fixture count.** "33" becomes the count O29 yields: 37 in the
simulated option (fv-rest:16).

**`:157`, `:381` — the selected-alias description.** It follows O12.

**`:178`** is KEEP. It is out of scope (amendment, *Noticed, not in scope*).

**`:184` — TW revision.** It follows 1.2.0; this is the only prose pin of that revision.
```
old: the TW specialization revision is 1.1.6 (including
new: the TW specialization revision is 1.2.0 (including
```

**`:294` — Change check 12.** coverage:15. **O25**. Simulated option (a), C-SESSION's second and
third sentences:
```
old: 12. One dedicated PR session plans and implements one work unit.
new: 12. PR-30's session plans with PR-20 and builds. PR-35 runs in its own dedicated session, entered from PR-30's handoff, and continues the same pull request.
```

**`:393` — rescope receiver compatibility.** sweep:20, verbatim:
```
old: resumes the recorded phase in the same session/worktree/branch/open PR under the original Proceed.
new: resumes the recorded phase in that phase's own session, worktree, branch and open PR under the original Proceed.
```

No literal reads these lines. Only `SKILL_TREE_SHA256` reads them, and it moves last.

### 8b.7 `flowmaster-validate/scripts/validate_gcfpe_20260914.py` — the reversals

Each reversal is listed with what it keeps and the regression ids of 8b.10. New error-code names are
**O30**. The simulated names are used below.

**1. Header check → `PROMPT_BODY_RELEASE_HEADER`.** Sources: D23-G, step 42, fv-main:0, fv-rest:22
and §7 G12–G14 (the header window).
- `prompt_identity_header_valid` (`:1046`–`:1078`) keeps:
  - the exact title;
  - the `Prompt ID:` line;
  - one neutral `Notion URL:` line in `nonblank[:12]`.

  It drops the `Prompt [Vv]ersion` and `Ecosystem release` requirements. The `len(nonblank) >= 7`
  floor becomes **O28**; the simulated value is 4.
- `:910` `PROMPT_VERSION_HEADER_RE` is REPLACED by the key tuple. Nothing else imports it (measured).
- A new function, `prompt_body_release_header`, is modelled on `prompt_body_governance_state` and
  uses the same normaliser.
- `validate_prompt_bodies` (`:2333`–`:2335`) emits `PROMPT_BODY_RELEASE_HEADER:<id>`.
- The `:904`–`:908` comment is rewritten to cite D23-G.
```
RELEASE_HEADER_KEYS = ("Prompt Version:", "Prompt version:", "Set:", "Ecosystem release:")

def prompt_body_release_header(nonblank: list[str]) -> bool:
    """True when the header window carries a release-bound line, which D23-G prohibits."""
    stripped = [governance_line_normalised(line) for line in nonblank[:8]]
    return any(line.startswith(key) for line in stripped for key in RELEASE_HEADER_KEYS)
```
```
        if prompt_body_release_header(nonblank):
            errors.append(f"PROMPT_BODY_RELEASE_HEADER:{prompt_id}")
```
An old seven-line header now gives exactly `PROMPT_BODY_RELEASE_HEADER`. It does not also give
`PROMPT_BODY_IDENTITY`. Regressions: R-HDR-1 to R-HDR-3.

**2. `PR35_ADDED_BOUNDARY` → exact map** (`:1742`–`:1743`). Sources: fv-main:2, fv-rest:15, §4
G9–G10, and sweep:11, which retires fv-main:2's opposite fixture. The ten zeros are KEEP. "Session may
be nonzero" is not the rule.
```
EXPECTED_PR35_ADDED_BOUNDARIES = {
    "approval": 0, "cross_session_route": 1, "duplicate_work_vehicle": 0, "merge_authority": 0,
    "proceed": 0, "product_owner_gate": 0, "r1_row": 0, "role": 0, "session": 1, "work_unit": 0,
    "work_vehicle": 0,
}
    if not isinstance(development, dict) or development.get("added_boundaries") != EXPECTED_PR35_ADDED_BOUNDARIES:
        errors.append("PR35_ADDED_BOUNDARY")
```
Regressions: R-AB-1 to R-AB-3.

**3. `PR_PHASE_CONTINUITY`** (`:876`–`:880`, `:1744`–`:1745`). Source: fv-main:3.
- The list is the nine fields in order.
- The exact comparison is KEEP.
- The explicit absence test fv-main:3 asks for emits the same code.
```
EXPECTED_PHASE_CONTINUITY = [
    "WORK_UNIT_ID", "original Product Owner Proceed",
    "workspace/worktree", "branch", "pull request", "PR instruction", "detailed PR plan",
    "primary skill authority", "continuous recovery/artifact lineage",
]
    if not isinstance(development, dict) or development.get("shared_exactly_one") != EXPECTED_PHASE_CONTINUITY or "dedicated PR-development session" in development.get("shared_exactly_one", []):
        errors.append("PR_PHASE_CONTINUITY")
```
Regression: R-PC.

**4. `EXPECTED_PR35_RESULTS`** (`:853`–`:856`). Sources: sweep:3, adversary:9, A1-5. The value is
used at `:1747` (`PR35_RESULT_VOCABULARY`) and `:1921` (`PR35_STATE_ROUTES`).
```
EXPECTED_PR35_RESULTS = [
    "MERGE_PENDING", "MERGE_OBSERVED", "RESCOPE_PENDING", "RECOVERY_PENDING", "REMOTE_EVIDENCE_PENDING",
    "PRODUCT_OWNER_DECISION_REQUIRED",
]
```
Regressions: R-V-1, R-V-2.

**5. `DIRECT_PR35_PR40_EDGE` and `GRAPH_DIRECT_PR40_EDGE` → one exact positive rule** (`:1837`–`:1838`,
`:1349`–`:1355`).

Sources: fv-main:11, pr-relay-graph:22, fv-rest:20, coverage:19, adversary:9, sweep:0, A1-5, A1-7,
and §4 E4–E5.
- **The rule.** Exactly PR-35 and RS-40, each with exactly one edge to PR-40. Each edge is a prompt
  edge with `automatic: false`, transport `COMPLETE_NEXT_PROMPT_HANDOFF` and sole state
  `MERGE_OBSERVED`. It has one `merge_observed` branch whose condition is A1-7's exact string.
  Exact condition equality, rather than a substring, is **O31**.
- **The narrowing, stated as AF-001 requires.** `GRAPH_DIRECT_PR40_EDGE`'s prohibition set shrinks
  from `{"PR-30", "PR-35"}` to `{"PR-30"}`. PR-35 and RS-40 may now route to PR-40, but only on this
  exact edge.
- **Kept:**
  - `DIRECT_PR30_PR40_EDGE` (`:1835`–`:1836`), with its fixture;
  - "no agent merges", guarded by `agent_merge_authorized` and `POST_MERGE_CONTRACT`;
  - "no entry before Nathan merges", guarded by R-DE-5.
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
In `validate_contract`, in place of `:1837`–`:1838`:
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
Regressions: R-DE-1 to R-DE-8.

**6. `PR40_MANUAL_MERGE_BOUNDARY`** (`:1925`–`:1948`). Source: fv-main:12. A1-5 keeps the fallback
boundary and leaves the DOC-20 → PR-40 edge unchanged.
- The boundary half is KEEP: exactly one edge from `NATHAN_MANUAL_MERGE_ASSERTION`, `automatic:
  false`.
- The DOC-20 half is KEEP: every other prompt inbound edge is DOC-20, `automatic: false`, with "after
  Nathan asserts the manual merge".
- The PR-35 and RS-40 observed-merge edges leave the recovery list. Rule 5 owns them, so one defect
  fires one code.
```
    recovery_pr40 = [edge for edge in inbound_pr40 if edge.get("from_kind") == "prompt" and edge.get("from") not in OBSERVED_MERGE_EDGE_CONDITIONS]
```
Regressions: R-MB-1 to R-MB-4.

**7. `POST_MERGE_CONTRACT` and `POST_MERGE_THREE_EVENTS`** (`:1768`–`:1780`).
- `direct_PR35_to_PR40_automatic_edge: False` is KEEP. A1-5 supersedes fv-main:13's "True"
  (sweep:11).
- `agent_merge_authorized: False` is KEEP.
- `event_1` and `event_3` are KEEP, as is `event_2.actor`.
- `event_2.fact` is REPLACED with §4 G14's value (sweep:10).
```
        or (postmerge.get("event_2") or {}).get("fact") != "product_owner_manual_merge_observed_or_asserted"
```
- No check is compiled for §4's `pr35_observed_merge_edge` record (**O33**), or for `event_2.time`.

Regressions: R-PM-1 to R-PM-3.

**8. `ROUTE_GRAPH_SHORTHAND`** (`:1782`–`:1798`). Exact equality is KEEP. The literal equals §6's
`route_graph`. The three keys that change come from sweep:10 and child C8. The other keys are
unchanged. If §6 differs, §6 governs.
```
        "ordinary_pr_work_unit": ["PR-10", "PR-20", "NATHAN_PROCEED", "PR-30", "PR-35", "PR-40"],
        "pr35_no_subscription_fallback": ["PR-35", "NATHAN_MANUAL_MERGE_ASSERTION", "PR-40"],
        "pr40_reject_replan": ["PR-40", "PR-20", "NATHAN_PROCEED", "PR-30"],
```
Regressions: R-RG-1, R-RG-2.

**9. The PR-40 re-plan route.** This is new, placed after rule 5 in `validate_contract` (child C8;
fv-main:30). It asserts that the PR-40 `REJECT` branch targets PR-20 and that no PR-40 edge goes to
PR-30. `rescope_contract.new_proceed_required: False` stays KEEP (C8).
```
        replan = [e for e in edges if isinstance(e, dict) and e.get("from") == "PR-40" and any(isinstance(b, dict) and b.get("branch_id") in {"reject_replan", "reject_existing_pr_owner"} for b in e.get("route_branches", []))]
        if len(replan) != 1 or replan[0].get("to") != "PR-20" or any(isinstance(e, dict) and e.get("from") == "PR-40" and e.get("to") == "PR-30" for e in edges):
            errors.append("PR40_REJECT_REPLAN_ROUTE")
```
Regressions: R-RP-1, R-RP-2.

**10. `receiver_compatibility` content check.** This is new, at the end of `validate_contract`. A1-6
says the v4 validator "gains the `receiver_compatibility` content check it lacks" (adversary:10,
fv-main:32, coverage:13, child C9, sweep:21).
- It is exact equality per receiver, with the expected table equal to §6's `receiver_compatibility`.
- The code follows the v3 precedent (`validate_gcfpe_current.py:446-448`).
- It is C9's verification. No entry except PR-20 accepts a `PR_WORK_UNIT_LINEAGE_REVIEW` `REJECT`.
```
    receivers = contract.get("receiver_compatibility")
    for receiver in sorted(set(EXPECTED_RECEIVERS) | set(receivers or {})):
        if not isinstance(receivers, dict) or receivers.get(receiver) != EXPECTED_RECEIVERS.get(receiver):
            errors.append(f"RECEIVER_CONTRACT:{receiver}")
```
Regressions: R-RC-1 to R-RC-4.

**11. `HANDOFF_CONTRACT` → exact-key check** (`:1481`–`:1494`). A1-2 ("`HANDOFF_CONTRACT` becomes an
exact-key check"), fv-main:17, fv-rest:13, adversary:3.
- The key set must equal §6's `transition_contract` key set, and every value must equal §6's.
- `prohibited_references` sits in the key set. Its value is left to `HANDOFF_PROHIBITED_REFERENCES`,
  so one defect fires one code.
- `actual_pasteable_complete_prompt: True` is KEEP, so fixture `reject-incomplete-handoff` still
  guards it.

`HANDOFF_PROHIBITED_REFERENCES` (`:1495`–`:1500`) becomes the old five entries plus step 12's three:
```
        "Library ID", "unlinked filename", "above", "conversation reconstruction",
        "model/strength/reasoning/eligibility/suitability/account/configuration route",
        "branch", "commit", "restated artifact content",
```
The graph ⊆ contract prohibited-reference parity check (fv-main:17, coverage:12) is **O32**.
Regressions: R-HC-1 to R-HC-3.

**12. R1 identity claims** (`:1951`–`:1957`, `:1960`–`:1967`, `:1375`–`:1382`, `:1127`–`:1133`). A1-2:
"the R1 identity flags tell the truth: `r1_oracle_changed: true`".
- `:1966` `r1_oracle_changed` becomes `True`.
- `:1956` `protected_r1_46_rows_unchanged` takes §6's value. The simulated value is `False` (fv-rest:3;
  coverage:11, whose kept-row check is §5's).
- `:1964`, `:1379` and `:1130`: `r1_oracle_sha256` takes the successor digest from §5.
- `:1131` and `:2611`: `r1_runtime_map_sha256` takes the successor map digest and path from §5.
- **KEEP:**
  - `r1_rows` 46, `r1_core_rows` 26 and `r1_material_rows` 20;
  - `pr35_adds_r1_row: False`;
  - `flowmaster_primary_core_changed: False` and the core digest `4d8bb9bf…`;
  - `pr35_same_r1_row_as_pr30: True` (`:1953`) and `PR-35_same_r1_row_as_PR-30` (`:1367`; §4 G11).

Regressions: R-R1-1 to R-R1-3.

**13. Kept deliberately.**
- `PRESERVATION_CONTRACT` `versioned_sibling_successors: True` (`:1972`). A1-2 and A1-3 keep it,
  which supersedes fv-main:31.
- `EXPECTED_CONTRACT_TOP_LEVEL_KEYS` (`:339`–`:398`) is unchanged, because no top-level key is added
  (A1-5).

**14. Other literals.**
- `:1390` `contract_revision` → `"4.1.0"` (A1-2; fv-main:35). Regression: R-ID.
- `:207`–`:208` → `fecc319bdd4ce7ee6201cb77d7231861` / `284` (A1-7; fv-main:9). Every route-edge
  regression also shows `ROUTING_SURFACE_CHANGED`.
- `:1722` `primary_skill_revision` → `"1.3.0"`. This is §8a.5's value at a site in this package.
  Regression: R-PS.
- `:1090` `validator_revision` → **O27**.
- `:1118` `edge_count` → `229` (A1-7; fv-main:15).
- `:1123` `count` → the O29 count.
- `:941`–`:945` are byte pins, set in §5's order (fv-main:16, fv-main:29): graph sha and bytes,
  contract sha and bytes, fixture sha.
- `:2441`–`:2450` `exact_markers` (sweep:2, fv-rest:21, fv-main:33). PR-40's three markers are KEEP
  ("historical pre-merge", "independent", "glow-merged-change-attribution-lock"; child C4).
  ```
        "PR-35": ("REMOTE_EVIDENCE_PENDING", "PR_REMOTE_ACTION_LEDGER", "MERGE_PENDING", "MERGE_OBSERVED"),
        "RS-40": ("SOURCE_RESOLUTION_ERROR", *EXPECTED_RETURN_PHASES, "MERGE_OBSERVED"),
  ```
  Regression: R-MK.
- `:2580`–`:2586` `CHANGE_FLOW_CONTRACT`. KEEP all markers. The revision marker reads profile
  `installed_skill_revisions['change-flow']`, which becomes `3.3.0`.
- `:2590`–`:2597` `SKILL_CONTRACT`. `:2592` becomes `1.3.0` and `:2594` becomes `{NINE}` (fv-main:24).
  `:2593`, `:2595` and `:2596` are KEEP (fv-main:25). §8a.6 measured these.
- `:2607`–`:2609` `PRIMARY_FILE_IDENTITY` `0665507…` is KEEP.
- **Comments, not checks.**
  - `:2657`–`:2659` and runner `:726` take C-D22 (step 45; fv-main:34).
  - The docstring at `:2288`–`:2291` has no persistence clause. It falls under §3 open question 8
    (**O26**).

### 8b.8 `validate_flowmaster.py`, `validate_gcfpe_current.py`, `run_gcfpe_current_fixtures.py`

**Revisions** (fv-rest:26, pr-relay-graph:16, sweep:5, adversary:17):
```
validate_flowmaster.py:128   "TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0",
validate_flowmaster.py:147   "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",
validate_flowmaster.py:182   "SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0",
validate_flowmaster.py:686   "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0",     (maintenance_metadata value; its key "…: 2.0.0" is the oracle's token and stays)
validate_flowmaster.py:1221  "validator_revision": <O27>,
validate_gcfpe_current.py:634-635   "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0" (both occurrences)
```

**`CONTRACT_REQUIRED`** (A1-6). `{OVERRIDE}` is added as one entry to each of `tw-flowmaster` (after
`:128`), `change-flow` (after `:147`) and `session-relay-flowmaster` (after `:182`). Every existing
entry is KEEP. `:148`, the R1 profile id, is §5's.

**`CONTRACT_FORBIDDEN`.** These are append-only; no existing entry is narrowed.
- **`session-relay-flowmaster`** (after `:334`):
  - "same-session PR-35 handoff" (N4; pr-relay-graph:19);
  - "preferred live control plane" (N4; pr-relay-graph:19);
  - "launched as a new session" (first-draft N6, the task's N6).
- **`tw-flowmaster`** (after `:309`):
  - "same-session PR-35 handoff";
  - "preferred live control plane";
  - "The Product Owner's PR-40 invocation supplies merge approval" (sweep:5).
- Whether each skill also takes the other skill's extra phrase is **O4**.
- Measured: none occurs, case-insensitively, anywhere in either edited file, the core included.
```
    "tw-flowmaster": (
        …existing four…,
        "same-session PR-35 handoff",
        "preferred live control plane",
        "The Product Owner's PR-40 invocation supplies merge approval",
    ),
    "session-relay-flowmaster": (
        …existing eleven…,
        "same-session PR-35 handoff",
        "preferred live control plane",
        "launched as a new session",
    ),
```

**`OPTIONAL_REFERENCES['change-flow']`** (`:360`–`:364`). The allowlist must equal the links in
`SKILL.md` (sweep:7, adversary:10).
- Add `references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json`, which `:559` now links.
- Whether `references/gcfpe-current-direct-handoff-contract.json` stays depends on **O12**. The
  simulated option (a) removes it, because `:559` no longer links it.
- The runtime-map entry follows §5's `:557` link.

**Default overlay path** (fv-rest:23, adversary:10). Under **O12**, option (a) (simulated) re-points
three sites to the 091426.1 contract. Its schema-4.0 dispatch (`validate_gcfpe_current.py:619-622`,
`run_gcfpe_current_fixtures.py:105-109`) then runs the v4 validator and the v4 fixtures in the default
suite:
```
validate_gcfpe_current.py:615        change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
run_gcfpe_current_fixtures.py:104    change_skill_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
validate_flowmaster.py:818           str(change_dir / "references" / "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),
```

The following stay as they are:
- The v3 path, reached only when the historical alias is passed explicitly. Its literals
  `validate_gcfpe_current.py:651` (→ `1.3.0`, per §8a.5) and `:652` ("one dedicated PR-development
  session", which §8a's edits remove from the PR skill) are **O14**.
- `validate_gcfpe_current.py:80`–`:83`, which are historical (fv-main:21; §5).
- `validate_gcfpe_20260914.py:2557`–`:2575`, which run only for an `UNSELECTED_CANDIDATE` contract.
- `validate_gcfpe_current.py:602`, whose `NameError` on `--bodies-stdin` is out of scope (amendment,
  *Noticed, not in scope*; fv-rest:24).

**§5's sites, listed here and not changed by this section:**
- `validate_flowmaster.py:24`–`:42`, `:148`, `:355` and `:360`–`:364` (the runtime-map entry);
- `run_change_flow_fixtures.py:15`;
- `validate_gcfpe_20260914.py:1130`–`:1131`, `:1379`, `:1964` and `:2610`–`:2612`;
- the validation profile at `:35` and `:37`;
- `validate_gcfpe_current.py:81` and `:659`;
- the historical-layer pins, which are never edited: `validate_strength_middleware.py:14`,
  `validate_integrated_readiness.py:8`/`:150`, `validate_pre_guide_correction.py:9`/`:66` and
  `validate_final_scan.py:68` (sweep:8).

### 8b.9 Fixtures: `run_gcfpe_20260914_fixtures.py` and `scenarios.json`

The rules the fixtures must express come from the findings. Their ids, fact names and labels are
**O29**. The simulated option (a) adds four scenario ids. Option (b) uses variants only, which keeps
33/18/15.

**Projection changes (`project_behavior`).**
- **`pr_split`** (fv-main:5, fv-main:6, fv-rest:16).
  - `requests_new_session` leaves the failure test and `pr35_in_pr30_session` enters it.
  - The positive requires `new_dedicated_pr35_session` and the exact `EXPECTED_PR35_ADDED_BOUNDARIES`
    map, and returns `PR30_TO_PR35_NEW_DEDICATED_SESSION`.
  - The extra-Proceed failure is KEEP.
- **`handoff`** (fv-main:7, fv-main:28, fv-rest:20, coverage:3, coverage:19, sweep:14, adversary:9).
  - **PR-30 → PR-35:** accepted only with `same_session` false and `session_disposition:
    NEW_DEDICATED`.
  - **Any PR-40 entry:** `automatic_dispatch`, `session_created_by_agent` or `merge_performed_by:
    agent` fails.
  - **The fallback** is KEEP (`PR40_CONDITIONAL_HANDOFF_ACCEPTED`), and now also requires that no
    `MERGE_OBSERVED` result was returned (A1-5's predicate).
  - **The observed merge** (`PR40_OBSERVED_MERGE_HANDOFF_ACCEPTED`) requires:
    - origin PR-35 or RS-40;
    - an active subscription and the observed merge event;
    - `merge_performed_by: Nathan`, and the three events separate;
    - the contract's `direct_PR35_to_PR40_automatic_edge` false.
  - The five runnable-prompt negatives are KEEP (C-HANDOFF).
- **`replan`**, new (child C8, fv-main:30).
  - It accepts a PR-40 `REJECT` for a precise in-scope defect only under all of these:
    - the receiver is PR-20;
    - the session is a new top-level one that Nathan creates;
    - the plan is new, with a new Proceed on it;
    - the contract's `reject_replan` edge targets PR-20;
    - `new_proceed_required` is false.
  - A second Proceed on the same plan, a Proceed between PR-30 and PR-35, or a receiver of PR-30
    fails.
- **`observation`** is KEEP. Its `same_session_reentry` names the PR-35 session's own re-entry.

**Scenario edits** (simulated option (a)). `scenarios.json` keeps its hand layout: pretty-printed
header keys, and one compact row per line.
- **PR-SPLIT-POS-01:** the input fact `same_session_pr35` becomes `new_dedicated_pr35_session`. The
  expected value becomes `PR30_TO_PR35_NEW_DEDICATED_SESSION`.
- **PR-SPLIT-NEG-01:** the input becomes `{requests_additional_proceed, pr35_in_pr30_session}`. The
  variant `new-session-only` becomes `pr35-in-pr30-session-only`. Its attribution
  `PR35_ADDED_BOUNDARY` is KEEP.
- **HANDOFF-POS-01, HANDOFF-NEG-01 and all five of its variants:** `same_session` becomes false, with
  `session_disposition: NEW_DEDICATED`.
- **HANDOFF-POS-02** is kept for the fallback (coverage:19). It gains the variant
  `subscription-accepted-not-delivering` (sweep:14, coverage:3).
- **New HANDOFF-POS-03** is the `MERGE_OBSERVED` positive, with an RS-40 variant (sweep:0).
- **New HANDOFF-NEG-02**, with these variants:
  - `before-any-merge`;
  - `observed-without-active-subscription`;
  - `agent-merge`;
  - `automatic-dispatch`;
  - `fallback-after-merge-observed`.
- **New REPLAN-POS-01** and **REPLAN-NEG-01**. REPLAN-NEG-01's variants are
  `second-proceed-same-plan`, `proceed-between-pr30-and-pr35` and `reject-routed-to-pr30`.
- `required_fixture_ids` gains the four ids, and `negative_rule_attribution` and
  `EXPECTED_NEGATIVE_RULES` (runner `:31`–`:47`) gain two labels. In the simulation:
  ```
  "HANDOFF-NEG-02": "PR40_ENTRY_ON_OBSERVED_OR_ASSERTED_MERGE",
  "REPLAN-NEG-01": "PR40_REJECT_REPLAN_PROCEED",
  ```
- **Counts** (runner `:258`, `:260`, `:267`): 37 ids, 20 positive, 17 negative.

**Runner-level cases.**
- **Independent cases.**
  - `("requests_additional_proceed", "requests_new_session")` becomes
    `("requests_additional_proceed", "pr35_in_pr30_session")` (`:324`).
  - The five `independent-handoff-*` cases take `same_session: False` with
    `session_disposition: NEW_DEDICATED` (`:332`).
- **Mutation cases.** `reject-pr35-direct-pr40` (`:361`) is reversed into
  `reject-second-pr35-pr40-edge`, with the same append and the same expected set. Its meaning is now
  "a second edge" (fv-main:11, fv-rest:20, adversary:9). The cases of 8b.10 are then appended. Each
  compares exact error sets, as the runner does now.
- **Kept mutation cases:**
  - `reject-new-proceed-boundary`, which now proves the exact map;
  - `reject-pr30-direct-pr40`;
  - `reject-missing-pr35-result`;
  - `reject-agent-merge`;
  - `reject-incomplete-handoff`;
  - `reject-primary-core-change`.
- **Header cases.**
  - `clean_header` is rebuilt as title, `Prompt ID: PR-35`, `Notion URL: …` and
    `## Native purpose`, padded to the O28 floor. It has 4 lines when the floor is 4.
  - The two URL-label mutations re-index from 5 to 2.
  - The four URL-label negatives are KEEP.
  - Added: `accept-header-free-of-release-lines`, plus ten `reject-release-header-*` cases: `Prompt
    Version:`, `Prompt version:`, `Set:` and `Ecosystem release:`, each plain, then bold, bullet,
    blockquote, bold-label-only, code-span and table-cell forms. They are drawn from the
    governance-state vector list (fv-main:1). How many of that list's 18 vectors are carried is part
    of O29. The measurement in 8b.12 fired on 12.
- **Other literals:** the runner docstring `:2` ("33"), and `:702` `validator_revision` (O27).

**Pins** (fv-main:29): `EXPECTED_FIXTURE_SHA256` (`:945`), and the profile's `fixtures.sha256` and
`count` (`:15`, `:12`). Both are set after `scenarios.json` is final, in §5's order.

**Not in this section.** Child C3's R1 path fixture, GCF-17.LINEAGE → GCF-14, belongs in
`fixtures/change-flow/scenarios.json`, which is §5's.

### 8b.10 Must-fail regressions

The contract-side regressions run on the candidate contract. The header and body regressions run on
in-memory text. The skill-text regressions run on a scratch copy of the edited tree. The fixture-suite
counterpart of each contract regression is the mutation case of the same meaning (8b.9).

Each regression, as `id — what it serves — the mutation`:

```
R-CF-1…13    change-flow retired-phrase loop    inject each of the 13 phrases, one per run, before <!-- FLOWMASTER_SPECIALIZATION_END -->
R-CF-A18     change-flow NEW literal            delete C-SESSION's A1-8 sentence at :301
R-CF-9       :1022                              delete {NINE}
R-CF-REV     :746                               revision 3.3.0 → 3.2.9
R-OV-1…3     CONTRACT_REQUIRED override         replace {OVERRIDE} in change-flow, relay or tw
R-FB-R1…3    relay CONTRACT_FORBIDDEN           inject each relay phrase
R-FB-T1…3    tw CONTRACT_FORBIDDEN              inject each tw phrase
R-REV-R, R-REV-T revision pins                      relay 3.1.0 → 3.0.0; tw 1.2.0 → 1.1.6
R-HDR-1      release header                     a body with Prompt Version: 091426.1 after its Prompt ID: line
R-HDR-2      release header                     each decorated vector in the header window
R-HDR-3      kept identity half                 the four URL-label negatives
R-AB-1…3     exact map                          session 1→0; cross_session_route 1→0; proceed 0→1
R-PC         continuity                         re-insert "dedicated PR-development session" at index 2
R-V-1, R-V-2 vocabulary                         contract list without MERGE_OBSERVED; registry PR-35 result_states without it
R-DE-1…8     positive rule                      see the expected sets below
R-MB-1…4     manual-merge boundary              remove the boundary edge; boundary automatic true; DOC-20 condition loses its phrase; a QA-10 prompt edge into PR-40
R-PM-1…3     post-merge                         automatic-edge flag true; event_2.fact → product_owner_manual_merge_assertion; agent_merge_authorized true
R-RG-1, R-RG-2 shorthand                          old ordinary_pr_work_unit; drop pr40_reject_replan
R-RP-1, R-RP-2 re-plan route                      PR-40 REJECT edge and state route → PR-30; new_proceed_required true
R-RC-1…4     receivers                          PR-35 old same-session flag; PR-40 nathan_manual_merge_assertion_required; PR-30 gains a REJECT context; PR-20 removed
R-HC-1…3     handoff                            re-insert status_completed_work_decisions_constraints_unresolved_authority; actual_pasteable_complete_prompt false; drop branch from prohibited_references
R-R1-1…3     R1 claims                          r1_oracle_changed false; protected_r1_46_rows_unchanged true; pr35_adds_r1_row true
R-ID         revision                           contract_revision 4.0.6
R-PS         primary skill                      primary_skill_revision 1.2.5
R-MK         markers                            a PR-35 body without MERGE_OBSERVED
```

Expected results. `RS` stands for `ROUTING_SURFACE_CHANGED`.

```
R-CF-n        exit 1; stdout "FAIL: retired skill clause present: <phrase n>"; non-fail-fast count 1
R-CF-A18      exit 1; "FAIL: missing skill clause: never as a subagent, forked agent or workflow agent of PR-30"
R-CF-9        exit 1; "FAIL: missing skill clause: {NINE}"
R-CF-REV      exit 1; "FAIL: specialization revision"
R-OV-n        FLOWMASTER_SUITE_FAIL; that skill only: "missing specialization contract: {OVERRIDE}"
R-FB-*        FLOWMASTER_SUITE_FAIL; that skill only: "superseded contract present: <phrase>"
R-REV-R       session-relay-flowmaster only: "missing specialization contract: SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0"
R-REV-T       tw-flowmaster only: "missing specialization contract: TW_FLOWMASTER_SPECIALIZATION_REVISION: 1.2.0"
R-HDR-1       {PROMPT_BODY_RELEASE_HEADER:PR-35}
R-HDR-2       prompt_body_release_header true for all 12 vectors; identity stays valid
R-HDR-3       prompt_identity_header_valid false for all four
R-AB-1..3     {PR35_ADDED_BOUNDARY}
R-PC          {PR_PHASE_CONTINUITY}
R-V-1         {PR35_RESULT_VOCABULARY}
R-V-2         {PR35_STATE_ROUTES, STATE_REGISTRY_MISMATCH:PR-35}
R-DE-1  second PR-35→PR-40 edge                        {DIRECT_PR35_PR40_EDGE, RS}
R-DE-2  PR-35→PR-40 automatic true                     {DIRECT_PR35_PR40_EDGE, RS}
R-DE-3  RS-40→PR-40 automatic true                     {DIRECT_PR35_PR40_EDGE, RS}
R-DE-4  PR-35→PR-40 merge condition missing            {DIRECT_PR35_PR40_EDGE, RS}
R-DE-5  PR-40 entered before any merge (MERGE_PENDING) {DIRECT_PR35_PR40_EDGE, RS}
R-DE-6  RS-40→PR-40 edge removed                       {DIRECT_PR35_PR40_EDGE, RS, STATE_EDGE_MISMATCH:RS-40:merge_observed}
R-DE-7  PR-30→PR-40 edge (kept)                        {DIRECT_PR30_PR40_EDGE, RS}
R-DE-8  graph and contract both gain a second PR-35 edge: contract {DIRECT_PR35_PR40_EDGE, RS}; graph {GRAPH_DIRECT_PR40_EDGE}
R-MB-1..4     {PR40_MANUAL_MERGE_BOUNDARY, RS}
R-PM-1        {POST_MERGE_CONTRACT}
R-PM-2        {POST_MERGE_THREE_EVENTS}
R-PM-3        {POST_MERGE_CONTRACT}
R-RG-1, -2    {ROUTE_GRAPH_SHORTHAND}
R-RP-1        {PR40_REJECT_REPLAN_ROUTE, RS}
R-RP-2        {RESCOPE_CONTRACT}
R-RC-n        {RECEIVER_CONTRACT:<that receiver>}
R-HC-1, -2    {HANDOFF_CONTRACT}
R-HC-3        {HANDOFF_PROHIBITED_REFERENCES}
R-R1-1, -3    {PROTECTED_IDENTITIES}
R-R1-2        {GRAPH_PROOFS}
R-ID          {CONTRACT_IDENTITY}
R-PS          {PR_DEVELOPMENT_CONTRACT}
R-MK          {PROMPT_ROUTE_SEMANTICS:PR-35:MERGE_OBSERVED}
```

**A limit, measured.** Reverting `{NINE}` to `{TEN}` in place fires two checks: the new literal goes
missing, and the old one is retired. Only the injection form meets "exactly its own finding", as
§8a.4 found for the PR skill.

A second limit: `flowmaster-validate/SKILL.md` prose has no literal guard. Only
`SKILL_TREE_SHA256` reads it.

### 8b.11 Revisions and pin sites

The amendment's *New revisions* say that every revision pin moves in the same set. The byte and
identity pins are set in §5's order: matrix → oracle → runtime map → graph → contract → profile →
literals → fixtures → `SKILL_TREE_SHA256` last.

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

validator_revision 3.2.14 → <O27>
  flowmaster-validate/scripts/validate_flowmaster.py:1221
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1090
  flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:702
  flowmaster-validate/references/gcfpe-20260914.1-091426.1-validation-profile.json:45

glow-hde-pr-development 1.2.5 → 1.3.0, sites in this package (value §8a.5)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:1722, :2592
  flowmaster-validate/scripts/validate_gcfpe_current.py:651          (O14)
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
  flowmaster-validate/references/…-validation-profile.json:20
  change-flow/scripts/validate_gcfpe_20260914.py:806

bundled graph sha and bytes (value from the final build, §5 order)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:941, :942
  change-flow/scripts/validate_gcfpe_20260914.py:21
  validation profile :19, :24

contract sha and bytes (value from §6's regenerator, §5 order)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:943, :944
  validation profile :4, :8

fixtures sha and count (O29)
  flowmaster-validate/scripts/validate_gcfpe_20260914.py:945, :1123
  flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py:2, :258, :260, :267 (and :31-:47 attribution)
  validation profile :12, :15
  flowmaster-validate/SKILL.md:176, :381, :383

R1 identities and paths: §5 (listed in 8b.8)

SKILL_TREE_SHA256 (last)
  flowmaster-validate/SKILL.md:9
```

### 8b.12 Measured

Every experiment ran on copies under `/tmp/claude-0/spec/s8b/`. They ran with
`PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` inside the scratch area. Afterwards no `.pyc` existed in
any copy. Nothing in the synced skills or the repository was written, and no prompt body was read.
The simulated options are the defaults marked above.

1. **Copy A: the SKILL.md edits and validator literals of 8b.1–8b.6 and 8b.8,** with today's
   contract, graph and R1 files, and `SKILL_TREE_SHA256` recomputed.
   - The default suite returned `FLOWMASTER_SUITE_PASS`. `gcfpe_current_fixtures` ran the v4 set,
     172 cases, all OK, through the re-pointed default.
   - `--strict-warnings --gcfpe-contract … --gcfpe-candidate-root <graph-only root>` returned
     `FLOWMASTER_SUITE_PASS` with zero findings.
   - The `change-flow` validator returned `PASS`.
   - `validate_gcfpe_20260914.py` returned `ok: true`, and its fixtures 172/172.
   - The relay self-test returned `PASS`, 230 cases, 0 failed.
   - `validate_gcfpe_current.py` returned `ok: true`, and `run_change_flow_fixtures.py` returned
     `fixture_suite_ok: true`.
   - The embedded core measured `4e565e40…` in all three edited skills.
2. **Regressions on copy A.**
   - Each of the 13 retired-phrase injections gave exit 1 and exactly its own line, with a
     non-fail-fast count of 1.
   - R-CF-A18, R-CF-9 and R-CF-REV each gave exactly one failure.
   - R-OV-1…3, R-FB-R1…3, R-FB-T1…3, R-REV-R and R-REV-T each gave exactly one error, in the named
     skill only.
   - The in-place `{NINE}`→`{TEN}` revert gave two, which is the stated limit.
3. **Copy B: the 8b.7 reversals, on a measurement candidate.** The candidate was:
   - §6's prototype output `/tmp/claude-0/spec/s6/after_contract.json` and `after_graph.json`;
   - with `cross_session_route` 1 (§4 G10);
   - with a stand-in `receiver_compatibility` table that has PR-20 added and PR-35 and PR-40 per
     sweep:10;
   - with `route_graph.pr35_no_subscription_fallback` added.

   The stand-ins are for measurement only; §6 governs the values. Results:
   - `validate_contract` and `validate_graph_contract` both returned `[]`.
   - `routing_surface` returned `('fecc319bdd4ce7ee6201cb77d7231861', 284)`, with 229 edges.
   - All 38 contract and graph regressions of 8b.10 gave exactly their expected sets.
   - Today's 091426.1 contract under the new validator returns 18 codes, so every reversal rejects
     the old state:
   ```
   CONTRACT_IDENTITY DIRECT_PR35_PR40_EDGE GRAPH_PROOFS HANDOFF_CONTRACT HANDOFF_PROHIBITED_REFERENCES
   POST_MERGE_THREE_EVENTS PR35_ADDED_BOUNDARY PR35_RESULT_VOCABULARY PR35_STATE_ROUTES PR40_REJECT_REPLAN_ROUTE
   PROTECTED_IDENTITIES PR_DEVELOPMENT_CONTRACT PR_PHASE_CONTINUITY RECEIVER_CONTRACT:PR-20 RECEIVER_CONTRACT:PR-35
   RECEIVER_CONTRACT:PR-40 ROUTE_GRAPH_SHORTHAND ROUTING_SURFACE_CHANGED
   ```
4. **The header.**
   - With floor 4, a 4-line identity header is valid, and an old 7-line header is identity-valid
     but raises the release header.
   - With floor 7, the 4-line header is invalid, so fv-rest:22's padding is needed.
   - All 12 decorated vectors fire. The prose controls, inside and outside the window, are silent.
   - The four URL-label negatives still reject.
   - R-HDR-1 and R-MK gave exactly their codes on a synthetic PR-35 text.
5. **The fixture runner, option (a),** on the candidate: 216 cases, 0 failed. `profile_errors` was
   `PROFILE_FIXTURE_HASH` and `PROFILE_GRAPH_PIN` before the pins moved.
   - Against today's 172 cases, 3 are removed: `PR-SPLIT-NEG-01::new-session-only`,
     `independent-requests_new_session` and `reject-pr35-direct-pr40`. 47 are added.
   - Today's `scenarios.json` under the new runner fails `PR-SPLIT-POS-01`, `HANDOFF-POS-01` and the
     document-shape checks, so the old fixtures are rejected.
6. **Copy B2: B with the candidate written into both skills and every §8b pin moved to the
   candidate's measured identities.** The R1 digests are today's, standing in for §5's.
   - The strict candidate suite returned `FLOWMASTER_SUITE_PASS`, zero findings, with both 216-case
     suites OK.
   - The default suite returned `FLOWMASTER_SUITE_PASS`.
   - The `change-flow` validator returned `PASS`.
   - All 12 historical-layer commands of §2 gave output byte-identical to the baseline, all exit 0.

### 8b.13 Findings placed, and rows superseded

**Placed here.** Where the value belongs to §5 or §6, the site is placed here and the value is
cited.
- **Preflight:**
  - fv-main:0–3, 5–7, 9, 11–17, 19, 23–35 (and 18, 20, 21 as §5 pin sites);
  - fv-rest:3, 9–26, 28 (and 0–2, 4–8, 27 as §5 sites, 29 as §9's command);
  - pr-relay-graph:16–22, 32.
- **Critics:**
  - coverage:3, 4, 7–9, 12–15, 19, 23;
  - sweep:0, 2, 3, 5–8, 10–14, 20–22;
  - adversary:1, 3, 7, 9, 10, 13, 16, 17.

**Superseded by the amendment.** These are recorded so §E can cite them (coverage:7, sweep:11):

| row | superseded part | governed by |
|---|---|---|
| fv-main:2 | fixture "reject-cross-session-route=1"; the map with `cross_session_route` 0 | §4 G10, sweep:11: the negative is `cross_session_route` = 0 |
| fv-main:9 | 281/282 rows | A1-7: 284 |
| fv-main:13 | `direct_PR35_to_PR40_automatic_edge` true | A1-5: stays false |
| fv-main:15 | edge count 226 | A1-7: 229 |
| fv-main:20, fv-rest:1, fv-rest:2 | in-place re-pin of historical map and alias | A1-1 (§5) |
| fv-main:31 | change `versioned_sibling_successors` | A1-2, A1-3: kept |
| fv-rest:20 | rewrite HANDOFF-POS-02 | A1-5, coverage:19: kept for the fallback |
| fv-rest:23 | "record the alias as a known contradiction" | A1-6: re-pointed |
| sweep:13 | predicate "where no subscription existed" | A1-5's single predicate |

**Anchor corrections**, where the site named is unambiguous:
- sweep:5 cites `tw-flowmaster:9`; the revision is on `:8`.
- Step 45's old string is at `:231`–`:232`, not at `:55`–`:60`.

### 8b.14 Open questions

Each is left open. The simulated option, where there is one, is marked. It is not a ruling.

1. **O1 — The override's position.** A1-6 fixes only "outside the core", and sweep:6 says "in the
   specialization block". Any position between the specialization markers passes, as measured for
   the (a) options.
   - `change-flow`: (a) a new paragraph after `:263` (simulated); (b) after `:299`; (c) after `:353`.
   - Relay: (a) after `:255` (simulated); (b) beside `:713`, as first-draft N6 had it.
   - `tw-flowmaster`: (a) the first paragraph under `### GCFPE binding` (simulated); (b) after `:317`.
2. **O2 — Provisioning.** Relay `:255` and `:713` return `SESSION_PROVISIONING_REQUIRED` "for
   Session Branch Flowmaster", which creates sessions. For GCFPE main-ecosystem stages, the override
   and rule 2 of the `D23` clarification say nothing creates a session. Options:
   - (a) leave both lines, and let the override govern GCFPE stages by its own scope (simulated);
   - (b) scope `:255` and `:713` to non-GCFPE exchanges;
   - (c) wording Nathan gives.
3. **O3 — The `CONTRACT_REQUIRED` entry for the override.** (a) The whole text, so any edit fails
   (simulated). (b) A distinctive substring, which tolerates rewording.
4. **O4 — `CONTRACT_FORBIDDEN` symmetry.** The relay gets "launched as a new session" (first-draft
   N6). `tw-flowmaster` gets "The Product Owner's PR-40 invocation supplies merge approval"
   (sweep:5). Options:
   - (a) as compiled (simulated);
   - (b) both skills take all four phrases. All four are absent from both edited files (measured).
5. **O5 — `change-flow:275` glue.** (a) "The policy for each planned PR work unit, run in two
   dedicated sessions, …" (simulated). (b) Other wording from C-SESSION.
6. **O6 — `change-flow:365` table cell.** (a) C-SESSION's second and third sentences (simulated).
   (b) A1-1's GCF-17 actor cell, "Dedicated PR session (PR-30 phase) and dedicated PR-35 session
   (PR-35 phase)".
7. **O7 — `change-flow:411`.** (a) Delete "manual-merge-assertion " (simulated). (b) Reword it to name
   both entry facts: the observed merge event, and the assertion on the fallback path.
8. **O8 — `change-flow:453`.** (a) Substitute A1-1's actor cell only (simulated). (b) Also append
   A1-1's PR-35 session cell.
9. **O9 — `change-flow:455`.** No source gives words for three things: the fallback-conditioned
   entry, the `MERGE_OBSERVED` path, and the new GCF-17.LINEAGE → GCF-14 transition. Options:
   - (a) the simulated text, whose words come from `{FALLBACK}`, C-DISPATCH and A1-7's
     `reject_replan` condition;
   - (b) wording Nathan gives.
10. **O10 — `change-flow:313`, `:323`, and C-LAT at `:453`–`:454`.** Child C7 keeps `:313` and `:323`
    verbatim, while steps 14 and 24 name them. This is §3 open question 12.
11. **O11 — The wording at `change-flow:557`.** A1-1 and §5 re-point the link and digest to the
    successor map. The sentence calls the map "immutable historical baseline evidence". Options:
    - (a) describe the successor as the current projection, and name the historical map as provenance
      at `:561`;
    - (b) keep the wording for the successor;
    - (c) wording Nathan gives.
12. **O12 — The alias and the default overlay path.** A1-6 re-points `:559` and says nothing else.
    - (a) Unlink the alias and drop it from `OPTIONAL_REFERENCES`. Re-point
      `validate_gcfpe_current.py:615`, `run_gcfpe_current_fixtures.py:104` and
      `validate_flowmaster.py:818`, so the default suite validates the v4 overlay (simulated).
    - (b) Keep the alias linked as historical provenance, and the validator defaults on it. The v3
      path then needs O14.

    Under either option, `flowmaster-validate/SKILL.md:157` and `:381` follow.
13. **O13 — `change-flow:563` after the re-point.** The shared `contract_id` no longer resolves to the
    current overlay. Options:
    - (a) add the alias to the superseded list, and state that the current overlay is the 091426.1
      contract, by its own `contract_id`;
    - (b) wording Nathan gives.
14. **O14 — The v3 path's installed-skill markers.** They are `validate_gcfpe_current.py:651` (`1.2.5`)
    and `:652` ("one dedicated PR-development session"), which §8a removes from the PR skill. Options:
    - (a) move `:651` to `1.3.0`, and REPLACE `:652` with "run in two dedicated sessions";
    - (b) retire those two markers;
    - (c) leave them, so an explicit alias run fails.
15. **O15 — Retired-phrase matching.** (a) Case-sensitive, like the loop above it (simulated).
    (b) Case-insensitive, like `CONTRACT_FORBIDDEN`. Both pass today (measured).
16. **O16 — Unrequested guards.** No source asks for these:
    - required literals for C-DISPATCH, C-PROCEED or C-HANDOFF in the `change-flow` validator;
    - `CONTRACT_REQUIRED` entries for C-SESSION or C-DISPATCH in the relay or `tw-flowmaster`.

    Options: (a) none (simulated); (b) add them, each with a deletion regression.
17. **O17 — The carve-out at relay `:259` and tw `:304`.** Step 14 gives "runtime handoffs may name
    versioned files; reusable prompt text stays versionless". But the line still forbids a static URL
    in "temporary … handoff prompt" text, and C-HANDOFF requires the direct Notion URL
    (pr-relay-graph:18). Options:
    - (a) append step 14's sentence only (simulated);
    - (b) also remove "/handoff" from the line's scope;
    - (c) wording Nathan gives.
18. **O18 — Handoff content at relay `:273` and `change-flow:277`.** Relay `:273` carries results "in
    the existing handoff". `change-flow:277` says the same, and no finding names it. Options:
    - (a) the relay line becomes "in the output artifact that the handoff names", and `:277` is
      unchanged (simulated);
    - (b) the same edit at both;
    - (c) wording Nathan gives.
19. **O19 — Relay `:279` and tw `:315`.**
    - Order of `{C-PLACE}` and `{C-HANDOFF}` at relay `:279`: simulated with C-PLACE first.
    - tw `:315`: (a) the whole line equals the relay's new `:279`, which also changes "an attached
      artifact" to "a referenced artifact" (simulated); (b) only the edited span, keeping tw's
      wording. A1-6's "byte-identical" describes `:304`, `:319` and `:321`, not `:315`.
20. **O20 — Relay `:283` and tw `:319`.**
    - `{C-SESSION}`: (a) prepended to the line (simulated); (b) as its own paragraph before it.
    - The "supplies merge approval" clause: (a) deleted (simulated); (b) reworded to "is not a merge
      approval or merge instruction", using `change-flow:353`'s words.
21. **O21 — Relay `:285` and tw `:321`.** (a) Verbatim (simulated). (b) Converge "same-session resume"
    on C-SESSION.
22. **O22 — Relay `:353` and `:372`, `CONTROL_PLANE`** (pr-relay-graph:17). Options:
    - (a) keep the enum, and state that `NOTION` means a destination-named maintenance surface. No
      words are given for this.
    - (b) add `REPOSITORY`. That changes `validate_relay_manifest.py:1094`–`:1118`, fixture
      `:1633`–`:1640`, `manifest-v2-examples.md:51` and `:118`, `behavioral-test-fixtures.md:20` and
      `validate_flowmaster.py:232`.
    - (c) leave unchanged (simulated).
23. **O23 — Relay `:624`, `NOTION_REFERENCE`.** This is §3 open question 13.
24. **O24 — tw `:311`.** sweep:5 gives the intent, not the words. (a) The simulated text. (b) Other
    wording.
25. **O25 — `flowmaster-validate/SKILL.md:294`.** (a) C-SESSION's second and third sentences
    (simulated). (b) The successor GCF-17 row's name.
26. **O26 — C-D22 per-site wording.** The sites are `flowmaster-validate/SKILL.md:60`,
    `validate_gcfpe_20260914.py:2657`–`:2659` and runner `:726`, and the question extends to the
    docstring at `:2288`–`:2291`. This is §3 open question 8.
27. **O27 — `validator_revision`'s new value** at its four sites. The amendment says it moves
    "alongside" 3.3.0 but gives no value. (a) 3.3.0 (simulated). (b) A distinct value.
28. **O28 — The header floor.** (a) 4, which is 7 minus the three deleted lines (fv-main:0;
    simulated). (b) Keep 7 and pad the fixture header (fv-rest:22).
29. **O29 — Fixture shape.**
    - (a) Four new scenario ids: HANDOFF-POS-03, HANDOFF-NEG-02, REPLAN-POS-01 and REPLAN-NEG-01. That
      gives 37 ids, a 20/17 split, two new attribution labels and 216 runner cases (simulated).
    - (b) Variants and runner cases only, keeping 33/18/15.

    No source sets the fact names, the expected labels or the attribution labels.
30. **O30 — Error-code names.** Simulated: `RECEIVER_CONTRACT:<receiver>`, from the v3 precedent;
    `PR40_REJECT_REPLAN_ROUTE`; and the positive rule under the existing `DIRECT_PR35_PR40_EDGE` and
    `GRAPH_DIRECT_PR40_EDGE`. The alternative is new names.
31. **O31 — The positive rule's condition test.** (a) Exact equality to the A1-7 strings
    (simulated). (b) A substring that names the observed merge (fv-main:11).
32. **O32 — The graph ⊆ contract prohibited-reference parity check** (fv-main:17, coverage:12). It is
    not in A1-2. (a) Omit it (simulated). (b) Add it as a new graph-parity code, with a regression.
33. **O33 — §4's `pr35_observed_merge_edge` record (§4 OQ-5) and `event_2.time`.** No validator check
    is compiled for either. (a) None (simulated). (b) Add literal checks once §4 and §6 fix the
    values.
34. **O34 — `change-flow:321`.** It says RS-40 resumes "in the same session/workspace/worktree/branch/open
    PR". That is the wording sweep:20 converges at `flowmaster-validate:393`, but no finding names
    `:321`. (a) Leave it (simulated). (b) Apply sweep:20's wording.

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
