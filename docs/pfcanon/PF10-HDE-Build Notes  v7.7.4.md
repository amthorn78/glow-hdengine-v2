# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** 7.7.4  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

**Purpose.** Working scratchpad for new, not-yet-merged documentation. When an entry is merged into canon, delete that entry here in the next cut. This file temporarily supersedes canon for the covered items. Higher numbers supersede. Titles-only cross-refs (no version numbers in body). 

TEMPLATE — Addendum Entry (do not edit/remove)  
ADDENDUM \<number\> — \<short, action-oriented title\>  
Timestamp: \<mmddyy hh:mm\>  
owner: \<role/person\>  
Details: \<specific information to drain to canon, it’s origin, and any evidence available\>

---

1) # Numbered Addenda Begin

---

### **Updated Section – PF10 Build Notes Addendum**

## **Addendum 1 — PF16 Epics Map Failure, Retirement, and Deferral to PF20**

**Timestamp:** 2025-11-21TXX:XXZ  
 **Owner:** PO / Engine Governance

### **Intent**

Record the outcome of **HDE-EPIC011 — Vendor Ingest & Data Durability** as a **failed epic**, retire **PF16 — Canon-HD Engine Epics Map**, and formally **defer all future epic planning** to **PF20 — Canon-HDE-Phased Epics**.

This addendum is descriptive; it does **not** introduce new technical requirements. It captures the historical result of the EPIC011 gate and the document-level retirement of PF16.

### **Normative effect (now)**

1. **EPIC011 outcome — failed gate**

   * EPIC011 is recorded as **failed**:

     * Its acceptance roster (DB posture, ingest idempotence, evidence discipline, partition plan, SAFE rails, BodyGraph invariance) was **not fully satisfied**.

     * The epic did not reach a state where all required tokens (e.g., `PARTITION_PLAN_OK`, `INGEST_IDEMPOTENT_OK`, evidence/mirror gates) were green at the same time for a production-ready release.

   * PF16 and PF19 are updated to:

     * Mark EPIC011 as **failed** in the epics map and QA guide,

     * Treat any residual work items as **recorded debt**, not as open EPIC011 acceptance.

2. **PF16 status — retired / historical only**

   * **PF16 — Canon-HD Engine Epics Map** is **retired** as an active planning document and is maintained **for history only**:

     * The front-matter “Deprecation note” is updated to state that:

       * EPIC011 is **failed**,

       * EPIC012 and all later epics in PF16 are **“won’t do”** (preserved as design history only),

       * PF16 must **not** be used as the source of truth for new work.

   * Any references in other PF docs to PF16 as the active epic roadmap are now **historical**; forward-looking references must point to PF20 by title.

3. **Deferral to PF20 — Canon-HDE-Phased Epics**

   * **PF20 — Canon-HDE-Phased Epics** is established as the **single home** for:

     * All future epic planning and phasing of HDE work,

     * Any future epics that revisit topics originally scoped under PF16 (e.g., a future PK epic, partition refactors, new A7/Catalog work),

     * The canonical mapping between phases, epics, and acceptance rosters.

   * PF10 build notes, PF04 Governance, PF09 Build Checklist, PF19 QA Guide, and other PF docs must:

     * Route any **new** epic-level decisions by title to PF20, not PF16,

     * Treat PF16 as archival context when referencing EPIC011.

4. **Preservation of EPIC011 activity as history**

   * All EPIC011 build notes, evidence, and addenda remain part of PF10 as a **historical record**:

     * Addenda that pinned SAFE rails, evidence discipline, and vendor/DB posture (for example Addenda 8, 9, 10, 17, 24, 28, 30\) remain valid as **“what was attempted and partially implemented”**.

     * PF16 and PF19 incorporate the redlines that:

       * Make EPIC011 non-deferred on partition (`PARTITION_PLAN_OK` only),

       * Mark CLI, vendor ingest, compat math, and Aux as **preservation surfaces**,

       * Tie BodyGraph observability and evidence discipline to the EPIC011 work.

   * PF20 is free to:

     * Re-use or supersede EPIC011 concepts selectively,

     * Define new epics that explicitly absorb remaining debt (e.g., PK epic, refined vendor override epic), with fresh acceptance rosters.

### **Drain to (titles-only)**

* **PF16 — Canon-HD Engine Epics Map**

  * Deprecation note updated to mark EPIC011 \= failed, EPIC012+ \= won’t do.

  * EPIC011 scope updated with non-deferred partition stance and preservation surfaces.

* **PF20 — Canon-HDE-Phased Epics**

  * New single home for epic planning, phase mapping, and future epic acceptance rosters.

* **PF19 — Canon-Glow QA Guide**

  * QA stance updated to:

    * Treat EPIC011 as failed and historical,

    * Handle lifecycle / OPS-managed evidence and preservation surfaces accordingly.

* **PF04 / PF09 / PF12**

  * Continue as single homes for token semantics, build gates, and schemas.

  * May reference EPIC011 as historical context, but epic planning is now routed to PF20.

---

## Addendum 2 \- PR Policy Change

EPIC017 is implemented as a 5‑PR series, one per deliverable (D1–D5). Same‑PR parity rules (code ↔ evidence) still apply to each PR; epic‑level acceptance (PF20 tokens) occurs only after all five PRs merge. PF06’s “one PR per epic” will be revised to allow for up to 10 PRs per epic. This is a PO Referendum and approved.

## ADDENDUM 3 \- HDE-EPIC017 PR01

### Review Summary

This PR implements the PR1 / WS-D1 slice for HDE-EPIC017 by centralizing the canonical JSON serializer, routing Reader v1 and hdctl showcompat through the shared emitter path, and adding AB/BA, two-run, Reader/CLI parity, and preimage-recompute harnesses plus evidence indexing. The changes are consistent with the approved EPIC017 Implementation Plan and with PF05/PF09/PF12/PF14 semantics for canonical JSON, CLI behavior, and evidence discipline. Tests and artifacts convincingly demonstrate canonical output and CLI/Reader parity under closed rails and deterministic env settings.

I do not see any correctness or canon-drift issues that require remediation in this PR.  
---

### Findings

1. **Canonical JSON serializer centralized and aligned with canon**  
   * engine/stable/sercanon.py now exposes dumps\_minified\_sorted and serialize with ensure\_ascii=False, compact separators, configurable sort\_keys, and an explicit “exactly one trailing LF” contract. engine/serializer/canon.sercanon delegates to stable\_sercanon.serialize, keeping PF-level requirements (“canonical JSON from engine/serializer/canon.py, UTF-8 \+ sorted keys \+ one LF”) intact while moving the implementation into a stable helper.  
   * This respects the single-home rule for canonical JSON (PF01/PF12) and AGENTS’ “canonical JSON with one LF per canon serializer” guidance.  
2. **Reader v1 envelope uses the shared presenter/emitter path**  
   * presenter/reader\_v1/emitter.emit\_reader\_v1 now builds the preimage, then uses engine.presenter.emitter.emit\_compact\_json both for preimage bytes (for idempotence\_hash) and the final envelope bytes. The emitter itself uses canon.sercanon, so Reader v1 now shares the exact canonical serializer used for CLI and HTTP compat.  
   * \_dedupe\_and\_sort\_categories still enforces “categories as a set” with id dedupe, band sanity, and stable sorting, and \_build\_preimage still produces the six-key, numeric-free envelope. This matches PF01/PF05/PF14’s Reader v1 covenant (six keys, numeric-free, bands-only) while tightening the “single emitter path” invariant.  
3. hdctl showcompat **semantics brought in line with PF05**  
   * engine/cli/main.showcompat now:  
     * Canonicalizes the pair using compat.ordering.normalize\_pair via a new \_canonical\_pair helper, then computes compat features and compat\_public on the canonical (a,b).  
     * Builds a compat payload { "a": ..., "b": ..., "viewer\_prefs": ..., "compat": { "categories": \[...\], "meta": {engine\_tag, release\_id, invocation\_tag} } } and emits it via emitter.emit\_public, so stdout is compat/admin JSON, not the Reader envelope.  
     * Calls emit\_reader\_public\_envelope for the charts and writes those bytes to the \--dump-reader sidecar via \_dump\_reader\_bytes when requested.  
   * Tests adjust accordingly:  
     * tests/cli/test\_cli\_canonical\_bytes.py now asserts stdout has shape {a,b,compat,viewer\_prefs}, is LF-terminated with no double LFs, and that compat.categories is a list with a meta.release\_id.  
     * tests/cli/test\_showcompat\_sources.py now reads stdout compat JSON for both \--source vendor and \--source db, asserting compat.meta.engine\_tag/release\_id/invocation\_tag rather than Reader-envelope meta fields.  
   * This matches PF05’s revised showcompat contract: stdout is compat/admin JSON, and Reader parity is via \--dump-reader sidecar, not stdout.  
4. **AB↔BA parity, two-run identity, Reader/CLI parity, and preimage recompute are all wired and tested**  
   * Script scripts/cli/canonical\_harness.py and new test tests/cli/test\_showcompat\_parity\_and\_identity.py together prove:  
     * **AB↔BA parity:** artifacts/cli/ab.json and artifacts/cli/ba.json are generated by running scripts/hdctl.py showcompat on (A,B) and (B,A) with the same env and are byte-identical; artifacts/cli/summary.json records both SHA-256 hashes and ab\_ba\_equal: true.  
     * **Two-run identity:** the harness runs showcompat twice for the same input and asserts identical stdout bytes; the hash and equality flag are recorded in summary.json.  
     * **Reader/CLI parity:** the harness calls emit\_reader\_public\_envelope directly, then runs scripts/hdctl.py showcompat \--dump-reader ... on the same pair and writes CLI dump bytes into artifacts/cli/reader\_cli\_parity.bytes, which tests compare to the runtime Reader bytes.  
     * **Preimage recompute:** the harness recomputes the Reader envelope preimage hash using emitter.emit\_public(preimage) and logs computed\_sha256, stored\_sha256, and match=True into artifacts/cli/preimage\_recompute.log.  
   * Tests validate these behaviors and enforce canonical JSON properties:  
     * test\_two\_run\_identity\_and\_reemit ensures two runs of showcompat under pinned env yield identical bytes and that re-emitting the parsed compat payload via the emitter yields the same bytes (two-run \+ re-emit identity).  
     * test\_reader\_dump\_matches\_runtime verifies CLI \--dump-reader output equals emit\_reader\_public\_envelope output for the same pair and that idempotence\_hash matches the recomputed value.  
5. **Serializer guard and emitter symbol proof added with correct scope**  
   * scripts/cli/serializer\_guard.py scans engine, adapter, and presenter for json.dumps calls, whitelisting only engine/serializer/canon.py, engine/stable/sercanon.py, and engine/cli/\_admin\_dump.py, and writes the findings to artifacts/cli/guards/serializer\_grep\_guard.log. This gives us an explicit view of any remaining ad-hoc JSON serialization on governed paths.  
   * scripts/cli/emitter\_symbol\_proof.py documents emit\_public call sites for Reader/CLI by ripgrepping engine/cli/main.py, engine/runtime/public.py, and presenter/reader\_v1/emitter.py, writing the result to artifacts/cli/guards/emitter\_symbol\_proof.txt. The proof correctly shows showcompat using emitter.emit\_public and confirms Reader uses emit\_compact\_json (so no emit\_public match there), which is still consistent with the single-emitter architecture because both go through canon.sercanon and engine/presenter/emitter.  
6. **Evidence index and mirror are updated with full path-proofs**  
   * docs/evidence/INDEX.json now contains entries for:  
     * artifacts/cli/ab.json (cli.showcompat.ab)  
     * artifacts/cli/ba.json (cli.showcompat.ba)  
     * artifacts/cli/summary.json (cli.showcompat.summary)  
     * artifacts/cli/reader\_dump.json (cli.showcompat.reader\_dump)  
     * artifacts/cli/reader\_cli\_parity.bytes (cli.showcompat.reader\_cli\_parity)  
     * artifacts/cli/preimage\_recompute.log (cli.showcompat.preimage\_recompute)  
     * artifacts/cli/guards/serializer\_grep\_guard.log (cli.guards.serializer\_grep\_guard)  
     * artifacts/cli/guards/emitter\_symbol\_proof.txt (cli.guards.emitter\_symbol\_proof)  
       each with .path\_proof.txt anchors created in this PR.  
   * artifacts/evidence\_index.jsonl now includes corresponding mirror records for these artifacts with the PF12 field set (artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes) sorted and LF-terminated. The mirror update matches the Index additions, preserving 1:1 parity and the “single mirror file” rule.  
7. **Tests are run under correct rails and are focused on EPIC017 CLI behavior**  
   * Codex ran pytest for the core CLI tests with environment SAFE\_MODE=1 ALLOW\_NETWORK=0 LC\_ALL=C LANG=C TZ=UTC, as required by our EPIC017 rails and PF19’s QA posture, and all relevant tests pass.  
   * The changes are confined to serializer/emitter, CLI, harness scripts, and CLI tests; no transport routes, Aux behavior, or DB rails are modified in ways that conflict with PF02/PF05/PF07.

---

Because none of these findings indicate a bug, drift, or missing acceptance behavior for D1, **no remediation is needed** for this PR.

### Doc Deltas

Even though doc updates will be fully handled in the later doc-delta PR (WS-D5), this PR already implies the following deltas that should be captured there:

* **PF05 — HDE-CLI-API-Vendor-Ref v1.3.3**  
  * The “QA status note” that hdctl showcompat sometimes emits empty stdout can be revised once EPIC017 is closed and we have full evidence across all slices. After this PR, stdout is clearly non-empty compat JSON via the canonical emitter and we have AB↔BA, two-run, Reader/CLI parity, and preimage evidence for the CLI slice. The doc-delta should mark the showcompat stdout emptiness issue as resolved once all EPIC017 CLI tokens are closed.  
* **PF09 — HDE-Build Checklist**  
  * Phase I “Canonical Serialization Package” row can now cite this PR’s artifacts (cli.showcompat.ab, cli.showcompat.ba, cli.showcompat.summary, cli.showcompat.reader\_dump, cli.showcompat.reader\_cli\_parity, cli.showcompat.preimage\_recompute, cli.guards.\*) as evidence for D1 direction. Status stays “in progress” until D2–D4 are complete but the row should reference these artifact keys and the new tests.  
* **PF20 — HDE-Phased Epics Map**  
  * In EPIC017’s record, the D1 token group (CLI\_NO\_ALT\_JSON\_OK, CLI\_SHOWCOMPAT\_CANON\_OK, CLI\_AB\_BA\_PARITY\_OK, TWO\_RUN\_IDENTITY\_OK, CLI\_READER\_PARITY\_OK, JSON\_CANONICAL\_CHECK\_OK, PREIMAGE\_RECOMPUTE\_OK) can now point to this PR’s evidence keys in the “Tokens & Evidence” section (to be formalized in PR5’s doc-delta work).

## ADDENDUM 4 \- HDE-EPIC017 PR02

### Review Summary

This PR is the EPIC017 PR2 / WS-D2 “Evidence skeleton & topology orientation demo” slice. It hardens the human Evidence Index \+ hash sentinel \+ machine mirror, enforces path-proof discipline for governed artifacts, adds a topology orientation demo artifact and CI gates, and wires tests to prove the skeleton is coherent and drift-free. The changes are consistent with the approved EPIC017 Implementation Plan and align cleanly with PF09/PF12/PF14/PF19/PF20 requirements for evidence structure, schema, and CI posture.

I don’t see any bugs, canon drift, or missing acceptance behaviors for WS-D2; no remediation is required.  
---

### Findings

1. **Evidence Index and hash sentinel are canonical and single-sourced**  
   * tools/evidence/update\_evidence\_index.py now owns the human index and hash sentinel, with HUMAN\_INDEX and HASH\_SENTINEL constants pointing to docs/evidence/INDEX.json and docs/evidence/INDEX.sha256. It normalizes legacy entries (title, path, proof) into {artifact\_key, discovered\_physical\_path} pairs via \_normalize\_index\_entry and \_load\_human\_index. INDEX.json is rendered as a deduped, sorted list of {artifact\_key, discovered\_physical\_path} objects using canonical JSON (sorted keys, compact, single LF), and INDEX.sha256 is computed as SHA-256 over those bytes and written as \<sha\> docs/evidence/INDEX.json.  
   * tests/evidence/test\_evidence\_skeleton.py and tests/ops/test\_evidence\_index.py validate that the on-disk INDEX.json matches the canonical render, and that the sentinel hash line matches the actual hash of INDEX.json, catching drift early.  
2. **Machine mirror and self-record handling match PF12/PF09 semantics**  
   * The mirror path is now explicit (MIRROR\_PATH \= ROOT / "artifacts/evidence\_index.jsonl"), and \_render\_mirror builds records only from normalized index entries, enforcing a fixed field set (artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes), sorted by (artifact\_key, discovered\_physical\_path) and rendered as canonical JSONL with one LF per line.  
   * The mirror’s **self-record** logic handles index.machine\_mirror specially: it uses the body of all other lines to compute a canonical sha256 and iterates to reconcile size\_bytes with the final mirror size, then writes a matching path-proof entry. ci/checks/check\_mirror\_schema.sh was updated to treat the self-record as a special case and verify SELF\_SHA, SELF\_SIZE, and proof consistency, which is exactly the sort of hardened behavior PF12/PF14 call for on the mirror index.  
3. **Path-proof discipline is consistently applied across governed artifacts**  
   * \_write\_path\_proof centralizes path-proof generation, writing path, size\_bytes, sha256, and produced\_at\_utc lines with a trailing blank line, and preserves existing produced\_at\_utc when valid. \_load\_existing\_proof parses existing proof files and supplies metadata when recomputing proofs or mirror values.  
   * The PR re-synced .path\_proof.txt files for a large set of governed artifacts (DB, DB-bridge, bodygraph, vendor, ops, QA, transport snapshots, etc.), and mirror records now refer to those proofs via proof\_anchor. The tests in tests/evidence/test\_evidence\_skeleton.py and tests/ops/test\_evidence\_index.py assert that proof\_anchor paths exist and that proof path, sha256, and size\_bytes match the mirror and the artifact, closing the loop that PF09/PF12 describe for evidence integrity.  
4. **Topology orientation demo is implemented and CI-gated as intended**  
   * tools/evidence/orientation\_demo.py provides \_load\_mirror\_records, \_validate, \_render\_report, and generate\_orientation(check) that:  
     * Load normalized INDEX entries and sorted mirror records.  
     * Check for MISSING\_MIRROR, MISSING\_ARTIFACT, MISSING\_PROOF, SHA\_MISMATCH, and SIZE\_MISMATCH conditions.  
     * Render a deterministic report with header, total\_artifacts, status: ok|mismatch, and either a sample: line or an issues: list.  
     * Write the report to audit/gates/topology/orientation\_demo.txt when check=False, and raise ORIENTATION\_MISMATCH (if there are issues) or ORIENTATION\_DRIFT (if the existing file differs from the freshly rendered report in \--check mode).  
   * The final version explicitly compares existing\_text \!= text and only raises ORIENTATION\_DRIFT when the on-disk orientation demo is stale w.r.t. the current INDEX/mirror state, fixing the earlier false-positive behavior. tests/evidence/test\_orientation\_demo.py asserts that generate\_orientation(check=False) produces the expected header and status: ok, and that \_validate detects synthetic mirror/index mismatches. CI now runs python tools/evidence/orientation\_demo.py \--check under pinned env, so both coherence and freshness for the topology demo are enforced.  
5. **CI wiring enforces evidence skeleton rules and adds pytest availability**  
   * .github/workflows/ci.yml now explicitly installs pytest (python \-m pip install pytest) after the usual dependency install steps, and runs the evidence tests via python \-m pytest tests/evidence tests/ops/test\_evidence\_index.py, which fixes the earlier “pytest: command not found” failure and aligns execution with the configured interpreter.  
   * The CI job also runs python tools/evidence/update\_evidence\_index.py \--check, python tools/evidence/orientation\_demo.py \--check, and ci/checks/check\_mirror\_schema.sh, so any drift in Index, sentinel, mirror, path-proofs, or orientation demo will fail CI. This is exactly what PF09/PF12/PF19 expect from an evidence skeleton.  
6. **Scope and rails are respected; no cross-epic drift introduced**  
   * All changes are confined to evidence tooling (tools/evidence/\*), CI (ci/checks/check\_mirror\_schema.sh, .github/workflows/ci.yml), evidence/index artifacts (docs/evidence/INDEX.\*, artifacts/evidence\_index.jsonl\*, .path\_proof.txt files), and new tests under tests/evidence/ and tests/ops/. There are **no** changes to Reader endpoints, CLI behavior beyond the already-approved EPIC017 PR1, Aux surfaces, or registry\_report semantics.  
   * Env rails (SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC) are pinned in the CI job environment, matching PF07/PF19 rails posture for evidence runs.

Given these findings and that CI is green with the new checks, I judge this PR as **acceptable** with no required remediation.  
---

### Doc Deltas

These should be captured in the later doc-delta / close-out work (WS-D5), but they arise directly from this PR:

* **PF09 — HDE-Build Checklist (Phase I; Evidence skeleton rows)**  
  * Update the Phase I items for “Evidence Index & machine mirror” to reference the now-canonical shape of docs/evidence/INDEX.json (list of {artifact\_key, discovered\_physical\_path} objects) and the stricter self-record handling for artifacts/evidence\_index.jsonl.  
  * Note that the topology orientation demo artifact topology.orientation\_demo under audit/gates/topology/orientation\_demo.txt and its path-proof are now part of the governed evidence skeleton.  
* **PF12 — HDE-Schemas and Artifacts (Index & mirror schema)**  
  * Clarify that the **human index** is now canonicalized to {artifact\_key, discovered\_physical\_path} and that legacy title/path/proof shapes are normalized by tooling (not treated as separate schema).  
  * Confirm the mirror record schema and self-record semantics (body-hash-based sha256, size iteration, and dedicated path-proof) used here as the go-to example for the evidence index.  
* **PF14 — HDE-Mechanics Guide (Evidence & CI coupling)**  
  * Add a reference that tools/evidence/update\_evidence\_index.py and tools/evidence/orientation\_demo.py are the canonical jobs for Evidence Index/mirror and topology orientation, and that CI must run them with \--check under rails-closed env.  
  * Document ci/checks/check\_mirror\_schema.sh’s current behavior as the enforcement mechanism for PF12 mirror schema constraints.  
* **PF20 — HDE Phased Epics Map (EPIC017 record, D2 section)**  
  * Under the EPIC017 D2 “Evidence skeleton & topology orientation demo” entry, point the tokens for EVIDENCE\_INDEX\_UPDATED\_OK, EVIDENCE\_INDEX\_MIRROR\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, CI\_CHECK\_MIRROR\_SCHEMA\_OK, CI\_CHECK\_FINAL\_LF\_OK, and the topology orientation token (if named) to the specific artifacts and tests introduced by this PR (e.g., topology.orientation\_demo, tests/evidence/test\_evidence\_skeleton.py, tests/evidence/test\_orientation\_demo.py, ci/checks/check\_mirror\_schema.sh).  
* **PF10 — HDE-Build Notes (EPIC017 progress addendum)**  
  * Add a brief addendum entry noting that HDE-EPIC017 PR2 hardened the evidence skeleton and introduced audit/gates/topology/orientation\_demo.txt, with Index/mirror/path-proof parity enforced via CI. This addendum should be referenced when we later mark D2 as “Done” in PF09/PF20.

## ADDENDUM 5 \- HDE-EPIC017 PR03

### Review Summary

This PR is the EPIC017 PR3 / WS-D3 “Programmatic configuration loader & canonical registry\_report” slice. It introduces a PF12-aligned registry loader, a canonical registry\_report.v1 generator, and wires the report into the evidence skeleton (Index, mirror, path-proofs), while also refreshing the topology orientation demo after those changes. The behavior matches the approved EPIC017 Implementation Plan and is aligned with PF09/PF12/PF14/PF19/PF20; tests and CI convincingly cover loader failures, alias policy, registry\_report determinism, and evidence wiring.

I don’t see any correctness or canon-drift issues that require remediation in this PR.  
---

### Findings

1. **Registry loader is PF12-style, typed, and fail-closed**  
   * engine/config/registry\_loader.py defines RegistryConfig plus typed error classes (RegistryConfigError, UnknownIdError, DuplicateIdError, AliasPolicyError, SchemaValidationError) and loaders for gates, channels, Magic-10, and manifest:  
     * Gates: gates\_v1.json must have a gates list of objects with gate (int) and center (non-empty string). Duplicate gate IDs raise DuplicateIdError.  
     * Channels: channels\_v1.json must contain a channels array of objects with id, gates, centers, circuit\_primary, primary\_domain, domains, flags. Channel IDs must be NN-NN, normalized via \_normalize\_channel\_id, and must match the sorted gate pair; unknown gates or centers raise UnknownIdError; missing primary\_domain or mismatched domains raise SchemaValidationError.  
     * Magic-10: magic10.json order must match FROZEN\_MAGIC10\_ORDER; magic10\_caps.json must cover the full order and each entry must provide inputs and bounds.min/max; magic10\_seeds.json must be an object with required fields per seed and no extra IDs.  
     * Manifest: manifest.json must contain an entries array of objects with path, sha256, size and no duplicate paths.  
   * The top-level load\_registry\_config orchestrates these, returning a RegistryConfig with maps of gates, channels, alias mappings, Magic-10 order/caps/seeds, manifest entries, centers, and domains. Unknown IDs, duplicate IDs, malformed records, and alias violations all raise the relevant typed errors, which matches the “fail-closed” behavior described in the EPIC plan and PF12/PF14 loader semantics.  
2. **Alias policy is explicit and enforced both OFF and ON**  
   * \_load\_channels supports alias entries that have alias\_for only when allow\_aliases=True and a non-empty alias\_ledger is provided. Otherwise, alias entries or missing ledger entries raise AliasPolicyError.  
   * It ensures no duplicate alias IDs, ledger entries match alias\_for, and alias targets exist in the canonical channel set; unknown alias targets and format issues (non-string IDs, bad gates) produce AliasPolicyError or SchemaValidationError.  
   * tests/config/test\_alias\_policy\_enforcement.py creates a temporary catalog copy, injects an alias entry, and asserts:  
     * With alias policy OFF (default), load\_registry\_config raises AliasPolicyError.  
     * With alias policy ON but empty ledger, AliasPolicyError still raises.  
     * With allow\_aliases=True and alias\_ledger={"09-10": "01-08"}, the loader returns a config whose alias\_map is exactly {"09-10": "01-08"}.  
   * This exactly matches the plan’s requirement: alias policy OFF by default, ON only via allow-list, and fail-closed behavior for illegal or undeclared aliases.  
3. **Canonical registry\_report is PF14-shaped, deterministic, and canonical**  
   * tools/generate\_registry\_report.py introduces:  
     * \_stable\_generated\_at() that uses SOURCE\_DATE\_EPOCH (if set) or reuses the existing generated\_at\_utc from registry\_report.json if present; otherwise it falls back to "1970-01-01T00:00:00Z". This ensures stable timestamps for two-run identity unless the environment explicitly opts into new timestamps.  
     * \_build\_registry\_inputs(config) that collects catalog paths, counts, and hashes for channels, gates, Magic-10 caps/order/seeds, and manifest entries (with path/sha/size/count), matching PF12’s catalog \+ manifest semantics.  
     * \_domain\_counts(config) that computes counts per domain across channels, returning a sorted dict.  
     * \_magic10\_versions(config) that emits order, seeds, and caps with the same field shapes as the loader, keyed by Magic-10 category.  
     * build\_registry\_report returning a PF14-style object:

`{`  
  `"schema": "registry_report.v1",`  
  `"generated_at_utc": "...",`  
  `"inputs": {...},`  
  `"artifacts": {`  
    `"registry": {`  
      `"channel_ids": [...],`  
      `"gate_centers": {...},`  
      `"centers": [...],`  
      `"domains": [...],`  
      `"domain_counts": {...},`  
      `"magic10": {...},`  
      `"alias_policy": {"mode": "off|allow_list", "aliases": {...}}`  
    `}`  
  `},`  
  `"notes": ["registry_report is generated programmatically; generated_at_utc is stable unless SOURCE_DATE_EPOCH is set."]`  
`}`

*   
  * and write\_registry\_report() writes the report via canon.sercanon(..., sort\_keys=True) to artifacts/registry/registry\_report.json.  
  * Tests in tests/config/test\_registry\_report\_determinism.py call the generator twice and assert byte-for-byte equality, schema \== "registry\_report.v1", the presence of trailing LF, and matching SHA-256 hashes. test\_registry\_report\_exists\_and\_is\_canonical checks for a LF-terminated JSON document with the correct schema. This satisfies the EPIC017 D3 requirements for two-run identity and canonical JSON.  
4. **Registry\_report is correctly wired into the evidence skeleton**  
   * docs/evidence/INDEX.json now includes an entry for artifact\_key: "registry.registry\_report" with discovered\_physical\_path: "artifacts/registry/registry\_report.json".  
   * artifacts/evidence\_index.jsonl contains a mirror record for that path with role: "snapshot", matching sha256 and size\_bytes, and a proof\_anchor: "artifacts/registry/registry\_report.json.path\_proof.txt".  
   * artifacts/registry/registry\_report.json.path\_proof.txt records the correct path, size\_bytes, sha256, and produced\_at\_utc for the report. The path-proof for the mirror file also carries both old and new size/hash pairs, and the mirror’s self-record handling (from PR2) knows how to interpret that format for self-validation.  
   * tests/config/test\_registry\_report\_indexing.py end-to-end checks that:  
     * The report exists and its SHA and size match those recorded in INDEX and mirror.  
     * The mirror record’s artifact\_key matches the Index entry.  
     * The proof\_anchor matches the path-proof file, and the path-proof contents match the artifact’s SHA and size.  
   * This fully satisfies the EPIC017 plan’s requirement that registry\_report be a governed artifact in the evidence skeleton.  
5. **Evidence skeleton and orientation demo are consistent after the new report**  
   * PR3 re-ran update\_evidence\_index and orientation demo after adding registry.registry\_report, resulting in:  
     * Updated docs/evidence/INDEX.json with an additional artifact entry and a new sentinel hash in docs/evidence/INDEX.sha256.  
     * Updated artifacts/evidence\_index.jsonl with mirror records for registry.registry\_report and a new self-record for the mirror (index.machine\_mirror) and orientation demo (topology.orientation\_demo), aligned with the self-record semantics.  
     * Updated audit/gates/topology/orientation\_demo.txt from total\_artifacts: 109 to total\_artifacts: 110, with status: ok and the same sample line.  
     * Updated audit/gates/topology/orientation\_demo.txt.path\_proof.txt with the new sha/size and produced\_at\_utc.  
   * tools/evidence/orientation\_demo.py retains the corrected logic from PR2:  
     * generate\_orientation(check=True) now only raises ORIENTATION\_DRIFT if the on-disk orientation report differs from the freshly rendered text while \_validate reports no mismatches; post-remediation, CI shows python tools/evidence/orientation\_demo.py \--check returning successfully, so both coherence and freshness of the skeleton are now proven.  
6. **Tests & CI cover loader behavior, registry\_report, and evidence wiring under rails-closed env**  
   * The PR runs:  
     * python tools/generate\_registry\_report.py  
     * python \-m pytest tests/config  
     * python tools/evidence/update\_evidence\_index.py \--check  
     * python tools/evidence/orientation\_demo.py \--check  
     * python \-m pytest tests/evidence tests/ops/test\_evidence\_index.py  
       all under the rails-closed CI environment with pytest explicitly installed, which is aligned with PF07/PF19’s QA posture and the EPIC017 rails.  
   * Tests for config loader (unknown IDs, duplicates, alias policy) plus tests for registry\_report determinism and indexing give good coverage for D3 tokens (CONFIG\_GEN\_OK, UNKNOWN\_IDS\_FAIL\_CLOSED\_OK, JSON\_CANONICAL\_CHECK\_OK for registry\_report, and the evidence-index tokens for registry\_report).  
7. **Minor observation (future doc clarity, not a blocker)**  
   * The mirror file contains multiple records for certain artifact\_keys (e.g., index.machine\_mirror and topology.orientation\_demo) with different produced\_at\_utc and size/sha values. Tests and CI treat this as acceptable, and PF12/PF09 do not currently forbid multiple time-stamped records for the same (artifact\_key, discovered\_physical\_path) so long as they are internally coherent and self-record handling is correct.  
   * **NEW CANON PROPOSAL (for PF12/PF09, not required here):** clarify in PF12/PF09 whether mirrors are allowed to carry “history” records (multiple rows per artifact over time) or if they must enforce strict uniqueness per (artifact\_key, discovered\_physical\_path). This PR is consistent with current behavior and tests, so no change is needed now.

Given these findings, I consider this PR acceptable as-is; no remediation is necessary.  
---

### Doc Deltas

These deltas should be captured in the later doc-delta/close-out (WS-D5) work, but they follow directly from this PR:

* **PF12 — HDE-Schemas and Artifacts (catalogs, manifest, registry)**  
  * Document engine.config.registry\_loader as the canonical PF12-aligned loader for the PF12 catalogs and manifest, including:  
    * Gate/channel schema (gates\_v1.json, channels\_v1.json) and fail-closed behaviors for unknown/duplicate IDs and alias policy enforcement.  
    * Magic-10 (order, caps, seeds) validation and the requirement that order match FROZEN\_MAGIC10\_ORDER exactly.  
    * Manifest uniqueness constraints and typed error classes (UnknownIdError, DuplicateIdError, AliasPolicyError, SchemaValidationError).  
  * Add registry.registry\_report to the registry/evidence schema section as a governed artifact, with its top-level fields (schema, generated\_at\_utc, inputs, artifacts.registry, notes) and the Magic-10/circuit/alias\_policy substructures.  
* **PF14 — HDE-Mechanics Guide (Programmatic Configuration System and registry\_report)**  
  * Update the Programmatic Configuration System section to reference engine.config.registry\_loader.load\_registry\_config and tools/generate\_registry\_report.py as the canonical loader and registry\_report generator.  
  * Clarify that:  
    * registry\_report is generated programmatically using the canonical serializer, with two-run identity guaranteed via SOURCE\_DATE\_EPOCH or reuse of generated\_at\_utc.  
    * The report’s alias\_policy field reflects the current alias allow-list mode and ledger contents.  
* **PF09 — HDE-Build Checklist (D3 row)**  
  * For the D3 “Programmatic Config System & registry\_report” entry, update the “Evidence” column to reference:  
    * engine.config.registry\_loader (loader),  
    * tools/generate\_registry\_report.py,  
    * artifacts/registry/registry\_report.json,  
    * artifacts/registry/registry\_report.json.path\_proof.txt,  
    * and tests under tests/config/ (unknown IDs, alias policy, determinism, indexing).  
* **PF20 — HDE Phased Epics Map (EPIC017 record, D3 section)**  
  * Under EPIC017 D3, attach acceptance tokens (CONFIG\_GEN\_OK, UNKNOWN\_IDS\_FAIL\_CLOSED\_OK, JSON\_CANONICAL\_CHECK\_OK for registry\_report) to:  
    * The loader tests and registry\_report tests added by this PR.  
    * The evidence artifacts and mirror records described above.  
* **PF10 — HDE-Build Notes (EPIC017 progress)**  
  * Add a short addendum noting that EPIC017 PR3 implemented the PF12-aligned registry loader and PF14-shaped registry\_report.v1, wired it into the evidence skeleton, and refreshed the topology orientation demo after adding registry.registry\_report.

## ADDENDUM 6 \- Escalation Remediation Decisions \- PR4 CI Failures

We made these decisions because PR4’s CI failures were not about the ordering math itself, but about fragile evidence plumbing around it. Ordering artifacts changed while the Evidence Index, mirror, and path-proofs did not, which produced SHA and size mismatches and duplicate or malformed proof records. To stop this from recurring, we centralized responsibility into a small set of tools, made them the only writers for ordering artifacts and evidence files, and required them to fully rewrite the Index, mirror, and proofs from a single source of truth on every run.

The impact is that ordering artifacts, the Evidence Index, the machine mirror, and all related path-proofs now move in lockstep, are deterministic under pinned environment settings, and are actively guarded by CI rather than just validated once. CI runs the generator and evidence tools in a fixed sequence under closed rails, then enforces mirror and proof invariants before tests, so evidence drift is caught immediately. Canon will be updated to describe this hardened behavior, and WS-D4 tokens for ordering determinism and evidence gates can now be set to green with concrete, governed artifacts backing them.

**Doc Deltas**

These deltas arise directly from PR4 and its remediation CRD. They should be drained in the EPIC017 doc‑delta / close‑out work (PR5 / WS‑D5), but PF10 records them here as the ledger of what changed.

* **PF09 — HDE‑Build Checklist (Phase I; Deterministic core & Evidence)**

  * Under the Phase I evidence rows and deterministic core notes, explicitly:

    * Reference the four ordering artifacts (`channels_sorted.snapshot.json`, `categories_iter.snapshot.json`, `props_total_order.log`, `abba_identity.bytes`) as governed, generator‑owned artifacts.

    * Add or clarify acceptance items for:

      * `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK` (only `generate_ordering_artifacts.py` writes ordering artifacts),

      * `ORDERING_ARTIFACTS_DETERMINISTIC_OK` (two‑run identity via `--check`),

      * `CI_CHECK_MIRROR_SCHEMA_OK` (mirror \+ proofs gate).

    * Note that any PR touching governed artifacts under `artifacts/**`, `docs/**`, or `audit/**` MUST run the evidence tools and CI gates listed in Findings §5 before merge.

* **PF12 — HDE‑Schemas & Artifacts (Evidence Index, mirror, and proofs)**

  * Extend the machine mirror section to make explicit:

    * The canonical `mirror_jsonl` record shape:  
       `artifact_key`, `discovered_physical_path`, `produced_at_utc`, `proof_anchor`, `role`, `sha256`, `size_bytes`; unknown keys are rejected.

    * **Self‑record semantics** for `index.machine_mirror`: `sha256` is the hash of the mirror body (excluding the self‑record); `size_bytes` is the full file size including the self‑record; the associated `.path_proof.txt` contains exactly one `sha256` \+ one `size_bytes` pair matching those values.

  * Clarify the canonical `.path_proof.txt` schema (no duplicate sha/size pairs) and its relationship to `proof_anchor`.

  * If not already present in PF12, add a brief note that path‑proof transcripts MAY include `produced_at_utc` and, where adopted by mechanics, an informational `mtime_utc`, but these do not change acceptance semantics for sha/size matching.

* **PF14 — HDE‑Mechanics Guide (Evidence change workflow & single‑writer tools)**

  * Under “Evidence discipline” / “Evidence jobs”:

    * Record that only the evidence tools may write governed evidence artifacts:

      * `tools/order/generate_ordering_artifacts.py` → ordering artifacts under `artifacts/engine/order/*`.

      * `tools/evidence/update_evidence_index.py` → `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and all governed `*.path_proof.txt`.

    * Add (or confirm) the **Evidence change workflow**:

       Any PR that changes governed artifacts must:

      * Run `python tools/order/generate_ordering_artifacts.py` and `--check` when ordering artifacts are in scope.

      * Run `python tools/evidence/update_evidence_index.py` and `--check`.

      * Run `python tools/evidence/orientation_demo.py` and `--check`.

      * Run `ci/checks/check_mirror_schema.sh`.

      * Record an evidence addendum in PF10 for the PR.

    * Reiterate that governed artifacts are tooling‑generated, not hand‑edited; manual edits are limited to canonical doc‑delta work.

* **PF19 — Canon‑Glow QA Guide (CI ordering and rails posture for evidence)**

  * In the QA rails / CI sections, document the **canonical CI sequence** for EPIC017 evidence‑governed PRs (mirroring Findings §5):

    * Generate \+ `--check` ordering artifacts.

    * Update Evidence Index and mirror \+ `--check`.

    * Run orientation demo \+ `--check`.

    * Run `check_mirror_schema.sh`.

    * Run the associated `pytest` suites for ordering and evidence.

  * Specify that CI caches must not allow `check_mirror_schema.sh` to see stale artifacts: cache invalidation must include `artifacts/engine/order/**`, `artifacts/evidence_index.jsonl`, `docs/evidence/INDEX*`, and relevant `audit/**` proofs whenever generator or evidence tooling changes.

* **PF20 — HDE‑Phased Epics (EPIC017 WS‑D4 record)**

  * Under EPIC017’s WS‑D4 “Deterministic tie‑break & total‑order module” entry:

    * Point tokens such as `COMPOSITE_ABBA_IDENTITY_OK`, `TIEBREAK_TOTAL_ORDER_OK` (or equivalent), `ORDERING_ARTIFACTS_SINGLE_SOURCE_OK`, `ORDERING_ARTIFACTS_DETERMINISTIC_OK`, `EVIDENCE_PATH_PROOFS_OK`, and `CI_CHECK_MIRROR_SCHEMA_OK` to:

      * Ordering artifacts under `artifacts/engine/order/*`.

      * Mirror record(s) for those artifacts in `artifacts/evidence_index.jsonl`.

      * Their corresponding path‑proofs.

      * The tests and CI jobs listed in Findings §5 (`tests/order/*`, `tests/mech/test_order_properties.py`, `tests/evidence/*`, `tests/ops/test_evidence_index.py`, and `ci/checks/check_mirror_schema.sh`).

    * Make explicit that D4’s acceptance requires the **remediated** evidence architecture (no duplicate mirror records, no multi‑sha proofs, correct self‑record semantics).

* **PF10 — HDE‑Build Notes**

  * This Addendum 6 is the canonical ledger for PR4’s evidence and ordering remediation. When PF09/PF12/PF14/PF19/PF20 have absorbed the deltas above and EPIC017 is fully closed, a future PF10 cut may prune this addendum as “drained,” but until then it remains the source of truth for how PR4 fixed WS‑D4’s evidence discipline.

## ADDENDUM 7 \- **PRO4**

## 

### Review Summary

This PR4 iteration for **HDE-EPIC017 WS-D4** implements the new ordering layer (comparators \+ ordering artifacts) and substantially hardens the evidence system (single writer for INDEX/mirror/proofs, Machine Mirror self-record, path-proof shape, orientation demo, CI checks), but it **does not yet achieve a fully passing CI state**. The latest run of python \-m pytest tests/evidence tests/ops/test\_evidence\_index.py still fails on mtime\_utc mismatches between path-proofs and filesystem stat() values, and ci/checks/check\_mirror\_schema.sh reports PROOF\_MTIME and ABBA parity issues at various points during the remediation cycle.

On the positive side, the repo now has a dedicated engine/order package, deterministic ordering artifacts under artifacts/engine/order/\*, a single evidence index writer (tools/evidence/update\_evidence\_index.py), and a hardened mirror schema check. On the negative side, the introduction of mtime\_utc as a first-class field in proofs collided with Git/CI behavior (non-reproducible mtimes across clones), and a follow-up fix that tried to decouple mtime\_utc from stat() made the evidence tests fail because they still expect mtime\_utc \== expected\_mtime.

Given your decision to **close PR4** and handle the remaining mtime/ABBA issues in a separate remediation PR, the correct posture is: treat this PR as **partially successful Calcination work** (ordering math and evidence skeleton mostly hardened), but explicitly record that CI failed and that WS-D4 tokens depending on stable mtime\_utc semantics are **not yet green**.  
---

### Findings

1. **Ordering layer and artifacts are in place and deterministic (good)**  
   * A new ordering package engine/order defines comparators and helpers for IDs, channels, categories, and arrays-as-sets (compare\_ids, normalize\_channel\_id, compare\_channels, compare\_categories, canonicalize\_set etc.), with legacy mechanics comparators delegating to these helpers.  
   * tools/order/generate\_ordering\_artifacts.py is the canonical generator for four ordering artifacts:  
     * artifacts/engine/order/channels\_sorted.snapshot.json  
     * artifacts/engine/order/categories\_iter.snapshot.json  
     * artifacts/engine/order/props\_total\_order.log  
     * artifacts/engine/order/abba\_identity.bytes  
       and supports a \--check mode that recomputes and compares bytes.  
   * New tests tests/order/test\_total\_order\_properties.py and tests/order/test\_ordering\_artifacts\_stability.py assert total order properties (antisymmetry, transitivity, totality) and artifact stability / ABBA parity.  
2. **Evidence index, mirror, and proofs moved to a single-writer model (good)**  
   * tools/evidence/update\_evidence\_index.py is now the **sole writer** for:  
     * docs/evidence/INDEX.json  
     * docs/evidence/INDEX.sha256  
     * artifacts/evidence\_index.jsonl  
     * governed \*.path\_proof.txt under artifacts/\*\* and audit/\*\*.  
   * The script:  
     * Normalizes the human index to {artifact\_key, discovered\_physical\_path} and writes canonical JSON \+ sentinel hash.  
     * Renders the mirror with enforced uniqueness of (artifact\_key, discovered\_physical\_path) and sorted order.  
     * Writes path proofs with the hardened shape {path,size\_bytes,sha256,mtime\_utc,produced\_at\_utc} via \_write\_path\_proof.  
   * Mirror self-record (index.machine\_mirror) is computed in a single deterministic pass as a **body hash** of all mirror lines except the self-line plus the final file size; the mirror path-proof and mirror row are kept in sync.  
3. **CI mirror checks and orientation demo were tightened (good)**  
   * ci/checks/check\_mirror\_schema.sh now:  
     * Enforces the PF12 key set (artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes).  
     * Rejects duplicate keys or unsorted rows.  
     * Validates proofs’ shape (requires mtime\_utc and produced\_at\_utc) and checks that proof sha/size match both mirror and filesystem; for index.machine\_mirror, it checks body hash and full size.  
   * tools/evidence/orientation\_demo.py:  
     * Treats INDEX \+ mirror \+ proofs as a topology and reports PROOF\_FIELDS, PROOF\_MTIME, SHA\_MISMATCH, SIZE\_MISMATCH etc.  
     * In \--check mode, distinguishes ORIENTATION\_MISMATCH (actual inconsistencies) from ORIENTATION\_DRIFT (stale report text only).  
4. **High-priority bug: path-proof** mtime\_utc **semantics still unresolved (bad)**  
   * The **first** implementation of mtime support made mtime\_utc equal to artifact\_path.stat().st\_mtime, and check\_mirror\_schema.sh compared this to the current stat each run. CI logs show PROOF\_MTIME errors across almost all artifacts:  
     * PROOF\_MTIME:N:2025-11-22T17:56:16Z\!=2025-11-22T18:02:14Z  
       indicating proofs captured an earlier mtime than the current stat() time.  
   * Codex correctly flagged a **P1 bug**: Git/CI do not preserve mtimes across clones, so “mtime equals stat” is not reproducible and will *routinely* drift.  
   * The **follow-up bug fix** in update\_evidence\_index.py and check\_mirror\_schema.sh attempted to:  
     * Stop using stat().st\_mtime and instead reuse or default mtime values to avoid drift (making mtime a deterministic/logical field rather than a FS stat transcript).  
     * Change check\_mirror\_schema.sh and orientation\_demo to validate **format only** and not equality with FS times.  
   * But the evidence tests still assert proof\["mtime\_utc"\] \== expected\_mtime\_from\_stat, causing:  
     * test\_mirror\_schema\_and\_parity and test\_evidence\_index\_has\_required\_artifacts to fail with assertions like:  
       * assert '2025-11-22T18:08:38Z' \== '2025-11-22T18:26:45Z'.  
   * Net: the repo is now in an **inconsistent state** where:  
     * check\_mirror\_schema.sh has been relaxed to format checks,  
     * update\_evidence\_index writes deterministic/logical mtime,  
     * but tests still demand mtime \== stat().  
5. **ABBA parity and mirror duplication issues were mitigated but not fully eradicated (partial)**  
   * The ABBA artifact (artifacts/engine/order/abba\_identity.bytes) is now generated as a 32-byte digest; path-proof and mirror entries reflect that in the final diff. However, at several points during remediation, stale 18-byte ABBA files coexisted with 32-byte metadata, and **duplicate mirror records** for ABBA and Machine Mirror appeared in artifacts/evidence\_index.jsonl.  
   * The final PR state shows a cleaned-up mirror with a single ABBA row and a single Machine Mirror row, but this safety depended on update\_evidence\_index being re-run in the correct sequence; there is still no guard preventing future stale ABBA/mirror drift if someone edits the artifact manually without re-running the updater.  
6. **CI status at close — failing evidence tests (bad, recorded as known debt)**  
   * The final CI run you attached shows:  
     * tests/evidence/test\_evidence\_skeleton.py::test\_mirror\_schema\_and\_parity failing on mtime\_utc.  
     * tests/ops/test\_evidence\_index.py::test\_evidence\_index\_has\_required\_artifacts failing for the same reason.  
   * Given you have elected to close PR4 despite these failures and handle them in a follow-up remediation PR, those test failures must be treated as **known, explicitly recorded defects** in WS-D4, not as unknown flakiness.

---

### Doc Deltas

These are the doc/build-notes updates implied by this PR and its outcomes:

* **PF10 — HDE-Build Notes (“HDE-EPIC017 PR4 Evidence Remediation”)**  
  * Add an addendum summarizing what PR4 actually did:  
    * Introduced engine/order comparators and ordering artifacts.  
    * Centralized evidence index writer in tools/evidence/update\_evidence\_index.py.  
    * Hardened Machine Mirror self-record and path-proof schema.  
    * Regenerated path-proofs across the repo.  
    * Tightened check\_mirror\_schema.sh and orientation\_demo.  
  * Explicitly note:  
    * CI failed on mtime\_utc tests and that path-proof mtime semantics are **unsettled**.  
    * A follow-up remediation PR (WS-D4b) will align update\_evidence\_index, check\_mirror\_schema, orientation\_demo, and tests on a single mtime\_utc story.  
* **PF09 — Canon-HDE-Build Checklist (D4 row)**  
  * Under D4 (“Deterministic tie-break & total-order module”), update the evidence row to point at:  
    * engine/order/comparators.py, engine/order/artifacts.py, tools/order/generate\_ordering\_artifacts.py.  
    * Ordering artifacts under artifacts/engine/order/\* and their proofs.  
    * Evidence tests tests/order/\*, tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py.  
  * Add a **note** that CI\_CHECK\_MIRROR\_SCHEMA\_OK is *temporarily red* due to mtime\_utc semantics, with a pointer to PF10’s PR4 addendum and the planned remediation PR.  
* **PF12 — Canon-HDE-Schemas and Artifacts (Machine Mirror & Proofs)**  
  * Document:  
    * The Machine Mirror self-record semantics (body hash \+ full size, role \== "self\_record").  
    * The path-proof schema (path,size\_bytes,sha256,mtime\_utc,produced\_at\_utc) for governed artifacts.  
  * Add a **TODO note** that mtime\_utc’s meaning is currently under remediation:  
    * Tests still assume mtime\_utc \== stat().  
    * This PR’s fix moved toward deterministic mtime independent of stat().  
    * PF canon will be updated once the remediation PR chooses the final behavior.  
* **PF14 — Canon-HDE-Mechanics Guide (Evidence workflow & WS-D4)**  
  * Update the evidence workflow section to:  
    * Call out tools/order/generate\_ordering\_artifacts.py and tools/evidence/update\_evidence\_index.py as the **sole writers** for ordering artifacts and evidence index/mirror/proofs.  
    * List the CI command sequence (generate → update evidence → orientation demo → mirror check → pytest).  
  * Note that mtime\_utc behavior and corresponding checks are in flux and will be finalized in the WS-D4 remediation PR.  
* **PF19 — Canon-Glow QA Guide (Proof semantics & checks)**  
  * Add a subsection describing:  
    * Path-proofs as “stat transcripts” including mtime and produced\_at.  
    * The pivot away from raw stat() equality toward a deterministic/logical mtime if that’s the final choice.  
  * Reference the current test/design discrepancy as a known defect until the remediation PR updates both tests and scripts.  
* **PF20 — Canon-HDE-Phased Epics (EPIC017 WS-D4 record)**  
  * In the EPIC017 D4 row:  
    * List the ordering comparators, ordering artifacts, and evidence hardening as delivered.  
    * Mark the mtime/CI issues as **open**, with a reference to the planned remediation epic or card (e.g., EPIC017-D4b / “Evidence mtime re-alignment”).

## ADDENDUM 8 \- PR04r

### PRO4R Review Summary

This follow-up PR (WS-D4b) successfully stabilizes **evidence** mtime\_utc **semantics**, fixes the ABBA ordering artifact parity, and wires a **write-then-check evidence refresh** into CI so that all ordering/evidence tests and mirror checks now pass. It aligns tools/evidence/update\_evidence\_index.py, ci/checks/check\_mirror\_schema.sh, the evidence tests, and CI workflow around a single, practical definition of mtime\_utc (refresh-time, monotone, UTC ISO) and regenerates all governed path-proofs accordingly. CI is green and the high-priority ABBA proof mismatch is resolved.

I don’t see any remaining correctness or canon-drift issues that require further remediation in this PR; the changes are coherent with PF12/PF14/PF19 and the EPIC017 WS-D4 remedial plan, and the new mtime semantics are clearly marked as NEW CANON in code comments for later drainage into PF docs.  
---

### Findings

1. mtime\_utc **semantics are now coherent and CI-stable (NEW CANON noted in code)**  
   * tools/evidence/update\_evidence\_index.py introduces \_isoformat\_from\_timestamp and \_parse\_utc\_iso8601, and reworks \_write\_path\_proof to:  
     * Always compute size\_bytes and sha256 from the artifact on disk.  
     * Set mtime\_utc either from an explicit argument (the current stat().st\_mtime, truncated), an existing proof, or a default, and validate format in \--check mode.  
     * Treat mtime\_utc as **refresh-time mtime**, not something that must match future clone mtimes, and enforce only that it is a UTC ISO8601 timestamp with zero microseconds and not later than the current stat().st\_mtime.  
   * Evidence tests in tests/evidence/test\_evidence\_skeleton.py and tests/ops/test\_evidence\_index.py now assert:  
     * mtime\_utc parses as UTC with microsecond \== 0\.  
     * parsed\_mtime \<= stat\_mtime (monotone semantics) instead of strict \== equality.  
     * Comments explicitly mark this as **NEW CANON (EPIC017 WS-D4)** for mtime\_utc.  
2. **Mirror schema check enforces shape \+ monotonicity without requiring strict mtime equality**  
   * ci/checks/check\_mirror\_schema.sh now includes parse\_utc\_iso8601 and:  
     * Validates each record has the PF12 key set (artifact\_key, discovered\_physical\_path, produced\_at\_utc, proof\_anchor, role, sha256, size\_bytes).  
     * Ensures mtime\_utc and produced\_at\_utc exist and are valid UTC ISO8601 timestamps with zero microseconds.  
     * For normal artifacts, checks that mtime\_utc is **not later** than the current FS stat().st\_mtime, but does not require exact equality.  
     * Continues to enforce Machine Mirror semantics (body hash \+ full file size; single index.machine\_mirror self-record) and strict sha/size parity between mirror, proofs, and artifacts.  
3. **ABBA ordering artifact and its evidence are finally aligned**  
   * artifacts/engine/order/abba\_identity.bytes has been regenerated via tools/order/generate\_ordering\_artifacts.py so that:  
     * The on-disk file is 32 bytes; its SHA matches the canonical digest computed by engine/order/artifacts.py.  
     * The mirror record for engine.order.abba\_identity.bytes in artifacts/evidence\_index.jsonl and the associated path-proof (abba\_identity.bytes.path\_proof.txt) both record the 32-byte size and correct SHA.  
   * A high-priority bug where the proof was updated to 32 bytes / new SHA while the binary remained an 18-byte legacy payload has been fixed by regenerating the artifact and re-adding it, and python tools/order/generate\_ordering\_artifacts.py \--check now passes.  
4. **All governed path-proofs have been refreshed under the new semantics**  
   * This PR rewrites a large set of \*.path\_proof.txt files across artifacts/\*\* and audit/\*\* to:  
     * Use the new mtime semantics (single mtime\_utc line, monotone vs artifact stat()).  
     * Retain produced\_at\_utc as the logical “evidence refresh time,” reusing the previous value or a default per run.  
   * The mirror (artifacts/evidence\_index.jsonl) and its path-proof are also refreshed so the Machine Mirror self-record and its proof match the body hash and file size.  
5. **CI workflow now includes a write-then-check evidence refresh and full suites**  
   * .github/workflows/ci.yml has been updated to:  
     * Install dependencies, run env/CLI checks.  
     * Run python tools/order/generate\_ordering\_artifacts.py and python tools/evidence/update\_evidence\_index.py (write mode) to refresh artifacts and evidence in the ephemeral CI tree.  
     * Run generate\_ordering\_artifacts.py \--check, update\_evidence\_index.py \--check, tools/evidence/orientation\_demo.py \--check, check\_evidence\_index\_hash.sh, check\_bridge\_consistency.py, check\_mirror\_schema.sh, check\_final\_lf.sh.  
     * Then run pytest tests/evidence tests/ops/test\_evidence\_index.py and pytest tests/order tests/mech/test\_order\_properties.py.  
   * This sequencing ensures that tests and schema checks always run against a self-consistent set of artifacts, mirror, and proofs, satisfying the EPIC017 WS-D4 requirement for an explicit evidence refresh pipeline.  
6. **Bug fix record is clear and self-documenting**  
   * The bug report notes the P1 issue (“Align abba\_identity proof with actual artifact contents”) and the fix summary (“Regenerated artifacts/engine/order/abba\_identity.bytes so its contents now match the recorded 32-byte size and SHA”) with explicit testing commands (generate\_ordering\_artifacts.py \--check).  
   * The WS-D4b PR description notes that this PR:  
     * Adopts monotonic refresh-time semantics for mtime\_utc.  
     * Relaxes mirror/tests to match that semantics.  
     * Regenerates ABBA and path-proofs.  
     * Updates CI to perform a write-then-check evidence refresh and full suites.

Given that CI is passing (mirror schema, evidence tests, ordering tests), and the changes are bounded to evidence/ordering surfaces and CI, I don’t see any remaining issues that require immediate remediation in this PR.  
---

### Doc Deltas

These deltas should be captured in PF docs and PF10:

* **PF12 — Canon-HDE-Schemas and Artifacts (Machine Mirror & path-proofs)**  
  * Document the updated path-proof schema: path, size\_bytes, sha256, mtime\_utc, produced\_at\_utc.  
  * Define mtime\_utc as **refresh-time mtime** (filesystem mtime at the time of evidence refresh, truncated to seconds, UTC ISO), not as something that must remain equal to future stat() values across clones.  
  * Define produced\_at\_utc as the logical evidence refresh timestamp; note that mtime\_utc must be a valid UTC timestamp with zero microseconds and **not later** than current FS mtime (monotone semantics).  
* **PF14 — Canon-HDE-Mechanics Guide (Evidence workflow and WS-D4)**  
  * Update the “Evidence workflow” section to:  
    * Name tools/evidence/update\_evidence\_index.py as the single writer for INDEX, sentinel, mirror, and path-proofs.  
    * Name tools/order/generate\_ordering\_artifacts.py as the single writer/checker for ordering artifacts.  
    * Record the WS-D4 canon for mtime\_utc (refresh-time, monotone) as described above.  
* **PF19 — Canon-Glow QA Guide (Evidence CI rails and** mtime\_utc **semantics)**  
  * Describe the CI pipeline: generate → update evidence (write) → generate/check → evidence checks → mirror schema → pytest.  
  * Clarify that QA checks validate mtime\_utc format and monotonicity vs stat(), not strict equality, and that any future changes to this behavior must be reflected in both scripts and tests.  
* **PF09 — Canon-HDE-Build Checklist (EPIC017 D4 row)**  
  * Mark CI\_CHECK\_MIRROR\_SCHEMA\_OK, EVIDENCE\_PATH\_PROOFS\_SHAPE\_OK, ORDERING\_ARTIFACTS\_SINGLE\_SOURCE\_OK, and ORDERING\_ARTIFACTS\_DETERMINISTIC\_OK as green, pointing to:  
    * tools/order/generate\_ordering\_artifacts.py, engine/order/artifacts.py, and tests/order/\*.  
    * tools/evidence/update\_evidence\_index.py, ci/checks/check\_mirror\_schema.sh, and tests/evidence/test\_evidence\_skeleton.py, tests/ops/test\_evidence\_index.py.  
* **PF20 — Canon-HDE-Phased Epics (EPIC017 WS-D4 tokens)**  
  * For EPIC017 WS-D4, list that:  
    * Ordering comparators and artifacts are in place and deterministic.  
    * Evidence index/mirror/proofs follow the new mtime semantics.  
    * All CI gates (mirror schema, evidence tests, ordering tests) pass.  
* **PF10 — HDE-Build Notes (EPIC017 PR4/WS-D4 addendum)**  
  * Extend the EPIC017 WS-D4 addendum to include WS-D4b:  
    * Note that WS-D4b resolved the mtime\_utc vs stat().st\_mtime inconsistency by adopting refresh-time semantics and monotone checks.  
    * Note that ABBA artifact parity is now fully aligned in dev and CI clones, and that all WS-D4 evidence tokens are green.

