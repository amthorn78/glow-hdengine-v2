#!/usr/bin/env python3
"""Generate PROPOSAL.md's figure blocks from the run output, or check them against it.

    render.py (--write | --check)

The proposal's figures all come from `pf10_dependency.proposal.json`, which is landed beside it.
The claim inventory flagged forty of them, correctly: a figure copied out of a JSON file by hand is
a figure nothing recomputes, which is the defect this whole round has been about.  So the mechanical
blocks are marker-delimited and emitted from the JSON, and `--check` fails if they drift.

Argument figures in the prose -- the individual confidences quoted while reasoning about a row --
are not generated.  They are accounted for individually in the claim inventory's allow-list, each
naming the row it came from, because a sentence making a case is not a table.
"""
import argparse
import collections
import json
import pathlib
import re
import sys

sys.dont_write_bytecode = True

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "pf10_dependency.proposal.json"
DOC = HERE / "PROPOSAL.md"


def blocks(d: dict) -> dict[str, str]:
    R = d["results"]
    tally = collections.Counter(r["choice"] for r in R.values())
    bands = collections.Counter(r["band"] for r in R.values())
    need = [(k, v) for k, v in sorted(R.items()) if v["band"] != "CLEAR"]
    usage = d["usage"]
    run = [
        "| | |",
        "|---|---|",
        # No default.  A hard-coded `jev-1.13.0` published an identity nothing had read; an
        # absent value renders as unknown, which is what it is.
        f'| model requested / served | `{d["model_requested"]}` / '
        f'{"`" + d["model_served"] + "`" if d.get("model_served") else "**unknown — not captured**"} |',
        f'| rows classified | **{len(R)}** of {d.get("rows_available", len(R))}, '
        f'every `state_routes` row |',
        f'| contract classified | `{d["contract"]["sha256"]}` |',
        f'| blocking states, from the briefs | {", ".join(f"`{x}`" for x in d["blocking_states"])} |',
        f'| options | {", ".join(f"`{o}`" for o in d["pre_registered"]["options"])} |',
        f'| bands, fixed before the run | `CLEAR` ≥ {d["pre_registered"]["clear_at"]} · '
        f'`UNCERTAIN` {d["pre_registered"]["uncertain_at"]}–{d["pre_registered"]["clear_at"]} · '
        f'`UNRESOLVED` < {d["pre_registered"]["uncertain_at"]} |',
        f'| embedded controls | **{d["controls_correct"]}/{d["controls_total"]} correct**, '
        f'{d["pre_registered"]["controls_per_batch"]} per batch, including both paraphrase controls |',
        f'| tokens | {usage["input_tokens"]:,} in / {usage["output_tokens"]:,} out |',
    ]
    result = ["| label | rows |", "|---|---|"] + [
        f"| `{lab}` | {tally[lab]} |" for lab in
        sorted(tally, key=lambda x: (-tally[x], x))
    ] + ["",
         f'**{bands["CLEAR"]} `CLEAR`, {bands["UNCERTAIN"]} `UNCERTAIN`, '
         f'{bands["UNRESOLVED"]} `UNRESOLVED`.**']
    terminal_need = [(k, v) for k, v in need if v["terminal"]]
    reading = [
        f'Of the **{len(need)}** rows outside the `CLEAR` band, **{len(terminal_need)}** are terminal: '
        + ", ".join(f'`{k}` ({v["choice"]}, {v["confidence"]:.2f})' for k, v in terminal_need) + ".",
        "",
        "| row | proposed | conf | terminal | lexical | condition |",
        "|---|---|---|---|---|---|",
    ] + [
        f'| `{k}` | {v["choice"]} | {v["confidence"]:.2f} | {"yes" if v["terminal"] else "no"} '
        f'| {v["lexical"]} | {v["condition"][:95].replace("|", chr(92) + "|")}… |'
        for k, v in need
    ] + ["", f'The other {bands["CLEAR"]} are `CLEAR`. Full per-row output, with every probability '
             f'distribution, is in `{DATA.name}` beside this file.']
    return {"run": "\n".join(run), "result": "\n".join(result), "reading": "\n".join(reading),
            "reproducibility": reproducibility(d)}


def reproducibility(_d: dict) -> str:
    """Compare every retained run, from the retained files.

    The two-run claim was prose while only the later JSON survived, so a reviewer could not check
    the comparison the conclusion rested on. Every run is retained now and this block is derived
    from those files, so the claim and its evidence cannot drift apart.
    """
    runs = sorted((HERE / "runs").glob("*.json"))
    if len(runs) < 2:
        return ("Only one run is retained, so no reproducibility comparison is made. "
                f"Retained: {[r.name for r in runs] or 'none'}.")
    loaded = [(r.name, json.loads(r.read_text(encoding="utf-8"))) for r in runs]
    lines = ["| retained run | served | contract | controls | labels | bands |",
             "|---|---|---|---|---|---|"]
    for name, d in loaded:
        R = d["results"]
        lab = collections.Counter(v["choice"] for v in R.values())
        bnd = collections.Counter(v["band"] for v in R.values())
        lines.append(
            f'| `{name}` | `{d["model_served"]}` | `{d["contract"]["sha256"][:12]}…` '
            f'| {d["controls_correct"]}/{d["controls_total"]} '
            f'| {" / ".join(str(lab[k]) for k in ("NONE", "READ_ONLY", "COMPARISON", "SOURCE_AVAILABILITY"))} '
            f'| {" / ".join(str(bnd[k]) for k in ("CLEAR", "UNCERTAIN", "UNRESOLVED"))} |')
    a, b = loaded[0][1]["results"], loaded[-1][1]["results"]
    keys = sorted(set(a) & set(b))
    same_label = sum(1 for k in keys if a[k]["choice"] == b[k]["choice"])
    same_band = sum(1 for k in keys if a[k]["band"] == b[k]["band"])
    moved = [k for k in keys if a[k]["band"] != b[k]["band"]]
    worst = max(keys, key=lambda k: abs(a[k]["confidence"] - b[k]["confidence"]))
    cmp_a = sorted(k for k in a if a[k]["choice"] == "COMPARISON")
    cmp_b = sorted(k for k in b if b[k]["choice"] == "COMPARISON")
    lines += [
        "",
        f'Label columns are `NONE / READ_ONLY / COMPARISON / SOURCE_AVAILABILITY`; band columns are '
        f'`CLEAR / UNCERTAIN / UNRESOLVED`. Comparing the first and last retained runs over '
        f'{len(keys)} shared rows:',
        "",
        f'- **identical label: {same_label} of {len(keys)}**',
        f'- identical band: {same_band} of {len(keys)}'
        + (f' — moved: {", ".join("`" + k + "`" for k in moved)}' if moved else ""),
        f'- largest confidence difference: **{abs(a[worst]["confidence"] - b[worst]["confidence"]):.3f}** '
        f'on `{worst}`',
        f'- the `COMPARISON` candidate set is '
        + ("**the same in both**" if cmp_a == cmp_b else f"**different**: {cmp_a} vs {cmp_b}"),
    ]
    return "\n".join(lines)


def apply(doc: str, name: str, body: str) -> str:
    o, c = f"<!-- generated: {name} -->", f"<!-- /generated: {name} -->"
    pat = re.compile(re.escape(o) + r".*?" + re.escape(c), re.S)
    if not pat.search(doc):
        raise SystemExit(f"cannot find the `{name}` block in {DOC.name}")
    return pat.sub(lambda _m: f"{o}\n{body}\n{c}", doc, count=1)


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_true")
    g.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if not DATA.is_file():
        raise SystemExit(f"{DATA.name} is absent; there is no run to render")
    d = json.loads(DATA.read_text(encoding="utf-8"))
    # A run that classified a SLICE cannot be rendered as this proposal, whose generated blocks
    # say "every `state_routes` row".  Refused rather than annotated, because the document's
    # claim is completeness.
    if d.get("complete") is False or (
            d.get("rows_available") and d["rows_classified"] != d["rows_available"]):
        raise SystemExit(f"{DATA.name} records a limited run "
                         f"({d['rows_classified']} of {d.get('rows_available')} rows); this "
                         f"proposal claims every row and will not be rendered from a slice")
    b = blocks(d)
    doc = DOC.read_text(encoding="utf-8")
    if args.write:
        for name, body in b.items():
            doc = apply(doc, name, body)
        DOC.write_text(doc, encoding="utf-8")
        print(f"PROPOSAL.md regenerated: {len(b)} blocks")
        return 0
    problems = [name for name, body in b.items() if body not in doc]
    if problems:
        print(f"PROPOSAL STALE — {len(problems)} block(s) do not match the run output: "
              f"{', '.join(problems)}")
        return 1
    print(f"PROPOSAL.md agrees with the run output: {len(b)} blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
