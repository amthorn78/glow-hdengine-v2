# Notion worker notes: PLAN repair round, MODIFICATION-20260923-closeout-residuals

Worker: PLAN r1 Notion worker, 2026-09-23. Nothing was written to Notion, Drive, the repository or
`/root/.claude/skills`. The drafts are in `edits.json`: 14 `update_content` edits, each with an
`old_str` that occurs exactly once in the page as fetched.

## 1. Sources read

| page / file | id | last edited | fetched as of | how much was read |
|---|---|---|---|---|
| Glow Operations Hub | `3ce4590a05eb814f8892f88ff8539308` | 2026-09-23T17:46:27.946Z | 2026-09-23T22:24:21.603Z | 173,645 chars, 1,034 lines (harness-saved). I read these lines: 100-140, 152-166, 240-265 and 685-712. I also grepped the full text for every pattern named below. I did not read the rest line by line. |
| PE Metaprompt 091426.1 | `3db4590a05eb8174be35d9e35acb3f77` | 2026-09-23T17:17:22.217Z | same | Read completely: chars 0-76,125, 353 lines (harness-saved). I treated it as a prompt body under D22 (see §7). |
| GCFPE MGMT Change-Process Redesign — Tracking | `3e34590a05eb81e7927efe0541258916` | 2026-09-23T17:45:35.845Z | same | Read completely (returned inline). |
| Glow HDE Prompt Flow Index — GCFPE-20260914.1 — 091426.1 | `3db4590a05eb81de9736ea69bac61016` | 2026-09-23T17:43:21.509Z | same | Read completely (returned inline). |
| GCFPE Membership and Release Register | `3d24590a05eb81ce942ad994cfca9fa1` | 2026-09-23T17:43:39.489Z | same | 91,078 chars, 413 lines (harness-saved). I read the headings and lines 305-322, and grepped the full text for the patterns in §5. |
| GCFPE Alpha Feedback — Deferred Items — 091426.1 | `3df4590a05eb8111a6a5f67cb82f96f6` | 2026-09-23T17:26:17.764Z | same | Read completely (returned inline). |
| HDE Change Flow Overview | `3c74590a05eb811d8433e7022629e213` | 2026-09-23T17:43:53.114Z | same | Read completely (returned inline). |
| HDE IA — GCFPE-20260914.1 — 091426.1 | `3db4590a05eb8195a2ccf7c0959a8b6e` | 2026-09-23T17:18:27.894Z | same | Read completely (returned inline). |
| HDE Change Flow — GCFPE-20260914.1 — 091426.1 | `3db4590a05eb81d59059eb6b95ed5fcf` | 2026-09-21T19:42:29.626Z | same | Read completely (returned inline). |
| GCFPE Expanded Prompt Repair Plan and Six-Batch Checklist — 20260915.1 | `3dc4590a05eb81a9adf1d8f800863937` | 2026-09-23T17:43:56.381Z | same | 174,179 chars (harness-saved). Grepped only. |
| Checklist rows for items 1-4 (Glow Operations Checklist) | `3d54590a05eb8142a187d32ad4435950`, `3d54590a05eb8119affafcfb024ba990`, `3d54590a05eb8159a73cf6af261c1c2b`, `3d54590a05eb8118b229e0ca25bdfd42` | 2026-09-08T07:23:26/28/29/30Z | same | Each read completely (returned inline). |
| CL-40 — Repair CRD candidate scope definition (Checklist row) | `3d54590a05eb81bd853bdd49a0954213` | 2026-09-08T09:50:01.316Z | same | Read completely (returned inline). |
| Drive `Candidate-CRD-Items-List.md` | `1JPN7WcqCddC2J7UKkHdO4gnIPYRJPGJO` | modifiedTime 2026-09-08T07:25:47.904Z | 2026-09-23 | Metadata, plus complete content: `read_file_content` (backslash-escaped rendering) and `download_file_content` (raw base64, inline, not saved). |
| Repository | `docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md`, `.../evidence/closeout-residuals/ANALYZE-anchor-census.md` (sha256 `759bdd52007cabe74a05aee2619212b819325a8d0e8b36b98d0e727008bbf205`, 56 lines), `docs/prompt_ecosystem_management/gcfpe.decision-record.md` (D22 :1160-1222, D23-G successor :1420-1433), `docs/prompt_ecosystem_management/notion-write-boundary.md` | — | — | Read only. |

Before applying any edit, EXECUTE must re-fetch its page and confirm that `old_str` still occurs
exactly once. Every page above can change after these fetch times.

## 2. PART-12 / ITEM-24: the Hub, *Worker communication rules* §2

- The named states are defined at fetched lines 691-694. Line 691 reads "Every message ends in one of exactly three states, named:", and lines 692-694 are the three bullets. The last bullet is `- **IN FLIGHT** — something is running; the Product Owner waits`, followed by `## 3. …` at line 695.
- Edit `PART-12-HUB-01` inserts the P-32 sentence verbatim, as a new paragraph directly after the IN FLIGHT bullet. The sentence was extracted programmatically from DECISIONS.md line 136, so it was not retyped.
- `old_str` count on the page: 1. The only other "IN FLIGHT" is at line 819, inside the *Standard skill reviewer prompt* template: "close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT." That template has no handoff block, so it does not conflict with P-32 and no edit is drafted for it.

## 3. PART-18 / ITEM-37: C-LAT placement

**PE Metaprompt GCFPE overlay: no placement statement found.**
- **Where it is:** page `3db4590a05eb8174be35d9e35acb3f77`, section `# GCFPE controlled release overlay`, lines 208-290. I read the whole page.
- **What it says about C-LAT:** it never lists which bodies carry C-LAT or the *Decide it during work* block. It has no "all 10 bodies" wording.
- **Its only placement rule is by delegation**, in *Candidate authoring contract*: each other canonical text, C-LAT included, appears "where its registry row requires it". That remains correct after this Modification, because the registry drafter keeps the required Material regex on all 10 rows and moves 'Decide it during work' to forbidden on the 8 (plan_result.json `reg.clat_guard_changes`).
- **Its other C-LAT mention** is in *PR execution, rescope, merge, and abort contract*. It applies C-LAT to PR-30 and PR-35, which is correct under Q2 (a).
- **No edit is drafted.**
- **Searches run:** `PE Metaprompt GCFPE overlay`, `C-LAT`, `Decide it during work`, `C-LAT placement bodies Decide it during work`. Full-text greps for `C-LAT`, `three-step`, `Decide it`, `decide it, implement`, `ten bodies`, `10 bodies`, `latitude` and `D23-C` ran on the Hub, the register and the Expanded Repair Plan page. The Flow Index, the Overview and the IA and Change Flow hubs were read in full.

Only one other Notion control page states C-LAT's placement:
- **Where:** *GCFPE Alpha Feedback — Deferred Items — 091426.1* (`3df4590a05eb8111a6a5f67cb82f96f6`), in AF-009's disposition: "(C-LAT, in the ten bodies with a rescope threshold)".
- **The draft:** edit `PART-18-AF009-01` appends a dated amendment note after the paragraph's last sentence. The disposition itself is dated, so it is not rewritten (`AUTH-001`).
- **Scope flag:** this page is not among PART-18's named targets. Your decision.

**No placement statement on the other pages checked:**
- Hub: 0 hits.
- Flow Index: 0 hits.
- Register: 0 hits for `C-LAT`, `Decide it during work`, `three-step`, `ten bodies`. Its 11 "Material" hits are PF10/review wording.
- Expanded Repair Plan: 0 hits.
- Overview, IA hub and Change Flow hub: none.

## 4. PART-11 / Decision 11: the D20 redesign tracking page

- **Where dated entries go.** The page's convention is a bold-dated paragraph at the end of *Where things actually stand*. Examples: "**2026-09-23: those results are void**" and "**2026-09-23: stage 4's first real use ran end to end.**"
- **Placement.** Edit `PART-11-TRACK-01` inserts one entry dated 2026-09-23 immediately before the heading `## The three decisions — answered 2026-09-22`. The heading is unique, and it is the section's end.
- **Source.** The entry names `ANALYZE-anchor-census.md`, section *The proposed MGMT-10 body*. It says these items are not resolved by this Modification, citing §A Decision 11.
- **What it lists:**
  - both read-only 'Must not' lines;
  - exactly one Modification, together with EXECUTE's new-scope Modification;
  - result codes;
  - the approval fields;
  - artifact locations;
  - the entry contract;
  - the open-PR outcome;
  - install verification;
  - the release-selection boundary;
  - YAML governance state.
- **Coverage.** The census has 12 items. The two read-only lines share one bullet, which gives 10 bullets.
- **Quotes.** Five body quotes, each at most 11 words, all taken from the census.
- **Dating.** The entry is dated 2026-09-23 as instructed. If EXECUTE writes it on a later day, the plan should say whether to keep 2026-09-23 (the census date) or use the write date.
- **Stale lines on the same page, not drafted:**
  - the yaml `status: STAGE_4_FIRST_USE_COMPLETE_FOLLOW_UP_MODIFICATION_AT_INTAKE`;
  - "which is at `INTAKE` with `ANALYZE` in progress";
  - the Records row "`INTAKE`, branch `claude/epic-tesla-17406z`".

  ANALYZE was approved on 2026-09-23, so these are out of date. EXECUTE's close-out should update them.

## 5. PART-06: the Candidate CRD Items List

### (a) Parent page
Glow Operations Hub: `3ce4590a05eb814f8892f88ff8539308`.
- This is the same page as the task's Hub. Its property title is "Glow Operations Hub", the emoji icon 🧭 is separate, and its ancestor path is empty.
- The tracking page and the Glow Operations Checklist database (`67f82c6bf83e4c88865eadfebf770c03`) are its children.
- **No existing page is titled "Candidate CRD Items List".** Searching `Candidate CRD Items List` and `Candidate-CRD-Items-List.md` returned no page with that title.

### (b) Drive file
- **Metadata.**
  - name `Candidate-CRD-Items-List.md`;
  - mimeType `text/markdown`;
  - size 31,923 B;
  - created 2026-09-05T07:49:18.517Z;
  - modifiedTime 2026-09-08T07:25:47.904Z;
  - owner nathan@englishbiztraining.com;
  - parent folder `1rtlPtV1FLkyaeFSvQ2lsw1I-Lq-YFbG8`.
- **Encoding.** The raw bytes (base64 from `download_file_content`) are UTF-8 with LF line endings; no CR was seen. The escapes such as `\#` and `\*` exist only in `read_file_content`'s rendering, not in the file.
- **Metadata lines.** Four of the five header lines end with two spaces, which are Markdown hard breaks.

**Structure outside the code fence (the current register)**
- **Headings.**
  - One H1, "Candidate CRD Items List".
  - Twelve H2s: Document purpose; Controlling scope statement; Inclusion criteria; Exclusion criteria; Classification test; Candidate item format; Review-status definitions; Routing instructions; Active CRD candidate list; Moved-items history; Maintenance rule; Scope-repair revision record.
  - One H3, "Preserved pre-repair source", under Moved-items history.
- **Header metadata fields.** There are five: `Updated`, `Document status`, `Home`, `Decision owner`, `Persistent filename`.
- **Lists.**
  - Numbered: Inclusion criteria (5) and Routing instructions (7).
  - Bulleted: Classification test (5), Candidate item format (13 bold field labels) and Scope-repair revision record (2).
  - One blockquote, the controlling scope statement.
- **Pipe tables.** There are two:
  - Review-status definitions: 2 columns, header plus 6 rows (New, Needs Review, Accepted for CRD Drafting, Rejected, Moved to Operational Tracking, Deferred).
  - Moved-items history: 6 columns (Original local item, Title, Final classification, CRD review status, Preserved operational outcome, Current Notion identity), header plus 4 rows.
- **Links.** Eight Markdown links, all to Notion:
  - `3ce4590a05eb814f8892f88ff8539308` (the Hub);
  - `67f82c6bf83e4c88865eadfebf770c03` (the Checklist);
  - the Item 1-4 rows `3d54590a05eb8142a187d32ad4435950`, `3d54590a05eb8119affafcfb024ba990`, `3d54590a05eb8159a73cf6af261c1c2b` and `3d54590a05eb8118b229e0ca25bdfd42` (each with `?pvs=204`);
  - `3d44590a05eb81cbb93ffe032b9aaa61`;
  - `3d54590a05eb81bd853bdd49a0954213` (with `?pvs=204`).

**Structure inside the code fence** (one fenced block, info string `markdown`, holding the complete 2026-09-07 pre-repair source verbatim):
- **Headings.**
  - One H1.
  - Seven H2s: Purpose; Candidate items; 1. Repository prompt-use provenance helper; 2. QA-10 substantive, paste-ready PF10 findings summary; 3. QA-90 explicit Product Owner task selection; 4. Combined audit-and-plan invocations for IA and QA preparation; Revision record.
  - Twenty-one H3s: 6 under item 1 and 5 under each of items 2-4.
- **Pipe tables.** There are two: Candidate items (5 columns, header plus 4 rows) and Historical implementation proposal (2 columns, header plus 5 rows).
- **Links.** Twelve Markdown links plus one bare URL:
  - Notion: `3ce4590a…`, `3d14590a05eb81458dadf3fabd021b97` (×2), `3d24590a05eb8108864cc13216e91848` (×3) and `3d44590a05eb81cbb93ffe032b9aaa61` (×3, plus the bare URL);
  - GitHub (×2): PR #398, and a blob at `42a854c7…`;
  - Drive (×1): `11O-sdAL6gDPDTYivxOoX5UUIr6NGArr0`.
- **Bullets.** Three under "Questions for future consideration" and four in the revision record.

**Candidate items**
- Active candidates: **0**. The *Active CRD candidate list* section states that the list is empty.
- Items: **4**, all moved to operational tracking. Their local identifiers are 1-4, with these titles:
  1. Repository prompt-use provenance helper
  2. QA-10 substantive, paste-ready PF10 findings summary
  3. QA-90 explicit Product Owner task selection
  4. Combined audit-and-plan invocations for IA and QA preparation
- Each of the four appears in the moved-items table and again as an H2 inside the code fence.

**What Notion Markdown would change** (from `notion://docs/enhanced-markdown-spec`):
1. **Pipe tables are not Notion Markdown.** The two tables outside the fence must be converted to `<table header-row="true">` with `<tr><td>` rows. Cell links stay `[text](url)` rich text. The two tables inside the fence stay literal text.
2. **Blank lines are stripped.** Each paragraph, list item and heading becomes its own block.
3. **Hard breaks.** The five metadata lines become five paragraphs, or one paragraph joined with `<br>`.
4. **Code block content is literal and is not escaped.** The fence holds no nested triple backticks. It contains `<change-id>` and backticks, which are safe inside a code block.
5. **Characters that would need escaping outside code** (`\ * ~ $ [ ] < > { } | ^`) appear literally nowhere outside the fence and tables. Every `*`, `[ ]`, backtick and `>` there is markup. EXECUTE should confirm this with a scan of the raw bytes.
6. **The body H1 duplicates the page title.** Drop it from the body; the title carries it.
7. **Notion may rewrite Notion links**: a different domain, a dropped `?pvs=`, or a `<mention-page>` on fetch. Compare links by target, not by exact string.
8. **Non-ASCII text** (—, –, “ ”, §) is preserved as UTF-8.

**The file's text still names Drive as its own store in 8 places outside the fence.** Listed by location only:
- the metadata fields `Document status`, `Home` and `Persistent filename` (and `Updated`, the file date, goes stale);
- *Document purpose*, paragraph 2, sentence 1;
- *Classification test*, closing paragraph ("active Drive list");
- *Routing instructions* item 3 ("active Drive entry … this file's moved history") and item 4 ("active Drive list");
- *Maintenance rule*, sentence 3 (re-read this exact Drive file before updating it).

The dated 2026-09-08 bullet in *Scope-repair revision record* and everything inside the fence are historical and stay as written.

**Migration method.** Recommendation: M2.
1. **Preconditions.** The D25-A entry is committed (commit 1). The destination-rule row exists in `notion-write-boundary.md` (P-30; its URL is filled in commit 2).
2. **Collision check.** Run `notion-search` with query `Candidate CRD Items List` and `page_url` set to the Hub. No child with that exact title may exist.
3. **Read the source.** Get the raw bytes with `download_file_content`, decode as UTF-8, and record byte length and sha256 in the evidence file. It is not a prompt body, so hashing is allowed. Keep no copy of the content in the repository: the Notion page is the list's only store.
4. **Convert.**
   - Drop the body H1 and use it as the title.
   - Add one callout at the top recording the migration: source file name and id, 31,923 B, the modifiedTime above, the migration date, `GCFPE-MGMT-10`, and `MODIFICATION-20260923-closeout-residuals` PART-06 (`D25-A`). It states that this page is the list's only store and the Drive file is Nathan's reference copy.
   - Write metadata lines as paragraphs, H2 and H3 unchanged, lists unchanged and the blockquote as one `> ` line.
   - Convert both outside tables to `<table header-row="true">`.
   - Copy the fence as ` ```markdown ` … ` ``` `, with its content byte-identical.
   - Escape nothing.
   - **M2 (recommended):** rewrite the 8 Drive store references so they name this page, and append one dated bullet to *Scope-repair revision record* saying what moved and which references changed.
   - **M1:** migrate everything verbatim and rely on the callout. M1 leaves the only store telling writers to re-read and update a Drive file, which contradicts CL-40's new sentence (R-ITEM18).
   - Under M2, the replacement wording for the 8 references must be drafted in the spec from a fresh read of the file. This worker did not draft it, because doing so means quoting the file.
5. **Create.** Call `notion-create-pages` with parent page `3ce4590a05eb814f8892f88ff8539308`, title `Candidate CRD Items List`, and the converted content. If the call rejects roughly 32 KB of content, create the page through *Moved-items history* first, then append the H3, the code block and the last two sections with `notion-update-page` (insert after), re-reading after each write.
6. **Read back.** Fetch the returned page completely. Every field below must pass. On a failure, fix only the failing block and read back again. Never blindly repeat a create.
7. **Normalize the URL.** Put it in the form `https://app.notion.com/p/<32 hex>` (the form G-K45 requires). Only then fill `{{CANDIDATE_CRD_LIST_URL}}` in CL-40 (R-ITEM18), in the P-30 row and in the pointer edits below.
8. **Nathan banners the Drive file** as superseded, pointing to the page.

**Readback criterion: the fields compared.**
- **F1.** Page title equals `Candidate CRD Items List` (also the Drive H1). The ancestor-path parent is `3ce4590a05eb814f8892f88ff8539308`.
- **F2.** The ordered (level, text) heading sequence outside the code block equals the Drive's 12 H2 plus 1 H3.
- **F3.** Item count. The active candidate list holds 0 entries in both, and the "Empty — 0 active …" statement is present. The moved-items table holds 4 data rows in both.
- **F4.** For each moved-items row, all 6 cells are equal after whitespace normalization:
  - the local id (1-4);
  - the title (the four titles above);
  - the final classification;
  - the CRD review status;
  - the preserved operational outcome;
  - the Notion identity (link text `Item N` plus the target page id).
- **F5.** Review-status table: 6 rows × 2 cells equal.
- **F6.** Links outside code. The multiset of (link text, normalized target) is equal, 8 items. Normalization for Notion URLs keeps the 32-hex page id: drop the domain, dashes and `?pvs`, and accept a `<mention-page>` with the same id. Non-Notion URLs are compared exactly.
- **F7.** Exactly one code block, language `markdown`. Its content equals the Drive fence content byte for byte after LF normalization. Any difference, including trailing whitespace, is recorded and fails the readback unless it is purely trailing spaces on a line. Derived checks inside it:
  - 12 links plus 1 bare URL;
  - 7 H2 and 21 H3 lines;
  - 4 item H2s whose titles equal F4's.
- **F8.** List counts: Inclusion 5, Routing 7, Classification 5, Candidate item format 13 (labels equal), and Scope-repair record 2 original bullets (plus 1 under M2).
- **F9.** The normalized plain text of every block outside code equals the Drive's, except the callout, the M2 rewrites and the M2 bullet. Any other difference fails.
- **F10.** Identifiers: the set {1,2,3,4} and the four titles appear in F4 and in the code-block H2s of both.

### (c) Pages that mention the list or the Drive file
**Pointer edits drafted (10):**

| page | edits | what changes |
|---|---|---|
| Hub `3ce4590a05eb814f8892f88ff8539308` | `PART-06-HUB-01` | Current *Candidate CRD Items* section, line 110: the "authoritative" Drive link becomes a link to the Notion page. Adds a correction note. |
| same | `PART-06-HUB-02` | Line 112: the moved-items history is no longer "the Drive moved-items history". |
| same | `PART-06-HUB-03` | Line 123: ambiguous items go to the Checklist's *Ambiguous* view, out of the active list. |
| Item rows 1-4 (4 pages, table in §1) | `PART-06-ITEM{1..4}-01` | The *Evidence and history* bullet naming the "Authoritative Drive register" becomes a link to the Notion page, and the Drive link is kept as a labelled reference copy. |
| same | `PART-06-ITEM{1..4}-02` | Appends a dated movement entry after the dated 2026-09-08 entry, which says to preserve facts "in the same Drive file". The dated entry itself is not rewritten (`AUTH-001`). |

**No edit, with the reason.** I classified these from full reads, search highlights and each page's own historical labels.

| page | mention | why no edit |
|---|---|---|
| Hub, lines 67 and 70 (*Historical selection — GCFPE-20260907.2*) | concrete-target test; "updates the existing CRD candidate list" | Historical section. |
| Hub, line 125 | dated 2026-09-08 prompt follow-up | Dated record (`AUTH-001`). |
| Hub, lines 128-132 (`<details>` historical navigation) | two Drive links | Historical. |
| Register, line 321 (*Product Owner decision — 2026-09-05: Deferred*, inside *Mandatory PR and PF-document authority boundaries*) | Drive link | Dated decision record. |
| Register, lines 232, 240, 243, 340 | "existing (CRD) candidate list" | Historical selections; the wording names no store. |
| CL-40 — Repair CRD candidate scope definition `3d54590a05eb81bd853bdd49a0954213` | "[Drive register]" navigation link; the quoted 2026-09-08 recommendation | Done record of a 2026-09-08 repair. Optional. |
| GCFPE — QA and OPS Execution Sources and Commit Progression — Alpha 1 `3d24590a05eb81c39bffeb3af5c6e3e7` | copy of the 2026-09-05 decision | Historical (2026-09-05). Not fetched in full. |
| GCFPE — Alpha Establishment and Change Management Checklist `3d24590a05eb81059255fa60ed15ee7b` | copy of the 2026-09-05 decision | Predecessor checklist; the current one is `3db4590a05eb812f87caed515836687f`, and a page-scoped search found no mention on it. Not fetched in full. |
| GCFPE — CRD Alpha Test 1 — Manual Flow Checklist `3d24590a05eb8108864cc13216e91848` | Drive link; "existing candidate list" | Alpha Test 1 completed 2026-09-07; historical. Not fetched in full. |
| GCFPE-END-CYCLE-SCAN-20260907 `3d44590a05eb8124b84fc37df470cb7b` | candidate list | Historical 2026-09-07 case. Not fetched in full. |
| HDE Change Flow Overview `3c74590a05eb811d8433e7022629e213` | "updates the existing … CRD candidate list" ×2 | Only in historical sections, and the wording names no store. |
| CL-40 bodies | list update instructions | The live `3db4590a05eb81db9c88cde6027e07bf` is handled by R-ITEM18 and R-A4c. The archived 091226.1, 091226.3, 091326.1 and 091326.2 versions are never edited. |
| Flow Index, IA hub, Change Flow hub, Expanded Repair Plan | — | No mention. |

## 6. Item 5: duplicate check

| page | P-32-equivalent sentence | pointer to a Candidate CRD *Notion* page |
|---|---|---|
| Hub | None. Greps for `named state`, `immediately before`, `Nothing follows`, `comes last` and `last line` all return 0. The *Handoff format* section says the response ends with the block, but it does not place the named state. | None. The current pointer (line 110) and the historical ones (129, 132) all go to the Drive file. |
| Flow Index | None. There is no named-state text at all. | None. No candidate-list mention. |
| Register | None. `IN FLIGHT`, `NOTHING NEEDED`, `DECISION NEEDED`, `named state`, `immediately before` and `Nothing follows` all return 0. | None. The only mention is the dated 2026-09-05 Drive link (line 321). |

The drafts therefore duplicate nothing.

## 7. D22 disclosure

- **Harness-saved files my reads created**, all under `/root/.claude/projects/-home-user-glow-hdengine-v2/398e36e8-b34a-56a2-83e3-75550250e4f5/tool-results/`:
  - `mcp-Notion-notion-fetch-1790204004900.txt`: the Hub, a control page.
  - `mcp-Notion-notion-fetch-1790204188352.txt`: PE Metaprompt 091426.1. I treated it as a prompt body.
    - It was read once, completely and in place (chars 0-76,125), for the placement check only.
    - It was not copied, hashed, byte-compared or reused, and it was not read again.
    - I did not delete it: the harness refuses a session `rm` in its tool-results directory (D22's refinement). It is left to the harness's teardown.
  - `mcp-Notion-notion-fetch-1790204278915.txt`: the register, a control page.
  - `mcp-Notion-notion-fetch-1790204407005.txt`: the Expanded Repair Plan, a control page.
- **No other prompt body was fetched.** `notion-search` highlights showed short snippets of CL-40, RS-10/20, PR-10/20/30/35/40, DOC-10/20 and IA-30 in tool output. None was saved or reused.
- **Quotes of any prompt body in my outputs:** at most 11 words each. The tracking entry quotes the proposed MGMT-10 body via the census. The AF-009 note uses "Decide it during work" (4 words). These notes quote the overlay's "where its registry row requires it" (6 words).
- **The Drive file** is not a prompt body. Its content came back inline and was not saved. These notes carry only counts, identifiers and headings from it.

## 8. Open decisions for the plan author

1. **AF-009 edit scope.** `PART-18-AF009-01` falls outside PART-18's named targets. Include it as a same-class statement of C-LAT placement, or record it for a follow-up.
2. **The database property `Authoritative Drive register`** (URL) on the Glow Operations Checklist, data source `collection://7947854b-ce35-4520-901e-ae912a9fb6f8`, holds the Drive URL on the 4 item rows and on the CL-40 repair row. `update_content` cannot change it. The options are:
   - **(a)** leave it, as history;
   - **(b)** set the value to the Notion page URL with a `notion-update-page` property update, which leaves the column name wrong;
   - **(c)** rename the column with `notion-update-data-source`, then do (b).

   None is drafted. (b) and (c) are writes that PART-06's targets do not name.
3. **M1 or M2** for the list's own 8 Drive references. M2 is recommended. Its wording needs a fresh read of the file at spec time.
4. **The pointer edits are not named in PART-06's targets.** Without them, the Hub and the item rows keep sending readers to Drive as the authoritative list. The plan should list them as PART-06 steps so that they are task-authorized writes.
5. **Tokens to fill.** `{{CANDIDATE_CRD_LIST_URL}}` appears in 9 edits and `{{EXECUTE_DATE}}` in 6.
   - Refuse any `update_content` whose `new_str` still contains `{{`.
   - The pointer edits run only after the page's readback passes.
6. **The Hub must keep its `<page>` child tags** when edited. The new page will appear there as a `<page>` block, and removing one would detach that child.
7. **Stale tracking-page status lines** (§4) are not drafted. They belong to EXECUTE's close-out.
