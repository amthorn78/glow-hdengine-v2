---
artifact_type: RESCOPE_REQUEST
artifact_id: HDE-EPIC040-PR02-F02-RESCOPE-REQUEST
artifact_version: 1.0
status: RESCOPE_PENDING
decision: NOT_YET_REVIEWED
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
finding_ref: HDE-EPIC040-PR02-F02
review_thread_ref: 3997351898
originating_stage: RS-40 continuation of proceeded PR-30
producer_role: dedicated PR02 engineer
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: PR-02 HDE-EPIC040
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR02 / RS-40 / F02 executing-code coherence / PR404
context_conflict: NONE
ecosystem_release: GCFPE-20260913.1
prompt_version: 091326.2
selected_membership_count: 54
created_at_utc: 2026-09-13T17:39:41Z
---

# HDE-EPIC040-PR02 — F02 Executing-Code Coherence Rescope Request v1.0

## 1. Requested decision and exact finding

State: **RESCOPE_PENDING**. F01's owning-Gate-schema delta is approved and its substantive manual drain is verified. This new request addresses only the separately retained executing-module/source question, GitHub thread [3997351898](https://github.com/amthorn78/glow-hdengine-v2/pull/404#discussion_r3997351898).

The published loader can return a bundle representing current disk source while previously imported code executes. The preserved local continuation tries to fix this by hashing its source file during import, removing its shared serializer import, and copying the category order. A fresh adverse experiment proves that attempt still accepts B's manifest/source hash when Python executes A from a valid stale timestamp-based bytecode cache. Freshly compiled B refuses on those same disk inputs. It is not a completed repair and is not authorized by F01 merely because it exists in the preserved directory.

A minimal standalone experiment shows that retaining the actual module execution code object and comparing it with compilation of the captured source can distinguish those A/B cases. Completing that approach while preserving existing shared owners would require two additional manifest-bound first-party helper sources, beyond the approved 42-member set. Section 4 supplies the exact proposed delta and explicit limits. No compliant complete local repair was established under the current 42-member authority; this is not a claim that every possible design has been disproven.

## 2. Identity, immutable authority and existing work

| Field | Preserved/observed value |
|---|---|
| Change / work unit | `HDE-EPIC040` / `HDE-EPIC040-PR02` |
| Dedicated engineer | `PR-02 HDE-EPIC040`; user-assigned continuing role, not an invented platform session identity |
| Execution / disposition | `MANUAL_PROMPT_EXECUTION` / `RETAIN_EXISTING` |
| Same IA receiving review | `Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent session`, exactly as identified in the approved F01 review; not Isis-50 |
| Repository / PR | `amthorn78/glow-hdengine-v2`; https://github.com/amthorn78/glow-hdengine-v2/pull/404 |
| Current remote lifecycle | Open, draft, unmerged; two attributable commits; no publication in this invocation |
| Branch / base branch | `hde-epic040-pr02-immutable-admission` / `main` |
| Accepted base | `3828d4b3454259841a3e48d13039dd1475754f2f` |
| First attributable commit | `3dda87853466fa18247654ffe5bb67561364b0f4` |
| Current remote head | `eed8a63807f573abc29de6f6d5ceac54f0c8da85` |
| Current remote tree | `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d` |
| Recorded recovery directory | `/workspace/scratch/b736cdb96988/pr02-recovery`; preserved files accessible, Git metadata absent in this environment |
| Original user workspace | `/workspace/scratch/8d666e9ba95b/glow-hdengine-v2`; not accessible at that path in this environment; no deletion or modification was performed |
| Original Proceed | Preserved by implementation Result v1.0 §1 and the approved F01 review; remains the same implementation authority |
| Accepted PR01 | PR #403 remains accepted and final; no rerun or reopening |
| Actual release manifest | Still the current 15-member file; no release cut or promotion |

| Role | Exact source | SHA-256 |
|---|---|---|
| Approved Specification | [HDE-EPIC040-specification-v1.1-approved.md](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk) | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| Immutable whole-change Plan | [HDE-EPIC040-implementation-plan-v2.1.md](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk) | `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| Approving Plan review | [HDE-EPIC040-implementation-plan-review-v2.1.md](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk) | `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| PR02 Instruction | [HDE-EPIC040-PR02-pr-instruction-v1.0.md](https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk) | `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c` |
| PR02 detailed Plan | [HDE-EPIC040-PR02-pr-implementation-plan-v1.0.md](https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk) | `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0` |
| Original implementation Result / Proceed | [HDE-EPIC040-PR02-pr-implementation-result-v1.0.md](https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk) | `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0` |
| Original F01 proposal | [HDE-EPIC040-PR02-rescope-proposal-v1.0.md](https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk) | `d4892199b87482224b96153c40de91e7037d8cd4c96c7e7d7d41255cff007da3` |
| Approved F01 review | [HDE-EPIC040-PR02-rescope-review-v2.0.md](https://drive.google.com/file/d/1rNSVietXHUCA8OG2xUWHeOHcQbFsUmKK/view?usp=drivesdk) | `86509f67869c0a95e8b9e1035dc0dbebe4ca19f9d3ea8005127426bed075ffc8` |
| Approved F01 addendum | [HDE-EPIC040-PR02-PF10-build-notes-addendum-v2.0.md](https://drive.google.com/file/d/17-TV-9KeP0c0KmHuhogik_uyYXyBqNPV/view?usp=drivesdk) | `5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d` |
| Current authoritative PF10 | [PF10-HDE-Build-Notes-v13.2.1.md](https://drive.google.com/file/d/1zCDNwfUjs9sqVZWK-nY2rGFmnpMg4RF1/view?usp=drivesdk) | `5c0f6f96a52b8821cb7826d492b0066322bf5eb12b48eff5b390eee002e5a7c9` |
| Selected operating procedure | [GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v3.1.0-20260913.md](https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk) | `c62dde03425b09e1b8bc51b6cc5d870392075e8a0e0cd21ad961c7ecdc6d8e7c` |

The Specification's actual approving owner is Thoth-17, APPROVE at 2026-09-08T13:23:24Z. Whole-change Plan v2.1's actual independent approving review is Isis-50, APPROVE at 2026-09-09T13:36:43Z. Both remain immutable. The same whole-change IA reviewing F02 is distinct from that independent reviewer.

Selected runtime prompt: [RS-40 — Approved Rescope — Resume PR Implementation — 091326.2](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204). The [GCFPE Membership and Release Register](https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1?pvs=204) explicitly selects GCFPE-20260913.1 / 091326.2, exactly 54 members. RS-20 was read as the destination; no RS-20 decision was executed by this session.

### 2.1 Verified F01 drain and current PF10

The Product Owner's RS-40 invocation supplies the manual-drain assertion. The original handoff-linked PF10 is an earlier version ending at §2.6. Independent discovery in `Glow / Core Docs / PFCanon` found the current PF10 with §2.7, **HDE-EPIC040-PR02 — Rescoping**, followed by §2.8, **PF10-FORM-001 — Establish Page-Ready Canonical Form for Agent-Authored Addenda**. The current file's front matter identifies v13.2.1, effective September 13, 2026, and its current-version rule governs selection; the earlier file is not used as current authority.

Every substantive section 1–9 of the exact approved F01 addendum matches the drained §2.7 after accounting only for Markdown heading depth, escaping, hyperlink display, table separators, bullet markers and trailing whitespace. The seven-part bounded overlay, requirement effects, dependencies, findings, exclusions, alternatives, recovery/CI order, and carried conflict register are all present. The drained entry names the exact review v2.0 and same decision owner; the fetched review in turn binds the exact standalone addendum link and immutable base hashes.

This is substantive delta equality, **not a byte-identical whole-file claim**. The standalone YAML/front matter and its final §10 manual-drain/transport directions are not copied into §2.7. Those directions are already supplied by this invocation and the selected RS-40 prompt; they add no omitted technical delta. No implementation relies on §2.8 as a substitute for the manual drain. No PF10 file or addendum was edited.

The verified effective F01 overlay adds `schemas/gates_v1.schema.json` as member 42; captures it from the same selected root with exact manifest-bound path/bytes/hash/size/canonical form/local references; executes its owning schema before active admission while retaining shared relational validation; refuses all missing, extra, invalid, changed or unbound cases without a partial handle or fallback; updates only synthetic complete-release fixtures in PR02; and leaves actual manifest materialization, final identity recomputation and promotion to PR06. All exclusions in the F01 approval remain effective.

Folder provenance was checked through Glow → Core Docs → PFCanon and a direct-child controlled-Markdown listing, with matching parent metadata. The current PF10's own current-version and addendum-supersession rules distinguish the newer active version from earlier surviving files. No native Google Doc or Office PFCanon content was used.


## 3. Source-backed material boundary

The immutable detailed PR02 Plan §5.1 requires one owned byte-capture pipeline; §5.2 fixes the root and restricts schema authority to captured sources; §5.3 fixes the exact roster, now overlaid to 42 by F01; §5.4 requires the existing schema/relational implementations; §5.5 separates captured-source and manifest identities. Whole-change Plan §§4.3 and 5.5 preserve one actual validation path and exact captured-source identity. Instruction §6 retains the shared pipeline, absence of fallback and complete-or-refuse active handle.

Current PF10 §2.7.6 and F01 review v2.0 §7 explicitly exclude thread 3997351898 from F01 approval, prohibit an unmanifested authority/import-reload/deployment solution, and require one new formal request if no compliant local repair exists. The current roster contains `engine/config/registry_loader.py` and `engine/serializer/canon.py`, but not `engine/stable/sercanon.py` or `engine/categories/registry.py`. The published loader imports `canon` and `FROZEN_MAGIC10_ORDER`; `canon.sercanon` delegates to `engine.stable.sercanon.serialize`. Thus the two named omitted files define actual first-party behavior/constants used by the admission path. This is distinct from the approved Gate-schema member-42 correction.

The proposed additional code comparison is not supplied by the current source-byte digest. The new experiment makes that distinction observable through a material refusal change, not merely a differing SHA. The proposal requires an explicit new roster decision and a defined code-equivalence claim. The engineer cannot approve those by changing tests or relying on historical security/CI results.

## 4. Exact proposed bounded delta — pending IA decision

Request a bounded F02 overlay against the same immutable base, retaining the verified F01 overlay. The following is **proposed, not authorized**:

1. Make active-admission code coherence a separate checked predicate: the already executing first-party admission implementations must match the compiled form of their exact captured, manifest-bound source bytes before an active bundle is returned. Keep existing source-byte hashes, configuration hashes and `release_id = sha256(manifest bytes)` unchanged. Do not claim that code-object equality proves which original raw source bytes Python imported.
2. Preserve the existing shared serializer and category authority. Remove the preserved local attempt's duplicate `_canonical_json_bytes` serializer, copied category-order definition and import-time disk-hash substitute as part of a later authorized coherent correction. This request itself changes none of those files.
3. Add exactly two existing first-party helper sources to the effective synthetic admission roster: `engine/stable/sercanon.py` and `engine/categories/registry.py`. The former defines the serializer called through already-rostered `engine/serializer/canon.py`; the latter defines the frozen category order imported by the published loader. Both were inspected and are absent from the effective 42-member roster. The proposed complete roster becomes **44**, namely the F01 42-member set plus these two paths. No other member is proposed. Sorted roster order remains authoritative; “43/44” denotes the two additions, not a hard-coded alphabetical row position.
4. In the four existing modules `engine/config/registry_loader.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py`, and `engine/categories/registry.py`, retain a private immutable reference to the actual top-level code object while that module executes, using the executing frame rather than reading its file. At admission, compile each corresponding captured source with the same interpreter/optimization semantics and compare to that retained code object. Compilation validates code; it must not execute the captured module, reload imports, mutate `sys.modules`, choose another root or introduce a second validator. Keep these implementation details private and out of public/API/CLI contracts.
5. Fail closed with an owning internal typed refusal if an expected module, its usable code provenance, exact captured source member, safe origin, compatible compilation semantics or code comparison is unavailable or mismatched. No disk-hash guess, bytecode-cache timestamp/size, source inspection fallback, permissive platform fallback, selector or prior active handle may substitute. Pin the expected module references internally; do not accept caller-supplied code/module identities.
6. Bind the two added helper files through the same existing exact path, bytes, hash, size, canonical member format and unchanged-source capture. Keep one physical manifest read per admission attempt and retain the existing bounded final metadata/change-detection pass. The approved Gate schema remains a required captured owning schema.
7. Limit the new claim to the active-admission validation/serialization/category implementation closure identified above. It is not a universal attestation of every imported package, arbitrary in-memory mutation, all application runtime code, deployment atomicity or all forty-four roster members' future execution. Existing third-party/stdlib dependency policy is unchanged. This bounded guarantee and its limits require an explicit IA disposition; this engineer does not label them already sufficient for the Specification.
8. PR02 owns the internal predicate, helper-source capture, synthetic 44-member fixtures and adverse tests. The actual current 15-member manifest stays unchanged. PR06 retains final manifest materialization, identity recomputation, evidence convergence and eventual promotion, with a proposed effective complete roster of 44 only after this delta is approved and manually drained. PR03–PR05 retain their existing functional owners and dependency order; future complete fixtures adopt the approved roster. PR07 later documents the delivered boundary and its limits. No new unit, deployment protocol, immutable-deployment requirement or earlier-unit rerun is added.

This is a concrete architecture/roster proposal for review, not a replacement Plan. The passive code-provenance mechanism was tested only in a tiny synthetic feasibility case. Full behavior, private-test-root compatibility, safe public module-origin binding, compiler/debug metadata handling, candidate-loader compatibility, imports, exception behavior, ownership classification and current-head review remain implementation obligations if approved. No complete implementation is claimed.

Code-object equality can accept different raw text when it compiles to the same code representation. The manifest still hashes exact current source bytes; the new predicate would establish executable-code equivalence, **not historical imported-source byte identity**. If the intended requirement instead demands proof of the exact original raw bytes used by the interpreter, this proposal cannot establish it and must not be approved as if it did. That stronger guarantee would require a separately authorized source-to-execution trust boundary; no import hook, reload scheme or deployment mechanism is proposed or authorized here.

The IA must decide whether this exact bounded predicate, scope and 44-member roster are sufficient within the approved Specification. If they are not, return precise native redlines or the actual Specification/Product Owner question; do not approve an unspecified larger mechanism, infer a waiver, or send the approved base back for replacement.


## 5. Proposed validation and acceptance effects

Requirement wording and public identity formulas remain unchanged. K040-REQ-006/007/008/009 and AC040-04/05 receive additional implementation/evidence burden only if the IA approves this exact F02 delta.

Required focused proof for a later approved implementation:

- Exact 44-member synthetic success; 42- or 43-member incompleteness and an unapproved 45th member refuse. Both new helper members receive missing, malformed, changed, wrong-hash and wrong-size cases.
- Fresh matching module code accepts; loader, canonical wrapper, serializer implementation and category module code changed before or after import refuse when their captured compilation differs.
- A valid timestamp-based stale `.pyc` containing A while the source/manifest represent materially different B is refused; demonstrate that A and B actually differ in behavior, not only in a digest.
- Missing/unsupported provenance fails closed without breaking unrelated candidate APIs or silently selecting a fallback. Private synthetic-root tests retain their explicit non-production role; public-root/origin tests cannot be satisfied solely by monkeypatching `__file__`.
- Actual owning Gate schema execution, remote/unbound reference refusal, duplicate-aware canonical bytes, exact Gate input, source-change checks, recursive freeze, alias protection and no stale active fallback remain covered.
- Count actual packaged-manifest reads on success and appropriate adverse paths, rather than merely asserting a helper's logical cache count; retain manifest-change-after-initial-read refusal using captured metadata.
- Exercise the existing shared serializer and category owners and their consumers; do not duplicate implementations to make source closure smaller. Do not modify the actual 15-member manifest or existing owned data/schema semantics.
- Run the necessary targeted suite, default regression, nine governed writer/evidence checks, changed-path ownership/classification and clean-worktree checks locally before one meaningful commit/push. New source ownership must be registered in the existing classifier as necessary.
- After the coherent authorized correction, obtain substantive code and security review for the current head, resolve applicable findings through the repository review owner, and run CI once against the exact final candidate. Do not spend CI on a known blocked candidate.

No current test result satisfies these proposed future predicates. The passive code-object comparison is not a cryptographic trust anchor, arbitrary in-process tamper proof or stronger portability promise. The approved non-atomicity limitation remains unchanged.


## 6. Alternatives, recommendation and interim treatment

| Alternative | Evidence / disposition requested |
|---|---|
| Passive actual-code provenance plus the two manifest-bound helper members | Recommended bounded F02 proposal. It avoids source-file reads at import, keeps existing owners and identity formulas, and the tiny stale-bytecode experiment supports feasibility. Complete implementation and independent review are still required. |
| Preserve the current local import-time disk hash | Not a valid complete repair: the stale-bytecode experiment admits B's identity while cached A executes. |
| Preserve a second serializer and copied category order in the loader | Not accepted: it changes authority/ownership to avoid dependency closure and does not fix the actual-code proof. |
| Keep 42 members and validate helper source from outside that set | Not authorized by F01: it creates additional unmanifested source authority. |
| Add imports/reloads, custom import hooks, immutable deployment, cross-process locks or an atomic release-root protocol | Outside this proposal and the existing approved limits. No implementation or blanket authorization requested. |
| Explicitly accept only captured-disk identity and waive executing-code coherence | Not assumed. The same IA must classify whether any such narrowing is compatible with K040-REQ-006/007/008/009 and AC040-04/05; a product/Specification change belongs to the actual owner. |

Interim treatment: retain the remote PR and every local change unchanged. Do not publish the preserved source-binding attempt, complete reviews by declaration, resolve the threads, or run CI. F01 remains valid within its exact drained scope; no accepted work, immutable Plan or original Proceed is revoked. This request concerns the separately retained F02 question only.


## 7. Separate findings, review, CI and validation history

| Finding | Current disposition / owner |
|---|---|
| `3997320377`, `3997320916` / F01 | Authority approved and substantive drain verified. Prior local files contain the schema/42-member delta; no completed current-candidate test, review or publication claim. Engineer owns completion and proof. |
| `3997320380` | Preserve the remote-head deployment-symlink correction; final current-head review disposition remains with the repository review owner. |
| `3997320917` | Preserve the remote-head bounded inter-read correction and its explicit non-atomicity limit. The local attempt changes the mutation-test target while skipping a second physical manifest read; not yet accepted. |
| `3997351895` | Ordinary in-scope repair. Preserved local code skips the manifest's second byte read and retains final identity checks; a read-count test exists. Completion and adverse proof remain with the engineer. |
| `3997351898` / new F02 | Unresolved material executing-code/source boundary. Remote behavior and the preserved attempt's stale-bytecode bypass were reproduced. Exact proposed additional scope is in this request; approval belongs to the same whole-change IA through selected RS-20. |
| `3997351903` | The requested atomic multi-file guarantee conflicts with the explicit approved limitation. Preserve that classification and the observed residual window; do not call the thread repaired, waived or a false positive. |
| Security comment `5648272341` | Historical no-findings evidence for `eed8a638…` only; no changed-source security review, acceptance or waiver. |


Historical evidence remains attributed to `eed8a63807f573abc29de6f6d5ceac54f0c8da85`: 472 targeted tests passed; 1,724 default-regression tests passed with three existing closed-rails vendor skips; nine writer/evidence checks passed; all seven applicable CI lanes passed in run [34715034846](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34715034846); code review [5187778352](https://github.com/amthorn78/glow-hdengine-v2/pull/404#pullrequestreview-5187778352) retained blockers; security comment [5648272341](https://github.com/amthorn78/glow-hdengine-v2/pull/404#issuecomment-5648272341) reported no security issues for that head.

The current workflow read reports that run completed successfully. There was no active returned PR-head run to cancel. No CI was triggered, rerun, awaited as a completion gate, or billed through a new action in this invocation. All seven returned review threads remain unresolved. Author replies and historical passes are not review acceptance.

This invocation executed only the three bounded local synthetic experiments recorded below, under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`, Python 3.12.14. They are diagnostic/feasibility evidence, not a completed PR test suite, QA execution, production test or security review. Targeted/regression/writer/classifier/clean-Git-worktree checks for a final candidate, substantive current-head code/security review and final candidate CI are **NOT EXECUTED** because no authorized complete candidate was established.


## 8. Recovery and preserved work

The remote recursive tree was retrieved completely (`truncated: false`) and compared without modifying the recorded recovery directory. Of 5865 remote tracked blobs, 573 accessible files matched their Git blob identity, four differed, and 5288 were not available at their expected paths. This is an incomplete local materialization, not evidence that the remote repository lost files. The local directory has no Git metadata, so no local HEAD, staging state or clean-worktree claim is made. The remote branch and ordered commits are independently verified.

The four existing differences were already present before this invocation. No author or prior-session execution timestamp is inferred. Three contain the resumed schema/read-count work plus a source-binding attempt. The fourth is a terminal-newline difference in `tests/artifacts/test_cli_text_artifacts_bom_lf.py`; preserve it separately and establish its intended ownership before any later commit.

| Preserved local file | Bytes | SHA-256 |
|---|---:|---|
| `engine/config/registry_loader.py` | 68380 | `79fa00ca3dcb5c9b311ae1174aa8b1d7f9ddac4d72a786d42fbb4f995369a556` |
| `tests/artifacts/test_cli_text_artifacts_bom_lf.py` | 858 | `c3279c6654e58d1b2c6fd6ef9f298c553ff74ef9056784885fc179f12b137d59` |
| `tests/config/helpers.py` | 4668 | `cea929551e632fd85428219092a66a19b038f5c6ef739cd770a0e7323fcd7335` |
| `tests/config/test_production_admission.py` | 27750 | `fbfed8cfce48e6024296fc765d5aea5dfd46a5ec3962d24896dd659545084262` |

The recorded original workspace is inaccessible in this environment; the historical Result documents its preservation and unrelated work. This invocation did not delete, alter, restore over, or recreate that original path. It did not initialize a new checkout, create a branch, rebase, reset, clean, commit, push, close or merge anything. Reconstitution of missing Git metadata/files in the same recorded recovery directory remains an engineering recovery obligation before future mutation/publication; it is not a request for Nathan to rebuild the repository or issue a new Proceed.

The complete four-file local delta against the exact remote head is embedded in Appendix B. That delta preserves the prior work; it is not an approved patch or a recommendation to apply the attempted serializer/category/source-hash changes. All synthetic probes used newly created temporary fixture directories outside the preserved worktree. They are test data, not replacement engineering workspaces.


## 9. Carried Canon-conflict register

The complete immutable C040 proposal/decision history remains in whole-change Plan v2.1 §11 and its actual approval; the current disposition is preserved from F01 review v2.0 §10 and current PF10 §§2.2–2.7. Neither the earlier proposal history nor its permanent-drainage owners is reauthored here.

| Item | Exact carried decision/current treatment |
|---|---|
| C040-01 | `CANON_RECONCILIATION / APPROVED`, Thoth-17, 2026-09-08T13:23:24Z; PF10 §§2.2/2.4 retained. |
| C040-02 | Same approved Thoth-17 decision; PF12 identity history and PF10 §§2.2/2.4 retained. |
| C040-03 | Same approved Thoth-17 decision; PF14 identity history and PF10 §§2.2/2.4 retained. |
| C040-04 | Same approved Thoth-17 decision; PF19 identity history and PF10 §§2.2/2.4 retained. |
| C040-05 | `CANON_RECONCILIATION / APPROVED`, alternative A, Isis-49, 2026-09-09T03:57:16Z; PF10 §2.3 retained; permanent PF14 maintenance remains separately owned. |
| C040-06 | `NEW_CANON / APPROVED`, alternative A, Isis-50, 2026-09-09T11:48:08Z; exact thirty-six-row taxonomy and sixteen-state conformance retained in PF10 §2.5. |
| HDE-EPIC040-PR02-F01 | Review v2.0's source-native state remains `APPROVED_PENDING_MANUAL_PF10_DRAIN` as history. This invocation verifies its substantive delta in current PF10 §2.7; only its member-42/owning-schema scope is effective. |
| HDE-EPIC040-PR02-F02 | **New finding identifier assigned in this invocation.** Proposed bounded implementation delta concerning thread 3997351898. Not yet reviewed or approved; no decision time or new Canon approval is invented. |

F02 is not an automatic new Canon decision. Its affected requirements are K040-REQ-006/007/008/009 and AC040-04/05; exact sources, alternatives, recommendation, interim treatment and risks are set out below. Existing permanent Canon drainage remains with its existing owners. No new permanent-document change is authorized by this request; the IA must identify any actual owner impact in its decision.


## 10. Exact native review request and return

Run **RS-20 — Review Bounded Work-Unit Rescope — 091326.2** at https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204 in the same `Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent session` that issued F01 review v2.0. This engineering session does not run that review or contact another session.

Review this new `RESCOPE_REQUEST` as its actual artifact type. Classify the exact proposed F02 delta using the selected native outcomes. The requested decision is whether passive code-object/source equivalence for the four named modules, with the two named additional manifest members, is a sufficient bounded correction within the approved Specification. Approval must expressly address executable equivalence versus exact historically imported bytes and the limited first-party closure. Do not treat the feasibility probe as production proof or silently strengthen the guarantee.

If approved, the same IA records one exact `RESCOPE_REVIEW` and exactly one standalone qualifying PF10 build-notes addendum with explicit scope and exclusions. The current selected handoff still requires Nathan's manual drain/verification before affected implementation. Preserve current PF10 §2.8's page-ready content requirement when authoring the substantive addendum; any prompt/form tension must be reported explicitly, not repaired by this engineer or used to omit the required standalone addendum. The downstream engineering return is selected RS-40 in `PR-02 HDE-EPIC040`, using the same PR, branch, recorded recovery directory, preserved work and original Proceed. No replacement Plan, Instruction, workspace or Proceed is requested.

If classified as in-scope repair, provide the exact source-grounded reason and complete bounded return required by the selected RS-20. If rejected or revision-required, preserve this request and all work and return the native reason/redlines. A genuine Specification/Product Owner decision is terminally returned by its owning prompt; this request does not preselect or impersonate that decision.

No RS-10 insertion, PR-30 restart, IA-30/IA-40 Plan replacement, PR01 rerun, agent invocation of PR-50, merge, PF10 edit, QA/Ops, vendor/database contact, deployment, release activation or Epic closure is authorized. Nathan is asked only to relay the completed selected-prompt package and, if a qualifying delta is later approved, perform the manual PF10 publication already retained in the flow.


## 11. Actual prompt-use and claim boundary

- New usage identifier: `GCFPE-USE-HDE-EPIC040-PR02-RS40-F02-20260913-01`.
- Executed selected prompt: RS-40 / 091326.2, GCFPE-20260913.1, dedicated continuing PR02 engineer.
- Exact source prompt page and its returned edit time: https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204; 2026-09-13T11:35:51.889Z.
- Capture: 2026-09-13T17:39:41Z; actual observed local runtime Python 3.12.14. No model/configuration assessment.
- Result: source/drain verification, read-only continuity inspection, preserved existing local changes, two adverse reproductions and one tiny feasibility experiment; one new pending F02 request.
- Prior use/history: original implementation Result v1.0 and F01 review v2.0 retain their actual source-bound entries; they are not relabeled as this invocation.
- No repository provenance write was attempted. Future authorized repository persistence remains non-gating and must use an actually installed supported procedure.

## Appendix A. Exact diagnostic results and reproduction steps

All three scripts exited zero. No original worktree source, actual manifest, branch or PR was changed. Fixtures are non-production data outside the engineering directory.

### A.1 Observed result

```json
{
  "probe": "exact remote eed8a638 loader imported before local synthetic source replacement",
  "synthetic_only": true,
  "manifest_roster_count": 41,
  "compiled_source_sha256": "14f95014ef70fd9a905fc3e8130cae84bf6c477c3b6b18ede028735d2cd76031",
  "disk_source_sha256": "eb6ff74ae7fa8c7a39fad8360f1d809a3ac689f44e04b9b886c8415caec818d9",
  "returned_loader_source_sha256": "eb6ff74ae7fa8c7a39fad8360f1d809a3ac689f44e04b9b886c8415caec818d9",
  "active_bundle_returned": true,
  "claim_limit": "41-member historical remote loader behavior; no new F01 implementation or production conformance"
}
```

### A.2 Observed result

```json
{
  "probe": "preserved uncommitted import-hash attempt, not remote HEAD",
  "synthetic_only": true,
  "source_path": "/workspace/scratch/2cc1d0be2240/pr02-source-coherence-probe-99cllz24/synthetic-complete-release-only/engine/config/registry_loader.py",
  "manifest_roster_count": 42,
  "compiled_source_sha256": "79fa00ca3dcb5c9b311ae1174aa8b1d7f9ddac4d72a786d42fbb4f995369a556",
  "current_disk_source_sha256": "2516101d5d52f474ace9b0f1f5cc688d679175538ba2cb422134771357ff7fab",
  "returned_loader_source_sha256": "2516101d5d52f474ace9b0f1f5cc688d679175538ba2cb422134771357ff7fab",
  "import_time_disk_hash": "2516101d5d52f474ace9b0f1f5cc688d679175538ba2cb422134771357ff7fab",
  "cached_execution_returned_active_bundle": true,
  "source_B_has_different_refusal_logic": true,
  "same_size": true,
  "timestamp_cache_preserved": true,
  "fresh_same_disk_source_result": "EXECUTING_SOURCE_MISMATCH",
  "conclusion": "cached execution admits B identity while fresh B execution refuses"
}
```

### A.3 Observed result

```json
{
  "synthetic_only": true,
  "proposal_not_implemented_in_repository": true,
  "cached_behavior": "A",
  "actual_A_code_matches_compiled_A": true,
  "actual_A_code_matches_compiled_B": false,
  "fresh_behavior": "B",
  "actual_B_code_matches_compiled_B": true,
  "limits": "A mechanism feasibility probe only; no complete implementation, compatibility, public-root, module-closure or independent review proof."
}
```

### A.4 Deterministic reproduction recipe

For the remote-head reproduction, build the existing labeled synthetic fixture outside the worktree. Replace only its loader source with the exact fetched `eed8a638…` loader bytes. Import that fixture's loader once using Python's normal file-spec machinery. Change the fixture's loader source, recalculate only the fixture manifest using that loaded module's 41-path roster, and invoke its public no-argument admission. The returned source identity binds changed disk bytes, whereas the loaded implementation remains the original. The original remote loader SHA-256 in A.1 matches original Result v1.0.

For the preserved-attempt reproduction, build the current local helper's labeled 42-member fixture. Compile its preserved loader source A to a normal timestamp-based `.pyc`. In the fixture only, replace the single occurrence of `imported is None` with equal-length `imported != None` to form B; keep source size and timestamp identical so the standard cache remains valid. Rebuild the fixture's manifest from B's exact bytes. Import through `spec_from_file_location`, registering the temporary module in `sys.modules` for dataclass handling, and call its public admission function. Cached A executes and admits B's identity. Remove only that fixture's `.pyc`, import the same B source under a fresh temporary module name, and call again: B returns `EXECUTING_SOURCE_MISMATCH`. The source A digest in A.2 matches the preserved-local-file table. This probe changes a refusal condition, so its A/B difference is behavioral.

For the passive-code feasibility probe, use this complete synthetic module A:

```python
import sys
EXECUTED_MODULE_CODE = sys._getframe().f_code
def behavior():
    return "A"
```

Compile A to a timestamp-based cache, replace only `return "A"` with `return "B"`, preserve size/mtime and import as above. Compare the retained actual code object with `compile(source_bytes, observed_code.co_filename, "exec", dont_inherit=True, optimize=sys.flags.optimize)`. Cached A equals compilation of A and differs from compilation of B. After removing the fixture cache, fresh B returns B and equals compilation of B. This is not the proposed production implementation or a complete source-closure test.

## Appendix B. Complete preserved pre-existing delta against remote head

This is recovery evidence. Do not apply it as an approved patch. It contains the prior attempt's out-of-scope/unproven source-binding work as well as F01/read-count changes and the separate newline change. The exact remote base for every diff is `eed8a63807f573abc29de6f6d5ceac54f0c8da85`.

### `engine/config/registry_loader.py`

Pre-change remote SHA-256: `14f95014ef70fd9a905fc3e8130cae84bf6c477c3b6b18ede028735d2cd76031`. Preserved local SHA-256: `79fa00ca3dcb5c9b311ae1174aa8b1d7f9ddac4d72a786d42fbb4f995369a556`.

```diff
--- a/engine/config/registry_loader.py
+++ b/engine/config/registry_loader.py
@@ -18,9 +18,33 @@
 from referencing import Registry, Resource
 from referencing.exceptions import NoSuchResource
 
-from engine.serializer import canon
-
-from engine.categories.registry import FROZEN_MAGIC10_ORDER
+
+def _capture_imported_source_identity(
+    source_path: str,
+) -> tuple[str, int] | None:
+    """Remember the exact admission source present when this module imported."""
+    try:
+        path = Path(source_path)
+    except (TypeError, ValueError):
+        return None
+    if not path.is_absolute():
+        return None
+    try:
+        raw = path.read_bytes()
+    except OSError:
+        return None
+    return hashlib.sha256(raw).hexdigest(), len(raw)
+
+
+_IMPORTED_ADMISSION_SOURCE_IDENTITY = _capture_imported_source_identity(__file__)
+
+
+def _canonical_json_bytes(value: object) -> bytes:
+    """Serialize the loader's canonical-byte comparison without an internal import."""
+    return (
+        json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
+        + "\n"
+    ).encode("utf-8")
 
 
 # PF12 — HDE Schemas & Artifacts, §2.1 owns the closed Gate domain 1..64,
@@ -139,6 +163,20 @@
 # order unless an owning contract declares set semantics.  The current Magic-10
 # calculators consume these values as tuples in catalog order.  Freeze the exact
 # ordered input contract here without sorting or deduplicating it.
+FROZEN_MAGIC10_ORDER = (
+    "harmony",
+    "heat",
+    "communication",
+    "alignment",
+    "comfort",
+    "consistency",
+    "expansion",
+    "creativity",
+    "drive",
+    "balance",
+)
+
+
 FROZEN_MAGIC10_INPUTS = {
     "harmony": ("rapport_delta", "resonance_strength"),
     "heat": ("spark_intensity", "momentum_flux"),
@@ -421,6 +459,7 @@
     "migrations/005_identity.sql",
     "presenter/reader_v1/emitter.py",
     "schemas/channels_v1.schema.json",
+    "schemas/gates_v1.schema.json",
     "schemas/magic10_compat_result_v1.schema.json",
     "schemas/magic10_mechanics_v1.schema.json",
     "schemas/magic10_result_v1.schema.json",
@@ -429,7 +468,7 @@
     "engine/serializer/canon.py",
 }))
 
-if len(ADMITTED_RELEASE_ROSTER) != 41:  # pragma: no cover - import-time invariant
+if len(ADMITTED_RELEASE_ROSTER) != 42:  # pragma: no cover - import-time invariant
     raise RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")
 
 @dataclass(frozen=True)
@@ -554,7 +593,7 @@
         _validate_unicode(data)
         # Existing consumer schema documents retain their independently owned formatting.
         canonical_required = relative_path not in _CONSUMER_SCHEMAS if require_canonical is None else require_canonical
-        if canonical_required and canon.sercanon(data, sort_keys=True) != raw:
+        if canonical_required and _canonical_json_bytes(data) != raw:
             raise SchemaValidationError('NONCANONICAL_JSON', f'noncanonical JSON bytes: {relative_path}')
         return data
     except RegistryConfigError:
@@ -624,8 +663,18 @@
         self.sources[relative_path] = source
         return source
 
-    def verify_unchanged(self) -> None:
+    def verify_unchanged(
+        self,
+        *,
+        identity_only: frozenset[str] = frozenset(),
+    ) -> None:
+        if not identity_only.issubset(self.sources):
+            raise SchemaValidationError(
+                'UNBOUND_SOURCE', 'identity-only verification requires a captured source'
+            )
         for name, source in self.sources.items():
+            if name in identity_only:
+                continue
             raw, identity = _read_captured_file(self.root, name)
             if identity != source.identity or raw != source.raw:
                 raise SchemaValidationError('SOURCE_CHANGED', f'captured source changed: {name}')
@@ -1236,10 +1285,35 @@
     return tuple(identities)
 
 
+def _validate_executing_admission_source(
+    source_identities: tuple[SourceIdentity, ...],
+) -> None:
+    """Bind the executing admission code to its captured roster member."""
+    imported = _IMPORTED_ADMISSION_SOURCE_IDENTITY
+    loader = next(
+        (
+            source
+            for source in source_identities
+            if source.path == 'engine/config/registry_loader.py'
+        ),
+        None,
+    )
+    if (
+        imported is None
+        or loader is None
+        or (loader.sha256, loader.size) != imported
+    ):
+        raise SchemaValidationError(
+            'EXECUTING_SOURCE_MISMATCH',
+            'executing admission source does not match the captured release member',
+        )
+
+
 def _validate_admitted_schema_documents(capture: _MechanicsCapture) -> None:
     draft_2020 = 'https://json-schema.org/draft/2020-12/schema'
     for path in (
         'schemas/channels_v1.schema.json',
+        'schemas/gates_v1.schema.json',
         'schemas/magic10_mechanics_v1.schema.json',
         'schemas/magic10_result_v1.schema.json',
         'schemas/magic10_compat_result_v1.schema.json',
@@ -1322,11 +1396,9 @@
     manifest = _parse_manifest(manifest_source.data)
     _validate_admitted_manifest(manifest)
     source_identities = _capture_admitted_members(capture, manifest)
-
-    # schemas/gates_v1.schema.json is intentionally outside the exact release
-    # roster.  The gate domain is therefore checked by the closed loader rules
-    # below, while every roster-authorized schema is executed from this capture.
-    gates, centers = _load_gates(capture, validate_schema=False)
+    _validate_executing_admission_source(source_identities)
+
+    gates, centers = _load_gates(capture)
     channels, aliases, domains = _load_channels(
         capture,
         gate_map=gates,
@@ -1352,7 +1424,9 @@
     if not isinstance(frozen_mechanics, Mapping):  # guarded by mechanics schema
         raise SchemaValidationError('INVALID_MECHANICS', 'mechanics config must be an object')
     manifest_sha256 = manifest_source.sha256
-    capture.verify_unchanged()
+    capture.verify_unchanged(
+        identity_only=frozenset({'catalog/manifest.json'}),
+    )
     return AdmittedMechanicsBundle(
         registry=frozen_registry,
         mechanics=frozen_mechanics,
```

### `tests/artifacts/test_cli_text_artifacts_bom_lf.py`

Pre-change remote SHA-256: `d75da0d03d9e898bad4649da22cb57daffba8af88ce3677e9e07fd00f09ae746`. Preserved local SHA-256: `c3279c6654e58d1b2c6fd6ef9f298c553ff74ef9056784885fc179f12b137d59`.

```diff
Exact byte delta: append one LF byte (0x0a); no other bytes change.
```

### `tests/config/helpers.py`

Pre-change remote SHA-256: `eada86aa7856f39b67bfe3e923c2454e40b78f26fbd6112b02beab5635c04ea0`. Preserved local SHA-256: `cea929551e632fd85428219092a66a19b038f5c6ef739cd770a0e7323fcd7335`.

```diff
--- a/tests/config/helpers.py
+++ b/tests/config/helpers.py
@@ -102,7 +102,7 @@
     *,
     source_root: Path | None = None,
 ) -> Path:
-    """Build a labeled, non-production 41-member admission fixture."""
+    """Build a labeled, non-production 42-member admission fixture."""
     from engine.config.registry_loader import (
         ADMITTED_RELEASE_BUILT_AT_UTC,
         ADMITTED_RELEASE_ROSTER,
```

### `tests/config/test_production_admission.py`

Pre-change remote SHA-256: `fcb73f64acdc138d13ea9bfc65497fa1452a238ebd63aea9786e06370e3ade9a`. Preserved local SHA-256: `fbfed8cfce48e6024296fc765d5aea5dfd46a5ec3962d24896dd659545084262`.

```diff
--- a/tests/config/test_production_admission.py
+++ b/tests/config/test_production_admission.py
@@ -58,6 +58,8 @@
     assert isinstance(bundle, AdmittedMechanicsBundle)
     assert bundle.manifest.version == ADMITTED_RELEASE_VERSION
     assert bundle.manifest.built_at_utc == ADMITTED_RELEASE_BUILT_AT_UTC
+    assert len(ADMITTED_RELEASE_ROSTER) == 42
+    assert "schemas/gates_v1.schema.json" in ADMITTED_RELEASE_ROSTER
     assert tuple(row.path for row in bundle.manifest.files) == ADMITTED_RELEASE_ROSTER
     assert tuple(row.path for row in bundle.source_identities) == ADMITTED_RELEASE_ROSTER
     assert bundle.config_sha256 == hashlib.sha256(mechanics_raw).hexdigest()
@@ -116,24 +118,56 @@
     assert caught.value.code == "UNSAFE_SOURCE_PATH"
 
 
+def test_public_admission_refuses_changed_source_loaded_before_admission(
+    release_root: Path, monkeypatch
+) -> None:
+    module_path = release_root / "engine/config/registry_loader.py"
+    module_path.write_bytes(module_path.read_bytes().rstrip(b"\n") + b"\n# changed after import\n")
+    write_synthetic_release_manifest(release_root)
+    monkeypatch.setattr(registry_loader, "__file__", str(module_path))
+
+    with pytest.raises(RegistryConfigError) as caught:
+        load_active_mechanics_bundle()
+    assert caught.value.code == "EXECUTING_SOURCE_MISMATCH"
+
+
 def test_source_changed_after_its_verification_read_is_refused(release_root: Path, monkeypatch) -> None:
     original = registry_loader._read_captured_file
     reads = 0
-
-    def replace_verified_manifest(root, relative_path):
+    target = "adapter/http_reader.py"
+
+    def replace_verified_source(root, relative_path):
         nonlocal reads
         result = original(root, relative_path)
-        if relative_path == "catalog/manifest.json":
+        if relative_path == target:
             reads += 1
             if reads == 2:
                 # Initial capture was read 1. Change a source after read 2
                 # returned its old verified bytes, while other reads remain.
-                (root / relative_path).write_bytes(b"{}\n")
+                (root / relative_path).write_bytes(b'"""Changed after verification."""\n')
         return result
 
-    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_manifest)
+    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_source)
     _expect_code(release_root, "SOURCE_CHANGED")
     assert reads == 2
+
+
+def test_packaged_manifest_is_physically_read_once_per_admission(
+    release_root: Path, monkeypatch
+) -> None:
+    original = registry_loader._read_captured_file
+    reads = 0
+
+    def count_manifest_reads(root, relative_path):
+        nonlocal reads
+        if relative_path == "catalog/manifest.json":
+            reads += 1
+        return original(root, relative_path)
+
+    monkeypatch.setattr(registry_loader, "_read_captured_file", count_manifest_reads)
+    bundle = _load_active_mechanics_bundle_from_root(release_root)
+    assert isinstance(bundle, AdmittedMechanicsBundle)
+    assert reads == 1
 
 
 def test_source_removed_during_final_identity_check_has_typed_refusal(release_root: Path, monkeypatch) -> None:
@@ -256,6 +290,57 @@
     _expect_code(release_root, "RELEASE_TIMESTAMP_MISMATCH")
 
 
+def test_gate_schema_is_required_and_an_unlisted_41_member_release_is_incomplete(
+    release_root: Path,
+) -> None:
+    manifest = _manifest(release_root)
+    manifest["files"] = [
+        row for row in manifest["files"] if row["path"] != "schemas/gates_v1.schema.json"
+    ]
+    assert len(manifest["files"]) == 41
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "INCOMPLETE_RELEASE_ROSTER")
+
+
+def test_missing_gate_schema_member_is_refused(release_root: Path) -> None:
+    (release_root / "schemas/gates_v1.schema.json").unlink()
+    _expect_code(release_root, "MISSING_FILE")
+
+
+@pytest.mark.parametrize(
+    ("raw", "code"),
+    [
+        (b'{"broken":\n', "INVALID_JSON"),
+        (b'{ "$id": "schemas/gates_v1.schema.json" }\n', "NONCANONICAL_JSON"),
+    ],
+)
+def test_gate_schema_member_bytes_must_be_valid_and_canonical(
+    release_root: Path, raw: bytes, code: str
+) -> None:
+    (release_root / "schemas/gates_v1.schema.json").write_bytes(raw)
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, code)
+
+
+def test_gate_schema_hash_and_size_are_manifest_bound(release_root: Path) -> None:
+    manifest = _manifest(release_root)
+    row = next(
+        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
+    )
+    row["sha256"] = "0" * 64
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "MANIFEST_MEMBER_HASH_MISMATCH")
+
+    write_synthetic_release_manifest(release_root)
+    manifest = _manifest(release_root)
+    row = next(
+        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
+    )
+    row["size"] += 1
+    _write_manifest(release_root, manifest)
+    _expect_code(release_root, "MANIFEST_MEMBER_SIZE_MISMATCH")
+
+
 @pytest.mark.parametrize("unsafe", ["/absolute.json", "../escape.json", "a\\b.json", "a/./b.json", "a//b.json"])
 def test_manifest_member_paths_remain_canonical(release_root: Path, unsafe: str) -> None:
     manifest = _manifest(release_root)
@@ -337,6 +422,50 @@
     write_canonical(gates_path, gates)
     write_synthetic_release_manifest(release_root)
     _expect_code(release_root, "GATE_CENTER_COUNTS_MISMATCH")
+
+
+def test_manifest_bound_gate_schema_is_executed(release_root: Path) -> None:
+    schema_path = release_root / "schemas/gates_v1.schema.json"
+    write_canonical(
+        schema_path,
+        {
+            "$id": "schemas/gates_v1.schema.json",
+            "$schema": "https://json-schema.org/draft/2020-12/schema",
+            "not": {},
+        },
+    )
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, "SCHEMA_VALIDATION_FAILED")
+
+
+def test_gate_schema_remote_reference_and_source_change_fail_closed(
+    release_root: Path, monkeypatch
+) -> None:
+    schema_path = release_root / "schemas/gates_v1.schema.json"
+    schema = json.loads(schema_path.read_bytes())
+    schema["$ref"] = "https://example.invalid/gates.json"
+    write_canonical(schema_path, schema)
+    write_synthetic_release_manifest(release_root)
+    _expect_code(release_root, "NONLOCAL_SCHEMA_REFERENCE")
+
+    source_schema = Path(__file__).resolve().parents[2] / "schemas/gates_v1.schema.json"
+    schema_path.write_bytes(source_schema.read_bytes())
+    write_synthetic_release_manifest(release_root)
+    original = registry_loader._read_captured_file
+    reads = 0
+
+    def change_gate_schema_on_verify(root, relative_path):
+        nonlocal reads
+        result = original(root, relative_path)
+        if relative_path == "schemas/gates_v1.schema.json":
+            reads += 1
+            if reads == 2:
+                (root / relative_path).write_bytes(b"{}\n")
+        return result
+
+    monkeypatch.setattr(registry_loader, "_read_captured_file", change_gate_schema_on_verify)
+    _expect_code(release_root, "SOURCE_CHANGED")
+    assert reads == 2
 
 
 def test_mechanics_defaults_and_source_bindings_remain_closed(release_root: Path) -> None:
@@ -491,8 +620,8 @@
     captures = []
     original = registry_loader._MechanicsCapture.verify_unchanged
 
-    def retain_capture(capture):
-        original(capture)
+    def retain_capture(capture, **kwargs):
+        original(capture, **kwargs)
         captures.append(capture)
 
     monkeypatch.setattr(registry_loader._MechanicsCapture, "verify_unchanged", retain_capture)
```

RESCOPE_PENDING. No F02 approval, implementation completion or merge readiness is claimed.
