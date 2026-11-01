# HDE-EPIC041 doc deltas (Step-0B)

Written by check step-0b-doc-delta-capture of the HDE-EPIC041 Live QA Plan v1.0. PF documents are named by title. Every item is a non-mandatory drain candidate owned by the Product Owner; none is a QA gate or a close blocker.

## BLOCKERS

none

## CAVEATS

- DELTA-001 (CAVEAT; drives decision: No): HDE Architecture §1.1 still contains the text "The checked-in loader remains current repository reality until separately remediated", which describes the removed chart loader as current. Drain target: HDE Architecture §1.1, owner Product Owner, after all QA tasks are complete.
- DELTA-002 (CAVEAT; drives decision: No): HDE Mechanics Guide §1.1 still contains the text "The non-BodyGraph loader responsibility represented by", which describes the removed chart loader as current. Drain target: HDE Mechanics Guide §1.1, owner Product Owner, after all QA tasks are complete.
- DELTA-003 (CAVEAT; drives decision: No): HDE State of the Repository §2.2 still contains the text "still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging", which describes the removed chart loader as current. Drain target: HDE State of the Repository §2.2, owner Product Owner, after all QA tasks are complete. This item is a candidate; HDE State of the Repository is a reference document.
