"""E2 step 3 (spec v2 §4.3 G16, §4.9 steps 3-4, §5.11 step 4).

usage: PYTHONDONTWRITEBYTECODE=1 python3 g16_graph.py <repo> <skills-root> <scratch-dir>

1. Builds the commit-1 parts to scratch and records bytes/sha256 (expected 575074 B, 716c4cfc...).
2. Writes the successor oracle's sha256 into docs/graph/parts/global.json protected_identities.r1_oracle_sha256
   (repository working tree; scripted, §4.1 serialization), and checks that only that path changed.
3. Builds the final parts to scratch, checks 55/229/55 and routing surface fecc319b.../284.
4. Writes the embedded JSON + LF to both skills' bundled candidate-graph copies.
"""
import copy, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
repo, skills, scratch = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
scratch.mkdir(parents=True, exist_ok=True)
GLOBAL = repo / "docs/graph/parts/global.json"
BUILDER = skills / "glow-graph-contract/scripts/graph_parts.py"
ORACLE = skills / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json"
HIST = "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"
COMMIT1_GLOBAL = "ef4abb9cda68a9b75495036981903c76e822d6926421eb754ff0e0067f5dda60"
BUNDLED = ("change-flow/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json",
           "flowmaster-validate/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json")

sys.path.insert(0, str(skills / "flowmaster-validate/scripts"))
spec = importlib.util.spec_from_file_location("fv", skills / "flowmaster-validate/scripts/validate_gcfpe_20260914.py")
fv = importlib.util.module_from_spec(spec); spec.loader.exec_module(fv)


def build(tag):
    out = scratch / f"graph_{tag}.md"
    r = subprocess.run([sys.executable, str(BUILDER), "build", str(repo / "docs/graph/parts"), str(out)],
                       capture_output=True, text=True)
    assert r.returncode == 0 and "WARNING" not in r.stdout + r.stderr, r.stdout + r.stderr
    lines = out.read_text(encoding="utf-8").split("\n")
    s = lines.index("```json")
    e = max(i for i, l in enumerate(lines) if l == "```")
    emb = ("\n".join(lines[s + 1:e]) + "\n").encode("utf-8")
    g = json.loads(emb)
    info = {"builder": r.stdout.strip(), "nodes": len(g["nodes"]), "edges": len(g["edges"]),
            "state_routes": len(g["state_routes"]), "bytes": len(emb), "sha256": hashlib.sha256(emb).hexdigest(),
            "routing_surface": list(fv.routing_surface({"route_edges": g["edges"], "state_routes": g["state_routes"]}))}
    return emb, g, info


before_bytes = GLOBAL.read_bytes()
oracle_sha = hashlib.sha256(ORACLE.read_bytes()).hexdigest()
if hashlib.sha256(before_bytes).hexdigest() == COMMIT1_GLOBAL:
    _, _, c1 = build("commit1")
    print("commit-1 build:", json.dumps(c1))
    obj = json.loads(before_bytes)
    old = copy.deepcopy(obj)
    assert obj["protected_identities"]["r1_oracle_sha256"] == HIST
    obj["protected_identities"]["r1_oracle_sha256"] = oracle_sha
    new_bytes = (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    assert (json.dumps(old, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8") == before_bytes
    GLOBAL.write_bytes(new_bytes)
else:
    obj = json.loads(before_bytes)
    assert obj["protected_identities"]["r1_oracle_sha256"] == oracle_sha, "global.json is neither commit-1 nor G16"
    new_bytes = before_bytes
diff_lines = [(a, b) for a, b in zip(before_bytes.decode().split("\n"), new_bytes.decode().split("\n")) if a != b]
print("global.json:", len(new_bytes), "B sha256", hashlib.sha256(new_bytes).hexdigest(), "changed lines:", diff_lines)
emb, g, fin = build("final")
print("final build:", json.dumps(fin))
assert (fin["nodes"], fin["edges"], fin["state_routes"]) == (55, 229, 55)
assert fin["routing_surface"] == ["fecc319bdd4ce7ee6201cb77d7231861", 284]
assert g["protected_identities"]["r1_oracle_sha256"] == oracle_sha
for rel in BUNDLED:
    (skills / rel).write_bytes(emb)
(scratch / "graph_final.json").write_bytes(emb)
print("bundled both copies:", len(emb), hashlib.sha256(emb).hexdigest())
