---
artifact_type: SPECIFICATION_KICKOFF
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION-KICKOFF
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: KICKOFF_READY
producer: Master Scrum
prompt: CF-C-10 — Prepare CRD Specification Kickoff Handoff — 100926.1 (https://app.notion.com/p/3f44590a05eb810f83d4d539e5b0e588)
created_at: 2026-10-12T18:55:00Z
repository_head_read: origin/main 483b9f7
class_selection_ref: docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md
source_ref: docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md
po_context_ref: none (Product Owner context is held in source_ref and class_selection_ref)
next_prompt: CF-C-20
next_actor: Isis
---

# HDE-CRD-0002 — CRD Specification kickoff

This kickoff is transient scaffolding between class selection and the Specification. It is not a Specification, an approval, an Implementation Plan, a QA plan or a PF10 artifact. It grants no authority to implement, plan or mutate anything.

## 1. Lineage

| Link | Reference | State |
| --- | --- | --- |
| Class selection | `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md` | `CLASS_SELECTED`, class CRD, selected by Nathan / Product Owner; on `main` (#612) |
| Primary source | `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md` | Current; supersedes v1.1 and v1.0; read completely (21,054 bytes) on `main` |
| Register | Candidate CRD Items List, items 5–8 (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d) | Items 5–8 `Accepted for CRD Drafting` (Product Owner, 2026-10-11) |
| Author of source | Isis, Lead Developer | Intake findings only; bounded scope is not approved |

Verification of class, identity and lineage (CF-C-10 step 1): class CRD and identity `HDE-CRD-0002` agree across the selection record, the source and the Notion register. `HDE-CRD-0002` matches `^HDE-CRD-[0-9]{4,}$`. No conflicting claim found.

## 2. CRD primary-source warrant

- **Observed-change basis.** All four items are observed defects or gaps in the current system, recorded during HDE-EPIC040 delivery, QA, closure and its CL-40 scan, and in the week's PR history. None is planned PF09 work.
- **Controlled identity.** `HDE-CRD-0002`, chosen by the Product Owner (verbatim evidence in the selection record). No PF09 inventory is formed or required (PF04 §9.1, "Epic and CRD change lanes").
- **Lane rationale (source-stated, Lead Developer finding).** Items 5, 6(b), 7 and 8 belong in the CRD lane. Item 6(a) is "not naturally CRD lane": it is a prompt change whose native route is GCFPE-MGMT-10, carried here by Product Owner direction. The Specification decides whether 6(a) is delivered inside the CRD or routed to GCFPE-MGMT-10 and tracked.
- **Product Owner decisions (verbatim, from the source):** 2026-10-11 "Move all items to accepted for CRD drafting."; "You can create a handoff for this to begin the process for HDE-CRD0002"; "Yes, add all seven to HDE-CRD-0002." 2026-10-12 "Add the 7 items to the CRD"; "APP_ENV in railway is set to prod" (a configuration report, not observed by the Lead Developer or Master Scrum).

## 3. Change summary

One CRD over four items:

| Item | Title | Parts |
| --- | --- | --- |
| 5 | HDE-EPIC040 carried defects | (a), (b), (c-1), (c-2), (c-3), (d), (e) ×7, (f), (g), (h), (i) ×3 |
| 6 | Open code PRs only after the implementation is pushed; review the code that missed it | (a), (b) |
| 7 | Read-only pre-push / pre-plan check script | one |
| 8 | Close-pack writer cannot produce a canon close report | one |

## 4. Scope by item

Key: **[S]** source-stated, from the briefs v1.2, with the briefs' own re-check commit where given; **[V]** verified read-only by Master Scrum on `main` at `483b9f7` for this kickoff; **[U]** unknown.

No file outside `docs/` and `AGENTS.md` changed on `main` between `d86b8850` (the briefs' check point) and `483b9f7` [V]. The `AGENTS.md` change concerns Codex review scope for Markdown and touches no item below [V].

### Item 5 — HDE-EPIC040 carried defects

**Need and facts**

- **(a) Wheel install omits release members.** `pyproject.toml` package-data covers only `catalog/*.json` and `math/*.json` [V]. A wheel install therefore omits release members and admission refuses outside a source checkout (O-12) [S].
- **(b) Production 404s are not governed.** The production app (`adapter.factory`, per the `Procfile`) returns Flask HTML 404s without `no-store` for unknown non-compat paths; only `/api/compat/v1` and `adapter.wsgi` return the governed `ERR_NOT_FOUND` (O-P06a-22) [S].
- **(c) CI coverage gaps.**
  - (c-1) 129 test files run in no CI lane (O-11, counted at PR05), holding 57 recorded failures and 13 collection errors, plus the `tests/reader_v1/test_cli_proof.py` baseline failure (RA-08, O-P06a-03). Some rewrite tracked evidence when run in the repository tree [S]. The count is from PR05; the source says the Specification recounts on `main` [U: current count].
  - (c-2) The classifier gives an unregistered `tools/qa/*.sh` or `*.sql` file the `evidence` and `qa` lanes with no owner test (O-22); the fail-closed unknown-source check covers only `tools/bodygraph/` [S, re-checked `d86b8850`].
  - (c-3) `ci.yml` `paths-ignore` lists 4 documentation prefixes [V: `docs/pfcanon/`, `docs/ephemeral/`, `docs/graph/`, `docs/prompt_ecosystem_management/`]; the classifier's `_DOCUMENTATION_PREFIXES` lists 8 (RA-12) [S]. A PR touching only `docs/crd/`, `docs/plans/`, `docs/qa/` or `docs/run/` still starts a CI run [S].
- **(d) Attestation on Debian.** The attestation builder's wheel stage fails under Debian-patched setuptools (O-10) [S].
- **(e) Seven carried defects (Product Owner, 2026-10-11).**
  - O-P07-01: `hdctl --help` showcompat summary says "Emit canonical Reader v1 bytes from vendor JSON (stdin or files)" [V, `engine/cli/main.py` ~line 79]; stdout is `magic10_compat_result.v1` [S]. The file is a release member [S].
  - O-P07-02: `aux-preview --band` is not applied when the band comes from the pair file [S].
  - O-P07-03: `dev/reader_harness/app.py` calls `app.getattr(...)` at import [V], raising `AttributeError` [S]. `VERIFY.sh` and `docs/acceptance/reader_a7_crib.md` still name it [S].
  - O-P07-04 (security-relevant): dev `GET /reader` in `adapter/http_reader.py` refuses only when `os.environ.get("APP_ENV", "dev") != "dev"` [V, line 603], so it serves when `APP_ENV` is unset or exactly `dev`. The production factory mounts that blueprint [S]. Production sets `APP_ENV=prod` per the Product Owner's 2026-10-12 report, so the route refuses today [S, not observed]. The fail-open default remains [V].
  - O-P06a-23: the engine-core evidence currency test ignores `release_id` [S].
  - O-P06b-17: current-release captures carry origin-family Mirror labels [S].
  - O-OPS01-01: the isolated closure's admission probe depends on the ambient installed package [S].
- **(f) `--allow-prod-vendor` is not implemented** (DD-04, QA50-B01). PF05 §7.1.11a–f states it as a Required-Now contract (flag on `hdctl bg:resolve --source vendor`; environment classification; rail and flag matrix; evaluation order; error carrier; audit contract) [S]. No match for `allow-prod-vendor` or `allow_prod_vendor` in `engine/`, `adapter/`, `scripts/` or `tools/` [V]. PF29 §16 tells users it is absent [S].
- **(g) Endpoint catalog incomplete** (RA-14). `docs/ENDPOINTS_CATALOG.json` (a symlink to `artifacts/audit/ENDPOINTS_CATALOG.json`) has no entry for `/api/aux/narrative`, `/aux/narrative`, `/internal/healthz`, `/internal/readyz`, `/ops/db/unavailable`, `/ops/probe/env`, `/ops/rails/refusal` or `/ops/writer/diagnostic` [V: 0 matches each; `/reader` matches]. Those routes are registered in `adapter/` [S].
- **(h) `.env.example` has no `GEO_API_KEY` entry** [V]. PF20 §2.26.7 records it with the implementation lane [S].
- **(i) Stale operator documentation** [S, re-checked `d86b8850`]:
  - O-P07-05: `docs/ADAPTER_009.md` "Readiness rules" describe a `compute_pair` smoke and typed 503s for `/internal/readyz`; `adapter/wsgi.py` returns 200 unconditionally and no `compute_pair` exists. Its port statements are stale.
  - DD-11: `docs/ADAPTER_009.md` (`COMPAT_GET_BODY_400_OK`) says `body_not_allowed`; the code emits `invalid_json` (FND-017). The code side was not re-checked by the source.
  - O-P07-06: `ARCHITECTURE.md` misstates the `emit_compact_json` return type, and its "Routing (dev only)" heading now also covers the production mount.

**Warrant [S].** (b) is live on the public production surface. (c) hides regressions in 129 files from CI, and (c-3) spends CI runs on documentation-only PRs. (d) breaks the next release attestation. O-P07-04 is not exposed today but fails open; the other (e) defects are misleading help, an ignored flag, a dead harness and evidence-tooling gaps. (f) is a canon requirement with no implementation, so no audited production vendor override is possible. (g) makes the source-of-truth catalog wrong. (h) and (i) mislead whoever configures or operates the service.

**Affected surfaces [S].**
- code: `pyproject.toml`, `adapter/factory.py`, `adapter/http_reader.py`, `tools/evidence/build_release_attestation.py`; the uncovered test files, `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`; for (e) `engine/cli/main.py`, the `aux-preview` CLI path, `dev/reader_harness/app.py`, `VERIFY.sh`, the engine-core evidence test, Mirror provenance labels and the attestation closure probe; for (f) the `hdctl bg:resolve` parser and vendor resolver; for (g) the endpoint catalog and its audit mirror; for (h) `.env.example`.
- data: none.
- operations: release attestation; for (f) the production override's audit trail.
- documentation: `docs/ADAPTER_009.md`, `ARCHITECTURE.md`, and as affected.
- governance: none expected.
- canon: none expected; (f) implements existing canon (PF05 §7.1.11).

**Constraints and risks [S].**
- (a) or (b) may change release members, forcing a manifest re-cut and new admission pins (`ADMITTED_RELEASE_*` in `engine/config/registry_loader.py`). O-P07-01 changes a release member and shares that re-cut; (f) may too.
- (c-1) may expose real defects that enlarge the work. Running the uncovered files in the repository tree can rewrite tracked evidence, so any sweep runs in a throwaway copy.
- O-P07-04's fix must not break dev, test or local use of `/reader`.
- (f) keeps generic SAFE rails first: the override never opens a closed rail and never lets public Reader or Aux traffic call the vendor (PF05 §7.1.11).
- (g)'s audit mirror is produced by its owning tool, never hand-edited.

**Lead Developer proposed bounded scope [S; not approved].** Fix (a), (b), (d), (h), (i). For (c-1), bring each uncovered file into a CI lane or retire it with a recorded reason; fix (c-2) and (c-3) in the same work. For (e), fix each defect or retire it with a reason; O-P07-04 by refusing the dev route unless `APP_ENV` is explicitly `dev`, `test` or `local`. For (f), implement PF05 §7.1.11 as written. For (g), catalog every served route or remove the route, and regenerate the mirror through its owner.

**Exclusions [S].** No Reader contract or payload change. No release re-cut beyond what (a), (b), (e) or (f) requires. No new evidence family. No canon change.

**Expected outcome [S].** Wheel installs admit the release. Every production 404 uses the governed envelope. Every test file runs in CI or is retired; the classifier fails closed on unregistered `tools/qa/` sources; documentation-only PRs start no CI run. Attestation builds on Debian. The (e) defects are fixed or retired, and dev `/reader` is never served without an explicit dev, test or local `APP_ENV`. `--allow-prod-vendor` works as PF05 §7.1.11 states. The catalog lists every served route. `.env.example`, `docs/ADAPTER_009.md` and `ARCHITECTURE.md` match the code.

**Size note [S].** (c) is the largest part and may justify its own phase block; (f) is the largest new part.

### Item 6 — Open code PRs only after the implementation is pushed; review the code that missed it

**Need [S].**
- (a) Codex security review runs when a PR opens. PR04 #467 and PR06 #501 were opened holding only a plan, so their code got no security review. PR05 #492 and PR06a #508 were reviewed on their first push only.
- (b) No one has since reviewed the code those four PRs merged (RA-09), including the production Reader route and the compat HTTP handler.

**Warrant [S].** Public HTTP routes merged without a security review of the code. PF20 §2.26.7 keeps this as a stated limitation.

**Affected surfaces [S].** code: for (b), the code merged by #467, #492, #501 and #508, as review input, with fixes only where a confirmed finding needs one. governance: for (a), the PR-30 prompt text (GCFPE). canon: none.

**Constraints and risks [S].** (a) none material. (b) may find defects that enlarge the work; findings in code a later PR already changed are reviewed against `main`.

**Lead Developer finding [S].** Valid; not already satisfied (the 2026-10-09 GCFPE round #598 did not include (a); no review of the (b) code is recorded). (a) not naturally CRD lane; (b) CRD lane.

**Proposed bounded scope [S; not approved].** (a) PR-30 opens the code PR with the implementation commit, and plan successors go in a separate PR. (b) One security review of the code merged by #467, #492, #501 and #508, read on `main`; each confirmed finding fixed in this CRD or routed with a reason.

**Exclusions [S].** No change to the review tooling. No re-review of accepted PR lineages beyond security.

**Expected outcome [S].** Every code PR is security-reviewed on code, and the HDE-EPIC040 code that missed review has had one.

### Item 7 — Read-only pre-push / pre-plan check script

**Need [S].** Each PR session re-derives by hand, or skips, the base-versus-head sweep of tests no lane runs, CI-lane impact, release membership and the `ci.yml` replay. PR04 had 4 failed CI runs out of 19.

**Warrant [S].** Fewer paid CI failures and fewer rescopes caused by unchecked lane or release impact.

**Affected surfaces [S].** code: a new script and its test (location set by the Specification). canon: none.

**Constraints and risks [S].** Duplicates CI logic and must track `ci.yml` changes. Overlaps item 5(c), so it is sequenced after it.

**Lead Developer finding [S].** Valid; not already satisfied (no such script at `d86b8850`); CRD lane (tooling).

**Proposed bounded scope [S; not approved].** One read-only script with its own test that sets up a Python 3.12 venv; prints the current PF10 path and hash; shows CI lanes and release membership for given paths; runs the uncovered-test sweep in a throwaway copy; replays `ci.yml` in a throwaway worktree.

**Exclusions [S].** No writes. No SessionStart hook.

**Expected outcome [S].** One command gives a session its pre-push picture.

### Item 8 — Close-pack writer cannot produce a canon close report

**Need [S].** `tools/qa/generate_epic_close_pack.py`, the only governed close-pack writer, is limited by `schemas/epic_close_candidate_source.v1.json` [V: present, `additionalProperties: false`, `epic_id` pattern `^HDE-EPIC[0-9]{3}$`] to four fixed headings, ten fixed sentences and five fixed nonclaims. It cannot write: the acceptance section with `SATISFIED` / `NOT SATISFIED` (Change Process Guide §3.5.2.1); the deferrals and later-drain statements (HDE Schemas & Artifacts close-pack artifacts); the QA RCA summary; the heading `QA Rails — Open/Close (Final PR)` (Glow QA Guide). The close workflow's same-run evidence has no admitted home once the QA manifest is final.

Additional verified fact [V]: the schema's `epic_id` pattern admits only Epic identities, so a CRD identity such as `HDE-CRD-0002` cannot be a close-pack subject under the current schema. The Specification decides whether CRD support is in scope.

**Warrant [S].** No epic or CRD can complete the ordinary Close Gate; HDE-EPIC040 needed exceptional closure for this reason.

**Affected surfaces [S].** code: `tools/qa/generate_epic_close_pack.py`, its schema, `tests/qa/test_generate_epic_close_pack.py`, possibly `tools/evidence/update_evidence_index.py`. canon: Change Process Guide §3.5.2 and §0.7, the HDE Schemas & Artifacts close-pack rules, and Glow QA Guide close-pack truthfulness; an ADR is required (PF30.1 §1 "A canon-changing CRD MUST have an approved accompanying ADR").

**Constraints and risks [S].** HDE-EPIC039 made the generic writer neutral on purpose, so this reverses a design choice and must weigh that rationale. It touches the release-sanity and close-validation lanes.

**Lead Developer finding [S].** Valid; not already satisfied (schema unchanged at `d86b8850`); CRD lane (cross-change tooling with a canon ADR).

**Proposed bounded scope [S; not approved].** A governed, feedback-free writer that produces a canon-conforming close report and manifest from tracked inputs, and an admitted home for close-workflow run evidence that does not reopen an approved QA manifest.

**Exclusions [S].** No new evidence families, no acceptance tokens, no retroactive close pack for HDE-EPIC040.

**Expected outcome [S].** A closing change can pass the ordinary Close Gate.

**Sequencing [S].** Needed before the next epic or CRD closes, not before one starts. HDE-CRD-0002's own closure depends on it unless the Specification provides otherwise.

## 5. Reviewed and left out by the source (2026-10-12)

Carried so the Specification can confirm the exclusions, not to reopen them [S]:

| Item | Reason |
| --- | --- |
| O-P07-07 (`VERIFY.sh` imports the dead harness) | Covered by O-P07-03 |
| O-P07-08 (PF10 storage defect) | Moot after the PF10 v13.5 rewrite |
| O-P07-09 (`AGENTS.md` cites PF10 by section) | Resolved at `d86b8850` |
| RA-11, RA-15 | Information only; no requirement established |
| RA-16 (repository root clutter) | Low value; repository owner |
| Final-check window atomicity | Disclosed limitation, not a promise |
| O-OPS01-02, CC-4 | Prompt or process work for GCFPE-MGMT-10 |
| CC-3, CC-5, CC-6 | Canon wording for their owners |
| Live Gate readiness and live Reader success | PF09.7 HDE-COAG003.8 and HDE-COAG003.9 |

## 6. Cross-cutting dependencies

- Release re-cut coupling: (a), (b), O-P07-01 and possibly (f) may each change release members; one re-cut and one admission-pin update would serve them together [S].
- Item 7 after item 5(c) [S].
- Item 8 before HDE-CRD-0002's own ordinary close [S, inferred from its sequencing note].
- Item 8's ADR precedes its canon drainage [S].
- Item 6(a)'s lane decision (CRD or GCFPE-MGMT-10) [S].

## 7. Unknowns and open points for the Specification

None blocks authoring.

| # | Point | Owner |
| --- | --- | --- |
| U-1 | Current count of test files in no CI lane (source gives 129 at PR05 and asks for a recount on `main`) | Isis (Specification) / IA |
| U-2 | Production `APP_ENV=prod` is a Product Owner report, not an observation | Product Owner; no change needed to author |
| U-3 | Whether item 6(a) is delivered inside the CRD or routed to GCFPE-MGMT-10 | Isis, decided in the Specification |
| U-4 | Whether item 8 extends the close-pack schema to CRD identities | Isis, decided in the Specification |
| U-5 | Phase structure: the source suggests (c) may justify its own phase block | Isis |
| U-6 | DD-11's code side was not re-checked by the source | IA (Implementation Audit) |
| U-7 | Canon tension for format resolution: PF06 §0.1 places the CRD Specification format in HDE CRD Records; PF04 §9.1.1 calls HDE CRD Records historical/reference only and retires the "CRD Plan". PF30.1 §4.1 and §7 still use "CRD Plan" language. CF-C-20 resolves the format from canon and cites it. | Isis (format resolution); canon owner if a change is needed |

## 8. Sanitization note

The source's intake findings, proposed bounded scope and recommendations are carried as source-stated proposals. Nothing in this kickoff approves them. No raw embedded instructions, implementation plans or historical approval language are passed as authority.

## 9. TypeSafe reading for the receiving session (CF-C-20)

Action sent (v6): "Author the first version of a new CRD Specification from a complete kickoff covering four items with about twenty defect parts across packaging, HTTP adapter, CI coverage, CLI, security review and close-pack tooling, at scope and outcome level, with one item needing a canon ADR; no code is written and no live provider run occurs, and an independent reviewer approves or redlines it before any planning."

- TypeSafe cell: Opus 5.5 at extra high
- Rung probabilities: score 3.26, confidence 0.51: low 0.00, medium 0.02, high 0.20, extra high 0.27, max 0.50, ultracode 0.01; twelve cells (computed): Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.11, Opus 5.5 at extra high 0.14, Opus 5.5 at max 0.27, Opus 5.5 at ultracode 0.01, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.01, Fable 5.1 at high 0.09, Fable 5.1 at extra high 0.13, Fable 5.1 at max 0.23, Fable 5.1 at ultracode 0.00. Flags: model near tie
- Model probabilities: Fable 5.1 0.47, Opus 5.5 0.53, confidence 0.06
- Detail: v6 sent 2026-10-12T18:51:26Z; HTTP 200 in 0.86 s; 4188 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: model near tie.
- Nathan's pick: not stated.

Surface advice: run CF-C-20 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access. It needs repository read access and writes only to `docs/ephemeral/`. It must read the CRD format owner from `docs/pfcanon/` on `main`.

## 10. Canon relied on

Read on `main` at `483b9f7`:
- PF04-Canon-HDE-Governance v2.8.7: §9.1, "Epic and CRD change lanes"; §9.1.1 Change authority and exact-artifact lineage, including the role table rows "Epic/CRD class selection" and "Class-specific kickoff".
- PF06-Canon-Change-Process-Guide v2.5.4: §0.1, the "Specification format authority" paragraph.
- PF30.1-Canon-HDE-CRD-Records v0.9: §1 Purpose & scope; §2 Authority, ownership & boundaries; §3.1 CRD identifier governance; §3.2 Record lifecycle; §4.1 Initial registration; §7 "Intake, analysis & bounded scope".
- PF10-HDE-Build-Notes: searched for kickoff rules; none found.

In-flight documents: `docs/ephemeral/HDE-CRD-0002-change-class-selection-v1.0.md`; `docs/ephemeral/HDE-CRD-0002-candidate-item-briefs-v1.2.md`.
