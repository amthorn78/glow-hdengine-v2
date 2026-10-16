#!/usr/bin/env python3
"""Score session or job descriptions with TypeSafe (systemone, jev-1.13.0) using request v8
(Glow app and repository sessions) or hd-v3 (Human Design report-production jobs), and apply
the pre-registered rule. Standard library only.

The ladder: four models, each with six rungs on its effort slider (low, medium, high,
extra high, max, ultracode), so 24 cells. One request asks two independent questions:
  effort  Score over the six rungs (v6's question for v8, hd-v1's for hd-v3, unchanged)
  model   Choice over four options (no product names in the request):
            most_capable_model         Fable 5.1
            strong_lower_cost_model    Opus 5.5
            balanced_model             Sonnet 5.5
            fastest_lowest_cost_model  Haiku 5.5
Rule (pre-registered): rung = the rung nearest the effort score, exact halves up (cuts 0.5,
1.5, 2.5, 3.5, 4.5); model = the option with the highest probability, an exact tie going to
the higher-priced model; cell = "<model> at <rung>".
Recorded, never used by the rule: every probability, both confidences, all 24 cell
probabilities (the product of the two independent answers), and two flags: boundary (score
within 0.10 of a cut, or the top two rungs within 0.20) and model near tie (the top two model
probabilities within 0.20).

Credential: by default the script sends no Authorization header and reads no environment
values; the environment's proxy attaches the credential for api.typesafe.ai (the Glow app and
glow-hdengine-v2 environments). With --key-from-env it reads TYPESAFE_API_KEY once, removes it
from the environment, sends it only to api.typesafe.ai as a Bearer header and redacts it from
any error text (the HD Reader environment). The version is taken from the request file, whose
SHA-256 must match the pin below, or nothing is sent.
"""
import argparse, hashlib, json, math, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timezone
from pathlib import Path

RUNGS = ["low", "medium", "high", "extra high", "max", "ultracode"]
CUTS = (0.5, 1.5, 2.5, 3.5, 4.5)
# Highest price first; this order breaks exact ties and orders the printed cells.
MODELS = {"most_capable_model": "Fable 5.1", "strong_lower_cost_model": "Opus 5.5",
          "balanced_model": "Sonnet 5.5", "fastest_lowest_cost_model": "Haiku 5.5"}
ORDER = list(MODELS.values())
URL = "https://api.typesafe.ai/v1/systemone"
PINS = {  # request file name -> (version, SHA-256); a changed request is a new version
    "request-v8.json": ("v8", "PIN_V8"),
    "request-hd-v3.json": ("hd-v3", "PIN_HD3"),
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


def apply_rule(answers):
    eff = answers["effort"]
    score = float(eff["score"])
    probs = {RUNGS[int(k)]: float(v) for k, v in eff["probabilities"].items()}
    rung = RUNGS[min(5, int(math.floor(score + 0.5)))]
    ordered = sorted(probs.items(), key=lambda kv: -kv[1])
    modal, runner = ordered[0], ordered[1]
    boundary = any(abs(score - c) < 0.10 for c in CUTS) or (modal[1] - runner[1] < 0.20)
    raw = answers["model"]["probabilities"]
    if set(raw) != set(MODELS):
        raise KeyError(f"model options {sorted(raw)} are not the four pinned options")
    mp = {MODELS[k]: float(v) for k, v in raw.items()}
    ranked = sorted(ORDER, key=lambda m: (-mp[m], ORDER.index(m)))
    model, model_runner = ranked[0], ranked[1]
    return {
        "score": round(score, 2),
        "effort_confidence": round(float(eff["confidence"]), 2),
        "rung_probabilities": {r: round(probs.get(r, 0.0), 2) for r in RUNGS},
        "rung": rung, "modal_rung": modal[0], "runner_up_rung": runner[0], "boundary": boundary,
        "model_probabilities": {m: round(mp[m], 2) for m in ORDER},
        "model_confidence": round(float(answers["model"]["confidence"]), 2),
        "model": model, "runner_up_model": model_runner,
        "model_near_tie": mp[model] - mp[model_runner] <= 0.20,
        "cell": f"{model} at {rung}",
        "cell_probabilities": {f"{m} at {r}": round(mp[m] * probs.get(r, 0.0), 3) for m in ORDER for r in RUNGS},
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


def fmt(d, places=2):
    return ", ".join(f"{k} {v:.{places}f}" for k, v in d.items())


def flags(r):
    f = []
    if r["boundary"]:
        f.append(f"boundary between {r['runner_up_rung']} and {r['modal_rung']}")
    if r["model_near_tie"]:
        f.append(f"model near tie between {r['model']} and {r['runner_up_model']}")
    return f


def header(r):
    if "error" in r:
        return f"- TypeSafe {r['version']}: not read ({r['error']}, sent {r['sent_utc']}). Do not fill in a reading by hand."
    fl = flags(r)
    return (f"- **TypeSafe {r['version']}: {r['cell']}.** Effort score {r['score']:.2f} "
            f"(confidence {r['effort_confidence']:.2f}); rung probabilities {fmt(r['rung_probabilities'])}. "
            f"Model probabilities {fmt(r['model_probabilities'])} (confidence {r['model_confidence']:.2f}). "
            f"Twenty-four cells, computed from the two answers: {fmt(r['cell_probabilities'], 3)}."
            + (f" Flags: {'; '.join(fl)}." if fl else "") + f" Sent {r['sent_utc']}. Nathan picks the cell.")


def notion_properties(r, step, session="", pick="pending", kind="live"):
    """The complete uses-table row for this reading; paste it verbatim, then read it back."""
    session = session or r.get("session", "")
    v = r["version"]
    notes = f"Action sent ({v}): {r.get('action', '')}"
    if "error" in r:
        props = {"Step": step, "Kind": kind, "Version": v, "TypeSafe cell": "not read", "Nathan's pick": pick,
                 "TypeSafe detail": f"{v} not read: {r['error']} (sent {r['sent_utc']}). Never fill a reading in by hand.",
                 "Rung probabilities": "not read", "Model probabilities": "not read", "Notes": notes}
    else:
        fl = flags(r)
        props = {
            "Step": step, "Kind": kind, "Version": v, "Notes": notes,
            "TypeSafe cell": r["cell"], "Nathan's pick": pick,
            "TypeSafe level": r["rung"], "TypeSafe model": r["model"],
            "TypeSafe ultracode": "__YES__" if r["rung"] == "ultracode" else "__NO__",
            "Rung probabilities": (f"score {r['score']:.2f}, confidence {r['effort_confidence']:.2f}: {fmt(r['rung_probabilities'])}; "
                                   f"twenty-four cells (computed): {fmt(r['cell_probabilities'], 3)}"
                                   + (f". Flags: {'; '.join(fl)}" if fl else "")),
            "Model probabilities": f"{fmt(r['model_probabilities'])}, confidence {r['model_confidence']:.2f}",
            "TypeSafe detail": (f"{v} sent {r['sent_utc']}; HTTP 200 in {r['latency_s']} s; {r['usage'].get('input_tokens')} input and "
                                f"{r['usage'].get('output_tokens')} output tokens; {r['response_model']}. Rung by rule: {r['rung']} "
                                f"(nearest to the score, halves up); model by rule: {r['model']} (the most probable of the four "
                                f"options, a tie going to the higher-priced model)." + (f" Flags: {'; '.join(fl)}." if fl else "")),
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
    g.add_argument("--batch", help="JSON file: list of {label, action, session}")
    ap.add_argument("--request", required=True, help="request-v8.json or request-hd-v3.json (pinned)")
    ap.add_argument("--label", default="", help="the Step name of the uses-table row")
    ap.add_argument("--session", default="")
    ap.add_argument("--kind", default="live", help="live, acceptance or calibration")
    ap.add_argument("--key-from-env", action="store_true", help="read TYPESAFE_API_KEY (HD Reader environment only)")
    ap.add_argument("--markdown", action="store_true")
    ap.add_argument("--out", help="write the JSON results to this file after every reading")
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
            print(f"### {r.get('label') or '(unlabelled)'}\n{header(r)}\n\nNotion row (paste verbatim as the page properties):\n"
                  + json.dumps(notion_properties(r, r.get("label", ""), r.get("session", ""), kind=a.kind), indent=1, ensure_ascii=False) + "\n")
    else:
        print(json.dumps(results, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
