# T-PF07 — exact redlines from PF07 v2.3.3

Run: `gtwpe-20261026-pf10-v13-8-8/T-PF07`. Preparation revision: `P1`.
Originating preparer: TW-DRAIN-10 in the Nathan-started T-PF07 document session, Claude Code cloud session https://claude.ai/code/session_01Tgfx3BStUkwc3FCxt1iDDU.
Target: `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md` (`PF07-Canon-Glow-Infrastructure` v2.3.3) at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`, byte-identical at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; Git blob `7d2734ce2b75a7277a632b881bfb931ff88bf7af`; 98,175 bytes; 1,431 lines; no trailing newline; raw UTF-8 SHA-256 `573ceecfb93557cb93db04179a535a0d3c1209a99f5128e0408384f22b4110cc`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, unchanged on `main`), task `T-PF07`, rows A19, A09 with X05, A20, A35.
Sources: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223; addenda 2.9 (1003–1101), 2.19 (2082–2321), 2.20 (2322–2395), 2.35 (3725–3955). Supporting cross-reference X05: `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` §17 (701–739), blob `6baead456619`.
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Preparation outcome: `READY` after whole-batch producer validation. Save completeness is recorded in the separate proof log.

These are eight independent original-bound operations: seven `REPLACE` and one `FIND_AND_REPLACE`. Header control fields are reserved for TW-APPLY-10. Payloads are literal: the single LF immediately before a closing fence is presentation only and is not part of the payload. Every other payload newline and every trailing space is exact. Fences are four backticks, longer than any backtick run in a payload. Each `REPLACE` OLD block consists of complete original lines and occurs exactly once in the whole original. The original line numbers are context only, not locators.

## RL-001

Redline number: RL-001
Findings or source items: A19 (PF10 v13.8.8 addendum 2.19, P-18; Unresolved obligations)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 3\) Provider inventory (names-only)` > `## **3.1 Railway**`
Original-bound location: the end of the **Base URLs (names-only)** list (`  * **Glow Backend:** **TBD**`) through the section's closing italic routing line
Original lines (context only): 582–584
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.19 P-18 records the Product Owner direction of 2026-10-21 that the HD Engine candidate reaches the service when its commit lands on `main` of `amthorn78/glow-hdengine-v2`, a PO-provided deployed environment fact that PF07 §2.4 does not allow to be downgraded to OPEN/TBD, and names §3.1 as a doc-delta target. Adds a names-only deploy-source entry to the Railway provider inventory; the closing routing line is reproduced unchanged.

OLD

````text
  * **Glow Backend:** **TBD**

*Names-only; no policy, runbooks, or tokens here. Transport/A7 policy is routed by title to the relevant product’s governance and contract documents.*
````

NEW

````text
  * **Glow Backend:** **TBD**


* **Deploy source (names-only):**  
    
  * **HD Engine:** commits landing on `main` of `amthorn78/glow-hdengine-v2` (Product Owner-provided deployed environment fact)

*Names-only; no policy, runbooks, or tokens here. Transport/A7 policy is routed by title to the relevant product’s governance and contract documents.*
````

## RL-002

Redline number: RL-002
Findings or source items: A19 (PF10 v13.8.8 addendum 2.19, P-18, P-9, Unresolved obligations)
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **4\) Component maps**` > `## **4.1 HD Engine**`
Original-bound location: the **Source** and **Build artifact** bullets
Original lines (context only): 632–633
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.19 P-18 names §4.1 as the second doc-delta target for the deploy source and states that the build and start commands are not discovered or recorded. Inserts a **Deploy source** bullet between the unchanged **Source** and **Build artifact** bullets; Build artifact stays **TBD**.

OLD

````text
* **Source:** repository **amthorn78/glow-hdengine-v2** (repo root; no file paths pinned)  
* **Build artifact:** container image (Railway) — **TBD**  
````

NEW

````text
* **Source:** repository **amthorn78/glow-hdengine-v2** (repo root; no file paths pinned)  
* **Deploy source:** commits landing on `main` of **amthorn78/glow-hdengine-v2** (Product Owner-provided deployed environment fact; the build and start commands are not recorded)  
* **Build artifact:** container image (Railway) — **TBD**  
````

## RL-003

Redline number: RL-003
Findings or source items: A20 (2.20, Facts behind the decision; Unresolved obligations); A35 (2.35, Not candidates); A19 (2.19 P-18; Facts behind the decision)
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **4\) Component maps**` > `## **4.1 HD Engine**`
Original-bound location: the **Start command (inventory)** bullet
Original line (context only): 638
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.20 and 2.35 keep the live Railway start setting unverified as a stated limit, and 2.19 records that the start command is not recorded. PF07 §10 already states that no declaration is asserted to be the current Railway start command. The §4.1 pointer's "canonical Railway command kept verbatim" contradicts that limit; this aligns the pointer with it.

OLD

````text
* **Start command (inventory):** see **§10** (canonical Railway command kept verbatim)  
````

NEW

````text
* **Start command (inventory):** see **§10** (checked-in declarations only; the live Railway start setting is not verified)  
````

## RL-004

Redline number: RL-004
Findings or source items: TW-DRAIN-10 100926.1 marker rule (no ledger row)
Change type: DOC_HYGIENE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 6\) Domains & DNS (names-only)` > `## 6.3 Subdomains by environment & component (names-only)` > `### 6.3.1 Production`
Original-bound location: the **Backend** bullet
Original line (context only): 871
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: The prompt's document-control rule requires removing an unresolved drafting note or instruction to a future writer that canon does not require. "— confirm" is a bare to-do; **TBD** (canon-required notation, PF07 §6.5 and §8) already records that the value is unconfirmed, and the two candidate forms are kept.

OLD

````text
* **Backend:** **TBD** *(Railway app domain **or** a `*.glowme.io` subdomain — confirm)*  
````

NEW

````text
* **Backend:** **TBD** *(Railway app domain **or** a `*.glowme.io` subdomain)*  
````

## RL-005

Redline number: RL-005
Findings or source items: TW-DRAIN-10 100926.1 marker rule (no ledger row)
Change type: DOC_HYGIENE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# 6\) Domains & DNS (names-only)` > `## **6.4 DNS provider & record types (names-only)**`
Original-bound location: the **CNAME** bullet
Original line (context only): 895
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: "confirm exact hostnames as we populate" is a to-do with drafting-status language. The replacement keeps its meaning, that the exact CNAME hostnames are not recorded, in PF07's own notation, as the adjacent TXT bullet does.

OLD

````text
* CNAME *(confirm exact hostnames as we populate)*  
````

NEW

````text
* CNAME *(exact hostnames OPEN/TBD)*  
````

## RL-006

Redline number: RL-006
Findings or source items: TW-DRAIN-10 100926.1 marker rule (no ledger row)
Change type: DOC_HYGIENE
Operation: `FIND_AND_REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **7\) Databases & Schemas \[Required-Now\]**` > `## **7.1 Instances**`
Original-bound location: the three **Database (shared)** bullets (Production, Staging/QA, Development); scope: the whole PF
Original lines (context only): 956, 965, 974
Scope: whole PF.
Expected non-overlapping occurrence count: `3`.
Action: replace every exact FIND occurrence in the scope with the complete REPLACE literal; after application FIND is absent from the scope.
Controlling basis and rationale: "; confirm" is a bare to-do. The replacement keeps the qualifier that the DB-proxy route is not confirmed, which PF07's no-guessing rule (§6.5, §8) requires, without the instruction form.

FIND

````text
*(via DB proxy; confirm)*
````

REPLACE

````text
*(via DB proxy; unconfirmed)*
````

## RL-007

Redline number: RL-007
Findings or source items: A09 with X05 (PF10 v13.8.8 addendum 2.9, Required canon drainage; X05 §17 row "Glow Infrastructure §8 config keys")
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **8\) Config keys & references (names \+ current values)**` > `  ## **8.2 Component-specific keys**` > `  ### **8.2.1 HD Engine**`
Original-bound location: the last bullet of **Vendor-ingest keys (present where noted; secrets redacted)**
Original line (context only): 1268
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.9 carries the plan v1.0 §17 doc-delta candidates; X05 §17 lists "Glow Infrastructure §8 config keys | the new key `HDE_VENDOR_OVERRIDE_AUDIT_PATH`". The key name and the sink locations were confirmed read-only in `engine/bodygraph/vendor_audit.py` on `main` at `0838ba08`. Semantics stay with HDE-CLI-API-Vendor-Ref by title. The existing bullet is reproduced unchanged and the new key block follows it.

OLD

````text
* No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider base URL, AI-provider API key, AI-provider secret-binding name, or AI-provider runtime rail is required or permitted by this HDAPI v2 conformance update.
````

NEW

````text
* No OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider base URL, AI-provider API key, AI-provider secret-binding name, or AI-provider runtime rail is required or permitted by this HDAPI v2 conformance update.

**`HDE_VENDOR_OVERRIDE_AUDIT_PATH` — production vendor-override audit sink (names-only)**

* **Key.** Names the local file to which `hdctl bg:resolve --source vendor` appends its production vendor-override audit events. The value is a filesystem path, not a secret. Per-environment bindings are **OPEN/TBD**.  
* **Checked-in code (routing-only):** `engine/bodygraph/vendor_audit.py` reads this key. When the key is unset or blank, the code uses `glow-hdengine/vendor_prod_override.jsonl` under `XDG_STATE_HOME` when that value is an absolute path, and otherwise under `~/.local/state`. The code does not use a path that is not absolute or that resolves inside the repository checkout.  
* The override flag, the audit event and its fields, its durability, and the refusal when no sink is available are owned by **HDE-CLI-API-Vendor-Ref**. PF07 records only the key name and the sink locations the checked-in code uses.
````

## RL-008

Redline number: RL-008
Findings or source items: TW-DRAIN-10 100926.1 marker rule (no ledger row)
Change type: DOC_HYGIENE
Operation: `REPLACE`
Target document: `PF07-Canon-Glow-Infrastructure`
Section path: `# **8\) Config keys & references (names \+ current values)**` > `  ## **8.2 Component-specific keys**` > `### **8.2.3 Glow Frontend — TBD (names-only)**`
Original-bound location: the second bullet of the closing **Notes (inventory-only).** list
Original line (context only): 1295
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: "Please supply the value when known." is a request to the reader, not a rule. The sentence before it, which defines OPEN/TBD, is kept unchanged.

OLD

````text
* Any **OPEN/TBD** indicates “not present in the variable report / not confirmed.” Please supply the value when known.  
````

NEW

````text
* Any **OPEN/TBD** indicates “not present in the variable report / not confirmed.”  
````

END OF REDLINES
