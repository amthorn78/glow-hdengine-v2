# Proof log — PF02-from-v2.4.6.md (application report)

## 1. Artifact and outcome

- Artifact: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/PF02-from-v2.4.6.md`, the complete revised PF02-Canon-HDE-Architecture, version `v2.4.7`.
- Output bytes: 142,444 bytes; LF only; no BOM; no final LF, as in the original; 1,624 LF characters (1,625 lines, the last unterminated); SHA-256 `fc0001e215e5a42bcf91f1e043f0f88a94867e00edae2ab387535869b855a149`.
- This proof log: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/PF02-from-v2.4.6.proof-log.md`, beside it.
- Outcome: applied. Eight operations were applied: five content `REPLACE` redlines and three document-control fields. Every check in §7 passed.
- The revised PF is not an authoritative publication. Canon stays `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md` until Nathan transfers a document there.
- Applier: TW-APPLY-10 — Apply Validated Redlines — 100926.1, page https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b. It was fetched live at the start of the session and again when this step began; both times it showed version 100926.1 and page state as of 2026-10-09T11:05:22.207Z. It ran in Claude Code session https://claude.ai/code/session_01M9PsXYe8yx3bTeqJUj1sTL on 2026-10-26, under Nathan's T-PF02 handoff, which authorizes preparation and then Apply in this one session.

## 2. Inputs

| Input | Identity |
| :- | :- |
| Original | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md` on `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`. Blob `b0bf3d66965d0de91044b519a29bc30b1cc2d040`, unchanged since the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a`. 140,533 bytes; SHA-256 `4bfa53ad9775f6b69432b28ae11048b6458461249186c9bb9161e51e5ecb28db`; 1,617 LF characters, 1,618 lines; title `PF02-Canon-HDE-Architecture`; version `v2.4.6` |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/redlines-PF02-from-v2.4.6.md` at commit `78a1a54b616f82f9662feff3f386139d36b488f9`; blob `ba65cc8a74e07d8b9e0d6e44bd8a4765c01c82f6`; 16,358 bytes; SHA-256 `783e9f23824e6cc9388fe47e70ee58ecac43296c3fee5dc12d6790fd06f5d5ea`. Unchanged since it was first committed at `3fa8745` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf02/redlines-PF02-from-v2.4.6.proof-log.md` at `78a1a54`; blob `6f447ef10dc8dd980e327269f427fddf0a75008e`. Two preparer corrections were made before this step validated the package. `6241cb7` corrected the destination record. `78a1a54` corrected the baseline line count. Neither changes a redline, count or validation result |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, HDE Build Notes v13.8.8; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`. Selected units: front matter 1–223; 2.6 at 531–687 (context); 2.7 at 688–889; 2.8 at 890–1002; 2.10 at 1102–1204 |
| Supporting cross-references | X04, plan v2.0 §18, lines 753–792 (blob `1d6a92a483e2`); X06, result v1.0 §10, lines 156–165 (blob `20b170490447`) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF02, rows A06 (context), A07, A08 with X04, A10 with X06 |
| Editorial standard | `PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a`, read in full |

## 3. Intake and preparation-state verification

- Originating preparer: TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, in this same session. Run `gtwpe-20261026-pf10-v13-8-8/T-PF02/TW-DRAIN-10/r1`.
- Preparation outcome `READY` and save completeness `COMPLETE_PACKAGE` are stated in the package's proof log, §1 and §12. Both package files were read complete from commit `78a1a54`.
- Coverage the package records: the complete target (lines 1–1618) and each selected unit in full. The selection agrees with the handoff and the ledger row T-PF02.
- Unresolved items: H-03 (LR5-O1) is held and is not drafted in any redline. The four observations in the package proof log §9 are reported, not drafted, and do not block. No blocking change or dependency remains.
- Closure: HDE-CRD-0002 is closed (CL-C-10 v1.2, CLOSE, CHANGE_CLOSED by Isis, 2026-10-26T16:40:00Z). No change is held on closure grounds.
- Baseline drift: when this step began, `origin/main` was `0838ba0`. PF02 is blob `b0bf3d66965d` and PF10 is blob `680b0accb0bd`, both equal to the preparer's identities. No newer PF02 or PF10 exists in `docs/pfcanon/`.

## 4. Applied operations and their basis

| ID | Original span (bytes; lines) | Change | Basis, as the preparer recorded it | Source rows |
| :- | :- | :- | :- | :- |
| RL-01 | 70330–70645; 896–897 | §3.3: the "Current repository discrepancy" paragraph (no environment-specific unmount) becomes "Current repository behavior (production posture)", followed by a "Static inspection cannot establish" limit | HDE Build Notes 2.10 records S19-F03, delivered by #656, and routes §3.3 as stale. WU-PR-05 plan v1.0 §19 names the stale statement. On `main` `0838ba0`, `bp.record(_mount_for_production)` installs, in a production-like posture only, a hook that refuses the dev `GET /reader` endpoint and the four dev/admin endpoints before their handlers run. The rules are unchanged | A10 with X06 |
| RL-02 | 71544–71580; 914 | §3.4: label `Future concepts [Speculative]` becomes `Liveness and readiness probes [Required-Now]`, routed to HDE-Mechanics Guide | HDE Build Notes 2.7 names §3.4's speculative label against HDE Mechanics Guide §32.3, which requires both probes. 2.8 and plan v2.0 §18 (X04, line 763) carry the same item | A07; A08 with X04 |
| RL-03 | 73970–74464; 955–956 | §3.5: the retired routes' discrepancy keeps the `RETIRED/NONCANONICAL` classification and the nonclaims, and adds that their code stays and that a production-like application answers them as unknown paths | HDE Build Notes 2.10 routes §3.5 as stale; plan §19 names the statement. On `main`, `_refuse_in_production` answers the retired endpoints, and unrouted methods on their paths, with the not-found answer. The Endpoint Catalog has no record for them | A10 with X06 |
| RL-04 | 83165–83695; 1089 | §3.8.1 bullet: "exposes the same Reader and internal/dev sampler routes" becomes "registers the same", plus the production-like refusal of the dev-only routes | HDE Build Notes 2.10 routes §3.8.1 as stale; plan §19 names the statement. On `main`, `adapter.http_reader.create_app` and `adapter.factory.create_app` register the same three blueprints | A10 with X06 |
| RL-05 | 84449–84977; 1093–1094 | §3.8.1: the `dev/reader_harness/app.py` discrepancy becomes current behavior (no tracked `dev/reader_harness/` path; the start helper's exact `APP_ENV` propagation; the module runner's blueprint set), and the root helpers stay a stated discrepancy | HDE Build Notes 2.10 routes §3.8.1 as stale and carries the root helpers as X-02, which is undecided. 2.7 and 2.8 record the S09 harness retirement; 2.6 records the start helper's propagation. HDE Mechanics Guide §34 names the canonical runner. On `main`, `run_flask.py` and `run_flask_dev.sh` start `adapter.factory:create_app` with the reloader on and the debugger on by default | A10 with X06; A07, A08; A06 context |
| META-VERSION | 65–84; 4 | `**Version:** v2.4.6` becomes `**Version:** v2.4.7` | TW-APPLY-10 header contract: the final numeric component of the native `v` plus three-integer version is incremented once | none |
| META-DATE | 106–136; 7 | `**Effective date:** 2026-10-09` becomes `**Effective date:** 2026-10-26` | The actual application execution date, 2026-10-26 (UTC), in the native `YYYY-MM-DD` form | none |
| META-GATE | 138–257; 9 | `**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` becomes `**Last Update Gate:** BN 13.8.8` | The package records one change source, `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, PF10 version 13.8.8. The gate becomes `BN 13.8.8`. X04 and X06 are supporting reading, not sources | none |

No package operation addresses the header, so no duplicate authorization arose. Fields not changed: `**Title:**`, `**Status:** Canon` (not stale under PF02's rules), and `**Invocation tag:** INV-f2ac55d77ce9aacc`. The document restates neither its version nor its date anywhere else. PF02 has no change log or revision-history entry format, so no history entry is required, and none is supplied. Version, date and gate agree with one another and with the package.

## 5. Constraints and interpretations

- The operations were applied original-bound, in descending offset order, with no rematching against changed text. Content was handled as raw UTF-8 bytes; no line-ending conversion, whitespace trimming or normalization was performed.
- The package's literal convention was used as stated: the bytes between a literal's opening and closing four-backtick `text` fences, with no LF after the last line. Trailing double spaces are part of the literals.
- The revised PF contains no report or administrative content. The NEW text states repository facts at `0838ba08254eaefc888019df49a06aa2ae99cc6c`, as the preparer verified them. This step did not re-decide them, improve their wording or change any redline.

## 6. Whole-batch validation before any output byte was written

- Each of the eight operations matched exactly once in the unchanged original, with expected 1 and observed 1. Each is `REPLACE` or a single-occurrence header field. No `FIND AND REPLACE` or `FIND_AND_REPLACE` appears, so RL-045 does not arise.
- Original-bound plan in offset order: META-VERSION, META-DATE, META-GATE, RL-01, RL-02, RL-03, RL-04, RL-05. No spans intersect or touch; the smallest gap is 2 bytes, between META-DATE and META-GATE. No NEW literal is used as a locator.
- The baseline's SHA-256 and byte count matched the preparer's record before validation began.

## 7. Verification of the output

- Reconstructed expected byte stream: the original with each planned span replaced by its NEW literal, in order. It is byte-identical to the output.
- Every untouched interval of the original (nine intervals) is byte-identical at its mapped offset in the output. Each NEW literal occurs once at its mapped offset, and no OLD content literal remains.
- An independent `git diff --no-index -U0` of the original against the output shows only these hunks: `-4 +4`, `-7 +7`, `-9 +9`, `-896,2 +896,5`, `-914 +917,2`, `-956 +960`, `-1089 +1093`, `-1092,0 +1097,3`, `-1094 +1101`. That is 16 insertions and 9 deletions. Git shows the unchanged label lines of RL-03 and RL-05 as context, which agrees with their literals.
- Header after application: `v2.4.7`, `2026-10-26`, `BN 13.8.8`. `v2.4.6` and `2026-10-09` no longer occur anywhere in the output.
- EOF and encoding: no final LF, as in the original; no CR; no BOM.
- Markers: no `TODO`, `TBD`, `FIXME` or "draft" occurs. The placeholder rules at their original places (original lines 181, 1160 and 1218; output lines 181, 1167 and 1225) are canon text that requires that exact language. No ASCII three-period ellipsis or U+2026 occurs.
- Line arithmetic: 1,617 LF characters in, 1,624 out, which equals the net LF change of the eight operations.
- These are text checks only. They are not product QA, and they establish no runtime behavior.

## 8. Limitations and unresolved items

- Not drafted, and reported in the package proof log §9: the route-name split between HDE Mechanics Guide §32.3 and HDE Build Checklist — Coagulation (`/healthz`, `/readyz`) and PF02, the Endpoint Catalog and the code (`/internal/healthz`, `/internal/readyz`); whether probes defined only in `adapter/wsgi.py` meet HDE Mechanics Guide §32.1A and §32.3; §3.5's retained nonclaim on catalog mutation; and the three commit-pinned behavior paragraphs that keep their `cc754cfb` pins.
- Held: H-03 (LR5-O1), with the Product Owner. X-02 and the other S19 routed findings stay with the Product Owner (HDE Build Notes 2.10; 2.35 item 9).
- Repository claims rest on code read at `0838ba0`. The app was not started and no test was run. The S19 lineage review's Flask test-client probes on `822ce15`, recorded in HDE Build Notes 2.10, cover the same bytes for every inspected file.
- This step establishes no QA verdict, acceptance, canon adoption, PF09 or PF30 movement, deployment or closure.

## 9. Next manual action

Nathan reviews the shared draft PR #761 (https://github.com/amthorn78/glow-hdengine-v2/pull/761) and merges it when ready. Whether and when `PF02-from-v2.4.6.md` (v2.4.7) is transferred into `docs/pfcanon/` is his decision and his manual action.

## 10. Save and completion

Recorded only after both outputs were read back; see the receipt below.

Receipt (2026-10-26, this session):
- `PF02-from-v2.4.6.md`: read back complete. It is byte-identical to the verified application output: 142,444 bytes, SHA-256 `fc0001e215e5a42bcf91f1e043f0f88a94867e00edae2ab387535869b855a149`.
- This proof log: read back complete before this receipt was added (sections 1 to 10 present, LF only, no ellipsis). It does not carry its own hash.
- Save completeness: complete. Both required outputs are saved and verified; no diagnostic was written.
