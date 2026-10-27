---
artifact_type: ADR_DECISION_BRIEF
artifact_id: HDE-S19-ROUTED-FINDINGS-CANON-POLICY-ADR-BRIEF
artifact_version: "1.0"
subject: Canon policy decisions needed before the HDE-CRD-0002 S19 routed security findings S19-R01, S19-R02, S19-R03, S19-R05 and S19-R07 can be fixed
source_register: Candidate CRD Items List, item 9 (https://app.notion.com/p/3e54590a05eb813c8d89d065026f694d), state Open, review status New
source_record: docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md, §4 "Confirmed, routed" (reviewed head 1e97ba9b)
requested_by: Nathan / Product Owner, 2026-10-27 ("create a brief for the canon policy decisions you mentioned that I can submit for ADR approval to Isis. She will need to draft her decision as a PF10 build notes addendum")
addressed_to: Isis, Lead Developer
decision_owner: Product Owner. Isis drafts the decision; it takes effect when the Product Owner publishes the addendum into HDE Build Notes (§2)
author: Master Scrum (https://claude.ai/code/session_014G3ZYHihBTaXjPP5yrEC1N)
repository_head_read: origin/main 44dba78 (code unchanged outside docs/ since 0adce9d9, the CL-40 scan's head)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.9.md, read in full (10,569 bytes): "No current addenda"
created_at: 2026-10-27T02:05:00Z
---

# S19 routed findings — canon policy decisions (ADR brief)

## 1. Decisions requested

HDE-CRD-0002's code security review confirmed seven findings it did not fix, because a fix would set policy that canon does not state, or would contradict canon (S19 review §4). Five of them need a canon decision before any implementing change can fix them:

| # | Finding | Question for Isis | Canon state on `main` |
| :- | :- | :- | :- |
| D-1 | S19-R01 | Must `hdctl showcompat --source vendor` and conjunction vendor acquisition meet a production gate? | Silent. The production override covers only `bg:resolve` (HDE-CLI-API-Vendor-Ref §7.1.11, §7.1.11a) |
| D-2 | S19-R02 | Does a non-`v1`/`v2` configured base fail closed, or keep the legacy BodyGraph fallback? | **In conflict.** HDE-CLI-API-Vendor-Ref §7.1.10 fails closed; HDE Mechanics Guide §1.1 and HDE Users Guide §11.3 keep the fallback |
| D-3 | S19-R03 | How is `POST /api/compat/v1` gated and authenticated outside production? | **In conflict and incomplete.** HDE Governance §4.1.4 requires `APP_ENV` exactly `dev`, `test` or `local` for dev/admin surfaces; HDE-CLI-API-Vendor-Ref §5.5 excludes only production-like values and names no authentication mechanism |
| D-4 | S19-R05 | Who owns an evidence tool's output root, and what may the tool write or delete there? | Partial. HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3 cover the attestation builder's entry checks only; silent on the sanity pipeline's `--log-path` |
| D-5 | S19-R07 | May governed gate check rows carry exception text and absolute local paths? | Silent for gate rows. The keys-only diagnostics rule (HDE Governance §6.3.2) is scoped to direct database diagnostics |

Each decision is independent. Isis may decide all five in one addendum, or some now and some later.

## 2. Authority and output

- **Ownership.** ADRs are the Product Owner's. Agents may draft; the Product Owner is the final maintainer (HDE Governance §9.7.3). The Product Owner has asked Isis to draft the decision. It becomes canon when the Product Owner publishes it into HDE Build Notes (HDE Build Notes, "Precedence, versioning, and scope" item 1). This is the same route the AQ-1 ADR decision took, as addendum 2.15.
- **Why an ADR.** Fixing these findings changes canonical rules and contracts. A CRD that does so must have an approved ADR, which identifies the affected canon and its drainage consequences (Change Process Guide §1.0.5, §0.1A). The implementing change is Candidate CRD Items List item 9; this decision is its prerequisite, not a substitute for it.
- **Requested output.** One HDE Build Notes addendum record under `docs/ephemeral/`, landed by pull request. It must follow the addendum form (Change Process Guide §0.1A, the paragraph on agent-authored HDE Build Notes addenda):
  - self-contained;
  - one H2 with the number and a descriptive title, and only H3 or lower inside it;
  - declarative language;
  - no role-addressed publication, routing or record-maintenance instructions.
- **For each decision decided, the addendum states:**
  - the decision, in normative terms;
  - the canon it supersedes or adds to, by title and section;
  - the drainage targets;
  - consequences for tests, governed evidence and frozen captures;
  - what stays undecided.
- **Numbering.** HDE Build Notes v13.8.9 carries no addenda ("No current addenda"). The number and its publication are the Product Owner's.
- **Not requested.** No ADR file under `docs/adr/`, no canon edit, no code, test or evidence change, no CRD creation. A separate ADR file is Isis's call, and writing outside `docs/ephemeral/` needs the Product Owner's instruction.

## 3. The decisions

### D-1 — Production gate for showcompat and conjunction vendor acquisition (S19-R01)

**Finding (Low).** `hdctl showcompat --source vendor`, and conjunction mode with any source other than `db` or `auto`, acquire from the vendor through `resolve_compat_chart` (`engine/bodygraph/resolver.py` line 1083, `_acquire_dry_run` line 915). Only the generic rails apply: there is no production override, audit event or production gate. Production rails are open by default (Glow Infrastructure §2.4: `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=prod`), so any production shell reaches it.

**Canon now.**
- HDE Governance §3.1, "Admin ops windows (vendor override)": "Ops may run vendor calls in prod. Vendor override is driven by CLI flags."
- HDE-CLI-API-Vendor-Ref §7.1.11a: `--allow-prod-vendor` is "accepted only by `hdctl bg:resolve --source vendor`".
- HDE-CLI-API-Vendor-Ref §7.1.11, implementation state, records the gap: "Vendor acquisition through the compat chart resolver, which `hdctl showcompat --source vendor` and its conjunction mode use, applies the generic rails but not this gate. The HDE-CRD-0002 close report defers that gap to the Product Owner as pending and non-gating."

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | Extend the §7.1.11 gate to these two paths: classification, rail and flag matrix, evaluation order, error carrier and pre-I/O audit event | Amends §7.1.11a's "accepted only by" scope. Reuses the delivered S14 machinery. Production showcompat vendor runs become audited and Product Owner-authorized |
| B | Refuse vendor acquisition for these paths in any production-like environment; production uses `db` only | No new flag. Removes an operator capability in production. Needs a new typed refusal and a Users Guide change |
| C | Accept the current posture (generic rails only) as a recorded risk | No code change. §7.1.11's informative gap note becomes a decided limit |

**Master Scrum's suggestion (not binding): A.** It follows HDE Governance §3.1, which already routes production vendor calls through CLI flags.

**Drainage targets.** HDE-CLI-API-Vendor-Ref §7.1.11 and §7.1.11a; HDE Users Guide §13.3 and §16; HDE Governance §3.1 if its wording changes.

### D-2 — Vendor route selection for non-v1/v2 bases (S19-R02)

**Finding (Low).** `engine/bodygraph/vendor_client.py` reads the version from any path segment, case-insensitively. A `v2` anywhere selects `charts`. Any other base, including unversioned, nonterminal and `v3`, takes legacy `bodygraphs` with the `HD-Api-Key` credential. Userinfo, query and fragment are not refused.

**Canon now (in conflict).**

| Source | Rule |
| :- | :- |
| HDE-CLI-API-Vendor-Ref §7.1.10 | A terminal, case-sensitive `v2` selects `charts`; a terminal `v1` selects `bodygraphs`. "An unversioned base, unsupported version, nonterminal version marker, multiple conflicting version markers, or otherwise ambiguous base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or any external I/O." The base must contain "no userinfo, query, or fragment, and end in exactly `v1` or `v2`". The v1 path "is retained legacy selection, not fallback" |
| HDE Mechanics Guide §1.1 | "Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback". It also says to keep v1 "until the owning architecture and byte-contract homes decide whether v1 remains a fallback or is retired" |
| HDE Users Guide §11.3, §13.3, §16 | "When the configured base is non-v2, explicit legacy BodyGraph fallback is preserved." |
| `AGENTS.md` (EPIC036 and EPIC038 postures) | "non-v2 configured bases preserve explicit legacy BodyGraph fallback" |
| Code and pins | The code follows the fallback posture. It is pinned by `tests/bodygraph/test_bg_resolve_route_policy.py` line 86, `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py` line 237, and the governed EPIC038 evidence predicate `explicit_legacy_fallback` (`tools/evidence/generate_v2_mapped_cache_evidence.py` line 275). The frozen EPIC036 and EPIC037 captures record the same posture |

**A second tension for the decision.** HDE Mechanics Guide §1.1 also says runtime request construction must not "infer runtime behavior from vendor API version path strings". HDE-CLI-API-Vendor-Ref §7.1.10 selects the route from the terminal version segment. The decision should say which governs, or how they fit together.

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | HDE-CLI-API-Vendor-Ref §7.1.10 governs: fail closed on any base that does not end in exactly `v1` or `v2`, and enforce the configured-base boundary | Drain the fallback text out of HDE Mechanics Guide §1.1, HDE Users Guide §11.3, §13.3 and §16, and `AGENTS.md`. The two route-policy tests and the `explicit_legacy_fallback` predicate are replaced through their owners. Frozen captures stay as history. Operators with an unversioned base get `PROVIDER_ROUTE_UNSUPPORTED` |
| B | The fallback posture governs: amend §7.1.10 to keep non-v2 legacy fallback | No code or test change for routing. §7.1.10's fail-closed rule is withdrawn |
| C | Split: enforce the configured-base boundary (absolute HTTPS, host, no userinfo, query or fragment) now, and leave the fallback question open | Closes the credential-projection risk of a malformed base. Leaves the canon conflict open |

**Master Scrum's suggestion (not binding): A.** HDE Mechanics Guide §1.1 defers the v1 question to "the owning architecture and byte-contract homes". HDE-CLI-API-Vendor-Ref, the byte-contract home, has since decided it in §7.1.10.

**Drainage targets.** HDE Mechanics Guide §1.1; HDE Users Guide §11.3, §13.3 and §16; `AGENTS.md` route-policy lines (a Product Owner-instructed edit); HDE-CLI-API-Vendor-Ref §7.1.10 under option B.

### D-3 — Gating and authentication of `POST /api/compat/v1` (S19-R03)

**Finding (Low).** `POST /api/compat/v1` returns the internal numeric result with no authentication (`engine/http/compat_handler.py` lines 130 to 173). Its guard refuses only when `adapter/env_guard.py::_compute_env_mode` returns `prod`. That function treats an unset `APP_ENV` and `ENGINE_ENV` as `dev`, and passes `staging` through unchanged. So the route serves results whenever the environment is unset, staging or any unrecognized value.

**Exposure fact.** Glow Infrastructure §2.2 lists the Staging/QA HD Engine against the **shared production database instance**. A reachable staging deployment would serve compat results for real stored users, unauthenticated.

**Canon now.**
- HDE-CLI-API-Vendor-Ref §5.5 calls the route "dev only" and "internal admin".
  - Its gate fails closed only "in any resolved production-like posture" (`prod`, `production`, `live`).
  - Its success body is "dev/internal; authenticated" and comes "after the production-excluding environment gate and internal authentication". It names no authentication mechanism.
- HDE Governance §4.1.4, "Dev/admin APP_ENV gating (dev/test/local only)": dev/admin-only surfaces "MUST" allow exactly `{"dev","test","local"}`. A missing, empty or other value is a rails violation and fails closed, with no default.
- HDE Governance §8.3.2 defines a pre-Glow admin credential, but only for admin bundle surfaces. The work that implements it, Coagulation Build Checklist HDE-COAG006.5, is Not done.

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | Classify the compat route as a dev/admin surface under HDE Governance §4.1.4: serve only with `APP_ENV` exactly `dev`, `test` or `local`, and fail closed otherwise. Remove "authenticated" from §5.5 | Closes the staging and unset-environment exposure with existing canon. No credential machinery. Staging can no longer use the route |
| B | Require an admin credential on the route, extending HDE Governance §8.3.2 beyond admin bundles; the transport is pinned in HDE-CLI-API-Vendor-Ref | Needs new credential, transport and rotation machinery, which overlaps HDE-COAG006.5 |
| C | A now, with B later through HDE-COAG006.5 | Closes the exposure now; authentication arrives with the planned admin-surface work |

**Master Scrum's suggestion (not binding): C.** Option A rests on a rule canon already states. The credential belongs with the planned admin-surface work.

**Drainage targets.** HDE-CLI-API-Vendor-Ref §5.5; HDE Governance §4.1.4 (naming the compat route) or §8.3 (under B or C); Coagulation Build Checklist HDE-COAG006.5 notes (under C).

### D-4 — Output-root ownership for evidence tools (S19-R05)

**Finding (Low; operator only, since CI uses a fresh `$RUNNER_TEMP` path).**
- `tools/evidence/run_sanity_pipeline.py` resolves `--log-path` through symlinks (line 347), so it can overwrite a governed file.
- `tools/evidence/build_release_attestation.py` accepts any existing empty output root and follows symlinks on later writes. On failure it removes `evidence/` and bundle files it did not create. In the review's probe, this destroyed a concurrent run's bundle.

**Canon now.** HDE Schemas & Artifacts §6.2.1 and HDE Mechanics Guide §27.3: the builder "MUST refuse a symlinked output root, an output inside the source repository, a non-directory destination, a non-empty destination, or overwrite of existing output", and must leave the checkout byte-stable. Canon accepts an existing empty directory. It says nothing about symlinks below the root, about what a failing run may delete, or about the sanity pipeline's log target.

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | Exclusive ownership: the builder creates its output root itself (an existing directory is refused) or holds an exclusive lock; it never follows symlinks below the root; on failure it removes only what it created. `--log-path` refuses symlinks and any tracked path other than its canonical log | Strongest. Changes the documented invocation (callers pass a path that does not yet exist) |
| B | Keep "existing empty directory", and add: no symlink following below the root, and on failure remove only files this run created. `--log-path` refuses symlinks and tracked paths other than its canonical log | Smaller change to the documented interface. A concurrent run in the same empty root is still not excluded |
| C | Accept as an operator-only risk | No change |

**Master Scrum's suggestion (not binding): B.** It removes the destructive behaviour without changing the documented command line.

**Drainage targets.** HDE Schemas & Artifacts §6.2.1; HDE Mechanics Guide §27.3; for the sanity pipeline, the owning section Isis names (canon is silent).

### D-5 — Content of governed gate check rows (S19-R07)

**Finding (Low).** `tools/evidence/run_canonical_json_gate.py` line 1205 records `validation_error:<type>:<exception text>` in the governed check rows, absolute local paths included. Write mode publishes them into `audit/gates/json_gate/canonical/`.

**Canon now.**
- HDE Governance §6.3.2: diagnostics are "keys-only and secret-free" and "MUST NOT retain passwords, DSNs, tokens, endpoint values, request or response bodies, raw SQL, or stack traces". The rule sits under the direct database posture.
- HDE Governance §2.0.10, `LOGS_KEYS_ONLY_OK`, covers "governed logs (including A7 proofs, BodyGraph diagnostics, and ops probes)".
- HDE Governance §2.0.6 requires discovered physical paths to be repository-relative ("no absolute paths").
- None of these says whether a gate check row is a governed log, or whether it may carry exception text.

**Options.**

| Option | Decision | Consequence |
| :- | :- | :- |
| A | Governed gate check rows carry only a typed error class and repository-relative paths, never exception text or absolute paths | Rows become portable and deterministic across machines. Diagnosis of a failing run moves to stderr, which is not governed |
| B | Exception text is allowed, but absolute paths are rewritten repository-relative | Keeps diagnostic detail. Exception text from third-party libraries can still vary between runs |
| C | Accept | No change |

**Master Scrum's suggestion (not binding): A.** It extends the existing keys-only principle to gate evidence.

**Drainage targets.** HDE Governance §2.0.10 (`LOGS_KEYS_ONLY_OK`) or §6.3.2, and HDE Schemas & Artifacts "Canonical JSON and topology" for the check-row shape.

## 4. Not in this brief

| Item | Why not here | Owner |
| :- | :- | :- |
| S19-R04 (owner tools act on `--help` and rewrite tracked files) | The review routes it as an owner-tool invocation contract, plus a frozen EPIC030 family. Isis may add it as a further decision if she judges canon silent here too | Product Owner |
| S19-R06 (relative `scripts/hdctl.py` in a frozen-family generator) | Frozen-family owner decision, not canon policy | Product Owner |
| X-01 to X-04 | Fixes with no policy question (S19 review §8) | Implementing change for item 9 |
| Candidate item 10 | Defects, not policy | Product Owner |

## 5. Facts checked for this brief

- `main` at `44dba78`. No file outside `docs/` has changed since `0adce9d9`, the CL-40 scan's head, so every finding is still in the code.
- Re-read on `main`:
  - `engine/bodygraph/vendor_client.py` (any-segment, case-folded version selection);
  - `engine/http/compat_handler.py` and `adapter/env_guard.py::_compute_env_mode` (unset means `dev`; `staging` passes);
  - `tools/evidence/run_canonical_json_gate.py` line 1205;
  - `tools/evidence/run_sanity_pipeline.py` line 347;
  - `resolve_compat_chart` and `_acquire_dry_run` in `engine/bodygraph/resolver.py`;
  - the route-policy tests and the evidence predicate cited in D-2.
- The HDE-CRD-0002 record in HDE CRD Records (`PF30.1-Canon-HDE-CRD-Records`, deferred or residual work) states that item 9 has "no disposition yet".
- No live, production or vendor behaviour was observed.

## 6. TypeSafe reading for the receiving session (Isis, this decision)

Action sent (v8.2): "In the continuing Lead Developer session, decide five canon policy questions routed from one already-recorded code security review: a production vendor gate for two CLI acquisition paths, vendor route selection where three canon documents conflict, authentication for one internal HTTP route, output-root ownership for two evidence tools, and the diagnostic content of one gate's records. Read about ten canon sections and the cited code, and draft one build-notes addendum recording the decisions, affected canon and drainage targets. A written brief with options exists; no code, test or canon change and no live run against a provider occurs; the Product Owner publishes the addendum, and a separate implementing change follows later."

As printed by the script:
- **TypeSafe v8.2: Opus 5.5 at extra high.**
  - Effort score 2.81 (confidence 0.79). Rung probabilities: low 0.00, medium 0.02, high 0.21, extra high 0.71, max 0.06, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.01, Opus 5.5 0.93, Sonnet 5.5 0.06, Haiku 5.5 0.00 (confidence 0.91).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.002, Fable 5.1 at extra high 0.007, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.019, Opus 5.5 at high 0.195, Opus 5.5 at extra high 0.660, Opus 5.5 at max 0.056, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.013, Sonnet 5.5 at extra high 0.043, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - Flags: none.
- **Detail:** v8.2 sent 2026-10-27T02:03:21Z; HTTP 200 in 0.57 s; 5474 input and 71 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- Request v8.2 and `score_v8.py`, run once with session kind `review`. No Notion row was written. Nathan's pick: not stated.

**Surface advice.**
- **Session.** The continuing Isis session, or a new top-level session for Isis on `amthorn78/glow-hdengine-v2`.
- **Access.** Read `main`, including `docs/pfcanon/` and the cited code. Write one branch and one pull request under `docs/ephemeral/`.
- **Not needed.** Notion writes, production, vendor, Railway or database access.

## Canon relied on

Read on `main` at `44dba78`:
- PF04-Canon-HDE-Governance v2.8.8:
  - §1.1;
  - §2.0.6; §2.0.10, including `LOGS_KEYS_ONLY_OK`;
  - §3.1 "Public traffic (Reader/Aux)" and "Admin ops windows (vendor override)";
  - §4.1.4 "Dev/admin APP_ENV gating (dev/test/local only)";
  - §6.3.2 "Diagnostics and failure handling";
  - §8.3, §8.3.1, §8.3.2;
  - §9.1, "Epic and CRD change lanes";
  - §9.7.3.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.4: §5.5; §7.1.10; §7.1.11 including its implementation-state limits; §7.1.11a to §7.1.11f.
- PF06-Canon-Change-Process-Guide v2.5.5: §0.1A, including the paragraph on agent-authored HDE Build Notes addenda; §1.0.5.
- PF07-Canon-Glow-Infrastructure v2.3.4: §2.2, Production and Staging/QA; §2.4.
- PF10-HDE-Build-Notes v13.8.9, in full.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7: §6.2.1; "Canonical JSON and topology".
- PF14-Canon-HDE-Mechanics-Guide v3.5.9: §1.1; §27.3.
- PF29-Canon-HDE-Users-Guide v1.0.3: §11.3; §13.3; §16.
- PF09.7-Canon-HDE-Build-Checklist-Coagulation v1.1.9: HDE-COAG006.5.
- PF30.1-Canon-HDE-CRD-Records v0.9.2: the HDE-CRD-0002 record, deferred or residual work.

In-flight and source documents:
- `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md` §1 to §5, §8 and §9;
- `docs/ephemeral/HDE-CRD-0002-CL-40-cycle-gap-scan-v1.1.md`;
- the Candidate CRD Items List (Notion), item 9;
- the precedent form of `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.1.md` and `docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-aq1-adr-v1.0.md`;
- `AGENTS.md`.
