#!/usr/bin/env python3
"""Dependency closure and gate tier for one GCFPE prompt, computed from the graph parts.

The graph is the authority for routing (D13), so "what breaks if I change this prompt" is a
query rather than an investigation. ANALYZE runs this instead of naming affected surfaces in
prose: a script returns the same answer twice and a prompt does not (DERIV-001).

    python3 docs/prompt_ecosystem_management/closure.py <PROMPT_ID> [--parts DIR] [--json]

Reports, for the named prompt:

  upstream        prompts that hand TO it
  downstream      prompts it hands TO  -- prompt consumers only
  boundaries      non-prompt destinations (terminal returns); NOT consumers
  state_sharers   other prompts declaring at least one of the same result states
  radius          the set a Tier 1 gate must cover: upstream | downstream | state_sharers

Boundaries are reported separately and deliberately. A terminal return to Nathan is not a
downstream consumer, and counting it as one overstates the blast radius of every prompt in the
corpus.

Tier is NOT decided here. This gives the radius; the tier follows from whether the rebuilt graph
part actually moved -- see the redesign plan, section 3.4. Tier 0 means routing provably
unaffected, never provably harmless: a body can change what an artifact says while keeping its
state name, and the graph cannot see that.
"""
import json
import sys
from pathlib import Path

DEFAULT_PARTS = Path(__file__).resolve().parents[2] / "docs/graph/parts/prompts"


def load(parts_dir):
    """Return {prompt_id: {"to": set, "boundaries": set, "states": set}} over every part."""
    graph = {}
    for path in sorted(Path(parts_dir).glob("*.json")):
        pid = path.stem
        part = json.loads(path.read_text(encoding="utf-8"))
        to, boundaries, states = set(), set(), set()
        for edge in part.get("edges", []):
            if edge.get("from") != pid:
                continue
            dest, kind = edge.get("to"), edge.get("to_kind")
            if dest:
                (to if kind == "prompt" else boundaries).add(dest)
            states.update(edge.get("state_predicates") or [])
            for branch in edge.get("route_branches", []):
                states.update(branch.get("applicable_states") or [])
                if branch.get("state"):
                    states.add(branch["state"])
        graph[pid] = {"to": to, "boundaries": boundaries, "states": states}
    return graph


def closure(pid, graph):
    if pid not in graph:
        raise KeyError(pid)
    me = graph[pid]
    upstream = {o for o, g in graph.items() if o != pid and pid in g["to"]}
    downstream = {d for d in me["to"] if d in graph}
    sharers = {o for o, g in graph.items() if o != pid and (g["states"] & me["states"])}
    return {
        "prompt": pid,
        "upstream": sorted(upstream),
        "downstream": sorted(downstream),
        "boundaries": sorted(me["boundaries"]),
        "state_sharers": sorted(sharers),
        "states": sorted(me["states"]),
        "radius": sorted(upstream | downstream | sharers),
    }


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    parts = DEFAULT_PARTS
    if "--parts" in argv:
        parts = Path(argv[argv.index("--parts") + 1])
    if not args:
        print(__doc__.strip())
        print(f"\nknown prompts ({len(load(parts))}):")
        print("  " + "  ".join(sorted(load(parts))))
        return 2
    graph = load(parts)
    try:
        result = closure(args[0], graph)
    except KeyError:
        print(f"unknown prompt: {args[0]}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(result, indent=2))
        return 0
    print(f"{result['prompt']}  -- closure over {len(graph)} graph parts\n")
    for key in ("upstream", "downstream", "state_sharers", "boundaries"):
        label = "boundaries (NOT consumers)" if key == "boundaries" else key
        print(f"  {label:28s} {len(result[key]):3d}  {', '.join(result[key]) or '-'}")
    print(f"\n  radius a Tier 1 gate must cover: {len(result['radius'])}")
    print(f"  {', '.join(result['radius']) or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
