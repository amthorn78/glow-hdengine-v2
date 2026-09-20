---
artifact_type: GCFPE_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-19
round: 17
release: GCFPE-20260914.1 / 091426.1 / 55
status: PACKAGED_AWAITING_INSTALLATION
authority: Product Owner approval, 2026-09-19
package_sha256: 51dd7b8ead7f98ec355f969af954f83499e83a38dc13228edc0991ffd2d45ed6
---

# Round 17 — D8/D15 guard v6, and `SF10-01`

Packaged, not installed. Skills live in a one-way synced directory; only the Product Owner
installs. Three files change.

## What was approved, and what was built

The approved direction was to **stop selecting a subset**. Five guards had each pinned a
subset of the routing surface and each was defeated by moving outside it.

Two designs were built and measured, rather than one being assumed:

| Design | Attacks caught | Fixture cost |
|---|---|---|
| Whole **contract** digest | 9 of 9 | **41 of 140 fixtures broken** |
| Whole **routing surface** digest | 8 of 9 | 3 fixtures, all of which inject routing changes |

The whole-contract variant was **rejected on evidence**: it fires on every negative fixture
that mutates anything at all, including mutations with nothing to do with routing, which
destroys the fixture suite's ability to test other guards in isolation. It is also close to
redundant with the existing contract byte pins.

**v6 is the whole-routing-surface digest.** It applies no selector within `route_edges`/
`edges` and `state_routes`: every edge and every state-route entry is serialised whole, so
no vocabulary is consulted, no field is privileged, no branch shape is required, and no
container key or value type decides membership. Rows are a sorted **list**, not a set — v5's
set keyed on `(surface, from, branch-json)` let a byte-identical terminal branch be copied or
re-homed for free.

Pin: `7380cd14430777675f1e8b2cdfa4a0da`, **282 rows** (227 edges + 55 states), identical
across all four bundled contract files.

### What v6 does not cover, stated plainly

It reads `route_edges`/`edges` and `state_routes` and nothing else. Routing declared in
another contract key — `route_graph`, `terminal_contract` — does **not** move this digest.
That residue is covered by the contract byte pins, which no contract edit can evade. The
guard's comment says exactly this. It claims to detect **change, not intent**, and nothing
more; it cannot judge whether a routing change is lawful.

## D14 — injected regressions, all fired

| Regression | Result |
|---|---|
| A-02 string-typed handoff count | FIRED |
| A-03 selector fields absent | FIRED |
| A-04 selector fields null | FIRED |
| A-05 gate on the edge object | FIRED |
| A-06 alternate container key | FIRED |
| A-13 consistent across both surfaces | FIRED |
| A-14 re-homed terminal branch | FIRED |
| Reword of an existing non-terminal branch | FIRED |
| A-12 `route_graph` | not fired — outside this pin by design, covered by byte pins |

## `SF10-01`

The prompt-identity URL check now compares **page identity** rather than a literal line:
the 32-hex page id is extracted whether the line is a bare URL or a `<mention-page>`
rendering, and the `?pvs=204` query is not treated as identity. Exactly-one-URL-line, the
correct `Candidate `/`Selected ` prefix, and position within the first twelve lines are all
preserved.

Proven against the live PR-40 body: installed returns `False`, packaged returns `True`.

## Fixture change

Three fixtures now declare an expected error **set** instead of a single code:
`reject-pr30-direct-pr40`, `reject-pr35-direct-pr40`, `reject-pr50-prompt-inbound`. Each
appends an edge to `route_edges`, so each legitimately trips the routing pin as well. This
uses the mechanism the harness already documents — *"the exact set of codes when a single
injected defect is legitimately caught by more than one independent check"* — and comparison
stays exact-equality, not containment. The fixtures live in the runner script, so
`EXPECTED_FIXTURE_SHA256` is unaffected.

## Gates from the packaged tree, each read from the tool's own top-level flag

| Tool | Flag | Result |
|---|---|---|
| `change-flow/validate_gcfpe_20260914.py` | process exit + PASS line | PASS, exit 0 |
| `flowmaster-validate/validate_gcfpe_20260914.py` | `ok` | `true`, `errors: []` |
| `run_gcfpe_20260914_fixtures.py` | `fixture_suite_ok` | `true`, 140 cases, 0 failing |
| `validate_flowmaster.py` | `suite_ok` / `verdict` | `true` / `FLOWMASTER_SUITE_PASS`, all counts 0 |

## Files changed — three

| File | sha256 (first 16) |
|---|---|
| `change-flow/scripts/validate_gcfpe_20260914.py` | `2fdb690ae0aa7cb8` |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `bdaa21e9757f368d` |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `e3607d1b4efafc17` |

## On installation

The new pin must be re-stamped by the installer, and §10 requires the dedicated skill review
to be **re-run against the final installed snapshot**. Round 17 does not close the gate; it
supplies the artifact the ninth review will judge.

§10 also requires an approved skill edit to be made with `skill-creator`. These edits were
authored as working copies against a frozen tree because this session cannot install; that
requirement applies at the point of installation and commit.
