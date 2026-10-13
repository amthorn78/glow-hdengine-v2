---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.14.md
artifact_version: "1.14"
artifact_state: PR-35 FINAL RECORD, superseding v1.13 as the final record. The PR-35 result is MERGE_PENDING, returned only when v1.9 §2's three predicates hold on the head that adds this file. R-16 and R-21 are settled (§3). A file cannot record the CI run or review of the commit that adds it; the PR-35 return message reports them
phase: PR-35 (review correction and merge readiness), final record
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.13.md (v1.13; preserved unchanged). Everything in v1.9 to v1.13 stands except what §1 to §5 below add or replace
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1)
PR_RETURN_PHASE: none (no rescope is open)
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1 (unchanged)
pf10_ref: as v1.9
proceed: the original Product Owner Proceed recorded in PR_IMPLEMENTATION_RESULT v1.0. No other Proceed exists or is requested
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (NEW_DEDICATED). The worker process restarted three times during this round. Each time the branch, the thread replies, the probe scripts and the logs survived, and nothing was redone from memory. One restart lost the question to the Product Owner before it was shown; it was asked again
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, base main e3a5ed4)
entry_head_for_this_push: fb95d258ec783a69ce1004cd8bcff4545556f52c (the v1.13 record commit)
final_code_commit: 65ee506fd3da966435b62e21ef1b113886b04c00 (unchanged from v1.13; this round changes no code)
record_commit: the commit that adds this file; its own identity is not written into itself
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.14 (PR-35 final record)

## 1. Result

**PR-35 result: `MERGE_PENDING` (Ready to merge), subject to v1.9 §2's predicates on this record's head.** R-16 and R-21 are settled by the Product Owner's decisions PO-D6 and PO-D7 (§3), and no review thread is left open. The PR-35 return message reports the evidence. Only Nathan merges. This record establishes no QA verdict, acceptance, PF09 movement or closure.

## 2. Fourteenth review round: R-21

**Verification of v1.13's push.**
- The push was `6cf498b..fb95d25` at 06:58:31Z. `git ls-remote` gave `fb95d258ec783a69ce1004cd8bcff4545556f52c`, and `main` was unchanged at `e3a5ed4`.
- R-19's thread `PRRT_kwDOP103ks6rvHyN` was answered (r4255632581) and resolved. R-20's thread `PRRT_kwDOP103ks6rvHyW` was answered (r4255633297) and resolved.
- CI on `fb95d25`, run 38359809090, completed **`success`** at 07:17:35Z.
- The PR description was updated to the state of v1.13. A read-back of the live body matched the source byte for byte (10,943 bytes).

**Codex code review of `fb95d25`.** Review 5499922358 at 07:04:04Z raised one P2 finding:

| # | Source and thread | Head reviewed | Finding | Class | Disposition |
| :- | :- | :- | :- | :- | :- |
| R-21 | Codex 5499922358, `PRRT_kwDOP103ks6rvtTl` (r4255673450), `tools/evidence/hdapi_v2_boundary_analyzer.py` lines 2503 to 2507 | `fb95d25` | "Reject implicit exception exits from presenter helpers": a helper that runs `if SAFE_MODE: {}["missing"]` before its presenter-backed return is accepted. Flask turns the `KeyError` into a non-presenter 500 response. The parent reports the route | the limit v1.13 records as OBS-16 (k), not specific to the helper shape (L-123). No complete fix keeps the production Reader | answered (r4255793356) and referred to the Product Owner. **Recorded as a limit, with no code change, by PO-D7** (§3) |

**L-123, R-21 probe (`probe_round18.py`), base / `fb95d25`.**

| Shape | Helper route | Direct-view analogue |
| :- | :- | :- |
| `if SAFE_MODE: {}["missing"]` (R-21) | reported / accepted | not reported / not reported |
| `assert not SAFE_MODE` | reported / accepted | not reported / not reported |
| `if SAFE_MODE: 1 / 0` | reported / accepted | not reported / not reported |
| a call to a module function that raises `KeyError` | reported / accepted | not reported / not reported |
| control, no exception | reported / accepted | — |

Production loci are `['adapter/http_reader.py:reader_post']` on the base and `[]` at `fb95d25`.

The base reports the helper route because it cannot follow the presenter through the parameter. It reports the control helper too, which raises nothing. On the base, the direct-view analogues are not reported. The resulting response is Werkzeug 3.1.9's `InternalServerError` page, which is static HTML with no Reader data.

**Why no complete fix keeps the production Reader.** Its helper `_production_reader_response` indexes values (`meta["engine_tag"]`, `bands[0][1]`) and calls imported code (`identity_meta()`, `emit_fn(...)`), and any of these can raise. Rejecting only definite forms (literal subscripts, `assert`, division by a literal zero) would close the four forms above and leave every other implicit exception open.

## 3. Product Owner decisions

Both questions were put to the Product Owner together, with what each check does, what passes today, the options and their costs, and a recommendation. He answered at about 09:30Z.

| ID | Decision | Options he was given | Basis |
| :- | :- | :- | :- |
| PO-D6 | **R-16: record as a limit, with no code change.** A blueprint registration outside `adapter/` whose method name is joined from constant strings, as in `getattr(app, "register_" + "blueprint")(bp)`, is not flagged by the architecture guard. The text-based guard on `main` misses it as well | record as a limit (recommended); join constant string pieces before checking | Product Owner. Failing closed on every dynamic `getattr` was set out as unworkable, because it flags 11 current files outside `adapter/` |
| PO-D7 | **R-21: record as a limit, with no code change.** OBS-16 (k) covers it: an ordinary exception raised by the helper or by code it calls becomes Flask's static 500 page, as it does for every direct view on `main` | record as a limit (recommended); reject the definite forms; send it through the rescope lane as a new finding to the Implementation Agent (PF10 addendum 2.2, Binding requirements) | Product Owner |

R-16's thread `PRRT_kwDOP103ks6rtqz7` and R-21's thread `PRRT_kwDOP103ks6rvtTl` are answered with these decisions and resolved after this record is pushed. A later finding of either kind is answered and recorded under PO-D6 or PO-D7, not fixed in #627, as PO-D4 does for the cross-module kind.

## 4. Hosted CI (additions)

| Head | Run | Conclusion |
| :- | :- | :- |
| `fb95d25` | 38359809090 | **success** at 07:17:35Z. The code tree tested was `58a334c` (commit `65ee506`), the final code tree |
| this record's head | started by this push | reported in the PR-35 return |

This record changes only `docs/ephemeral/`, so the final code tree stays `58a334c`, and v1.13 §3's local validation (L-112 to L-122) applies to it unchanged.

## 5. Review summary and owners

Over fourteen Codex reviews, the PR received twenty Codex findings (R-1 to R-21; R-6 is PR-35's own).
- Seventeen are corrected.
- R-14 (PO-D4), R-16 (PO-D6) and R-21 (PO-D7) are recorded as limits by Product Owner decision.

The owners of those limits are as follows:
- R-21 and OBS-16 (a) to (k), the analyzer items: the whole-change IA.
- R-16, a guard gap that `main` shares: the whole-change IA.

The TypeSafe reading for the PR-40 handoff stays the one in v1.9 §7, for the reasons in v1.10 §5. With R-21 the review ran fourteen rounds, and the PR has 118 changed paths.

## 6. Canon relied on (additions)

No new source:
- PF10-HDE-Build-Notes v13.5.3 (on `main`), addendum 2.2, Binding requirements (the rescope-lane option for R-21, and the classification of R-16 and R-21);
- PF19-Canon-Glow-QA-Guide v3.0.6 §13.14 (fail closed);
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.2.3 (the Reader's `error_v1` envelope). It governs the errors the Reader emits and is silent on unhandled exceptions, so it does not decide R-21.

Canon is silent on whether an unhandled exception's 500 page counts as a presenter bypass for the analyzer. That is why R-21 went to the Product Owner.

## 7. Recovery

As v1.9 §9. There is no unpushed code. If this record's push is lost, re-push it, then reply on R-16's and R-21's threads with PO-D6 and PO-D7 and resolve both.
