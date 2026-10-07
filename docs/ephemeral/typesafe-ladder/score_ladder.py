#!/usr/bin/env python3
"""Score session or job descriptions with TypeSafe (systemone, jev-1.13.0) using request v7
(Glow app and repository sessions) or hd-v2 (Human Design report-production jobs), and apply
the pre-registered rule. Standard library only.

The ladder: each model, Opus 5.5 and Fable 5.1, runs at five effort levels (low, medium, high,
extra high, max), each with the many-agent workflow setting (ultracode) off or on: ten rungs
per model, twenty cells in all. One request asks three independent questions:
  effort     Score over the five levels
  ultracode  Noul: should the work run with independent agents (ultracode on)?
  model      Choice: most_capable_model (Fable 5.1) or strong_lower_cost_model (Opus 5.5)
Rule (pre-registered): level = nearest to the effort score, exact halves up (cuts 0.5, 1.5,
2.5, 3.5); ultracode on when P(yes) >= 0.5; model = Fable 5.1 when P(most capable) >= 0.5,
else Opus 5.5; cell = model at level, plus "with ultracode" when on.
Recorded, never used by the rule: every probability, both confidences, the ten rung
probabilities for the chosen model and all twenty cell probabilities (computed as the product
of the independent answers), and three flags: effort boundary (score within 0.10 of a cut, or
the top two levels within 0.20), ultracode near tie (P between 0.40 and 0.60), model near tie
(P between 0.40 and 0.60).

Credential: by default the script sends no Authorization header and reads no environment
values; the environment's proxy attaches the credential for api.typesafe.ai (the Glow app and
glow-hdengine-v2 environments). With --key-from-env it reads TYPESAFE_API_KEY once, removes it
from the environment, sends it only to api.typesafe.ai as a Bearer header and redacts it from any
error text (the HD Reader environment). The version is taken from the request file, whose SHA-256
must match the pin below, or nothing is sent.
"""
import argparse, hashlib, json, math, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

LEVELS = ["low", "medium", "high", "extra high", "max"]
CUTS = (0.5, 1.5, 2.5, 3.5)
MODELS = {"most_capable_model": "Fable 5.1", "strong_lower_cost_model": "Opus 5.5"}
URL = "https://api.typesafe.ai/v1/systemone"
HERE = Path(__file__).resolve().parent
PINS = {  # request file name -> (version, SHA-256); a changed request is a new version
    "request-v7.json": ("v7", "834e43ea17fb0743bc12fd93cf2af2fe4ef1c89d066ecd6d59208cb8200c4dbb"),
    "request-hd-v2.json": ("hd-v2", "39709aac99baaa4a6481bd6371fca503f6c6f63706d649aea7a77df12f7b792c"),
}
_KEY = None


def redact(text):
    return text.replace(_KEY, "[REDACTED]") if _KEY else text


def send(body, timeout=120):
    headers = {"Content-Type": "application/json"}
    if _KEY:
        headers["Authorization"] = f"Bearer {_KEY}"
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=headers, method="POST")
    sent = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status, text = resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        status, text = e.code, e.read().decode(errors="replace")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        status, text = 0, f"{type(e).__name__}: {e}"
    return sent, status, round(time.time() - t0, 2), redact(text)


def rung_name(level, ultra):
    return f"{level} with ultracode" if ultra else level


def apply_rule(answers):
    eff = answers["effort"]
    score = float(eff["score"])
    probs = {LEVELS[int(k)]: float(v) for k, v in eff["probabilities"].items()}
    level = LEVELS[min(4, int(math.floor(score + 0.5)))]
    ordered = sorted(probs.items(), key=lambda kv: -kv[1])
    modal, runner = ordered[0], ordered[1]
    boundary = any(abs(score - c) < 0.10 for c in CUTS) or (modal[1] - runner[1] < 0.20)
    p_ultra = float(answers["ultracode"]["noul"])
    ultra = p_ultra >= 0.5
    mp = {MODELS[k]: float(v) for k, v in answers["model"]["probabilities"].items()}
    p_fable = mp["Fable 5.1"]
    model = "Fable 5.1" if p_fable >= 0.5 else "Opus 5.5"
    rung = rung_name(level, ultra)
    rungs = {}
    for lv in LEVELS:
        rungs[rung_name(lv, False)] = probs.get(lv, 0.0) * (1 - p_ultra)
        rungs[rung_name(lv, True)] = probs.get(lv, 0.0) * p_ultra
    cells = {f"{m} at {r}": pm * pr for m, pm in mp.items() for r, pr in rungs.items()}
    return {
        "effort_score": round(score, 2),
        "effort_confidence": round(float(eff["confidence"]), 2),
        "level_probabilities": {lv: round(probs.get(lv, 0.0), 2) for lv in LEVELS},
        "level": level, "modal_level": modal[0], "runner_up_level": runner[0],
        "effort_boundary": boundary,
        "p_ultracode": round(p_ultra, 2), "ultracode": ultra,
        "ultracode_near_tie": 0.40 <= p_ultra <= 0.60,
        "model_probabilities": {m: round(mp[m], 2) for m in ("Fable 5.1", "Opus 5.5")},
        "model_confidence": round(float(answers["model"]["confidence"]), 2),
        "model": model, "model_near_tie": 0.40 <= p_fable <= 0.60,
        "rung": rung, "cell": f"{model} at {rung}",
        "rung_probabilities": {r: round(p, 2) for r, p in rungs.items()},
        "cell_probabilities": {c: round(p, 3) for c, p in cells.items()},
    }


def load_request(request_path):
    rp = Path(request_path)
    raw = rp.read_bytes()
    if rp.name not in PINS:
        sys.exit(f"refused: {rp.name} is not a pinned request ({', '.join(PINS)})")
    version, pin = PINS[rp.name]
    digest = hashlib.sha256(raw).hexdigest()
    if digest != pin:
        sys.exit(f"refused: {rp.name} SHA-256 {digest} does not match the pin {pin}")
    return version, json.loads(raw)


def score_one(action, label, request_path, session=""):
    version, body = load_request(request_path)
    body["state"]["action"] = action
    base = {"label": label, "version": version, "session": session, "action": action}
    for attempt in (1, 2):
        sent, status, latency, text = send(body)
        if status == 200:
            break
    if status != 200:
        return dict(base, error=f"HTTP {status} after {attempt} attempt(s)", sent_utc=sent, body=redact(text)[:300])
    try:
        resp = json.loads(text)
        out = dict(base, sent_utc=sent, latency_s=latency, response_model=resp.get("model"), usage=resp.get("usage", {}))
        out.update(apply_rule(resp["answers"]))
    except (ValueError, KeyError, TypeError) as e:
        return dict(base, error=redact(f"unreadable answer ({type(e).__name__}: {e})"), sent_utc=sent, body=redact(text)[:300])
    return out


def fmt(d):
    return ", ".join(f"{k} {v:.2f}" for k, v in d.items())


def fmt3(d):
    return ", ".join(f"{k} {v:.3f}" for k, v in d.items())


def flags(r):
    f = []
    if r["effort_boundary"]:
        f.append(f"effort boundary between {r['runner_up_level']} and {r['modal_level']}")
    if r["ultracode_near_tie"]:
        f.append("ultracode near tie")
    if r["model_near_tie"]:
        f.append("model near tie")
    return f


def header(r):
    if "error" in r:
        return f"- TypeSafe {r['version']}: not read ({r['error']}, sent {r['sent_utc']}). Do not fill in a reading by hand."
    fl = flags(r)
    return (f"- **TypeSafe {r['version']}: {r['cell']}.** Effort score {r['effort_score']:.2f} "
            f"(confidence {r['effort_confidence']:.2f}): {fmt(r['level_probabilities'])}. "
            f"Ultracode P(on) {r['p_ultracode']:.2f}. Model probabilities {fmt(r['model_probabilities'])} "
            f"(confidence {r['model_confidence']:.2f}). The ten rungs, computed from the effort and ultracode answers "
            f"(the same for either model; rounded): {fmt(r['rung_probabilities'])}."
            + (f" Flags: {'; '.join(fl)}." if fl else "") + f" Sent {r['sent_utc']}. Nathan picks the cell.")


def notion_properties(r, step, session="", pick="pending", kind="live"):
    session = session or r.get("session", "")
    notes = f"Action sent ({r['version']}): {r.get('action', '')}"
    if "error" in r:
        props = {"Step": step, "Version": r["version"], "TypeSafe cell": "not read", "Nathan's pick": pick,
                 "TypeSafe detail": f"{r['version']} not read: {r['error']} (sent {r['sent_utc']}). Never fill a reading in by hand.",
                 "Rung probabilities": "not read", "Model probabilities": "not read", "Kind": kind, "Notes": notes}
        if session:
            props["Session"] = session
        return props
    fl = flags(r)
    props = {
        "Step": step, "Kind": kind, "Version": r["version"], "Notes": notes,
        "TypeSafe cell": r["cell"], "Nathan's pick": pick,
        "TypeSafe level": r["level"], "TypeSafe model": r["model"],
        "TypeSafe ultracode": "__YES__" if r["ultracode"] else "__NO__",
        "Rung probabilities": (f"effort score {r['effort_score']:.2f}, confidence {r['effort_confidence']:.2f}: "
                               f"{fmt(r['level_probabilities'])}; ultracode P(on) {r['p_ultracode']:.2f}; "
                               f"ten rungs (computed from the effort and ultracode answers, the same for either model; rounded): {fmt(r['rung_probabilities'])}"
                               + (f". Flags: {'; '.join(fl)}" if fl else "")),
        "Model probabilities": f"{fmt(r['model_probabilities'])}, confidence {r['model_confidence']:.2f}",
        "TypeSafe detail": (f"{r['version']} sent {r['sent_utc']}; HTTP 200 in {r['latency_s']} s; "
                            f"{r['usage'].get('input_tokens')} input and {r['usage'].get('output_tokens')} output tokens; "
                            f"{r['response_model']}. By rule: level {r['level']} (nearest to the effort score, halves up); "
                            f"ultracode {'on' if r['ultracode'] else 'off'} (P(on) 0.5 or more is on); model {r['model']} "
                            f"(P(most capable) 0.5 or more is Fable 5.1)." + (f" Flags: {'; '.join(fl)}." if fl else "")),
        "Model": r["response_model"],
        "Input tokens": r["usage"].get("input_tokens"), "Output tokens": r["usage"].get("output_tokens"),
        "date:Date:start": r["sent_utc"][:10], "date:Date:is_datetime": 0,
    }
    if session:
        props["Session"] = session
    return props


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--action")
    g.add_argument("--action-file")
    g.add_argument("--batch", help="JSON file: list of {label, action}")
    ap.add_argument("--request", required=True, help="request-v7.json or request-hd-v2.json (pinned)")
    ap.add_argument("--label", default="")
    ap.add_argument("--session", default="")
    ap.add_argument("--kind", default="live", help="live, acceptance or calibration")
    ap.add_argument("--key-from-env", action="store_true", help="read TYPESAFE_API_KEY (HD Reader environment only)")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    global _KEY
    if a.key_from_env:
        _KEY = os.environ.pop("TYPESAFE_API_KEY", None)
        if not _KEY:
            sys.exit("refused: --key-from-env given but TYPESAFE_API_KEY is not set")
    load_request(a.request)  # refuse before sending anything if the request is not the pinned one
    if a.batch:
        cases = json.loads(Path(a.batch).read_text())
    else:
        action = a.action if a.action is not None else Path(a.action_file).read_text().strip()
        cases = [{"label": a.label, "action": action, "session": a.session}]
    results = []
    for c in cases:
        results.append(score_one(c["action"], c.get("label", ""), a.request, c.get("session", a.session)))
        if a.out:  # written after every reading, so a later failure loses nothing already read
            Path(a.out).write_text(json.dumps(results, indent=1, ensure_ascii=False) + "\n")
    if a.markdown:
        for r in results:
            cells = "" if "error" in r else (
                "\nAll twenty cells, computed (rounded): " + fmt3(r["cell_probabilities"]) + "\n")
            print(f"### {r.get('label') or '(unlabelled)'}\n{header(r)}\n{cells}\nNotion row:\n"
                  + json.dumps(notion_properties(r, r.get("label", ""), r.get("session", ""), kind=a.kind), indent=1, ensure_ascii=False) + "\n")
    else:
        print(json.dumps(results, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
