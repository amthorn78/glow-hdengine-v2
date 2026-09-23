# ANALYZE skill evidence — MODIFICATION-20260923-closeout-residuals

Measured 2026-09-23 against the installed trees (`/root/.claude/skills/synced/…/`), which are identical
(`diff -rq`) to the round-a5 reviewed packages. Every test ran on scratch copies under
`PYTHONDONTWRITEBYTECODE=1`; nothing was written into the skills directory, and no prompt body was
read (synthetic bodies only). One analyst produced the findings. Two adversarial verifiers then tried
to refute them by reproduction (workflow run `wf_575cf35d-078`). Where the verifiers corrected the
analyst, the corrected fact is the one stated here.

## Baseline

Every installed suite passes today:

- `validate_flowmaster.py --strict-warnings`: `FLOWMASTER_SUITE_PASS`, 0 findings, `core_sync` true in
  all five core-carrying skills.
- Change Flow fixtures: 32 of 32.
- `run_gcfpe_current_fixtures.py` and `run_gcfpe_20260914_fixtures.py` (091426.1 contract): 228 of 228
  each.
- The PR skill validator: PASS.
- The relay self-test: 230 of 230.
- The governance-audit fixture suite: 35 tests OK.
- `graph_parts.py build`: 55 nodes, 229 edges, 55 state_routes; embedded JSON 575 074 B, sha256
  `ae2bd159…`, equal to the bundled graph copies.
- `glow-graph-contract` has no suite of its own.

## Pins every edit must respect

- **`flowmaster-validate` self-identity.** `SKILL.md:9` `SKILL_TREE_SHA256` covers every file in that
  skill. Any `flowmaster-validate` edit, including a profile edit, fails `FMV-GCF-CURRENT-001` until it
  is re-declared. The verifier confirmed this is the only pin those edits break.
- **Revision pins.**
  - `change-flow` 3.3.0: `change-flow/scripts/validate_gcfpe_20260914.py:746`,
    `validate_flowmaster.py:149` and `:1257`, and `validate_gcfpe_current.py:637-638`.
  - relay 3.1.0: `validate_flowmaster.py:185`.
  - PR skill 1.3.0: its own validator `:26`, `validate_gcfpe_20260914.py:2702` and `:1816`,
    `validate_gcfpe_current.py:654`, and the contract's `primary_skill_revision`.
  - `flowmaster-validate` 3.3.0: four sites.
  - A revision bump moves every one of these pins.
- **The protected core.** It sits between `FLOWMASTER_CORE_BEGIN` and `FLOWMASTER_CORE_END` and has
  sha256 `4d8bb9bf…` in `change-flow`, `session-relay-flowmaster`, `tw-flowmaster`,
  `flowmaster-primary` and `session-branch-flowmaster`.
  - `validate_flowmaster.py:1899` checks `core_sync`.
  - `change-flow/scripts/validate_gcfpe_20260914.py:26` pins `EXPECTED_CORE_SHA`.
  - `PRIMARY_FILE_IDENTITY` `0665507…` pins the whole of Primary.
  - No core byte may move.
- **Hidden markup.** FMV-GCF-DISPATCH-001 rejects `<!--`, `-->` and `--!>` in nine carrying files. No
  proposed text contains them.

## Per item

| item | status against installed bytes | sites | proposed change | detection | class / tier |
|---|---|---|---|---|---|
| ITEM-01 | VERIFIED | PR skill `SKILL.md:143` (the RS-20 package carries lineage, tests, reviews and CI evidence) | The RS-20 package is a `NEXT_PROMPT_HANDOFF` naming the saved `RESCOPE_REQUEST` by path; the request holds the content. Validator literal `:58` is kept (verifier: PASS on the edited tree) | add forbidden `package containing the actual finding` to the PR validator | B / 0 |
| ITEM-02 | VERIFIED, wider | relay `:279`, `:281`, first half of `:283` (model/strength and surface/model/reasoning advice carried in the handoff) | For GCFPE, no handoff, relay message or ledger carries a model assessment or reasoning recommendation; the named artifact holds what the receiver needs. Applies the retired-assessment rule (`change-flow:299`, governance-audit interop `:56`) | `CONTRACT_FORBIDDEN["session-relay-flowmaster"]` gains the two retired phrases | B / 0 |
| ITEM-03 | VERIFIED | `flowmaster-validate/SKILL.md:178` requires a `Selection status` header that its own validator rejects | describe the identity-only header, with `PROMPT_BODY_GOVERNANCE_STATE` and D23-G | fixtures already enforce the behaviour | C / 0 |
| ITEM-04 | VERIFIED | `flowmaster-validate/SKILL.md:212`, `:382`, `:398`, `:402`; profile `:43`; `validate_flowmaster.py:1765` help | bodies arrive on `--bodies-stdin`; the candidate root holds the graph only | ITEM-16 guard | B / 0 |
| ITEM-05 | VERIFIED, text and code | governance-audit description, `:109`, `:110`, `:113`; `report-contracts.md:39`; `epic-reengineering-interoperability.md:62`; code `audit_workspace_governance.py:445-480` hashes `prompt`, `notion_prompt` and `notion_page` sources and raises SRC-003 on a changed hash (`:572-574`) | Text: bodies are read live, never snapshotted or hashed. Code: prompt-kind sources carry no digest, and SRC-003 skips them | new fixture: a prompt-kind record carries no digest, and changed text raises no SRC-003 | B / 0 |
| ITEM-06 | VERIFIED as a GCFPE carve-out | relay `:378` (binding by content hash), `:263` (optional digest); `change-flow:295` (content identity) | a GCFPE prompt is bound by stable ID, version and direct Notion URL only. Message and response hashes (`PAYLOAD_HASH`, `RESPONSE_HASH`) are legitimate and stay | ITEM-16 guard | B / 0 |
| ITEM-07 | VERIFIED | governance-audit `behavioral-fixtures.md:49` rejects the cross-session PR-35 route | accept PR-30 → PR-35 across sessions by D23-D, only into the dedicated session Nathan created | prose fixture, none | C / 0 |
| ITEM-08 | CONFIRMED | the core's content pin and "content hashes" ledger field, in all five core carriers | One GCFPE override sentence outside the core, after the A1-6 sentence, in `change-flow` and `session-relay-flowmaster` only, following the A1-6 precedent. `flowmaster-primary` and `session-branch-flowmaster` are generic and unchanged; `tw-flowmaster` is out of scope. A verifier applied the insertion: `FLOWMASTER_SUITE_PASS`, `core_sync` true in all five | `CONTRACT_REQUIRED` for both skills | B / 0 |
| ITEM-09 | VERIFIED | `glow-graph-contract/SKILL.md:13` (277 rows, measured 282), `:133-134` (235 edges, measured 229), `:12` 94.3% (not reproducible without its method); `change-flow/scripts/validate_gcfpe_20260914.py:802` comment says 227 edges | state one dated proof token with its digest and drop the unreproducible percentage | none (no suite) | C / 0 |
| ITEM-10 | VERIFIED | `change-flow/SKILL.md:280` | the register names the selected release; 091326.2 is a superseded predecessor | none | C / 0 |
| ITEM-11 | PARTLY TRUE; location corrected | **`flowmaster-validate/scripts/validate_gcfpe_current.py:605`**. `change-flow` has no copy. It fires only when `--contract` names the schema-3.1 alias (the historical 091326.2 contract) together with `--bodies-stdin`, whatever the stdin | iterate the bodies supplied, not `required_markers`, so it fails closed with a named result instead of a `NameError` | two new fixture cases | C / 0 |
| ITEM-12 | CONFIRMED | `docs/graph/parts`: 222 indices in the prompt parts plus 13 in `global.json` for 229 edges; CF-C-10, ESC-40, PR-35, QA-70, RS-40 mismatch | re-derive every index from the assembled order (27 files); the build stays byte-identical (`ae2bd159…`); `graph_parts.py` gains `reindex`, and `build` fails on a count mismatch; the reindex lands before or with the stricter builder | the new builder check | C / 0 |
| ITEM-13 | CONFIRMED, wider | the contract regenerator and its recipe (`evidence/regenerate_contract.py`, `evidence/repair-a4/contract_recipe.py`); the registry deriver is the §7.5 rule inside `evidence/e1_registry_apply.py`, not a script | Move both into `glow-graph-contract/scripts/`. The recipe needs the pre-E2 contract `2b78f877…`, which was in scratch only; it is now kept at `evidence/pre-e2-contract/` (commit `245b21b`). A verifier regenerated `6902924a…` byte-identical from it | acceptance test: the kept input regenerates the shipped contract | C / 0 |
| ITEM-14 | VERIFIED, wider | relay `:273` (Drive the preferred artifact plane), `:358` (`GOOGLE_DRIVE / NONE`), `:265` (a Drive reference location) | Outside GCFPE a project may name Drive; for GCFPE the repository is the plane (D7). The enum gains `REPOSITORY`, and `validate_relay_manifest.py:1095` must accept it: a verifier showed the text-only edit fails the validator. Add a self-test case and update `manifest-v2-examples.md` | `CONTRACT_FORBIDDEN` `preferred artifact plane`; relay self-test | B / 0 |
| ITEM-15 | CONFIRMED | 5 distinct findings, all in `validate_flowmaster.py`: F2 (`:711`), N1/F3 and N4/F4 (`:757-758`), N2/F1 (`:790-800`), N3 (`:1320-1353`). None fires on today's files | the five fixes and their regressions; plus a dated correction note on the repair-a4 record's C8 and §2 wording, which overstates the guard (the claim-level half of N1/F3) | new regressions | C / 0 |
| ITEM-16 | **REFUTED as prototyped** | The prototype gave 23 findings before and 9 after, not 29 and 0. It missed 30 of 30 paraphrased violations and flagged the edits' own prohibitions | **Redesign:** (1) `CONTRACT_REQUIRED`: ITEM-08's override sentence in `change-flow` and `session-relay-flowmaster` (the two carriers; `tw-flowmaster` excluded); (2) `CONTRACT_FORBIDDEN`: every retired phrase this Modification removes; (3) the governance-audit code fixture (ITEM-05); (4) the limit recorded under `D14`: prose paraphrase is not mechanically detectable, and review holds it | GUARD-001: each guard fires on an injected regression | B / 0 |
| ITEM-24 | VERIFIED | `glow-po-reporting` (end every message in a named state); Hub *Worker communication rules* §2; `session-working-rules.md:83` | the named state is the line immediately before a `NEXT_PROMPT_HANDOFF` block | skill review | B / 0 |
| ITEM-36 | CONFIRMED | registry: all 55 rows carry the three `\A`-anchored guards with the `{0,7}` window; flowmaster-validate `validate_gcfpe_20260914.py:1145-1149` checks `nonblank[:8]`. A label line after 8 non-blank lines passes both (synthetic bodies; verification B4a-c). The census found 0 such lines in the 55 live bodies and 2 in the proposed MGMT-10 body | line-anchored whole-body patterns in the registry and in `PROMPT_BODY_RELEASE_HEADER`; `prompt-body-content-policy.md` updated | an injected label line past line 8 fails | B / 0 |
| ITEM-39 | VERIFIED, measured | broad match over the packaged skills for ALPHA_STOPPED, ALPHA_RESUMED, "PR04 not started", "Alpha remains", "sole operative state", `next_intended_unit` and `alpha_resumption` (TW excluded): prose in change-flow `SKILL.md:335`, flowmaster-validate `SKILL.md:174`, governance audit `interoperability-contracts.md:96` and `behavioral-fixtures.md:59`; validator markers requiring change-flow's line at change-flow `validate_gcfpe_20260914.py:1033` and flowmaster-validate `:2692`; machine records in both 091426.1 contracts and both graph copies (6 lines per file), checked at flowmaster-validate `:1901-1908` and change-flow `:1017-1018`, and in `docs/graph/parts/global.json` (`alpha_resumption_contract`) | prose: a pointer to the Epic's artifacts (the `D18` successor); markers moved; machine records per Open question 3 | the moved markers guard change-flow's line only; the other three prose sites are unguarded | B / 0 |
| ITEM-25 | VERIFIED | `glow-graph-contract/SKILL.md:59` | the bundled graph copies are validator fixtures built from `docs/graph/parts` | none | C / 0 |

## Registry parent IDs (ITEM-22)

Each registry row's page ID was found among the child pages of the six 091426.1 parent pages. Every row
matched exactly one parent, and none matched its registry value.

| old ID (registry today) | old title | new ID (actual parent) | new title | lane values | row values |
|---|---|---|---|---|---|
| `3c74590a05eb811d8433e7022629e213` | HDE Change Flow | `3db4590a05eb81d59059eb6b95ed5fcf` | HDE Change Flow — GCFPE-20260914.1 — 091426.1 | 7 | 18 |
| `3c74590a05eb81f2953de712f2adb6fa` | HDE IA | `3db4590a05eb8195a2ccf7c0959a8b6e` | HDE IA — GCFPE-20260914.1 — 091426.1 | 5 | 21 |
| `3c74590a05eb8149905fd694f6d2901a` | HDE QA | `3db4590a05eb814d96d3dcfa8835f96d` | HDE QA — GCFPE-20260914.1 — 091426.1 | 1 | 10 |
| `3c74590a05eb8123bc55ca7f99ce176c` | Escalation | `3db4590a05eb81cd938de84cfffead9c` | Escalation — GCFPE-20260914.1 — 091426.1 | 1 | 4 |
| `3c74590a05eb8176baf8cb59f1631f3c` | HDE TW | `3db4590a05eb811b9c14f2ae89c28df7` | HDE TW — GCFPE-20260914.1 — 091426.1 | 1 | 1 |
| `3cc4590a05eb8101b5ded32c12616eb6` | Glow HDE Prompt Flow Index | `3db4590a05eb81de9736ea69bac61016` | Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | 1 | 1 |

The six IDs cover 16 lane values and 55 row values, 71 in all. The titles are 16 lane titles and 54
row titles (PR-35's row has no title field). The audit's NAM-002 check (`audit_workspace_governance.py:604`)
compares the snapshot's `parent` against `expected_parent_id` as a plain string, and skips the
comparison when `parent` is absent. The PLAN gate therefore supplies a snapshot with undashed parents
and injects one wrong parent.

## Revisions that must move

| skill | advertised identity | pinned at | new |
|---|---|---|---|
| flowmaster-validate | `FLOWMASTER_VALIDATE_REVISION: 3.3.0` | four sites, and `SKILL_TREE_SHA256` | 3.3.1 |
| change-flow | `CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0` | its own validator `:746`; `validate_flowmaster.py:149`, `:1257`; `validate_gcfpe_current.py:637-638` | 3.3.1 |
| session-relay-flowmaster | `SESSION_RELAY_FLOWMASTER_SPECIALIZATION_REVISION: 3.1.0` | `validate_flowmaster.py:185` | 3.2.0 |
| glow-hde-pr-development | `GLOW_HDE_PR_DEVELOPMENT_SKILL_REVISION: 1.3.0` | its validator `:26`; `validate_gcfpe_20260914.py:2702`, `:1816`; `validate_gcfpe_current.py:654`; the contract's `primary_skill_revision` | 1.3.1, and the contract is regenerated |
| amthor-workspace-governance-audit | `WORKSPACE_GOVERNANCE_AUDITOR_REVISION: 1.12.0` | `scripts/run_fixture_suite.py:308` | 1.13.0 |
| glow-graph-contract, glow-po-reporting | none advertised | — | freeze digest only (`D19`) |

## Packages

| package | items |
|---|---|
| `flowmaster-validate` | 03, 04, 11, 15, 16, 39 (`:174` and the `:2692` marker); the regenerated contract copy and its pins (`:1012`, `:1477`, `:1816`, profile `:8`, `:27-28`); `CONTRACT_REQUIRED` for 08; `CONTRACT_FORBIDDEN` for 02, 14 and 16; whole-body release-line check for 36; its revision and self-identity |
| `change-flow` | 06 (`:295`), 08, 09 (the `:802` comment), 10, 39 (`:335` and its validator marker); the regenerated contract copy; its revision and pins |
| `session-relay-flowmaster` | 02, 06, 08, 14 (text, validator, self-test, examples); its revision |
| `glow-hde-pr-development` | 01 |
| `amthor-workspace-governance-audit` | 05 (text, code, fixture), 07, 39 (`:96`, `:59`) |
| `glow-graph-contract` | 09, 12 (`reindex` and the builder check), 13, 25 |
| `glow-po-reporting` | 24 |
| repository pull request | `docs/graph/parts` reindex (12); registry (22, guards); management documents |

`flowmaster-primary`, `session-branch-flowmaster` and `tw-flowmaster` are not changed. The core bytes
stay `4d8bb9bf…`.
