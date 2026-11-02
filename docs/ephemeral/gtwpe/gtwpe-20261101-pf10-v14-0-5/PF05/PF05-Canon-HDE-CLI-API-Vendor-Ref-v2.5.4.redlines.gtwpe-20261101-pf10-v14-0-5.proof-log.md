# Proof log — PF05 redlines — gtwpe-20261101-pf10-v14-0-5 — T-02 — drain-r2

## 1. Identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.md`, in this directory |
| This log | `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Directory | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-02/drain-r2`. It supersedes `drain-r1` (commit `0d22343e742c08012fc3bb6d613fb0c334026725`) at the same paths, on the Product Owner's direction of 2026-11-02 (§1A). `drain-r1` stays readable in that commit. |
| Preparer | TW-DRAIN-10 "Prepare PF Document Redlines", version 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of each run (`drain-r1` and `drain-r2`; page last edited 2026-10-09T11:05:22Z, unchanged between them) |
| Session | The Claude Code document session Nathan started for T-02, on branch `claude/gtwpe-triage-authoring-j94ewf`, 2026-11-02 (UTC). `drain-r2` runs in the same session, under Nathan's T-02 remediation handoff. No subagent, reviewer or other session was used. |
| Authorized sequence | The remediation handoff authorizes TW-DRAIN-10 (`drain-r2`), then TW-APPLY-10 100926.1 (page `3f44590a05eb81eebff6e3afa3d9aa5b`, run `apply-r2`), in this session, replacing the `apply-r1` output |
| Preparation outcome | `READY` |
| Save state | Recorded in §11 after both files were read back |

## 1A. Correction in drain-r2 (Product Owner direction, 2026-11-02)

Direction. In the T-02 remediation handoff of 2026-11-02, the Product Owner directed a corrected package. Its terms:

- Location: §1 "Map at a Glance", the bullet "Legacy BodyGraph fallback and bounded HumanDesignAPI v2 chart path — implemented with remaining PF05 gaps." (v2.5.4 line 119).
- `drain-r1` §8 kept this bullet as a dated repository-state record. It stays a dated record, but it must stop calling the legacy route a fallback. Its title and the sentence "non-v2 bases retain an explicit legacy `bodygraphs` fallback" contradict HDE Build Notes v14.0.5 2.1 D-2 ("The v1 path is retained legacy selection, not fallback"; "No non-v2 base reaches bodygraphs by fallback") and PF05's own §7.1.10.
- The corrected bullet must: (a) keep its pin `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, its nonclaims and its pointer to §§7.1.10, 7.2 and 7.4; (b) say that a terminal v1 base selects the retained legacy `bodygraphs` route under §7.1.10, as legacy selection, not fallback; (c) say that legacy selection by any other non-v2 base, at that pin, is the material gap recorded in §7.2.0, not a retained capability; (d) not use "fallback" for the legacy route, in the title or the body.
- Before writing (c), check the current behaviour read-only, and stop if the code no longer selects legacy for other non-v2 bases. Search all of v2.5.4 for any other text that calls the legacy route a fallback.
- Unchanged: the thirteen `drain-r1` operations, renumbered only if position requires it; RL-13's v2.5.5 Change Log entry is extended to cover this change; §7.2.0 stays as written (H-09); AGENTS.md is not edited (H-05); the source is HDE Build Notes v14.0.5 2.1 D-2, lines 277–344 (row C-02), and the Last Update Gate stays `BN 14.0.5`.

What `drain-r1` said and what is now true. `drain-r1` §8 left line 119 unchanged as "a dated repository-state record", on the ground that it described implementation, not policy. Its wording still calls the legacy route a fallback, in the title and the body, and so restates the posture D-2 rejects. `drain-r2` adds RL-14, which keeps the record and its pin and corrects only that characterization.

Behaviour check (read-only, closed rails, `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`; `engine/` is identical at `e2b7427`):

- `engine/bodygraph/vendor_client.py` lines 102–109: `_configured_base_version` lower-cases every path segment and returns `v2` if any segment is `v2`, `v1` if any is `v1`, otherwise `unversioned`.
- Lines 124–153: `classify_bg_resolve_route_policy` gives the v2 chart route only for `v2`. Every other result, including `unversioned`, gets resource `bodygraphs`, route family `legacy_bodygraph`, classification `explicit_legacy_fallback` and `supported: True`.
- `engine/bodygraph/resolver.py` lines 686–705: `_classify_env_route_policy` passes the configured base straight to that classifier.

So the code still selects the legacy route for non-v2 bases other than a terminal `v1`, and (c) holds. The pin `cc754cfb` itself is not in this clone's shallow history and could not be read. RL-14 therefore makes no new claim about it: it re-characterizes the behaviour the dated record already states at that pin, which current code still shows.

Search. An exact case-insensitive search of all of v2.5.4 for "fallback", "fall back", "falls back" and "falling back" found 25 lines. Only two call the legacy route a fallback:

- Line 119, the bullet above. RL-14 corrects it.
- Line 956, §4.6 ("Non-v2 configured bases MAY preserve the legacy BodyGraph route only as explicit legacy fallback"). `drain-r1` RL-01 already corrects it.

The other 23 concern vendor, local, timezone, credential, base-URL or narrative fallbacks, or negate fallback (lines 3493 and 4306). After `drain-r2`, every remaining "fallback" near "legacy" in the simulated result is a negation. A T-04 finding of line 119 alone is consistent with reading v2.5.5, where line 956 was already corrected.

Changes in `drain-r2`:

- RL-14 (new, CONSISTENCY, row C-02): replaces line 119. The title becomes "Retained legacy BodyGraph selection and bounded HumanDesignAPI v2 chart path — implemented with remaining PF05 gaps." The clause "; non-v2 bases retain an explicit legacy `bodygraphs` fallback." becomes ". A terminal `v1` base selects the retained legacy `bodygraphs` route under §7.1.10, which is legacy selection, not fallback. Legacy selection by any other non-v2 base at that pin is the material gap recorded in §7.2.0, not a retained capability." The pin, the Fermentation sentence, the nonclaims and "See §§7.1.10, 7.2, and 7.4." are unchanged. The word "fallback" now appears in the bullet only in "not fallback", which (b) requires.
- RL-13 (extended): the v2.5.5 Change Log entry adds "and correct the §1 legacy-route wording to terminal-v1 legacy selection with the §7.2.0 non-v2 gap". The first `drain-r2` build worded this "instead of a legacy fallback". It was reworded before saving so that the entry doesn't use the term either.
- RL-01 to RL-12: unchanged, byte for byte. No renumbering: each operation binds to its own unique original span, so IDs need not follow document order. RL-14 sits at line 119, before RL-01.

Not changed by this correction: §7.2.0 (H-09, held) and AGENTS.md (H-05). The Product Owner separately instructed the AGENTS.md edit for a new PR, and it went to draft PR [amthorn78/glow-hdengine-v2#827](https://github.com/amthorn78/glow-hdengine-v2/pull/827), on its own branch, outside this package and this ledger task.

## 2. Target

| Field | Value |
| :---- | :---- |
| Path | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` |
| In-document title | `PF05-Canon-HDE-CLI-API-Vendor-Ref` (logical title HDE CLI/API/Vendor Ref) |
| Version | v2.5.4, Status `Canon`, Effective date 2026-10-26 |
| Git blob | `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe` |
| SHA-256 of the original bytes | `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028` |
| Size | 327,342 bytes; 4,461 lines; UTF-8; LF only (zero CR bytes); ends with `---` and one blank line |
| Read at | `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`, the handoff and ledger baseline |
| Currency check | `origin/main` moved to `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` during the session. `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty, and the PF05, PF10 and PF03 blobs are identical at both commits. No target or source change affects this package. Re-checked for `drain-r2`: unchanged. |
| Scope anchor | §0.2 "Scope", Ownership bullet: PF05 owns the bytes for CLI, Reader transport and Vendor ingest |
| Coverage | Complete. `drain-r2` reuses this session's complete reading of the same verified bytes, and re-read line 119 and the whole-file fallback search above. Lines 1–4,461 were read in full, in windows of up to 400 lines with no gap: 1–400, 400–800, 800–1200, 1200–1600, 1600–2000, 2000–2400, 2400–2800, 2800–3200, 3200–3529, 3529–3858, 3858–4178, 4178–4461. Every heading, table, fence and appendix was inside a window. |

Baseline document-control schema, for TW-APPLY-10 (§0.1 "Header", lines 5–10, exact field order):

- `**Title:** PF05-Canon-HDE-CLI-API-Vendor-Ref`
- `**Version:** v2.5.4`
- `**Status:** Canon`
- `**Effective date:** 2026-10-26` (ISO `YYYY-MM-DD`)
- `**Last Update Gate:** BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md ` (the baseline value carries one trailing space before its two-space line break)
- `**Invocation tag:** INV-f2ac55d77ce9aacc`

Lines 5–8 end with a two-space Markdown line break, line 9 with three spaces, and line 10 with none. The baseline names HDE Build Notes in the Last Update Gate as `BN <version>`. No other line restates the document's own version or date, except the §11.1 Change Log entries, which are history.

Version scheme. The Change Log runs v2.4.6, v2.4.7, v2.4.8, v2.4.9, v2.5.3, v2.5.4, so a revision bumps the patch number. The version TW-APPLY-10 is expected to derive is v2.5.5. RL-13 names v2.5.5 in the Change Log entry. The Change Log format records no date.

## 3. Source and inputs

Source of the update, in source order (for the Last Update Gate):

1. `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5 (effective 2026.11.01). Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` (recomputed in this session from the blob); 385,734 bytes; 1,976 lines; read at `e2b7427`. It is the single unlettered PF10 base version on `main`.

No other source justified a change. PF05's own rules in §0.4 and §11.1 require the Change Log entry (RL-13); they are the target's rules, not a second source.

Selected units, each read completely in this session:

| Unit | SRC-1 lines | Rows |
| :---- | :---- | :---- |
| 2.1 D-1, "The production vendor override covers showcompat and conjunction acquisition (S19-R01)" | 225–276 | C-01 |
| 2.1 D-2, "Vendor route selection fails closed outside a terminal v1 or v2 (S19-R02)" | 277–344 | C-02 |
| 2.1 D-3, "POST /api/compat/v1 is a dev/admin surface (S19-R03)" | 345–396 | C-03 |
| 2.1 heading, timestamp and details; "Decision and approval status" | 205–224 | C-06 |
| 2.1 "Scope, exclusions and nonclaims"; "Dependencies and unresolved obligations"; "Evidence" | 491–516 | C-06 |

D-4 and D-5 (lines 397–490) were not selected and were not read for drainage.

Other inputs:

| Input | Identity | Role |
| :---- | :---- | :---- |
| Ledger `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` | Commit `142feb35144d8795f927e0c78b665ace52279064`, the head of `claude/gtwpe-triage-authoring-j94ewf` at session start | Routing only: task T-02, rows C-01, C-02, C-03, support C-06, holds H-05 and H-09. Not a change source and not a Last Update Gate. |
| `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` | v1.8.8, blob `504712df548a02f3aa4e7b8c37027385e46a3878`, 633 lines, read in full | Common editorial standard |
| Draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826) | Open, draft, head `142feb3` at session start | Shared execution destination |
| Product Owner direction, 2026-11-02 (T-02 remediation handoff) | Inline in this session; terms in §1A | Correction authority for RL-14 and the RL-13 extension. Not a change source for the Last Update Gate, which stays `BN 14.0.5`. |

Supporting reading, not drainage:

| Document | Sections | Why |
| :---- | :---- | :---- |
| PF04-Canon-HDE-Governance v2.8.8 | §4.1.4 "Rails posture — closed refusal; open conformance", including "Dev/admin APP_ENV gating (dev/test/local only)"; §8.3.2; §8.3.4 | Confirms the anchors D-3 cites and RL-02 names. PF04 is T-01's target and is not edited here. |
| PF07-Canon-Glow-Infrastructure v2.3.4 | §2.2 "Environment facts" | Confirms the shared database and the documented `127.0.0.1` access that RL-02's residual-risk line routes to |
| PF30.1-Canon-HDE-CRD-Records v0.9.2 | HDE-CRD-0002 record, "Deferred or residual work" | Confirms the term "Candidate CRD Items List item 9" that RL-02 and RL-07 use |
| HDE Build Notes v14.0.5 front matter, "Precedence, versioning, and scope" §1 to §3 | Lines 1–60 | PF10 authority and addendum scope. Not drained (ledger row C-00). |
| HDE Build Notes v14.0.5, all lines outside 2.1 | Search only | `grep` for `allow-prod-vendor`, `compat/v1`, `PROVIDER_ROUTE_UNSUPPORTED`, `PROD_OVERRIDE`, `Vendor Ref` and `item 9` outside lines 205–516 found no occurrence. No later addendum overlaps D-1 to D-3. |

## 4. Canon relied on

- HDE Build Notes v14.0.5, front matter "Precedence, versioning, and scope" §1 "PF10 authority" and §2 "Scope within an individual PF10 document"; addendum 2.1, D-1, D-2 and D-3, with its status, scope, dependencies and evidence parts.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.4, all of it, in particular §0.2 "Scope", §0.3 "Tagging convention", §0.4 "Change policy", §4.6, §5.5, §7.1.10, §7.1.11 to §7.1.11f, §7.2.0 and §11.1.
- PF03-Reference-Technical-Writing-Best-Practices v1.8.8, §3 "Governing editorial principles", §5, §6, §7, §8, §9 "Source selection and citation", §11 and §14.
- PF04-Canon-HDE-Governance v2.8.8 §4.1.4, §8.3.2 and §8.3.4; PF07-Canon-Glow-Infrastructure v2.3.4 §2.2; PF30.1-Canon-HDE-CRD-Records v0.9.2, HDE-CRD-0002 record. These were read in support only.
- AGENTS.md (repository agent rules): canon-first rule, PF canon read-only, closed rails and PF10 citation rule. Read as governing instructions.

## 5. Repository inspection (closed rails)

All inspection was read-only, with `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1` and `ALLOW_NETWORK=0`, using `git show` and `git grep` against `e2b7427ff418ca8f08f05587c4a541308a76da56`. No vendor or provider call was made. `git diff --stat e2b7427 origin/main -- engine adapter` is empty, so every finding below holds equally at `84d6d1c`.

| Claim used in a redline | Evidence at `e2b7427` |
| :---- | :---- |
| The CLI pre-scan refuses `--allow-prod-vendor` on every command other than `bg:resolve` | `engine/cli/main.py` lines 52–59 (usage strings, including "accepted only by bg:resolve --source vendor") and lines 231–256 (`_allow_prod_vendor_usage_error` returns the command usage error unless the command is `bg:resolve`); line 293 runs it before argparse |
| `bg:resolve` refuses the flag with a non-vendor source | `engine/cli/main.py` lines 260–262 |
| Conjunction mode passes the vendor source policy for every source other than `db` or `auto`, including an absent `--source` | `engine/cli/main.py` line 799 (`source_policy="local" if source in ("db", "auto") else "vendor"`); lines 112–116 declare `showcompat --source` with choices `db`, `vendor`, `auto` and no default |
| The compat chart resolver applies the generic rails but not the production override | `engine/bodygraph/resolver.py` line 1083 `resolve_compat_chart`: its body (lines 1083–1175) references rails but no authorization reference, override or audit. The override lives in lines 171–380 (`resolve_bodygraph` path). |
| The compat route guard refuses only production-like posture | `engine/http/compat_handler.py` line 5 imports `_compute_env_mode` from `adapter/env_guard.py`; line 112 returns 404 only when it yields `prod` |
| `_compute_env_mode` treats absent or blank `APP_ENV` and `ENGINE_ENV` as `dev` and passes other values through | `adapter/env_guard.py` line 17 (`_PROD_ALIASES = {"prod", "production", "live"}`) and lines 31–51 |
| (`drain-r2`) Every non-v2 base other than a terminal `v1`, including an unversioned one, still selects the legacy route | `engine/bodygraph/vendor_client.py` lines 102–109 and 124–153; `engine/bodygraph/resolver.py` lines 686–705 (§1A), checked at `84d6d1c` |

These findings concern checked-in bytes only. They establish no runtime behavior, test result, deployment or acceptance.

## 6. The decision in the handoff: D-1 l.259 against the existing §7.1.11 text

The handoff asked this session to reconcile D-1 l.259 with "the existing §7.1.11 'Required-Now implementation gap (DD-04; held)' paragraph". The ledger's T-02 row says the same.

Finding. That paragraph does not exist in the v2.5.4 baseline. An exact search for `DD-04; held` in PF05 returns no occurrence. The only `DD-04` in PF05 is line 3507, inside §7.1.11 "Implementation state (informative)", which records that HDE-CRD-0002 delivered the contract as S14 and so resolved DD-04. The PF05 v2.5.4 Change Log (line 4148) records that v2.5.4 removed the override from the gap statements; the v2.5.3 entry (line 4147) is where "retain held DD-04" appears. The handoff's label describes v2.5.3 wording. The clone's history is shallow, so the v2.5.3 bytes could not be read to confirm the exact earlier text.

Resolution. D-1 l.259 targets the text that v2.5.4 actually carries: the bullet "The gate covers only the command §7.1.11a names …" in the "These limits apply:" list of "Implementation state (informative)". D-1 makes that limit "a gap against this decision, not a decided limit". So:

- RL-07 moves the bullet out of the limits list and restates it as a "Required-Now implementation gap", with bounded inspection at `e2b7427` (§5) and the implementing change (Candidate CRD Items List item 9).
- RL-06 narrows the delivery sentence to `hdctl bg:resolve --source vendor`, because once the contract covers three paths, S14 delivered one of them.
- DD-04 stays resolved for `bg:resolve`, as v2.5.4 records. No held DD-04 posture is restored: the gap D-1 creates is a new gap against a new decision, not DD-04.

## 7. Change and disposition ledger

Every change in the selected units has one disposition.

### D-1 (C-01), SRC-1 lines 225–276

| Source item | Disposition | Target location |
| :---- | :---- | :---- |
| Three-path scope: bg:resolve, showcompat `--source vendor`, conjunction when it selects vendor acquisition (l.229–232) | RL-08 | §7.1.11a |
| Each path applies §7.1.11b, §7.1.11c and §7.1.11e unchanged (l.233) | RL-08 | §7.1.11a |
| The flag is accepted by those paths and no other command; syntax, single occurrence and value rules unchanged (l.234) | RL-08; the syntax, regex and invalid-value text (lines 3535–3541) is already represented and kept | §7.1.11a |
| Order: §7.1.11d applies to each path; step 2 reads "the invocation selects vendor acquisition"; misuse is usage, exit 64, for db, auto and conjunction with db or auto (l.235) | RL-08 (order applies to each path); RL-09 (step 2); RL-11 (usage carrier wording) | §7.1.11a, §7.1.11d, §7.1.11e |
| Scope of one authorization: at most one acquisition per party, two for a pair; no write, no public Reader or Aux traffic, no opening of a closed rail (l.236–238) | RL-10 | §7.1.11d |
| Audit: one §7.1.11f event per production-like invocation of these paths before any I/O; command is one of three values; every other field and exclusion unchanged (l.239–241) | RL-12 (command values). The event rule is already represented by the path-neutral first sentence of §7.1.11f (line 3594) together with RL-08's "each path applies"; no edit there. | §7.1.11f |
| Error carrier: showcompat refusals use its existing typed carrier with the same four codes and exit 1; outbound-attempt count 0 (l.242–244) | RL-11; outbound-attempt count 0 is already represented (line 3588, kept) | §7.1.11e |
| Basis (l.246–251) | Rationale only; recorded in RL-07 to RL-12 | — |
| "Canon superseded": §7.1.11a, §7.1.11d step 2, §7.1.11e, §7.1.11f (l.255–258) | RL-08, RL-09, RL-11, RL-12 | as listed |
| "Canon superseded": §7.1.11 implementation-state limit becomes a gap (l.259) | RL-06, RL-07; see §6 | §7.1.11 |
| HDE Governance §3.1 unchanged (l.260) | No PF05 edit | — |
| Drainage targets: HDE Users Guide §13.3 and §16 (l.265) | Out of this target: T-08 (PF29) | — |
| Drainage target: AGENTS.md "Showcompat Live QA posture" (l.266) | H-05: not a PF target and not in this package. The Product Owner instructed it on 2026-11-02 for a separate PR (draft PR #827). | — |
| Consequences for tests, evidence and frozen captures (l.268–273) | Not PF05 text; belongs to the implementing change (item 9). No edit. | — |
| Left undecided: none (l.275) | Nothing to drain | — |

### D-2 (C-02), SRC-1 lines 277–344

| Source item | Disposition | Target location |
| :---- | :---- | :---- |
| What governs: §7.1.10 governs route selection and the configured-base boundary for bg:resolve and compat chart acquisition by showcompat and conjunction (l.281–283) | RL-05 | §7.1.10 scope sentence (line 3476) |
| Selection: terminal case-sensitive v2 and v1; every other base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or I/O (l.284–286) | Already represented | §7.1.10 lines 3478–3480 |
| The base: absolute HTTPS, host, no userinfo, query or fragment, ends in v1 or v2 (l.287) | Already represented | §7.1.10 line 3487 |
| The v1 path is retained legacy selection, not fallback; retirement needs a separate versioned decision (l.288) | Already represented | §7.1.10 line 3493 |
| No fallback: no non-v2 base reaches bodygraphs by fallback (l.289) | Already represented in §7.1.10 (lines 3480–3481, 3493). RL-01 removes the contradicting permission in §4.6 (line 956, "Non-v2 configured bases MAY preserve the legacy BodyGraph route only as explicit legacy fallback"). RL-14 (`drain-r2`) corrects the §1 dated record (line 119), which called the legacy route a fallback. | §7.1.10; §4.6; §1 |
| The two canon rules fit together; single permitted classification; HDE Mechanics Guide §1.1 prohibitions (l.290–297) | Out of this target: it adds to HDE Mechanics Guide §1.1 (T-05). PF05 §1 line 123 already forbids inferring route or auth from hardcoded `/v1` or `/v2` strings; no conflict, no edit. | — |
| Classification label `explicit_legacy_fallback` kept as an existing wire value (l.298) | Out of this target: it is a governed-evidence wire value, not a PF05 byte contract, and PF05 never mentions it (exact search, no occurrence). D-2 names no PF05 location for it. | — |
| Basis (l.300–308) | Rationale only | — |
| "Canon superseded": HDE Mechanics Guide §1.1 (two items), HDE Users Guide §11.3, §13.3, §16, Plan Templates route-policy posture (l.312–314, l.316) | Out of this target: T-05, T-08, T-07 | — |
| "Canon superseded": HDE CLI/API/Vendor Ref §7.1.10 added to (l.315) | RL-05 | §7.1.10 |
| Drainage target: §7.2.0, "the gap, once the implementing change delivers" (l.322) | Held, H-09 (see §8) | — |
| Drainage target: AGENTS.md EPIC036 and EPIC038 lines (l.324) | H-05: outside this package; draft PR #827 | — |
| Consequences for tests, evidence and frozen captures (l.326–339) | Not PF05 text; implementing change. No edit. | — |
| Left undecided: v1 retirement stays a separate versioned decision (l.341–343) | Already represented | §7.1.10 line 3493 |

### D-3 (C-03), SRC-1 lines 345–396

| Source item | Disposition | Target location |
| :---- | :---- | :---- |
| Classification: the compat namespace and descendants are a dev/admin-only surface under HDE Governance §4.1.4 (l.349) | RL-02 (gate bullet) | §5.5 "Validation and environment gating" |
| Gate order, step 1: production-like posture keeps its 404 response (l.351) | Already represented | §5.5 line 2492 |
| Gate order, step 2: served only when `APP_ENV` is exactly dev, test or local; otherwise 403 `ERR_WRITER_FORBIDDEN`, no-store, no ETag, no HEAD body; `ENGINE_ENV` never admits (l.352–354) | RL-02 | §5.5 "Validation and environment gating" |
| Gate order: the existing method, probe and POST rules apply (l.355) | RL-02 (last sentence of the gate bullet); RL-03 aligns "Method and subpath handling", which said "In non-production posture" | §5.5 |
| Authentication: no credential while admitted only under dev, test or local; "authenticated" and "internal authentication" withdrawn (l.356–358) | RL-02 (Authentication bullet; Success body), RL-04 (Parity) | §5.5 |
| Wider exposure: a later decision must require the §8.3.2 credential or an equivalent pinned in PF05, and add the §8.3.4 logging rules (l.359–361) | RL-02 (Authentication bullet) | §5.5 |
| Residual risk, accepted and recorded (l.362–364) | RL-02 (Residual risk bullet), routed to Glow-Infrastructure §2.2 for the access facts | §5.5 |
| Basis (l.366–373) | Rationale only. Its code facts at `adbacfa2` were re-inspected at `e2b7427` (§5) and support RL-02's implementation-state bullet. | — |
| "Canon superseded": §5.5 "Validation and environment gating" added to (l.377) | RL-02 | §5.5 |
| "Canon superseded": §5.5 "Success body" and "Parity (clarified)": "authenticated" superseded (l.378) | RL-02, RL-04 | §5.5 |
| "Canon superseded": HDE Governance §4.1.4 added to; §8.3 unchanged (l.379–380) | Out of this target: T-01 (PF04) | — |
| Drainage targets: HDE Governance §4.1.4; HDE Users Guide §16 (l.385–386) | Out of this target: T-01, T-08 | — |
| Consequences for tests and evidence; compat-route proof bytes need no change (l.388–393) | No PF05 edit. §5.5 "Evidence" (lines 2522–2531) stays as written. | — |

### C-06 context, SRC-1 lines 205–224 and 491–516

| Source item | Disposition |
| :---- | :---- |
| Decisions are canon from publication and govern conflicting permanent text until drained (l.211) | Applied: this package drains them |
| Each fix belongs to the implementing change for Candidate CRD Items List item 9 (l.223) | Applied in RL-02 and RL-07, which name item 9 by title only |
| Nonclaims: no code, test, tool, schema or evidence change; no CRD identity or Specification for item 9; no QA, acceptance, PF09/PF30 movement, deployment or closure (l.497–500) | Applied: no redline claims implementation, QA or closure. The gap statements say the gates are not delivered. |
| Item 9 is open; drainage targets are unperformed; AGENTS.md needs the Product Owner (l.506–507) | Applied; H-05 and H-09 below |
| Current facts read at `adbacfa2`; a later code change makes a consequence a fresh question, not the decision (l.502) | The code facts were re-read at `e2b7427` (§5); none changed the decisions |

### RL-13

PF05 §0.4 "Editorial vs. normative" and §11.1 "Policy" require any change to transport or the public contract to be logged. RL-13 adds the v2.5.5 entry in the existing one-line format, with "Sentinel updated: NO" because no Human Evidence Index change is made.

## 8. Held, out-of-target and considered items

Held. Not drafted.

| ID | Item | What it waits for |
| :---- | :---- | :---- |
| H-09 | PF05 §7.2.0 gap row under D-2 (SRC-1 l.322), "broad non-v2 legacy selection", line 3626 | D-2 drains it only "once the implementing change delivers". That change is Candidate CRD Items List item 9, which is open (SRC-1 l.506) and has no CRD identity or Specification. The gap stays as written until item 9 delivers and the route classifier fails closed. |
| H-05 | AGENTS.md edits under D-1 and D-2 (SRC-1 l.266, l.324, l.507) | Not a PF target, and not in this package. The Product Owner instructed them on 2026-11-02 for a separate PR: draft PR [amthorn78/glow-hdengine-v2#827](https://github.com/amthorn78/glow-hdengine-v2/pull/827), on branch `claude/nifty-thompson-jjwptl`. |

Considered and left unchanged, with reason:

| PF05 location | Why no edit |
| :---- | :---- |
| §1 "Vendor ingest (HDAPI)", line 119: "non-v2 bases retain an explicit legacy `bodygraphs` fallback" | Superseded in `drain-r2`. The `drain-r1` disposition, preserved as written: "A dated repository-state record pinned to `main@cc754cfbce2f288b16ced5eef3d0f66a6ef5928a`, pointing to the remaining gaps in §7.2. It describes implementation, not policy, and it changes when the H-09 gap closes." That left the bullet calling the legacy route a fallback, contrary to D-2. By the Product Owner's direction, RL-14 now corrects it and keeps the dated record (§1A). |
| §3.7 "Interim no-user QA mode": `showcompat --source vendor` in pre-Glow production QA | The subsection states that CLI bytes and flag semantics elsewhere in PF05 remain canonical. It does not say the flag is unneeded, so it does not conflict with §7.1.11. The operator-facing restatement D-1 names is AGENTS.md (H-05). |
| §4.1.2 "Rails interaction" and §4.1.4 "Errors and exit codes" | Rails remain a necessary condition. §4.1.4's exit-1 single-token carrier is the carrier RL-11 points to. Neither conflicts. |
| §4.1.6 "Implementation status" | The override gap is recorded once, in §7.1.11 (RL-07), which D-1 names. Repeating it would create a second home. |
| §5.6 Endpoint Catalog row for `/api/compat/v1`: "production-excluding environment gate" | Still true and not contradicted. The Catalog record's `env_gate` value is owned by HDE-Schemas & Artifacts, and D-3 names no §5.6 change. A later Catalog update belongs with the implementing change. |
| §7.2.0 line 3626: "The production-vendor override flag and audit gate … are delivered (§7.1.11)" | Inside the held §7.2.0 paragraph (H-09), and a dated record at `0838ba08`. Its §7.1.11 pointer leads to RL-07's gap statement. |
| Existing ellipses at lines 279, 2117, 2188, 2495 and 3239 | Pre-existing example elisions and a code literal. PF03 forbids ellipses, but TW-DRAIN-10 applies PF03 to authorized wording only, and these are not the drafting markers it authorizes as hygiene. No redline adds an ellipsis. |
| `[OPEN]` markers at lines 251, 255, 866 and 1031 | Canon-recorded open decisions, not drafting notes. Kept. |

No `Draft` status language, TODO, TBD or drafting note was found in PF05.

## 9. Constraints and interpretations

- Redline form. TW-DRAIN-10 is the operator's redline contract. Its fenced literal payloads take precedence over PF03 §8's default "no code fences around paste text" (PF03 §8: "When the operator supplies a redline format, follow it exactly").
- Every operation is `REPLACE` with an exact OLD block that occurs once in the whole original. Two of them insert new text by widening: RL-02 replaces the "Success body" bullet with the new gate sub-bullet, the revised bullet and three new bullets; RL-13 replaces the v2.5.4 Change Log line with itself plus the v2.5.5 line. This avoids an insertion gap that touches a replaced span.
- PF10 citation rule. No redline cites HDE Build Notes by addendum, section, heading, version or line; it is named by title only, as PF05 §0.2 and PF03 §3 require.
- Repository claims. All new repository claims use one snapshot, `e2b7427` (PF03 §4 step 5). Existing dated claims keep their own pins.
- RL-14 is a consistency change, made on the Product Owner's direction (§1A). It keeps the bullet a dated record and adds no new repository claim at the pin.
- RL-01 is a consistency change. The ledger routed C-02 to the §7.1.10 scope sentence only, but D-2's decision ("No non-v2 base reaches bodygraphs by fallback") also governs PF05 §4.6's contrary permission, which is in the selected unit's scope and in this target. Leaving it would keep PF05 contradicting both D-2 and its own §7.1.10.
- RL-02's implementation-state bullet and RL-07's gap paragraph are qualifications, not new requirements. They keep the new Required-Now rules from reading as delivered (PF05 §0.3; PF03 §3 "Claim-state separation").
- Anchors to other documents. RL-02 cites HDE-Governance §4.1.4, §8.3.2 and §8.3.4 and Glow-Infrastructure §2.2. Each anchor was confirmed in the owning document (§3), and PF05 already cites HDE-Governance by section elsewhere.

## 10. Producer validation

Method. A scratch script, kept outside the repository, built every OLD and NEW literal. It checked that each OLD block occurs exactly once in the original, by character count over the whole file; that every quoted heading line occurs exactly once and precedes its span in order; that no two spans overlap or touch; and that no NEW literal adds an ellipsis. It then applied all fourteen operations in one pass to the unchanged original, by original position. A second, independent script parsed only the saved redlines file. It re-extracted each payload from its four-backtick fences, repeated the count, overlap and one-pass checks, and compared the result with the first script's.

| ID | Operation | Original line(s) | Expected / observed OLD count | Character span in the original | Conflicts |
| :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | REPLACE | 956 | 1 / 1 | [85007, 85104) | none |
| RL-02 | REPLACE | 2493 | 1 / 1 | [189764, 190200) | none |
| RL-03 | REPLACE | 2509 | 1 / 1 | [191897, 191978) | none |
| RL-04 | REPLACE | 2520 | 1 / 1 | [193270, 193326) | none |
| RL-05 | REPLACE | 3476 | 1 / 1 | [256843, 256973) | none |
| RL-06 | REPLACE | 3507 | 1 / 1 | [259896, 259956) | none |
| RL-07 | REPLACE | 3515–3521 | 1 / 1 | [260978, 261835) | none |
| RL-08 | REPLACE | 3533 | 1 / 1 | [262345, 262535) | none |
| RL-09 | REPLACE | 3577 | 1 / 1 | [265281, 265385) | none |
| RL-10 | REPLACE | 3584 | 1 / 1 | [265727, 265850) | none |
| RL-11 | REPLACE | 3588 | 1 / 1 | [266196, 266426) | none |
| RL-12 | REPLACE | 3604 | 1 / 1 | [267979, 268015) | none |
| RL-13 | REPLACE | 4148 | 1 / 1 | [309120, 309474) | none |
| RL-14 | REPLACE | 119 | 1 / 1 | [15975, 16690) | none |

Results:

- 14 of 14 operations resolve to exactly one occurrence. No `FIND_AND_REPLACE` is used, so the RL-045 rule has nothing to apply to.
- The spans are strictly ordered with gaps between them: no overlap, no shared boundary, no insertion at a replaced boundary, and no operation reads another's output.
- After one-pass application, each NEW literal occurs exactly once. Each OLD literal is absent, except in RL-13, whose NEW literal keeps the v2.5.4 line by design.
- The `drain-r2` simulated result is 332,470 bytes with SHA-256 `1587ea2110a62813f82e43c715c45c5dc097aecc88aabb9c2f71914667e2bad6`. The independent check of the saved file reproduced that hash exactly. Against the `drain-r1` simulation (`a3c9a08b…48ee`), it differs only at line 119 and in the v2.5.5 Change Log line. The simulation was a scratch file only; TW-APPLY-10 produces the final PF and its document-control fields, so the final file will differ from the simulation in the header.
- The diff between the original and the simulation was read in full. It touches only the fourteen spans above.

Corrections to this preparer's own package. Each was followed by a full rebuild and revalidation of the whole batch:

1. Before the first save, the residual-risk sentence in RL-02 was reworded for clarity.
2. After the first save, a check of every HDE Build Notes line citation against the numbered source found that the "Source basis" fields of eleven redlines, and the matching rows of this log, cited lines a few positions off (for example D-1's three-path scope as l.229–235 instead of l.229–232). The citations were corrected in the redlines file and here. No OLD or NEW literal changed: the corrected redlines file re-validated to the same simulated SHA-256 `a3c9a08b7f0c685bfd5ba6a59441f63b0a961e475587e86efcf9483a34a248ee`. The first saved redlines file (SHA-256 `737318bdd3d9fce7641a08a83e872a2d84c6c8c1c5c6ee02f5b73f926f2fddc5`) was overwritten in the working tree before any commit; it was never committed or offered for application.
3. `drain-r2`, on the Product Owner's direction (§1A): RL-14 added and RL-13 extended. Within the `drain-r2` build, RL-13's first wording ("instead of a legacy fallback") was replaced before saving, so that the entry doesn't use the term. The `drain-r1` file (SHA-256 `c1804a5954a288573ded0e427253d633aa0248fd96fb5d44c335a1e19aa1faab`) is overwritten at the same path; it remains in commit `0d22343`.

## 11. Save state

| File | Path | Bytes | SHA-256 | Verified |
| :---- | :---- | :---- | :---- | :---- |
| Redlines (`drain-r2`) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF05/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.redlines.gtwpe-20261101-pf10-v14-0-5.md` | 25,034 (392 lines) | `cc0984889e9c9e3e40f23f6a86c5a05d32d78c5b21372a14fae1399378bb043a` | Byte-identical to the validated build; independent re-validation passed; read back in full; ends with `END OF REDLINES` |
| Proof log (`drain-r2`) | This file | — | Not self-hashed | Read back in full after writing, and again after this receipt was added |

Completion receipt (`drain-r2`, 2026-11-02, UTC). Both files were read back from disk in this session. The redlines file matched the validated build byte for byte, ended with `END OF REDLINES`, and passed the independent re-validation: 14 of 14 operations, count 1 each, non-overlapping, one-pass result SHA-256 `1587ea2110a62813f82e43c715c45c5dc097aecc88aabb9c2f71914667e2bad6`. Its diff against the `drain-r1` file is limited to the run identity, the simulated-result row, RL-13's new entry line and the added RL-14. This log was read back in full; its identities agree with the redlines file: target, source, ledger rows, run identity `drain-r2`, preparer and outcome.

Save state: `COMPLETE_PACKAGE`. Preparation outcome: `READY`.

## 12. Next step

On `READY` / `COMPLETE_PACKAGE`, the remediation handoff authorizes TW-APPLY-10 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) in this session, fetched live, as run `apply-r2`, with:

- original: `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` at `e2b7427`, SHA-256 `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028`;
- redlines and this proof log, at the paths in §11;
- ledger rows T-02, C-01, C-02, C-03, support C-06;
- source: HDE Build Notes v14.0.5, addendum 2.1 D-1 to D-3 and context, at the boundaries in §3;
- branch `claude/gtwpe-triage-authoring-j94ewf` and draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826);
- final output: the revised PF under the name TW-APPLY-10 derives (expected `PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.5.md`) with its `.proof-log` file, in this directory;
- diagnostic, if needed: `PF05-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`, in this directory.

A returned diagnostic comes back to this preparer, which issues a corrected package under a new run identity (`drain-r3`) and revalidates the whole batch.

This package changes no PF canon, Specification or AGENTS.md. It establishes no implementation, QA verdict, acceptance, deployment or closure.
