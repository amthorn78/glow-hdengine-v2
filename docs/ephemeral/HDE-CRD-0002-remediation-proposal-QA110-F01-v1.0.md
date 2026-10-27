---
artifact_type: REMEDIATION_PROPOSAL
REMEDIATION_PROPOSAL_ID: HDE-CRD-0002-REMEDIATION-PROPOSAL-QA110-F01
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: REMEDIATION_PENDING
approval_sentinel: "ASK OK?"
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
ORIGINATING_FINDING_REF: docs/ephemeral/HDE-CRD-0002-ESC10-qa-escalation-report-v1.0.md (QA_ESCALATION_REPORT v1.0, AWAITING_THOTH_REMEDIATION; blob 2cfc8e558a32; SHA-256 fcee46493367e4e49204198fa44d820ff52a28e2976fcbb8d67bc425ffeedc43; on main through amthorn78/glow-hdengine-v2#729 as 1643768), finding QA110-F01, with its intake docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md §6 (blob 0a797250aa81)
originating_stage: QA-110 — Review QA Evidence and Route the Next Action — 100926.1 (ESCALATION_REQUIRED), then ESC-10 — Create QA Escalation Report — 100926.1; Kronos (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV). Return owner Kronos, check 13's verification (report §12)
requirement: S20 (Specification v1.1-approved, unchanged by Specification delta 01); QA Plan v1.2 check 13 `qa-13-prepush-check`, task T13, attempt 1
evidence_of_record: audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log on main (blob 4c6d826ae0ac; SHA-256 71a0d11afff1b89a76a9c7624d0cfa93d22845f5714a3618a87c7967b9593ef7)
tested_source: 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171; tools/ci/prepush_check.py blob 4dc098566620 and tests/tools/test_prepush_check.py blob 8d2c0be36e2e there and on main at 1643768 (the blobs WU-PR-06 landed, HDE Build Notes addendum 2.12)
predecessor: none (the first remediation proposal for QA110-F01). Prior remediation lineage in this change: FND-001, proposal v1.0 and v1.1, remediation review v1.0 (APPROVE_AS_CHANGED) and v1.1 (APPROVE), WU-REM-01 (#716, accepted, addendum 2.25); closed and unrelated to this finding
work_unit_proposed: WU-REM-02 (a new routed work item under Glow QA Guide §10.6; WU-PR-06 is accepted-final and is not reopened)
author: Thoth, Head of Development, continuing HDE-CRD-0002 remediation author. Role continuity from https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum (retired by the Product Owner); execution identity of this run https://claude.ai/code/session_01RxSyQc1jdJZ9VtegkPWSNf
reviewer: Isis, continuing Lead Developer, ESC-40 — Review and Return Approved Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb8173905cc6d17a40457b)
prompt: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9; page state as of 2026-10-12T02:29:51.552Z; fetched and read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
created_at: 2026-10-25T03:25:00Z
repository_head_read: origin/main 1643768 (#729 merged). Outside docs/ephemeral/ and docs/pfcanon/, the only differences from the tested source 2e03a268 are the QA evidence #726 published (audit/qa/hde-crd-0002/, the Index, Mirror, orientation and path-proof files); no code, test or workflow differs
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (blob fa7810c75426; SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; 519,440 bytes); the last addendum in the file is 2.26
pf10_addendum: none (ESC-30 produces none)
PR_RETURN_PHASE: not applicable (WU-REM-02 has no instruction, Proceed, branch or pull request)
next_prompt: ESC-40 — Review and Return Approved Remediation — 100926.1
canon_conflict_register: CR-1 to CR-11 carried unchanged; no new entry (§13)
---

# HDE-CRD-0002 — Remediation proposal for QA110-F01 (S20, check 13), v1.0

## 1. Result

**REMEDIATION_PENDING.** The finding is valid, its cause is established by reproduction, and this is one complete bounded remedy.

- **Cause (proven, §4).** `make_copy` in `tools/ci/prepush_check.py` makes every throwaway copy with `git clone --shared`, so the copy borrows the source checkout's object store through `.git/objects/info/alternates`. Whenever a process in a copy, or in anything cloned from a copy, writes an object the source already holds, git does not write it again: it *freshens* the file that holds it, with `utime(2)`, which moves that file's mtime and ctime. The file it freshens is the source checkout's pack. The tool's guard digests the mtime and ctime of every file under the source's `.git`, so it reports a violation, correctly.
- **The writers (observed, §5.3).** In replay step 08 ("Run affected behavioral tests in isolation"), the tool's own owner test `tests/tools/test_prepush_check.py` makes fixtures with `git clone --shared` of the replayed tree and commits in them. Four git invocations, from two tests, each freshened the source's pack: `commit -am "tool change"`, `add -A` and `commit -m "unregistered"` in `test_lanes_equals_the_classifier_for_refs_and_for_given_paths`, and `commit -am "classifier with a write on load"` in `test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy`. The same four, with the same effect, under git 2.43.0 and git 2.53.0.
- **The venue (established, §5.4).** Git version is not the factor (H-2 refuted). The source's layout is (H-3): for a **shallow** source, git ignores the local-clone optimisation and `--shared` with it, and the copy gets its own pack, so nothing in it can touch the source. The two earlier passing venues were cloud containers whose checkouts are shallow (`git clone --depth 50`), and their scratch clones were made from those checkouts. The QA-100 venue's E-L was a full-history clone, as the QA Plan requires, and the failure reproduces on demand on a full-history clone here, under both git versions.
- **The reading of S20 (§4.5).** A freshen is a write to the repository under ID-2: a syscall on a file in the checkout's `.git` that changes its metadata. The guard's precision is right; the copy mechanism is the defect. The remedy changes no Specification boundary.
- **The remedy (§6).** The copy owns its objects: `make_copy` clones with `--no-hardlinks --dissociate` instead of `--shared`, and refuses a copy that still borrows. On a violation the tool names each changed entry and the fields that moved, so the next such finding is diagnosable from its own output. Four regression tests, one with a negative control that reproduces the mechanism, pin it. Rehearsed in throwaway clones under both git versions (§5.5, §5.6): the owner test passes (141 tests) and the full check 13 step-1 command exits 0 with "repository unchanged".
- **O-1 (§10).** The OPS03 cross-device failure is an independent defect, outside S20 and this remedy; it needs separate Product Owner disposition.

This proposal approves nothing and creates no addendum, Plan, instruction, Proceed or work vehicle. It awaits Isis's ESC-40 decision (`ASK OK?`).

## 2. Working state and inputs read

| Item | State |
| :- | :- |
| Prerequisite | #729 merged before this run started: origin/main at 1643768 (02:00Z) |
| Inputs read in full | The escalation report v1.0; the QA-110 review v1.0 §6 and R-2; the check 13 primary (both executions); the QA-100 results v1.0 §2 and §5.2; QA Plan v1.2 check 13 and §9; Specification v1.1-approved S20 and Specification delta 01; Implementation Plan v1.1 WU-PR-06 block and Plan delta 01 v1.1; the WU-PR-06 instruction v1.0 (ID-2, ID-3, §5.7, §5.8); the WU-PR-06 lineage review v1.0 (§5, LR6-O1, LR6-O6, LR6-O7); the postmortem v1.1 (D-1); the remediation review FND-001 v1.1 and proposal v1.1 (format and lineage); the ESC-10 checkpoint and handoff; `tools/ci/prepush_check.py` (lines 230 to 400, 730 to 845, 1521 to 1755), `tests/tools/test_prepush_check.py` (lines 1 to 120, 596 to 940, 1031 to 1070), `.github/workflows/ci.yml` (steps 08, 14, 15), README.md "Pre-push check (HDE-CRD-0002)"; PF canon as "Canon relied on" lists it |
| Rehearsal venue | This cloud container: Ubuntu 24.04.5, 4 CPUs, git 2.43.0, `/usr/bin/python3.12` (3.12.3), `ruby` 3.3.x at `/usr/local/bin`, `bash`, `curl`. Git 2.53.0 built from the kernel.org tarball `git-2.53.0.tar.xz` (SHA-256 5818bd7d80b061bbbdfec8a433d609dc8818a05991f731ffc4a561e2ca18c653, matching the published `sha256sums.asc` entry) into the scratchpad with `NO_CURL=1 NO_GETTEXT=1 NO_TCLTK=1 NO_PERL=1 NO_EXPAT=1 NO_PYTHON=1`. A CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`). Closed rails through `env -i`: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `HOME` an empty scratch directory with a `.gitconfig` holding only `user.name` and `user.email`. Every source was a scratch clone; nothing was committed to a tracked branch or pushed from them |
| Writes | This proposal only, under `docs/ephemeral/`, by pull request |

## 3. Finding validation (ESC-30 step 1)

| Item | Validated |
| :- | :- |
| Approved objective | Specification S20: "One read-only command reports … writing nothing to the repository". Implementation Plan v1.1 WU-PR-06 acceptance (1): "the repository tree is byte-identical before and after (asserted by the tool and by its test)". WU-PR-06 instruction ID-2 (binding reading): the repository is the checkout's working tree, ignored files included, and its `.git` directory; "No report may create, modify or delete any file there", git metadata included. Glow QA Guide §2.2.11: "A non-writing check MUST NOT mutate the repository or external state" |
| Expected | QA Plan v1.2 check 13 step 1: exit 0, five reports `status=PASS`, a final `PREPUSH_CHECK_RESULT: PASS … repository unchanged` line |
| Observed | Two executions in attempt 1 on the Product Owner's workstation (git 2.53.0, full-history E-L clone): exit 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION`, no result line. Execution 2 (the Moon Loop) had all five reports `PASS`, replay steps 01 to 16 `SUCCESS`, "copy after replay: clean". Steps 2 to 4 passed both times (primary; report §4, §5) |
| Classification | `FAIL_BEHAVIOR`, by check 13's own Outcomes line and Plan Templates "Exact status predicates" and "Causal precedence": readiness held, the QA tooling is trustworthy, and the delivered surface contradicts an explicit predicate. Agreed |
| Attempt history | One attempt, two executions; the ordinary rerun is consumed (R-2). A later execution is the remediation route's verification, not attempt 2 (report §12) |
| Evidence | E-1 to E-6 of the report stand; each is reproduced or extended below. The executor's observation that only the pack's mtime and ctime moved, and the Kronos verification that `repository_state()` differs in `metadata` only after a write of an existing object in a `--shared` copy, are both confirmed |
| Dependencies | The close of HDE-CRD-0002 (S21's writer): a `FAIL_BEHAVIOR` check blocks a v2 `SATISFIED` decision (addendum 2.17 resolution A). The QA-120 report waits on this check (and on the unselected checks 16 to 21). Check 21 is not blocked (report §9) |
| Real input | The operator's shell on a full-history checkout (addendum 2.11 rule 4(b)); the QA Plan's E-L is defined as exactly that ("a plain `git clone` without `--depth`, never a clone of a shallow checkout"). PO-35-6 is met: the write is one that code the tool runs in a copy makes, observed, not constructed |
| Return owner | Kronos, for check 13's verification after an approved and delivered repair (report §12) |

## 4. Diagnosis

### 4.1 The mechanism (proven under both git versions)

Git's object writer (`write_object_file`) checks whether an object already exists before writing it. If it does, in any object store the repository reaches, loose or packed, git calls `freshen_file`, which is `utime(path, NULL)` on the file holding that object, and writes nothing. The purpose is to protect recently referenced objects from pruning; the effect is a metadata write to a file the process did not otherwise touch. A `--shared` clone reaches the source's object store through `objects/info/alternates`; a clone of a clone inherits the alternate (git copies the alternates file into local clones), and a `git worktree` shares its repository's store. So a write of an existing object anywhere down that chain freshens the **source's** pack or loose-object file.

Measured here with the tool's own `repository_state()`, imported from `tools/ci/prepush_check.py` at blob 4dc098566620, in scratch repositories (E1; identical results under git 2.43.0 and 2.53.0):

| Copy made with | Source state after clone and detached checkout | Source state after `git hash-object -w` in the copy of a blob the source holds |
| :- | :- | :- |
| `--shared`, packed source | equal | **differs**: `.git/objects/pack/pack-….pack` mtime and ctime |
| `--shared`, loose source | equal | **differs**: the loose object's file, mtime and ctime |
| `--local` (hardlinks; git's default for a path) | **differs at clone**: the pack, `.idx`, `.rev` and `objects/info/packs` ctime (link count 1 to 2) | differs: the pack (one inode, two names) |
| `--no-hardlinks`, packed or loose source | equal | equal |
| `--no-hardlinks` of a source that itself borrows (a `--shared` clone of a base) | equal; the copy keeps the alternate, so the write freshens the **base's** pack (outside the guarded repository) | equal for the source |
| `--no-hardlinks --dissociate` of that borrowing source | equal; the copy has no alternates | equal for the source and for the base |

Ordinary operations that write existing objects in a `--shared` copy (E3; both git versions, packed source, timestamps reset before each probe): editing one file and `git commit -a` (racily-clean index entries are re-hashed and written), `git add -A` of a new file with unique content, `git add` of a file whose bytes equal an existing blob, and `git add` of an *unchanged* tracked file all freshened the source's pack. `git status`, an empty commit, `git stash`/`pop`, branch checkouts, `git write-tree` on a primed cache tree and `git worktree add`/`remove` did not.

### 4.2 Which file, which field (report §8 item 1)

The source checkout's one pack file, `.git/objects/pack/pack-<id>.pack`, in its mtime and ctime (both set by the freshen; the size and bytes do not change). No other `.git` file changed in any reproduction here (§5.3), which agrees with the executor's inspection in the QA-100 venue (results §5.2) and excludes H-4.

### 4.3 Which step, which command (report §8 item 2)

Replay step 08. The step runs the full-validation targets in a `git worktree` of the replay copy; the owner test `tests/tools/test_prepush_check.py` is one of those targets. Its `_clone()` fixture (line 92) makes a `git clone --shared --no-checkout` of `ROOT`, which inside the replay is that worktree, and two tests commit in such fixtures. The instrumented runs (§5.3) attribute every source change to exactly these four invocations:

| Test (`tests/tools/test_prepush_check.py`) | Line | Invocation in the fixture clone | Source change |
| :- | -: | :- | :- |
| `test_lanes_equals_the_classifier_for_refs_and_for_given_paths` | 798 | `git commit --quiet -am "tool change"` | pack mtime, ctime |
| same | 801 | `git add -A` | pack mtime, ctime |
| same | 802 | `git commit --quiet -m "unregistered"` | pack mtime, ctime |
| `test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy` | 859 | `git commit --quiet -am "classifier with a write on load"` | pack mtime, ctime |

Chain for each: fixture clone → alternates → the worktree's repository, the replay copy → alternates → the source checkout's `objects/`. The object freshened is whichever existing blob or tree the commit re-hashes; the file freshened is the source's pack, where every object of the head lives in a fresh full-history clone.

The same tests run directly in the checkout in check 13's step 3, which is why the executor saw the E-L pack's timestamps move inside step 3 both times (results §5.2). Step 3 is not under the guard, and that observation is not an S20 breach; it is the same mechanism acting on the developer's checkout from the owner test's own fixtures (§14, O-A).

### 4.4 The venue (report §8 item 3)

| Venue | Source | Shallow? | Result |
| :- | :- | :- | :- |
| PR-40 lineage review at `fc51620` (addendum 2.12) | "fresh scratch clones of the session's checkout (`--no-hardlinks`)" | the session checkout of a Claude Code cloud container is a `--depth 50` clone (this container's is: `git rev-parse --is-shallow-repository` → `true`); a clone of a shallow repository is shallow | exit 0, "repository unchanged" |
| QA Audit v1.0 §7 item 9 at `0b15328d` | "throwaway clones under this session's scratchpad"; their origin is not recorded | not recorded; the same container class | exit 0 |
| QA-100 executions 1 and 2 at `2e03a268` | E-L: "plain `git clone`" from GitHub, `shallow=false` recorded by the readiness read | no | exit 4, twice |
| This proposal, unpatched tool at `1643768` (code equal), git 2.43.0 and 2.53.0 (§5.3) | full-history clones from GitHub, `shallow=false` | no | exit 4, both; the four writers above |

Why shallowness decides it (E4, both git versions): `git clone --shared` of a shallow source prints no warning for `--shared`, but git disables the local-path optimisation for a shallow source and clones through the transport instead. The copy then has **its own packs and no `objects/info/alternates`**, so `--shared` has no effect and nothing in the copy can reach the source. Of a full-history source, the same command gives a copy with no packs of its own and an alternates file naming the source's `objects/`. The owner test's own comment (line 805) records the fallback: "a shallow source makes `git clone --shared` fall back to copying ref history".

So the two earlier venues passed because their sources were shallow and the mechanism was never engaged; the QA Plan's E-L, defined as full-history, is the first venue in the lineage where the delivered design met the condition it fails on. H-2 (git version) is refuted by E1, E3 and the two instrumented runs, which agree line for line between 2.43.0 and 2.53.0. H-3 is confirmed in this form. The Audit venue's shallowness is inferred from the container class, not recorded; it is the only part of this table that is not observed.

### 4.5 Is a timestamp-only freshen a "write to the repository"? (report §8 item 4)

Yes, under the approved reading.

- ID-2 defines the repository as the checkout including its `.git` directory, and the rule as "No report may create, modify or delete any file there", naming git metadata. A freshen is `utime(2)` on a file under the source's `.git`: the kernel changes the inode's mtime and ctime at the request of a process the tool started. That is a modification of a repository file made by code the tool runs in its copies, on a real input.
- The guard's design (`_metadata_digest`'s docstring: "Any write to a file changes its st_ctime_ns, which user space cannot set back, so a rewrite with the same bytes is seen too") was built to see exactly this class. It saw it. Narrowing the guard to ignore timestamp-only changes under `objects/` would hide a real write path (a `--local` hardlink clone, for example, changes the same files' ctime at clone time, §4.1) and is the over-correction report §13 warns of.
- The defect is therefore in the copy mechanism, not in the guard, and the remedy keeps the guard's precision unchanged. S20's text, acceptance intent and Live QA class are unchanged; no Specification decision arises (ESC-30 step 5; §9 below).

### 4.6 Hypotheses disposed

| Report §7 | Disposition |
| :- | :- |
| H-1 | **Confirmed and completed**: the step is replay step 08; the writers are the four owner-test invocations in §4.3; the file is the source's pack (§4.2) |
| H-2 | **Refuted**: identical behaviour under git 2.43.0 and 2.53.0 in E1, E3 and the full runs (§5) |
| H-3 | **Confirmed in a specific form**: shallow against full-history source (§4.4); packed against loose does not matter (E1: both freshen) |
| H-4 | **Refuted**: no other `.git` file changed in any instrumented run; IF-35-24 (concurrent git activity) is not involved |

## 5. Reproduction and rehearsal evidence

### 5.1 Method

All work in the scratchpad of this container, as §2 states. A per-invocation `git` wrapper (a Python script first on `PATH`, running the real git of the chosen version) recorded, for every git process started during a run, its working directory, arguments, exit status, and any change to the lstat identity (mode, size, mtime, ctime) of every file under the source's `.git`, so the writer of any change is named by its own command line. The tool's child environments inherit `PATH`, so the wrapper covered the reports, the replayed steps and the tests they run; git's own subprocesses use its exec path and are covered by their parent.

Timing values are from this venue, under four concurrent full runs on four CPUs, and are not representative of a workstation.

### 5.2 Source clones

`src-full` and `src-full-253`: full-history clones of `amthorn78/glow-hdengine-v2` at `16437685af7aca1f16d1b47375343ae68fe904e0` (origin/main; code equal to the tested source), `shallow=false`, one pack `pack-d440e19b9061cc7cbaf2f4e05afd771df3f5bd61` (33,823 objects, 57,021,511 bytes), status empty. `proto-repo` and `proto-repo-243`: `--no-hardlinks` clones of `src-full` with the prototype (§6.3) committed on top as a scratch commit `386b86b4e87d280aeee19944fb0aa840faec0fc4` (never pushed).

### 5.3 The delivered tool reproduces the finding (unpatched; both git versions)

Check 13 step 1's exact command, `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay`, from the clone's root.

| Run | git | Window (UTC, 2026-10-25) | Exit | stderr | Git invocations logged | Source changes |
| :- | :- | :- | :- | :- | -: | :- |
| unpatched, `src-full` | 2.43.0 | 02:03:04Z to 02:15:55Z | **4** | `PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git metadata changed` | 3,716 | 4, all to `objects/pack/pack-d440e19b….pack` (mtime, ctime), by the four invocations of §4.3, at 02:13:39Z, 02:13:39Z, 02:13:40Z and 02:14:50Z, each with cwd `<temporary>/replay-runner-temp/hde-changed-test-source` (step 08's worktree) and `-C <pytest tmp>/test_lanes_…/clone` |
| unpatched, `src-full-253` | 2.53.0 | 02:03:04Z to 02:15:54Z | **4** | the same line | 3,716 | the same 4, at 02:13:38Z, 02:13:38Z, 02:13:38Z and 02:14:50Z |
| unpatched, `src-full-253` again, `ruby` on `PATH` (the clean reproduction) | 2.53.0 | 02:25:23Z to 02:55:31Z | **4** | the same line | 3,990 | 2: `commit --quiet -am "tool change"` at 02:35:36Z and `commit --quiet -am "classifier with a write on load"` at 02:36:37Z, both to the pack's mtime and ctime |

The first two runs: `lanes`, `membership` and `build-notes` `PASS`; the source's `git status --porcelain` empty before and after; the pack's mtime after the run 02:14:50Z (the last writer). Rehearsal deviation, recorded as such: `PATH` for those two runs omitted `/usr/local/bin`, where this container's `ruby` lives, so `sweep` was `TOOLING_FAILURE missing on PATH: ruby` and step 08 reported "11 failed, 4512 passed" (9 `tests/evidence/test_hdapi_v2_contract_inventory.py` tests and the two owner tests that run `sweep`, all `FileNotFoundError: 'ruby'`), with steps 09 to 15 skipped and step 16 failing on that. None of the 11 touches the guard, and all four source changes happened before the owner test's sweep cases ran.

The third run is the QA venue's picture exactly: every report `PASS` (`sweep` `uncovered=0`), replay steps 01 to 16 `SUCCESS` (step 08 "4523 passed"; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "copy after replay: clean"; replay 1,798.7 s), the source's status empty, and exit 4 with no result line. Only two of the four invocations registered a change this time: the `add -A` and the `commit -m "unregistered"` followed `commit -am "tool change"` within the same filesystem timestamp tick, so their freshen set the same mtime again, which lstat cannot distinguish. The mechanism and the writers are the same.

### 5.4 The venue fact (E4)

In scratch repositories, for git 2.43.0 and 2.53.0 alike: `git clone --shared --no-checkout` of a full-history source → copy with 0 packs of its own and `objects/info/alternates` naming the source; of a `--depth 1` source → copy with 3 packs of its own and no alternates file. This container's checkout is shallow.

### 5.5 The prototype's owner test (both git versions)

`python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` in `proto-repo`, `PYTHONPATH` the clone, `ruby` on `PATH`: **141 passed in 191.09 s, exit 0** under git 2.43.0; **141 passed in 191.43 s, exit 0** under git 2.53.0. 137 existing tests plus the four of §6.3 (one parametrised twice). An earlier pair of runs without `/usr/local/bin` on `PATH` failed the same two sweep tests for `ruby` and passed the other 139, under both versions. The new negative control (`--shared` copy, write of an existing blob, `repository_state` differs in `metadata` only, `state_changes` names the pack with `mtime, ctime`) passed under both versions, which is the venue-independent proof that the test detects the mechanism it guards against.

### 5.6 The patched tool: check 13 step 1 (both git versions)

The same command as §5.3 from `proto-repo` (git 2.53.0) and `proto-repo-243` (git 2.43.0), `ruby` on `PATH`, the wrapper watching each source:

| Run | git | Window (UTC, 2026-10-25) | Exit | Result line | Git invocations logged | Source changes |
| :- | :- | :- | :- | :- | -: | :- |
| patched, `proto-repo-243` | 2.43.0 | 02:11:40Z to 02:43:13Z | **0** | `PREPUSH_CHECK_RESULT: PASS lanes=PASS membership=PASS build-notes=PASS sweep=PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)` | 4,138 | 0 |
| patched, `proto-repo` | 2.53.0 | 02:11:39Z to 02:43:13Z | 4, **invalid as a verification** (below) | none; stderr the violation line and then seven `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: git metadata …` lines naming the source's six loose objects (the scratch commit's two blobs and four trees) and its pack, each `(mtime, ctime)` | 4,138 | 0 by any wrapped git process |
| patched, `proto-repo-253b` (a fresh `--no-hardlinks` clone of `proto-repo`; nothing else ran in it), with a second, independent watcher: a sampler polling every file under its `.git` every 50 ms, ready to dump the process table on any change | 2.53.0 | 02:49:17Z to 03:19:48Z | **0** | the same `PREPUSH_CHECK_RESULT: PASS … repository unchanged` line | 4,138 | 0 by any git process; 0 by the sampler over the whole run |

Every report `PASS` in all runs: `lanes` and `membership` as predicated for the two paths, `build-notes` the v13.7.8 file and its SHA-256, `sweep` `uncovered=0`; replay steps 01 to 16 `SUCCESS`, step 08 "4527 passed" (the 4,521 of the QA venue plus the four new tests and its two skips, which do not skip here), product 77, compat 119 passed, 3 skipped, 2 xfailed, db 269, rails 138, evidence 134, qa 488, release 79, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`, "copy after replay: clean"; replay about 1,870 s under load.

**Why the second run is invalid, and what it shows anyway.** Its source, `proto-repo`, was also the checkout in which this proposal's two owner-test rehearsals (§5.5) ran, with `ROOT` equal to `proto-repo`, from about 02:10:30Z until 02:13:42Z and 02:13:52Z. Their `--shared` fixtures committed in that window, and at 02:12:32Z those commits freshened `proto-repo`'s own objects (the six loose objects of the scratch commit, then its pack: the order a `git add` and `write-tree` take), inside the guarded window of the tool run that had started at 02:11:39Z. That is concurrent git activity in the checkout (the stated limit IF-35-24), caused by this author's rehearsal arrangement, not by the patched tool: the wrapper watching `proto-repo` saw no change from any git process the tool or its replay started, the sampler-watched rerun below saw none, and the 2.43 run on a source nothing else touched exited 0. Two things it does show: the new diagnostics (R-2) named the seven changed entries and their fields on the first occasion they were needed, which is what this escalation lacked; and the owner test's fixtures freshen the checkout they run in (§14, O-A).

### 5.7 Negative controls

- The delivered code fails the new regression test's first half (a `--shared` copy is exactly what `make_copy` made): E1's `--shared` rows and §5.3 are that failure, observed with the tool's own `repository_state()`.
- The test's negative control (second half) reproduces the mechanism in-test, so a future `make_copy` that borrows again fails the test on any git version and any filesystem with nanosecond timestamps; the pack's timestamps are reset to a fixed past instant first, so a coarse clock cannot mask a freshen.
- `--local` hardlinks (git's default for a path argument) are not a remedy: they change the source's ctimes at clone time (E1).
- `state_changes` names no file content: paths and field names only (the new test asserts the fixture's content does not appear).

## 6. Proposed bounded remediation

### 6.1 Overlay on the immutable bases (`AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`)

| Base | Passage | Overlay |
| :- | :- | :- |
| Implementation Plan v1.1 (with delta 01 v1.1 and the FND-001 overlay) | §7 WU-PR-06, acceptance (1) and (3) | Unchanged in meaning. One new routed work unit, **WU-REM-02** (PR; Distillation; not production-affecting; S20), delivers the repair; WU-PR-06 stays accepted-final (addendum 2.12). WU-REM-02 lands after WU-REM-01 and before the QA-120 report |
| WU-PR-06 instruction v1.0 | ID-2, "Measured feasible: `git clone --shared` plus a detached checkout (§5.8)" | The rule of ID-2 stands as written. Its example mechanism is superseded for WU-REM-02: the copy is made with `git clone --no-hardlinks --dissociate --no-checkout` plus the detached checkout (R-1). §5.8's measurement is recorded history |
| Specification v1.1-approved | S20 | Unchanged |
| QA Plan v1.2 | check 13 | Unchanged by this proposal. Its step 3 predicate ("137 passed") will no longer match once WU-REM-02 lands (141 tests); that is a Plan revision for QA-80 and QA-70, or Kronos's decision at the return (report §12; §11 below) |

### 6.2 Required behaviour (PR-20 designs the code; the prototype in §6.3 is one implementation that meets it)

- **R-1. The copy owns its objects.** `make_copy` makes every throwaway copy with `git clone --quiet --no-hardlinks --dissociate --no-checkout -- <source> <destination>` and the detached checkout as before. `--no-hardlinks` copies the object files instead of linking them (a hardlink changes the source's ctime and shares the inode a freshen would touch). `--dissociate` repacks away any alternates the *source* itself borrows from, so a source made with `--shared` or `--reference` yields a copy that reaches no other repository (git documents this use of `--dissociate` for local clones of a borrowing repository). After the clone, a copy whose `.git/objects/info/alternates` exists is a `ToolingError`, so the guarantee is checked, not assumed. All four copying reports (`lanes`, `membership`, `sweep`, `replay`) share `make_copy`, so none can freshen the source.
- **R-2. A violation names what changed.** `repository_state()` keeps the git-metadata entries by name (path with mode, size, mtime, ctime, and a SHA-256 of the bytes outside `objects/`), and a new `state_changes(before, after)` lists, one line each, the differing entries with the fields that moved (`HEAD`, status, tracked, ignored, directory, and `git metadata <dir>/<rel> (mtime, ctime)`), capped at 20 lines plus a count. `main` prints them to stderr after the existing `PREPUSH_CHECK_READ_ONLY_VIOLATION` line, as `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: <line>`. Exit status 4, stdout and the result line are unchanged. Paths and field names only; no file content, no environment value.
- **R-3. The guard's precision is unchanged.** Every field `repository_state()` compared before is compared after; the comparison is still equality of the whole state. Only the representation of `metadata` changes (entries instead of one digest per directory), so that R-2 can name entries.
- **R-4. Regression tests in `tests/tools/test_prepush_check.py`.** (a) A copy of a packed source and of a loose source made by `make_copy` has no alternates; a write in it of a blob the source holds leaves `repository_state(source)` equal and `state_changes` empty; and, as a negative control in the same test, a `--shared` copy of the same source with the same write makes `repository_state(source)` differ in `metadata` only, `state_changes` naming the object file with `mtime, ctime`. (b) A copy of a source that itself borrows objects reaches neither the source nor the base. (c) `state_changes` names a rewritten tracked file and a rewritten `.git/config` with `(mtime, ctime)`, and carries no file content. The existing 137 tests stay as they are.
- **R-5. Documentation.** README.md "Pre-push check (HDE-CRD-0002)": the exit-status line gains "; the changed entries are named on stderr" after "4 when the repository changed during the run", and the Limits list gains one line: "The throwaway copies own their objects: a source that borrows objects from another repository (`--shared`, `--reference`) is dissociated in the copy, at the cost of a repack." No other documentation changes; `AGENTS.md` is not touched.
- **R-6. Nothing else changes.** No report's output lines, the inventory pin, the child environment, the temporary-directory rules, exit codes, the classifier registration (`tools/ci/prepush_check.py` keeps its owner test) or any file outside `tools/ci/prepush_check.py`, `tests/tools/test_prepush_check.py` and `README.md`.

### 6.3 The prototype, rehearsed (one implementation of R-1 to R-4; PR-20 may improve it)

`git diff` of the scratch commit `386b86b4` against `16437685`, two files, +125/−18. `tools/ci/prepush_check.py` keeps every string constant the no-hook test forbids out of it.

```diff
diff --git a/tests/tools/test_prepush_check.py b/tests/tools/test_prepush_check.py
index 8d2c0be3..eedd6446 100644
--- a/tests/tools/test_prepush_check.py
+++ b/tests/tools/test_prepush_check.py
@@ -736,6 +736,71 @@ def test_repository_state_covers_ignored_files(tmp_path: Path) -> None:
     assert tool.repository_state(repo).metadata != settled.metadata
 
 
+@pytest.mark.parametrize("packed", [True, False])
+def test_a_copy_owns_its_objects_so_a_write_in_it_cannot_freshen_the_source(tmp_path: Path, packed: bool) -> None:
+    """QA110-F01: git freshens the file holding an object when that object is written again, even from a copy
+    that borrows the source's object store, so the source's pack (or loose object) changes its mtime and ctime
+    without any content change.  A copy therefore owns its objects, and the source stays as it was."""
+    source = _synthetic(tmp_path / "source", {"a.txt": "alpha\n", "d/b.txt": "beta\n"})
+    if packed:
+        _git(source, "repack", "-a", "-d", "-q")
+        _git(source, "prune-packed", "-q")
+    head = _git(source, "rev-parse", "HEAD")
+    past = 1_600_000_000_000_000_000  # a fixed past instant, so a freshen to "now" is seen on any clock
+    object_files = [p for p in (source / ".git" / "objects").rglob("*") if p.is_file()]
+    assert object_files
+    for path in object_files:
+        os.utime(path, ns=(past, past))
+    before = tool.repository_state(source)
+    copy = tool.make_copy(source, head, tmp_path / "copy")
+    assert not (copy / ".git" / "objects" / "info" / "alternates").exists()
+    assert tool.repository_state(source) == before
+    # Write, inside the copy, a blob the source already holds.
+    subprocess.run(["git", "-C", str(copy), "hash-object", "-w", "--stdin"], input=b"alpha\n", check=True,
+                   capture_output=True)
+    assert tool.repository_state(source) == before
+    assert tool.state_changes(before, tool.repository_state(source)) == []
+    # Negative control: a borrowing copy shows the mechanism this test guards against.
+    shared = tmp_path / "shared"
+    subprocess.run(["git", "clone", "--quiet", "--shared", "--no-checkout", "--", str(source), str(shared)],
+                   check=True, capture_output=True)
+    _git(shared, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", head)
+    assert tool.repository_state(source) == before
+    subprocess.run(["git", "-C", str(shared), "hash-object", "-w", "--stdin"], input=b"alpha\n", check=True,
+                   capture_output=True)
+    freshened = tool.repository_state(source)
+    assert freshened != before and freshened.metadata != before.metadata
+    assert freshened.tracked == before.tracked and freshened.status == before.status
+    (change,) = tool.state_changes(before, freshened)
+    assert change.startswith("git metadata ") and "/objects/" in change and "mtime" in change and "ctime" in change
+
+
+def test_a_copy_of_a_source_that_borrows_objects_borrows_none_itself(tmp_path: Path) -> None:
+    base = _synthetic(tmp_path / "base", {"a.txt": "alpha\n"})
+    _git(base, "repack", "-a", "-d", "-q")
+    source = tmp_path / "borrowing"
+    subprocess.run(["git", "clone", "--quiet", "--shared", "--", str(base), str(source)], check=True, capture_output=True)
+    head = _git(source, "rev-parse", "HEAD")
+    before_base, before_source = tool.repository_state(base), tool.repository_state(source)
+    copy = tool.make_copy(source, head, tmp_path / "copy")
+    assert not (copy / ".git" / "objects" / "info" / "alternates").exists()
+    subprocess.run(["git", "-C", str(copy), "hash-object", "-w", "--stdin"], input=b"alpha\n", check=True,
+                   capture_output=True)
+    assert tool.repository_state(source) == before_source
+    assert tool.repository_state(base) == before_base
+
+
+def test_a_read_only_violation_names_the_changed_entries(tmp_path: Path) -> None:
+    repo = _synthetic(tmp_path / "named", {"README.txt": "fixture\n"})
+    before = tool.repository_state(repo)
+    (repo / ".git" / "config").write_bytes((repo / ".git" / "config").read_bytes())
+    (repo / "README.txt").write_text("fixture\n", encoding="utf-8")
+    changes = tool.state_changes(before, tool.repository_state(repo))
+    assert any(c == "tracked README.txt" for c in changes)
+    assert any(c.startswith("git metadata ") and c.endswith("/config (mtime, ctime)") for c in changes)
+    assert all("fixture" not in c for c in changes)
+
+
 # --------------------------------------------------------------------------
 # every report on the repository: read-only, and the expected answers
 # --------------------------------------------------------------------------
diff --git a/tools/ci/prepush_check.py b/tools/ci/prepush_check.py
index 4dc09856..697aeda2 100644
--- a/tools/ci/prepush_check.py
+++ b/tools/ci/prepush_check.py
@@ -265,32 +265,30 @@ def resolve_commit(repo: Path, ref: str) -> str:
     return result.stdout.decode("ascii").strip()
 
 
-def _metadata_digest(directory: Path) -> str:
-    """Digest of git metadata: every file's lstat identity, its bytes outside objects/, and every directory's name.
+def _metadata_entries(directory: Path) -> tuple[tuple[str, str], ...]:
+    """Git metadata: every directory's name, and every file's lstat identity with its bytes' digest outside objects/.
 
     Any write to a file changes its st_ctime_ns, which user space cannot set
     back, so a rewrite with the same bytes is seen too; an object is therefore
     not read.  An empty directory holds no file, so without its name its
-    creation or removal would go unseen.
+    creation or removal would go unseen.  Each entry is kept by name so that a
+    violation can say which entry changed.
     """
-    digest = hashlib.sha256()
+    entries = []
     for path in sorted(directory.rglob("*")):
         rel = path.relative_to(directory).as_posix()
         if path.is_dir() and not path.is_symlink():
-            digest.update(f"{rel}/\0".encode())
+            entries.append((f"{rel}/", ""))
             continue
         if not (path.is_file() or path.is_symlink()):
             continue
         info = path.lstat()
-        digest.update(f"{rel}\0{info.st_mode}\0{info.st_size}\0{info.st_mtime_ns}\0{info.st_ctime_ns}\0".encode())
-        if rel.startswith("objects/"):
-            continue
-        if path.is_symlink():
-            digest.update(os.readlink(path).encode())
-        else:
-            digest.update(path.read_bytes())
-        digest.update(b"\0")
-    return digest.hexdigest()
+        identity = f"mode={info.st_mode} size={info.st_size} mtime={info.st_mtime_ns} ctime={info.st_ctime_ns}"
+        if not rel.startswith("objects/"):
+            content = os.readlink(path).encode() if path.is_symlink() else path.read_bytes()
+            identity += f" sha256={hashlib.sha256(content).hexdigest()}"
+        entries.append((rel, identity))
+    return tuple(entries)
 
 
 def _ignored_entries(repo: Path) -> tuple[tuple[str, int, int, int, int], ...]:
@@ -347,7 +345,7 @@ class RepositoryState:
     tracked: tuple[tuple[str, int, int, int, int], ...]
     ignored: tuple[tuple[str, int, int, int, int], ...]
     directories: tuple[tuple[str, int, int, int], ...]
-    metadata: tuple[tuple[str, str], ...]
+    metadata: tuple[tuple[str, tuple[tuple[str, str], ...]], ...]
 
 
 def repository_state(repo: Path) -> RepositoryState:
@@ -357,15 +355,24 @@ def repository_state(repo: Path) -> RepositoryState:
         Path(git_text(repo, "rev-parse", "--absolute-git-dir")),
         (repo / git_text(repo, "rev-parse", "--git-common-dir")).resolve(),
     }
-    metadata = tuple(sorted((str(d), _metadata_digest(d)) for d in directories))
+    metadata = tuple(sorted((str(d), _metadata_entries(d)) for d in directories))
     return RepositoryState(head=head, status=status, tracked=_tracked_entries(repo), ignored=_ignored_entries(repo),
                            directories=_directory_entries(repo), metadata=metadata)
 
 
 def make_copy(repo: Path, commit: str, destination: Path) -> Path:
-    """Clone ``commit`` outside the repository; the source repository is only read."""
+    """Clone ``commit`` outside the repository; the source repository is only read.
+
+    The copy owns its objects.  A copy that borrowed the source's object store
+    (``--shared``, or a hardlinked ``--local`` clone) would let git freshen the
+    source's pack or loose-object file, changing its mtime and ctime, whenever
+    a step in the copy writes an object the source already holds; that is a
+    write to the repository under S20 (QA110-F01).  ``--no-hardlinks`` copies
+    the objects and ``--dissociate`` drops any alternates the source itself
+    borrows from, so nothing the copy does reaches the source or its alternates.
+    """
     result = subprocess.run(
-        ["git", "clone", "--quiet", "--shared", "--no-checkout", "--", str(repo), str(destination)],
+        ["git", "clone", "--quiet", "--no-hardlinks", "--dissociate", "--no-checkout", "--", str(repo), str(destination)],
         env=_git_env(),
         capture_output=True,
         check=False,
@@ -374,6 +381,8 @@ def make_copy(repo: Path, commit: str, destination: Path) -> Path:
     if result.returncode != 0:
         raise ToolingError("git clone into the temporary directory failed: "
                            + result.stderr.decode("utf-8", errors="replace").strip())
+    if (destination / ".git" / "objects" / "info" / "alternates").exists():
+        raise ToolingError("the throwaway copy still borrows objects from another repository")
     if git(destination, "cat-file", "-e", f"{commit}^{{commit}}", check=False).returncode != 0:
         raise ToolingError(f"commit {commit} is not available to the throwaway copy")
     git(destination, "-c", "advice.detachedHead=false", "checkout", "--quiet", "--detach", commit)
@@ -382,6 +391,37 @@ def make_copy(repo: Path, commit: str, destination: Path) -> Path:
     return destination
 
 
+def state_changes(before: RepositoryState, after: RepositoryState, limit: int = 20) -> list[str]:
+    """What differs between two repository states, one line per entry, for the read-only violation message."""
+    lines: list[str] = []
+    if after.head != before.head:
+        lines.append(f"HEAD {before.head} -> {after.head}")
+    if after.status != before.status:
+        lines.append("git status output changed")
+    for name, old, new in (("tracked", before.tracked, after.tracked), ("ignored", before.ignored, after.ignored),
+                           ("directory", before.directories, after.directories)):
+        old_by_path, new_by_path = {e[0]: e for e in old}, {e[0]: e for e in new}
+        for path in sorted(set(old_by_path) | set(new_by_path)):
+            if old_by_path.get(path) != new_by_path.get(path):
+                lines.append(f"{name} {path}")
+    old_meta, new_meta = dict(before.metadata), dict(after.metadata)
+    for directory in sorted(set(old_meta) | set(new_meta)):
+        old_by_path, new_by_path = dict(old_meta.get(directory, ())), dict(new_meta.get(directory, ()))
+        for rel in sorted(set(old_by_path) | set(new_by_path)):
+            old_identity, new_identity = old_by_path.get(rel), new_by_path.get(rel)
+            if old_identity == new_identity:
+                continue
+            if old_identity is None or new_identity is None:
+                detail = "created" if old_identity is None else "removed"
+            else:
+                old_fields, new_fields = dict(f.split("=", 1) for f in old_identity.split()), dict(f.split("=", 1) for f in new_identity.split())
+                detail = ", ".join(k for k in old_fields if old_fields[k] != new_fields.get(k)) or "changed"
+            lines.append(f"git metadata {directory}/{rel} ({detail})")
+    if len(lines) > limit:
+        lines = lines[:limit] + [f"and {len(lines) - limit} more"]
+    return lines
+
+
 def copy_status(copy: Path) -> tuple[bool, str]:
     diff = subprocess.run(["git", "-C", str(copy), "diff", "--exit-code", "--name-only"],
                           capture_output=True, text=True, check=False)
@@ -1742,6 +1782,8 @@ def main(argv: Sequence[str] | None = None) -> int:
     if after != before:
         print("PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git "
               "metadata changed", file=sys.stderr)
+        for line in state_changes(before, after):
+            print(f"PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: {line}", file=sys.stderr)
         return EXIT_READ_ONLY_VIOLATION
     overall = "PASS" if all(status == "PASS" for _n, status, _d in results) else "FAIL"
     print("PREPUSH_CHECK_RESULT: " + overall + " "
```

R-5 (README.md) is not in the prototype; it is two lines of prose for PR-20.

### 6.4 Stated limits of the remedy

- Each copy now holds the source's object store by value: for this repository about 58 MB per copy. The cost is within noise in a quiet venue (`lanes` 1.3 s, `membership` 1.1 s, `sweep` 1.2 s with the patched tool, against 1.1 s each with the delivered tool in the same venue, §5.3 and §5.6) and 4 to 7 s per report with four full runs sharing four CPUs. `lanes` and `membership` each make one copy, `sweep` one, `replay` one. The owner test makes several per run; it took 191 s here under that load against 130 s recorded for the delivered code in a quiet venue (LR6-O6); PR-20 measures it in its venue.
- A source that borrows objects (`--shared`, `--reference`) costs one `git repack -a -d` in the copy (`--dissociate`); a plain clone costs none.
- A shallow source still makes copies hold ref-reachable history only (LR6-O7 F-3; unchanged).
- The guard still reports concurrent git activity in the checkout as a violation (IF-35-24; unchanged), now with the changed entries named.

### 6.5 Verification

| Check | Where | Pass condition | Owner |
| :- | :- | :- | :- |
| V-1 | PR-30, the PR session's clone (CI's install, Python 3.12, `ruby`, `bash`, `curl`, closed rails) | `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py`: 141 passed, exit 0 | PR-30 |
| V-2 | PR-30 and PR-35, a **full-history** scratch clone of the candidate head (`git rev-parse --is-shallow-repository` prints `false`; a shallow clone does not engage the mechanism, §4.4) | check 13 step 1's command exits 0 with every report `PASS` and `PREPUSH_CHECK_RESULT: PASS … repository unchanged`; step 2 exits 0 as predicated; the source's `git status --porcelain` empty before and after | PR-30, PR-35 |
| V-3 | PR-30, the same scratch clone | Negative control at the command level: with `make_copy` temporarily reverted to `--shared` in the scratch clone only, the same command exits 4 and its stderr names `objects/pack/pack-….pack (mtime, ctime)`; reverted before commit | PR-30 |
| V-4 | Hosted CI on the pull request | The `changed-tests` step (the owner test is the tool's registered owner test) and every selected lane green; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | PR-35 |
| V-5 | PR-40 | The landed blobs equal the reviewed head; V-1 to V-4 recorded; the measure below assessed | Implementation Agent (PR-40) |
| V-6 | The return: check 13's verification by Kronos in the QA-100 venue class (E-L, full history, git 2.53.0) | Plan v1.2 check 13 steps 1, 2 and 4 as predicated; step 3 with the test count the revised Plan states (§11) | Kronos |

The rehearsals of §5.5 and §5.6 are this proposal's evidence that V-1 to V-3 are achievable; they are not V-1 to V-3.

### 6.6 Business case (addendum 2.11 rule 1, as addendum 2.18 narrows it)

| Field | Content |
| :- | :- |
| Beneficiary | Every PR session and operator who runs `tools/ci/prepush_check.py` on a full-history checkout, which is the tool's real operating environment (the operator's shell; the QA Plan's E-L): the tool's only guarantee under S20 holds there, and its result line is reachable. Kronos: check 13 can be verified. The close of HDE-CRD-0002: a `FAIL_BEHAVIOR` check blocks the v2 `SATISFIED` decision (addendum 2.17 resolution A) |
| Evidence | QA110-F01, both executions (the primary); §5.3 here, twice more, under two git versions |
| Benefit | Exit 0 with "repository unchanged" on a full-history checkout; a violation, when one occurs, names its cause in the tool's own output, which this escalation lacked (report §6 "The guard names no file") |
| Measure | (1) Check 13's verification exits 0 with the result line in the QA-100 venue class (V-6). (2) The regression tests pass on hosted CI on the pull request and on `main` after the merge. Neither is observable at PR-40 beyond V-4; PR-40 records V-1 to V-4 as the proxy and the measure as "not yet measurable" (addendum 2.18 rule 5) |

There is no cost ceiling (addendum 2.18 rule 1). This is a fix of a guarantee breach on a real input (addendum 2.11 rule 7: "a breach of the read-only or no-secrets guarantees"), not tooling for its own sake (rule 2).

## 7. Affected surfaces

| Surface | Effect |
| :- | :- |
| Requirement S20 | Met on full-history checkouts once delivered; unchanged in text |
| `tools/ci/prepush_check.py` | `make_copy`, `_metadata_digest` → `_metadata_entries`, `RepositoryState.metadata`, new `state_changes`, two lines in `main`. Not a release member (`catalog/manifest.json` unchanged; release 1.3.0, `release_id` 77204764… unchanged) |
| `tests/tools/test_prepush_check.py` | Four tests added; 137 unchanged |
| `README.md` | Two lines under "Pre-push check (HDE-CRD-0002)" (R-5) |
| CI | The pull request selects the lanes the classifier gives for these three paths; the owner test is the registered owner of the tool (`_CI_TOOL_TEST_OWNERS`), so the `changed-tests` step runs it. No `ci.yml` change; the replay's pin is untouched |
| QA Plan v1.2 check 13 | Step 3's literal count becomes 141 (§11) |
| Downstream | Check 13's verification, then the QA-120 report; the S21 close decision |
| Not affected | Production, the deployed service, every release member, vendor and database paths, the evidence graph, PF canon |

## 8. Preserved bases, overlays and exclusions

- **Preserved unchanged:** Specification v1.1-approved with delta 01 (addendum 2.20); Implementation Plan v1.1 (IA-30 `INITIAL_APPROVE`) with delta 01 v1.1 (addendum 2.19) and the FND-001 overlay (addenda 2.23, 2.24); QA Plan v1.2 (QA-70 APPROVE); the WU-PR-06 instruction v1.0, plan v1.0 and accepted lineage (addendum 2.12); every Product Owner decision in the lineage (PO-35-1 to PO-35-6; D-2 to D-5; PO-1 to PO-5 of QA-100).
- **Active overlays this proposal adds (pending Isis):** §6.1's two rows; WU-REM-02 as a new routed work item.
- **Exclusions:** no change to the guard's fields or equality rule (R-3); no change to the owner test's existing fixtures (`_clone`, `_clone_at` keep `--shared`; §14 O-A); no change to `ci.yml`, the classifier, the sweep's coverage definition, the child environment, the temporary-directory rules or the exit codes; no `AGENTS.md` edit; no PF canon edit; no addendum; no Plan, instruction, Proceed, branch or pull request created here; no QA executed; no Ops.

## 9. Authority: within remediation, not a Specification change

- S20's text, acceptance intent, Live QA class and exclusions are unchanged. The remedy makes the delivered tool meet S20 as the WU-PR-06 instruction read it (ID-2), on the input class the QA Plan already defines (E-L, full history).
- The Specification decision owner is this Thoth (CF-C-30). No Specification delta is proposed or needed; the open Product Owner decisions D-1/LR6-O1 (whether S20 is removed by a later delta) and FND-028 (whether the replay report is removed) are not presumed. If the Product Owner removes S20, WU-REM-02 is moot and stops; if the replay report is removed, R-1 still governs the three remaining copying reports, and `make_copy`, which they share, stays as proposed. Neither decision is a remedy, and this proposal does not wait on either.

### Alternatives considered

| Alternative | Why not |
| :- | :- |
| (a) Narrow the guard: ignore mtime and ctime changes under `objects/`, or compare pack files by size and name only | Hides a real write class (a hardlink clone's ctime change, a pack rewrite with the same size); contradicts ID-2's rule and the guard's stated design; the over-correction report §13 names. Rejected |
| (b) Keep `--shared` and stop the writers (change the owner test's fixtures to own their objects) | Fixes the four observed writers only. Any other replayed test, tool or step that writes an existing object in a copy, or in a worktree or clone of one, would freshen the source again; the mechanism, not the instance, is the defect. Rejected as the remedy; see §14 O-A for the fixture hygiene as an observation |
| (c) `git clone --local` (hardlinks) | Changes the source's ctimes at clone time (E1). Rejected |
| (d) `git worktree add` from the source | Writes `.git/worktrees/` in the source; excluded by ID-2 and §5.7 of the instruction. Rejected |
| (e) Export the tree without a repository (`git archive`) | The replay's steps run `git worktree add`, `git diff`, `git status` and `git rev-parse` in the copy and need a repository; the lanes classifier diffs base against head. Rejected |
| (f) `--no-hardlinks` without `--dissociate` | Equal for the guarded repository; a source that borrows objects would leave the copy freshening the *base's* files outside the repository (E1). `--dissociate` closes that at no cost for a plain clone. The proposal takes both |

## 10. O-1: the OPS03 cross-device failure (report §10)

Execution 1's replay failed `tests/ops/test_hde_epic038_ops03.py::test_candidate_replacement_failure_is_persisted_before_cleanup` and `::test_validator_rejects_authorized_candidate_symlink` because the OPS03 tool's fixed `RUN_ROOT` `/tmp/hde-epic038-ops03` and pytest's `tmp_path` under `TMPDIR` were on different filesystems (`EXDEV`). Thoth's decision on scope: **not in scope of this remedy.** It is an independent defect: no HDE-CRD-0002 requirement names OPS03, the replay reported it truthfully, and it is produced by, blocks or invalidates nothing in S20 or in this repair (Glow QA Guide §3.4.8 "An independent or opportunistic defect requires separate Product Owner disposition"). Its input is real (a developer shell with `TMPDIR` on another filesystem; hosted CI, where `TMPDIR` is unset, is unaffected). It is routed to the Product Owner as a later-change candidate, with the record in the primary and in the report §10. Nothing here fixes, skips or quarantines those tests.

## 11. Delivery and return map

1. **ESC-40**, Isis: APPROVE, APPROVE_AS_CHANGED or DENY. A qualifying approval writes one HDE Build Notes addendum recording the overlay (§6.1, §6.2).
2. **PR-10** — Create PR Work-Unit Instructions — 100926.1, by the whole-change Implementation Agent, for `WORK_UNIT_ID: WU-REM-02`, under the approved overlay. The instruction carries R-1 to R-6, the stated limits (§6.4), V-1 to V-5, the business case (§6.6) and the bounded file set (`tools/ci/prepush_check.py`, `tests/tools/test_prepush_check.py`, `README.md`).
3. **PR-20**, in a new dedicated WU-REM-02 PR session: the detailed plan. It may adopt §6.3 as its prototype or improve it within R-1 to R-6; it measures the copy cost in its venue and rehearses V-1 to V-3 on a full-history clone.
4. **Then the ordinary unit lineage:** Product Owner Proceed → PR-30 → PR-35 → Nathan's merge → PR-40 lineage review.
5. **Return:** Kronos, check 13's verification (report §12). Because WU-REM-02 adds four tests, Plan v1.2 check 13's step 3 predicate ("137 passed") stops matching; under report §12, the Plan is revised first through QA-80 and QA-70 (step 3's count to 141; the step 1 predicate unchanged, since the tool's stdout lines are unchanged), and the verification then runs as a QA-90 task for check 13 under the remediation return, republishing `check_id` `qa-13-prepush-check` (Glow QA Guide §3.4.3). Whether a Plan revision or Kronos's narrower reading applies is Kronos's and Isis's call, not this proposal's.

`PR_RETURN_PHASE`: not applicable. WU-REM-02 has no instruction, Proceed, branch or pull request.

## 12. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The ESC-40 decision on this proposal | Isis |
| WU-REM-02 instruction (PR-10) and plan (PR-20) | Whole-change Implementation Agent; the WU-REM-02 PR session |
| Publication into PF10 of any addendum for this proposal | Product Owner |
| QA Plan v1.2 check 13 step 3's count after WU-REM-02 (QA-80, QA-70) | Kronos; Isis |
| O-1, the OPS03 cross-device failure (§10) | Product Owner, as a later-change candidate |
| O-A, the owner test's fixtures freshening the developer's checkout (§14) | Product Owner, as a later-change candidate; or PR-20 if the Product Owner widens WU-REM-02 |
| D-1 / LR6-O1 and FND-028 (S20's and the replay's fate) | Product Owner (unchanged; not presumed here) |
| The Audit §7 item 9 venue's shallowness (§4.4), inferred not recorded | None; stated as an inference. It does not bear on the remedy |
| CR-9 (PROPOSED; WU-OPS-01 Plan-text conflict), unaffected | Isis (IA-30) |
| PR35-C1 / FND-024 (the auto-maintenance race in the owner test on git 2.55) | As recorded (addendum 2.21; triage v1.1). Unchanged by this remedy; a verification run red with that signature is `FAIL_TOOLING` under check 13's Outcomes |

## 13. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from the escalation report §15, the QA-110 review §12, the QA-100 results §10 and QA Plan v1.2 §13, where the full entries are. This proposal adds none: ID-2's "Measured feasible: `git clone --shared`" is an example mechanism recorded as feasible at `5e62a65`, not a rule in conflict with S20, and §4.5 is a reading of S20 that confirms the approved text rather than a conflict between sources.

| Entry | Status | Reviewer / record |
| :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth; Specification v1.1 lineage |
| CR-4 | `APPROVED` | Product Owner; WU-PR-01 disposition §2 |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner; same record §3 |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20; addendum 2.6 |
| CR-7, CR-8 | `APPROVED`, alternative (a) | Product Owner direction of 2026-10-14; addendum 2.7 |
| CR-9 | `PROPOSED`; unreviewed | Isis, IA-30 boundary |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40; addendum 2.24 |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | QA-70 review v1.0; applied in check 1 |

## 14. Observations (no action in this remedy)

- **O-A. The owner test's fixtures freshen the developer's checkout.** `_clone()` and `_clone_at()` in `tests/tools/test_prepush_check.py` make `--shared` clones of `ROOT`; when the test runs in a full-history checkout (check 13's step 3, a PR session's own run, or hosted CI's worktree), their commits freshen that checkout's pack (§4.3; results §5.2). The checkout's content, status and HEAD are untouched, the tool's guard samples state only around its own run, and hosted CI is unaffected, so it is not an S20 breach. It is the same hazard class, and it overwrote the step-1 evidence in the QA-100 venue (report §6: the post-run inspection followed step 3). R-2 removes that diagnostic dependence. Changing the two fixture lines to `--no-hardlinks --dissociate` would end the hazard at a cost of about 58 MB per fixture clone; it is left to the Product Owner as a later-change candidate, or to PR-20 if WU-REM-02 is widened to include it.
- **O-B.** The QA Plan's E-L definition ("never a clone of a shallow checkout") is what made check 13 the first run in the lineage to engage the mechanism. A pre-approval run of a read-only tool in a shallow scratch clone does not exercise `--shared`; Plan authors and reviewers may want that fact for later tools that clone the repository. Recorded for Kronos; no action here.
- **O-C.** In this venue `/tmp` and the checkout share one filesystem, so O-1's `EXDEV` does not reproduce here; it was not attempted.

## 15. TypeSafe reading for the receiving session (ESC-40)

Action sent (v8.2): "Review, as the independent integrated-remediation reviewer, one new remediation proposal, not yet reviewed, for one escalated QA failure of a delivered developer tool: a read-only pre-push command whose repository-unchanged guard reports a violation in one venue while every report it runs passes. The proposal diagnoses the cause from reproductions under two git versions, proposes a bounded change to the tool's copy mechanism of about ten lines, a named-entries violation message, and four regression tests in the owner test module, each already rehearsed in throwaway clones; decide approve, approve as changed or deny, and on approval write one standalone build-notes addendum and route to a new work-unit instruction. No task list exists; it is a read-only review of Markdown records against canon and the repository: no code is written and no live run against a provider occurs; a work-unit instruction, a pull-request plan and implementation with their own reviews, and a QA verification of the check follow; the work is one unit, not many independent units."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.36 (confidence 0.71); rung probabilities low 0.00, medium 0.04, high 0.67, extra high 0.18, max 0.11, ultracode 0.00. Model probabilities Fable 5.1 0.12, Opus 5.5 0.82, Sonnet 5.5 0.06, Haiku 5.5 0.00 (confidence 0.76). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.080, Fable 5.1 at extra high 0.022, Fable 5.1 at max 0.013, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.033, Opus 5.5 at high 0.549, Opus 5.5 at extra high 0.148, Opus 5.5 at max 0.090, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.040, Sonnet 5.5 at extra high 0.011, Sonnet 5.5 at max 0.007, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-25T02:16:24Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-25T02:16:24Z; HTTP 200 in 0.56 s; 5557 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request:** the installed TypeSafe scoring skill's `request-v8.2.json` and `score_v8.py`, run once with session kind `review` and label "ESC-40 HDE-CRD-0002 QA110-F01 remediation review", before this proposal was saved.
- **Records:** the Notion row was not written.
- **Picks:** ESC-40: Nathan's pick is not stated. This ESC-30: Nathan's pick is not stated; its reading is in the escalation report §16 (Fable 5.1 at high, score 2.36). The model this session ran on is recorded only in the session, not here.

**Surface advice for ESC-40.**
- **Session:** the continuing Isis session for HDE-CRD-0002, or a top-level Claude Code cloud session Nathan creates for that role, on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt.
- **Reads:** this proposal (§1, §4, §5, §6, §9, §10, §11); the escalation report v1.0 §7, §8, §12; `tools/ci/prepush_check.py` lines 235 to 400 and 1690 to 1755; `tests/tools/test_prepush_check.py` lines 46 to 117 and 792 to 880; `.github/workflows/ci.yml` step 08 (lines 107 to 133); HDE Build Notes addenda 2.11 (rules 1, 2, 4, 7), 2.12 (LR6-O6, LR6-O7), 2.17 (resolution A), 2.18, 2.21 (PR35-C1); Glow QA Guide §10.6 and §3.4.8.
- **Re-running a rehearsal (optional):** E1 and E3 take seconds in any clone (`git clone --shared` of a packed scratch repository, then `git hash-object -w` of an existing blob, with the tool's `repository_state()` before and after). A full check 13 step-1 run needs a **full-history** clone (a shallow one does not engage the mechanism), CI's install on Python 3.12, `ruby` on `PATH`, and about 25 to 45 minutes; git 2.43 suffices, since the behaviour is version-independent (§4.4).
- **Writes:** only its review and any addendum, under `docs/ephemeral/`.
- **Not needed:** production, vendor, Railway or database access.
- **Order:** this proposal's pull request is merged first.

## 16. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | `GCFPE-USE-HDE-CRD-0002-ESC-30-20261025-QA110-F01-01` |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1, with Specification delta 01 |
| requirement / work unit | S20; QA Plan v1.2 check 13, task T13, attempt 1; finding QA110-F01; proposed WU-REM-02 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, https://app.notion.com/p/3f44590a05eb81e385dbd4fe337ad9d9 (page state as of 2026-10-12T02:29:51.552Z) |
| role/stage | continuing Thoth, ESC-30 (first proposal for QA110-F01) |
| capture time | 2026-10-25T03:25:00Z |
| execution identity | https://claude.ai/code/session_01RxSyQc1jdJZ9VtegkPWSNf (no worker subagents), carrying the role from https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum |
| result | REMEDIATION_PENDING (this proposal); next ESC-40 |
| inherited usage | `GCFPE-USE-HDE-CRD-0002-ESC-10-20261025-01` (the escalation report §"Provenance") and those it lists |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main` at 1643768); recorded here only |

## Canon relied on

Read from `docs/pfcanon/` on `main` at 1643768; this branch edits no `docs/pfcanon/` file. Each source maps to the decision topics it governs.

| Decision topic | Sources and sections |
| :- | :- |
| This prompt's contract: inputs, step 1 to 6, `AUTHORING_CONTEXT`, discovery against remedy, no Specification change, no Plan, vehicle, Proceed or addendum, routing, the handoff form | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, fetched and read in full in this invocation ("Required inputs", "Execute" 1 to 6, "Required result", "Result routing", "Runtime artifacts, readback, and handoff", "Carried conflict and decision lineage") |
| The remediation route, the return owner, one coherent approved basis, the attempt limit | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6 "Remediation QA evidence and review rules" ("Artifact and owner boundaries"; "Common remediation cycle and return owner" steps 1 to 5), read in full |
| Non-QA-root remediation, Moon Loop boundary, independent defects (O-1) | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.8 "Rails posture for manual Live QA" ("Hard boundary"; "Non-QA-root remediation boundary"; "An independent or opportunistic defect requires separate Product Owner disposition"), read in full; PF06-Canon-Change-Process-Guide v2.5.4 the Extended Moon Loop conditions (the passage ending "An independent or opportunistic defect requires separate Product Owner disposition"), read |
| The non-mutating rule | PF19-Canon-Glow-QA-Guide v3.0.6 §2.2.11 "Evidence-governed CI sequence (names-only)": "A non-writing check MUST NOT mutate the repository or external state" |
| Republication of a check | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.3 "Evidence layout: current-state first" (opening) |
| Classification of the finding | PF27-Canon-Plan-Templates v2.0.5 "Exact status predicates" and "Causal precedence", read in full |
| PF10 authority, business case, real inputs, finding disposition, no ceiling | PF10-HDE-Build-Notes v13.7.8: addendum 2.11 ("Rule" 1 to 8; "Findings behind the rules"; "Scope and supersession"), read in full; addendum 2.18 ("Rule" 1 to 6), read in full; addendum 2.14 ("Rule" 1 to 6; the P1 exception), read in full |
| WU-PR-06's acceptance, stated limits, D-1 and the independent checks' venue | PF10-HDE-Build-Notes v13.7.8 addendum 2.12 ("Approval and source record"; "The review's independent checks on merged main fc51620"; LR6-O1, LR6-O3, LR6-O6, LR6-O7), read |
| What blocks a v2 SATISFIED decision | PF10-HDE-Build-Notes v13.7.8 addendum 2.17 ("Resolved": resolution A; "What blocks SATISFIED"), read |
| The option A line, the hosted image and git 2.55, PR35-C1, FND-028 | PF10-HDE-Build-Notes v13.7.8 addenda 2.16 ("Option A line"), 2.21 (PR35-C1 row; run 39697136314's image and git version), 2.26 (triage v1.1 Product Owner items FND-028, FND-024), read |
| The FND-001 precedent for a remediation proposal's form and lineage | PF10-HDE-Build-Notes v13.7.8 addenda 2.23, 2.24, 2.25 (headings and summaries); `docs/ephemeral/HDE-CRD-0002-remediation-proposal-FND-001-v1.1.md` and `docs/ephemeral/HDE-CRD-0002-remediation-review-FND-001-v1.1.md`, read |
| Repository rules | `AGENTS.md`: canon-first rule; closed rails; search tooling; pytest readiness; pre-push check; "Code review guidelines" (real-input rule); "Evidence attribution, currentness and distinct decisions"; "PR descriptions"; the truncation guardrail |
| In-flight documents | The escalation report v1.0 (in full); the QA-110 review v1.0 §6, §7; the check 13 primary (in full); the QA-100 results v1.0 §2, §5.2; QA Plan v1.2 §3.2, check 13, §9; QA Audit v1.0 §7 (header and item 9); the QA-90 collection v1.0 §2 and §4.3; Specification v1.1-approved (S20 row, Live QA table); Specification delta 01 (S20 unchanged); Implementation Plan v1.1 §7 WU-PR-06; Plan delta 01 v1.1 (overlay form); the WU-PR-06 instruction v1.0 (ID-2, ID-3, §5.7, §5.8); the WU-PR-06 lineage review v1.0 (§5, §7); the postmortem v1.1 (D-1 rows); the Product Owner direction on tool-version pinning v1.0 (`PENDING_DRAINAGE`; bears on git versions, which §4.4 shows are not the factor) |
| Repository facts | `tools/ci/prepush_check.py` (blob 4dc098566620): `_git_env`, `_metadata_digest`, `repository_state`, `make_copy`, `in_copy`, `child_environment`, `report_replay`, `_execute`, `main`; `tests/tools/test_prepush_check.py` (blob 8d2c0be36e2e): `_git`, `_snapshot`, `_run`, `_clone`, `_synthetic`, `_clone_at`, the tests named in §4.3, `test_tool_installs_no_hook_fetches_nothing_and_opens_no_network`; `.github/workflows/ci.yml` (blob 3836bad11c39) steps 08, 14, 15 (`git worktree add --detach`); `README.md` "Pre-push check (HDE-CRD-0002)"; `ci/checks/classify_ci_changes.py` line 861 (the owner-test registration) |

Canon searched (`git grep -n -i` on `origin/main -- docs/pfcanon/`) for `freshen`, `alternates`, `--shared`, `hardlink`, `shallow`, "read-only command", "writing nothing" and "non-writing": no PF section speaks to git object-store borrowing or to shallow clones; the hits are the Glow QA Guide §2.2.11 rule and the PF10 addenda already listed, plus unrelated uses of "alternates" (spelling and serializer rules). Canon is silent on the mechanism, so ID-2's reading and S20's text govern, as §4.5 applies them.

ASK OK?
