1

GTWPE-TW-DOCUMENT-RULES-PLAN-A: full PLAN review 1 of at most 2 (D26-A) of MODIFICATION-20261006-gtwpe-tw-document-rules, §P at fd14d328ab5b591f65459b570a3f633377691e88. I found one required defect. The record prompts' new rule against placeholders, and the check they run before saving, cannot be met on the PF20 and PF30.1 files they must copy byte for byte, because those canon files already carry placeholders of their own. The defect is not in text the last repair added. The rest of the plan holds:
- The gate texts carry Nathan's ruling exactly.
- DR-1's rollover rule is faithful to HDE CRD Records §6 and to §A's R8 statement, and P-3 is right.
- The drains' and TW-APPLY-10's edits bring every ITEM-01 field forward and make any disagreement a loud stop.
- The selection route and its readbacks are sound.

**The brief's hash matches.** `PLAN-REVIEW-BRIEF.md` at 3a12db1 has sha256 `97460f5f9d5d6f396d0dfc7cc212b4ddf7dd103b9e9f3e7043b995322fd58bd2` (13,907 bytes), the value I was given. Commit 3a12db1 adds only that file to fd14d32.

**Checks I ran:**
- The record at fd14d32 is 118,842 bytes, sha256 `97ac1d68…bb48`.
- `edits.json` is 38,960 bytes, sha256 `fc3510c8…a0bb01`, which equals «H».
- `ctl_check.py` has sha256 `4e968007…20923c5`. It is byte-identical to `evidence/gtwpe-tw-repository-io/ctl_check.py` on main.
- `PYTHONDONTWRITEBYTECODE=1 edits_check.py` returns PASS and exits 0:
  - 57 edits: DRAIN-10 7, DRAIN-20 9, RECORD-10 14, RECORD-20 18, APPLY-10 9.
  - 8 GTWPE-D1 items read from the decision record.
  - Longest anchors: REC-FIELDS at 210 characters (in both record prompts) and AP-REF at 145.
- Each of the 11 `--inject` faults exits 1 and is caught by its own code. Some also trip SHARED, OVERLAP or ABSENT.
- I ran the script in the working tree. The working-tree copies of the record, the three evidence files and the GTWPE decision record equal fd14d32's blobs by sha256, so these runs tested the committed bytes.

REQUIRED

R-1: R2, a silent wrong edit to a prompt body. It is also R1, because it breaks the edited record prompts' normal path. Normal path. The conflict is certain on main's PF20 and PF30.1; how a given run resolves it is not.
- **Text, in `edits.json`:**
  - REC-FIELDS-PF20 (RECORD-10-09): "The updated PF20 carries no `Draft` or similar status language about the document, and no placeholder, TODO, unresolved drafting note, editorial comment or instruction to a future writer, and no stale status."
  - REC-FIELDS-PF30 (RECORD-20-11): the same sentence for "The updated PF30", "except a new volume's review copy".
  - REC-CHECK (RECORD-10-12, RECORD-20-14): "check that each updated file differs from its original only by the inserted entry and its control fields, that those fields agree, and that no `Draft` status language, placeholder or TODO remains."
  - Beside these, REC-OUT-PF20 and REC-OUT-PF30 (RECORD-10-08, RECORD-20-10) say the output is the canon file "copied byte for byte … every other byte is preserved, and only the document-control fields below change."
- **Evidence:**
  - **PF30.1 has placeholders.** HDE CRD Records (PF30.1) on main has its own CRD record template in §7. That is canon content of the volume, and 45 of its lines carry backticked `<…>` markers, such as `<CRD_ID>` and `<YYYY-MM-DD>`. Plan Templates' section "Template-safe placeholders and omission syntax" calls `<PLACEHOLDER>` a placeholder marker.
  - **PF20 has placeholders.** HDE Phased Epics (PF20) on main reads "**Date completed:** TBD" in §2.6.1, the historical HDE-EPIC021 record. Its §1 keeps fourteen `<allocated>` entries, which "MAY remain `<allocated>` indefinitely". Change Process Guide §1.1.11 and HDE Governance §9.7.7 both name "TBD" a placeholder.
  - **Canon says to keep them.** HDE Governance §9.1.1 says to "Preserve existing PF20/PF30 content … as dated history", and PF20 §0's drain posture leaves closed records alone.
  - **So every normal run meets a contradiction.** The copy must keep those markers (REC-OUT, and REC-CHECK's "differs … only by"). It must also carry none (REC-FIELDS, and REC-CHECK's "no … remains"). The record prompts have no way to remove them: unlike the drains they prepare no hygiene redlines, and they may change only the entry and the control fields.
  - **The plan made this exception elsewhere, but not here.** DC-HIST and AP-VERIFY both say "unless the document's own canonical format requires that exact language". The record texts have no such clause, and that clause would not cover PF20's historical TBD in any case.
  - **No step in §P can see it.** The dry run's P4 read each passage on the prompt pages, not against the files the prompts copy. X1.3 (g)(4) checks only that each new text is present.
- **Consequence.** Every TW-RECORD-20 run on PF30.1, and every TW-RECORD-10 run on PF20, meets a pre-save check it cannot honestly pass. One of three things happens:
  - The run stops. The record prompts' normal path is then blocked.
  - The run reads the rule narrowly. Its proof log then records a check ("no placeholder … remains") that the file beside it contradicts.
  - At worst, the run edits the template or a historical record, and then fails its own "differs only by" check.
  EXECUTE would land these texts with every check passing.
- **Smallest correction.** Limit both rules to what the record prompts write:
  - In REC-FIELDS-PF20 and REC-FIELDS-PF30, change "The updated PF20 [PF30] carries no" to "The inserted entry and the control fields carry no". End each with "; every other byte stays as canon has it, a template's placeholders and earlier records among them". PF30 keeps its review-copy exception.
  - In REC-CHECK, change "and that no `Draft` status language, placeholder or TODO remains." to "and that the inserted entry and those fields carry no `Draft` status language, placeholder or TODO."
  - Then run `edits_check.py` again (NODRAFT, SHARED and OVERLAP still hold), fix «H» again, and re-read the two passages.
  - This stays within ITEM-03's "except where canon requires it".
  - Optionally, the sentence "No produced document says Draft or carries placeholders … except a new PF30 volume's review copy" in *SECTION* and in its *Current operation* can add "beyond what canon itself carries".
- **In text the last repair added:** no. All three sentences are already in the §P draft at 88a0383. DR-2 changed only REC-FIELDS' list of control fields.

LISTED (each line: attack item; path; likelihood; consequence; whether it is in text the last repair added)
- **L1 (A1, REC-VOL).** After a rollover, the pull request proposes PF30.1 at `Closed to new CRDs` while it holds a CRD registered in that same version, and the next volume at `Pending activation`. No volume is `Active` until Nathan's publication makes the review copy `Canon` and `Active`, as §6 requires. The record report says only that the two files "take effect together". A careful run may read §6's "no new CRD may be registered" against REC-VOL and stop. Rollover path; low, since only Nathan decides a rollover; a loud stop, or a pull request he reviews. In repair text: yes (DR-1).
- **L2 (A1, REC-VOL and REC-ENDPT-PF30).** REC-VOL leaves the review copy's version, effective date and gate unset, while §6 says the volume's version suffix "is established when that volume is created". REC-ENDPT-PF30 names one file and one proof log, where a rollover writes two of each. Rollover; low; left to judgement in a copy Nathan reviews (partly K-11). In repair text: partly (DR-1).
- **L3 (A1, REC-MISSING).** "not permission to create one: only Nathan's rollover decision opens a new volume" can be read as letting a rollover stand in for a missing active volume. REC-VOL still puts the record in the active volume, so such a run most likely ends at a blocker. Failure; low; loud. Not in repair text.
- **L4 (A1, REC-FIELDS, from DR-2).** "every internal restatement of the document's own version or date" lacks AP-REF's guard, "only when it exactly duplicates". On PF30.1, HDE-CRD-0001's "Last material update: `2026-09-07`" equals the volume's effective date. A careless run could change it; REC-CHECK's "differs only by" would then catch the change. Normal; low; loud. In repair text: yes (DR-2).
- **L5 (A3, DC-HIST).** "the preparation date as the revision date" applies whether or not the target's entries carry a date. HDE CLI-API-Vendor Ref §11.1 ("One line per version") and the HDE Copy Tonality Guide's change log carry none. A drain may add a date, which drifts from the format and then meets K-4 if applied on a later day. Or it may omit the date and fail AP-AUTH's "naming the version and date this plan derives". Normal; medium for those two targets; minor format drift or a loud stop. Not in repair text.
- **L6 (A3, DC-HIST against its own first sentence and AP-STATUS).** "remove any such marker anywhere in the target" also reaches a status in the header. The same paragraph reserves header fields to Apply, and AP-STATUS sets a stale status, so the two operations overlap and meet Apply's kept conflict rules. Normal; low, since no PF header on main says Draft; loud. Not in repair text.
- **L7 (A3, DC-HIST and AP-VERIFY).** Glow Infrastructure deliberately marks unknown facts OPEN/TBD, about 97 times; its §2.1 says "Replace TBD as facts are confirmed". Change Process Guide §0.6.1 and Glow QA Guide §11.3 rely on those marks. They fall under the hygiene rule unless each run judges them "required by the document's own canonical format". A run that judges otherwise must either block or propose removing canon's unknown-fact markers. Normal; low to medium for each PF07 run; loud, or visible in the redlines. Not in repair text.
- **L8 (A2, AP-GATE).** The kept sentence "Never substitute the redlines artifact/report filename or an inferred gate token" now sits beside a rule that requires values like `BN 13.5`. A cautious run may read the two as conflicting. Normal; low; loud. Not in repair text.
- **L9 (A5, *SECTION*'s third *Current operation* paragraph).** It keeps "The rules for drains, PF09, package validation and application in the historical operation of TW-ALPHA-20260908.1, below, still apply", with only the gate and the paste-ready sections excepted. §A's D26-E search of the control pages looked for only four old texts, and no X4.3 check looks in that historical operation for the old rules of ITEM-01, ITEM-03 or ITEM-04: Apply's three fields only, status left untouched, a row's status set on instruction. Normal; not measurable from committed text; the page could re-assert a superseded rule by reference. Not in repair text.
- **L10 (A5, W19 and W20).** HDE-NEW and HUB-NEW rename only the old heading. C2's present-tense text, "selects «R»" on *HDE TW* and "**TW-ALPHA-20261006.1 is selected.**" on the Hub, will then sit under "Historical" headings. This is E-038's pattern again, for the release C3 retires. The request leaves E-038 to PE39 after C3, so I note it for that fix rather than raise it. Normal; certain; low. Not in repair text.
- **L11 (A5, carried from C2's review, its L8).** X4.3 (2), X4.4 and X4.6 check «PA» by its text, and «S» matches the same text when approval and selection fall on the same UTC day. Normal; medium; a missing «PA» would pass. Not in repair text.
- **L12 (A6).** X1.3 (g) predicts no counts, so a new text duplicated elsewhere on a page is seen only if it adds a heading or changes the page's last words. A resend cannot cause such a duplicate, because of the OVERLAP rule. A stray copy left by a repeated W1, titled "… — 100626.1 (1)", is not counted by (h). Failure; very low; silent clutter. Not in repair text.
- **L13 (A6, `edits_check.py`).** The eleven checks test what they say. But ONELINE's injected fault exercises only the `new` half, and VALUES would not catch any other «…» value left in a `new`. None is there: «V» appears only in the ten identity edits and the rules note. Normal; low. Not in repair text.
- **L14 (procedure, P-1 to P-3).** §P goes on past its findings on §A, where `modification-template.md` rule 1 says to return to Nathan. The findings are disclosed (K-14) and go to him with the plan, as the model-advice change's L16 did. Normal; certain; procedural. P-3 is tied to the repair (DR-1).
- **L15 (attribution).** §P has no *Canon and rulings relied on* section of its own, unlike C1's and C2's §P. Its canon is cited inline and in the brief, while `AGENTS.md` asks every artifact to record it. Normal; certain; procedural. Not in repair text.

**Attack items, answered:**
- **A1 (the record prompts' output).** DR-1 is faithful to §6. The active volume takes the new record, and on a rollover also `Closed to new CRDs` and a *Next volume* field. The review copy takes no record, a *Previous volume* field, and `Draft` with `Pending activation`, a status §6 says "MUST NOT accept CRD registrations". This matches §A's R8 statement. P-3 is right that §A's risk 6 ("changes only its Volume status and Next volume fields") is inexact.
  - A record prompt knows where to write the review copy: at the path the invocation names for it, or else it stops at the kept missing-input rule. It writes each proof log beside its file, named with `.proof-log` before `.md`.
  - REC-BLOCK agrees with the kept sentences the brief quotes ("Do not invent volumes, rollover thresholds, numbering/insertion authority", "insert into an authoritative PF", "successful creation is not source insertion"), since the output is a copy in the pull request.
  - The defect is R-1; L1 to L4 remain.
- **A2 (the gate).** AP-GATE, DC-SRC, DC-SUB and REC-FIELDS carry the ruling exactly:
  - `BN` and the PF10 version when the source is PF10;
  - a non-PF10 source's filename alone;
  - never another PF as a source;
  - "not a citation of HDE Build Notes";
  - `; ` between sources (K-3);
  - `BN 13.5` as the example (K-13), the same form as canon's `BN 12.8.9`.

  DC-SUB's ban and the handoff's "source-file header provenance" stay true, and no edit touches the fileless-source sentence. L8 remains.
- **A3 (document control and no Draft).** Every field ITEM-01 lists is carried forward:
  - the version (kept text);
  - the dates (AP-DATE; "any other control date that records this revision" is a narrower and better reading of §A's "any other date");
  - the gate (AP-GATE);
  - the change history (DC-HIST, AP-AUTH, AP-VERIFY);
  - version-sensitive restatements (AP-REF);
  - agreement among them (AP-AGREE, AP-VERIFY);
  - a stale status (AP-STATUS, DC-OTHER).

  K-4 is a loud stop on the plain reading, because AP-AUTH expects the change-history entry to name "the version and date this plan derives". L5 to L7 remain.
- **A4 (PF09).** PF09-JUDGE and PF09-EVID agree with the kept Done rule and the rule on unrelated rows. They also agree with HDE Build Checklist — Distillation §0.3 ("An existing PF09 status does not override contradictory current repository reality") and §0.6. No finding.
- **A5 (the selection route).** The route is sound:
  - Sending SEL-1 before SEL-2 leaves exactly one `Current operation` heading.
  - *SECTION* carries the diagram and four paragraphs.
  - In all four places the waiver says "for TW Flowmaster" and names both skills, as Nathan's Q-1 answer requires.
  - `ctl_check.py`'s headings, `--has` strings and rows match A1-NEW and HUB-NEW.
  - CAT-NEW chains onto C2's catalog text.
  - «R»'s rule gives TW-ALPHA-20261006.2 on 2026-10-06.

  L9 to L11 remain.
- **A6 (the readback and the evidence).**
  - A partial edit fails (g)(4) and (5). A misplaced edit fails (g)(4), and X1.0 (3) makes each anchor unique. Edits sent to the wrong member fail at the call.
  - D22 holds: no file the branch adds carries a body passage longer than an edit's anchor. Anchors are at most 210 characters, and the longest quote of kept body text in the record or the brief is 107.
  - L12 and L13 remain.

**Method and disclosure:**
- **Read-only commands throughout:**
  - `git show`, `log`, `rev-parse`, `ls-tree`, `grep` and `branch -a`, and `git diff --stat` between commits;
  - `grep`, `sed`, `awk`, `cut`, `head`, `tail`, `wc`, `sha256sum`, `stat` and `date`;
  - `edits_check.py` and its eleven `--inject` runs, with `PYTHONDONTWRITEBYTECODE=1`. Each exit code quoted is the script's own, read through `PIPESTATUS`.
- **No fetch:** `origin/main` as known locally is b1bd769. No Notion, Drive, GitHub, session or agent action. I wrote no file.
- **Not run:** `modification_validate.py`, `gtwpe_record_check.py` and `ctl_check.py`, which the brief does not list. `ctl_check.py pre` would also write a state file.
- **One side effect, from the harness, not my commands:** the repository's PostToolUse hook (`.claude/settings.json`, running `.claude/hooks/check_canon_relied_on.py`) runs after each Bash call and keeps its state in `.git/canon_relied_on_hook.json`. That file was modified at 2026-10-06T13:36:13Z, during this review. I saw no output that the harness saved to a file.
- **No TW prompt body and no Notion page was read** (D22; the brief). What I say about kept text rests on §A, §P, `edits.json`, the brief and earlier evidence.
- **Not exercised, as for the dry run:** any Notion write, the duplication and its polling, and how Notion renders the new texts (K-5).
- **Scope of this review:** it is the D26-A PLAN review Nathan directed, not an automated code review, so `AGENTS.md`'s line on CI-exempt paths does not apply.

## Canon relied on
- **AGENTS.md:** the canon-first rule; PF canon is read-only; evidence attribution, currentness and distinct decisions; the code-review scope line. The requirement for this block comes from ledger E-036 in `docs/ephemeral/gtwpe.rewrite/ERRORS.md`. I also read rows E-035, E-037 and E-038 there.
- **PF canon, from `docs/pfcanon/` on main at b1bd769**, searched with `git grep` for "Last Update Gate", TBD, TODO, placeholder, the status fields and change-log or Doc-Delta headings:
  - HDE CRD Records (PF30.1): §0 front matter and §1 to §6 in full; the opening of §7's record template; the record control of HDE-CRD-0001 in §8.
  - HDE Governance (PF04): §0.1; §9.1.1 and §9.1.6 in full; §9.2; §9.3 and the opening of §9.3.1; the TBD line in §9.7.7.
  - Reference Technical Writing Best Practices (PF03): front matter; §7, §14, §15.1 and §15.2 in full.
  - HDE Phased Epics (PF20): front matter and §0 in full; §1; the opening of §2; the status lines of §2.6.1; the last record headings.
  - HDE Build Notes (PF10): front matter; 2.30 PF10-CITE-001 in full; the source and rule sections of 2.29 PF10-CANON-001 and 2.38 PF10-AINEUTRAL-001.
  - HDE Build Checklist — Distillation (PF09.6): §0.1 header, §0.3, §0.5 and §0.6.
  - HDE CLI-API-Vendor Ref (PF05) §11.1, and the front matter and change log of HDE Copy Tonality Guide (PF15).
  - Plan Templates (PF27), "Template-safe placeholders and omission syntax".
  - The TBD lines of Change Process Guide (PF06) §0.6.1 and §1.1.11, of Glow QA Guide (PF19) §11.3, and of Glow Infrastructure (PF07) §2.1 and the rest of PF07 (by grep).
  - The Last Update Gate in every PF header (by grep).
- **Governing documents in `docs/prompt_ecosystem_management/`, at fd14d32, the same as main for these paths:**
  - `gcfpe.decision-record.md` D20 to D26;
  - `modification-template.md` and `ecosystem-change-management.md`, whole;
  - `gtwpe/gtwpe.decision-record.md`, GTWPE-D1;
  - `reviewer-prompt-template.md`, the second template;
  - `notion-write-boundary.md` and `prompt-body-content-policy.md`, whole;
  - outside that directory, the scope of `.claude/hooks/check_canon_relied_on.py`.
- **In flight:**
  - The record's §A and §P at fd14d32, whole; `edits.json`, `edits_check.py` and `ctl_check.py`; the brief at 3a12db1.
  - The target architecture on main: §§4, 5, 8 and 9, Nathan's answers 6 and 8, his later directions and the status updates. Nathan's gate ruling as `analyze_approved_by` quotes it.
  - C1's §A, A.1 to A.8. C2's §P steps and control texts, its successor plan and its §E.
  - The earlier edits files: `gtwpe-tw-repository-io/edits-2.json`, `gtwpe-writing-side/edits.json`, and `gtwpe-tw-model-advice/edits.json`, which I skimmed.
  - The earlier GTWPE PLAN reviews, for calibration.

IN FLIGHT: R-1 goes to repair. Then, as Nathan directed, a second reviewer or a check of the repair's diff follows, and the plan goes to him with L1 to L15 as listed findings.
