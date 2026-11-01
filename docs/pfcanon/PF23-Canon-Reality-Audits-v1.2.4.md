# 0\) Front Matter

**Title:** PF23-Canon-Reality-Audits

**Version:** v1.2.4

**Status:** Canon

**Effective date:** 2026-11-01

**Last Update Gate:** HDE-EPIC041

---

**Intent & scope \[Required-Now\]**

These audits are **Codex review passes run by the Product Owner at the closure of each epic** to compare what actually shipped (code, evidence, repo layout) with what PF-Canon and the epic plan said should exist. Their purpose is to:

* Highlight any **gaps between reality and expectation** (missing evidence, drift from PF docs, unrecorded behavior, or unclosed issues).

* Produce a **historical record** of what was found at close (including any “unknowns” that become future work, PF10 addenda, PF20 issues, or PF09 updates).

* Feed back into canon and planning **after** the epic is closed, without blocking day-to-day execution.

These audits:

* Are **PO-only responsibilities**; they are **not** part of any agent plan, CRD, or implementation workflow.

* Do **not** introduce new acceptance gates for agents and must **not** be treated as tasks or subtasks in PF09 or PF20.

* Are **archived for history** as standalone artifacts (for example, under `audit/codex/...`) so future epics and doc updates can refer to them when reconciling drift.

Agents may **read** these audits as context when planning future work, but they do **not** schedule, trigger, or satisfy them.

# 1\) **HDE Repository Reality Audit — `amthorn78/glow-hdengine-v2` at `2ddf63d`**

**Status: PARTIAL.** This is a read-only, factual record of the repository at one pinned commit, compared with PF23 v1.2.3's audit at `0adce9d`. It is not QA evidence, not acceptance and not a gate (PF04 §2.0.18; PF06 §0.6.1); it creates no task. §4 explains why the status is PARTIAL rather than COMPLETE: the scale of PF23's own evidence catalog (682 `E-` ids, 84 `N-` ids, 52 `RA-` ids, 25 `FND-` ids, and a 2,316-row canon-claims comparison) could not all be re-opened line-by-line in this session; the method used for the bulk of them is stated plainly in §3 and is itself a legitimate read-only re-confirmation (file-blob equality), not a judgement substitute.

## **1\. Audit Snapshot Metadata**

| Field | Value |
| :---- | :---- |
| Repository and commit | `amthorn78/glow-hdengine-v2` at `2ddf63dc68bdff0803a053d68c3cee0cfcca9998`, the head of `main` when pinned (subject "PF10", committed 2026-11-01T17:13:59Z) |
| Baseline | PF23 v1.2.3 §1's audited commit `0adce9d9c7c8437e92d2f9c3a99eb98daeeca35b` (2026-10-26T17:49:24Z). 70 commits separate baseline and pin. |
| Observation | Pinned and inspected 2026-11-01T17:45:59Z (session clock, UTC) |
| Method | Static, read-only inspection: `git log/show/diff/ls-tree/ls-files/grep`, `grep`, `find`, `sed -n`, `wc`, and `python3 -I` for parsing only. No repository script, validator, generator, test or build was executed. One read-only GitHub API call for CI was attempted and returned HTTP 403 (anonymous rate limit); no authenticated credential was available in this session, so hosted CI for the pinned commit is recorded as Unknown (§10). |
| Tools | `git` 2.43.0; host Python 3.11.17 for parsing only |
| Environment | Recorded by name and SET/UNSET only. This session's commands ran with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` set explicitly for each command. `APP_ENV`, `DATABASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL` and `ENGINE_ENV` are all UNSET in this session (checked by name at observation time). No vendor or database call was made or was possible to make from this environment. |
| Earlier audits | PF23 v1.2.3 (the audit at `0adce9d`) was used as comparison evidence only. No section, table or count was copied from it; every fact below was freshly observed at the pinned commit. |

**Canon relied on:** PF23-Canon-Reality-Audits (the whole §0 and §1, read in full, governing this audit's form and limits); PF04 HDE Governance §2.0.18 (drift stub form); PF06 Change Process Guide §0.6.1 (PF23 update is Nathan's manual action); AGENTS.md (read in full, including the HDE-EPIC041 and HDE-CRD-0002 posture sections, which this audit treats as the changed set's governing context, not as code to execute). HDE Build Notes (PF10) was searched for the surfaces in the changed set (`SEPA006`, `EPIC041`, `chart_orchestration`, `charts/pure`) at the pinned commit's tracked copy, `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.9.md`, and its §2.3–§2.10 and the addenda they reference were read.

**Coverage.** A section is COMPLETE only when every unit of its population was read in full; PARTIAL names what was not.

| § | Population | Status |
| :---- | :---- | :---- |
| 1 | Pin, tool versions, environment names | COMPLETE |
| 2 | Top-level repo map, recomputed fresh at the pin | COMPLETE |
| 3 | Packaging and entrypoint files (unchanged blobs, re-confirmed) | COMPLETE |
| 4 | Changed engine/adapter surface (`engine/charts/*`, `adapter/chart_orchestration.py`) read in full; unchanged engine modules re-confirmed by blob equality only, not re-opened | PARTIAL |
| 5 | Adapter/HTTP surfaces: no file in this area is in the changed set; re-confirmed by blob equality only | PARTIAL |
| 6 | Presenter/Emitter: no file in this area changed; re-confirmed by blob equality only | PARTIAL |
| 7 | CLI surfaces: `engine/cli/main.py` unchanged; `scripts/make_compat_determinism_artifacts.py` changed and read in full | PARTIAL |
| 8 | Vendor seam / BodyGraph storage: unchanged; re-confirmed by blob equality only | PARTIAL |
| 9 | Evidence, indices, catalogs: `tools/evidence/update_evidence_index.py`, `schemas/close_candidate_source.v2.json`, `tools/qa/generate_epic_close_pack.py`, `tools/ci/prepush_check.py`, `ci/checks/classify_ci_changes.py` read for their actual diffs; the Human Index/Mirror content change confirmed structurally, not replayed | PARTIAL |
| 10 | Tests, QA harness, CI/checks: new and changed test files read; hosted CI read attempt returned 403 (Unknown); no test was executed | PARTIAL |
| 11 | Flows and call chains: only the chart-load flow (`adapter/chart_orchestration.py` → `engine/charts/pure.py`) traced in full; other flows re-confirmed by blob equality only | PARTIAL |
| 12 | Drift and comparisons: every PF23 `RA-`/`FND-` id given one status (§12.1); every PF23 `E-`/`N-` id given one status by the blob-equality method (§12.2); not independently re-derived from first principles | PARTIAL |
| 13 | Negative claims used in this audit | COMPLETE |

**Limitations (stated plainly, not hidden in a footnote):**

* No route, database or vendor probe was made or attempted. Runtime, deployed and production state are Unknown.  
* Hosted CI for the pinned commit could not be read: the GitHub API returned HTTP 403 ("API rate limit exceeded") for an unauthenticated request, and no credential was available in this session. This is an access limit, not a decision to skip a required read. See §10.  
* PF23 v1.2.3's own evidence catalog (682 `E-` ids, 84 `N-` ids) was not re-opened line-by-line. Instead, each id's cited repository path(s) were parsed from its citation text, and that path's git blob was compared between baseline and pin (`git diff --name-only <baseline>..<pin>` plus `git ls-tree` existence checks). A path identical at both commits re-confirms the id's underlying file content is unchanged, which is the "re-confirm by file blob" method PF23's own Rule 2 names; a path that changed, was added or was deleted is flagged and, where tractable in this session, was actually opened and checked (§12.2 and its "REVIEW" items). An id whose citation does not resolve to a concrete repository path (a producer scratch-script invocation, or a whole-tree aggregate command) is recorded Unknown, "not re-run: read-only audit; aggregate recomputed fresh where it affects this audit's own §2–§11 facts".  
* PF23's §12.1.B compares 2,316 individual canon claims of PF02, PF05, PF10, PF12 and PF14 against the repository at baseline. All five of those documents changed version between baseline and pin (PF02 v2.4.6→v2.4.7; PF05 v2.5.3→v2.5.4, renamed; PF10 v13.8.6→v13.9.9 across several intermediate versions; PF12 v2.9.6→v2.9.7; PF14 v3.5.8→v3.5.9, implied by HDE-CRD-0002/EPIC041 drainage work, not independently diffed line-for-line in this session). None of those 2,316 claim-rows could be re-derived against the new text in this session; §12.1 records this as a fact about the comparison's currency, not as a re-run of the comparison.

## **2\. Top-level Repo Map**

* EA-02-001 `git ls-tree -r 2ddf63d | wc -l` → 6,175 tracked entries: 6,038 `100644`, 135 `100755`, 2 `120000` symlinks. PF23 recorded 8,374 at baseline (8,235/137/2). The drop (−2,199) is almost entirely the `docs/ephemeral/` pruning below.  
* EA-02-002 `git ls-tree 2ddf63d | wc -l` → 97 root entries: 57 files, 40 directories (same directory count as PF23's 40; same lowercase-name set, re-confirmed — FND-008 persists).  
* EA-02-003 Root directory tracked-file counts recomputed fresh (`git ls-tree -r <dir> | wc -l` per root dir). Notable deltas from PF23's baseline counts: `docs/` 2,567 → 310; `audit/` 3,196 → 3,248 (+52, the new `audit/qa/hde-epic041/` and `audit/EPIC-041_*` family); `tests/` 255 → 260 (+5: the four HDE-SEPA006.1 chart tests plus `tests/scripts/test_make_compat_determinism_artifacts.py`); `adapter/` 17 → 18 (+1: `adapter/chart_orchestration.py`); `engine/` 102 (unchanged count: `engine/charts/loader.py` removed, `engine/charts/pure.py` added). All other root directories unchanged in tracked-file count (re-confirmed; not individually re-enumerated).  
* EA-02-004 `docs/` now holds 18 second-level directories (same set of names as PF23) but 310 files, not 2,567. By directory: `ephemeral` 60 (was 2,319; −2,259), `pfcanon` 34 (unchanged count; 13 files renamed/version-bumped inside it, §2.1 below), `graph` 59 (was 58), `prompt_ecosystem_management` 33 (was 32), `schemas` 20 (unchanged), `evidence` 9 (unchanged), `design` 8 (unchanged), `plans` 8 (unchanged), `run` 6 (unchanged), `adr` 5 (unchanged), `crd` 3 (unchanged), `acceptance` 2, `architecture` 2, `changes` 2, `contracts` 2, `qa` 2, `ops` 1, `server` 1 (unchanged), plus 53 files directly under `docs/` (unchanged count).  
* EA-02-005 The `docs/ephemeral/` reduction is almost entirely deletions: the baseline-to-pin diff shows 2,323 `D` (deleted) paths, 102 `M`, 124 `A` and 13 `R` (renames) across the whole repository; the great majority of the `D` rows are under `docs/ephemeral/`.  
* EA-02-006 The two symlinks are unchanged: `docs/ENDPOINTS_CATALOG.json` → `../artifacts/audit/ENDPOINTS_CATALOG.json`, and `artifacts/ops/internal_version/body_get.json.sha256` → `body_get.sha256` (both paths present and unchanged blobs at the pin; FND-010 persists).  
* EA-02-007 344 zero-byte tracked files (same count as PF23). The root zero-byte files PF23 named — `Run`, `assert`, `import`, `temp_run.err`, `temp_run.out` — are each still tracked at size 0 (FND-012 persists; RA-16 persists).  
* EA-02-008 `NONASCII_OR_SPACE`: 46 tracked paths contain a space (was 50); 0 contain a non-ASCII byte (was 1). The one non-ASCII path PF23 named, `docs/ephemeral/GCFPE Direct-Handoff and Runtime Artifact Operating Procedure v3.0.0 — 20260913.md`, is deleted at the pin (confirmed by `git ls-tree 2ddf63d -- 'docs/ephemeral/GCFPE Direct-Handoff*'` returning nothing); it is the only root-cause of the non-ASCII-path and part of the space-path drop.  
* EA-02-009 `ci/checks/classify_ci_changes.py`'s prefix lists: `_HISTORICAL_PREFIXES` now at `:164–172` (was `:156–165`, content identical, 8 entries, same values); `_DOCUMENTATION_PREFIXES` now at `:179–188` (was `:171–180`, content identical, same 8 entries: `docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/`). Only line numbers moved, by \+8, because a new 9-line block (`_CLOSE_STAGE_TESTS`) was inserted above them and one line was replaced (§9 below).

### **2.1 `docs/pfcanon/` renames in the changed set**

13 files in `docs/pfcanon/` were renamed with a version bump between baseline and pin (git detected as renames, similarity 89–99%): PF02 (v2.4.6→v2.4.7), PF04 (v2.8.7→v2.8.8), PF05 (v2.5.3→v2.5.4, sourced from a `docs/ephemeral/gtwpe/...` working file), PF06 (v2.5.4→v2.5.5, from the same `gtwpe` tree), PF07 (v2.3.3→v2.3.4, same), PF09.3 (v1.1.7→v1.1.8), PF09.4 (v1.3.1→v1.3.2), PF09.7 (v1.1.8→v1.1.9), PF12 (v2.9.6→v2.9.7, from `gtwpe`), PF14 (v3.5.8→v3.5.9, from `gtwpe`), PF19 (v3.0.6→v3.0.7), PF27 (v2.0.4→v2.0.6, from `gtwpe`), PF29 (v1.0.2→v1.0.3). PF10 itself is not a rename in this diff but moved from `v13.8.6` (PF23's audited version) to `v13.9.9` at the pin — a larger change spanning the 70 intervening commits, not just this one diff — and shrank from 692,581 bytes / \~3,641 lines to 277,111 bytes / 1,326 lines (`wc -lc`), ending with the same authored `<eof>` marker PF23 recorded (`tail -c 7` → `\<eof>`). This is consistent with drainage of PF10 addenda into the permanent registers named above (§12.1, RA-18).

## **3\. Packaging and Entrypoints**

* `pyproject.toml`, `requirements.txt`, `requirements-dev.txt`, `Procfile` are all absent from the changed-file list (`git diff --name-only <baseline>..<pin>`); their blobs are unchanged. PF23's packaging facts (name `glow-hdengine`, version `0.0.0`, `dependencies = []`; one console script `hdctl = "engine.cli.main:cli"`; `requirements.txt` listing `psycopg[binary]`, `Flask<3.0`, `gunicorn<22`, `jsonschema==4.23.0`) are re-confirmed by blob equality, not re-opened.  
* `scripts/make_compat_determinism_artifacts.py` changed. It now imports `from adapter.chart_orchestration import load_chart` (previously `from engine.charts.loader import load_chart`) and still exits 2 with `"compat_public not implemented"` before any chart call reaches `engine.compat.compute.compat_public`, which is still absent — AGENTS.md's "current posture" claim is confirmed current at the pin (EA-03-001).  
* No `Dockerfile*`, `setup.py` or `setup.cfg` is tracked at the pin (`git ls-files | grep -iE '(^|/)(dockerfile[^/]*|setup\.(py|cfg))$'` → 0 hits; NA-03-001). Not re-run: wheel build (forbidden; not executed).

## **4\. Engine Modules (changed surface)**

* `engine/charts/loader.py` is deleted (confirmed absent: `git show 2ddf63d:engine/charts/loader.py` errors; not in `git ls-tree -r 2ddf63d`). `engine/charts/pure.py` is new, 101 lines, read in full: it imports only `re`, `unicodedata` and `typing` (stdlib), performs no time, environment, network, provider, logging or filesystem access, and exposes `ChartInputError`, `BirthInputs`, `validate_birth_inputs` and `normalize_chart`. Its own calendar/time-shape validation duplicates the acceptance of `engine.util.input_validators.parse_time_hh_mm` "without strptime's locale and TZ reads" (its own comment, line \~49).  
* `adapter/chart_orchestration.py` is new, 113 lines, read in full: it owns the `SAFE_MODE` read, both clocks (`datetime.now`, `time.perf_counter`), the correlation id, the pinned ISO-3166/IANA list reads (anchored to the repo root via `Path(__file__).resolve().parents[1]`, not the working directory), a fixture-chart return, and one keys-only JSON log line per call with `"route": "loader.load_chart"` as a label string (not a module path — AGENTS.md's own caution that this string is a label, not a live import, is accurate: `grep -rn 'engine.charts.loader'` outside `.audit_src/` and the deliberately-named guard test/CI-classifier entry finds nothing; NA-04-001).  
* `tests/charts/test_chart_loader_import_guard.py` (new) asserts the module path is absent and fails if any import of `engine.charts.loader` returns; `tests/charts/test_chart_pure_purity.py` and `tests/charts/test_chart_pure_interface.py` (new) target `engine/charts/pure.py`; `tests/adapter/test_chart_orchestration.py` (new) targets the adapter entry. These four tests were read for their assertions, not executed (forbidden).  
* `git grep -n 'engine\.charts\.loader' -- '*.py'` at the pin finds 10 hits, all under `.audit_src/` (an archived, non-live copy) and inside the guard test's own literal strings; none in a live `engine/`, `adapter/`, `scripts/` or `tools/` module (EA-04-001). This confirms AGENTS.md's HDE-EPIC041 posture claim: "no shim" and no live caller of the retired module.  
* All other `engine/` modules PF23 names (`engine/core/`, `engine/magic10/`, `engine/compat/compute.py`, `engine/bodygraph/`, `engine/sampler/core.py`, `engine/config/registry_loader.py`) are absent from the changed-file list; their blobs are unchanged, and their PF23 facts are re-confirmed by blob equality only, not re-opened line by line in this session.  
* `catalog/manifest.json` and `catalog/manifest.json.path_proof.txt` are both absent from the changed-file list; the mismatch PF23 recorded (RA-20261026-10: path-proof records `size_bytes: 1981`/`sha256: dbf89997…` for a 5,881-byte, differently-hashed manifest) persists unchanged (confirmed by reading `catalog/manifest.json.path_proof.txt` at the pin: same two values).

## **5\. Adapter / HTTP Surfaces**

No file under `adapter/` other than the new `adapter/chart_orchestration.py` (§4) is in the changed-file list. `adapter/http_reader.py`, `adapter/wsgi.py`, `adapter/factory.py`, `adapter/etag_core.py`, `adapter/app.py` and `adapter/gunicorn.conf.py` are all unchanged blobs. PF23's Reader, compat-guard, endpoint-catalog and server-configuration facts are re-confirmed by blob equality only; this audit did not re-open or re-derive them. `scripts/qa/dev_sampler_healthcheck.py`, `scripts/demo_mvp.sh`, `scripts/start_web.sh`, `run_flask.py` and `run_flask_dev.sh` are likewise unchanged.

## **6\. Presenter / Emitter**

No file under `presenter/` or `engine/stable/` (the serializer/canon module PF23 cites) is in the changed-file list. PF23's emitter/serializer facts are re-confirmed by blob equality only.

## **7\. CLI Surfaces**

`engine/cli/main.py` (961 lines in PF23) is absent from the changed-file list; unchanged. `scripts/make_compat_determinism_artifacts.py` changed (§3). No `hdctl` help run was executed (forbidden; `hdctl` is not installed or invoked in this session).

## **8\. Vendor Seam & BodyGraph Storage**

No file under `engine/bodygraph/`, `engine/db/`, `migrations/` or `sql/` is in the changed-file list. PF23's vendor-client, DBAccess, mapped-cache and migrations facts are re-confirmed by blob equality only.

## **9\. Evidence, Indices, Catalogs**

* `schemas/close_candidate_source.v2.json` changed substantially (full diff read): the v1-style `plan_path`/`requirements_binding`/`qa_plan_binding`/`qa_report_binding` fields are replaced by a `planning_records` object (`specification`, `implementation_plan`, `qa_plan`, `qa_report`), plus new top-level `requirement_ids`, `qa_checks` and `qa_verdict` fields; `register`\+`heading` replaces `binding`\+`heading` for one acceptance-path shape; two new `anyOf`/`oneOf` branches allow `evidence_records` as an alternative to `evidence_bindings`/`binding`; two new pattern exclusions forbid a causal pointer or causal text under `docs/ephemeral/` or `docs/pfcanon/`; `ti_id` now also accepts `ISSUE-EPIC###-TI-##`. The schema's own description states the reason: "No causal input lies under docs/ephemeral/ … or docs/pfcanon/ …: the change's requirement IDs, QA plan checks and their criteria, and QA verdict are recorded here … never read."  
* `tools/evidence/update_evidence_index.py` changed (+348 lines net, full diff not reproduced here; not executed). `tools/qa/generate_epic_close_pack.py` changed (+360/−modified lines; not executed). Both are consistent with the new v2 schema fields above and with the second close pack the repository now carries (`audit/EPIC-041_close_report.md`, `audit/EPIC-041_MANIFEST.json`, `audit/EPIC-041_close_candidate_source.json`, all new, read for presence only — not validated, since validation would require running the writer or its `--check`, which this audit does not do).  
* `audit/HDE-CRD-0002_MANIFEST.json`, `..._close_report.md` and `..._close_candidate_source.json` are all modified (not newly created) at the pin, consistent with AGENTS.md's "HDE-CRD-0002 refreshed the manifest in place" posture.  
* `tools/ci/prepush_check.py` changed by 6 lines: `compute_coverage` now also unions `classifier._CLOSE_STAGE_TESTS` into its reported test roots, with the comment "A close-stage test runs when its owners change, never as full validation."  
* `ci/checks/classify_ci_changes.py` changed: a new `_CLOSE_STAGE_TESTS = ("tests/qa/test_generate_epic_close_pack.py",)` and `_CLOSE_STAGE_TEST_OWNERS` mapping move that one test out of `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` (removed from that tuple) and into a new owner-gated path keyed on `.github/workflows/epic-closeout-validation.yml`; four new `_PRODUCT_TEST_OWNER_PATHS` entries register the HDE-EPIC041 chart-separation files and their owning tests (`engine/charts/pure.py`, `adapter/chart_orchestration.py`, `engine/charts/loader.py` → the import-guard test, `scripts/make_compat_determinism_artifacts.py`); `_full_validation_test_targets` now excludes `_CLOSE_STAGE_TESTS`; `changed_test_targets` now also calls the new `_close_stage_owner_targets`. The `_HISTORICAL_PREFIXES`/`_DOCUMENTATION_PREFIXES`/`_DOCUMENT_SUFFIXES`/`_DOCUMENT_PATHS`/`_HISTORICAL_BACKUP_PATHS` constants are unchanged in content (only shifted by \+8 lines; confirmed by direct read, §2 and §9 above).  
* `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` (+ their `.sha256`/`.path_proof.txt` siblings) are modified at the pin, consistent with the new HDE-EPIC041 evidence family being indexed. This audit did not replay `update_evidence_index.py --check` (forbidden) and so cannot state whether the Index and Mirror are currently self-consistent; that is Unknown, "not run: read-only audit".

## **10\. Tests, QA Harness, CI/Checks**

* `find tests -name 'test_*.py' | wc -l` → 220 at the pin (root-tree count for all of `tests/` is 260 tracked entries, including non-`test_*` files, `__init__.py`, `retired_tests.md` and path-proof companions). PF23 recorded 215 test files at baseline; 5 new files are the HDE-SEPA006.1/.2 chart tests plus `tests/scripts/test_make_compat_determinism_artifacts.py`.  
* `.github/workflows/` holds `ci.yml` and `epic-closeout-validation.yml`, both unchanged blobs at the pin.  
* **Hosted CI: Unknown.** `curl https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/2ddf63d.../status` (and `/check-runs`) each returned HTTP 403, `"API rate limit exceeded for <IP>. … Authenticated requests get a higher rate limit."` No GitHub credential was present in this session's environment. This audit therefore cannot state the hosted `ci` run's conclusion for the pinned commit from this session; `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.9.md` §2.4 records an exact-head CI success for an earlier HDE-EPIC041 commit (`8200d1fb`, run `40774524113`, "all seven lanes … true with outcome success … CI\_APPLICABILITY\_AND\_EXACT\_HEAD\_OK") and §2.10 records Isis closing HDE-EPIC041 at 2026-11-01T16:39Z — 34 minutes before the pinned commit's timestamp — but neither of those PF10 entries names the pinned commit `2ddf63d` itself, so this audit does not attribute that CI result to the pin. **Reason recorded: "not established — GitHub API read blocked by anonymous rate limit; no credential available in this session."**  
* No pytest install, pytest run, `hdctl` help run or any other executable check was performed, per the rules governing this audit.

## **11\. Flows & Call Chains**

Only the chart-load flow was traced in full, because it is the one flow in the changed set: a caller (`scripts/make_compat_determinism_artifacts.py`, or a test) calls `adapter.chart_orchestration.load_chart(**kwargs)`, which reads `SAFE_MODE`, builds a correlation id, validates argument shape, calls `engine.charts.pure.validate_birth_inputs` (pure) with the pinned ISO/IANA lists it has itself read from `artifacts/constants/`, then `engine.charts.pure.normalize_chart` on a fixture chart dict, and finally emits one keys-only JSON log line with `"route": "loader.load_chart"`, `"provider": "fixtures"`, `"source": "default"`. No network, database or vendor call occurs anywhere in this path (confirmed by reading both files in full; neither imports `socket`, `urllib`, `psycopg`, `engine.db` or `engine.bodygraph.vendor_client`). All other flows PF23 traces (Reader request, showcompat, bg:resolve, conjunction) touch no file in the changed set; they are re-confirmed by blob equality only, not re-traced.

## **12\. Drift and Reality vs Expectations**

### **12.1 PF23 `RA-`/`FND-` ids: one status each**

Method: for each PF23 `RA-`/`FND-` id, every PF23 `E-`/`N-` id it cites was looked up in the §12.2 blob-equality classification. Where every cited id's file is unchanged ("Same"), the row is **Persistent** (or **Resolved**/**Unverifiable** if PF23 itself already recorded that status and nothing in the changed set touches it). Where a cited id's file changed, was added or removed, the row was actually opened and re-checked in this session (listed as "reviewed" below); 16 of 76 rows needed this.

Comparison-list size: 76 (18 `RA-01`…`RA-18`; 32 `RA-20261026-01`…`-32`; 1 bundled entry `RA-20261026-33to39` for PF23's §12.1.B per-document canon-claim-count summary, which this audit did not re-derive, see §1 Limitations; 25 `FND-001`…`FND-025`).

| Id | PF23 status | This audit's status | Basis |
| :---- | :---- | :---- | :---- |
| RA-01 | Aligned/Persistent | Persistent | `catalog/manifest.json`, `engine/config/registry_loader.py` unchanged blobs |
| RA-02 | Aligned/Persistent | Persistent | `adapter/http_reader.py` unchanged blob |
| RA-03 | Aligned/Persistent | Persistent (narrower claim) | Evidence tool blobs mostly unchanged; `update_evidence_index.py` changed, so the "all rc 0" claim specifically is **Unverifiable this pass** (not re-run) |
| RA-04 | Drift, carried/Persistent | Persistent | Packaging files unchanged; wheel not rebuilt (forbidden) |
| RA-05 | Resolved | Persistent-resolved | `adapter/factory.py`, `adapter/http_reader.py` unchanged blobs |
| RA-06 | Partial/Changed | Persistent | `adapter/http_reader.py` unchanged blob |
| RA-07 | Drift, carried/Resolved | Persistent-resolved | `engine/cli/main.py` unchanged; `.audit_src/` copy still the only `app.getattr` hit |
| RA-08 | Informational/Changed | **Reviewed — Changed** | Test-file count moved 215→220 (`test_*.py`); the underlying claim (not all files named by a fixed lane/roster) was not re-derived from the CI classifier (`ci/checks/classify_ci_changes.py` changed; new owner entries registered for the 5 new test files, confirmed by diff read, §9) |
| RA-09 | Unverifiable | Unverifiable | No new PF10 or security-review record was read for this; unchanged |
| RA-10 | Unverifiable | Unverifiable | No database probe made, as before |
| RA-11 | Persistent | Persistent | `engine/cli/main.py`, `engine/stable/sercanon.py` unchanged |
| RA-12 | Resolved | Persistent-resolved | `.github/workflows/ci.yml` unchanged blob |
| RA-13 | Resolved | Persistent-resolved | `ci/checks/check_mirror_schema.sh` unchanged; AGENTS.md diff (10 lines, read in full) does not touch its mirror-schema wording |
| RA-14 | Changed/Persistent | **Reviewed — Persistent** | `ci/checks/classify_ci_changes.py`'s `dev/reader_harness/app.py` → `{"product"}` mapping is unchanged content, only its line number moved (266→274, confirmed by direct read); `.audit_src/dev/reader_harness/app.py` is still the only tracked copy |
| RA-15 | Partial | **Reviewed — Persistent** | `_HISTORICAL_BACKUP_PATHS` in the changed `ci/checks/classify_ci_changes.py` still lists the same 6 entries and still omits `scripts/hdctl.clean.py` (confirmed by direct read) |
| RA-16 | Persistent/informational | Persistent | Zero-byte/scratch root files all still present at size 0 (§2) |
| RA-17 | Resolved | **Reviewed — Persistent-resolved** | PF10 is now `v13.9.9` (not `v13.8.6`), 1,326 lines / 277,111 bytes, still ends with the authored `\<eof>` marker (`tail -c 7`); no truncation found |
| RA-18 | Changed (pending) | **Reviewed — Resolved** | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md`, `PF05-...-v2.5.4.md` and `PF12-...-v2.9.7.md` each now name C040-06/-07/-08 with delivered, decided content (direct read, multiple lines each); PF10 v13.9.9 no longer carries that content as "pending drainage" language. Canon drainage that PF23 recorded as an open question appears complete in the currently-tracked canon text. |
| RA-20261026-01 … \-05, \-07, \-09, \-11 … \-13, \-16 … \-24, \-26 … \-32 | (as recorded) | Persistent | None of their cited files are in the changed set (confirmed programmatically and spot-read; see §12.2) |
| RA-20261026-06 | Drift | Unverifiable | Hosted CI for the pin could not be read (§10); the cited PF10 version (`v13.8.6`) is itself superseded (§2.1), so the comparison's source text has moved |
| RA-20261026-08 | Aligned | **Reviewed — Changed** | `engine/charts/loader.py` is deleted; its SAFE\_MODE read, `time.perf_counter` timing, provider resolution and file logging are replaced by `adapter/chart_orchestration.py` (SAFE\_MODE read, timing, keys-only stdout/log-sink line — no file write) and `engine/charts/pure.py` (no I/O at all) — see §4 |
| RA-20261026-10 | Drift | **Reviewed — Persistent** | `catalog/manifest.json` and its `.path_proof.txt` are both unchanged blobs; the same size/hash mismatch persists |
| RA-20261026-14 | Drift | **Reviewed — Persistent** | See RA-14 above (same fact, this audit's own numbering is PF23's own duplicate citation of it) |
| RA-20261026-15 | Partial | **Reviewed — Persistent** | See RA-15 above |
| RA-20261026-25 | Drift | **Reviewed — Persistent** | `tools/evidence/run_sanity_pipeline.py` (the file naming stage 11\) is unchanged; its stage-11 name and its call to `update_evidence_index.py --check` are both still present, confirmed by direct read, even though `update_evidence_index.py` itself changed substantially |
| RA-20261026-33to39 | (per-document canon-claim counts) | **Unverifiable (not re-derived)** | The five compared documents all changed version (§2.1); re-deriving the 2,316-claim comparison against the new text was not attempted this session (§1 Limitations) |
| FND-001 … FND-013, FND-018, FND-020, FND-021, FND-023 … FND-025 | (as recorded) | Persistent (or already-Resolved, held) | None of their cited files are in the changed set |
| FND-014, FND-015 | Persistent (presence only) | Persistent | `tools/qa/qa_harness.py` unchanged blob; `tests/evidence/test_evidence_index_missing_state.py` changed, but the presence-only claim (a truthful-compatibility-claims helper exists) does not depend on that test's content |
| FND-016 | Persistent (presence only) | **Reviewed — Persistent** | `AGENTS.md` (modified, still present), `docs/ADAPTER_009.md` (modified, still present), `docs/acceptance/http_transport_evidence.md` and `docs/qa_harness_pattern.md` (both unchanged, confirmed tracked at the pin) |
| FND-017 | Resolved | **Reviewed — Persistent-resolved** | `docs/ADAPTER_009.md` at the pin still contains no occurrence of `body_not_allowed` (`grep -c` → 0\) and one occurrence of `invalid_json` |
| FND-019 | Resolved in PF19 v3.0.5 | **Reviewed — Persistent-resolved** | PF19 is now `v3.0.7` (renamed); its line 4262 (was 4253\) still reads "A changed, different or unavailable SHA alone must never block progression …" |
| FND-022 | Persistent | **Reviewed — Changed** | Same basis as RA-20261026-08: the file this id describes no longer exists |

Status counts: Persistent (or persistent-resolved) 65, Changed 3 (RA-08 partially, RA-20261026-08, FND-022 — all three the same chart-separation fact), Unverifiable 7 (RA-09, RA-10, RA-20261026-06, RA-20261026-33to39, and the narrowed parts of RA-03/RA-08), Resolved (newly, beyond what PF23 already held) 1 (RA-18). No id is New (every id in this list is PF23's own) and none is recorded Not found (every `RA-`/`FND-` id's claim text could still be evaluated, even where Unverifiable).

### **12.2 PF23 `E-`/`N-` item table**

**Method** (stated once; applied uniformly): for each of PF23's 682 `E-` ids (Evidence list) and 84 `N-` ids (Negative-Claim appendix), this audit parsed the repository-relative path(s) named in its citation text. A path's git blob was compared between the baseline commit and the pin:

* both commits have the path, unchanged blob → **Same**;  
* both have the path, blob differs, OR the path exists only at the pin → **Changed**;  
* the path existed at baseline and is absent at the pin → **Not found**;  
* no concrete repository path could be parsed from the citation (a producer scratch-script invocation such as `{SCRATCH}/scripts/s2_map.py`, or a whole-tree aggregate `git grep`/`wc` command with no single named file) → **Unknown**, reason "aggregate or scratch-tool citation; not re-run (read-only audit)". Where such an aggregate affects this audit's own §2–§11 facts, the aggregate was recomputed fresh there (for example `TRACKED_TOTAL`, `ROOT_DIRS`, `ZERO_BYTE`, `NONASCII_OR_SPACE` in §2) rather than left Unknown twice.

A citation naming more than one path is **Changed** if any one of its paths is Changed/Not found/absent-at-baseline, even if others are Same; this is a conservative "needs re-review" signal, not a claim that the fact itself is false. Of the "Changed" rows, this audit actually opened and manually re-checked every one whose changed file plausibly affects a load-bearing fact (listed in §§2–11 and §12.1 above, under "Reviewed"); the remainder are recorded Changed without further manual re-reading, because their citation path's mere presence in the diff (for example a `docs/pfcanon/` rename, or a `tests/retired_tests.md` edit unrelated to the cited line) does not, on its own, establish which specific fact changed, and re-deriving it would require re-opening PF23's full working citation, which this session's scope does not reach for all 682+84 ids.

Comparison-list size: 766 (682 `E-` ids \+ 84 `N-` ids). The table below has exactly 766 data rows.

Status counts: Same 512 (490 `E-` \+ 22 `N-`), Changed 43 (35 `E-` \+ 8 `N-`), Not found 35 (26 `E-` \+ 9 `N-`), Unknown 176 (131 `E-` \+ 45 `N-`).

The full 766-row table is in **Appendix A** below, generated by the method above and spot-checked against direct reads for every row discussed in §§2–11 and §12.1.

## **13\. Negative-Claim Proof Appendix (this audit's own)**

| Id | Claim | Pattern | Tool | Scope | Command | Result |  |  |  |  |  |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| NA-03-001 | No tracked `Dockerfile*`, `setup.py` or `setup.cfg` at the pin | \`(^ | /)(dockerfile\[^/\]\* | setup.(py | cfg))\$\` | \`git ls-files \\ | grep \-iE\` | all tracked paths | \`git ls-files \\ | grep \-iE '(^ | /)(dockerfile\[^/\]\* | setup.(py\\ | cfg))\$' \\ | wc \-l\` | `0` |
| NA-04-001 | No live (non-`.audit_src`, non-guard-test-literal) module imports `engine.charts.loader` | `engine\.charts\.loader` | `git grep -n` | tracked `*.py` | `git grep -n 'engine\.charts\.loader' -- '*.py'` | 10 hits, all under `.audit_src/` or inside `tests/charts/test_chart_loader_import_guard.py`'s own literal strings |  |  |  |  |  |  |  |  |  |
| NA-02-001 | No non-ASCII byte remains in any tracked path | `[^\x00-\x7F]` | `grep -P` on `git ls-tree -r --name-only -z` | all tracked paths | \`git ls-tree \-r \--name-only \-z 2ddf63d \\ | tr '\\0' '\\n' \\ | grep \-P '\[^\\x00-\\x7F\]' \\ | wc \-l\` | `0` |  |  |  |  |  |  |
| NA-02-002 | `engine/charts/loader.py` is absent from the tracked tree at the pin | `engine/charts/loader.py` | `git ls-tree -r --name-only` | all tracked paths | \`git ls-tree \-r \--name-only 2ddf63d \\ | grep \-x engine/charts/loader.py\` | `0` (no match) |  |  |  |  |  |  |  |  |

## **Appendix A — PF23 `E-`/`N-` item table (766 rows)**

Columns: PF23 id; repository path(s) this audit parsed from its citation (may be empty); status by the §12.2 method.

| PF23 id | Paths cited (parsed) | Status |
| :---- | :---- | :---- |
| E-02-001 | — | Unknown |
| E-02-002 | — | Unknown |
| E-02-003 | — | Unknown |
| E-02-004 | — | Unknown |
| E-02-005 | artifacts/audit/ENDPOINTS\_CATALOG.json, artifacts/ops/internal\_version/body\_get.json.sha256, docs/ENDPOINTS\_CATALOG.json | Same |
| E-02-006 | — | Unknown |
| E-02-007 | — | Unknown |
| E-02-008 | — | Unknown |
| E-02-009 | — | Unknown |
| E-02-010 | — | Unknown |
| E-02-011 | — | Unknown |
| E-02-012 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-013 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-014 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-015 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-016 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-017 | docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md | Not found |
| E-02-018 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-020 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-021 | AGENTS.md, docs/ADAPTER\_009.md, docs/acceptance/http\_transport\_evidence.md, docs/qa\_harness\_pattern.md | Changed |
| E-02-022 | AGENTS.md | Changed |
| E-02-932 | — | Unknown |
| E-02-933 | — | Unknown |
| E-02-934 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md, docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md | Changed |
| E-02-2012 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-2013 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-2052 | — | Unknown |
| E-02-2053 | docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md | Same |
| E-02-2058 | docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md | Same |
| E-02-2059 | docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md | Same |
| E-02-2060 | — | Unknown |
| E-02-2061 | docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md | Same |
| E-02-2062 | docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md, docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md | Changed |
| E-02-2801 | audit\_src/dev/reader\_harness/app.py | Unknown |
| E-02-2812 | docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md | Not found |
| E-02-2813 | docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md | Not found |
| E-02-2816 | — | Unknown |
| E-02-2818 | — | Unknown |
| E-02-2823 | — | Unknown |
| E-02-3203 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-3204 | docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md | Unknown |
| E-02-3625 | — | Unknown |
| E-02-3680 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-3684 | docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md | Same |
| E-02-3685 | docs/pfcanon/PF09.2-Canon-HDE-Build-Checklist-Dissolution-v1.2.4.md | Same |
| E-02-3699 | docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md | Same |
| E-02-3703 | ci/checks/check\_bridge\_consistency.py, lists/K-14-1556.txt, tests/unit/test\_check\_bridge\_consistency.py, tools/evidence/generate\_db\_bridge\_parity.py | Unknown |
| E-02-3704 | ci/checks/check\_bridge\_consistency.py | Unknown |
| E-02-3705 | tests/unit/test\_check\_bridge\_consistency.py | Unknown |
| E-02-4020 | \_artifacts/primary.log, \_sets/primary.log | Unknown |
| E-02-4040 | artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json, artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json | Same |
| E-02-4864 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-4865 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-02-4866 | docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md | Not found |
| E-02-4868 | docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.0.md | Not found |
| E-03-002 | — | Unknown |
| E-03-014 | pyproject.toml | Same |
| E-03-015 | pyproject.toml | Same |
| E-03-019 | pyproject.toml | Same |
| E-03-021 | pyproject.toml | Same |
| E-03-024 | pyproject.toml | Same |
| E-03-026 | pyproject.toml | Same |
| E-03-027 | pyproject.toml | Same |
| E-03-029 | engine/cli/main.py | Same |
| E-03-040 | requirements.txt | Same |
| E-03-041 | requirements.txt | Same |
| E-03-042 | requirements.txt | Same |
| E-03-043 | requirements.txt | Same |
| E-03-045 | requirements-dev.txt | Same |
| E-03-047 | requirements-dev.txt | Same |
| E-03-048 | requirements-dev.txt | Same |
| E-03-049 | requirements-dev.txt | Same |
| E-03-054 | Procfile | Same |
| E-03-055 | Procfile | Same |
| E-03-061 | adapter/gunicorn.conf.py | Same |
| E-03-062 | adapter/gunicorn.conf.py | Same |
| E-03-063 | adapter/gunicorn.conf.py | Same |
| E-03-064 | adapter/gunicorn.conf.py | Same |
| E-03-078 | adapter/factory.py | Same |
| E-03-080 | adapter/factory.py | Same |
| E-03-090 | adapter/http\_reader.py | Same |
| E-03-091 | adapter/http\_reader.py | Same |
| E-03-092 | adapter/http\_reader.py | Same |
| E-03-094 | adapter/http\_reader.py | Same |
| E-03-095 | adapter/http\_reader.py | Same |
| E-03-096 | adapter/app.py | Same |
| E-03-111 | scripts/start\_web.sh | Same |
| E-03-114 | — | Unknown |
| E-03-116 | — | Unknown |
| E-03-117 | — | Unknown |
| E-03-119 | — | Unknown |
| E-03-121 | — | Unknown |
| E-03-122 | — | Unknown |
| E-03-135 | audit\_src/dev/reader\_harness/app.py | Unknown |
| E-03-147 | ci/checks/classify\_ci\_changes.py, dev/reader\_harness/app.py | Changed |
| E-03-201 | adapter/app.py, scripts/demo\_mvp.sh | Same |
| E-03-216 | scripts/dev\_start\_reader.sh | Same |
| E-03-363 | scripts/hdctl.backup.py, scripts/hdctl.clean.py, scripts/hdctl.py | Same |
| E-03-393 | ci/checks/classify\_ci\_changes.py | Changed |
| E-03-394 | ci/checks/classify\_ci\_changes.py | Changed |
| E-03-395 | ci/checks/classify\_ci\_changes.py, engine/config/provider\_loader.py | Changed |
| E-03-396 | ci/checks/classify\_ci\_changes.py, engine/serializer/canon.py | Changed |
| E-03-397 | ci/checks/classify\_ci\_changes.py, scripts/card\_close.sh | Changed |
| E-03-398 | ci/checks/classify\_ci\_changes.py, scripts/hdctl.backup.py | Changed |
| E-03-399 | ci/checks/classify\_ci\_changes.py, scripts/hdctl.py | Changed |
| E-03-901 | — | Unknown |
| E-03-902 | catalog/manifest.json | Same |
| E-03-903 | catalog/manifest.json | Same |
| E-03-3602 | adapter/http\_reader.py | Same |
| E-03-3605 | adapter/http\_reader.py | Same |
| E-03-3613 | adapter/http\_reader.py | Same |
| E-03-3614 | adapter/http\_reader.py | Same |
| E-04-019 | engine/core/**init**.py | Same |
| E-04-024 | engine/magic10/**init**.py | Same |
| E-04-049 | engine/config/registry\_loader.py | Same |
| E-04-050 | engine/config/registry\_loader.py | Same |
| E-04-051 | engine/config/registry\_loader.py | Same |
| E-04-055 | engine/config/registry\_loader.py | Same |
| E-04-056 | engine/config/registry\_loader.py | Same |
| E-04-081 | engine/config/registry\_loader.py | Same |
| E-04-082 | engine/config/registry\_loader.py | Same |
| E-04-083 | engine/config/registry\_loader.py | Same |
| E-04-084 | engine/config/registry\_loader.py | Same |
| E-04-089 | engine/config/registry\_loader.py | Same |
| E-04-093 | engine/config/registry\_loader.py | Same |
| E-04-105 | engine/config/registry\_loader.py | Same |
| E-04-106 | engine/config/registry\_loader.py | Same |
| E-04-129 | engine/config/registry\_loader.py, math/thresholds.json | Same |
| E-04-137 | engine/config/registry\_loader.py | Same |
| E-04-143 | engine/config/registry\_loader.py | Same |
| E-04-144 | engine/config/registry\_loader.py | Same |
| E-04-149 | engine/config/registry\_loader.py | Same |
| E-04-150 | engine/config/registry\_loader.py | Same |
| E-04-151 | engine/config/registry\_loader.py | Same |
| E-04-169 | engine/config/registry\_loader.py | Same |
| E-04-173 | engine/config/registry\_loader.py | Same |
| E-04-174 | engine/config/registry\_loader.py | Same |
| E-04-175 | engine/config/registry\_loader.py | Same |
| E-04-177 | engine/core/**init**.py | Same |
| E-04-181 | engine/core/core.py | Same |
| E-04-183 | engine/core/core.py | Same |
| E-04-185 | engine/core/core.py | Same |
| E-04-186 | engine/core/core.py | Same |
| E-04-187 | engine/core/core.py | Same |
| E-04-188 | engine/core/core.py | Same |
| E-04-204 | engine/core/core.py | Same |
| E-04-206 | engine/core/core.py | Same |
| E-04-210 | engine/magic10/calculators.py | Same |
| E-04-211 | engine/magic10/calculators.py | Same |
| E-04-212 | engine/magic10/calculators.py | Same |
| E-04-213 | engine/magic10/calculators.py | Same |
| E-04-232 | engine/magic10/thresholds.py | Same |
| E-04-236 | math/thresholds.json | Same |
| E-04-240 | engine/compat/compute.py | Same |
| E-04-245 | engine/compat/compute.py | Same |
| E-04-247 | engine/compat/compute.py | Same |
| E-04-248 | engine/compat/compute.py | Same |
| E-04-249 | engine/compat/compute.py | Same |
| E-04-250 | engine/compat/compute.py | Same |
| E-04-264 | engine/compat/compute.py | Same |
| E-04-265 | engine/compat/compute.py | Same |
| E-04-266 | engine/compat/compute.py | Same |
| E-04-272 | engine/compat/compute.py | Same |
| E-04-274 | engine/compat/compute.py | Same |
| E-04-277 | engine/compat/compute.py | Same |
| E-04-288 | engine/runtime/public.py | Same |
| E-04-289 | engine/runtime/public.py | Same |
| E-04-290 | engine/runtime/public.py | Same |
| E-04-292 | engine/runtime/public.py | Same |
| E-04-308 | — | Unknown |
| E-04-351 | — | Unknown |
| E-04-369 | engine/charts/loader.py | Not found |
| E-04-414 | tests/core/test\_engine\_core\_purity.py | Same |
| E-04-427 | engine/sampler/core.py | Same |
| E-04-428 | engine/compat/compute.py, tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py | Same |
| E-04-431 | engine/core/core.py | Same |
| E-04-434 | engine/sampler/core.py | Same |
| E-04-437 | engine/bodygraph/**init**.py | Same |
| E-04-438 | engine/bodygraph/resolver.py | Same |
| E-04-439 | engine/bodygraph/resolver.py | Same |
| E-04-440 | engine/bodygraph/vendor\_client.py | Same |
| E-04-441 | engine/bodygraph/vendor\_client.py | Same |
| E-04-511 | catalog/channels\_catalog\_v1.json | Same |
| E-04-533 | catalog/manifest.json.path\_proof.txt | Same |
| E-04-534 | catalog/manifest.json.path\_proof.txt | Same |
| E-04-576 | engine/config/registry\_loader.py | Same |
| E-04-577 | engine/config/registry\_loader.py | Same |
| E-04-578 | engine/config/registry\_loader.py | Same |
| E-04-579 | engine/config/registry\_loader.py | Same |
| E-04-580 | catalog/manifest.json.path\_proof.txt | Same |
| E-04-581 | catalog/manifest.json | Same |
| E-04-652 | schemas/magic10\_compat\_result\_v1.schema.json | Same |
| E-04-653 | schemas/magic10\_mechanics\_v1.schema.json | Same |
| E-04-654 | schemas/magic10\_result\_v1.schema.json | Same |
| E-04-776 | catalog/magic10\_mechanics\_v1.json | Same |
| E-04-779 | — | Unknown |
| E-04-781 | schemas/magic10\_mechanics\_v1.schema.json | Same |
| E-04-787 | — | Unknown |
| E-04-790 | — | Unknown |
| E-04-798 | engine/config/registry\_loader.py | Same |
| E-04-800 | engine/config/registry\_loader.py | Same |
| E-04-801 | engine/config/registry\_loader.py | Same |
| E-04-823 | engine/magic10/signals.py | Same |
| E-04-835 | — | Unknown |
| E-04-901 | engine/core/**init**.py | Same |
| E-04-902 | — | Unknown |
| E-04-903 | engine/core/**init**.py, engine/core/core.py | Same |
| E-04-904 | — | Unknown |
| E-04-905 | — | Unknown |
| E-04-906 | — | Unknown |
| E-04-907 | engine/core/core.py | Same |
| E-04-908 | engine/compat/compute.py | Same |
| E-04-909 | engine/charts/loader.py | Not found |
| E-04-910 | engine/charts/loader.py | Not found |
| E-04-911 | engine/compat/compute.py | Same |
| E-04-912 | engine/compat/compute.py | Same |
| E-04-913 | engine/compat/compute.py | Same |
| E-04-914 | — | Unknown |
| E-04-915 | engine/charts/loader.py | Not found |
| E-04-916 | engine/charts/loader.py | Not found |
| E-04-917 | engine/charts/loader.py | Not found |
| E-04-918 | — | Unknown |
| E-04-919 | scripts/hdctl.backup.py, scripts/hdctl.clean.py | Same |
| E-04-2804 | engine/compat/compute.py | Same |
| E-04-2807 | engine/compat/compute.py | Same |
| E-05-031 | audit\_src/dev/reader\_harness/app.py | Unknown |
| E-05-037 | adapter/factory.py | Same |
| E-05-038 | adapter/http\_reader.py | Same |
| E-05-039 | adapter/http\_reader.py | Same |
| E-05-040 | adapter/http\_reader.py | Same |
| E-05-041 | adapter/http\_reader.py | Same |
| E-05-045 | adapter/wsgi.py | Same |
| E-05-069 | adapter/wsgi.py | Same |
| E-05-070 | adapter/wsgi.py | Same |
| E-05-077 | Procfile | Same |
| E-05-086 | adapter/app.py | Same |
| E-05-118 | engine/http/compat\_handler.py | Same |
| E-05-122 | adapter/http\_reader.py | Same |
| E-05-125 | adapter/http\_reader.py | Same |
| E-05-126 | adapter/http\_reader.py | Same |
| E-05-127 | adapter/http\_reader.py | Same |
| E-05-129 | adapter/http\_reader.py | Same |
| E-05-130 | adapter/http\_reader.py | Same |
| E-05-131 | adapter/http\_reader.py | Same |
| E-05-147 | adapter/http\_reader.py | Same |
| E-05-148 | adapter/http\_reader.py | Same |
| E-05-160 | adapter/http\_reader.py | Same |
| E-05-172 | engine/http/compat\_handler.py | Same |
| E-05-208 | adapter/factory.py | Same |
| E-05-209 | adapter/factory.py | Same |
| E-05-210 | adapter/factory.py | Same |
| E-05-211 | adapter/factory.py | Same |
| E-05-212 | adapter/factory.py | Same |
| E-05-213 | adapter/factory.py | Same |
| E-05-214 | adapter/factory.py | Same |
| E-05-215 | adapter/factory.py | Same |
| E-05-216 | adapter/factory.py | Same |
| E-05-217 | adapter/http\_reader.py | Same |
| E-05-218 | adapter/http\_reader.py | Same |
| E-05-219 | adapter/http\_reader.py | Same |
| E-05-220 | adapter/http\_reader.py | Same |
| E-05-224 | adapter/wsgi.py | Same |
| E-05-225 | adapter/wsgi.py | Same |
| E-05-246 | adapter/http\_reader.py | Same |
| E-05-288 | adapter/http\_reader.py | Same |
| E-05-289 | adapter/http\_reader.py | Same |
| E-05-356 | adapter/wsgi.py | Same |
| E-05-364 | adapter/wsgi.py | Same |
| E-05-389 | adapter/etag\_core.py | Same |
| E-05-393 | adapter/wsgi.py | Same |
| E-05-429 | adapter/wsgi.py | Same |
| E-05-442 | adapter/env\_guard.py | Same |
| E-05-443 | adapter/env\_guard.py | Same |
| E-05-450 | docs/ENDPOINTS\_CATALOG.json | Same |
| E-05-451 | artifacts/audit/ENDPOINTS\_CATALOG.json, docs/ENDPOINTS\_CATALOG.json | Same |
| E-05-457 | — | Unknown |
| E-05-465 | — | Unknown |
| E-05-477 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-478 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-479 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-480 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-481 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-482 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-483 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-484 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-485 | — | Unknown |
| E-05-486 | adapter/http\_reader.py | Same |
| E-05-487 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-488 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-489 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-490 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-491 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-05-501 | adapter/http\_reader.py | Same |
| E-05-502 | adapter/schemas/version\_v1.schema.json | Same |
| E-05-503 | adapter/schemas/version\_v1.schema.json | Same |
| E-05-504 | adapter/http\_reader.py | Same |
| E-05-505 | tests/adapter/test\_jsonschema.py | Same |
| E-05-2804 | adapter/factory.py | Same |
| E-05-2849 | adapter/http\_reader.py | Same |
| E-05-2851 | adapter/http\_reader.py | Same |
| E-05-2852 | adapter/http\_reader.py | Same |
| E-05-2853 | adapter/http\_reader.py | Same |
| E-05-2854 | adapter/http\_reader.py | Same |
| E-05-2877 | adapter/http\_reader.py | Same |
| E-05-3605 | adapter/http\_reader.py | Same |
| E-06-001 | engine/runtime/identity.py | Same |
| E-06-002 | engine/runtime/identity.py | Same |
| E-06-016 | engine/presenter/emitter.py | Same |
| E-06-018 | engine/presenter/emitter.py | Same |
| E-06-020 | engine/presenter/emitter.py | Same |
| E-06-023 | presenter/reader\_v1/emitter.py | Same |
| E-06-024 | presenter/reader\_v1/emitter.py | Same |
| E-06-025 | presenter/reader\_v1/emitter.py | Same |
| E-06-026 | presenter/reader\_v1/emitter.py | Same |
| E-06-027 | presenter/reader\_v1/emitter.py | Same |
| E-06-028 | presenter/reader\_v1/emitter.py | Same |
| E-06-029 | presenter/reader\_v1/emitter.py | Same |
| E-06-055 | presenter/reader\_v1/emitter.py | Same |
| E-06-056 | presenter/reader\_v1/emitter.py | Same |
| E-06-057 | presenter/reader\_v1/emitter.py | Same |
| E-06-058 | presenter/reader\_v1/emitter.py | Same |
| E-06-059 | presenter/reader\_v1/emitter.py | Same |
| E-06-060 | presenter/reader\_v1/emitter.py | Same |
| E-06-061 | presenter/reader\_v1/emitter.py | Same |
| E-06-062 | presenter/reader\_v1/emitter.py | Same |
| E-06-063 | presenter/reader\_v1/emitter.py | Same |
| E-06-065 | presenter/reader\_v1/emitter.py | Same |
| E-06-066 | presenter/reader\_v1/emitter.py | Same |
| E-06-067 | engine/runtime/public.py | Same |
| E-06-068 | engine/runtime/public.py | Same |
| E-06-070 | engine/runtime/public.py | Same |
| E-06-071 | engine/runtime/public.py | Same |
| E-06-072 | engine/runtime/public.py | Same |
| E-06-138 | presenter/json\_canon\_compare.py | Same |
| E-06-166 | engine/cli/main.py | Same |
| E-06-170 | engine/cli/main.py | Same |
| E-06-902 | \_v1/emitter.py | Unknown |
| E-07-030 | engine/cli/main.py | Same |
| E-07-031 | engine/cli/main.py | Same |
| E-07-032 | engine/cli/main.py | Same |
| E-07-053 | engine/cli/main.py | Same |
| E-07-063 | engine/cli/main.py | Same |
| E-07-075 | engine/cli/main.py | Same |
| E-07-141 | engine/cli/main.py | Same |
| E-07-143 | engine/cli/main.py | Same |
| E-07-145 | engine/cli/main.py | Same |
| E-07-147 | engine/cli/main.py | Same |
| E-07-901 | — | Unknown |
| E-07-903 | — | Unknown |
| E-07-2806 | engine/cli/main.py | Same |
| E-07-2807 | engine/cli/main.py | Same |
| E-07-2809 | engine/cli/main.py | Same |
| E-07-2810 | engine/cli/main.py | Same |
| E-07-2836 | engine/cli/main.py | Same |
| E-08-183 | engine/bodygraph/vendor\_client.py | Same |
| E-08-184 | engine/bodygraph/vendor\_client.py | Same |
| E-08-185 | engine/bodygraph/vendor\_client.py | Same |
| E-08-186 | engine/bodygraph/vendor\_client.py | Same |
| E-08-192 | engine/bodygraph/vendor\_client.py | Same |
| E-08-193 | engine/bodygraph/vendor\_client.py | Same |
| E-08-207 | engine/bodygraph/vendor\_client.py | Same |
| E-08-208 | engine/bodygraph/vendor\_client.py | Same |
| E-08-225 | engine/bodygraph/vendor\_client.py | Same |
| E-08-226 | engine/bodygraph/vendor\_client.py | Same |
| E-08-237 | engine/bodygraph/vendor\_client.py | Same |
| E-08-239 | engine/bodygraph/vendor\_client.py | Same |
| E-08-285 | engine/db/adapter.py | Same |
| E-08-286 | engine/db/adapter.py | Same |
| E-08-293 | engine/db/adapter.py | Same |
| E-08-428 | engine/bodygraph/mapped\_cache.py | Same |
| E-08-442 | engine/bodygraph/mapped\_cache.py | Same |
| E-08-455 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-456 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-457 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-460 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-465 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-466 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-468 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-08-641 | engine/bodygraph/ingest.py | Same |
| E-08-642 | engine/bodygraph/vendor\_client.py | Same |
| E-08-643 | engine/bodygraph/vendor\_client.py | Same |
| E-08-644 | engine/bodygraph/vendor\_client.py | Same |
| E-08-1901 | — | Unknown |
| E-08-2002 | engine/bodygraph/vendor\_client.py | Same |
| E-08-2826 | engine/bodygraph/vendor\_client.py | Same |
| E-08-2862 | engine/bodygraph/resolver.py | Same |
| E-08-2863 | engine/bodygraph/resolver.py | Same |
| E-08-2864 | engine/bodygraph/resolver.py | Same |
| E-08-2881 | engine/bodygraph/resolver.py | Same |
| E-08-4004 | engine/db/adapter.py | Same |
| E-08-4005 | engine/db/adapter.py | Same |
| E-09-001 | — | Unknown |
| E-09-002 | — | Unknown |
| E-09-003 | — | Unknown |
| E-09-004 | — | Unknown |
| E-09-005 | — | Unknown |
| E-09-006 | — | Unknown |
| E-09-007 | — | Unknown |
| E-09-008 | — | Unknown |
| E-09-009 | — | Unknown |
| E-09-010 | — | Unknown |
| E-09-011 | — | Unknown |
| E-09-012 | — | Unknown |
| E-09-013 | — | Unknown |
| E-09-020 | — | Unknown |
| E-09-021 | — | Unknown |
| E-09-022 | — | Unknown |
| E-09-023 | — | Unknown |
| E-09-024 | — | Unknown |
| E-09-026 | — | Unknown |
| E-09-029 | — | Unknown |
| E-09-030 | artifacts/db\_bridge/provider\_parity.proof.json, artifacts/release\_id.txt, artifacts/release\_pack\_manifest.json, artifacts/runtime/env\_connectivity.nondev\_failure.json | Same |
| E-09-031 | — | Unknown |
| E-09-032 | — | Unknown |
| E-09-033 | — | Unknown |
| E-09-034 | — | Unknown |
| E-09-035 | docs/evidence/INDEX.json | Changed |
| E-09-036 | docs/evidence/INDEX.json | Changed |
| E-09-037 | catalog/manifest.json | Same |
| E-09-038 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| E-09-039 | artifacts/cards/a3/IDENTITY\_OK.txt, artifacts/cards/a3/IDENTITY\_OK.txt.path\_proof.txt | Same |
| E-09-040 | — | Unknown |
| E-09-041 | — | Unknown |
| E-09-042 | — | Unknown |
| E-09-043 | — | Unknown |
| E-09-044 | — | Unknown |
| E-09-045 | — | Unknown |
| E-09-046 | — | Unknown |
| E-09-047 | — | Unknown |
| E-09-050 | — | Unknown |
| E-09-3202 | — | Unknown |
| E-09-3204 | — | Unknown |
| E-09-3205 | — | Unknown |
| E-09-3628 | tools/evidence/run\_sanity\_pipeline.py, tools/evidence/update\_evidence\_index.py | Changed |
| E-09-3654 | — | Unknown |
| E-09-3776 | audit/EPIC-030\_QA\_RCA.md | Same |
| E-09-4154 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-09-4156 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| E-09-4165 | docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md | Same |
| E-09-4166 | docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md | Same |
| E-09-4168 | docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md | Same |
| E-09-4170 | docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.6.1.md | Same |
| E-09-4280 | artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json | Same |
| E-09-4282 | docs/acceptance\_map\_epic034.json | Same |
| E-09-4283 | docs/acceptance\_map\_epic037.json | Same |
| E-10-009 | \_src/.github/workflows/ci.yml, github/workflows/ci.yml, github/workflows/epic-closeout-validation.yml | Unknown |
| E-10-011 | — | Unknown |
| E-10-012 | — | Unknown |
| E-10-032 | scripts/testpaths\_check.py | Unknown |
| E-10-053 | tests/conftest.py, tests/provider/conftest.py | Same |
| E-10-165 | tests/reader\_v1/test\_cli\_proof.py, tests/retired\_tests.md | Changed |
| E-10-174 | github/workflows/ci.yml | Unknown |
| E-10-175 | github/workflows/ci.yml | Unknown |
| E-10-177 | github/workflows/ci.yml | Unknown |
| E-10-178 | github/workflows/ci.yml | Unknown |
| E-10-180 | github/workflows/ci.yml | Unknown |
| E-10-184 | github/workflows/ci.yml | Unknown |
| E-10-188 | github/workflows/ci.yml | Unknown |
| E-10-191 | github/workflows/ci.yml | Unknown |
| E-10-193 | github/workflows/ci.yml | Unknown |
| E-10-213 | github/workflows/ci.yml | Unknown |
| E-10-228 | github/workflows/ci.yml | Unknown |
| E-10-294 | ci/checks/check\_mirror\_schema.sh, github/workflows/ci.yml | Changed |
| E-10-336 | github/workflows/ci.yml | Unknown |
| E-10-438 | ci/checks/classify\_ci\_changes.py | Changed |
| E-10-442 | ci/checks/classify\_ci\_changes.py | Changed |
| E-10-446 | ci/checks/classify\_ci\_changes.py | Changed |
| E-10-571 | scripts/classifier\_tables.py | Unknown |
| E-10-612 | github/workflows/ci.yml | Unknown |
| E-10-616 | — | Unknown |
| E-10-617 | — | Unknown |
| E-10-619 | scripts/venn.py | Unknown |
| E-10-620 | github/workflows/ci.yml | Unknown |
| E-10-621 | github/workflows/ci.yml | Unknown |
| E-10-622 | scripts/naming\_counts.py | Unknown |
| E-10-626 | — | Unknown |
| E-10-630 | tools/qa/qa\_harness.py | Same |
| E-10-631 | tools/qa/qa\_harness.py | Same |
| E-10-632 | tools/qa/qa\_harness.py | Same |
| E-10-633 | tools/qa/qa\_harness.py | Same |
| E-10-634 | tools/qa/qa\_harness.py | Same |
| E-10-635 | tools/qa/qa\_harness.py | Same |
| E-10-686 | ci/checks/check\_mirror\_schema.sh | Same |
| E-10-901 | — | Unknown |
| E-10-902 | — | Unknown |
| E-10-903 | — | Unknown |
| E-10-904 | — | Unknown |
| E-10-910 | — | Unknown |
| E-10-911 | — | Unknown |
| E-10-912 | — | Unknown |
| E-10-913 | — | Unknown |
| E-10-914 | github/workflows/ci.yml | Unknown |
| E-10-915 | tests/provider/conftest.py | Same |
| E-10-916 | — | Unknown |
| E-10-917 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.5.md, docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Changed |
| E-10-918 | tests/evidence/test\_evidence\_index\_missing\_state.py, tests/qa/test\_generic\_qa\_harness.py, tests/qa/test\_qa\_tool\_ownership.py, tools/qa/qa\_harness.py, tools/qa/step\_log\_header.py | Changed |
| E-10-919 | — | Unknown |
| E-10-2480 | — | Unknown |
| E-10-4003 | tests/retired\_tests.md | Changed |
| E-11-001 | adapter/http\_reader.py | Same |
| E-11-002 | adapter/http\_reader.py | Same |
| E-11-003 | adapter/http\_reader.py | Same |
| E-11-004 | adapter/http\_reader.py | Same |
| E-11-009 | adapter/factory.py | Same |
| E-11-010 | adapter/factory.py | Same |
| E-11-012 | adapter/wsgi.py | Same |
| E-11-013 | adapter/wsgi.py | Same |
| E-11-024 | adapter/http\_reader.py | Same |
| E-11-025 | adapter/http\_reader.py | Same |
| E-11-026 | adapter/http\_reader.py | Same |
| E-11-027 | adapter/http\_reader.py | Same |
| E-11-028 | adapter/http\_reader.py | Same |
| E-11-029 | adapter/http\_reader.py | Same |
| E-11-030 | adapter/http\_reader.py | Same |
| E-11-031 | adapter/http\_reader.py | Same |
| E-11-032 | adapter/http\_reader.py | Same |
| E-11-034 | adapter/http\_reader.py | Same |
| E-11-035 | adapter/http\_reader.py | Same |
| E-11-048 | engine/db/adapter.py | Same |
| E-11-049 | engine/db/adapter.py | Same |
| E-11-105 | engine/config/registry\_loader.py | Same |
| E-11-112 | engine/config/registry\_loader.py | Same |
| E-11-131 | engine/compat/compute.py | Same |
| E-11-132 | engine/core/core.py | Same |
| E-11-151 | engine/core/core.py | Same |
| E-11-186 | engine/runtime/public.py | Same |
| E-11-192 | engine/runtime/public.py | Same |
| E-11-193 | presenter/reader\_v1/emitter.py | Same |
| E-11-194 | presenter/reader\_v1/emitter.py | Same |
| E-11-199 | presenter/reader\_v1/emitter.py | Same |
| E-11-206 | engine/stable/sercanon.py | Same |
| E-11-207 | engine/stable/sercanon.py | Same |
| E-11-208 | engine/stable/sercanon.py | Same |
| E-11-227 | adapter/http\_reader.py | Same |
| E-11-228 | adapter/http\_reader.py | Same |
| E-11-229 | adapter/http\_reader.py | Same |
| E-11-230 | adapter/http\_reader.py | Same |
| E-11-231 | adapter/http\_reader.py | Same |
| E-11-232 | adapter/http\_reader.py | Same |
| E-11-233 | adapter/http\_reader.py | Same |
| E-11-234 | adapter/http\_reader.py | Same |
| E-11-237 | adapter/http\_reader.py | Same |
| E-11-239 | adapter/http\_reader.py | Same |
| E-11-240 | adapter/http\_reader.py | Same |
| E-11-266 | engine/http/compat\_handler.py | Same |
| E-11-267 | adapter/factory.py | Same |
| E-11-268 | adapter/wsgi.py | Same |
| E-11-269 | adapter/http\_reader.py | Same |
| E-11-270 | engine/http/compat\_handler.py | Same |
| E-11-271 | engine/http/compat\_handler.py | Same |
| E-11-274 | engine/http/compat\_handler.py | Same |
| E-11-275 | engine/http/compat\_handler.py | Same |
| E-11-276 | engine/http/compat\_handler.py | Same |
| E-11-281 | engine/http/compat\_handler.py | Same |
| E-11-314 | engine/http/compat\_handler.py | Same |
| E-11-315 | engine/http/compat\_handler.py | Same |
| E-11-317 | engine/http/compat\_handler.py | Same |
| E-11-319 | engine/http/compat\_handler.py | Same |
| E-11-327 | pyproject.toml | Same |
| E-11-328 | engine/cli/main.py | Same |
| E-11-329 | engine/cli/main.py | Same |
| E-11-339 | engine/cli/main.py | Same |
| E-11-388 | engine/cli/main.py | Same |
| E-11-389 | engine/cli/main.py | Same |
| E-11-390 | engine/cli/main.py | Same |
| E-11-440 | engine/bodygraph/resolver.py | Same |
| E-11-470 | engine/cli/main.py | Same |
| E-11-486 | engine/cli/main.py | Same |
| E-11-487 | engine/cli/main.py | Same |
| E-11-488 | engine/cli/main.py | Same |
| E-11-489 | engine/cli/main.py | Same |
| E-11-499 | engine/cli/main.py | Same |
| E-11-533 | engine/cli/main.py | Same |
| E-11-534 | engine/cli/main.py | Same |
| E-11-535 | engine/cli/main.py | Same |
| E-11-563 | adapter/http\_reader.py | Same |
| E-11-564 | adapter/http\_reader.py | Same |
| E-11-565 | adapter/http\_reader.py | Same |
| E-11-619 | engine/cli/main.py | Same |
| E-11-620 | engine/cli/main.py | Same |
| E-11-621 | engine/cli/main.py | Same |
| E-11-622 | engine/cli/main.py | Same |
| E-11-623 | engine/cli/main.py | Same |
| E-11-624 | engine/cli/main.py | Same |
| E-11-639 | engine/cli/main.py | Same |
| E-11-640 | engine/cli/main.py | Same |
| E-11-677 | — | Unknown |
| E-11-678 | engine/bodygraph/resolver.py | Same |
| E-11-679 | engine/bodygraph/resolver.py | Same |
| E-11-688 | engine/bodygraph/resolver.py | Same |
| E-11-689 | engine/bodygraph/resolver.py | Same |
| E-11-741 | engine/bodygraph/mapped\_cache.py | Same |
| E-11-745 | engine/bodygraph/mapped\_cache.py | Same |
| E-11-746 | engine/bodygraph/mapped\_cache.py | Same |
| E-11-782 | tools/evidence/update\_evidence\_index.py | Changed |
| E-11-783 | tools/evidence/update\_evidence\_index.py | Changed |
| E-11-784 | tools/evidence/update\_evidence\_index.py | Changed |
| E-11-901 | tools/config/generate\_config\_artifacts.py | Same |
| E-11-902 | tools/config/generate\_config\_artifacts.py | Same |
| E-11-903 | tools/config/generate\_config\_artifacts.py | Same |
| E-11-935 | tools/config/artifacts.py | Same |
| E-11-941 | tools/config/artifacts.py | Same |
| E-11-954 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-11-955 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-11-956 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-11-967 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| E-11-978 | tools/qa/epic021\_qa.py | Same |
| E-11-979 | tools/qa/epic021\_qa.py | Same |
| E-11-980 | tools/qa/epic021\_qa.py | Same |
| E-11-981 | tools/qa/epic021\_qa.py | Same |
| E-11-982 | tools/qa/epic021\_qa.py | Same |
| E-11-1044 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1045 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1046 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1047 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1048 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1119 | github/workflows/epic-closeout-validation.yml | Unknown |
| E-11-1120 | github/workflows/epic-closeout-validation.yml, tools/qa/generate\_epic\_close\_pack.py | Changed |
| E-11-1121 | github/workflows/epic-closeout-validation.yml | Unknown |
| E-11-1138 | scripts/cut\_release\_manifest.py | Same |
| E-11-1139 | scripts/cut\_release\_manifest.py | Same |
| E-11-1140 | scripts/cut\_release\_manifest.py | Same |
| E-11-1220 | tools/evidence/run\_sanity\_pipeline.py, tools/evidence/update\_evidence\_index.py | Changed |
| E-11-1238 | catalog/manifest.json | Same |
| E-11-1257 | adapter/wsgi.py | Same |
| E-11-1258 | adapter/wsgi.py | Same |
| E-11-1272 | adapter/factory.py | Same |
| E-11-1275 | adapter/factory.py | Same |
| E-11-1277 | adapter/factory.py | Same |
| E-11-1280 | adapter/http\_reader.py | Same |
| E-11-1281 | adapter/http\_reader.py | Same |
| E-11-1295 | adapter/wsgi.py | Same |
| E-11-1296 | adapter/wsgi.py | Same |
| E-11-1298 | adapter/wsgi.py | Same |
| E-11-1300 | adapter/wsgi.py | Same |
| E-11-1371 | adapter/http\_reader.py | Same |
| E-11-1383 | scripts/scratch.py | Same |
| E-11-1393 | scripts/qa/dev\_sampler\_healthcheck.py | Same |
| E-11-1394 | scripts/qa/dev\_sampler\_healthcheck.py | Same |
| E-11-1397 | ci/checks/classify\_ci\_changes.py, dev/reader\_harness/app.py | Changed |
| E-11-1398 | audit\_src/dev/reader\_harness/app.py | Unknown |
| E-11-1399 | tools/evidence/run\_sanity\_pipeline.py | Same |
| E-11-1400 | tools/evidence/run\_sanity\_pipeline.py | Same |
| E-11-1401 | engine/bodygraph/vendor\_client.py | Same |
| E-11-1402 | engine/bodygraph/vendor\_client.py | Same |
| E-11-1403 | engine/runtime/identity.py | Same |
| E-11-3177 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3194 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3202 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3209 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3319 | tools/ops/internal\_version\_artifacts.py | Same |
| E-11-3325 | tools/ops/internal\_version\_artifacts.py | Same |
| E-11-3569 | tools/evidence/update\_evidence\_index.py | Changed |
| E-11-3663 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3664 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3665 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3666 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3765 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3766 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3767 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-3768 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-5203 | tools/evidence/regenerate\_identity\_closure.py | Same |
| E-11-5204 | tools/evidence/regenerate\_identity\_closure.py | Same |
| E-11-5223 | tools/evidence/regenerate\_identity\_closure.py | Same |
| E-11-5224 | tools/evidence/regenerate\_identity\_closure.py | Same |
| E-11-5284 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-5285 | tools/evidence/run\_canonical\_json\_gate.py | Same |
| E-11-5331 | artifacts/bodygraph/source\_selection.snapshot.json, tools/evidence/generate\_bodygraph\_policy\_proofs.py | Same |
| E-11-5332 | schemas/bodygraph\_source\_invariance.run.v2.json, tools/evidence/generate\_bodygraph\_policy\_proofs.py | Same |
| E-11-5333 | schemas/bodygraph\_source\_invariance.summary.v2.json, tools/evidence/generate\_bodygraph\_policy\_proofs.py | Same |
| E-11-5341 | tools/evidence/generate\_v2\_mapped\_cache\_evidence.py | Same |
| E-11-5342 | tools/evidence/generate\_v2\_mapped\_cache\_evidence.py | Same |
| E-11-5343 | schemas/bodygraph\_v2\_mapped\_cache\_manifest.v1.json, tools/evidence/generate\_v2\_mapped\_cache\_evidence.py | Same |
| E-11-6738 | tools/qa/qa\_harness.py | Same |
| E-11-6742 | tools/qa/qa\_harness.py | Same |
| E-11-6813 | tools/qa/qa\_harness.py | Same |
| E-11-6937 | tools/qa/qa\_harness.py | Same |
| E-11-6938 | tools/qa/qa\_harness.py | Same |
| E-11-9293 | tools/evidence/orientation\_demo.py | Same |
| E-11-9294 | tools/evidence/orientation\_demo.py | Same |
| E-11-9295 | tools/evidence/orientation\_demo.py | Same |
| E-11-9296 | tools/evidence/orientation\_demo.py | Same |
| N-02-002 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-03-008 | — | Unknown |
| N-03-010 | — | Unknown |
| N-03-011 | — | Unknown |
| N-03-015 | Procfile | Same |
| N-03-019 | — | Unknown |
| N-03-025 | adapter/app.py, scripts/demo\_mvp.sh | Same |
| N-03-033 | ci/checks/classify\_ci\_changes.py, scripts/hdctl.clean.py | Changed |
| N-04-009 | engine/compat/compute.py | Same |
| N-04-013 | — | Unknown |
| N-04-017 | — | Unknown |
| N-04-023 | engine/core/**init**.py, engine/core/core.py, engine/magic10/**init**.py, engine/magic10/calculators.py, engine/magic10/composite.py, engine/magic10/signals.py, engine/magic10/thresholds.py | Same |
| N-04-024 | engine/bodygraph/gates.py, engine/bodygraph/projection.py, engine/bodygraph/v2\_adapter.py, engine/mech/compare.py, engine/sampler/core.py, engine/stable/sercanon.py | Same |
| N-04-025 | engine/compat/compute.py | Same |
| N-04-501 | catalog/**init**.py, catalog/channels\_catalog\_v1.json, catalog/manifest.json, catalog/manifest.json.path\_proof.txt, catalog/narratives/keys.json.path\_proof.txt, catalog/narratives/keys.json.sha256, catalog/narratives/manifest.json.path\_proof.txt, catalog/narratives/manifest.json.sha256, catalog/narratives/palettes.json.path\_proof.txt, catalog/narratives/palettes.json.sha256, catalog/narratives/suppression\_map.json.path\_proof.txt, catalog/narratives/suppression\_map.json.sha256, catalog/narratives/templates.json.path\_proof.txt, catalog/narratives/templates.json.sha256 | Same |
| N-04-502 | Procfile | Same |
| N-04-547 | catalog/channels\_v1.json | Same |
| N-04-901 | — | Unknown |
| N-04-902 | engine/compat/compute.py, engine/runtime/public.py | Same |
| N-05-012 | — | Unknown |
| N-05-013 | — | Unknown |
| N-05-020 | — | Unknown |
| N-05-029 | — | Unknown |
| N-05-030 | — | Unknown |
| N-05-031 | adapter/wsgi.py | Same |
| N-06-001 | — | Unknown |
| N-06-004 | engine/cli/main.py | Same |
| N-06-005 | engine/cli/main.py | Same |
| N-09-002 | — | Unknown |
| N-09-004 | docs/evidence/INDEX.json | Changed |
| N-09-005 | artifacts/evidence\_index.jsonl | Changed |
| N-09-006 | catalog/manifest.json, docs/evidence/INDEX.json | Changed |
| N-10-021 | github/workflows/ci.yml, github/workflows/epic-closeout-validation.yml | Unknown |
| N-10-023 | github/workflows/ci.yml | Unknown |
| N-11-001 | — | Unknown |
| N-11-008 | — | Unknown |
| N-11-013 | tools/bodygraph/check\_magic10\_gate\_readiness.py | Same |
| N-11-016 | tools/qa/generate\_epic\_close\_pack.py | Changed |
| N-11-028 | — | Unknown |
| N-12-901 | — | Unknown |
| N-12-902 | tests/conftest.py | Same |
| N-12-903 | — | Unknown |
| N-12-904 | engine/runtime/public.py | Same |
| N-12-905 | — | Unknown |
| N-12-906 | — | Unknown |
| N-12-907 | pyproject.toml | Same |
| N-12-908 | — | Unknown |
| N-12-909 | — | Unknown |
| N-12-910 | — | Unknown |
| N-12-911 | engine/cli/main.py, engine/http/compat\_handler.py, engine/runtime/public.py | Same |
| N-12-912 | artifacts/audit/ENDPOINTS\_CATALOG.json | Same |
| N-12-913 | docs/pfcanon/PF10-HDE-Build-Notes-v13.3.8.md, docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Changed |
| N-12-914 | pytest.ini | Same |
| N-12-915 | docs/ADAPTER\_009.md | Changed |
| N-12-916 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-917 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-918 | docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.2.md | Not found |
| N-12-919 | — | Unknown |
| N-12-920 | AGENTS.md | Changed |
| N-12-2005 | — | Unknown |
| N-12-2006 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-2007 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-2803 | — | Unknown |
| N-12-2804 | — | Unknown |
| N-12-2805 | — | Unknown |
| N-12-2806 | — | Unknown |
| N-12-2807 | — | Unknown |
| N-12-2810 | docs/ENDPOINTS\_CATALOG.json | Same |
| N-12-2811 | — | Unknown |
| N-12-2812 | — | Unknown |
| N-12-2815 | engine/cli/main.py | Same |
| N-12-2829 | — | Unknown |
| N-12-3604 | — | Unknown |
| N-12-3606 | — | Unknown |
| N-12-3608 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-3629 | — | Unknown |
| N-12-3635 | — | Unknown |
| N-12-3636 | — | Unknown |
| N-12-3639 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |
| N-12-4002 | — | Unknown |
| N-12-4005 | \_artifacts/primary.log, \_sets/primary.log | Unknown |
| N-12-4007 | — | Unknown |
| N-12-4010 | — | Unknown |
| N-12-4014 | docs/pfcanon/PF10-HDE-Build-Notes-v13.8.6.md | Not found |

## **Evidence list (this audit's own ids)**

| Id | Citation | Excerpt or result |  |  |  |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| EA-02-001 | \`git ls-tree \-r 2ddf63d \\ | wc \-l`; mode counts via`awk '{print \$1}' \\ | sort \\ | uniq \-c\` | `6175`; `100644: 6038, 100755: 135, 120000: 2` |  |
| EA-02-002 | \`git ls-tree 2ddf63d \\ | wc \-l`;`awk '\$2==...'\` split | `97` total; `57 blob, 40 tree` |  |  |  |
| EA-02-003 | \`for d in ; do git ls-tree \-r 2ddf63d \-- "\$d" \\ | wc \-l; done\` | per-directory counts quoted in §2 |  |  |  |
| EA-02-004 | \`for d in ; do git ls-tree \-r 2ddf63d \-- "\$d" \\ | wc \-l; done`;`git ls-tree 2ddf63d \-- docs/ \\ | awk '\$2=="blob"'\` | counts quoted in §2 |  |  |
| EA-02-005 | \`git diff \--name-status 0adce9d..2ddf63d \\ | awk '{print \$1}' \\ | cut \-c1 \\ | sort \\ | uniq \-c\` | `124 A, 2323 D, 102 M, 13 R` |
| EA-02-006 | \`git ls-tree \-r 2ddf63d \\ | awk '\$1=="120000"{print \$4}'\` | `artifacts/ops/internal_version/body_get.json.sha256`, `docs/ENDPOINTS_CATALOG.json` |  |  |  |
| EA-02-007 | \`git ls-tree \-r \-l 2ddf63d \\ | awk '\$4==0' \\ | wc \-l\` | `344` |  |  |
| EA-02-008 | \`git ls-tree \-r \--name-only \-z 2ddf63d \\ | tr '\\0' '\\n' \\ | grep \-c ' '`; same with`grep \-P '\[^\\x00-\\x7F\]'\` | `46`; `0` |  |  |
| EA-02-009 | \`grep \-n '\_HISTORICAL\_PREFIXES\\ | \_DOCUMENTATION\_PREFIXES' ci/checks/classify\_ci\_changes.py\` | `164:_HISTORICAL_PREFIXES`, `179:_DOCUMENTATION_PREFIXES` |  |  |  |
| EA-03-001 | `sed -n '1,30p' scripts/make_compat_determinism_artifacts.py` | `from adapter.chart_orchestration import load_chart`; `print("compat_public not implemented", file=sys.stderr); sys.exit(2)` |  |  |  |  |
| EA-04-001 | `git grep -n 'engine\.charts\.loader' -- '*.py'` | 10 hits, all under `.audit_src/` or in the guard test's literals (full list in session transcript) |  |  |  |  |
| EA-09-001 | `git diff 0adce9d..2ddf63d -- schemas/close_candidate_source.v2.json` | full diff read; new `planning_records`, `requirement_ids`, `qa_checks`, `qa_verdict` fields, `docs/ephemeral`/`docs/pfcanon` exclusion patterns added |  |  |  |  |
| EA-09-002 | `git diff 0adce9d..2ddf63d -- ci/checks/classify_ci_changes.py` | full diff read; `_CLOSE_STAGE_TESTS` added, 4 new `_PRODUCT_TEST_OWNER_PATHS` entries for chart-separation files |  |  |  |  |
| EA-10-001 | \`find tests \-name 'test\_\*.py' \\ | wc \-l\` | `220` |  |  |  |
| EA-10-002 | `curl -s -o /tmp/x -w '%{http_code}' https://api.github.com/repos/amthorn78/glow-hdengine-v2/commits/2ddf63d.../status` | `403`; body `{"message":"API rate limit exceeded ..."}` |  |  |  |  |
| EA-11-001 | Direct read of `adapter/chart_orchestration.py` and `engine/charts/pure.py` in full | no `socket`, `urllib`, `psycopg`, `engine.db` or `vendor_client` import in either file |  |  |  |  |
| EA-PF10-001 | `wc -lc docs/pfcanon/PF10-HDE-Build-Notes-v13.9.9.md`; `tail -c 7` | `1326 277111 ...`; `\<eof>` |  |  |  |  |
| EA-PF10-002 | `grep -n 'C040-0[5-8]' docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` | multiple matching lines in each file (quoted in §12.1, RA-18) |  |  |  |  |
| EA-PF10-003 | `sed -n '/2.10 HDE-EPIC041 CL-E-10/,+1p' docs/pfcanon/PF10-HDE-Build-Notes-v13.9.9.md` | "Isis closes HDE-EPIC041, Separation Pass 4, with CLOSE / CHANGE\_CLOSED at 2026-11-01T16:39Z" |  |  |  |  |

## **Provenance**

Producer: this session, read-only, under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` for every command. No install, no build, no repository script, no validator, no generator, no test runner and no route/database/vendor call was executed at any point. The repository was fetched and unshallowed (`git fetch --unshallow origin`) solely to reach the baseline commit `0adce9d`, which was not present in the initial shallow clone; this is a `git` read operation, not a write to the repository. The checkout is clean apart from this audit file (`git status --porcelain` showed no output before this file was added). One attempted read-only call outside `git`/`grep`/`find`/`python3 -I` was made: two GitHub REST API reads (`/commits/{sha}/status`, `/commits/{sha}/check-runs`), both over HTTPS to `api.github.com`, both returning HTTP 403 (anonymous rate limit) and establishing nothing; no other network call was attempted.

