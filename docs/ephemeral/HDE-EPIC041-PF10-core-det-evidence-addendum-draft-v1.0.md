---
artifact_type: PF10_ADDENDUM_DRAFT
artifact_version: "1.0"
logical_id: HDE-EPIC041-PF10-CORE-DET-EVIDENCE-ADDENDUM-DRAFT
target: "HDE Build Notes, the next addendum after 2.15 (numbered 2.16 on the current base version v14.0.4), plus one Addendum Index line"
publication: "The Product Owner's manual action. Nothing under docs/pfcanon/ is edited by this record."
origin: "Product Owner direction, 2026-11-01, on FND-005"
recorded: "2026-11-01T21:30Z"
repository_head_read: "origin/main 58723d4d (PF10 v14.0.4)"
producer: "Isis, continuing Lead Developer for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
---

# Draft PF10 addendum 2.16: GATE:CORE-DET evidence is the real compat path

**How to use this record.**
* The text between the two horizontal rules below is the addendum, ready to paste into HDE Build Notes after addendum 2.15.
* The index line under "Addendum Index line" goes at the end of §1.1.
* Bump the version and effective date as you usually do; HDE Build Notes §3 to §6 govern that.
* The body follows the HDE Build Notes cross-reference rule: PF documents are named by title and section only.

**Two things to fix in HDE Build Notes v14.0.4 when you paste.** These are document maintenance, not addendum content:
* **The 2.15 index line is in the wrong place.** It was pasted into the section heading: line 202 reads `# **2\) Nu2.15 Live QA …`. The §1.1 Addendum Index ends at 2.14, so the 2.15 line belongs there, and the heading should read `# **2\) Numbered Addenda**`.
* **The published 2.15 is the draft before its correction.** Its "Known nonconforming items" still say SYN-A and SYN-B are "not yet stored" and "not yet registered". Addendum 2.16 records both facts (R-3 below), so 2.15 itself needs no edit.

## Addendum Index line

* 2.16 GATE:CORE-DET evidence is the real compat path: the compat-determinism generator and eight absent evidence entries are retired (FND-005), and addendum 2.15's synthetic-people and evidence-list items are closed

---

## 2.16 GATE:CORE-DET evidence is the real compat path: the compat-determinism generator and eight absent evidence entries are retired (FND-005), and addendum 2.15's synthetic-people and evidence-list items are closed

Timestamp: 110126 21:30 (UTC). Details:
* **What this records.** The Product Owner's decision of 2026-11-01 on FND-005. The compat-determinism generator is not needed for the product, and no code changes.
* **What this decides.** What counts as `GATE:CORE-DET` evidence (R-1); which listed entries are retired (R-2); and two facts that close items addendum 2.15 left open (R-3).

### Decision and approval status

* **Decision.**
  * The Product Owner asked: "what I care about is if the product works. I don't want dev changes. So what about FND-005, why do we not need this?"
  * After the answer, he directed that this statement be drafted: "We may as well do all three, yes."
  * R-1 to R-3 state that decision as canon.
* **Status.** Proposed. The rules take effect as canon when this addendum is published in HDE Build Notes.
* **Relation to other canon.**
  * The `GATE:CORE-DET` pass conditions in HDE Governance §12.1 are unchanged: the preimage recipe, AB↔BA and two-run identity, and no nondeterminism on public paths.
  * This addendum supersedes only the evidence entries R-2 names, in four places:
    * HDE Governance §12.2, "GATE:CORE-DET — Determinism and identity";
    * HDE Governance Appendix B.2, "CI jobs";
    * HDE Governance Appendix D.1, "Byte-compare scripts" and "Composite fingerprint" and "Integration set";
    * HDE Governance Appendix D.3, "Identity marker/logs" and "Recompute scripts".
  * Every other entry in those sections still governs.

### The facts that prompted it

All read on `main` at `58723d4d`.

* **The generator never tested the real product.**
  * `scripts/make_compat_determinism_artifacts.py` was built to check `compat_public`. That function scored each category from a hash of the pair's identity and never read the charts.
  * Until HDE-EPIC040 PR-04 (#467, 2026-09-22), that placeholder was what `hdctl showcompat` and the compat handler ran. #467 replaced it with the real calculation (`evaluate_pair`, then `compute_core`) and removed `compat_public`.
  * The generator has exited 2, with `compat_public not implemented`, ever since. Its stored outputs (`artifacts/compat/AB.json`, `BA.json`, `identity_hash.txt`) are captures from the placeholder era.
* **Eight more listed entries do not exist.**
  * `artifacts/cards/A3/IDENTITY_OK.txt` is not on `main`. A lower-case copy, `artifacts/cards/a3/IDENTITY_OK.txt`, is a frozen marker last changed by HDE-EPIC024 (2026-01-22).
  * `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml` and `ci/jobs/two_run_identity_bytecompare.yml` never existed in the repository's history.
  * `fixtures/composite/abba/`, `fixtures/composite/integration_abba/`, `audit/gates/determinism/abba_compare.log` and `audit/gates/determinism/abba_compare_integration.log` never existed either, and no code refers to them.
* **The Reader goldens are current, but prove the emitter only.**
  * `scripts/make_reader_v1_goldens.py` regenerates the committed goldens byte-identically, and their tests pass (37).
  * But the script feeds fixed, hand-written bands. Its AB↔BA golden emits two identical inputs. So it proves the emitter's canonical bytes and preimage hashing, not compat AB↔BA.
* **The real compat path is proven.**
  * **CI owner tests**, 148 passed on `main` (3 open-rails cases skip under closed rails):
    * `tests/core/test_engine_core_abba.py` and `tests/core/test_engine_core_determinism.py`, which CI selects whenever the core, signal, composite or calculator code changes;
    * `tests/compat/test_evaluate_pair_eligibility.py`, selected when `engine/compat/compute.py` changes;
    * `tests/compat/test_compat_public_ab_ba_identity.py`;
    * `tests/cli/test_showcompat_parity_and_identity.py`, which every compat-lane run executes.

    The eligibility and showcompat tests recompute the idempotence hash from the preimage.
  * **The live compat test** of addendum 2.15, run as HDE-EPIC041-POSTCLOSE-OPS01, attempt 1, on 2026-11-01:
    * AB↔BA and two-run byte identity on live vendor charts;
    * production returned the same bytes as the CLI;
    * the preimage recipe holds on all nine live Reader bodies, four from production and five from the CLI.

### R-1 — What GATE:CORE-DET evidence is

`GATE:CORE-DET` evidence is the real compat path, in two parts:
* **Closed rails:** the CI owner tests above, run as CI selects them. A change that removes or weakens one of them needs its owner's review, like any other gate test.
* **Open rails:** each run of the addendum 2.15 live compat test. That is Ops evidence, under HDE Governance §3.4.

The Reader goldens remain evidence for canonical emission (`GATE:CORE-CANON`) and the Reader covenant (`GATE:CORE-READER`). They are not evidence of compat AB↔BA.

### R-2 — Retired evidence entries

These entries are no longer `GATE:CORE-DET` evidence. No record may cite them as current proof.
* `scripts/make_compat_determinism_artifacts.py` (HDE Governance §12.2, D.1, D.3);
* `artifacts/cards/A3/IDENTITY_OK.txt` (§12.2, D.3);
* `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml` and `ci/jobs/two_run_identity_bytecompare.yml` (B.2);
* `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`, `fixtures/composite/integration_abba/*.json` and `audit/gates/determinism/abba_compare_integration.log` (D.1).

**No code changes.** The generator, its test that pins exit 2, the `artifacts/compat/` captures and the lower-case `a3` marker stay as they are, as history. Deleting them would be a development change, and the Product Owner directed none.

FND-005 is closed by this decision.

### R-3 — Addendum 2.15 items closed

* **"The GATE:CORE-DET evidence list"** in 2.15's "Known nonconforming items" is resolved by R-1 and R-2.
* **SYN-A and SYN-B are stored.** HDE-EPIC041-POSTCLOSE-OPS01 v1.1, Part W, stored both in production on 2026-11-01:
  * one row each, `rows_written=1`, `read_back_match` true;
  * the production Reader then scored them in both orders, for v1 and v2.
* **SYN-A and SYN-B are registered.** Both are now in the EPIC011 test-identity record and the engine's synthetic identity map (#821).
* 2.15's two "not yet" bullets about them are superseded by these facts.

### Scope, exclusions and nonclaims

* **Scope:** which evidence counts for `GATE:CORE-DET`, the retired entries, and the two 2.15 items above.
* **Excluded:**
  * the gate's pass conditions;
  * any code, test or artifact change;
  * whether the compat scores are right, which is a separate product question;
  * conjunction.
* **Nonclaims.** This record:
  * runs no test;
  * makes no QA verdict, acceptance, Ops result, deployment or PF09 movement;
  * drains no canon.

### Dependencies and unresolved obligations

* **Publication.** Publishing this addendum in HDE Build Notes is the Product Owner's action.
* **Drainage into permanent canon** has not been done. Its targets are HDE Governance §12.2, Appendix B.2, Appendix D.1 and Appendix D.3.

### Evidence

* **Generator and placeholder:** commit `cd6f9e6c` (#467) removed `compat_public` from `engine/compat/compute.py`. At its parent, `engine/cli/main.py` and `engine/http/compat_handler.py` called `compat_public`. `tests/scripts/test_make_compat_determinism_artifacts.py` pins exit 2.
* **Absent entries:** `git ls-tree` on `main` and `git log --all` for each path R-2 names.
* **Reader goldens:** regenerated in a throwaway clone of `main` at `58723d4d`, with no byte changed; `tests/reader_v1/test_goldens.py`, `test_release_pack.py` and `test_emitter.py` gave 37 passed.
* **Owner tests:** the five files named above, 148 passed and 3 skipped at `58723d4d` under closed rails.
* **Live run:**
  * the evidence is under `audit/ops/hde-epic041/postclose-ops01/` (#822), with its execution result record;
  * the preimage recomputation used both the repository's emitter and an independent canonical form.

---

## Canon relied on

Read on `main` at `58723d4d`.

* **HDE Governance:**
  * §12.1, `GATE:CORE-DET`;
  * §12.2 "Evidence links";
  * Appendix B.2;
  * Appendix D.1, "Parity (Reader↔CLI, AB↔BA, two-run)";
  * Appendix D.3, "Idempotence coupling";
  * §3.4, for the live test's Ops class.
* **HDE Build Notes (v14.0.4):**
  * front matter, and "Precedence, versioning, and scope" §1 to §9;
  * §1 template and §1.1 index;
  * addendum 2.2, for the form of a rule addendum;
  * addendum 2.15 as published.
* **HDE Math Spec:** searched for a governed score or band distribution; none exists ("No current … category-distribution recipe is governed").
