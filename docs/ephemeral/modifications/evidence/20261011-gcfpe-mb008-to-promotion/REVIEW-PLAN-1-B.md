6 distinct confirmed REQUIRED findings.

# REVIEW-PLAN-1-B — PLAN of MODIFICATION-20261011-gcfpe-mb008-to-promotion, full review 1 of 2

Reviewer: REVIEWER-PLAN-1-B, fresh context. Brief: `BRIEF-PLAN-1-B.md`, committed at `0c0c510`. Reviewed: commit `1b742bb84e42b5fdceb63eebcc2ba3b7cce0b15d` — the record's §P and frontmatter, `PLAN-20261011.md` and `plan/`, read with `git archive` of that commit. Canon was read on `origin/main` `9312add2`; the branch changes nothing under `docs/pfcanon/`. Dates: 2026-10-11 to 2026-10-12 (UTC).

**Answer.** The plan's measurements reproduce:
- the byte equality of the shipped 091426.1 contract;
- all four graph tokens;
- both 100926.1 contracts, byte for byte against the dry-run receipt;
- the 25-substitution profile and its two pending errors;
- 46 of 46 redlines;
- the body rehearsal on a five-page fresh sample.

Six required defects remain.

Three put silent wrong content into governed or control surfaces:
- the control pages updated in place are only partly rewritten;
- the 100926.1 contracts carry 091426.1's `promoted_at`;
- the selected graph parts receive the candidate's header.

One leaves a release member naming the archived predecessor of a member this plan replaces.

Two are normal-path step gaps:
- X2's verification needs a profile that X8 builds;
- there is no post-merge checkpoint.

None of the six is in text a repair added, because this is round 1.

## REQUIRED findings

### P-B1 — R2: control pages updated in place keep 091426.1 bindings and facts under 100926.1 titles

- **Exact text** (PLAN §7):
  - X15(c): "the Flow Index retitled to 100926.1, its frontmatter, *Direct successor control bindings* and *Selected topology* rows moved to the 100926.1 pages and proof token".
  - X15(d): "the five hubs retitled to 100926.1, frontmatter `selected_release` (the stale `candidate_release` key is corrected) and their activation-contract sentence".
  - X16: "the four other "Current … — 091426.1" headings move to 100926.1".
- **Evidence.** Fresh read-only fetches of the pages these steps edit:
  - **Hubs.** The Escalation hub `3db4590a…cd938de84cfffead9c` has a `## Candidate family members` table. Its rows are "ESC-10 — Create QA Escalation Report — 091426.1 | `https://app.notion.com/p/3db4590a05eb81d582b8d490e77f9f40?pvs=204`" and so on: the 091426.1 pages that X19 archives. The TW hub `3db4590a…1b9c14f2ae89c28df7` has the same table for UTIL-10 091426.1. It also says "The candidate `PE Metaprompt 091426.1` is the authoring control for this release." X15(d) touches neither.
  - **Flow Index `3db4590a…de9736ea69bac61016`.** X15(c) leaves these sections untouched:
    - "## Activation contract — discharged 2026-09-21 **This index is operative**, because the register selected `GCFPE-20260914.1` / `091426.1` / `55`";
    - "Promotion evidence", which cites round 27;
    - "Native flow changes": "GCFPE-MGMT-10 complete repair returns `READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION` with one complete PR-10 invocation". That is false for the DN-C A successor.
  - **Register `3d24590a…ce942ad994cfca9fa1`.** These sections stay as written:
    - "## Current explicit membership — 091426.1": the 091426.1 catalog "is the exact 55-page mapping", "`PR-35` is the sole new member", "all 55 are `091426.1`";
    - "## Current GCFPE change-management process — 091426.1": links MGMT-10, MGR-10 and CL-40 at 091426.1;
    - "## Current GCFPE procedure and operator access — 091426.1": "[PE Metaprompt 091426.1] governs GCFPE authoring".

    Only the headings move. The 2026-09-21 promotion wrote new "Current" sections and moved the old text under "Historical" headings. The register still shows that pattern.
  - **Why nothing catches it.**
    - X15 verifies only "every named field and row equal to the packet's activation delta", and X16 only "selection reads 100926.1".
    - X19's "the hubs and Flow Index hold only 100926.1 members" counts child pages, not table rows.
    - X20's literal sweep cannot see statements without a literal: "PR-35 is the sole new member" and the Flow Index's MGMT-10 bullet carry none, and the member count 55 is the same for both releases.
    - Under P-L2 the post-flight reviews only the specified delta, and the omitted sections are not in it.
- **Path.** Normal path.
- **Likelihood.** High if §7 is followed as written. X20 mitigates it partly for rows that carry the literal.
- **Consequence.** After promotion, the selection register's current sections, the five hubs and the Flow Index name archived 091426.1 pages as the current catalog, manager, authoring control and family members. They also state false facts about the selected release. This is the "navigation was wrong" failure in `authoritative-surfaces.md`'s 2026-09-22 sweep: sessions reach navigation first.
- **Smallest correction.**
  - In §7, state each in-place control's complete release-bound content:
    - **hubs:** member table rows and bindings move to the 100926.1 pages; the TW authoring-control sentence names PE 100926.1; every release frontmatter key changes (`artifact_version`, `prompt_version_family`, `selection_rule`, `predecessor_*`, `activated_at`);
    - **Flow Index:** Activation contract, Promotion evidence, the MGMT-10 bullet in Native flow changes, and the MGMT-10 row of the actor map;
    - **register:** new "Current … — 100926.1" sections, with the 091426.1 text moved under "Historical … — 091426.1".
  - Add a check to X15 and X16 that can fail: on each re-fetched control page, no non-historical section links any of the 57 archive-set page ids.
- **In text the last repair added?** No (round 1).

### P-B2 — R2: both 100926.1 contracts carry `promoted_at: "2026-09-21"`, 091426.1's promotion date

- **Exact text.**
  - `patches/glow-graph-contract-mb008.patch`: "Promotion adds these keys (flowmaster-validate CONTRACT_LIFECYCLE_KEYS): present, naming the release, once it is selected; absent while it stages."
  - `PROMOTION_DERIVED` lists only `selected_release`, `selected_prompt_version` and `selected_member_count`.
  - Claim C5: "release-values-100926.1.json holds only true literals".
- **Evidence.**
  - The template `gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json` holds `"promoted_at": "2026-09-21"`, and neither the patch nor the release-values file touches it.
  - My candidate contract (634,454 B, `5d412504…`) and production contract (631,092 B, `17bf6c3f…`) are byte-identical to `dry-run.json`'s. Both carry `promoted_at: "2026-09-21"`.
  - The candidate contract is `UNSELECTED_CANDIDATE` and still carries it.
  - `CONTRACT_LIFECYCLE_KEYS` names `promoted_at`, and the validator's comment says "promotion genuinely adds promoted_at".
  - The derived validator's `validate_contract` returns `[]` on both contracts. `contract_lifecycle_key_shape` checks only the token's shape, and X12's comparison excludes lifecycle keys.
- **Path.** Normal path, X7 to X8.
- **Likelihood.** Certain.
- **Consequence.** After CF-F06-1, the shipped production contract is the current specialization overlay in change-flow and flowmaster-validate. It states a promotion date three weeks before its release existed. The staging contract contradicts the patch's own rule. Nothing catches either.
- **Smallest correction.** Add `["delete", ["promoted_at"]]` to `release-values-100926.1.json`. Neither 091426.1 regeneration passes a release-values file, so its byte equality is unaffected. I removed the key from the production contract and checked: `validate_contract`, `contract_top_level_key_drift` and `contract_lifecycle_key_shape` all return `[]`. Alternatively, pop it in the patch while staging and record the real date only after X16.
- **In text the last repair added?** No.

### P-B3 — R1: PR-35 100926.1 still names "the selected GCFPE-MGMT-10 … — 091426.1", which DN-C A replaces and X19 archives

- **Exact text** (PR-35 100926.1, fresh read as of 2026-10-09T20:12:39.512Z, *Prompt navigation and maintenance*): "Report a defect in this prompt/version to the selected `GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1`; do not repair prompt policy during a PR run."
- **Evidence.**
  - Under DN-C A, the duplicate becomes MGMT-10's successor at 100926.1 (X1–X3), and X19 archives `3db4590a05eb81d1bb64ebcb3ca8eb54`.
  - `edits.json` has two PR-35 operations, TS-PR-35 and T1-PR-35. Neither touches the sentence. No guard or profile check reads it.
  - The sentence was true under the parent's candidate, which reused MGMT-10 at 091426.1. DN-C A made it false.
  - The bodies I sampled use a versionless form: OPS-10 has "to GCFPE-MGMT-10 — Manage an Ecosystem Change in Notion directory …". A Notion search found only PR-35 among candidate pages with the versioned form. The search is not a measurement.
  - PF04 §9.1.6 requires every affected consumer to be reconciled "in one coherent successor selection".
  - X20 either misses the sentence, or has to edit a selected member body after X13 and X18. D17 says such an edit voids the verdict.
- **Path.** Normal path.
- **Likelihood.** Certain in the release text. It does harm only when a PR-35 session reports a defect.
- **Consequence.** A selected member names the archived six-input MGMT-10 as the selected manager. A PR-35 session reporting a defect is pointed at it. That page is the one A-4 found unfit, and its handoff names an archived PR-10. It is silent.
- **Smallest correction.**
  - Add one PR-35 operation that replaces the versioned name with the versionless form the other bodies use.
  - Add a forbidden guard over all 55 bodies, `GCFPE-MGMT-10[^.\n]{0,80}091426\.1`, broad match with no exceptions, to measure any other instance.
- **In text the last repair added?** No.

### P-B4 — R1: no post-merge checkpoint; X21 writes §E and closes MB-008 and MB-003 before PR #605 merges

- **Exact text.**
  - §7 X21: "… one new decision-record entry …; §E; MB-008 and MB-003 closed on the backlog | `modification_validate.py` passes; the build of `docs/graph/parts` reproduces the production token".
  - §9: "Merge PR #605 | after X21 | merging preserves the record and approves nothing (D21-C); the selected repository surfaces become current on `main`".
- **Evidence.**
  - The MGMT-10 testing body governs this run. Under `MODE = EXECUTE` it says: "After he acts, continue from that checkpoint, started from `main`: detect each merge by files on `main`, run the post-install digest comparison, and only then return `ECOSYSTEM_CHANGE_COMPLETE`". Under *Boundaries* it says: "The change itself is complete only when `EXECUTE` has verified what landed after his merges and installs".
  - Template §P: "Merge, install, promote — named, with how each is verified."
  - D26-C allows post-merge steps "started from `main`, with the merge detected by files on `main`".
  - No step follows X21. The merge row states an effect, not a verification.
- **Path.** Normal path.
- **Likelihood.** Certain that the step is missing. Harm when the merge is late or differs.
- **Consequence.** From X16 until the merge, `main` still says 091426.1 is selected: `authoritative-surfaces.md`, `docs/graph/parts` and the registry. `main` is the persistent authority ("the repository wins"). Meanwhile the register says 100926.1 and the backlog says MB-008 is closed. Nothing ever confirms the selected surfaces landed.
- **Smallest correction.**
  - Add X22: after Nathan merges PR #605, start from `main` and detect the merge by files on `main`. Build `docs/graph/parts` there and compare it with the production token. Then close MB-008 and MB-003, complete §E and return `ECOSYSTEM_CHANGE_COMPLETE`.
  - Move the backlog closure from X21 to X22, and put X22's check in §9's merge row.
- **In text the last repair added?** No.

### P-B5 — R1: X2's verification uses the 100926.1 profile, which does not exist until X8

- **Exact text.**
  - §P X2 verification: "identity and governance checks of the 100926.1 profile; `PROMPT_TYPESAFE_READING` passes; testing page state absent".
  - PART-05 table, M-HEAD: "the 100926.1 profile's identity and governance checks pass". M-TS: "the profile's `PROMPT_TYPESAFE_READING` passes".
- **Evidence.**
  - `validate_gcfpe_20261009.py` and its profile come from `make_profile_20261009.py`. That needs `--contract` (X7), `--graph` (X3, which needs the duplicate's URL) and `--fixtures`, and X8 writes it ("profile; fixtures; derived validators").
  - `PROMPT_TYPESAFE_READING` exists only in the derived validator (S16).
  - The dry run did not exercise X2 (the brief's "not exercised" list).
  - A scratch profile built from the stand-in URL would fail `PROMPT_BODY_IDENTITY` on the duplicate, because the member's `notion_url` would not be the duplicate's.
  - So at X2, after the first external writes X1 and X2, the named check cannot run.
- **Path.** Normal path.
- **Likelihood.** Certain.
- **Consequence.** Executed mechanically, the normal path stops under D26-B after two Notion writes. Otherwise the session improvises a reorder, which a mechanical plan does not allow.
- **Smallest correction.** Either of these:
  - Order X1 → X3 → X7 → build the 100926.1 profile in scratch, as dry-run N6 does → X2's edits and checks.
  - Give X2 the checks available at that point: the title line, the `Prompt ID:` line, a `Notion URL:` line naming the duplicate, the M-TS text once, and the three page-state literals absent. Move the profile checks on MGMT-10 to X12.
- **In text the last repair added?** No.

### P-B6 — R2: X21's selected `docs/graph/parts` takes the candidate header: "No assembled graph or shipped validation proof exists"

- **Exact text.**
  - §7 X21: "`docs/graph/parts/` replaced by the production parts".
  - `graph_assemble.py` `flip`: "a copy whose only change is the lifecycle literals the selected parts carry … Nothing else moves".
  - Claim C6: "lifecycle literals flipped, nothing else".
- **Evidence.**
  - The selected `docs/graph/parts/global.json` `_prologue` is "# GCFPE-20260914.1 Candidate Graph Contract" plus a YAML header. The header carries `selection_status: SELECTED_PRODUCTION`, `complete_source_bytes`, `complete_source_sha256` and `content_status`.
  - The production parts keep the parent's candidate `_prologue`, which `flip` does not touch. My build of the flipped parts shows it: "# GCFPE-20261009.1 Candidate Graph Source Parts / No assembled graph or shipped validation proof exists for these candidate parts. See ../README.md."
  - `graph_parts.py` `render` stamps `complete_source_*` only where those lines exist. After X21 the selected graph has no header hash. glow-graph-contract's `SKILL.md` promises "the header hash cannot go stale".
  - `docs/graph/README.md` does not exist.
  - X21's verification is the embedded-JSON token, which excludes the prologue.
- **Path.** Normal path.
- **Likelihood.** Certain.
- **Consequence.** Low. The selected graph source calls itself unvalidated candidate parts, and loses its selection and hash header. It is silent.
- **Smallest correction.** Have `flip`, or X21, write the selected prologue on the 091426.1 pattern for GCFPE-20261009.1 / 100926.1: `selection_status: SELECTED_PRODUCTION` and the `complete_source_*` lines. Have `check --flipped` compare the prologue too.
- **In text the last repair added?** No.

## LISTED findings

One line each: path; likelihood; consequence. None is in repaired text.

- **L-1 (C5)** `release-values`' `governing_plan` says `"representation": "REPOSITORY_FILE_ON_MAIN"`. That is false from X7 until PR #605 merges, which is after install. Normal path; certain; low: S12 pins the values and never reads `main`.
- **L-2 (C5)** `make_profile_20261009.py` changes more than release pins, F05 and the PF10 2.1 body check. S08; S12's new `PREDECESSOR_CONTRACT_PIN` and `RETIRED_091426_STAGING_SOURCE` checks; S13's F09 receivers. Normal; certain; claim wording only.
- **L-3 (A5)** `graph_assemble.py check` plans from the MGMT-10 part's own URL. Any URL of the right form, the stand-in included, passes X3. Failure path; low; loud at X12 (`PROMPT_BODY_IDENTITY`).
- **L-4 (C2, D26-C)** Insertion operations are not safe to send twice: C-PLACE survives inside `new_str`. A re-sent `update_content` after compaction doubles C-TYPESAFE. Failure path; low; loud at X6's landing check; then restoration from page history.
- **L-5** M-HEAD writes "Prompt ID: `GCFPE-MGMT-10`", and the testing body already has that line under the heading M-HEAD removes. The line is duplicated. Normal; certain; cosmetic; no check fires.
- **L-6 (C7)** The MGMT-10 part marks `PRODUCT_OWNER_ACTION_PENDING` `terminal_for_invocation: true`. The body says "Not terminal." It is graph-valid, since a no-handoff return can only be terminal. Normal; certain; a post-flight check for "nonterminal branch that emits none" may question it.
- **L-7 (C8)** X15 rewrites the live release's Flow Index and hubs before X16. A stop between them leaves the selected 091426.1 release with no operative index or hubs until restored. Failure path; low; loud; not in P-L1 to P-L6.
- **L-8 (A4)** The derived validator keeps `validate_package`'s staging "selected alias" checks, pinned to GCFPE-20260913.1 / 091326.2 / 54. Unreachable with the production bundle; latent.
- **L-9 (A4)** V5 does not name `validate_gcfpe_current.py`. Its default contract is the 091426.1 one, and its schema-4.0 branch delegates to `validate_gcfpe_20260914`. The suite's finding path and `REQUIRED_SCRIPTS` also name 091426.1 files. Normal; edits needed; loud at X9. The suite on the redlined copies gives 10 BLOCK findings, all in classes V1–V7 name.
- **L-10** `validate_flowmaster.py:364` forbids "surface/model/reasoning recommendation". ANALYZE §2a marked it "Partly conflicts", and PLAN neither changes nor disposes of it. Low; it matches only that literal phrase.
- **L-11 (C4)** Mapping the oracle's runtime token `KRONOS_NEVER_EXECUTES_OPS_OR_QA` in `maintenance_metadata` stretches a mechanism its comment limits to "historical package/lifecycle metadata anchors". D23 changed R1 behaviour through a successor oracle instead. No ruling beyond D27 is cited. A question for Nathan, not a defect.
- **L-12 (F01)** CF-F01-2 says the core's stable-session requirement "does not apply" for GCFPE. flowmaster-primary derives a specialization "without weakening the embedded core". D27 supports the behaviour, but the exception is not recorded as one. Loud at X9 or D24 if flagged.
- **L-13** SR-F07-1 reads "a relay that composes a GCFPE handoff itself, before saving its output artifact, run the installed …", where "runs" is meant. Cosmetic, in shipped text.
- **L-14 (C1)** C-TYPESAFE's "`TypeSafe: not read` with the reason" differs from what the skill prints on failure ("TypeSafe v6: not read (…)"), while the rule says "as the skill prints it". Low.
- **L-15 (C1)** C-TYPESAFE's "The artifact holds the reading …, and task-specific advice on execution surface, with no model, reasoning-level or effort content" can be parsed as excluding model content from the whole artifact. Low.
- **L-16 (C1)** PR-35 keeps "Runtime surface and configuration are operator decisions outside this prompt" beside the new surface-advice duty. Tension only; low.
- **L-17 (C8)** §8 omits two kinds of write. The inventory page's status paragraph says it "reuses GCFPE-MGMT-10 at 091426.1 unchanged", which the row update makes false. EXECUTE's maintenance-surface state records, as the parent made on the Flow Index, are also missing. Both have destination rules, but the "every write" claim is imprecise.
- **L-18** X16 marks the dated "Unselected candidate record — GCFPE-20261009.1 — 2026-10-09" as executed, in place. AUTH-001 adds a successor beside a dated record instead. Low.
- **L-19** The failure path reads "a failure record committed on this branch". D26-B and the template say it "reaches `main`, in a record pull request". The two are equivalent only once PR #605 merges.
- **L-20** M-TS has no registry assertion: the G-TS guards exclude MGMT-10, and only the profile's S16 checks it. Definition of done item 3; low.
- **L-21** `PLAN-20261011.md` omits PF27's precedence sentence. The record's §A.2 carries it. Low.
- **L-22 (question)** It is open whether the D24 and post-flight reviewer briefs MGMT-10 issues fall under PF10 2.1 rule 1. M-TS covers only next-mode returns. Not exercised.
- **L-23 (question; X11 not exercised)** The registry header carries `authority_sources` rows `SELECTED_RELEASE_REGISTER` and `SELECTED_CATALOG`, the latter with a catalog URL. X11 assembles the registry before X15(a) creates the new catalog, X21 copies it to `main`, and no step says which URL the row holds. The 2026-09-21 promotion record had to correct this exact row, which pointed at the wrong catalog. If the assembly rule leaves the 091426.1 catalog or the inventory page there, this becomes an R2. The fix would be X21 setting both rows to GCFPE-20261009.1 and X15(a)'s page.

## Claims

| Claim | Verdict |
|---|---|
| C1 | Holds on the five-page sample: every operation applies once and every guard passes afterwards. P-B3 is a reconciliation gap beside it. L-14, L-15 and L-16 apply. |
| C2 | Holds. The self-test reproduces 14 guards, 37 fixture rows and 17 of 17 span cases. L-4 applies. |
| C3 | Holds on PR-50, CL-40 and OPS-10. ESC-25 and ESC-30 are non-producers about themselves, which is lawful under PF06 §0.1A. |
| C4 | Holds as text: 46 of 46 redlines land, the audit suite passes, and no oracle file is touched. L-11 and L-12 apply. |
| C5 | Byte equality reproduced. The derived page ids, staged parents, named prompts and lifecycle values are correct, except P-B2. L-1 and L-2 apply. |
| C6 | The candidate and production contracts are equal under `release_semantic_view`, once lifecycle keys and the graph digest are excluded. No D17 breach found: nothing is installed before X16, and installation happens at X17. P-B6 and L-8 apply. |
| C7 | The part is as specified, with 12 of 12 self-test cases. P-B3, P-B5, L-5 and L-6 apply. |
| C8 | D17's order is followed. The 57-page set is complete, and nothing a successor depends on is in it. P-B1, L-7, L-17 and L-18 apply. |
| C9 | The dry run reproduces byte for byte on the gates that need no fetch, and N2 reproduces on five pages. P-B4 and P-B5 apply. |
| C10 | Nothing outside the nine items is added. P-B3 is a gap inside ITEM-06. |

## What I reproduced

All in scratch outside the repository, with `PYTHONDONTWRITEBYTECODE=1`, from copies of the installed skills.

- **Patch.** `glow-graph-contract-mb008.patch` applies with `patch -p2`. `contract_recipe.py --check`: EQUAL against both bundled 091426.1 contracts (`dbae180b…`, 613,326 B). The unpatched recipe is also EQUAL.
- **Graphs.**
  - parent: 237 edges, `ff296b1e…`;
  - candidate: 235 edges, `df3b57a5…`;
  - production: 235 edges, `8391ad84…`;
  - selected: `ae2bd159…`.
  - `graph_assemble.py check` returns ok on both builds, and its self-test passes 12 of 12.
- **Contracts.** Candidate `5d412504…` and production `17bf6c3f…` (631,092 B), both equal to the receipt. An unfilled marker is refused.
- **Dry run.** `dry_run.py` without fetches: N0, N1, N4, N5, N6 and N8 pass with the receipt's values. N6 shows only the two pending errors; N8 lands 46 of 46. N2, N3 and N7 need the session's fetches.
- **Body rehearsal.** `body_check.py plan` on my fresh reads of PR-35, CL-40, PR-50, PE and OPS-10:
  - each revision equals its pin;
  - every operation applies once;
  - every batch is safe;
  - every guard passes afterwards;
  - the landing check would pass.
- **Validator suite.** `validate_flowmaster.py` on the redlined copies: 10 BLOCK findings. They are revision tokens, the Kronos token, the current overlay, self-identity and the reference allowlist, all in classes V1–V7 name.
- **Records.** `modification_validate.py`: 16/16 records pass.

## Reads, and D22

- **Repository.** Commit `1b742bb` via `git archive`; canon via `git show origin/main`.
- **Notion control pages, read-only.**
  - the register (the harness saved it as `tool-results/mcp-Notion-notion-fetch-1791762420957.txt`; I read a scratch extract and deleted it);
  - the 20260914.1 register entry;
  - the TW and Escalation hubs;
  - the 091426.1 Flow Index;
  - the candidate inventory.
- **Notion prompt bodies, one transient read each.**
  - the MGMT-10 testing body, as of 2026-09-24T11:00:24.691Z;
  - PR-35, PR-50, CL-40 and OPS-10, each at its pinned revision. OPS-10 was saved by the harness as `tool-results/toolu_01A26cESBVfyXGD6RkeriJch.json`;
  - PE, saved by the harness as `tool-results/mcp-Notion-notion-fetch-1791763252168.txt`.

  They were used only for the counts of `body_check.py plan` and to locate the 091426.1 and MGMT-10 references quoted above. I deleted the two harness files after use (D22 condition 4). The inline reads stay in the session transcript, left to the harness's teardown and not read again. No body was copied, hashed or compared. I also ran five Notion searches, which return snippets only.

**Canon relied on:**
- AGENTS.md
- PF10-HDE-Build-Notes v13.5.2, complete; addendum 2.1
- PF04-Canon-HDE-Governance v2.8.7, §9.1.2, §9.1.3 and §9.1.6
- PF06-Canon-Change-Process-Guide v2.5.4, §0.1A
- PF27-Canon-Plan-Templates v2.0.5, *Canon precedence for template use*
- `gcfpe.decision-record.md`: D17, the D18 successors, D20 to D27 (D23 read as its rulings section)
- `modification-template.md`, `ecosystem-change-management.md` §5–§6, `skill-packaging-and-delivery.md`, `postflight-procedure.md`, `notion-write-boundary.md`, `authoritative-surfaces.md`, `prompt-corpus-policy.md`
- `PROMOTION-RECORD-20260921.md`, by way of the register entry and the release-values sources
- The register's text and the 20260914.1 register entry
- The GCFPE-MGMT-10 testing body
- The installed typesafe-scoring `SKILL.md` and `score.py`

NOTHING NEEDED from Nathan yet. Under D26-A the author repairs P-B1 to P-B6, and the second full review or the diff check follows.
