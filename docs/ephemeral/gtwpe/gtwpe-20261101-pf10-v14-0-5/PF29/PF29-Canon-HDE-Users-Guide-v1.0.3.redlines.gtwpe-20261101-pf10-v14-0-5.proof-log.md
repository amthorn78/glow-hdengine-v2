# Proof log — PF29-Canon-HDE-Users-Guide v1.0.3 redlines — gtwpe-20261101-pf10-v14-0-5 (T-08)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.md` (ten `REPLACE` redlines, RL-01 to RL-10, ending `END OF REDLINES`) |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-08/drain-r1`, the same in the redlines file |
| Producing prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1. Fetched live from Notion page `3f44590a05eb8172a314fe6b958bb9ff` at the start of this step on 2026-11-02; the page records "Prompt Version: 100926.1" and was last edited 2026-10-09T11:05:22Z. |
| Originating preparer | The Claude Code document session Nathan started for T-08, https://claude.ai/code/session_01Q789u3KLSaV6qHFgm3m8t4. No subagent, reviewer or other session took part. |
| Preparation date | 2026-11-02 |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE`: the redlines file and this proof log, both read back in full (§9) |
| Correction route | An Apply diagnostic returns to this preparer in this same session, as Nathan's handoff authorizes. A corrected package would carry a new run identity (`drain-r2`). |

## 2. Sources and inputs

| Role | Identity | Read |
| :---- | :---- | :---- |
| Target (original) | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.3.md`, in-document title PF29-Canon-HDE-Users-Guide, v1.0.3, Status Canon, effective 2026-10-26. Git blob `6730222d2f352221ddbe140a08c260380bbf5abc`; SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`; 76,613 bytes; 1,079 lines, LF-terminated. Read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; the same blob at current `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. | Complete: lines 1–1079, in three contiguous windows (1–300, 300–659, 659–1079). |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, PF10-HDE-Build-Notes v14.0.5, effective 2026.11.01, Status Living. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines. Same blob at `e2b7427` and `84d6d1c`. | Selected units complete: addendum 2.1 lines 205–516, which contain D-1 (225–276), D-2 (277–344), D-3 (345–396) and the context 205–224 and 491–516. Lines 1–12 read for identity. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, v1.8.8, git blob `504712df548a02f3aa4e7b8c37027385e46a3878`, SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`, 633 lines | Complete |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` (22,735 bytes). Task T-08; rows C-01, C-02, C-03; supporting C-06; hold H-05. Planning and routing only, not a change source or Last Update Gate. | Complete |
| Repository code (availability evidence) | Bounded read-only inspection at `e2b7427ff418ca8f08f05587c4a541308a76da56`, under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`), with `git show` and `git grep` only. `git diff e2b7427 84d6d1c` changes only two `docs/ephemeral/` files, so the inspected code is byte-identical at current `main`. | §4 |
| Supporting reading | None beyond the units above. PF05-Canon-HDE-CLI-API-Vendor-Ref and PF04-Canon-HDE-Governance were not read; the new text routes to them by title for ownership only (§6). | — |

Source-text search outside the selected units: PF10 lines 1–204 and 517–1976 were searched (not read) for "Users Guide", "PF29", "allow-prod-vendor", "compat/v1", "ROUTE\_UNSUPPORTED", "legacy fallback", "terminal v1", "showcompat", "bg:resolve", "PROVIDER\_PROD", "item 9" and "S19". No later addendum amends D-1 to D-3 or adds a PF29 rule for these surfaces. Addendum 2.11 (l.1376) records item 9 as still the Product Owner's.

Canon relied on, by title and section:

- PF29-Canon-HDE-Users-Guide §0.2 "Scope" (the currency rule: a surface is checked against current repository reality before it is documented as available, and planned or intended features are clearly marked), §0.4 "Single-home routing", §0.5 "Feature availability legend" (`\[Current gap\]`), §1.1 (its provenance sentence).
- PF03-Reference-Technical-Writing-Best-Practices §3 (truth and source fidelity, claim-state separation, structure and language, ellipsis rule), §4 (authoring method, one identified snapshot), §5, §6 (source precedence), §7, §8 (redlines and placement; protected headings), §12 "Runnable guides and usage documentation", §14.
- PF10-HDE-Build-Notes v14.0.5 addendum 2.1, in full for D-1 to D-3 and their context.
- The repository's agent rules in `AGENTS.md`: canon-first search, PF canon read-only, PF documents other than PF10 never cite PF10 by section, closed rails.

## 3. Turn preflight

1. Task: T-08, preparation under TW-DRAIN-10, to be followed in this session by TW-APPLY-10 only after a `READY` / `COMPLETE_PACKAGE` result. Nathan's handoff authorizes both steps, and a return from an Apply diagnostic.
2. Identities and access: each was verified directly (§2). The target and source are unchanged between the ledger baseline `e2b7427` and current `main`, so no ledger row is stale.
3. Selected scope: 2.1 D-1, D-2 and D-3, with the context lines 205–224 and 491–516 (C-06). Each was read completely. The handoff destinations are PF29 §13.3 and §16 with the override troubleshooting row (C-01); the §11.3, §13.3 and §16 fallback sentences (C-02); and the §16 compat line and the "HTTP 404 from POST /api/compat/v1 in prod" row (C-03).
4. Output size: ten single-block replacements, about 22 KB of redlines. The revised body grows from 76,613 to 81,919 bytes.
5. Branch: Nathan's handoff directs the shared branch `claude/gtwpe-triage-authoring-j94ewf` while draft amthorn78/glow-hdengine-v2#826 is open. On 2026-11-02 the PR was open and a draft, with head `142feb35144d8795f927e0c78b665ace52279064`. This session's own default branch (`claude/practical-cerf-x0hi33`) is not used, and nothing is pushed there.
6. Output collision: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/` did not exist on the branch at `142feb3`, so no existing file was overwritten.

## 4. The availability decision

The handoff asks this to be decided first. PF29 §0.2 requires every documented surface to be checked against current repository reality, and it permits intended behavior only when that behavior is clearly marked as not yet implemented. PF10 2.1 makes D-1 to D-3 canon from publication (l.211). Its implementing change, Candidate CRD Items List item 9, is open (l.506), and it establishes no code change (l.498).

Finding: none of the three decisions is delivered in the checked-in code at `e2b7427`. Six runtime-code facts that PF10 2.1 cites from `adbacfa2` for D-1 to D-3 still hold at the same lines: `engine/cli/main.py` line 799, `engine/bodygraph/resolver.py` line 704, `engine/bodygraph/vendor_client.py` lines 102–109, `engine/http/compat_handler.py` line 112, `adapter/env_guard.py` lines 31–51 and `adapter/http_reader.py` lines 901–907. For PF29 availability, 2.1's "fresh question" clause (l.502) is therefore not triggered. Its test, workflow and evidence-tool line citations were not re-read; they bear on the implementing change, not on what PF29 documents as available.

| Decision | Canon requires | Checked-in behavior at `e2b7427` (path, blob, lines) |
| :---- | :---- | :---- |
| D-1 | The production override gate also covers `showcompat --source vendor` and vendor-selecting conjunction. | `engine/cli/main.py` (blob `77b886026c106d3ccf430bf01481212567c48c36`): lines 52–59 define the usage message "--allow-prod-vendor is accepted only by bg:resolve --source vendor". Lines 231–256 reject the flag before argparse for any command other than `bg:resolve`, and lines 293–296 return exit 64. Only the `bg:resolve` parser declares the flag (lines 178–183). Showcompat vendor parties resolve with `source_policy="vendor"` (lines 748–755), and conjunction uses `"local" if source in ("db", "auto") else "vendor"` (line 799). `engine/bodygraph/resolver.py` (blob `5f238b9a1a1278efe85dc5a24354e4d1e736b7a2`): `classify_vendor_environment` (line 73) has one caller, `_resolve_vendor` (line 270), which is the `bg:resolve` path. Compat acquisition, `resolve_compat_chart` (line 1083) → `_acquire_dry_run` (lines 915–1032, called at line 1072), checks the rails and the route classification and then fetches. It does not classify the environment, apply the override or write an audit event. `git grep 'classify_vendor_environment\|PROVIDER_PROD_OVERRIDE' e2b7427 -- engine/ adapter/ scripts/` matches only `resolver.py`. |
| D-2 | Only a terminal, case-sensitive `v2` or `v1` segment selects a route; every other base fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or I/O. | `engine/bodygraph/vendor_client.py` (blob `ac98075772da2c446abed8d3bfb422143c82c0af`): `_configured_base_version` (lines 102–109) lower-cases every path segment and returns `v2` if any segment is `v2`, else `v1`, else `unversioned`. `classify_bg_resolve_route_policy` (lines 124–153) maps every non-`v2` result to `bodygraphs`, with `"classification": "explicit_legacy_fallback"` (line 150) and `"supported": True` (line 151). `resolver.py` line 704 (`_classify_env_route_policy`) feeds both `bg:resolve` (line 409) and compat acquisition (line 940); compat acquisition then calls the legacy `ingest_vendor_bodygraph` (line 1008). `git grep PROVIDER_ROUTE_UNSUPPORTED e2b7427 -- engine/ adapter/` returns nothing. A second, whole-repository search finds the token only in governed evidence, QA records, PF canon and the evidence generator `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py` (line 129), not in runtime code. |
| D-3 | Outside production-like posture, the compat namespace is served only when `APP_ENV` is exactly `dev`, `test` or `local`; any other value refuses `ERR_WRITER_FORBIDDEN` 403. | `engine/http/compat_handler.py` (blob `df9a6e033e2940eaff894e41b54ec453be5ce936`): `_compat_writer_transport_guard` (lines 108–120) returns 404 only when `_compute_env_mode(os.environ) == "prod"` (lines 112–113), and otherwise falls through. `adapter/env_guard.py` (blob `ba0cb043c469927e2ef18a6f7ffd5d26e11e2f72`): `_compute_env_mode` (lines 31–51) strips and lower-cases, passes `staging` and unknown values through, and returns `dev` when both variables are unset (line 51). `adapter/http_reader.py` (blob `ffba6c4e179401a3ac11bcaa4bdd630a71310bed`): the exact-match `_dev_admin_gate` exists (lines 901–907), but it is not applied to the compat blueprint, which line 1260 registers. `adapter/factory.py` and `adapter/wsgi.py` register the same blueprint with no other gate. |

Decision: drain, with accurate availability qualifiers. Blocking was rejected. A block would leave PF29 v1.0.3's statements that D-2 explicitly supersedes ("For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved" and its restatements) standing as current canon. PF29's own legend already has a truthful label for this posture: `\[Current gap\]`, "the workflow or claim is not truthfully implemented end-to-end in the current repository". Each redline therefore does three things:

- it states the decided rule as canon, with no invented future date, plan or owner;
- it states the checked-in behavior and marks the difference `\[Current gap\]` at the point of use (PF03 §12 "Runnable guides");
- it keeps PF29's existing description of what the checked-in code does, where that description is still true.

PF03 §3 forbids rewriting an unmet requirement as planned or deferred, so the label is `\[Current gap\]`, not `\[Planned, not implemented\]`. Static inspection proves checked-in bytes only. No recipe, test or vendor call was run, and no runtime or deployed behavior is claimed.

## 5. Change and disposition ledger

Every item in the selected units is accounted for below. RL numbers refer to the redlines file.

### D-1 (C-01) — production override scope

| Item (PF10 lines) | Disposition |
| :---- | :---- |
| The three paths, including vendor-selecting conjunction (229–232) | Drained: RL-05 (§13.3) and RL-08 (§16), each with the gap |
| Same classification, matrix and initiator rule (233) | Drained: RL-05 |
| Flag accepted by the three paths only; syntax unchanged (234) | Drained: RL-05 and RL-08. The flag syntax is not restated; PF29 already routes it to PF05-Canon-HDE-CLI-API-Vendor-Ref. |
| Order: usage error, exit 64, when no vendor acquisition is selected (235) | Drained: RL-05 |
| One authorization: one acquisition per party; nothing the override excludes (236–238) | Drained: RL-05 and RL-08 |
| Audit event before I/O (240) | Drained: RL-05 ("pre-I/O audit event") |
| The audit event's command-field values (241) | Not drained. This is a field of the audit contract, which PF05-Canon-HDE-CLI-API-Vendor-Ref owns (T-02). PF29 §16 already routes "audit contract" there. |
| Error carrier: same codes, exit 1, zero outbound attempts (242–244) | Drained: RL-05 and RL-10 |
| Basis (246–251) | Explanatory; not drained |
| Canon superseded in PF05 §7.1.11a, d, e and f, and the implementation-state limit (253–260) | T-02, not this target |
| Drainage target "HDE Users Guide §13.3, and §16 with its troubleshooting row for the three PROVIDER\_PROD\_OVERRIDE\_\* and PROVIDER\_AUDIT\_UNAVAILABLE codes" (265) | RL-05, RL-08 and RL-10. The troubleshooting row is in PF29 §17 "Troubleshooting" (l.1006), not §16. It is resolved by its unique literal text. |
| AGENTS.md "Showcompat Live QA posture" (266) | Held: H-05 (§7) |
| Consequences for tests, evidence and frozen captures (268–273) | For the implementing change. The operator-facing consequence, that an open-rails showcompat vendor run with an unset or unrecognized environment refuses with `PROVIDER_CONFIG_INVALID`, is drained in RL-05. |

### D-2 (C-02) — vendor route selection

| Item (PF10 lines) | Disposition |
| :---- | :---- |
| Scope: `bg:resolve` and compat chart acquisition (281–283) | Drained: RL-03 |
| Selection: terminal `v2` or `v1`; everything else fails with `PROVIDER_ROUTE_UNSUPPORTED` before credential projection or I/O (284–286) | Drained: RL-03, with the gap. Consistent statements in RL-02 (§1.1), RL-04 (§13.3) and RL-07 (§16). |
| Configured-base boundary: absolute HTTPS, host, no userinfo, query or fragment (287) | Routed to PF05-Canon-HDE-CLI-API-Vendor-Ref in RL-03 and not restated (PF03 §5). PF29's existing HTTPS row (§17, `PROVIDER_CONFIG_MISSING`) is unchanged. |
| v1 is retained legacy selection, not fallback (288) | Drained: RL-03 and RL-07 |
| Retirement of v1 needs a separate versioned decision (288, 343) | Not drained. It is left undecided, and its home is PF05-Canon-HDE-CLI-API-Vendor-Ref; PF29 states no retirement. |
| No fallback (289) | Drained: RL-03 |
| How the two canon rules fit, including the HDE Mechanics Guide §1.1 prohibitions (290–297) | Already represented. PF29 §12.2 (l.771) already says "Use version-neutral runtime resource paths. Do not hardcode /v1 or /v2 as active runtime request-construction inputs. The configured HD\_API\_BASE\_URL owns any vendor API version prefix." The rule's homes are PF05 and PF14 (T-02, T-05). |
| Classification label `explicit_legacy_fallback` kept as a wire value (298) | Drained: RL-03 |
| Basis (300–308) | Explanatory; not drained |
| Superseded PF29 text: §11.3, §13.3 and §16 (314) | RL-03 (§11.3), RL-04 and RL-05 (§13.3), RL-07 (§16) |
| Other superseded or added canon: PF14 §1.1, PF05 §7.1.10, PF27 (312–316) | T-05, T-02 and T-07; not this target |
| PF05 §7.2.0 gap (322) | H-09; not this target |
| AGENTS.md "EPIC036 docs posture" and EPIC038 lines (324) | Held: H-05 (§7) |
| Consequences for tests and frozen captures (326–339) | For the implementing change and the test owners; not operator guidance |

### D-3 (C-03) — compat route gating

| Item (PF10 lines) | Disposition |
| :---- | :---- |
| Classification: the compat namespace is dev/admin-only (349) | Drained: RL-06 |
| Production-like posture keeps 404 (351) | Already represented: PF29 §16 l.963, §7.2 l.417, §13.2 l.822. Retained unchanged in RL-06. |
| Any other request served only with `APP_ENV` exactly `dev`, `test` or `local`; else `ERR_WRITER_FORBIDDEN` 403; `ENGINE_ENV` never admits (352–354) | Drained: RL-06 and RL-09, with the gap. The header bytes (no-store, no ETag, no HEAD body) are PF05-owned and not restated. |
| Existing method, probe and POST rules (355) | Already represented: PF29 §7.2 l.411–417 |
| No credential while dev/admin-only; "authenticated" withdrawn (357–358) | Drained: RL-06 ("No credential is required"). PF29 v1.0.3 has no "authenticated" claim about the compat route to withdraw: its only "authenticat" matches, l.842, l.985 and l.1006, concern the override's human initiator. |
| Wider exposure needs a later decision with a credential and logging rules (359–361) | Drained in routed form in RL-06 ("needs a later decision", owned by PF04-Canon-HDE-Governance and PF05-Canon-HDE-CLI-API-Vendor-Ref). The credential and logging rules are not restated. |
| Residual risk, accepted and recorded (362–364) | Not drained. This is a governance record, not operator procedure. The operator-facing control, the loopback-only start helper, is already in PF29 §4.1 l.245. |
| Basis (366–373) | Explanatory; not drained |
| Canon superseded or added in PF05 §5.5 and PF04 §4.1.4 (377–380) | T-02 and T-01; not this target |
| Drainage target PF29 §16 line and troubleshooting row (386) | RL-06 (§16 l.963) and RL-09. The row is in PF29 §17 (l.998); it is resolved by its unique literal text. |
| Consequences for tests and evidence (388–393) | For the implementing change; not operator guidance |

### C-06 — context

| Item (PF10 lines) | Disposition |
| :---- | :---- |
| Canon from publication; governs over conflicting text until it is drained (211) | The basis for draining now |
| Independence; item 9 is the implementing change (223) | The basis for the `\[Current gap\]` qualifiers |
| Nonclaims: no code, test, evidence or closure change (497–500) | Respected. No redline claims delivery, QA, acceptance or closure. |
| Facts read at `adbacfa2` (502) | The six runtime-code citations for D-1 to D-3 were re-verified at `e2b7427` (§4); the test and workflow citations were not re-read |
| Item 9 open; its CRD identity and Specification are the Product Owner's (506) | H-10; not drained |
| Drainage unperformed; the AGENTS.md lines need the Product Owner's instruction (507) | This package drains the PF29 share. AGENTS.md is H-05. |
| Brief correction (508) | Test-naming history; not PF29 |

## 6. Constraints, interpretations and deviations

1. Section numbering. PF10 2.1 cites "HDE Users Guide §16" for the two troubleshooting rows. In PF29 v1.0.3 those rows are in §17 "Troubleshooting" (l.998, l.1006). Each is resolved by its unique literal row text.
2. Edits outside the handoff's named sections. Nathan should review these two.
   - RL-02 changes the §1.1 `hdctl bg:resolve` row. That row restates the superseded "Non-v2 configured bases preserve explicit legacy BodyGraph fallback". Leaving it would make the drained PF29 contradict itself and canon.
   - RL-01 adds one provenance sentence to §1.1. PF29 records there which repository snapshot each availability statement was inspected at, and PF03 §4 requires an identified snapshot for repository-dependent claims.
   Both are classified CONSISTENCY within C-01 to C-03. They introduce no new requirement.
3. Heading kept. The §11.3 heading "Non-v2 legacy fallback \[Implemented\] \[Operator-authorized only\]" is unchanged:
   - PF03 §3 and §8 protect section titles unless a structural change is explicitly authorized;
   - the handoff scopes D-2 to the "fallback sentences".
   The body now states the terminal-v1 rule and the gap. Renaming the heading, for example to the terminal-v1 legacy route, needs Nathan's explicit authorization.
4. Sections not drafted. These describe checked-in behavior that is still accurate, and neither D-1 nor D-3 names them:
   - §7.5 and §9.2: the vendor recipes set no `APP_ENV`, which canon will refuse with `PROVIDER_CONFIG_INVALID` once D-1 is delivered;
   - §17 `PROVIDER_CONFIG_INVALID` row (l.1005): scoped to `bg:resolve`;
   - §1.1 row l.100, §1.2 row l.122, §7.2 l.417 and §13.2 l.822: the compat route's 404 production posture, which stays accurate and consistent with canon.
   RL-05 and RL-06 state the canon rule where operators read production and limit posture. Revisiting these sections when item 9 is delivered is a candidate follow-up for Nathan; this package does not route it.
5. Ownership routing. PF29 §0.4 assigns CLI, HTTP and vendor bytes to PF05-Canon-HDE-CLI-API-Vendor-Ref, and rails and operational policy to PF04-Canon-HDE-Governance. PF10 2.1 names PF05 §5.5, §7.1.10 and §7.1.11 and PF04 §4.1.4 as the homes of these rules. The new text routes to those owners by in-document title. It cites no PF10 addendum or section.
6. Style. New code-like literals are in backticks. Unchanged text keeps its original escaping, and the availability label uses PF29's escaped `\[Current gap\]` form. No ellipsis was introduced (validated), and no placeholder, TODO or draft-status marker exists in the target or the payloads.
7. Header. No redline touches §0.1. TW-APPLY-10 derives the document-control fields. The baseline header schema and the source (PF10-HDE-Build-Notes v14.0.5, file `PF10-HDE-Build-Notes-v14.0.5.md`) are stated in the redlines file. PF29 has no change-log or Doc-Delta section, so no history-entry redline is needed.

## 7. Held and outside dependencies

| ID | Item | Waits for |
| :---- | :---- | :---- |
| H-05 | AGENTS.md edits under D-1 ("Showcompat Live QA posture": a production-like Live QA run needs the flag; PF10 l.266) and D-2 ("EPIC036 docs posture" and the EPIC038 posture lines that say non-v2 bases keep the fallback; l.324). Not a PF target. | The Product Owner's explicit instruction to edit AGENTS.md (PF10 l.507; ledger §5 H-05). Not drafted. |

No other dependency blocks this package. Item 9 (H-10) explains why the qualifiers are needed; it does not block the drain.

## 8. Producer validation

The validation ran against the unchanged original, both from the in-memory specification and from an independent parse of the saved redlines file. Both runs agree. Each check below is a script run under closed rails with `python3 -I`.

| Redline | Section | Original lines | Byte span | Expected | Observed | OLD SHA-256 | NEW SHA-256 |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | §1.1 | 81–81 | 4703–5484 | 1 | 1 | `f7d1b43b0a92152161bc7655658f2fade7a31aa0334e61c907feb162d3f0577a` | `3777a12d18bf8289d329cb2d43fd45bd45446c22e6f1c08cb09e1377fae3a798` |
| RL-02 | §1.1 | 92–92 | 6366–6937 | 1 | 1 | `e6c74c061f99e99fefd4c665b5b44865679e186cb8644feaca1db33cd417749b` | `08aa5f21f890730387085b4600ac4be37a3868a03048b44ddfc4c10287b317f4` |
| RL-03 | §11.3 | 712–714 | 45156–45552 | 1 | 1 | `562af25a1edc049a30cd3cc7496ac8057f4d956058e5750d153d572aa4c3810e` | `ec74d834aab848319e61cb9f145c280ec76405322ebb96bcb13ce275dcc9f9ac` |
| RL-04 | §13.3 | 838–838 | 51927–52296 | 1 | 1 | `3471cf41575a62d6058f2e155c1a751a89e92f6b17bb5cc0fc741d2a007aec4c` | `1571d7733e81754901426c51a0b2bca517fdd329859fe258966b23ec7a8f5a8b` |
| RL-05 | §13.3 | 848–848 | 54032–54153 | 1 | 1 | `7679268e2411da0ba69abf26fd0f53ad9350fab58fd4060d4f9daad168e9ee2c` | `9586e5aba82fe5090b75f2eaf86ccfd4445ba408cd3d21daa8b19a0211065117` |
| RL-06 | §16 | 963–963 | 62304–62506 | 1 | 1 | `ae508d574029fa5ab2a41a18b2d298f3967f692440f4a60146beec75203543e4` | `8ba7ed3293917dee1e25c6c0df5cc0a32d87a80a8886874b73ae2ace2d7cd45d` |
| RL-07 | §16 | 969–969 | 62691–62916 | 1 | 1 | `f39d3d56b1eea1f06c4371b498699337b6b86bff9385f8c9d9c9ec11ed1e0cd0` | `9d8025d8ea2efe77c695552775478e7933fe5e8a588a1fceee275d260c9c3aea` |
| RL-08 | §16 | 985–985 | 65513–66146 | 1 | 1 | `101362406db21e77b55803095ea7ab5cc40217910907232685a2ec1e919f5080` | `d3f92993fbab037e5f8fb573900bdeb48133fdd5b7424157f06a860994e8d920` |
| RL-09 | §17 | 998–998 | 67682–67849 | 1 | 1 | `cf1ff9c0fe98003092ff44235d25d13273aad19621fe88e0a023142ef598a537` | `e127634725fdcf40ee6d4dce9fd529f619ce063233fdd8060be266d0634c0c55` |
| RL-10 | §17 | 1006–1006 | 69328–69846 | 1 | 1 | `15a9aa873e6dfe546be9837b0c5d8d72aaf765d8e68de6fb2068c20e335f6ef3` | `4bd7b5d64ca19dcb190289dee18c589b58358a674706011eb5bb2c2c32914998` |

Checks run and their results:

- Operation dialect: all ten are `REPLACE`, with expected and observed occurrence 1. No `FIND_AND_REPLACE`, `INSERT`, `DELETE` or legacy boundary-pair locator is used, so the RL-045 rule is not engaged.
- Line bounds: every OLD block starts at a line start and ends before a line feed. The resolved line ranges match the stated locations.
- Overlap: sorted byte spans are strictly disjoint, and no two spans touch. No insertion gap is shared.
- Payloads: every NEW block is non-empty and differs from its OLD block. No payload line begins with a backtick fence. No payload contains an ASCII three-period ellipsis or the Unicode ellipsis.
- One-pass simulation on original offsets, applied end to start:
  - each NEW block occurs exactly once in the result;
  - the superseded literals "Non-v2 configured bases preserve explicit legacy BodyGraph fallback", "explicit legacy BodyGraph fallback is preserved", "With a non-v2 configured base, explicit legacy fallback may proceed", "For non-v2 legacy fallback" and "any supported non-v2 legacy fallback" occur zero times;
  - the simulated body before any header change has SHA-256 `c5fefd1f89330a5ed5c9a160cb6d2bcc11b975e161c25a33d7678be12195cfd8`, 81,919 bytes, 1,085 lines.
- Heading paths: each heading line in a section path occurs exactly once in the original.
- Correction recorded: before the package was saved, RL-03's gap paragraph gained "exactly `v2`" guidance, because a nonterminal `v2` marker is part of the same gap. The whole batch was revalidated afterwards. No other correction was made.

These checks establish the editorial and mechanical condition of the package only. They are not CI, QA or governed evidence.

## 9. Save verification

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.md` | 22,037 | `9a5b8b85e143e64e9e25d4f4c008620bcde40463008cd1175d1e35be6b91d10f` | Complete, lines 1–275, ending `END OF REDLINES`, then re-parsed and revalidated |
| This proof log | — | — | Complete, after writing. A self-referential hash is not recorded. |

## 10. Next step

TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) runs next in this session, as Nathan's handoff authorizes. Its inputs:

- the unchanged original at `e2b7427`;
- the redlines file and this proof log;
- ledger rows C-01, C-02 and C-03 (supporting C-06);
- branch `claude/gtwpe-triage-authoring-j94ewf`;
- the expected final output `PF29-Canon-HDE-Users-Guide-v1.0.4.md`, with its `.proof-log` file beside it, or the diagnostic `PF29-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`.

The fetched Apply prompt's derivation governs the final name.
