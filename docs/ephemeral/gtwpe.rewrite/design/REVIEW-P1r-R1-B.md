4 distinct confirmed REQUIRED findings

This round finds 4 required defects, down from the dry run's 6. That does not halve the count, and three of the four sit at least partly in text the last repair added, so both of D26-A rule 5's stop signals apply. The pilot's own path, a tool change, validates. The defects sit on paths the pilot does not exercise: prompt repairs (RB-1, RB-2), the capture tool from P4 on (RB-3), and the drift check over time (RB-4).

## Required findings

### RB-1 · R1 · A new prompt version keeps the old version's page title, and the readback never checks the title

- **Text.** §11.5, *A prompt page*: "Search for the exact new title first; duplicate the current version's page in Notion; apply the approved edits to the duplicate; set its identity lines to the new version." The repair rewrote the verification for DRr-6. It now checks "its identity lines; for each approved edit, its new text present and its replaced anchor absent; its section headings the same as the current version's…; and, after X4, the catalog's link to it."
- **Evidence.**
  - **No step sets the page title.** Nothing gives the new page's Notion title the new version, and the readback checks neither the title nor the parent.
  - **The design treats title and identity lines as separate.** §12.2's readback "checks the exact title and the parent; for a prompt page, its two identity lines". The identity lines are the body's first two lines (§4), and `prompt-body-content-policy.md` counts "the prompt's title" as a body line.
  - **The connector cannot set the title while copying.** Its duplicate operation takes only the source page's ID and "completes asynchronously, so do not rely on the new page … to be populated immediately" (tool description). A title changes only through a separate properties update ("For pages outside of a database: The only allowed property is 'title'"). The copy therefore keeps the current version's title, or a variant of it.
  - **Other rules assume the new page has the new title.** §2.1 keeps TW-MGMT-10's "recheck and exact-title search before each create". Plan §8 says "Inspect the exact target first, and never write twice blind". Both rely on the created page carrying the new title. §11.7's catalog row records a title, and §8.7 already guards the same mismatch for canon files (`TARGET_TITLE_MISMATCH`).
- **Path, likelihood, consequence.** Normal path. It is certain for every prompt change, starting with GTWPE-MGMT-10's own first repair (§13.2, *After it*). What follows:
  - The successor page's title names the old version while its identity lines name the new one.
  - Two sibling pages under the parent share one title, and the catalog's title disagrees with the page.
  - The exact-title search can never find an earlier copy, so a retry after an asynchronous or timed-out duplicate creates a second copy.
  - Nathan's rollback ("archives the unselected page") must choose between identically titled pages.
  - All of this passes the readback silently.
- **Smallest correction.** Once the duplicate is populated, set its title to the exact new title, then set its identity lines. Add "its exact title and its parent" to the readback, as §12.2's readback has.
- **In repair text.** In part. The readback the repair wrote (DRr-6) omits the title and parent. The route itself is from d087e4d, new in v1.1, and this is its first full review.
- **Refutation tried.** "Identity lines" could be read to include the title, since the first line repeats it. §12.2, the content policy and the connector all treat the title as separate. The pilot changes no prompt page (§16), so nothing catches this before the first real repair.

### RB-2 · R1 · A prompt-only repair cannot be selected until Nathan merges a pull request that holds only the record

- **Text.**
  - X2: "Push the branch and open its pull request; return PRODUCT_OWNER_ACTION_PENDING for Nathan's merge".
  - X3: "Resume after the merge, from main".
  - X4 moves the catalog row to the new version, after X3.
  - §11.3: the branch holds "the record and, at EXECUTE, its repository changes".
- **Evidence.**
  - A Modification whose changes are all in Notion (a prompt page, the catalog block) has no repository change except its record and evidence. X2 still opens a pull request and waits for its merge, and the selection at X4 waits behind it.
  - That merge approves nothing (D21-C; §4.4), and X3 can check nothing but the record's blob.
  - Nathan, 2026-09-28: "We can use them, but they cannot gate." W1 recorded this as "No phase, check or relay waits on a PR being opened, reviewed or merged" (CHECKPOINT §8).
  - The design applies that ruling to runs (§9.1) and to X5 ("nothing waits on that merge (D21-C)"), but not to X2.
- **Path, likelihood, consequence.** Normal path for every prompt-only Modification, which is the change prompt's main use ("so I can repair the rest of the prompts"). It is certain.
  - Each repair's selection waits on a record merge, which adds a round trip every time and contradicts the ruling.
  - If Nathan leaves the pull request unmerged, as the ruling allows, the repaired prompt is never selected.
- **Smallest correction.** X2 asks for a merge only when the Modification changes a repository file other than its record and evidence, or needs an install. Otherwise EXECUTE pushes the record and goes straight to X4, with the pin set as RB-4 corrects it.
- **In repair text.** No. X2 and X3 are from d087e4d, new in v1.1.
- **Refutation tried.** Merging and then resuming is how the design treats the canon pull request (§9.1) and a tool pull request. There, though, the merge is the adoption. A record-only merge adopts nothing, and X5 already says a record merge gates nothing.

### RB-3 · R3 · From P4 on, `capture` re-reads other workers' transcripts that hold a prompt body, and nothing reports it

- **Text.**
  - §11.6 lets "an isolated readback worker" fetch a body. It says a transcript that holds one "is read only within the check in hand: the fetch, its readback, or the capture of that check's worker return (§7.4)… left to the harness's teardown and never read again".
  - §11.4's capture paragraph, added by the repair, sends worker records through capture (§7.4) once P4 builds `gtwpe_redline.py capture`.
  - §7.4: capture "reads the harness's own subagent transcripts under `…/subagents/`, finds the one assistant message holding both markers", and fails on "two different matches".
- **Evidence.**
  - To rule out a second match, capture must open every transcript in that directory. Any capture made after an isolated readback worker has finished therefore reads that worker's transcript, which holds the new body, for a different check.
  - The change model the design cites makes that worker the expected choice. Class B's verification is "Isolated readback of everything changed", and definition-of-done item 2 is "Verified by isolated readback" (`ecosystem-change-management.md` §2, §5).
  - This breaks D22 condition 2 ("serves only the read or check in hand") and condition 4 ("never read again").
  - Nothing reports it. §16's accepted risk and DLr-3 cover only a capture of that same worker's return.
- **Path, likelihood, consequence.** Normal path from P4 on. It happens in a Modification that reads two prompt pages back through isolated workers, or that captures any worker's return after one. Likelihood is low to medium. The result is a silent, unreported second read of a harness file that holds a prompt body. This breaches a Product Owner ruling (D22), the same class as RQ-3 and E-022.
- **Smallest correction.** Capture opens only the transcript of the agent whose return it captures, found by the agent ID the Agent tool returns, and never scans the directory. §11.6 should say so.
- **In repair text.** In part. The capture paragraph is the repair's (DRr-3). §7.4's scan and §11.6's worker exceptions are older.
- **Refutation tried.** In P3 the targeted P1 method is used, so the pilot is clear. The breach starts with the scanning tool.

### RB-4 · R1 · The drift check never examines commits that land while a Modification runs, or those before P2(b)

- **Text.**
  - A0 runs `git log <the catalog's last-close commit>..origin/main` over the watched paths, once, at the start of ANALYZE.
  - X4: "Its last-close commit becomes X3's merge commit".
  - §11.7: "P2(b) sets that commit to `origin/main` as it writes the block".
- **Evidence.**
  - A watched-path commit that lands after a Modification's A0 and before its merge is an ancestor of the new pin. The next A0 excludes it, and this Modification's A0 ran before it existed, so no drift check ever reports it.
  - The same gap exists between the design's reading of its sources (`canon_read_at` 0db3f0e) and P2(b)'s pin. GTWPE-MGMT-10's body is authored from the design, so it misses anything that changed in that gap.
  - The watched paths took 38 commits on `main` between 2026-09-14 and 2026-09-28, 10 of them on 2026-09-27. A Modification spans two approvals and a merge.
- **Path, likelihood, consequence.** Normal path, on every Modification; likelihood high. A change to a source the GTWPE cites is never reported, so the D26-E search that A0 promises never runs. That is, silently, the D8 and E-019 failure A0 was added to prevent (§9.4; plan v1.2 §16.2).
- **Smallest correction.**
  - At X4, before moving the pin, run A0's `git log` over the watched paths from the commit A0 examined to X3's merge commit (or to `origin/main` where nothing merged), excluding the Modification's own files. Record each change in §E as a trigger finding.
  - At P2(b), set the first pin to the design's `canon_read_at` commit.
- **In repair text.** In part. X4's pin rule is the repair's (DRr-4). The P2(b) pin is from d087e4d.
- **Refutation tried.** The Notion pins are unaffected: X4 leaves them, so a later edit still shows. The PE's complete reads of PF03, PF06 and PF10 at P2(b) narrow the P2(b) gap for those three documents only. No other step re-runs A0.

## Listed findings

- L1 · A1 · The token measure (§11.3, §12.5) comes only from the transcripts' per-call usage, as in P1 (CHECKPOINT §9.5). In a GTWPE-MGMT-10 session those transcripts hold the body, since §13.2 reads it at each mode start and §11.5 reads it back. §11.6 says such files are never read again, so either the twice-the-estimate stop goes unmeasured or D22 condition 4 is broken again (P1 disclosed its re-read). Path normal; likely at each checkpoint; a D22 re-read or an unmeasured stop; not repair text.
- L2 · A2 · Closure "read from §6" cannot be repeated exactly. §6 names stages and actors (S1, S2, "Drafter", `main`), not members, so mapping them is judgement (does R2 consume H2?). Tier 0 turns on "provably changes neither", and even the pilot's tier 1 could be read as 2, since it fixes H2's artifact. Path normal; medium; the same change gets different gates; not repair text.
- L3 · A2 · At P4 the handoff table moves into `gtwpe-run-procedure.md`, but GTWPE-MGMT-10, landed at P2(b), reads "§6's handoff table" (§4.4, §11.3, §11.9), and no step repoints it. After the first tier-2 change, closures read a stale table. Path normal after P4; medium; a gate silently covers too little; not repair text.
- L4 · A3 · Under PROMOTION_CHECKPOINT_REQUIRED, X5 marks the record COMPLETE with the new version unselected. No step or resume point (§11.8) then performs Nathan's selection, because only X4 changes the catalog (§11.7). Path normal when a plan names no selection; certain then; a loud stop, then an improvised write or a whole Modification; repair text.
- L5 · A3 · X5 opens no pull request for the COMPLETE record, yet says "Nathan merges it". Path normal; certain; the session improvises one, or the record stays off `main`; repair text.
- L6 · A3 · X3 compares against "the branch's blob", which no step records. Merged branches are deleted (#541, CHECKPOINT §9.1), so a fresh-session resume at X3, a D26-C checkpoint, has nothing to compare against. Path failure; low; loud; not repair text.
- L7 · A3 · H13 runs the validator at ANALYZED, which cannot see a missing `item_count_at_approval` (required only from PLANNING); the gap surfaces at PL4. Path failure; low; loud; in part repair text.
- L8 · A3 · A6's "the validator's … dry-run checks" cannot fail in ANALYZE, because `_dry_run_first` tests PLAN only. Path failure; low; a skipped ANALYZE dry run passes unflagged; not repair text.
- L9 · A3 · The failure path's "the freeze kept" (D26-B's wording) names no GTWPE freeze. Path failure; low; an undefined step at a stop; not repair text.
- L10 · A4 · The prompt readback is done by the session that wrote the edits. The cited change model requires "Isolated readback" (class B; definition-of-done item 2), and the design does not name the deviation; the isolated alternative leads to RB-3. Path normal; certain without a named worker; a self-check; repair text.
- L11 · A4 · A rollback after X4 needs a whole new Modification, since only EXECUTE changes the catalog, and it inherits RB-2's merge wait. §11.5 names no actor. Path failure; low; a bad prompt stays selected longer; not repair text.
- L12 · A4 · D-10 allows "create child pages" and "update the parent's catalog block". Editing the duplicate after creation, and setting its title (RB-1), is not clearly covered by `notion-write-boundary.md`'s requirement that a rule "names this artifact type and its page". Path normal; low; a strict session stops; not repair text.
- L13 · A4 · "its replaced anchor absent" fails an approved insertion whose new text keeps its anchor. Path normal; low; loud; not repair text.
- L14 · A4 · A change coupling a prompt and a tool makes the tool current at merge but the prompt only at X4, or never. That leaves an incompatible pair live, which HDE Governance §9.1.6 rules out ("An edited subgroup is not ready while an affected counterpart remains incompatible"). Path normal for coupled tier-2 changes; low; a run mismatch, mostly loud; not repair text.
- L15 · A5 · S1 reads "its path" from a search result, but no record shows search returning a path. Recorded results carry a title and a minute-resolution `timestamp`, and the connector documents `path` on fetch only. The title test alone misses prompt bodies without the identity pattern: PE Metaprompt 091426.1, the GCFPE-MGMT-10 proposed body, TW-Flowmaster-082626.8. Nothing records whether the PE Metaprompt's parent hub `3db4590a05eb811b9c14f2ae89c28df7` lies under AI Prompts. Listed because unverified: if search returns no path, this is R3 (the body is fetched into `source/*.md` and pushed at S1). T5 should test such a page live. Path normal; low; as stated; repair text (DRr-5).
- L16 · A6 · No v1.0 build order remains, and §2.2, §3, §12.1, §12.5 and §13 match plan v1.2 §16.1 and §16.3. But §11.7 ("only EXECUTE changes it") and §2.2 contradict §12.2's P4 catalog update by W1 under G2. Path normal at P4; certain; an inconsistency only; in part repair text.
- L17 · A7 · The Notion pins follow fixed page IDs. From the next release a changed PE or GCFPE member gets a successor page (D23-G, Amendment 1, the PE successor), and promotion replaces the live GCFPE-MGMT-10 in place (D20-B). Such changes surface only through a watched repository file, which reopens E-019 after promotion. Path normal after promotion; medium; a missed trigger, listed as E-019 was; not repair text.
- L18 · A7 · X4 never updates the lineage pins, so a source or PE change that is adopted or declined is reported again by every later A0. Path normal; certain after the first; noise; not repair text.
- L19 · A8 · From P4, `capture` needs `GTWPE-RETURN <nonce>` markers, but the second template's fixed deliverable fixes the first line as the count, so reviewer capture fails with `CAPTURE_UNAVAILABLE` or needs edited fixed text. Path normal from P4; certain; loud; repair text.
- L20 · A8 · Both reviewer templates (fixed §6 "Write your record to <RECORD_PATH>"; "Each writes its own record"; D24's first template) have reviewers write their own files. §11.4 says "Reviewers write nothing" without naming the deviation or its authority (kickoff D6). P1's brief rewrote §6 while its front matter says it is unchanged. Path normal; certain; an undisclosed edit of fixed text, harmless in effect; repair text.
- L21 · A8 · D-13's cold run checks ANALYZE only, and PLAN and EXECUTE run with the author's context. The pilot changes no prompt page (§16), so §11.5's route, X4's selection and PROMOTION_CHECKPOINT_REQUIRED, where RB-1 and RB-2 sit, first run on the first real repair. Path normal; certain; untested before use; not repair text.
- L22 · A8 · D-14 weighs the pilot's second branch against the kickoff only. The installed `glow-write-boundary` also says "One branch per session, one PR per branch". Path normal (P3); certain; Nathan is not asked about the second rule; repair text.
- L23 · §12.2's G2 request "gives each body in the request itself", but Nathan limits reports to five plain sentences with every detail in `CHECKPOINT.md` (§10.1), and no body may enter the repository. The design does not say where Nathan reads the bodies. Path normal (P2(b), P4); certain; a loud conflict at G2; not repair text.
- L24 · The reader's selftest needs synthetic `.docx`, `.pdf` and `.xlsx` files. Plan §4 says "Fixtures: Synthetic Markdown only", and §13.2 does not say where these files live or what generates them (the lock holds readers, not writers). Path normal (P3 X1); certain; a pilot finding; not repair text.

## Attack list, answered

- **A1.** The "check in hand" reading holds only for one targeted read of a worker's own transcript inside its check, which is the P3 method. It fails for the scanning capture (RB-3) and for token accounting (L1). RQ-3's option (ii) would not help here, because in a GTWPE-MGMT-10 session the manager's own transcript also holds the body.
- **A2.** L2, L3.
- **A3.** RB-2, RB-4, L4–L9.
- **A4.** RB-1 and L10–L14. The rollback works before X4 but is slow after it (L11). No step copies a body.
- **A5.** L15.
- **A6.** L16.
- **A7.** Edits to the pinned pages after the pinned minute are seen. RB-4, L17 and L18 cover what is not. Before the first close, the last-close commit is `origin/main` at P2(b), which skips everything since 0db3f0e (RB-4).
- **A8.** L19–L22. H12 and H13 otherwise match §11.4.

## Prior findings and trend

The dry run found 6 required defects; this review finds 4, so the count did not halve. RB-1, RB-3 and RB-4 sit in part in the repair's text.

- DRr-1 and DRr-2: fixed.
- DRr-3: fixed, with a new defect (RB-3; also L19, L20).
- DRr-4: fixed, with a new defect (RB-4; also L4, L5).
- DRr-5: fixed as far as the committed text shows (L15).
- DRr-6: fixed, with a new defect (RB-1; also L10).

## Claims

- **C1** holds.
- **C2** holds for the pilot. It fails for a prompt change (RB-1, RB-2).
- **C3** holds in part: RB-4 and L2, L3, L17, L18.
- **C4** holds in part. No step needs a body copy, and rollback before X4 works; but see RB-3 and L1.
- **C5** holds in part: L15.
- **C6** holds in part: L12, L16.
- **C7** holds in part: L21.
- **C8** holds for the three target rulings. No step can list, draft, apply or open a pull request against PF10, and §8.7's classes match the 34 files on `main`. The G0 direction is served only in part (L21, RB-1, RB-2), and RB-2 contradicts the separate "cannot gate" ruling.

## Canon relied on

- **Canon, read from `origin/main` at 0db3f0e.**
  - PF04, HDE Governance §9.1.6, read in full. I found it with `git grep` over `docs/pfcanon/` for prompt-ecosystem terms.
  - The 34-file list of `docs/pfcanon/`.
  - I did not read PF03, PF06, HDE Build Notes, PF20, PF27 or PF30.1, and no finding rests on them.
  - AGENTS.md: the canon-first rule, canon is read-only, the truncation guardrail, evidence attribution, and the PR headings.
- **In-flight documents.**
  - The design v1.1 at a33647c, read whole (1,153 lines, 107,613 B, sha256 `14365db0…`), with the repair diff from 4e3a3db.
  - Read whole: `DRY-RUN-P1r.md`, `CHECKPOINT.md`, `P1-SOURCE-NOTES.md`, `REVIEW-P1-DIFFCHECK-R1.md`.
  - Read in part: `REVIEW-BRIEF-P1-DIFFCHECK.md` (front matter and §6) and `TW-MGMT-10-ANALYSIS-20260924.md` (lines 1–200).
  - Plan v1.2 and `ERRORS.md`, whole, from `origin/docs/20260928-pe37-gtwpe-facilitation` at 0ecb6a1.
- **Governing documents (byte-identical on main and at a33647c).**
  - `gcfpe.decision-record.md`: D17; D20–D22; D23-G with Amendment 1 and the PE successor; D26.
  - Read whole: `modification-template.md`, `modification_validate.py`, `ecosystem-change-management.md`, `reviewer-prompt-template.md`, `notion-write-boundary.md`, `prompt-body-content-policy.md`, `pe37.stage5/MGMT-10-REVISION.md`.
  - Read in part: `authoritative-surfaces.md` (through its Notion tables), `pe36-to-pe37.md` (the state and open items), and the cost and *Harness files* sections of `MODIFICATION-20260923-closeout-residuals`.
  - The installed `glow-write-boundary` SKILL.md.
  - The Notion connector's tool descriptions, loaded locally. I made no Notion call.

## Writes

None. Every git command I ran was read-only: show, log, diff, ls-tree, grep, rev-parse, status. `.git/index` and `FETCH_HEAD` carry timestamps from before I started. I listed only the file names in this session's `tool-results/` and `subagents/` directories; I opened none of those files and read no prompt body.

DECISION NEEDED
