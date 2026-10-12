4 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-DIFF — check of the PLAN repair's diff, MODIFICATION-20261011-gcfpe-mb008-to-promotion

Reviewer: REVIEWER-PLAN-DIFF-C, fresh context. I did not author the plan and was not reviewer A or B. Brief: `BRIEF-PLAN-DIFF.md` at `c1f0fa5`, which binds §3 (R1–R4) and §5 (cap and exit) of `BRIEF-PLAN-1-A.md` unchanged. Diff checked: `1b742bb8..4eb8872` on the record, `PLAN-20261011.md` and `plan/`, read from those commits with `git archive`, not from the working tree. Canon: `main` `9312add2`. Date: 2026-10-12 (UTC).

**Answer.** Seven of the eight round-1 findings are fixed. P-B1 is only partly fixed. Four required defects are open, and three of them sit in text the repair added.

| # | Class | Defect | In repair text |
|---|---|---|---|
| P-B1-R | R2 | The Flow Index keeps two release-bound statements that no delta rule restates and no check can see. One is the actor-map MGMT-10 row that reviewer B named. | the gap is in the new delta; the sentences are old |
| DIFF-1 | R1 (R2 on the other branch) | The delta's SUBST rule and `control_check.py` disagree on the register's *Release rule* line. Rendered correctly, the line fails X16's check after the register is written. Rendered the other way, the rule becomes false. | yes |
| DIFF-2 | R2 | NEW_CURRENT copies Current-selection paragraphs that the delta does not restate into the 100926.1 section: the 091426.1 graph proof token as the machine-contract binding, an Alpha-state paragraph, and a claim of archival. | yes |
| DIFF-3 | R2 | The assembled 100926.1 registry keeps a header note that cites the key the same build deletes and describes byte counts no row has. | yes |

**Trend.** The count fell from 8 to 4, exactly half. Three of the four sit in repaired text, so D26-A rule 5's second stop condition holds. This was the one diff check D26-A allows, so the plan now returns to Nathan with these findings open.

## The eight round-1 findings

| Finding | Disposition | Evidence (my reruns) |
|---|---|---|
| R-A1 / P-B3 | **Fixed** | MG-PR35, MG-PE-1 and MG-PE-2 each resolve once and apply on fresh reads of PR-35 and PE, at their pins. G-MGMT-1 matched 1 sentence on PR-35, 3 on PE and 1 on the testing page before the edits, and 0 after. One residual PE sentence is L-7. |
| R-A2 | **Fixed, with a new defect (DIFF-3)** | The row is now complete. Dropping the two D25 assertions is right under D25-B, because the successor body makes no read-only or does-not-change-the-repository claim. The candidate build is 535,955 B and reads back equal; the validator reports 0 errors and no derivation drift. On fresh reads with the edits applied in memory, the MGMT-10 and PR-35 rows pass, and all 34 injected regressions are reported. The selected stage checks, and `compare` finds differences only at the five specified paths. |
| R-A3 | **Fixed** | On the fresh read, M-HEAD's span holds exactly 15 line breaks. After the edits: one `Prompt ID` line (G-MGMT-2); the title line (G-MGMT-5); no page state (G-MGMT-3); the invocation and approval sentences adjacent (G-MGMT-4); the procedure once (G-TS-7). |
| P-B1 | **Partly fixed** | Fixed: every literal-bearing line has a rule, and a check that can fail now exists. Not fixed: literal-free statements outside the delta (P-B1-R). New defects in the delta's own rules: DIFF-1 and DIFF-2. |
| P-B2 | **Fixed** | Both 100926.1 contracts (634,423 B `215663f2…`; 631,061 B `769f2a11…`) carry no `promoted_at`. The shipped 091426.1 contract still regenerates EQUAL on both bundled copies. |
| P-B4 | **Fixed** | X22 starts from `main` and detects the merge by files, never by commit subjects. It rebuilds the parts, reruns the registry check and the digest comparison, and only then returns `ECOSYSTEM_CHANGE_COMPLETE`. This fits D26-C and the MGMT-10 body's EXECUTE paragraph. |
| P-B5 | **Fixed** | X2 is now a read-only rehearsal. M-HEAD and M-TS land at X5 with the other operations, the guards check them at X6, and the profile checks them at X12. Under the 100926.1 profile, the testing body with both edits in memory has 0 body errors. |
| P-B6 | **Fixed** | `flip` writes the selected prologue. The production build's header reads `selection_status: SELECTED_PRODUCTION`, with stamped `complete_source_bytes: 593569` and `complete_source_sha256: 8391ad84…`. The two new self-test rows pass. |

## Required findings

### P-B1-R — R2: release-bound statements on the Flow Index that carry no retired literal are left unstated

- **Exact text.** Flow Index, read as of 2026-10-11T20:10:23.284Z:
  - *Current actor, artifact, lifecycle, repair, and evidence map*, row `MGR-10`, `UTIL-10`, `GCFPE-MGMT-10`: "governed ecosystem repair result … GCFPE maintenance does not execute product work or Alpha; its final PR04 handoff remains Nathan-controlled."
  - *Direct successor control bindings*, opening paragraph: "**These bindings are operative.** The stable release register selected the complete successor on 2026-09-21 and every binding below was read back after activation."
- **Evidence.**
  - For the Flow Index, `activation-delta-100926.1.json` names only these sections: frontmatter, Activation contract, Direct successor control bindings ("every row SUBST"), Promotion evidence, Selected topology, Native flow changes and Alpha feedback candidate. It does not name the actor map. For the bindings section it covers the rows, not the opening paragraph.
  - Neither sentence holds a value `control_check.py` treats as retired. My run reports 134 Flow Index findings, none in either place.
  - Reviewer B's P-B1 correction named "the MGMT-10 row of the actor map".
  - Under DN-C A the successor emits no handoff, and MG-PE-2 makes PE say "GCFPE-MGMT-10 prepares no Alpha invocation".
  - PF04 §9.1.6 requires the Living Prompt Flow Map, which records "substantive inputs/outputs", to be updated when a prompt is "replaced by an immutable successor".
- **Path:** normal. **Likelihood:** certain.
- **Consequence:**
  - After promotion, the operative navigation page says the selected manager has a final PR04 handoff, and it dates the 100926.1 bindings to 2026-09-21.
  - Neither sentence is in the rendered delta the post-flight reviews, and X20's literal sweep cannot find them.
  - Same class, lower stakes: L-8.
- **Smallest correction:** add both to X15(c) in the delta:
  - the actor-map MGMT-10 row, restated for the three-mode body (`GCFPE_MODIFICATION_RECORD`, no handoff);
  - the opening paragraph, dated `@ACTIVATION_DATE`.
- **In text the repair added:** the omission is in the new delta, which claims to state "every release-bound change". The sentences themselves predate the repair.

### DIFF-1 — R1, R2 on the other branch: the register's *Release rule* line cannot be rendered both true and passing

- **Exact text.**
  - Delta, X16, *Current explicit membership — 091426.1*: "NEW_CURRENT: … and the Release rule line with SUBST". SUBST: "091426.1 → 100926.1 where they name the selected release".
  - The register line, read as of 2026-10-09T20:19:11.175Z: "It applies from the release after 091426.1; 091426.1's bodies were edited in place by `MODIFICATION-20260923-alpha-feedback-open-entries` (`D23-G`). … all 55 are `091426.1`, and all 55 bodies were revised in place on 2026-09-23".
- **Evidence.**
  - Once 100926.1 is selected, only "all 55 are `091426.1`" names the selected release. The other two mentions state historical facts.
  - I built the new section from the delta's catalog sentence plus that line, with SUBST applied only to the selected-release mention, and ran `control_check.findings` on it. It reports one finding: literal `091426.1` in *Current explicit membership — 100926.1*, with no predecessor marker in the 100 characters before it.
  - Substituting all three mentions passes the check, but then the register says the rule applies from the release after 100926.1, and that 100926.1's bodies were edited in place on 2026-09-23.
  - N10 tests only that each flagged section is named in the delta, not that the delta's treatment clears it. The dry run therefore could not show this.
- **Path:** normal, X16. **Likelihood:** certain that one branch or the other occurs.
- **Consequence:**
  - **Correct rendering:** X16's check fails after the register write. The run stops with the register selecting 100926.1 before X17's installs, X18's validation and X19's archival, and the state is left to Nathan.
  - **Full substitution:** the register's current membership rule becomes false, and no check catches it.
- **Smallest correction:**
  - State the line's exact 100926.1 text in the delta, with the historical clause marked, for example "it applied from the release after the predecessor 091426.1, whose bodies were edited in place …", and drop "all 55 bodies were revised in place on 2026-09-23".
  - Have N10 render the delta onto the dry-run reads and run the check on the result.
- **In text the repair added:** yes.

### DIFF-2 — R2: NEW_CURRENT copies Current-selection text the delta does not restate into the 100926.1 section

- **Exact text.**
  - NEW_CURRENT: "holding the old section's text with SUBST applied and any further change named in its row".
  - The X16 *Current selection* row names the heading, the selected line, a binding table (catalog, Flow Index, MGMT-10, PE, register entry, lane hubs) and the promotion evidence.
  - The rule therefore carries these unnamed passages:
    - the machine-contract row: "proof token `55 nodes · 229 edges · 55 state_routes · 575074 bytes · ae2bd159…` (after `D23`)";
    - "**Alpha — resumed 2026-09-21, separately from this promotion.** … the refactor it waited on **is** this release. Alpha was then `ALPHA_RESUMED`, with `HDE-EPIC040-PR04`'s `PR-10` stage `APPROVED`.";
    - "**Transaction order** … production validation was rerun against the activated state; the predecessor was archived intact only after that."
- **Evidence.**
  - None of the three holds a retired literal. My run flags 10 lines in that section, and these three are not among them.
  - SUBST changes nothing in them.
  - The Flow Index row of the same delta does replace its token ("the proof token → @PRODUCTION_TOKEN"). The register row does not.
  - `authoritative-surfaces.md` (D18 successor, 2026-09-23): "No Notion page holds or restates the Alpha state now." The current Alpha record the Flow Index points to is `ALPHA_STOPPED_FAILED_AT_QA`.
  - X16 writes all three at the register step, before X17–X19 have happened.
- **Path:** normal, from the X14 rendering to X16. **Likelihood:** likely; the rule carries the passages unless the renderer departs from it.
- **Consequence:**
  - The sole selection authority binds the 100926.1 selection to the 091426.1 graph's proof token. That contradicts `authoritative-surfaces.md` after X21.
  - It restates Alpha state as tied to 100926.1.
  - On a stop at X17–X19, it claims validation and archival that never happened.
  - No check fires. Only a reader of the rendered packet could catch it.
- **Smallest correction:** give the X16 *Current selection* row the new section's complete text:
  - the machine-contract row with `@PRODUCTION_TOKEN`;
  - no Alpha paragraph, only a pointer to the Flow Index's Alpha section;
  - the transaction-order sentence left to the register entry (f), which X19 completes.
- **In text the repair added:** yes.

### DIFF-3 — R2: the assembled registry cites the header key that its own build deletes

- **Exact text.**
  - `registry-header-100926.1.json` deletes `body_extraction_convention`. It also says: "Row 2, COMPLETE_PROMPT_FETCH_MANIFEST, is historical lineage and is carried unchanged."
  - In my builds of both stages, that row's note reads: "the evidence_contract byte count and SHA-256 on each row below identified the bodies before `D23` and no longer do (see body_extraction_convention.body_identity_disposition)".
- **Evidence.**
  - The same header file states: "No 100926.1 row carries a byte count or an extraction line."
  - The cited key is absent from the assembled file.
  - `check` returns `ok`, because `header_values_ok` covers only the `set` paths.
- **Path:** normal, X11 and X21. **Likelihood:** certain.
- **Consequence:** low. The selected registry on `main` describes row data it does not hold and cites a key that does not exist. Nothing reports it.
- **Smallest correction:** delete row 2 together with the convention, or rewrite its note for 100926.1. Then have `check` refuse any header string that names a deleted key.
- **In text the repair added:** yes.

## LISTED

Each line gives the path, likelihood and consequence. All are in text the repair added unless marked "pre-existing".

- **L-1 (`control_check.py`, a concrete case of P-L9).** On today's register, *Current GCFPE procedure and operator access* says "[PE Metaprompt 091426.1](…3db4590a05eb8174be35d9e35acb3f77) governs GCFPE authoring", and the check does not flag it. The preceding sentence about v4.0.0 says "superseded … historical", which falls inside the 100-character window. The delta names this change, so only the backstop is weaker. Normal; certain; low.
- **L-2 (claim).** PLAN §1 and §4 say every section N10 flags is "named in the activation delta". That is true, but N10 does not test that the named treatment clears the finding (DIFF-1). Wording.
- **L-3 (claim).** The PLAN's opening says "each assertion was shown to fire". `--inject` fires each required assertion and two release-wide forbidden ones per row; PART-07's table says this precisely. Wording.
- **L-4 (X15(c)).** At X15 the Flow Index's new activation paragraph says "Register-last promotion and complete binding readback succeeded; the predecessor … archived intact", before X16–X19 have run. A stop at any of those steps leaves it false, and DIFF-1 makes a stop at X16 likely. Failure path; loud stop.
- **L-5 (X18).** `registry_assemble.py assertions` applies the plan's operations in memory before it evaluates. An operation that came undone after X6 would be supplied in memory and pass. X18's text also omits `--page` and `--shared`; without them, MGMT-10 is evaluated on the testing page if a read of that page is still in the window. X12's profile reads the real bytes. Failure path; low.
- **L-6 (`mgmt10-registry-row.json`).** The marker `@MGMT10_LAST_EDITED` is described as "X2's fresh read after M-HEAD and M-TS". X2 is now read-only and the edits land at X5. The build overwrites the marker from X6's report, so nothing breaks. Wording.
- **L-7 (MG-PE-2).** PE's next sentence keeps "… and approves/invokes the final Alpha-resumption handoff", which names a handoff no GCFPE prompt now prepares. Pre-existing: the same section's YAML block still lists `HDE-EPIC040-PR04` as the next intended unit. Normal; certain; low.
- **L-8 (Flow Index and register rows, same class as P-B1-R).** All of these sit inside named sections, where the rendered packet shows them:
  - the *Skill fit and interoperability* and *Corrected raw-source manifest* bindings keep the 20260914.1 records;
  - *Frozen candidate graph* keeps "(after D23; 227 edges when frozen at promotion)" beside the new token;
  - the carried membership text keeps "verified across 280 graph rows … (229 edges)".

  Normal; likely; low.
- **L-9 (§2, §8).** The writes to the candidate inventory page (its status paragraph and MGMT-10 row) are authorized, but no X step performs or verifies them. X20's literal sweep would find the page's "091426.1". Low.
- **L-10 (F02 wording, pre-existing).** Two texts are not restated for F02, under which Kronos may execute QA when the Product Owner chooses: the QA hub's *Native purpose* ("execute bounded QA tasks through the authorized operator") and the Flow Index actor map's QA row. "Authorized operator" can be read to cover the change. Low.
- **L-11 (X22).** Two gaps:
  - X22 returns `ECOSYSTEM_CHANGE_COMPLETE` with its record pull request still open, and nothing verifies that merge.
  - After the squash merge, restarting the harness branch from `main` needs a reset and a force-push, which the plan does not state.

  Low.
- **L-12 (`control_check.py` historical rule).** Every H2 not beginning "Current" under the register's H1 *Historical register profile* counts as historical. That includes *Mandatory PR and PF-document authority boundaries*, which holds a "Current GCFPE PF10 reference boundary" paragraph. That paragraph has no retired literal today. Latent.

## Checks run

Everything ran in scratch, outside the repository, from copies of the installed skills, with `PYTHONDONTWRITEBYTECODE=1`. The fetch cutoff was `2026-10-12T01:00:40.000Z`.

| Check | Result |
|---|---|
| `dry_run.py`, all gates | **N0:** 7 of 7 digests. **N1:** 20 guards, 58 fixture rows, 20 of 20 resolver cases. **N4:** 14 of 14 self-test cases; parent 237 edges `ff296b1e…`, candidate 235 `df3b57a5…`, production 235 `8391ad84…`, all PASS. **N5:** the patch applies; shipped contract EQUAL; unfilled marker refused; contract bytes and digests equal the receipt. **N6:** 25 substitutions; only the two errors pending by design. **N8:** 46 of 46 redlines; second apply refused; fixture suite passes. **N10:** 16 of 16 self-test cases; 9 pages, 306 findings, 37 sections, none outside the delta. These all match `dry-run.json`. N2, N3, N7 and N9's `assertions` ran only on the three bodies I fetched. |
| `body_check.py plan` on MGMT-10 (testing page), PR-35 and PE | Revisions equal their pins. 12 of 12 operations apply once. Batches are safe. 22 of 22 guard rows pass afterwards, against 5 before. The landing check would pass. |
| `registry_assemble.py` build, check, assertions with `--inject`, compare | As in the R-A2 row above. On the MGMT-10 and PR-35 rows: 92 assertions, 34 injected regressions reported, 0 missed. The 100926.1 profile reports 0 body errors on the MGMT-10 and PR-35 bodies after the edits. |
| `control_check.py check --report-lines` on the nine control pages | Gave the per-section findings used above; excerpts went to the terminal only. |
| DIFF-1 simulation | `control_check.findings` run on a synthetic section built from the delta's text and the register's Release rule line. |

**Not run:**
- N2, N3, N7 and N9 on the other 53 candidate bodies, and G-MGMT-1's broad match on them. For those I rely on the receipt.
- The Notion writes, the duplicate, and EXECUTE's rendering of the delta (simulated for one line only).
- X12 on the successor's real URL, D24, the post-flight, and the promotion transaction.

## Reads and D22

Notion was read only, one fresh fetch per page:
- **Control pages:** the register, the Flow Index, the five hubs and the Alpha checklist.
- **Prompt bodies:** PE Metaprompt 100926.1, the MGMT-10 testing body and PR-35 100926.1.

The harness saved two results to this session's `tool-results` directory: the register (a control page) and PE (a prompt body).
- I read PE only through the plan's own readers and one count-and-sentence scan.
- I extracted the register's text to scratch to read its sections.
- I deleted both harness files after use.

Everything else returned inline and stays in the session transcript. No body was copied, hashed or byte-compared. This record quotes only cited sentences. My scratch directory held repository copies, skill copies and count-only outputs, and I deleted it at the end.

**Canon relied on:**
- `AGENTS.md`.
- PF04-Canon-HDE-Governance v2.8.7, §9.1.6, read on `main` `9312add2`.
- PF10-HDE-Build-Notes v13.5.2, searched on `main` for a rule on maps, registers or promotion: none applies beyond addendum 2.1.
- `gcfpe.decision-record.md` D17, D18 (its two successors), D22, D25 and D26.
- `authoritative-surfaces.md`: *Stale-state sweep* and *Restating is allowed; asserting is not*.
- The governance audit's `references/project-prompt-registry-schema.md`.
- `BRIEF-PLAN-1-A.md` §1, §3 and §5; `REVIEW-PLAN-1-A.md`; `REVIEW-PLAN-1-B.md`.

I claim nothing from PF27 or the other documents named in `BRIEF-PLAN-1-A.md` §1, which I did not read.

## For Nathan

The plan has four open required defects and no further review round under D26-A. DIFF-1 would stop the promotion at the register step, after the register already selects 100926.1.

- **Option 1:** approve the plan as it stands, accepting the four as risks. Not recommended, because of DIFF-1.
- **Option 2:** opt into one bounded repair of the four, priced as another round under D26-A rule 4. The repairs touch three places:
  - `activation-delta-100926.1.json`: the X15(c) and X16 rows;
  - `registry-header-100926.1.json`: row 2;
  - N10: render the delta, then check.

**Recommendation:** option 2.

DECISION NEEDED
