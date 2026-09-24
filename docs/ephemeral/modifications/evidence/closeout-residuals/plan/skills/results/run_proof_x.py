"""Run the committed manifest's commands literally, in spec §9 order, on a fresh scratch copy of the repository.

usage: PYTHONDONTWRITEBYTECODE=1 python3 run_proof_x.py <real-repo> <proof-dir> <apply_texts.py>
Order: X1.1 execute.1.then; X1.2 mkdir; X1.3 suite_gate.pre; X2.1 texts "X2.2"; X3.1 registry.diff (+ sha256);
X3.2 execute.2; X3.3 execute.3; X3.4 texts "X3.5"; X4.1 execute.4; X4.2 suite_gate.pkg; X7.4 suite_gate.post with
$PKG standing in as $INST. Writes <proof-dir>/proof_x.json; nothing outside <proof-dir>.
"""
import json, os, shutil, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
real, proof, apply_texts = (Path(a).resolve() for a in sys.argv[1:4])
EV = "docs/ephemeral/modifications/evidence/closeout-residuals/plan"
INST = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
if proof.exists():
    shutil.rmtree(proof)
proof.mkdir(parents=True)
repo, scratch = proof / "repo", proof / "scratch"
shutil.copytree(real, repo, symlinks=True)
ex = json.load(open(repo / EV / "skills/manifest.json", encoding="utf-8"))["execute"]
PKG = scratch / "pkg-root"
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(scratch / "tmp"), "SCRATCH": str(scratch),
       "PKG": str(PKG), "GATE": str(scratch / "gate"), "EV": EV, "INST": INST,
       "GGC": str(PKG / "glow-graph-contract"), "FV": str(PKG / "flowmaster-validate"), "CF": str(PKG / "change-flow"),
       "FVI": INST + "/flowmaster-validate", "CFI": INST + "/change-flow"}
LOG = []
def sh(step, cmd, extra=None):
    r = subprocess.run(["bash", "-c", cmd], cwd=repo, capture_output=True, text=True, env={**env, **(extra or {})})
    out = (r.stdout + r.stderr).strip().split("\n")
    LOG.append({"step": step, "cmd": cmd, "exit": r.returncode, "output_head": out[:6], "output_tail": out[-3:], "output_lines": len(out)})
    print(f"[{step}] exit {r.returncode}: {cmd[:100]}", file=sys.stderr)
    return r
K2 = "2_graph_reindex_ITEM-12_repository_in_execution_PR_before_install"
K3 = "3_contract_template_move_ITEM-13_repository_in_execution_PR"
K4 = "4_contract_regeneration_PART-01_after_steps_2_3_and_the_decision_record_commit"
for c in ex["1_base_unchanged_before_applying"]["commands"]:
    sh("X0.3(b)", c)
for c in ex["1_base_unchanged_before_applying"]["then"]["commands"]:
    sh("X1.1", c)
sh("X1.2", "mkdir -p $SCRATCH/tmp $GATE")
sh("X1.3 pre", ex["suite_gate"]["pre"]["command"])
sh("X2.1 texts X2.2", f"python3 {apply_texts} . {EV}/texts/edits.json X2.2")
sh("X3.1 registry", f"git apply {EV}/registry/registry.diff && sha256sum docs/prompt_ecosystem_management/project-prompt-contract-registry.md")
for c in ex[K2]["commands"]:
    sh("X3.2", c)
for c in ex[K3]["commands"]:
    sh("X3.3", c)
sh("X3.4 texts X3.5", f"python3 {apply_texts} . {EV}/texts/edits.json X3.5")
for c in ex[K4]["commands"]:
    sh("X4.1", c)
sh("X4.2 pkg", ex["suite_gate"]["pkg"]["command"])
sh("X7.4 post ($PKG as $INST)", ex["suite_gate"]["post"]["command"], {"INST": str(PKG)})
sh("git status", "git status --short | grep -v '^??'")
json.dump(LOG, open(proof / "proof_x.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
