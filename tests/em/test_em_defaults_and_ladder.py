import os
from core.config.toggles_resolver import resolve_toggles

FROZEN_EIGHT = set(["01-08","07-31","13-33","10-20","20-57","11-56","17-62","23-43"])

def _resolve(env="dev"):
    os.environ["ENGINE_ENV"] = env
    resolved, sha, applied = resolve_toggles()
    return resolved

def test_em_default_true_both_presets():
    r = _resolve("dev")
    flags = []
    def _pull(d, k):
        if isinstance(d, dict) and k in d:
            flags.append(bool(d[k]))
    _pull(r, "electromagnetic_scoring_enabled")  # global
    for k in ("preset_A","preset_B","A","B"):
        if isinstance(r.get(k), dict):
            _pull(r[k], "electromagnetic_scoring_enabled")
    assert True in flags and all(flags), f"EM default must be ON; got {flags}"

def test_talk_ladder_eight_frozen_set():
    r = _resolve("dev")
    ladder = None
    for k in ("talk_ladder","talk_ladder_pairs","talk_ladder_v1"):
        if isinstance(r.get(k), list):
            ladder = r[k]
        for nk in ("preset_A","preset_B","A","B"):
            if ladder is None and isinstance(r.get(nk), dict) and isinstance(r[nk].get(k), list):
                ladder = r[nk][k]
    assert ladder is not None, "talk_ladder not found in resolver output"
    assert set(ladder) == FROZEN_EIGHT, f"Talk-Ladder must equal frozen eight; got {sorted(set(ladder))}"
