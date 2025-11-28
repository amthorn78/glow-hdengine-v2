# QA directory casing normalization summary (HDE-EPIC018)

## Legacy directories discovered
- `Audit/QA/HDE-EPIC017/logs` contained EPIC017 QA evidence.

## Moves performed
- Relocated `Audit/QA/HDE-EPIC017` → `audit/qa/hde-epic017` (all subpaths already lowercase).
- Removed the empty `Audit/QA` and `Audit/` directories after the move.

## Reference updates
- Updated PF canon documents to point to the lowercase canonical QA root: `audit/qa/hde-epic017` and the generic `audit/qa/<epic-id>/...` pattern.

## Final QA evidence roots
- Canonical root: `audit/qa/`.
- Epic directories present: `audit/qa/hde-epic017/` (logs preserved).
- Prepared destination for this epic: `audit/qa/hde-epic018/logs/` (ready for new evidence).

No other legacy QA directories were found.
