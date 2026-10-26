# T-PF29 — exact redlines from PF29 v1.0.2

Run: `gtwpe-20261026-pf10-v13-8-8/T-PF29`. Preparation revision: `P1`.
Originating preparer: TW-DRAIN-10 in the Nathan-started T-PF29 document session, Claude Code cloud session https://claude.ai/code/session_016STkEGvGYVWWaqSxnj76eo.
Target: `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.2.md` (`PF29-Canon-HDE-Users-Guide` v1.0.2) at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, byte-identical at the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a`; Git blob `6a0d4725a710bfe1289282729156e15cc8acfcce`; 72,066 bytes; 1,072 lines; ends with one LF; raw UTF-8 SHA-256 `36c3b1bdce884f902dce56650065bdbd26aa3dcb1da8954f62f2c38f83fd5601`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, unchanged on `main`), task `T-PF29`, rows A10 with X06; S-APR with X05; A08 with X04.
Sources: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223; addenda 2.8 (890–1002) and 2.10 (1102–1204). HDE-CRD-0002 Specification v1.1 (`docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3`): approval block, phase blocks and "Canon, QA & Build Notes posture" (147–193), overlaid by delta 01 (`docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091b`) C-8 to C-12. Supporting cross-references: X04 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` §18, 753–792, blob `1d6a92a483e2`); X05 (`docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` §17, 701–739, blob `6baead456619`); X06 (`docs/ephemeral/HDE-CRD-0002-WU-PR-05-pr-implementation-result-v1.0.md` §10, 156–165, blob `20b170490447`).
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Preparation outcome: `READY` after whole-batch producer validation. Save completeness is recorded in the separate proof log.

These are fifteen independent original-bound `REPLACE` operations. Header control fields are reserved for TW-APPLY-10; no operation touches §0.1. Payloads are literal: the single LF immediately before a closing fence is presentation only and is not part of the payload. Every other payload newline is exact, and no payload carries a trailing space. Each OLD block consists of complete original lines, without the last line's own LF, and occurs exactly once in the whole original. Fences are four backticks, longer than any backtick run in a payload. The original line numbers are context only, not locators. RL-009 to RL-012 replace four consecutive original lines; their spans do not intersect, and the LF between each pair stays untouched.

## RL-001

Redline number: RL-001
Findings or source items: A08, A10 and S-APR together (every content redline below); PF03 §4 step 5
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **1\. Feature availability map**` > `## **1.1 Implemented local and QA surfaces**`
Original-bound location: the paragraph that opens §1.1 and names the inspected repository snapshot
Original lines (context only): 81
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: Every changed availability statement in this package was verified by bounded read-only inspection of `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`, while the paragraph attributes all availability to `e7265a09`, where those statements were false. PF03 §4 step 5 requires each repository-dependent claim to name the snapshot it was checked against; PF29 §0.2 requires availability to be checked against current repository reality. The replacement keeps the original snapshot for every unchanged statement, names the second snapshot and the exact statements it covers, and keeps the recipe-execution nonclaim unchanged.

OLD

````text
Availability below is based on bounded read-only inspection of repository snapshot `e7265a090ad0cc8de5f36de2f19481216aa3d073`. Commands are examples to run from the repository root with their stated prerequisites; no recipe was executed for this revision.
````

NEW

````text
Availability below is based on bounded read-only inspection of repository snapshot `e7265a090ad0cc8de5f36de2f19481216aa3d073`, except for the statements updated for delivered HDE-CRD-0002 behavior, which were inspected at repository snapshot `0838ba08254eaefc888019df49a06aa2ae99cc6c`: the retired-route production posture in this section, the start-helper bind in §4.1, the Reader environment gate in §6.1, Aux preview band selection in §10.1, the `bg:resolve --source vendor` environment classification and production override in §11.2, §13.3, §15 Recipe F, §16, §17 and §18, and the unknown-path, CLI help and dev-route gate limits in §16. Commands are examples to run from the repository root with their stated prerequisites; no recipe was executed for this revision.
````

## RL-002

Redline number: RL-002
Findings or source items: A10 (PF10 v13.8.8 addendum 2.10: S19-F03 and the review's production-posture probes; Required canon drainage) with X06 (WU-PR-05 result v1.0 §10 'Stale canon passages': HDE Users Guide §1.1)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **1\. Feature availability map**` > `## **1.1 Implemented local and QA surfaces**`
Original-bound location: the closing paragraph of the **Checked-in retired/noncanonical route drift (unsupported)** block
Original lines (context only): 113
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.10 records S19-F03 delivered on `main` `822ce15`: in a production posture each canon-retired `/ops` route answers `ERR_NOT_FOUND` 404, the same answer as an unknown path, before any handler runs, while the dev runner keeps the full mount; it names HDE Users Guide §1.1 as a stale canon passage. X06 §10 repeats that, and the WU-PR-05 plan §19 (supporting reading) states the needed change: add that a production-like application answers them as unknown paths. Confirmed read-only at `0838ba08` in `adapter/http_reader.py` (`_PRODUCTION_RETIRED`, `_production_posture`, `_mount_for_production`) and `adapter/env_guard.py` (`_compute_env_mode`). The posture is fixed when the application registers the blueprint. The sentence states the retired paths only and makes no claim about router-level OPTIONS or redirect answers on the dev-harness paths (held item H-03, LR5-O1). The existing sentence is kept unchanged.

OLD

````text
These rows report checked-in repository drift only; they do not define route bytes, promise removal, create a deprecation window, or imply compatibility support.
````

NEW

````text
These rows report checked-in repository drift only; they do not define route bytes, promise removal, create a deprecation window, or imply compatibility support. An application created while APP\_ENV resolves to prod, production, or live, or while APP\_ENV is empty and ENGINE\_ENV resolves to one of those values, answers all three paths as unknown paths for every method, with the governed `ERR_NOT_FOUND` 404, before any handler runs. In every other posture, including the dev runner in §4.1, their checked-in handlers still run. This records checked-in behavior only; it does not prove a deployed answer.
````

## RL-003

Redline number: RL-003
Findings or source items: A08 (PF10 v13.8.8 addendum 2.8: AD-3 'the canonical runner binds loopback with the debugger and reloader off'; S10 last clause 'the start helper propagates APP_ENV'; independent check 'Gate and runner') with X04 (WU-PR-03 plan v2.0 §18: HDE Users Guide §4.1)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **4\. Local/dev QA Reader harness**` > `## **4.1 Start the local Reader/dev harness \[Implemented\] \[Dev or QA only\]**`
Original-bound location: the bind paragraph after the `python \-m adapter.http\_reader` line
Original lines (context only): 245
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: X04 §18 lists this exact sentence ('binds the process through `python -m adapter.http_reader` to host `0.0.0.0` on `PORT`') as stale, owner the Product Owner as a canon doc-delta; 2.8 records AD-3 delivered and checked on merged `main`. Confirmed read-only at `0838ba08`: `adapter/http_reader.py` `__main__` runs `create_app().run(host="127.0.0.1", port=int(os.environ.get("PORT", "8000")), debug=False, use_debugger=False, use_reloader=False)`; `scripts/dev_start_reader.sh` exports `APP_ENV` only when it is set, defaults `PORT` to 8000 and prints `(host=127.0.0.1)`. The exception clause existed only to reconcile the old 0.0.0.0 bind with the client address; with a loopback-only bind it no longer applies and is removed.

OLD

````text
The helper binds the process through python \-m adapter.http\_reader to host 0.0.0.0 on PORT, with default PORT=8000. Use [http://127.0.0.1:8000](http://127.0.0.1:8000) as the documented local client access address unless an operator context requires a proven exception.
````

NEW

````text
The helper starts python \-m adapter.http\_reader, which binds host 127.0.0.1 (loopback only) on PORT, with default PORT=8000, and runs with the debugger and reloader off. The helper passes APP\_ENV through unchanged and sets no default; GET /reader then requires APP\_ENV=dev exactly (§6.1). Use [http://127.0.0.1:8000](http://127.0.0.1:8000) as the local client access address.
````

## RL-004

Redline number: RL-004
Findings or source items: A08 (PF10 v13.8.8 addendum 2.8: S10 / (2): GET/HEAD /reader served only for APP_ENV exactly dev, and 403 ERR_READER_FORBIDDEN for every other value, unset and empty included; CR-8; NC-1)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **6\. Reader v1 local workflow**` > `## **6.1 Reader route \[Implemented\] \[Dev or QA only\]**`
Original-bound location: the **Current repository discrepancy \[Current gap\]** paragraph after the bands-only paragraph
Original lines (context only): 341
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.8 records S10 delivered with an exact comparison (CR-8, AD-2): unset, empty, padded, differently cased, test, local and every other value refuse with 403 `ERR_READER_FORBIDDEN`. Confirmed read-only at `0838ba08`: `_reader_dev_env_explicit()` returns `os.environ.get("APP_ENV") == "dev"` and `reader_v1` refuses with `ERR_READER_FORBIDDEN` when it is false. The gap the paragraph records no longer exists, so its \[Current gap\] label goes; the claim boundary ('records checked-in behavior only and does not prove runtime exposure') is kept.

OLD

````text
**Current repository discrepancy \[Current gap\]:** `adapter/http_reader.py` treats a missing APP\_ENV as dev at the Reader guard. This does not weaken the explicit APP\_ENV=dev requirement above; it records checked-in behavior only and does not prove runtime exposure.
````

NEW

````text
The Reader guard compares APP\_ENV exactly, with no trimming or case-folding: an unset or empty value, test, local, a padded or differently cased dev, and every other value refuse with ERR\_READER\_FORBIDDEN. This records checked-in behavior only and does not prove runtime exposure.
````

## RL-005

Redline number: RL-005
Findings or source items: S-APR (Specification v1.1, Phase blocks, Fermentation row: S08 'holds on main'; as overlaid by D01 C-9) with X05 (WU-PR-04 plan v1.0 §17: HDE Users Guide §10.1, stale after S08)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **10\. Aux narrative preview workflow**` > `## **10.1 CLI Aux preview from compat output \[Implemented\]**`
Original-bound location: the pair-file mode paragraph
Original lines (context only): 637
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: X05 §17 lists 'The band comes from that row; --band does not override it' as stale after S08; S08's acceptance intent is that the band flag takes effect for pair-file input, and S-APR's Fermentation block places S08 in this change. Confirmed read-only at `0838ba08` in `engine/cli/main.py` `aux_preview._resolve_from_pair_file`: the category is taken from `--category` or the first row and must be present in the file (`MISSING_COMPAT_CATEGORY` otherwise); then `if args.band: band = args.band` ('S08: an explicit --band replaces only the band read from the file'). Every other sentence is kept.

OLD

````text
Pair-file mode reads the complete compat result's categories, or conjunction.compat for a conjunction result. Optional \--category selects an existing category; without it, the first category row is used, which is harmony in the governed result order. The band comes from that row; \--band does not override it. viewer\_prefs does not select the category. This preview does not rescore the intrinsic result.
````

NEW

````text
Pair-file mode reads the complete compat result's categories, or conjunction.compat for a conjunction result. Optional \--category selects an existing category; without it, the first category row is used, which is harmony in the governed result order. The band comes from that row unless \--band is supplied; an explicit \--band replaces only that band, and the selected category must still be present in the file. viewer\_prefs does not select the category. This preview does not rescore the intrinsic result.
````

## RL-006

Redline number: RL-006
Findings or source items: S-APR (Specification v1.1, Canon, QA & Build Notes posture: S14 status drainage; Phase blocks, Fermentation row: S14) with X05 (WU-PR-04 plan v1.0 §17, Recipe F row: 'the open-rails dry-run command supplies no APP_ENV; after S14 an unset value refuses PROVIDER_CONFIG_INVALID, and a production-like one needs the flag')
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **11\. BodyGraph resolve and vendor ingest workflow**` > `## **11.2 Open-rails configured-v2 vendor dry-run \[Implemented\] \[Operator-authorized only\]**`
Original-bound location: the run-precondition line and the dry-run command that follows it
Original lines (context only): 700–702
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: X05 names Recipe F; this command is byte-identical to Recipe F's and §18's, so the same S14 consequence applies here (PF29 §0.2 currency rule). Confirmed read-only at `0838ba08`: `engine/bodygraph/resolver.py` `_resolve_vendor` applies the SAFE and network rails, then `classify_vendor_environment`, which raises `PROVIDER_CONFIG_INVALID` when neither APP_ENV nor ENGINE_ENV names one recognized value or when they disagree, and refuses a production-like value without the flag with `PROVIDER_PROD_OVERRIDE_REQUIRED`; `bg:resolve` is its only CLI caller. HDE CLI/API/Vendor Ref §7.1.11b to §7.1.11d (supporting reading) own the values and order, so the new paragraph routes to that document by title. APP_ENV=dev matches §11.4 and Recipe G, and the existing sentence that APP_ENV=dev constrains only the local process is repeated so the two recipes agree.

OLD

````text
Run only after confirming authorization and required environment keys are present without printing their values:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

NEW

````text
Run only after confirming authorization and required environment keys are present without printing their values, with APP\_ENV naming a recognized non-production environment:

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json

Under open rails, bg:resolve \--source vendor classifies the environment from APP\_ENV, or from ENGINE\_ENV when APP\_ENV is blank, before any vendor request. An unset or unrecognized value, or an APP\_ENV and ENGINE\_ENV that disagree, refuses with PROVIDER\_CONFIG\_INVALID. A production-like value (prod, production, or live) refuses with PROVIDER\_PROD\_OVERRIDE\_REQUIRED unless the production override in §13.3 is used. APP\_ENV=dev constrains only the local HD Engine process; it does not classify the external vendor target. PF05-Canon-HDE-CLI-API-Vendor-Ref owns the recognized values and the evaluation order.
````

## RL-007

Redline number: RL-007
Findings or source items: S-APR (Specification v1.1: S14 'Implement the production vendor override as CLI/API/Vendor Ref §7.1.11a to §7.1.11f state it'; S14 status drainage) with X05 (WU-PR-04 plan v1.0 §17: 'a production-like one needs the flag')
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **13\. Production posture**` > `## **13.3 Production/open-rails vendor BodyGraph acquisition \[Operator-authorized only\]**`
Original-bound location: the production dry-run command between the persistence paragraph and the legacy-fallback sentence
Original lines (context only): 840
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: This section's command is the production-like vendor read. After S14 it refuses without the override, so the section must state the override to stay current (PF29 §0.2). Confirmed read-only at `0838ba08`: `engine/cli/main.py` defines `--allow-prod-vendor` (metavar `AUTHORIZATION_REF`) on `bg:resolve` only; `_resolve_vendor` refuses a production-like run without it (`PROVIDER_PROD_OVERRIDE_REQUIRED`), refuses an unavailable actor or audit sink (`PROVIDER_AUDIT_UNAVAILABLE`), and `_resolve_vendor_route` refuses `--upsert` or a non-dry-run under the override (`PROVIDER_WRITE_UNSUPPORTED`). The initiator rule, the reference's nature and 'a production dry run that contacts the vendor still requires the flag' are stated as HDE CLI/API/Vendor Ref §7.1.11a, §7.1.11d and §7.1.11e state them (supporting reading); that document is named by title as the owner. The two neighbouring paragraphs and the legacy-fallback sentence are unchanged.

OLD

````text
LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

NEW

````text
When APP\_ENV, or ENGINE\_ENV when APP\_ENV is blank, names prod, production, or live, bg:resolve \--source vendor reaches the vendor only with the production override \--allow-prod-vendor \<AUTHORIZATION\_REF\>, even for a dry-run. The reference identifies the approved Product Owner work item or recorded delegation; it is not a credential and must never contain a secret. Only an authenticated human initiator, as PF05-Canon-HDE-CLI-API-Vendor-Ref defines it, may supply the flag; an AI agent, CI job or unauthenticated shell cannot authorize itself by supplying it. Without the flag the command refuses with PROVIDER\_PROD\_OVERRIDE\_REQUIRED; with it, an unavailable actor identity or audit sink refuses with PROVIDER\_AUDIT\_UNAVAILABLE. Neither refusal makes a vendor request. The override permits one bounded vendor read; it never opens a closed rail, and \--upsert or any production write still refuses with PROVIDER\_WRITE\_UNSUPPORTED.

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=prod SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user approved-user-or-test-id \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \--allow-prod-vendor \<AUTHORIZATION\_REF\> \> vendor\_bodygraph\_dry\_run.json

Set APP\_ENV to the value that names the environment the process actually runs in; the flag never changes that classification.
````

## RL-008

Redline number: RL-008
Findings or source items: S-APR (Specification v1.1: S14 status drainage; Phase blocks, Fermentation row: S14) with X05 (WU-PR-04 plan v1.0 §17: HDE Users Guide Recipe F)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **15\. Minimum runnable recipes**` > `## **Recipe F — open-rails configured-v2 vendor dry-run**`
Original-bound location: the recipe's whole body: precondition paragraph, expected-behavior paragraph and command
Original lines (context only): 937–941
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: X05 §17 names Recipe F: the command supplies no APP_ENV, so after S14 it refuses `PROVIDER_CONFIG_INVALID` when APP_ENV is unset. Confirmed read-only at `0838ba08` as for RL-006. The command gains `APP_ENV=dev`, matching Recipe G; the precondition paragraph points to §11.2 for the classification instead of repeating it; the expected-behavior paragraph is unchanged.

OLD

````text
Before running, confirm the operator environment has HD\_API\_BASE\_URL, HD\_API\_KEY, and, for geocode-required routes, GEO\_API\_KEY. Do not print their values.

With a configured v2 base, current expected dry-run behavior is charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0.

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

NEW

````text
Before running, confirm the operator environment has HD\_API\_BASE\_URL, HD\_API\_KEY, and, for geocode-required routes, GEO\_API\_KEY. Do not print their values. Set APP\_ENV to a recognized non-production value, as the command below does; §11.2 states the environment classification and its refusals.

With a configured v2 base, current expected dry-run behavior is charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0.

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

## RL-009

Redline number: RL-009
Findings or source items: A08 (PF10 v13.8.8 addendum 2.8: S02 / (1) 'unknown paths on the production and http_reader factories answer the governed envelope for GET, HEAD, POST and OPTIONS')
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **16\. Known limitations and nonclaims**`
Original-bound location: the unknown-path bullet in the **Additional Gate/Reader limits** list
Original lines (context only): 977
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.8 records S02 delivered and checked on merged `main`. Confirmed read-only at `0838ba08`: `adapter/factory.py`, `adapter/http_reader.py` `create_app` and `adapter/wsgi.py` each register an `errorhandler(404)` that returns the `ERR_NOT_FOUND` error envelope through `emit_public` as `application/json`. The bullet's limitation no longer holds; the replacement keeps the ownership routing and the checked-in versus deployed boundary.

OLD

````text
* Unknown non-compat paths may still return Flask HTML 404 responses in the affected factories. Do not claim that every unknown path has the Reader JSON error envelope; the HTTP transport owner retains this limitation.
````

NEW

````text
* In the checked-in application factories, `adapter.factory`, `adapter.http_reader.create_app` and `adapter.wsgi`, an unknown path answers 404 with the governed `ERR_NOT_FOUND` JSON envelope, not framework HTML. PF05-Canon-HDE-CLI-API-Vendor-Ref owns those bytes; a checked-in handler does not prove a deployed answer.
````

## RL-010

Redline number: RL-010
Findings or source items: A08 (PF10 v13.8.8 addendum 2.8: S07 / (3) 'hdctl --help names magic10_compat_result.v1; check_cli_help.sh and CLI conformance --check exit 0')
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **16\. Known limitations and nonclaims**`
Original-bound location: the `--dump-reader` and CLI help bullet in the **Additional Gate/Reader limits** list
Original lines (context only): 978
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.8 records S07 delivered. Confirmed read-only at `0838ba08`: the `showcompat` subparser help in `engine/cli/main.py` reads 'Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader'. Only the help sentence changes; the `--dump-reader` v1-only statement, the `scripts/hd_cli.py` stub sentence (it still emits `open_leader` at `0838ba08`) and the historical test-baseline sentence are kept byte for byte.

OLD

````text
* `--dump-reader` remains v1-only. The CLI help still describes ordinary `showcompat` stdout as Reader v1 although its actual handler emits the full internal/admin compat result. `scripts/hd_cli.py` is a separate legacy stub that emits `open_leader`; do not use it as proof of the supported Reader contract. The historical `test_cli_proof.py` failure and the recorded unselected test baseline remain out-of-lane, not fresh results of this revision.
````

NEW

````text
* `--dump-reader` remains v1-only. The CLI help describes ordinary `showcompat` stdout as the canonical `magic10_compat_result.v1` document, matching its handler, and names `--dump-reader` as the only source of Reader v1 bytes. `scripts/hd_cli.py` is a separate legacy stub that emits `open_leader`; do not use it as proof of the supported Reader contract. The historical `test_cli_proof.py` failure and the recorded unselected test baseline remain out-of-lane, not fresh results of this revision.
````

## RL-011

Redline number: RL-011
Findings or source items: S-APR (Specification v1.1, Canon, QA & Build Notes posture: 'the --allow-prod-vendor bullet of HDE Users Guide §16 become[s] stale once S14 lands; their owners update them') with X05 (WU-PR-04 plan v1.0 §17: HDE Users Guide §16)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **16\. Known limitations and nonclaims**`
Original-bound location: the `--allow-prod-vendor` bullet in the **Additional Gate/Reader limits** list
Original lines (context only): 979
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: S-APR names this bullet as stale once S14 lands; X05 repeats it. S14 holds on `main`: `engine/cli/main.py` defines `--allow-prod-vendor` on `bg:resolve` and refuses it elsewhere as a usage error; `engine/bodygraph/resolver.py` implements the classification, flag matrix, actor and audit steps. The replacement states availability and its bounds and routes the contract to HDE CLI/API/Vendor Ref by title; it claims no live or deployed override run.

OLD

````text
* `--allow-prod-vendor` is absent from the inspected active CLI parser. Do not prescribe it as a runnable flag or infer production override support. Its requirement remains with the CLI and PF05 owners through change control.
````

NEW

````text
* `--allow-prod-vendor <AUTHORIZATION_REF>` is implemented, for `hdctl bg:resolve --source vendor` only. A production-like environment requires it for any vendor access and a recognized non-production environment refuses it; only an authenticated human initiator supplies it. It permits one bounded vendor read and authorizes no `--upsert`, production write, public Reader or Aux vendor traffic, or opening of a closed rail (§11.2, §13.3). PF05-Canon-HDE-CLI-API-Vendor-Ref owns the flag, environment classification, evaluation order and audit contract. The checked-in implementation does not prove a live or deployed override run.
````

## RL-012

Redline number: RL-012
Findings or source items: A08 (PF10 v13.8.8 addendum 2.8: S10 / (2) exact dev Reader gate); A10 (PF10 v13.8.8 addendum 2.10: S19-F02 exact HTTP gate; gate-matrix probe 'only exactly dev, test and local pass the gate')
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **16\. Known limitations and nonclaims**`
Original-bound location: the dev GET `/reader` APP_ENV bullet in the **Additional Gate/Reader limits** list
Original lines (context only): 980
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.8 records the exact `/reader` gate; 2.10 records S19-F02 and its gate matrix for the dev/admin routes. Confirmed read-only at `0838ba08`: `_reader_dev_env_explicit()` compares to `dev` exactly and `_dev_admin_gate()` tests `os.environ.get("APP_ENV") in {"dev", "test", "local"}`. The discrepancy the bullet records is gone, so its waiver sentence goes with it.

OLD

````text
* Dev GET `/reader` still defaults a missing APP_ENV to dev; conjunction dev routes require explicit dev/test/local values. The discrepancy does not waive the explicit environment requirement in this guide.
````

NEW

````text
* Dev GET `/reader` requires APP_ENV exactly `dev`, and the dev sampler and conjunction dev routes require exactly `dev`, `test` or `local`. Neither gate trims or case-folds the value, and an unset value refuses.
````

## RL-013

Redline number: RL-013
Findings or source items: S-APR (Specification v1.1: S14 'including environment classification, rails, evaluation order, error carrier, authorized initiator and audit') with X05 (WU-PR-04 plan v1.0 §17, Recipe F row: 'an unset value refuses PROVIDER_CONFIG_INVALID, and a production-like one needs the flag')
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **17\. Troubleshooting**`
Original-bound location: the `PROVIDER\_CONFIG\_INVALID` row of the troubleshooting table
Original lines (context only): 999
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: After S14 an operator following this guide's earlier vendor commands meets `PROVIDER_CONFIG_INVALID` for an unset APP_ENV, and a production-like run meets the three override refusals; the table, PF29's troubleshooting home, gave no cause or action for them. Codes, causes and the zero-I/O posture were confirmed read-only at `0838ba08` in `engine/bodygraph/resolver.py`. The existing row's cause and action are kept and extended; one row for the three override codes follows it. Neither row restates HDE CLI/API/Vendor Ref's contract.

OLD

````text
| PROVIDER\_CONFIG\_INVALID | Vendor configuration is ambiguous or violates contract. | Check for conflicting HD\_API\_BASE\_URL and HDAPI\_BASE\_URL or unpinned vendor policy. |
````

NEW

````text
| PROVIDER\_CONFIG\_INVALID | Vendor configuration is ambiguous or violates contract. For bg:resolve \--source vendor, this includes an unset or unrecognized APP\_ENV and ENGINE\_ENV, or the two disagreeing. | Check for conflicting HD\_API\_BASE\_URL and HDAPI\_BASE\_URL or unpinned vendor policy. For bg:resolve \--source vendor, set APP\_ENV to the recognized value that names the actual environment (§11.2). |
| PROVIDER\_PROD\_OVERRIDE\_REQUIRED, PROVIDER\_PROD\_OVERRIDE\_INVALID, or PROVIDER\_AUDIT\_UNAVAILABLE | bg:resolve \--source vendor ran in a production-like environment without \--allow-prod-vendor, supplied the flag in a recognized non-production environment, or could not resolve the authenticated actor or write the pre-I/O audit event. | Do not change the environment value to avoid the refusal. Only an authenticated human initiator supplies the flag (§13.3); for non-production work, use §11.2 without it. |
````

## RL-014

Redline number: RL-014
Findings or source items: S-APR (Specification v1.1: S14) with X05 (WU-PR-04 plan v1.0 §17, Recipe F row)
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **18\. Quick command reference**`
Original-bound location: the open-rails configured-v2 dry-run lead-in and its command
Original lines (context only): 1047–1049
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: The quick reference repeats the Recipe F command byte for byte; it receives the same `APP_ENV=dev` correction as RL-006 and RL-008 so the reference and the recipes agree. The expected-behavior wording is kept.

OLD

````text
Run open-rails configured-v2 vendor dry-run. With a configured v2 base, expect charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0:

LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

NEW

````text
Run open-rails configured-v2 vendor dry-run with APP\_ENV naming a recognized non-production environment (§11.2). With a configured v2 base, expect charts route selection, deterministic ChartResult adapter mapping, adapter-mapped no-raw-vendor-payload posture, and rows\_written=0:

LC\_ALL=C LANG=C TZ=UTC APP\_ENV=dev SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl bg:resolve \--user qa-user \--source vendor \--birthdate YYYY-MM-DD \--birthtime HH:MM \--location "Place" \--dry-run \> vendor\_bodygraph\_dry\_run.json
````

## RL-015

Redline number: RL-015
Findings or source items: S-APR (Specification v1.1: S14 status drainage of the §16 bullet), consequent on RL-011
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF29-Canon-HDE-Users-Guide`
Section path: `# **18\. Quick command reference**`
Original-bound location: the closing paragraph of §18
Original lines (context only): 1072
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 'unsupported flag' points at the §16 bullet that RL-011 replaces; after RL-011 that bullet states the production override's bounds, so the pointer names it as such. The rest of the paragraph is unchanged.

OLD

````text
Reader v1/v2 POST and read-only tooling examples are in §6.4, §7.6 and §7.7. Current-row examples require established dataset access; no row is created by a UUID example. The wheel, unsupported flag, legacy CLI and deferred live proof limitations in §16 apply to this reference.
````

NEW

````text
Reader v1/v2 POST and read-only tooling examples are in §6.4, §7.6 and §7.7. Current-row examples require established dataset access; no row is created by a UUID example. The wheel, production override, legacy CLI and deferred live proof limitations in §16 apply to this reference.
````

END OF REDLINES
