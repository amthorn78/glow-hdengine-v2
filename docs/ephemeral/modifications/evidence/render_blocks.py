#!/usr/bin/env python3
"""Render raw_findings.json into markdown blocks, one per finding, with nothing escaped or cut.
Values that may hold regexes or code go in fenced blocks, so a copied value is byte-exact.
Usage: render_blocks.py raw_findings.json > evidence.md"""
import json, sys

data = json.load(open(sys.argv[1]))


def fence(label, text):
    text = str(text)
    ticks = "````" if "```" in text else "```"
    return f"- **{label}**\n\n{ticks}text\n{text}\n{ticks}\n"


READERS = [("fv-main", "flowmaster-validate main validator"),
           ("fv-rest", "rest of flowmaster-validate, and change-flow"),
           ("pr-relay-graph", "PR skill, relay, graph skill and graph parts"),
           ("registry-audit", "registry and governance-audit skill")]
CRITICS = [("sweep", "completeness sweep"), ("coverage", "coverage audit"),
           ("adversary", "adversarial test of the amendment draft")]

print("## Part 1 — preflight readers (workflow wf_c18f4ad8-bae)\n")
for key, title in READERS:
    rows = [(k, v) for k, v in data["preflight"].items() if k.split(":")[0] == key]
    rows.sort(key=lambda kv: int(kv[0].split(":")[1]))
    print(f"### {key} — {title} ({len(rows)} findings)\n")
    for k, d in rows:
        print(f"#### `{k}` — {d['effect']} — step {d['plan_step']} ({d['part']})\n")
        print(f"- **Check or surface:** {d['check_or_surface']}")
        print(f"- **Location:** {d['location']}\n")
        print(fence("Asserts", d["asserts"]))
        print(fence("Required plan step", d["missing_plan_step"] or "none"))
        print(fence("Invariant", d["invariant_note"]))
    notes = data["preflight_notes"].get(key, {})
    for nk, nt in (("tooling", "Tooling"), ("live_window_risks", "Live-window risks"), ("notes", "Notes")):
        if notes.get(nk):
            print(f"#### {key} — {nt}\n")
            for x in notes[nk]:
                print(fence("item", x))

print("\n## Part 2 — critics of the amendment draft (workflow wf_d3847211-6a7)\n")
print("The first run's critic was interrupted by a user interrupt and returned nothing. These three "
      "ran afterwards against the first draft of Amendment 1.\n")
for key, title in CRITICS:
    rows = [(k, v) for k, v in data["critic"].items() if k.split(":")[0] == key]
    rows.sort(key=lambda kv: int(kv[0].split(":")[1]))
    print(f"### {key} — {title} ({len(rows)} findings)\n")
    for k, f in rows:
        print(f"#### `{k}` — {f['severity']} — {f['target']}\n")
        print(f"- **Location:** {f['location']}\n")
        print(fence("Evidence", f["evidence"]))
        print(fence("Problem", f["problem"]))
        print(fence("Fix", f["fix"]))
