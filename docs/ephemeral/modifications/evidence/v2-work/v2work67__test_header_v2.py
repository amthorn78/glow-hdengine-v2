import re, sys
sys.path.insert(0, "/tmp/claude-0/v2work67")
from guards_v2 import GUARDS
import texts_v2 as T
G = {g[0]: g[2] for g in GUARDS}
KEYS = {"G12": ["Prompt Version", "Prompt version"], "G13": ["Ecosystem release"], "G14": ["Set"]}
FORMS = ["{k}: X", "**{k}:** X", "**{k}**: X", "- {k}: X", "* {k}: X", "> {k}: X", "`{k}:` X",
         "| {k}: | X |", "1. {k}: X", "# {k}: X", "__{k}__: X", "_{k}:_ X"]
HEAD = "# PR-35 — Title\n\nPrompt ID: PR-35\nNotion URL: https://www.notion.so/x\n"
bad = 0
for gid, keys in KEYS.items():
    rx = re.compile(G[gid], re.M)
    for k in keys:
        hit = [f for f in FORMS if rx.search(HEAD + f.format(k=k) + "\n\n## Native purpose\n")]
        print(gid, repr(k), f"{len(hit)}/{len(FORMS)} forms caught")
        bad += len(hit) != len(FORMS)
    # window: the line at nonblank position 9 is outside
    far = "# T\n" + "".join(f"line {i}\n\n" for i in range(2, 9)) + keys[0] + ": X\n"
    near = "# T\n" + "".join(f"line {i}\n\n" for i in range(2, 8)) + keys[0] + ": X\n"
    print(gid, "8th nonblank line caught:", bool(rx.search(near)), "; 9th nonblank line caught:", bool(rx.search(far)))
    bad += (not rx.search(near)) + bool(rx.search(far))
CTRL = HEAD + "Settings: a\nSetup: b\n1. Setting up: c\n- Set up: d\n" + T.J["C-HANDOFF"] + "\n"
for gid in KEYS:
    s = bool(re.search(G[gid], CTRL, re.M)); print(gid, "silent on clean header + Settings/Setup/Setting up/Set up + C-HANDOFF:", not s); bad += s
print("HEADER FAILURES:", bad)
