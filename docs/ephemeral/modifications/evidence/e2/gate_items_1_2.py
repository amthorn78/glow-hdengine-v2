"""§9 items 1-2 on the E2 scratch tree, plus the §5.12 residual-hit greps.
usage: PYTHONDONTWRITEBYTECODE=1 python3 gate_items_1_2.py <skills-root> <repo>"""
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path
sys.dont_write_bytecode = True
K, REPO = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(K / "flowmaster-validate/scripts"))
import validate_gcfpe_20260914 as V  # noqa: E402
out = Path(tempfile.mkdtemp(dir="/tmp/claude-0/e2/tmp")) / "graph.md"
r = subprocess.run([sys.executable, str(K / "glow-graph-contract/scripts/graph_parts.py"), "build",
                    str(REPO / "docs/graph/parts"), str(out)], capture_output=True, text=True)
print("item1 builder:", r.returncode, " | ".join(l.strip() for l in r.stdout.splitlines()), "WARNING" in r.stdout + r.stderr)
lines = out.read_text(encoding="utf-8").split("\n")
s = lines.index("```json"); e = max(i for i, l in enumerate(lines) if l == "```")
emb = ("\n".join(lines[s + 1:e]) + "\n").encode("utf-8")
g = json.loads(emb)
print("item1 counts:", len(g["nodes"]), len(g["edges"]), len(g["state_routes"]), "bytes", len(emb), hashlib.sha256(emb).hexdigest())
for rel in ("change-flow", "flowmaster-validate"):
    b = (K / rel / "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json").read_bytes()
    print("item1 bundled", rel, "byte-identical:", b == emb)
for rel in ("change-flow", "flowmaster-validate"):
    c = json.loads((K / rel / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
    print("item2", rel, "validate_graph_contract:", V.validate_graph_contract(c, g), "validate_contract:", V.validate_contract(c),
          "routing_surface:", V.routing_surface(c))
def grep(args):
    r = subprocess.run(["grep", "-rn", *args], capture_output=True, text=True)
    return [l.split(":", 2)[0] + ":" + l.split(":", 2)[1] for l in r.stdout.splitlines()]
hits = grep(["-e", "52807e58", "-e", "5574666e", str(K / "flowmaster-validate"), str(K / "change-flow"), str(REPO / "docs/graph/parts")])
print("5.12 digest hits (%d):" % len(hits)); [print("  ", h.replace(str(K) + "/", "")) for h in hits]
hits = grep(["GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1", str(K / "flowmaster-validate"), str(K / "change-flow")])
print("5.12 old-profile hits (%d):" % len(hits)); [print("  ", h.replace(str(K) + "/", "")) for h in hits]
