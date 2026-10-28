---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC041-WU-PR-01-PR-IMPLEMENTATION-RESULT
artifact_version: "1.4"
phase: PR-35
record_kind: CHECKPOINT (after the coherent corrective push for the Codex P2 finding; before the wait for current-head CI and review)
result: none yet (nonterminal checkpoint). v1.3's MERGE_PENDING is withdrawn, because the Codex review of its own head raised a finding that needed a fix
predecessor: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.3.md (v1.3, PR-35, MERGE_PENDING on 8b556e94; 9,551 bytes; blob bab234ed314b; sha256 e9aa1841016da8e6c421756c2cb93e65953f93e13f1c2bfb99921c97c4c95fbe; pushed as b4f897d5; preserved unchanged)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md (v1.0)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
proceed: the Product Owner's invocation of PR-30 — PR Implementation Proceed — 102726.1 for exactly PR_IMPLEMENTATION_PLAN v1.0, 2026-10-28; carried over; no new Proceed requested or created
pf10_read: as v1.1 (docs/pfcanon/PF10-HDE-Build-Notes-v13.9.1.md; provenance)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1 (https://app.notion.com/p/4064590a05eb8108a9f5cececa4b3149)
primary_skill: glow-hde-pr-development 1.5.0
session: https://claude.ai/code/session_01Q789tzt85iauNogD8xS2zg (the dedicated WU-PR-01 PR-35 session)
pull_request: amthorn78/glow-hdengine-v2#791 (https://github.com/amthorn78/glow-hdengine-v2/pull/791)
branch: claude/wu-pr-01-implementation-plan-js521f
base: origin/main e121e354060afe3007a84d82b61b073df1da666b (unchanged)
tested_source: 72d40b5f49dd1081c5db82dc223b92a8945a2c9b (b4f897d5 plus the correction commit for F-1); this record's own commit adds only this file under docs/ephemeral/
created_at: 2026-10-28 (UTC)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged; no new entry
---

# HDE-EPIC041 WU-PR-01 — PR Implementation Result v1.4 (PR-35 checkpoint)

## 1. State

**Checkpoint, not a result. v1.3's `MERGE_PENDING` is withdrawn.** The Codex review of v1.3's own head, `b4f897d5`, raised one P2 finding (F-1). It shows a guarantee breach on a real input, so it is fixed in `72d40b5f`, which this record is pushed with. The next version records hosted CI and the Codex review on the pushed head, and the PR-35 result.

## 2. Finding F-1 and its disposition

| Field | Value |
| :- | :- |
| Source | Codex code review on `b4f897d5` (review 5685440601, 15:41:47Z), thread `PRRT_kwDOP103ks6xMqM-`, comment 4402710499, `engine/charts/pure.py` line 13 |
| Priority | P2 (the reviewer's label) |
| Finding | "Remove the operational dependency from the pure time parser": the import of `parse_time_hh_mm` loads `engine.util.input_validators`, which imports `secrets`, which imports `random`, whose module body seeds a global `Random()` from the clock or OS entropy. The fresh-import test misses it because its harness imports `random` and `secrets` before installing guards |
| Traced path | `engine/charts/pure.py:13` `from engine.util.input_validators import parse_time_hh_mm` → `engine/util/input_validators.py:7` `import secrets` → `secrets` imports `random` → `random`: `_inst = Random()`, and `Random.seed(None)` "seeds from current time or from an operating system specific randomness source" |
| Reproduced | In a fresh interpreter under closed rails (`env -i`, `SAFE_MODE=1 ALLOW_NETWORK=0`), `random` and `secrets` were not loaded before `import engine.charts.pure`. After it, these were newly loaded: `base64`, `datetime`, `hashlib`, `hmac`, `json` (with `json.decoder`, `json.encoder`, `json.scanner`), `random`, `secrets` |
| Real input | yes: a fresh process whose first import of this unit's planned deliverable is `engine.charts.pure` (the WU-PR-02 callers, a CLI process, the AC-02 fresh-interpreter check itself) |
| Guarantee breached | instruction I-1 ("reads no time, randomness … at import … Importing it has no side effect"); Specification AC-02 ("no import-time side effect"); HDE Architecture §1.1 purity rule ("no import-time side effects"). I-1's permission to reuse `parse_time_hh_mm` ("may") rested on that module importing cleanly, which it does not |
| Disposition | **fixed** in `72d40b5f` (ID-35-4); the thread reply names the commit, and the thread is resolved after the push |

## 3. In-flight decisions (added to v1.2 §6, ID-35-1 to ID-35-3)

| ID | What changed | Why necessary | Tested |
| :- | :- | :- | :- |
| ID-35-4 | `engine/charts/pure.py` (`72d40b5f`): a local `_parse_time` with exactly `parse_time_hh_mm`'s acceptance (the same regex `^[0-2]\d:[0-5]\d$` with `re.match`, the same `int` split, the same hour bound); the `input_validators` import removed. `tests/charts/test_chart_pure_purity.py`: (a) the fresh-interpreter harness first imports the module cold, before any operational module is loaded, and fails if the import loads one of `random`, `secrets`, `uuid`, `socket`, `subprocess`, `logging`, `datetime`, `time`, `json`, `pathlib`, `tempfile`, `locale`, `hashlib`, `hmac`, `base64`, `sqlite3`, `psycopg`, `redis`, `requests`, `urllib`, `http` or `engine.util.input_validators`; then the existing patched re-import and calls run unchanged. (b) The AST rule now forbids any import from `engine.util.input_validators`, with a planted case for `parse_time_hh_mm`. (c) A new negative self-test plants a module that does `import secrets` and requires the harness to flag it | F-1 is a guarantee breach (I-1, AC-02, HDE Architecture §1.1) on a real input. Both files are this PR's own (instruction §4, "may add"; §8, "an ordinary in-scope defect is repaired in place"). The behaviour of `validate_birth_inputs` is unchanged | Equality probe: the local check and `parse_time_hh_mm` agree on 579,212 inputs (every string of up to 5 characters over `0-9`, `:`, `a`, space and newline, plus trailing-newline, Unicode-digit, full-width-digit and non-string cases): 0 differences. New tests against the old `pure.py` (`b4f897d5`): `test_pure_module_has_no_forbidden_dependency_or_call` and `test_fresh_import_and_calls_have_no_external_side_effects` **fail** ("importing engine.charts.pure loads ['base64', 'datetime', 'engine.util.input_validators', …, 'random', …]"), and both planted self-tests pass. On `72d40b5f`: the cold import adds only `typing`, `contextlib`, `unicodedata` and the `engine` packages; plan §11 items 1 to 5 in §4 |

## 4. Local checks on `72d40b5f` (plan v1.0 §11 items 1 to 5)

Configuration as v1.1 §4 (CPython 3.12.3, CI's install, `env -i` closed rails; full-history clone). Actor: this PR-35 session. Limitations: local runs; not hosted CI, QA or governed evidence.

| # | Run | Result |
| :- | :- | :- |
| 1 | the four new test files | 47 passed (the 46, plus the new planted-import self-test) |
| 2 | `classify_ci_changes.py --base e121e354 --head 72d40b5f --event-name pull_request` | exit 0; `paths=11`; all seven lanes; the same 169 targets |
| 3 | the 169 targets, as CI's isolated changed-tests step runs them | 3,669 passed, 0 failed (15:46:51Z to 15:54:46Z), in a full-history clone; `git diff` clean; status empty. One more than v1.1's 3,668: the new planted-import self-test |
| 4 | `prepush_check.py` `lanes membership build-notes` with the 11 paths | PASS; not-member ×11; current HDE Build Notes resolved; "repository unchanged" |
| 5 | admission; `release_id_recompute.py --check-manifest-only` | `release_id` 77204764…6c51e; exit 0 |

The full replay (item 6) was not re-run for this correction: plan v1.0 §19 requires items 1 to 5 before a corrective push, and item 3 runs the replay's step 08 set.

## 5. PR_REMOTE_ACTION_LEDGER (continues v1.3 §6)

| # | Time (UTC) | Action | Outcome |
| -: | :- | :- | :- |
| 26 | ~15:38 | Committed and pushed v1.3 (`8b556e94..b4f897d5`); read back; updated the PR description; armed a safety-net check-in for 16:30Z (`trig_01SSKXwVxBUmgqcPcG4THhbP`) | remote head `b4f897d5` |
| 27 | 15:39:06 | Codex code review started on `b4f897d5` | — |
| 28 | 15:41:51 | Events: Codex review 5685440601 (`commented`) and comment 4402710499, P2, F-1 | §2 |
| 29 | 15:42 to 15:46 | Verified, reproduced and fixed F-1 locally; committed `72d40b5f` | §2, §3 |
| 30 | 15:46 to 15:54:46 | Plan §11 items 1 to 5 on `72d40b5f` | §4 |
| 31 | — | Hosted `test` run 40718015218 on `b4f897d5` (started 15:38:36Z) is stale: that revision needs the F-1 correction. It is not a gate. The push of this record supersedes it (`ci.yml` cancels superseded pull-request runs); no cancellation interface was used | stale |
| 32 | next | One push of `72d40b5f` and this record; read back the remote head; reply on the F-1 thread naming `72d40b5f` and resolve it; then hosted `test` and Codex on the pushed head, through the subscription | — |

**Repeated finding class.** F-1 is the first finding on this PR (rounds: `c6e50a98`, `1b273594` and `8b556e94` raised none). If the next round raises a finding of the same class, the purity of `engine/charts/pure.py`, the session asks the Product Owner one design question before fixing it.

## 6. Unchanged

v1.2 §8 (#792), §9 (unresolved items and owners, with OBS-4), §10 (the TypeSafe reading for PR-40, not re-run: the PR-40 action text is unchanged), §11 (prompt-use provenance) and §12 (the conditional PR-40 terms); v1.3 §3 (PO-35-1).

## Canon relied on

As v1.2 "Canon relied on", and for F-1:

| Topic | Sources and sections | How it governs |
| :- | :- | :- |
| Disposition of F-1 | Change Process Guide (v2.5.5), "PR review finding disposition (every pull request; real inputs only)"; Plan Templates (v2.0.6), "Review guardrails" ("Finding disposition on real inputs"); PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1, "Review findings on real inputs" | A P2 that shows a guarantee breach on a real input is fixed; the reply names the fix; repeated class triggers one design question |
| The guarantee | HDE Architecture (v2.4.7) §1.1, "Purity rule (normative)" and "Non-BodyGraph chart loader classification"; Specification v1.1 R-02 and AC-02; instruction v1.0 §3.2 I-1 | No import-time side effects; no randomness or time read at import |

## Nonclaims

This checkpoint is not a PR-35 result, merge readiness, a merge, hosted CI, a review verdict, QA, Ops, acceptance, PF09 movement, a canon change, a PF10 addendum or closure. Local results are not governed evidence. No agent merges #791; Nathan does.
