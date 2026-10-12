1 distinct confirmed REQUIRED finding.

# REVIEW-PLAN-DIFF-2 — check of the PLAN bounded repair's diff, MODIFICATION-20261011-gcfpe-mb008-to-promotion

**Reviewer:** REVIEWER-PLAN-DIFF-D, fresh context. I did not author the plan, and I was not reviewer A, B or C.

**Brief:** `BRIEF-PLAN-DIFF-2.md` at `621907a`. It binds §3 (R1–R4) and §5 (cap and exit) of `BRIEF-PLAN-1-A.md` unchanged. Nathan overrode `review_cap` for this one check.

**Diff checked:** `1fc352a..7c41120`, covering the record, `PLAN-20261011.md` and `plan/`. I read both commits with `git archive`, not the working tree.

**Canon:** `main` `9312add2`. **Date:** 2026-10-12 (UTC).

## Answer

All four repaired findings are fixed:

- **P-B1-R:** fixed.
- **DIFF-1:** fixed.
- **DIFF-2:** fixed.
- **DIFF-3:** fixed.

The five opted-in listed items (L-2, L-3, L-5, L-6, L-9) are also fixed. I reran the parts of the dry run that the repair changed, and they reproduce the receipt.

The repair adds one required defect, PIN-1. Under the new pin rule, the five lane hubs fail their pin at X15 on the normal path. Their fetch revision moves when X5 edits the member bodies under them, and the rule does not list them among the pages the plan moves itself. So X15 stops, after it has already created the catalog and the register entry.

| # | Class | Defect | In repair text |
|---|---|---|---|
| PIN-1 | R1 | The new pin rule refuses all five hubs at X15. X5 moves their revision by editing their child member bodies, and the rule names only PE, the Flow Index and the register. | yes |

## Repaired findings

| Finding | Disposition | Evidence (my reruns on fresh reads, cutoff `2026-10-12T01:44:31Z`) |
|---|---|---|
| P-B1-R (R2) | **Fixed** | FI-ACTOR-1, FI-ACTOR-2 and FI-BIND-P each resolve once on the Flow Index at its pin `2026-10-11T20:10:23.284Z`. The rendered MGMT-10 actor-map row reads "the `GCFPE_MODIFICATION_RECORD`" and "GCFPE-MGMT-10 returns every result to Nathan and emits no handoff". The bindings paragraph is dated `@ACTIVATION_DATE`, and its sentence "The operating-procedure binding is v5.0.0, unchanged since 2026-09-23" matches the table's v5.0.0 row. The same render also removes L-8's Flow Index cases (FI-B-SKILL, FI-B-MANIFEST, FI-B-GRAPH). |
| DIFF-1 (R1/R2) | **Fixed** | REG-MEM's *Release rule* carries no 091426.1 clause: "all 55 are `100926.1`". The historical clause stays under `## Historical explicit membership — 091426.1`. With every operation applied, the register gives 0 findings and `current_selection_ok` true. N10 now renders and then checks, which closes the gap that hid DIFF-1. |
| DIFF-2 (R2) | **Fixed** | REG-SEL is written in full. The machine contract carries `@PRODUCTION_TOKEN`. Alpha state is only a pointer, to *Alpha state — recorded in the repository, not here*, which exists on today's Flow Index, as the D18 successor requires. The transaction order is left to the register entry. The archival claim has left the selection section, but its class recurs in REG-MEM (M-1, listed). |
| DIFF-3 (R2) | **Fixed** | Both stages build: candidate 535,417 B (equal to the receipt), selected 535,408 B; both read back equal. Their YAML header has no fetch-manifest row and no `body_extraction_convention`, and it carries no extraction, byte-count or `evidence_contract` text. `check` is `ok` (`deleted_absent`, `manifest_row_absent`). A header string citing the deleted key is refused (`deleted_keys_cited: ["body_extraction_convention"]`). `compare` differs only at the five specified paths. |
| L-2, L-3 | **Fixed** | The PLAN opening and §4 now say what N9 and N10 actually prove. |
| L-5 | **Fixed** | `--landed` evaluates each page as read and requires every operation to be LANDED. A static check found no operation whose replacement or start anchor occurs inside another operation's replacement on the same page (87 operations on 56 pages), so `state()` reports LANDED after a correct landing. Without `--page`, the testing page now fails loudly instead of standing in. |
| L-6 | **Fixed** | The marker text now names X6's report. |
| L-9 | **Fixed** | X6a's three operations resolve once on the inventory at its pin `2026-10-11T19:47:45.856Z`. The rendered page carries the successor mention and neither "reuses GCFPE-MGMT-10 at 091426.1" nor "reused unchanged". |

## Required finding

### PIN-1 — R1: the new pin rule stops X15 on the five lane hubs

**Exact text.** PLAN §7, *The operations*:

> "**Pins:** each page's pin is its revision on the PLAN reads. Before its write, a page moves only through this plan's own steps: PE at X5, the Flow Index when X1 moves the successor under it and X15(a) creates the catalog under it, the register when X15(f) creates the entry under it. For those three the pin is passed with `--pin` … Any other page whose revision moved stops X15."

The rule is enforced by `activation_render.py plan`, through `row["revision_matches_pin"] = got[1] == pin`. It is repeated in the §P X15 row ("at the pins") and in P-L2 ("a page that moved after the post-flight read is refused at X15 by its pin").

**Evidence.**

- The revision the renderer compares is the fetch header's `as of` value (`control_check.latest`, `FETCH_HEAD` group 2), not the page's own last edit. For a hub, `as of` is the newest edit among the hub and its child pages. Each hub's pin in `activation-ops.json` equals, to the millisecond, its child member's pin in `edits.json`, and each hub's own `page_last_edited_at` is two days older:

| Hub | Pin (fetch `as of`) | Equal to the pin of child | Hub's own `page_last_edited_at` |
|---|---|---|---|
| HDE Change Flow `3db4590a05eb81d59059eb6b95ed5fcf` | 2026-10-11T15:47:22.369Z | CF-E-30 100926.1 `3f44590a05eb8104824fe084354a0ef8` | 2026-10-09T20:19:06.953Z |
| HDE IA `3db4590a05eb8195a2ccf7c0959a8b6e` | 2026-10-11T15:59:38.185Z | RS-20 100926.1 `3f44590a05eb81be9566cd6397c9424c` | 2026-10-09T20:19:03.530Z |
| HDE QA `3db4590a05eb814d96d3dcfa8835f96d` | 2026-10-11T15:57:29.752Z | QA-70 100926.1 `3f44590a05eb81209128ea7c82938faf` | 2026-10-09T20:19:05.496Z |
| Escalation `3db4590a05eb81cd938de84cfffead9c` | 2026-10-11T16:05:06.087Z | ESC-40 100926.1 `3f44590a05eb8173905cc6d17a40457b` | 2026-10-09T20:19:08.504Z |
| HDE TW `3db4590a05eb811b9c14f2ae89c28df7` | 2026-10-11T16:10:06.322Z | PE Metaprompt 100926.1 `3f44590a05eb81f98b76c83465dc1960` | 2026-10-09T20:19:09.916Z |

- Those five children are the bodies MODIFICATION-20261010's EXECUTE edited on 2026-10-11. Every 100926.1 member and PE is a child page of one of these hubs, as the hub fetches list.
- X5 edits all 54 runtime members and PE. Every page has at least one operation: N9's `--landed` fails all 55 rows before the writes. So by X15 every hub's revision differs from its pin.
- The dry run could not show this. Its reads predate X5, and N10 reports `pins_match: 10`.

**Path:** normal, from X13 to X15. **Likelihood:** certain.

**Consequence:**

- At X13, each post-flight reviewer's own `activation_render.py plan --emit` already shows the five hubs with `revision_matches_pin: false` and `ok: false`.
- At X15, the render runs after (a) and (f) have created the catalog and the register entry. It refuses the five hubs, so X15 stops for Nathan's disposition.
- The run then leaves:
  - a new catalog under the Flow Index;
  - a register entry already reading "X15 … done";
  - no binding written;
  - the register still selecting 091426.1.
- Nothing is destroyed, but the normal path cannot complete as written.
- P-L2's account of the pin is also wrong. The pins are PLAN-read revisions, not post-flight reads.

**Smallest correction:**

- In PLAN §7's *Pins*, add the five hubs to the pages the plan moves itself, because X5 edits their child bodies.
- Pass each hub's pin with `--pin`, from a fresh read taken after X6. That read can also serve X13's reviewers.
- Correct P-L2 to match.

**In text the repair added:** yes. The pin refusal is in the new `activation_render.py`, and the *Pins* paragraph is new in PLAN §7.

## LISTED

Each line gives the path, likelihood and consequence, and whether it sits in repair text. New in this check:

- **M-1 (the L-4 class persists).** PLAN §7 says "every new section and sentence is phrased to stay true at any moment of the transaction", and §10 says the complete texts "remove L-4's … cases". Four texts are false for part of the transaction:
  - REG-MEM, written at X16: "The predecessor `091426.1` versions … are archived intact". This is false through X17–X19, and it stays false after X18's "stop; no archival".
  - The register entry, created at X15(f) with X15 marked "done" before (b)–(e) are written. Its own rule says "a step not marked done has not happened".
  - FI-BIND-P at X15: "read back before the register changed", before X16 has run.
  - The Flow Index frontmatter keeps `predecessor_disposition: SUPERSEDED_ARCHIVED_INTACT` beside the new `predecessor_release: GCFPE-20260914.1`, from X15 to X19.

  Normal path, transient; certain. The texts persist only on loud-stop paths. Low to medium. Repair text, except the frontmatter key, which is carried.
- **M-2 (`check` coverage).** `activation_render.py check` tests LANDED only for the 59 listed operations. The 281 generated operations are covered only through `control_check`, which cannot see `activated_at`, `predecessor_release`, `predecessor_version_family` or the `recovery_correction_run` → `source_modification` swap. Nothing verifies the two new pages' content after creation, or the register entry's step-row writes at X16–X19. PLAN §7's "`check` verifies after the write that every operation landed" overstates this. Failure path (a dropped or partial write); low; silent. Repair text.
- **M-3 (invocation gaps).** Three commands lack arguments they need:
  - X15's `plan --emit` names no `--pages`, so it also renders the inventory, which X6a has already changed (its anchors gone, its revision moved), and reports `ok: false`. The new pages are rendered only without `--pages`.
  - X6a's `check` needs `--set @MGMT10_PAGE_ID`.
  - X13's reviewers cannot know `@POSTFLIGHT_VERDICT`, `@PROMOTION_APPROVED_AT` or the two new page ids. Without stand-ins, the operations carrying those markers are refused and not shown.

  Loud; procedural. Repair text.
- **M-4 (repository pointers before the merge).** Several texts describe the PR branch, while `main` keeps `GCFPE-PCR-20260914.1` and the 229-edge parts until Nathan merges at X22:
  - REG-SEL's per-prompt contracts row "(`GCFPE-PCR-20261009.1`)";
  - REG-SEL's machine-contract row and FI-B-GRAPH, which carry `@PRODUCTION_TOKEN`;
  - every `execute/` evidence path in REG-SEL and the Flow Index rows.

  Meanwhile `authoritative-surfaces.md` says "the repository wins". Normal path; certain; transient until a merge Nathan controls; low. The registry-id parenthetical is new text.
- **M-5 (`@ACTIVATION_DATE` across UTC midnight).** Only `activated_at` is corrected if X16 ends on a later date. REG-SEL's "Selected @ACTIVATION_DATE", and REG-EXEC's heading and sentence, keep X15's date. Low. Repair text.
- **M-6 (hub wording, pre-existing).** The selected hubs keep `## Candidate family members`, the "Candidate prompt" and "Candidate binding" columns, and `candidate_member_count`. The old delta kept them by design. Low.
- **M-7 (wording).** PLAN §8 says "the six binding pages", but X15 writes eight: PE, the Flow Index, five hubs and the Alpha checklist. The page-title property writes are not listed separately. Wording. Repair text.

Still listed, not opted in, and not reported as defects: L-1, L-7, L-10, L-11 and L-12, as REVIEW-PLAN-DIFF.md states them.

## Trend

The count of distinct confirmed required findings went from 8 (round 1) to 4 (diff check) to 1 (this check). That more than halves. But the one finding sits in text the last repair added, so D26-A rule 5's second condition holds. This was the one extra check Nathan authorized, and the plan now returns to him with PIN-1 and the listed findings open.

## Checks run

Everything ran in scratch, outside the repository, from copies of the installed skills, with `PYTHONDONTWRITEBYTECODE=1`.

| Check | Result |
|---|---|
| Graph parts | Built from the parent's parts: `graph_assemble.py apply` with the stand-in URL, shipped `reindex`, then `check` `ok` and `flip`. The production build has 55 nodes, 235 edges, 593,569 B, `8391ad84…`, PASS, equal to the receipt. |
| `control_check.py` | `selftest`: 16 of 16 cases, archive set 57. `check` on the nine fresh reads: 306 findings, equal to the receipt. |
| `activation_render.py` | `selftest`: 6 of 6. `plan` with the receipt's stand-ins: 10 pages at their pins; 340 operations (59 listed, 281 generated) applied, 0 refused; 0 findings; positive checks pass; catalog and register entry pass. All equal to the receipt. I read the rendered Flow Index, register, catalog and entry in the terminal. `check_text` on the rendered entry gives 0 findings. |
| Registry | 46 package redlines and the glow-graph-contract patch applied to the scratch copies. `registry_assemble.py` build, check and compare at both stages, and the stale-citation refusal, as in DIFF-3's row above. |
| Production graph facts | Two facts REG-MEM states hold: `PR-50` has no prompt-originated inbound edge (its only inbound edge comes from `NATHAN_ABORT_INSTRUCTION`), and MGMT-10's only edge is `TERMINAL_RETURN_NO_HANDOFF`. `producer_allocates_pf10_number` is true here and false on `main`. REG-SRC's sentence still holds, because it is scoped to the read-only check. |
| PIN-1 evidence | Each hub's pin compared with the `edits.json` body pins and with the hubs' own `page_last_edited_at`. |

**Not run:**
- N0–N3 and N5–N8, beyond applying the patch and the redlines as inputs.
- N9's `assertions`, with or without `--landed` and `--inject`. I fetched no runtime member body, so `--landed` was checked statically.
- The Notion writes, so I could not observe that X5 moves a hub's revision. PIN-1 rests on the five exact equalities above.
- The duplicate, the X6 report, the real marker values, D24, the post-flight and the promotion transaction.

## Reads and D22

Notion was read only, with one fetch per page:
- the register;
- the Flow Index;
- the five hubs;
- the Alpha checklist;
- PE Metaprompt 100926.1, a prompt body;
- the candidate inventory;
- Register Entry — GCFPE-20260914.1.

The harness saved two results to this session's `tool-results` directory: the register, a control page, and PE Metaprompt 100926.1, a prompt body.
- I read PE only through the plan's readers and one terminal print of its ten-line frontmatter block.
- The harness had already refused this session's `rm` on a `tool-results` file. So under D22's refined condition 4, both files are left to the harness's teardown and will not be read again.
- Two saved results of `git diff` output hold repository text only.

No body was copied, hashed or compared. This record quotes only control-page sentences and frontmatter keys. My scratch directory held repository snapshots, skill copies, graph parts and registry builds, and I deleted it at the end.

**Canon relied on:**
- `AGENTS.md`.
- PF04-Canon-HDE-Governance v2.8.7 §9.1.6, read in full on `main` `9312add2`.
- PF10-HDE-Build-Notes v13.5.2, addendum 2.1, read in full.
- `gcfpe.decision-record.md`: D17; D18 with its two successors; D22; D26-A and D26-B.
- `authoritative-surfaces.md`: *Release baseline*, its rule of precedence, *Stale-state sweep*, *Restating is allowed; asserting is not*, and the D18-successor paragraph.
- `BRIEF-PLAN-1-A.md` §1, §3 and §5; `BRIEF-PLAN-DIFF-2.md`; `REVIEW-PLAN-DIFF.md`.

I claim nothing from the other documents in `BRIEF-PLAN-1-A.md` §1, which I did not read: D20, D21, D23–D25, D27, the templates and procedures, PF04 §9.1.2 and §9.1.3, PF06 §0.1A, and PF27.

## For Nathan

The plan comes back for approval with PIN-1 open, plus M-1 to M-7 and the carried listed findings.

PIN-1 is a small text and command correction. It changes PLAN §7's *Pins* and the X13 and X15 commands, so that each hub's pin comes from a read taken after X6. Approved as written, X15 would stop on its first render, after creating the catalog and the register entry.

Recommendation: correct PIN-1 before EXECUTE. Whether that correction gets another review is your decision, because D26-A's cap is reached.

DECISION NEEDED
