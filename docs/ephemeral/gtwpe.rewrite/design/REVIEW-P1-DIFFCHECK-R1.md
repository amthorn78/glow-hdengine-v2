3 distinct confirmed REQUIRED findings

The count fell from 8 to 3, so it halved. All three sit in text the repair added, which is the stop signal in D26-A rule 5. P1's review budget (one dry run and one diff check) is now spent, so this goes to Nathan.

## Required findings

### RQ-1 · R1 · PF27 can change in a run with no specification

- **Text.** §4.1.1 marks PF27 "Not touched" on the row *A document only* (line 239) and the row *PF10 only* (line 243). Line 246 says a run with (a) and (c) "touches neither PF27 nor a record".
  - S2 (line 301) builds candidates from "every eligible PF the source names by number or title" and "every eligible PF whose purpose-and-scope sections the manager finds the source bears on". It also adds "the PFs that B-CLASSIFY-PF10 maps from the PF10 set".
  - `targets-check` then tests only two things: that a source unit is cited, and "the eligibility guard for this prompt (§8.7)".
  - §8.7 (line 550) puts PF27 in the General class, which GTWPE-RUN-10 writes.
- **Evidence.** Nathan's instruction of 2026-09-25 (plan §1, line 36) reads: "PF27 and PF30 are updated only when a specification exists."
  - Plan §2.2 (line 63) also limits the specification rows: "PF27 changes only if the specification changes a template it owns." §4.1.1 (line 240) keeps "PF27 evaluated: `CHANGE` or `NO_CHANGE`" but drops that limit, and no other part of the design states it.
  - Reproduction: run *PF10 only* with the whole PF10 set. Addendum 2.14 says "PF27 and PF30 adopt the same terms on their next revision" (the design quotes it in §8.5). B-CLASSIFY-PF10 maps 2.14 to PF27, S2 adds PF27, `targets-check` passes it, and B-DRAFT drafts it.
  - A Path A document that names PF27 goes the same way.
- **Path, likelihood and consequence.** This is the normal path, on the rows *PF10 only* and *A document only*. Likelihood is low to medium, because 2.14 is live in PF10 v13.4.2.
  - PF27 is edited without a specification, contrary to Nathan's instruction and to §4.1.1.
  - G3 shows the edit, but nothing marks it as outside the rule. No guard enforces the rule, although §8.7 gives a GUARD-001 guard to the rulings of 2026-09-28.
- **Smallest correction.** In S2, PF27 becomes a candidate only when (b) is given, and then only for a template PF27 owns that the specification changes. `targets-check` refuses PF27 in a run without (b). Add one negative selftest case.
- **In repair text.** Yes. §4.1.1, the S2 candidate rule and `targets-check` are all new text. The gap itself predates the repair: the old S2 had no exclusion either.
- **Refutation tried.** "Evaluate PF27 when a specification exists" could be read as excluding PF27 otherwise. It does not: it governs the required `CHANGE` or `NO_CHANGE` finding, and the same cell admits "every eligible PF".

### RQ-2 · R1 · The pointer records from DR-3 reach neither S1's command nor S2's search

- **Text.** S1 (line 300) says a repository input "is recorded by path, blob SHA and unit index, with no copy of its bytes". An input from outside the repository "is read into the record with `gtwpe_read.py`".
  - S1's check requires "reader and version" and "a unit index covering the whole input or the stated selection".
  - S2 (line 301) finds "every eligible PF the source names by number or title (an exact search of the records)".
  - Per H2 (line 350), the `.json` record holds "units with stable anchors" and no text.
- **Evidence.** Before the repair, S1 said "Read each input into a source record with `gtwpe_read.py`". The dry run's §2 table accepted `gtwpe_read.py` as S1's command, marked "yes".
  - Now `gtwpe_read.py` serves outside inputs only. Path B's inputs are all repository inputs: the specification, PF10 and the addendum files. No named command builds their unit index or checks that it covers the whole input (D26-A rule 1). Git can supply a byte count and a hash, but not a unit index.
  - No later check covers this. `targets-check` confirms only that a cited unit exists, and H4 checks set equality with the units assigned.
  - S2's "exact search of the records" cannot find a PF named inside a repository input, because that input's record holds none of its text.
- **Path, likelihood and consequence.** This is the normal path: every Path B run, and Path A with a repository document. The gap is certain as written.
  - Coverage arithmetic (`execution-and-delegation-model.md` §2) then depends on a unit index the manager builds by hand.
  - A unit missing from that index is never classified or drafted, and no check notices. The run is partial without anyone being told.
- **Smallest correction.** `gtwpe_read.py` records every input. For a repository input it writes only the `.json` pointer, with a unit index computed from the blob, and its exit status is S1's check. S2's exact search runs over each recorded source at its blob, or over its `.md`. Add one selftest case for a repository input.
- **In repair text.** Yes.
- **Refutation tried.** §9.2 says "The source record names the reader, its version", which could mean `gtwpe_read.py` records every input. But S1's new sentence assigns it to outside inputs only, and the P2 list does not widen its scope.

### RQ-3 · R3 · The live read that DR-4's repair adds is kept out of the record, but still falls under D22

- **Text.** S1 (line 300) says a prompt body "is recorded by identity only (page ID, title, `page_last_edited_at`), never its body (`D22`; plan §2.3); its drafter reads it live".
  - §7.4 (lines 415–417) says `capture` "reads the harness's own subagent transcripts" and "finds the one assistant message holding both markers".
  - §15 P1-6 (line 830) says those transcripts "also hold what was fetched".
  - None of these has a field for recording a transient read: RUN.md's frontmatter (§5.2, line 326), the H4 return and the surfaces §7.5's post-check watches.
- **Evidence.** D22 allows a transient file only while all five of its conditions hold. Three matter here:
  - Condition 2: "never a source for later work".
  - Condition 4, as refined: "left to the harness's teardown and never read again".
  - Condition 5: "the session says in its report that it happened".

  The kickoff's workaround D1 says "delete transient read files when the read is done, and report them".
  - A drafter or classifier that fetches the body leaves it in its own transcript. A body over about 30 KB also leaves a tool-results file; D22 counts thirteen GCFPE bodies that size.
  - `capture` then parses that transcript to extract the return, and nothing in the run reports the read.
  - P1-6 is the design's own record of the same disclosure being missed at P0.
- **Path, likelihood and consequence.** This is the normal path for a Path A run whose input is a Notion prompt body, unless §14 D-6's reader agents are installed; with them the input is `UNSUPPORTED_INPUT`. It is rare per run, but certain whenever such an input is used.
  - The result is an unreported on-disk copy of a prompt body, which the run then reads again.
  - That is a silent breach of D22, outside the repository.
- **Smallest correction.** Either of two:
  - (i) A prompt-body input is `UNSUPPORTED_INPUT notion-prompt-body` in every configuration, as D-6 already makes it. This narrows plan §2.3, so it is Nathan's decision.
  - (ii) RUN.md and REPORT.md name each live prompt-body read and the harness file it left. `capture` then takes that drafter's return from the Agent result in the manager's own transcript, not from the drafter's transcript.
- **In repair text.** Yes: the live-read sentence is new. The `capture` mechanism and the RUN.md fields it collides with are unchanged.
- **Refutation tried.** The RUN-10 body will cite D22 (§4 *References*), so a manager might report the read without being told. But the manager cannot see a drafter's read unless the drafter reports it, H4 has no field for it, and the design builds in `capture`'s re-read.

## Listed findings

| # | Finding | Path | Likelihood | Consequence | In repair text |
|---|---|---|---|---|---|
| 1 | `approval-check` confirms the reply names things, not that it approves them. A vague reply fails and returns to Nathan under H6. "The package version whose file list is fixed" has no stated test, although a package can hold unsure targets, `NEXT_REVISION` blocks and V9/V10 overrides that need his words. Whether a reply naming only the version "explicitly directs" each file (`AGENTS.md` line 16) rests on §10.1 and D-2 | normal | low | A decline, or "approve v2 except PF12", that names the run and the version passes the check. Only the manager's reading and G4 stop it: the result is an unwanted canon PR, not a merged edit | yes |
| 2 | The third clause of `verify-check`, "its hunks match `apply/<key>.json`", has no data to compare. H8 returns only unmapped hunks. `apply/<key>.json` holds SHAs, sha256 values and byte counts (§8.3, H7); the diff itself is in `apply/<key>.diff` (§5.2) | normal | certain as written | P2 must choose the data, or the clause passes with nothing to compare and S7 rests on the verifier's own report. S6's byte check still holds | yes |
| 3 | `targets-check` has no failure route, because S2's *On failure* cell covers only unsure targets. S2 adds the PFs B-CLASSIFY-PF10 maps without the "eligible" filter, so a Reference file, or a PF20 or PF30 edit that is not a record, meets a refusal with no stated outcome. G3 lists no such unit (PF03 §7) | normal, Path B | medium | The manager improvises: probably a loud stop, possibly a unit dropped without report | yes |
| 4 | §13.2 gives each new check one positive and one negative case. That cannot show each clause failing on its own (CHK-001, D11): `approval-check` has two alternatives, `verify-check` three clauses, `pr-check` and `targets-check` two each. `pr-check` must also read S6's `git mv` either as a rename or as a delete and an add | normal | medium | A clause that never fires still passes V2 | yes |
| 5 | S1's prompt-body exception is missing from S1's own *Output* and *Check* columns and from H2. There, every outside input gets a `.md`, and every record needs a byte count and "a unit index covering the whole input". No test says which Notion page is a prompt body | normal; failure if a page is misjudged | low | An identity-only record fails S1 loudly, or the manager indexes the live body. A prompt body not recognised as one is copied to `.md` and pushed at S1's checkpoint | yes |
| 6 | No rule stops a captured return, the G3 package or REPORT.md from quoting a prompt-body unit. The formats cite source units by anchor (PF03 §15.2), but `capture` commits the return exactly as written | normal | low | Part of a prompt body lands on the records branch | no; it arises from DR-4's repair |
| 7 | The brief (§7.2 item 3) and H3 give source units "by path and anchor", without the recorded blob SHA. With no copy in the run directory, a drafter reads whatever the working tree holds | normal | low | The drafter works from a different version of the source than S1 recorded, and no check notices | yes, as a consequence of DR-3 |
| 8 | (b) no longer brings the `PF10_BUILD_NOTES_ADDENDUM` files a specification names; they arrive only through (c) (§9.5 Q2), so (b) alone ignores them without notice. No row covers (a) plus (b) without PF10 | normal | medium | The Path B run is incomplete, but nothing wrong is written | yes |
| 9 | §1.1 claims more than the design delivers in three places. (1) The PF03 §6 row points to §7.2 item 4, which cites PF03 §3, §7, §8 and §15.2 but not §6; B-DRAFT reading PF03 in full is the real home. (2) The PF06 §3.5.2.8 row holds only for Path B: B-CLASSIFY-PF10 records QA state, but a Path A input that is an Epic's doc delta gets no QA check. (3) The row names `UNKNOWN` as a return, and no brief returns it | normal | certain as written | P3 follows wrong pointers, and drainage before QA could reach G3 with no QA state shown | yes |
| 10 | Contract tables: §4.2 and §4.3 still lack *Approval effects*, a PE field that §4.1 carries (the dry run's own trace lists it). §4.4's *Writes* row (Notion, `docs/ephemeral/modifications/`, `docs/prompt_ecosystem_management/gtwpe/`) contradicts §4's shared *Boundaries*, which bind "every GTWPE prompt". Otherwise §4.4 agrees with §11 on writes, exclusions and results | normal | certain as written | P3 would write a self-contradictory MGMT-10 body, likely caught at G2. The missing field has no effect at run time | yes; the §4.4 conflict predates the repair |
| 11 | R2's check names no command, and neither does S0's. The dry run supplied S0's command (`git cat-file -e`) itself and left R2 out of its table, so C3's "every stage check" is not literally true | normal, record prompts | low | Nonduplication and the ID check rest on the manager's search and on the drafter | no; Review Drift |
| 12 | No prompt can make an edit to PF20 or PF30.x that is not a record. Examples are PF10 2.14's terms for PF30.1 §7 and T6's first candidate. RUN-10's guard refuses them, and §4.2 and §4.3 limit their purposes to records | normal (T6) | certain for that candidate | A loud `TARGET_INELIGIBLE` at P5, or duties left with no route | no |
| 13 | §17 still reads `reviews: []` after the dry run, although DRY-RUN-P1.md says §17 "receives each round's ledger row after the round" | normal | certain | G1 would approve a ledger that omits its own dry run | no |

## Prior required findings and trend

| Prior | Disposition |
|---|---|
| DR-1 | Fixed, with a new defect. Input (c) makes PF10 explicit, and §4.1.1 maps all six plan rows plus (a) with (c). But the PF27 gate is not enforced and half of it is dropped (RQ-1); see also listed #8 |
| DR-2 | Fixed, with a new defect. S2, S5, S7 and S8 now name `targets-check`, `approval-check`, `verify-check` and `pr-check`, and §12.1 and §13.2 carry all nine subcommands. But S1 lost its command for repository inputs (RQ-2); see also listed #2 and #11 |
| DR-3 | Fixed, with a new defect. No repository input is copied (S1, H2, §5.2). But the pointer record reaches neither S1's command nor S2's search (RQ-2); see also listed #7 |
| DR-4 | Fixed, with a new defect. The record now keeps identity only. But nothing reports the drafter's live read, and `capture` reads it again (RQ-3); see also listed #5 and #6 |
| DR-5 | Fixed, with a new defect. S2 states the method, but its exact search misses repository inputs (RQ-2) and it admits PF27 without a specification (RQ-1) |
| DR-6 | Fixed. No "PF27 §1" remains, and six citations name *Review guardrails*. That H2 is unique in PF27 on `main` (line 988) and holds every cited rule: `ASK OK?` at line 1019, rendered escapes at 1128–1178, materiality at 1190, redline bundles at 1312 and review stability at 1329. The sub-headings the dry run named are not cited, but the H2 is enough |
| DR-7 | Fixed, except that §4.2 and §4.3 have no *Approval effects* row, and §4.4 contradicts §4's *Boundaries* (listed #10) |
| DR-8 | Fixed. §1.1 gives a home for every rule it lists; three of its claims go beyond the design (listed #9) |

**Trend.** Required findings went from 8 to 3, which halves the count. All three required findings, and 9 of the 13 listed ones, sit in text the repair added.

**Claims.**

| Claim | Holds? |
|---|---|
| C1 | Partly. All eight DRs are addressed, and the only other change is a new `revised:` front-matter line. DR-1 to DR-5 carry new defects |
| C2 | No: see RQ-1 |
| C3 | Partly: see RQ-2 and listed #11 |
| C4 | Yes for the run directory and the record. No for D22 outside the repository (RQ-3); see also listed #5 and #6 |
| C5 | Yes, but see RQ-2 for its search |
| C6 | Yes |
| C7 | Partly: see listed #9 and #10 |
| C8 | Yes. No row lets GTWPE-RUN-10 list, draft or apply PF10, PF20 or PF30.x: `targets-check`, V2, `apply` and `pr-check` refuse them, and each due record is named for its dedicated prompt. RQ-1 concerns the instruction in plan §1, not these three rulings |

## Decision for Nathan

I need your choice on RQ-1 to RQ-3. The design package goes to G1. Its run prompts are drafted from these contracts at P3, and its tools are built from them at P2.

| Option | Cost |
|---|---|
| A. Accept RQ-1 to RQ-3 as listed risks at G1, and fix them in P2 and P3 | No round now. Until they are fixed, a run can edit PF27 without a specification, repository-input coverage depends on an index built by hand, and a prompt-body input breaches D22 |
| B. Repair RQ-1 to RQ-3 once, and prove each fix with its P2 selftest case rather than another review | One repair round, priced under D26-D. Each fix is one or two sentences in §5.1 plus one selftest case. A second diff check would need your `review_cap` override |

**Recommendation: B, using option (i) for RQ-3,** which makes a prompt-body input unsupported, as D-6 already does. The three fixes are mechanical, and two of them guard your own instruction and D22. A failing selftest case is a sharper check than another reading. Option (i) narrows plan §2.3, so it needs your word. The 13 listed findings stay listed unless you opt in.

## Canon relied on

**Canon source.** Canon is `docs/pfcanon/` on `main`, read at `origin/main` 53449c9 in this checkout. I did not re-fetch it, because a fetch changes state. `docs/pfcanon/`, `AGENTS.md` and `docs/prompt_ecosystem_management/` are byte-identical from 8eb4ce0 (the design's `canon_read_at`) to 53449c9, and commit 42badb7 changes none of them. `AGENTS.md` has sha256 `2a28ac5c…81758f1`, as the design states.

**Canon.**
- `AGENTS.md`: the canon-first rule; PF canon is read-only; the truncation guardrail; evidence attribution.
- PF03 — Technical Writing Best Practices: §3, §4, §5, §6, §7 and §8; from §11, *Editorial validation* and *State language*; from §12, *Output contract* and *Claim language*; §15.1 and §15.2.
- PF06 — Change Process Guide: §3.5.2.8, the part headed *Post-QA documentation drainage ordering (normative)*.
- PF10 — HDE Build Notes: the Front Matter; *Precedence, versioning, and scope* §1 to §9; addendum 2.14, *Specification format authority*. For 2.8, 2.29, 2.30 and 2.31 I read the headings only.
- PF27 — Plan Templates: the heading map; under *Review guardrails*, the sections *Hard blockers for plan approval/execution* (the `ASK OK?` and rendered-escape rules), *Materiality-based blocker discipline for planning and review artifacts*, *Redline bundle construction discipline*, and *Review stability and no-moving-target discipline*.
- The file list of `docs/pfcanon/` on `main`, used to check the classes in §8.7.

**In-flight and governing documents read.**
- `design/GTWPE-DESIGN-v1.0.md` at 42badb7, whole: 860 lines, 76,495 B, sha256 `63a60d45…e834d812`. Also the repair diff from e70b8ed: 73 lines added, 19 removed.
- `design/DRY-RUN-P1.md` at e70b8ed, whole: 101 lines, 9,945 B. It is unchanged at 42badb7.
- `design/P1-SOURCE-NOTES.md` at 42badb7, whole: 160 lines, 34,806 B.
- `GTWPE-IMPLEMENTATION-PLAN-v1.1.md` at 42badb7, whole.
- `ERRORS.md` at 42badb7, whole.
- `CHECKPOINT.md` at 42badb7: §1, §2, §4.1 to §4.3, and §5 to §9, including §8's rulings verbatim.
- `gcfpe.decision-record.md`: D20 to D26, in full.
- `modification-template.md`: rules 1 to 8 and the shape of the `reviews` ledger.
- `ecosystem-change-management.md`, whole.
- `execution-and-delegation-model.md`: §2 to §8.
- Not read: `reviewer-prompt-template.md`, whose fixed text this brief carries.

**Writes.** None: every git command I ran was read-only. The harness saved one oversized output of mine to its own tool-results store. It holds the text of `P1-SOURCE-NOTES.md`, a repository record with no prompt body. I read it once, and it is left to teardown.

DECISION NEEDED
