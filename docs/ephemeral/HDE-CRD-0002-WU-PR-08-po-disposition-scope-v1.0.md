---
artifact_type: PRODUCT_OWNER_DISPOSITION
artifact_id: HDE-CRD-0002-WU-PR-08-PO-DISPOSITION-SCOPE
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
decision_owner: Nathan / Product Owner
decided_at: 2026-10-21, in the Isis Lead Developer session below (recorded 2026-10-21T17:32:34Z)
recorded_by: Isis, continuing Lead Developer for HDE-CRD-0002, session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 (recorder and drafter; the decision is the Product Owner's)
decides: decision 1 returned to the Product Owner by docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-work-unit-lineage-review-v1.0.md §12 (blob 6025be6ddbe38979c721b2f05932deea363e6af3), namely WU-PR-08's business case and the S01 real-input fact
approved_base_affected: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480), unchanged by this record
repository_head_read: origin/main 0dfaeebf
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (blob 840a57fdd2216479ca27451f7935ec984aceee04); addenda 2.11 and 2.12 read in full; 2.13 to 2.15 searched for WU-PR-08, S01 and 1.4.0 (no decision on them)
pf10_addendum_created: none
---

# HDE-CRD-0002 — Product Owner disposition: WU-PR-08 scope and business case (v1.0)

## 1. Product Owner's words (verbatim)

> "approve option 1, give me the handoff"

Option 1 is the first of three options put to the Product Owner in the same session. It is reproduced in §2 without change.

## 2. Decision: OPTION 1

| Part | Decision |
| :- | :- |
| S01 (every release member in the wheel) | **Removed** from HDE-CRD-0002's scope, through a Specification delta |
| `1.4.0` version cut | **Dropped.** The release stays on the refreshed `1.3.0`; no new admission version or timestamp is set |
| S16 and S17 | **Kept** as a reduced WU-PR-08 |
| Specification text forcing new admission pins | **Changed** in the same delta: a member change forces a manifest refresh at the current version, not new admission pins |

### Basis

Both facts were checked on `main` at `0dfaeebf`.

- **S01 has no real input** (addendum 2.11 rules 1 and 4):
  - The production start command is `Procfile`: `web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …`. Running Python with `-m` puts the working directory, the checkout at `/app`, first on the import path, so the engine loads its code and release members from the checkout whatever the build installs.
  - CI installs in editable mode (`-e .`), and the attestation builder installs its wheel only to exercise the `hdctl` entry point (Audit §6 S01, "Current behavior").
  - Because nothing runs the engine from an installed copy, the Railway build command no longer bears on S01, and the S01 real-input fact (addendum 2.12, decision 4) is no longer needed.
  - Limit: the live Railway start command is unverified (Glow Infrastructure §10). If it ever ran without the checkout, admission would refuse to start (`MISSING_FILE`), a loud failure rather than a silent one.
- **The `1.4.0` label has no reader:**
  - `/internal/version` returns `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256` and `release_id`, with no version field (`engine/runtime/identity.py` `_FIELDS`; `adapter/http_reader.py` `internal_version`).
  - Release identity is `release_id` (`AGENTS.md`, "Release identity").
  - The version appears only in `catalog/manifest.json`, the admission constants and change records.
  - One label naming different bytes after same-version refreshes has precedent with no recorded incident: `1.0.0` stayed the same across #403, #404 and #467.
- **Cost avoided.** The `1.4.0` cut was most of WU-PR-08's planned work: about ten evidence families regenerated in a fixed order, plus pinned-test rewrites (Plan v1.1 §10 and risk R-2).

### Business case for the reduced WU-PR-08 (addendum 2.11 rule 1)

| Field | Content |
| :- | :- |
| Beneficiary | Whoever configures an HD Engine environment from `.env.example` (S16), and operators and agents who use `docs/ADAPTER_009.md` for health checks and local access (S17) |
| Evidence | **S16:** `.env.example` holds only `HD_API_BASE_URL`, `HD_API_KEY` and `HD_API_SECRET`, while `engine/providers/vendor_http_hdapi.py` requires `GEO_API_KEY`. **S17:** `docs/ADAPTER_009.md` lines 46–51 describe `/internal/readyz` as a resolver, catalog and `compute_pair` smoke returning a typed 503 on failure. `adapter/wsgi.py` lines 47–51 return `{"ok": true, "schema": "v1"}` with 200 unconditionally, and `adapter/factory.py`, the production app, registers no `/internal/readyz`. Lines 122 and 138 give `127.0.0.1:5000`, while the runners bind `$PORT` (default 8000). All observed on `main` at `0dfaeebf` |
| Benefit | An environment set up from the template is complete; a health check or local call built from the document hits a real route and port |
| Measure | `.env.example` has a `GEO_API_KEY` entry (S16's acceptance intent), and each statement S17 corrects matches the code on the merged head, checked in WU-PR-08's lineage review (PR-40) |
| Cost ceiling | 1 PR, 2 sessions, 1 day from PR-10 to merge; past that, the unit returns to the Product Owner. Neither change touches a release member, so there is no manifest refresh and no full-validation CI run |

The carried items for S17 named in addendum 2.9 stay with WU-PR-08: the loopback bind statements and OBS-P4-5.

## 3. Approved Specification passages the decision affects

These are source facts for the reviewer's correction assessment, not redlines. Thoth decides the bounded correction (CF-C-30, `APPROVED_BASE_CORRECTION_ASSESSMENT`), and Isis authors the delta (CF-C-40). Text is quoted from `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`; "§" names its section headings.

| # | Location | Current text (quoted or summarized) | Affected by |
| :- | :- | :- | :- |
| A-1 | Requirements, S01 row | "Package every release member with the distribution" / "A regular wheel install admits the complete release outside a source checkout" | S01 removal |
| A-2 | Intake: Bounded scope; Expected outcome; Lead Developer finding | "S01 to S22" | S01 removal |
| A-3 | Constraints → Release members | "Those of S01 (`pyproject.toml`) and S02 (`adapter/factory.py`) are not. Any requirement whose implementation changes a release member forces a manifest re-cut and new admission pins; … The change converges on one coherent re-cut after the member-changing work lands." | Both parts |
| A-4 | Exclusions, bullet 2 | "No release re-cut beyond what the in-scope requirements require." | `1.4.0` drop (consistency check) |
| A-5 | Phase blocks: Coagulation row | Purpose "Durable packaging and environment discipline: S01, S16, S17"; dependency "S01 converges with the release re-cut"; boundary "S01, S16 and S17 hold on `main`" | Both parts |
| A-6 | Phase blocks: the "Recommended ordering" line, and the Conjunction and Fermentation rows' release re-cut dependencies | "the release re-cut after all member-changing work lands" | `1.4.0` drop |
| A-7 | Canon, QA & Build Notes posture → Production-affecting Live QA minimum, the S01 row | "Production-affecting, outside the functional-feature scope … S01 … Packaging of the deployed service" | S01 removal |
| A-8 | Intake: Affected surfaces; Why warranted | "packaging metadata"; any S01-specific wording | S01 removal (if present) |
| A-9 | Kickoff open points and Material-change history | No change expected; the delta adds its own history row on approval | — |

**Later route (not decided here).** After the Specification delta is approved, Implementation Plan v1.1 needs an approved-base change through IA-30 (`APPROVED_BASE_CHANGE_ASSESSMENT`) and IA-40. Plan passages that name S01 or the `1.4.0` cut:
- §3 "Release-identity spine";
- §6 (the S01 row, and "version bump `1.4.0` in WU-PR-08");
- §7 WU-PR-08 (title, scope, deliverables, acceptance) and WU-OPS-01 success criteria ("the `1.4.0` `release_id`");
- §10;
- §11 R-2 and R-6;
- §12;
- WU-DOC-01's AGENTS.md "release `1.4.0`" line.

## 4. What does not change

- S16 and S17 scope and acceptance intents.
- Every other requirement, exclusion and constraint.
- WU-PR-08's place in the order: after WU-PR-07, before WU-DOC-01.
- The same-version refreshes already made by earlier units.
- AQ-1 and the canon-conflict register as carried.
- Option A's measure for WU-PR-06: WU-PR-08's PR-40 records it.

## 5. Next stage

| Field | Value |
| :- | :- |
| Prompt | CF-C-30 — Review and Approve CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb8121af3bf2249c6d6ca8) |
| Mode | `APPROVED_BASE_CORRECTION_ASSESSMENT` |
| Receiving role | Thoth, the HDE-CRD-0002 Specification reviewer (reviews v1.0 and v1.1, session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum) |
| Inputs | The immutable approved Specification and this Product Owner scope decision |
| Return | `CORRECTION_REDLINE` to CF-C-40 (Isis), or a terminal result |

### TypeSafe reading for the receiving session (CF-C-30)

Action sent (v8.2): "Assess, as the independent Specification reviewer, a Product Owner scope decision against an already approved 22-requirement CRD Specification: remove one packaging requirement and change one release constraint so the change keeps its current release version instead of a new one, then return a bounded correction redline (or a terminal result) naming each affected passage of the approved Specification. It is a read-only assessment of one Specification and one decision record against canon: no delta is written here, no code and no live run occur, and the Specification author writes the delta for the same reviewer's later review."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.85 (confidence 0.73); rung probabilities low 0.00, medium 0.28, high 0.60, extra high 0.11, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.80, Sonnet 5.5 0.16, Haiku 5.5 0.01 (confidence 0.73). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.008, Fable 5.1 at high 0.018, Fable 5.1 at extra high 0.003, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.224, Opus 5.5 at high 0.480, Opus 5.5 at extra high 0.088, Opus 5.5 at max 0.008, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.045, Sonnet 5.5 at high 0.096, Sonnet 5.5 at extra high 0.018, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.003, Haiku 5.5 at high 0.006, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T17:32:34Z. Flags: none.
- **Detail:** v8.2 sent 2026-10-21T17:32:34Z; HTTP 200 in 0.64 s; 5456 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
- **Nathan's pick for CF-C-30:** not stated.
- **Notion row:** not written (addendum 2.1).

**Surface advice:** run CF-C-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the Thoth reviewer lineage. It reads from `main`:
- this record;
- the approved Specification;
- review v1.1;
- `docs/pfcanon/`, including PF10 addenda 2.11 and 2.12;
- for the basis facts: `Procfile`, `engine/runtime/identity.py`, `adapter/http_reader.py` (`internal_version`), `.env.example` and `docs/ADAPTER_009.md`.

It writes only its assessment under `docs/ephemeral/`, and needs no live vendor, production or database access. This record's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `0dfaeebf`.

- **PF10-HDE-Build-Notes v13.6.6:**
  - addendum 2.11, read in full (rule 1 business-case fields; rule 4 real inputs; rule 3 gates; "Epic, task, and status effects", which names WU-PR-08's open S01 fact);
  - addendum 2.12, read in full (decision 4, the S01 real-input fact before WU-PR-08's PR-10);
  - addendum 2.9 (S17's carried items), read in the passages cited;
  - addendum 2.1 (TypeSafe reading; no Notion row);
  - addenda 2.13 to 2.15, searched for WU-PR-08, S01 and `1.4.0`, with no decision found.
- **PF04-Canon-HDE-Governance v2.8.7 §9.1.1 and §9.1.2:** an approved Specification is changed only through its own correction route, and the IA may not reinterpret it; Product Owner dispositions govern within their scope.
- **CF-C-30 — Review and Approve CRD Specification — 100926.1:** `APPROVED_BASE_CORRECTION_ASSESSMENT` inputs ("an actual authorized Product Owner product/scope decision") and `CORRECTION_REDLINE` routing to CF-C-40.
- **PF07-Canon-Glow-Infrastructure v2.3.3 §10:** the live Railway start setting is unverified, cited through Audit §5.4; not re-read here.
- **`AGENTS.md`:** "Release identity" (`release_id` from `catalog/manifest.json`; intentional cuts through the cutter).

**In-flight documents read:**
- `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-work-unit-lineage-review-v1.0.md` §12;
- `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (the passages in §3);
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (the passages in §3's later route);
- `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md` §5.4 and §6 S01, S16, S17, read earlier in this session.

**Repository facts read on `main` at `0dfaeebf`:** `Procfile`; `engine/runtime/identity.py` `_FIELDS`; `adapter/http_reader.py` `internal_version`; `adapter/wsgi.py` lines 47–51; `adapter/factory.py` (no `readyz`); `.env.example`; `docs/ADAPTER_009.md` lines 6, 22, 46–51, 122, 138; `catalog/manifest.json` history.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / Product Owner disposition / WU-PR-08 scope and business case |
| change | CRD HDE-CRD-0002 |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis, Lead Developer, recording a Product Owner decision returned by PR-40 (WU-PR-07) |
| capture time | 2026-10-21T17:32:34Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
