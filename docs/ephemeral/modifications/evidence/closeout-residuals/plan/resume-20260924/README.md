# PLAN resumed under D26 — evidence, 2026-09-24

Evidence for the §P successor in
`docs/ephemeral/modifications/MODIFICATION-20260923-closeout-residuals.md` (*Successor, 2026-09-24 — the plan resumed
under D26*). No prompt body is stored here (`D22`): counts, ids, states and hashes only.

| file | what | how it was made |
|---|---|---|
| `dryrun-summary.json` | the `D26-A` dry run: X0.3–X4.3 and X6.3 on a scratch clone of `main` `d179277`; X3.6's NAM-002 on the six live hubs; X4.5's rehearsal per body; X4.6's Drive and anchor checks; X6.2 in `--simulate` mode; the text results on the new base | the plan's own tools (`EV/engine/`, `EV/registry/`, `EV/skills/`, `EV/texts/`), run read-only from this session's scratchpad; the per-body lines were run by four read-only workers through a wrapper that calls `land.py` with the patched registry and `$PKG` |
| `control-edits.json` | the control-page edits EXECUTE uses from X4.6 on: `EV/notion/edits.json` less `PART-11-TRACK-01`, the five stop-path edits and, under DN-8 (A), `TRACK-STATUS-01` to `03` — 15 of 24, each entry byte-for-byte as in `EV/notion/edits.json` | filtered by id from `EV/notion/edits.json`; `ctrl.py all --expect unlanded --edits control-edits.json` passes on the pages fetched in the dry run |
