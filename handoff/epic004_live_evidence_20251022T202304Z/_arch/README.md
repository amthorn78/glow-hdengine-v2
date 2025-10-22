# _arch snapshot bundle

This folder stores timestamped architecture snapshots per epic:
- routes.txt — mechanical scrape of route registrations (adapter/)
- imports.*.txt — forbidden import scans (adapters/, core/, server/)
- emit.dumps.txt — ad-hoc emitter usage in handlers/CLI
- tree.txt — compact directory tree
- status.txt — PASS/FAIL summary
- ARCHITECTURE_MAP_AFTER.md — copy of human-readable map (if present)

Run at any time:
  EPIC_ID=<epic-id> scripts/architecture_capture.sh
