# Focused post-flight brief — MB-008, AM-2's operations

Committed before either reviewer is spawned. Nathan's decision 2 after X13 (record §E, *Nathan's decisions after
X13*): amendment AM-2, "then two fresh reviewers run the post-flight on only the changed operations". Method,
independence and verdict set are `docs/prompt_ecosystem_management/postflight-procedure.md`'s. Two fresh-context
reviewer subagents receive the fenced prompt as their only brief: `REVIEWER-POSTFLIGHT-C` writes
`execute/REVIEW-POSTFLIGHT-C.md`, `REVIEWER-POSTFLIGHT-D` writes `execute/REVIEW-POSTFLIGHT-D.md`, each under this
directory.

```plain text
You are <REVIEWER_ID>, running a focused independent post-flight of the GCFPE-20261009.1 / 100926.1 release for
MODIFICATION-20261011-gcfpe-mb008-to-promotion. You did not author it; you are not one of its D24 reviewers and not
one of its first two post-flight reviewers. You are read-only: you repair nothing, install nothing, merge nothing,
promote nothing, and write to Notion nothing.

=== 1. WHAT GOVERNS YOU ===
Repository /home/user/glow-hdengine-v2, branch claude/mb-008-modification-promotion-fdz2sn (draft PR #606, NOT
MERGED; it was restarted from main after PR #605 merged). Read its HEAD. Read AGENTS.md first; it governs. Canon is
docs/pfcanon/ on main; search it for the terms you audit and read what governs. Then read in full:
  docs/prompt_ecosystem_management/postflight-procedure.md (method, verdict set, D22 corpus rule)
  docs/prompt_ecosystem_management/gcfpe.decision-record.md D24 and D26-A
  the record docs/ephemeral/modifications/MODIFICATION-20261011-gcfpe-mb008-to-promotion.md: §E rows X10 and X13, the
    *Failure record*, the *Return to Nathan — 2026-10-12, after X13*, and *Nathan's decisions after X13*
  execute/REVIEW-POSTFLIGHT-A.md and -B.md (the first post-flight, FAIL on one finding: F-1 / PFB-M1)
  execute/REVIEW-D24-A.md, -B.md, -C.md, -D.md (the D24 records the amended text must describe truly)
  plan/activation-ops.json (its `amendment` key and `markers`) and `git diff d86b885 -- plan/` for AM-2's exact change

=== 2. YOUR SCOPE: ONLY AM-2'S OPERATIONS ===
Nathan limited this post-flight to the changed operations. Everything else the first post-flight checked passed and
is not re-audited. The changed operations are:
  FI-B-SKILL and FI-PEV-2 (Flow Index, X15(c)): now cite @D24_RECORDS;
  FI-PEV-1 (Flow Index, X15(c)): now "@POSTFLIGHT_VERDICT; no mandatory open finding";
  REG-SEL (register, X16): predicate 1 cites execute/x11-registry.json; predicate 2 is "@POSTFLIGHT_VERDICT; no
    mandatory open finding."; the D24 sentence cites @D24_RECORDS;
  the new catalog's frontmatter line validation_evidence (activation_render.py, X15(a)).
The question is the first post-flight's: is any of this text false at some moment of X15–X22 or after it, does it
assert what the evidence will not support, or does it silently breach a Product Owner ruling? Above all: is F-1 /
PFB-M1 corrected, and did AM-2 add a defect of the same kind?

=== 3. WHAT TO RUN ===
  a. In your session, fetch with the Notion fetch tool the nine control pages: 3f44590a05eb81f98b76c83465dc1960 (PE),
     3db4590a05eb81de9736ea69bac61016 (Flow Index), 3db4590a05eb81d59059eb6b95ed5fcf, 3db4590a05eb8195a2ccf7c0959a8b6e,
     3db4590a05eb814d96d3dcfa8835f96d, 3db4590a05eb81cd938de84cfffead9c, 3db4590a05eb811b9c14f2ae89c28df7 (hubs),
     3db4590a05eb812f87caed515836687f (Alpha checklist), 3d24590a05eb81ce942ad994cfca9fa1 (register). Take a UTC time
     with milliseconds just before you fetch.
  b. From the repository root, render the activation twice with the pins below: once with the marker values Nathan
     will see at X14 (the INTENDED values below), once without --pages to render the two new pages. Read each changed
     operation's rendered text with --emit in your terminal; never redirect --emit output into the repository.
       python3 docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/activation_render.py plan
         --parts docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/candidate-graph-parts
         --pages <the nine ids above> --fetched-after <your time> [--emit]
         --set @MGMT10_PAGE_ID=3f74590a05eb81b69bd8c27106f7a59d
         --set "@PRODUCTION_TOKEN=55 nodes · 235 edges · 55 state_routes · 593,569 bytes · sha256 43f84f29…"
         --set @ACTIVATION_DATE=2026-10-13 --set @PROMOTION_APPROVED_AT=2026-10-13
         --set @CATALOG_PAGE_ID=00000000000000000000000000000000 --set @REGISTER_ENTRY_PAGE_ID=ffffffffffffffffffffffffffffffff
         --set "@D24_RECORDS=<INTENDED D24 value>" --set "@POSTFLIGHT_VERDICT=<INTENDED post-flight value>"
         --pin 3f44590a05eb81f98b76c83465dc1960=2026-10-12T02:30:10.895Z --pin 3db4590a05eb81d59059eb6b95ed5fcf=2026-10-12T02:29:57.710Z
         --pin 3db4590a05eb8195a2ccf7c0959a8b6e=2026-10-12T02:30:54.130Z --pin 3db4590a05eb814d96d3dcfa8835f96d=2026-10-12T02:30:51.327Z
         --pin 3db4590a05eb81cd938de84cfffead9c=2026-10-12T02:29:51.552Z --pin 3db4590a05eb811b9c14f2ae89c28df7=2026-10-12T02:30:10.895Z
         --pin 3db4590a05eb81de9736ea69bac61016=2026-10-12T02:34:11.699Z
     The rendering without --pages also tries the candidate inventory, whose three operations landed at X6a; its row
     fails for that reason alone. Read new_pages there.
     INTENDED D24 value (known now):
       `docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/REVIEW-D24-C.md` (`SKILL_FIT_CONFIRMED`) and `REVIEW-D24-D.md` (`SKILL_REPAIR_REQUIRED`; its one required finding, D-1, accepted by Nathan / Product Owner as a listed risk on 2026-10-12), on the six round-2 packages
     INTENDED post-flight value (your verdicts are not yet known; the brackets are filled at X14):
       `docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/REVIEW-POSTFLIGHT-A.md` and `REVIEW-POSTFLIGHT-B.md`: `FAIL`, each on one mandatory finding, which amendment AM-2 corrected; `REVIEW-POSTFLIGHT-C.md`: `[C's verdict]` and `REVIEW-POSTFLIGHT-D.md`: `[D's verdict]`, on AM-2's operations
     Pins: PE's and the hubs' are their revisions read after X6a (execute/x13-pins.json); the Flow Index's is a stand-in,
     since its X15 pin is read right after X15(a); the Alpha checklist's and the register's come from activation-ops.json.
     A page whose revision no longer matches its pin is a finding to report, not something to work around.
  c. Read the `ok` flag and each page's revision_matches_pin, refused, batch_safe and findings_after.

=== 4. KNOWN LIMITS ===
L1. The activation is reviewed as rendered operations on your reads, not as final bytes (PLAN §10 P-L2).
L2. Stand-in values (dates, the two page ids X15 creates, your own verdicts in the post-flight value) are not findings.
L3. LISTED findings of the earlier records stay listed (D26-A rule 4); restating one is not a new finding.
L4. PLAN-20261011.md is not edited by AM-2: the contracts and validators pin it by digest. §E records why.
L5. No prompt body is in scope. If you read one, D22 binds you: transient, outside the repository, deleted, disclosed.

=== 5. THE DELIVERABLE ===
Write your record to docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/<RECORD_FILE>.
First line: the verdict, exactly one of PASS, PASS WITH WARNINGS, FAIL, INDETERMINATE, and the count of mandatory open
findings. A finding is mandatory when the amended text as specified would write a false or unsupported statement, or
silently breach a Product Owner ruling, or stops the flow. For each finding: the operation, the exact defect, the
evidence as a quoted clause, the smallest correction, and whether it stops the flow or merely offends the record.
State the disposition of F-1 / PFB-M1 (corrected, not corrected, corrected with a new defect). State which checks you
ran and which you could not. End with a "Canon relied on" line (AGENTS.md).
Do not edit any other file, commit, push, merge, install, write to Notion, or edit a prompt body or skill.
Put your answer first and close with DECISION NEEDED, NOTHING NEEDED, or IN FLIGHT.
```
