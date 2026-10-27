## §P — Plan

**PLAN is complete, and its normal path passes a full dry run.** The detail is in [PLAN-20261027.md](evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md). Its tools, operations, guards, registry inputs, activation operations and dry-run receipts are under [plan/](evidence/20261027-gcfpe-backlog-open-items/plan/). EXECUTE lands the 36 items as one successor release, `GCFPE-20261027.1 / 102726.1 / 56`:
- 54 runtime successors, PE and the new member CL-05 (C-1); GCFPE-MGMT-10 is kept;
- four skill packages;
- `PROMOTION_CHECKPOINT_REQUIRED` with the packet, then, after Nathan's exact promotion approval, the register-last transaction (DN-1 D2).

The first dry run failed five gates. One bounded repair (C-15 to C-22, D26-F trigger 2) fixed them. The second, at `acc39b04` on reads after 2026-10-27T09:38:45Z, passes all eleven gates, N0 to N10. The PLAN review (D26-A) has not run yet.

Canon relied on:
- PF10-HDE-Build-Notes v13.9: its one addendum, 2.1 (S19), is silent here, and its numbering restart makes drained "2.x" citations ambiguous.
- PF04-Canon-HDE-Governance v2.8.8 §9.1.1 to §9.1.6 and §9.7.7.
- PF06-Canon-Change-Process-Guide v2.5.5 §0.1A, §1.0.6, §1.1.4, §3.5.1 and §3.5.2.
- PF19-Canon-Glow-QA-Guide v3.0.7 §0.4.3, §3.1.2, §3.1.3, §3.3, §3.4.3, §3.4.14, §3.5.7, §3.6 and §10.6.
- PF27-Canon-Plan-Templates v2.0.6: the sections in PLAN §1, with §3B.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7 §1.2 and §8.17.
- PF30.1-Canon-HDE-CRD-Records v0.9.2 §4.1.
- Decisions D8, D12 to D14, D17 and D20 to D30.

### Steps

Every step's verification can fail; a forbidden guard searches every page for surviving old text (template rule 4, D26-E). A failure takes D26-B's path: a failure record that reaches `main` in a record pull request, a read-only sweep, the freeze kept, and a return to Nathan. Resumption is only at D26-C's checkpoints: X0, X18's check on `main`, and X27. Not safe to send twice: X2, X5, X6, X8, X9, X20, X21 and X28 (PLAN §5).

| # | part | target | edit | authority | verification | rollback |
|---|---|---|---|---|---|---|
| X0 | all | skills, graph, PF10, register, 57 pages, 11 control pages | none: preflight; dry run rerun | D26-C | 9 digests; D29 token; PF10 v13.9 with only 2.1; selection 100926.1 / 55; every pin; D30 once on the branch | stop |
| X1 | 02, 19, 20, 21, 28 | v5.1.0 file; `skill-identity-and-freeze.md`; `reviewer-prompt-template.md`; `ecosystem-change-management.md` §3; PART-02 note after D30 | controls pull request; Nathan merges it before the packet | CD-9, CD-10, CD-11, C-11, C-12 | each `old` string at its count, each `new` once; repository guards; v5.0.0 unchanged; validator | revert before merge |
| X2 | 24 | 56 source pages | duplicate; move where needed; title | C-1; D23-G | parent, title, head, no child, source revision unchanged | move to archive |
| X3 | 24 | `execute/successor-pages-102726.1.json` | write the map once | W7-D8; D26-C | map checks: 56 members, 54 SUCCESSOR, 1 KEPT, 1 ADDED, PE | stop |
| X4 | body parts | 56 successors and GCFPE-MGMT-10 | none: fresh reads; `body_check.py plan` | D22 | `ok`; revisions at the map's pins | stop the page |
| X5 | 24 | PR-50 102726.1 | head and binding operations, one call | C-22 | every operation LANDED; head read back as planned | page history |
| X6 | 01, 03–14, 24, 26, 27 | the other 55 successors | one update_content each | §A.14 decisions; C-1 to C-22 | each call succeeds | page history |
| X7 | body parts | the same pages | none: `check` and `registry` | GUARD-001 | every operation LANDED; every guard passes; BIND, NAME and REL guards at 0 | page history |
| X8 | 17, 21 | Glow Operations Hub, register | 21 and 3 operations | DN-9; C-10 | `activation_render_102726.py check --phase part17`; Hub and register guards | page history |
| X9 | 24 | catalog (new), Flow Index, five hubs, register | candidate records | L-A13 / L-B2; D-W8-3, D-W8-5 | `check --phase candidate`; `control_check_102726.py --phase candidate` | page history |
| X10 | 24, 13 | regenerator, R1 successor | Q0 to Q2 | D23 successor; L-A14 | 100926.1 contract EQUAL; R1 47 rows at the recorded digests | discard scratch |
| X11 | 24, 08–10, 13 | candidate and production graphs | Q3, Q4 | C-11 | 56 · 240 · 56; route checks; flip-only difference | discard scratch |
| X12 | 24 | 102726.1 contracts | Q5 | W7-D5; C-7; C-19 | 56 ids; no `promoted_at`; semantic equality; PLAN pin | none |
| X13 | 24 and skill parts | 4 packages | Q6: 105 redlines, build, gates in two copies | D24; D28; W7-D2, W7-D3 | all LANDED; suite, fixtures, validators pass with only C-21's named findings | rebuild |
| X14 | 24 | 56 bodies | Q7, `x12_qualify_102726.py` | promotion predicate 1 | 56 validated, none unevaluated, `ok` | stop |
| X15 | 24 | `GCFPE-PCR-20261027.1` | Q8 | D13; GUARD-001 | validator 0; 56 rows; every regression reported | revert |
| X16 | 24 | the 4 packages | Q9, D24, two reviewers | D24; D26-A | both `SKILL_FIT_CONFIRMED` on the same digests | repair within cap |
| X17 | 24 | the release | Q10, post-flight, two reviewers | postflight-procedure | `PASS` or `PASS WITH WARNINGS`, no mandatory finding | stop |
| X18 | 24 | Flow Index; packet | C4, Q11; controls merge checked on `main` | DN-1 D2 | every packet value from a receipt; pins recorded | none |
| X19 | 25 | all | P0 | promotion approval | selection, pins, map, digests, v5.1.0 sha256 equal | stop |
| X20 | 25, 19 | entry (new), catalog, PE, Flow Index, five hubs, Alpha checklist | P1 bindings | D17 | `check`; `control_check_102726.py --phase activation --register-pending` | stop |
| X21 | 25, 19 | register | P2, last; procedure binding to v5.1.0 | D17; CD-9 | ten pages pass; selection names 102726.1 / 56 and v5.1.0 | stop |
| X22 | 25 | installed skills | P3: Nathan installs 4 | D24 | `freeze.py` digests equal the reviewed ones | reinstall |
| X23 | 25 | activated state | P4, `x18_validate_102726.py` | D17 | every flag; 56 bodies; every row passes | stop; no archival |
| X24 | 25 | 57 pages | P5, move to the archive | D17; D29 | all 57 under the archive, intact; `--phase archived` ok | move back |
| X25 | 25 | workspace | P6, sweep by literal; never a member body | authoritative-surfaces | a second search finds none | page history |
| X26 | 25 | this branch | R1 to R5: parts, registry, surfaces, D31, §E; promotion pull request | D17 | token reproduced; registry checks; validator | revert |
| X27 | 25 | `main` | R7 after Nathan's merge, detected by files | D26-C | token, registry, D31, digests on `main` | stop |
| X28 | all | backlog; record pull request | dispositions; `ECOSYSTEM_CHANGE_COMPLETE` | template rule 5 | backlog rows re-fetched | page history |

### Decisions applied

DN-1 to DN-12, CD-1 to CD-15 with Nathan's CD-6 and CD-9 conditions, and the opt-ins L-A12 / L-B1, L-A13 / L-B2 and L-A14 apply as recorded in §A.14. C-1 to C-22 apply as recorded in `plan/coordinator-decisions.md`. Among them:
- C-1, the cascade: every member citing a changed member's page gets a successor, so 54 plus PE plus CL-05.
- One successor map, written once.
- D30 is recorded now, the PART-02 note follows it, and the promotion entry is D31.
- A frozen PLAN file is pinned by the contract.
- The controls pull request is merged before the packet.
- One normalized text form for every check.
- C-16's judged lines.
- CL-05's parent comes from the map.
- One successor's write is read back before the batch.

PART-15 and PART-22 close `NOT_APPLICABLE` (DN-8 (c)). PART-16 and PART-18 are accepted risks (DN-7 (a), DN-10 (b)). PART-23 closes delivered (DN-11, in Nathan's words). PART-19's binding moves inside PART-25 (CD-9). R-P1 and R-P2 are prepared as excluded conditional sets (C-13).

### Open findings, accepted as risks

28, P-L1 to P-L28, each with its path, likelihood, consequence and reason in PLAN §10, together with those accepted at ANALYZE approval (§A.13, less the three opt-ins). They include:
- C-11's stale `candidate_member_rule`;
- C-19's carried parent ids;
- C-21's pre-existing suite findings;
- C-15's pre-existing rendering failure of the selected registry;
- the Hub's "all 55" line;
- C-16's judgement calls;
- stand-in-dependent digests;
- the Ops Hub's volatility;
- R-P1, R-P2 and the governance-audit lines of C-3, which are Nathan's.

Approving this plan accepts them (`DISP-001`).

### Product Owner actions

- Approve this plan in Nathan's own words, saying whether R-P1 and R-P2 are opted in.
- Merge the controls pull request before X18; X18 and P0 verify it on `main`.
- Approve promotion of the exact X18 packet snapshot.
- Install the four packages at X22, verified by `freeze.py` digest.
- Merge the promotion pull request; X27 verifies it from `main`.
- Merge the record pull request.

Each merge preserves the record and approves nothing (D21-C).

### Explicitly not in scope

- J-1 to J-14 and the C-14 backlog rows.
- The governance-audit lines (C-3); R-P1 and R-P2 unless opted in.
- QA-70's delta-mode retirement.
- The TW ecosystem and PE's general rules.
- typesafe-scoring and session-relay-flowmaster.
- The selected 100926.1 contract bytes.
- PF canon and A-10's canon inconsistencies.
- Alpha state.

### Disclosed deviations

- **Branch.** The branch is the harness's `claude/ecosystem-change-mgmt-drvb4v`, not `docs/20261027-modification-gcfpe-backlog-open-items`, as ANALYZE used the harness's branch.
- **Riders.** The four riders (ITEM-33 to ITEM-36) were added at approval, inside the frozen scope.
- **Cascade.** C-1 widens ITEM-31's measured surface to 54 runtime successors, PE and CL-05. No item is added.
- **PF10.** PF10 moved to v13.9 after ANALYZE's v13.8.9 baseline.
- **Merges.** The controls pull request adds a third merge to §A.8's count.
- **Re-price.** EXECUTE is re-priced at 18–30 h and 16–26M, replacing 24–40 h and 12–20M (PLAN §13).
