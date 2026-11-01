---
artifact_type: PRODUCT_ANALYSIS_RECORD
artifact_version: "1.0"
logical_id: HDE-EPIC041-POSTCLOSE-COMPAT-SCORE-RANGE
title: "Compat score range: what bands the real compat path gives across 20,000 synthetic pairs"
origin: "Product Owner, 2026-11-01: 'what I care about is if the product works. I don't want dev changes'; then 'We may as well do all three, yes' (the third being this score-range check); then 'go ahead with the 20000'"
repository_head_read: "origin/main 58723d4d; admitted release 1.3.0, release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e (the same release production reported on 2026-11-01)"
rails: "closed (LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev); no vendor call, no network, no database"
recorded: "2026-11-01T22:31Z"
producer: "Isis, continuing Lead Developer for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
---

# Compat score range across 20,000 synthetic pairs (v1.0)

## 1. Result

**Compat works, but in practice it gives almost only two of its four bands.**

Across 20,000 random pairs of synthetic people, scored by the real compat path at the release production runs:

| Band | Category scores (of 200,000) | Share |
| :- | -: | -: |
| Cool | 157,045 | 78.5% |
| Open | 42,093 | 21.0% |
| Warm | 859 | 0.43% |
| Glow | 3 | 0.0015% |

* **Whole pairs.**
  * 3,851 pairs (19.3%) are Cool in all ten categories.
  * 792 (4.0%) have any Warm or Glow at all.
  * 3 pairs have a Glow anywhere.
* **What a Reader v1 user sees.** Reader v1 shows only `harmony`: Cool 81.6%, Open 18.2%, Warm 21 pairs (0.10%), Glow 0.
* **What this is not.** It is not a defect against canon. The HDE Math Spec governs no score or band distribution (no "category-distribution recipe is governed"). The band thresholds (inclusive maxima 24, 49, 74) and the reduction are the governed ones. Whether this mix is the intended product experience is a Product Owner question.

## 2. Method

1. **Synthetic people.** 2,000 birth instants, drawn uniformly over 1950-01-01 to 2005-12-31 UTC with seed `20261101`. They are invented records, not real people.
2. **Their charts, computed offline (Appendix A).**
   * The personality and design activations of the 13 bodies come from PyEphem 4.2.1. That is tropical, geocentric ecliptic longitude of date.
   * The design moment is when the Sun stood 88° of arc before its natal longitude.
   * The lunar node is Meeus's mean node.
   * The gate wheel starts with Gate 41 at 302°, each gate 5.625°.
   * Each chart's gate set is the union of its 26 activations, which is all the engine reads (`normalize_gates`, the gate mask).
3. **Validated against the live product (Appendix B).** The offline charts for the four people in the live Ops run (HDE-EPIC041-POSTCLOSE-OPS01, P1 and P2) reproduce that run's vendor-backed results exactly: **60 of 60 numbers**, the 20 signals and 10 scores of each pair.
   * The true node gives 52 of 60, so the vendor uses the mean node.
4. **Scoring (Appendix C).**
   * 20,000 distinct random pairs went through `engine.compat.compute.evaluate_pair`, the function the Reader and `hdctl showcompat` use, with the admitted release of this checkout.
   * For speed, the release is admitted once and passed through `evaluate_pair`'s own `bundle_provider` argument. On 30 pairs, this gave full results byte-identical to the default call, which re-admits the release on every pair.
5. **Reproducibility.** Re-running the same seed reproduced the same band shares and pair counts; the second run added exact band counts. The summary JSON's SHA-256 is `bf4471885fdd818284e3065a671c06f1573aeea217b233eadd07dc192c8eddd2`.

## 3. Per-category results

| Category | Mean | Median | p90 | p99 | Max | Zero | Cool | Open | Warm | Glow |
| :- | -: | -: | -: | -: | -: | -: | -: | -: | -: | -: |
| harmony | 15.5 | 16 | 28 | 38 | 60 | 5.2% | 16,329 | 3,650 | 21 | 0 |
| heat | 18.1 | 16 | 35 | 50 | 75 | 7.8% | 14,112 | 5,671 | 215 | 2 |
| communication | 16.2 | 15 | 30 | 43 | 68 | 3.5% | 15,957 | 4,007 | 36 | 0 |
| alignment | 15.2 | 16 | 28 | 41 | 60 | 7.1% | 16,285 | 3,685 | 30 | 0 |
| comfort | 15.7 | 16 | 28 | 41 | 63 | 5.4% | 16,136 | 3,845 | 19 | 0 |
| consistency | 14.4 | 14 | 26 | 38 | 61 | 6.4% | 17,198 | 2,790 | 12 | 0 |
| expansion | 18.6 | 16 | 35 | 50 | 78 | 8.0% | 13,661 | 6,031 | 307 | 1 |
| creativity | 16.4 | 15 | 30 | 44 | 65 | 6.2% | 15,666 | 4,252 | 82 | 0 |
| drive | 19.4 | 18 | 33 | 48 | 70 | 2.5% | 13,785 | 6,089 | 126 | 0 |
| balance | 8.4 | 8 | 25 | 34 | 50 | 41.8% | 17,916 | 2,073 | 11 | 0 |

* **Signals.** Each of the 20 signals runs on its own scale, up to 133 to 200. Their medians sit at 0 to 40.
  * `equilibrium_score` is 0 in 79.6% of pairs, and `counterweight_ratio` in 53.1%. They feed `balance`, which is 0 in 41.8% of pairs.
* **The live run fits the same picture.** The two live pairs scored 0 to 40 (P1) and 0 to 32 (P2).

## 4. Why the scores are low (mechanism, not intent)

* **Scores come from channel states.** Each category score is a weighted mean of channel-state signals over the 36 channels (HDE Math Spec §5; `engine/magic10/`).
* **Random pairs rarely reach a high mean.** A signal contributes only when its channel states occur for the pair. Each signal is 0 for 17% to 80% of pairs, depending on the signal, and a random pair forms few of the states any one category weighs. So most category means land in the bottom quarter of the 0 to 100 scale, below Open's floor of 25.
* **Why Glow is all but unreachable.** It needs a mean of 75 or more, which needs most of a category's weighted signals near their caps at once.
* **The design reasons are not stated in canon.** This record does not say whether that was intended.

## 5. Limits

* **Births are uniform over 1950 to 2005, and pairs are random.** A real user pool and matching may differ. Nothing here says by how much.
* **The chart calculation is validated on four people.** It matched the vendor exactly on all 60 numbers for those four. A planet within arc-seconds of a gate boundary could still differ, but that cannot move a distribution of 20,000 pairs.
* **No live calls.** Every score was computed offline, on the same release production reports (`77204764…`).
* **No code, test, canon or data was changed.** The scripts live in this record only.

## 6. For the Product Owner

* **Is this the intended experience?** About 4 in 5 results are Cool, Warm is rare, and Glow essentially never appears, including for `harmony`, the only band Reader v1 shows.
* **Changing it means changing the HDE Math Spec.** The thresholds, signal weights or reduction would move. That is a math and product decision, not a fix.
* **What this record does not do.** It makes no recommendation on that choice, and it changes nothing.

## 7. Nonclaims

This record:
* makes no QA verdict, acceptance, Ops result, PF09 movement or canon change;
* claims no defect against the HDE Math Spec;
* does not call any score "wrong".

## Canon relied on

Read on `main` at `58723d4d`.

* **HDE Math Spec:**
  * searched for a governed distribution, and none exists ("No current … category-distribution recipe is governed");
  * §5 for the channel-state reduction, by its signal table.
* **HDE Governance:** §12.1 `GATE:CORE-MATCH`, for the band thresholds as inclusive maxima.
* **HDE Build Notes, addendum 2.15:** the live compat test and its synthetic people.
* **Code read:**
  * `engine/core/core.py` (`compute_core`, the band rule);
  * `engine/compat/compute.py` (`evaluate_pair`, `bundle_provider`);
  * `engine/bodygraph/gates.py` (the gate mask).

## Appendix A — `hdchart.py` (SHA-256 `5969513b1177b9b9086dc7abb2a38e0a7eca5f365d7ad3472bb6e25285d3b159`)

```python
"""Offline Human Design gate sets from birth data (analysis only; not product code).

Tropical, geocentric ecliptic longitudes of date from PyEphem; lunar node from Meeus,
Astronomical Algorithms, ch. 47 (mean, or mean plus the five main periodic terms).
Design moment: when the Sun stood 88 degrees of arc before its natal longitude.
Gate wheel: Gate 41 begins at 302 degrees; 64 gates of 5.625 degrees each.
"""
from __future__ import annotations

import datetime as dt
import math
from zoneinfo import ZoneInfo

import ephem

WHEEL = [41, 19, 13, 49, 30, 55, 37, 63, 22, 36, 25, 17, 21, 51, 42, 3, 27, 24, 2, 23, 8, 20, 16, 35,
         45, 12, 15, 52, 39, 53, 62, 56, 31, 33, 7, 4, 29, 59, 40, 64, 47, 6, 46, 18, 48, 57, 32, 50,
         28, 44, 1, 43, 14, 34, 9, 5, 26, 11, 10, 58, 38, 54, 61, 60]
assert sorted(WHEEL) == list(range(1, 65))
WHEEL_START = 302.0
PLANETS = (ephem.Moon, ephem.Mercury, ephem.Venus, ephem.Mars, ephem.Jupiter, ephem.Saturn,
           ephem.Uranus, ephem.Neptune, ephem.Pluto)


def gate_of(lon: float) -> int:
    return WHEEL[int(((lon - WHEEL_START) % 360.0) / 5.625)]


def _eclon(body, d: ephem.Date) -> float:
    body.compute(d, epoch=d)
    return math.degrees(float(ephem.Ecliptic(body, epoch=d).lon)) % 360.0


def _node(d: ephem.Date, true_node: bool) -> float:
    t = (ephem.julian_date(d) - 2451545.0) / 36525.0
    om = 125.0445479 - 1934.1362891 * t + 0.0020754 * t * t + t ** 3 / 467441 - t ** 4 / 60616000
    if true_node:
        r = math.radians
        dd = 297.8501921 + 445267.1114034 * t - 0.0018819 * t * t + t ** 3 / 545868 - t ** 4 / 113065000
        m = 357.5291092 + 35999.0502909 * t - 0.0001536 * t * t + t ** 3 / 24490000
        mp = 134.9633964 + 477198.8675055 * t + 0.0087414 * t * t + t ** 3 / 69699 - t ** 4 / 14712000
        f = 93.2720950 + 483202.0175233 * t - 0.0036539 * t * t - t ** 3 / 3526000 + t ** 4 / 863310000
        om += (-1.4979 * math.sin(r(2 * (dd - f))) - 0.1500 * math.sin(r(m)) - 0.1226 * math.sin(r(2 * dd))
               + 0.1176 * math.sin(r(2 * f)) - 0.0801 * math.sin(r(2 * (mp - f))))
    return om % 360.0


def _sun(d: ephem.Date) -> float:
    return _eclon(ephem.Sun(), d)


def _design_date(birth: ephem.Date) -> ephem.Date:
    target = (_sun(birth) - 88.0) % 360.0
    d = ephem.Date(birth - 88.5)
    for _ in range(60):  # Newton steps on the Sun's ~0.9856 deg/day motion
        diff = ((_sun(d) - target + 180.0) % 360.0) - 180.0
        if abs(diff) < 1e-7:
            break
        d = ephem.Date(d - diff / 0.9856)
    return d


def _activations(d: ephem.Date, true_node: bool) -> list[float]:
    sun = _sun(d)
    node = _node(d, true_node)
    lons = [sun, (sun + 180.0) % 360.0, node, (node + 180.0) % 360.0]
    lons += [_eclon(body(), d) for body in PLANETS]
    return lons


def gates_utc(when_utc: dt.datetime, true_node: bool = True) -> list[int]:
    birth = ephem.Date(when_utc.replace(tzinfo=None))
    design = _design_date(birth)
    lons = _activations(birth, true_node) + _activations(design, true_node)
    return sorted({gate_of(lon) for lon in lons})


def gates_local(date: str, time: str, tz: str, true_node: bool = True) -> list[int]:
    local = dt.datetime.fromisoformat(f"{date}T{time}").replace(tzinfo=ZoneInfo(tz))
    return gates_utc(local.astimezone(dt.timezone.utc), true_node)
```

## Appendix B — `validate.py` (SHA-256 `c23ac2f224a1856972f3028b1ee61ecd2224beffacd332eec3c3bc7d4a5be6fc`)

Run: `python3 validate.py <repo> <ops01-evidence-dir>`. Output on 2026-11-01:
* true node: `p1_ab_1` 22 of 30, `p2_ab` 30 of 30, 52 of 60 in total;
* mean node: `p1_ab_1` 30 of 30, `p2_ab` 30 of 30, **60 of 60** in total.

```python
"""Validate offline charts against the live vendor run: same 20 signals and 10 scores per pair."""
from __future__ import annotations

import json
import pathlib
import sys
import uuid

HERE = pathlib.Path(__file__).resolve().parent
REPO, EV = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(HERE))

from hdchart import gates_local  # noqa: E402
from engine.bodygraph.resolver import ResolvedCompatChart  # noqa: E402
from engine.compat.compute import evaluate_pair, evaluation_party  # noqa: E402
from tests.support.pr04_fixtures import complete_chart  # noqa: E402

PEOPLE = {
    "P1A": ("1990-01-01", "12:00", "Europe/Amsterdam"),
    "P1B": ("1985-07-15", "08:30", "Europe/London"),
    "P2A": ("1992-03-21", "18:45", "America/New_York"),
    "P2B": ("1978-11-02", "04:10", "Australia/Sydney"),
}


def party(name: str, gates: list[int]):
    uid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"scorerange-{name}"))
    return evaluation_party(ResolvedCompatChart(uid, complete_chart(uid, gates), "resolved", None, None, None, None))


def numbers(result) -> dict:
    out = {f"sig:{s['signal_id']}": s["q"] for s in result["signals"]}
    out.update({f"cat:{c['category_id']}": c["score"] for c in result["categories"]})
    return out


for true_node in (True, False):
    label = "true node" if true_node else "mean node"
    total = mism = 0
    for pair, (a, b) in {"p1_ab_1": ("P1A", "P1B"), "p2_ab": ("P2A", "P2B")}.items():
        live = numbers(json.loads((EV / f"{pair}.out").read_text()))
        mine = numbers(evaluate_pair(party(a, gates_local(*PEOPLE[a], true_node)), party(b, gates_local(*PEOPLE[b], true_node))))
        diff = {k: (live[k], mine.get(k)) for k in live if live[k] != mine.get(k)}
        total += len(live); mism += len(diff)
        print(f"{label:9} {pair}: {len(live) - len(diff)}/{len(live)} numbers match" + (f"; differ {diff}" if diff else ""))
    print(f"{label:9} TOTAL {total - mism}/{total} match")
for name, args in PEOPLE.items():
    print(name, "gates(true node):", gates_local(*args, True))
```

## Appendix C — `distribution.py` (SHA-256 `ee544853a813c1d5f6a5705b722cc38a9cde8aeff75fa6aa3eb589f8a40ddf05`)

Run: `python3 distribution.py <repo> <out.json> 2000 20000 cache`, under closed rails.

```python
"""Score distribution of the real compat path over seeded synthetic births (analysis only).

Charts: hdchart.gates_utc with the mean node, validated 60/60 against the live vendor run.
Scoring: engine.compat.compute.evaluate_pair with the admitted release of this checkout.
"""
from __future__ import annotations

import collections
import datetime as dt
import json
import pathlib
import random
import statistics
import sys
import time
import uuid

HERE = pathlib.Path(__file__).resolve().parent
REPO, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
N_PEOPLE, N_PAIRS, SEED = int(sys.argv[3]), int(sys.argv[4]), 20261101
sys.path.insert(0, str(REPO)); sys.path.insert(0, str(HERE))

from hdchart import gates_utc  # noqa: E402
from engine.bodygraph.resolver import ResolvedCompatChart  # noqa: E402
from engine.compat.compute import evaluate_pair, evaluation_party  # noqa: E402
from tests.support.pr04_fixtures import complete_chart  # noqa: E402
from engine.config.registry_loader import load_active_mechanics_bundle  # noqa: E402
# Analysis speed only: admit and verify the release once, then hand it to every pair
# through evaluate_pair's own bundle_provider seam (equivalence: cache_equiv.py).
_BUNDLE = load_active_mechanics_bundle()
_PROVIDER = (lambda: _BUNDLE) if len(sys.argv) > 5 and sys.argv[5] == "cache" else None

rng = random.Random(SEED)
start, span = dt.datetime(1950, 1, 1), (dt.datetime(2006, 1, 1) - dt.datetime(1950, 1, 1)).total_seconds()
t0 = time.time()
people = []
for i in range(N_PEOPLE):
    when = start + dt.timedelta(seconds=rng.random() * span)
    uid = str(uuid.uuid5(uuid.NAMESPACE_URL, f"scorerange-synthetic-{SEED}-{i}"))
    gates = gates_utc(when, true_node=False)
    people.append((uid, gates, evaluation_party(ResolvedCompatChart(uid, complete_chart(uid, gates), "resolved", None, None, None, None))))
t_charts = time.time() - t0

pairs, seen = [], set()
while len(pairs) < N_PAIRS:
    a, b = rng.sample(range(N_PEOPLE), 2)
    key = (min(a, b), max(a, b))
    if key not in seen:
        seen.add(key); pairs.append((a, b))

scores = collections.defaultdict(list); signals = collections.defaultdict(list)
band_count = collections.Counter(); any_warm_or_glow = 0; all_cool = 0; any_glow = 0; harmony_ge_warm = 0
t1 = time.time()
for a, b in pairs:
    r = evaluate_pair(people[a][2], people[b][2], bundle_provider=_PROVIDER)
    bands = []
    for c in r["categories"]:
        scores[c["category_id"]].append(c["score"]); band_count[(c["category_id"], c["band"])] += 1; bands.append(c["band"])
    for s in r["signals"]:
        signals[s["signal_id"]].append(s["q"])
    any_warm_or_glow += any(x in ("Warm", "Glow") for x in bands)
    any_glow += "Glow" in bands; harmony_ge_warm += bands[0] in ("Warm", "Glow") if r["categories"][0]["category_id"] == "harmony" else 0
    all_cool += all(x == "Cool" for x in bands)
t_pairs = time.time() - t1


def pct(v, p):
    v = sorted(v); return v[min(len(v) - 1, int(p / 100 * len(v)))]


rows = []
for cat, v in scores.items():
    n = len(v)
    rows.append({"category": cat, "mean": round(statistics.mean(v), 1), "p10": pct(v, 10), "median": pct(v, 50),
                 "p90": pct(v, 90), "p99": pct(v, 99), "max": max(v), "zero_share": round(v.count(0) / n, 3),
                 **{f"{b.lower()}_share": round(band_count[(cat, b)] / n, 3) for b in ("Cool", "Open", "Warm", "Glow")}})
summary = {
    "seed": SEED, "people": N_PEOPLE, "pairs": N_PAIRS, "births": "uniform UTC instants 1950-01-01 to 2005-12-31",
    "chart_seconds": round(t_charts, 1), "pair_seconds": round(t_pairs, 1),
    "pairs_with_any_warm_or_glow_share": round(any_warm_or_glow / N_PAIRS, 3),
    "pairs_all_cool_share": round(all_cool / N_PAIRS, 3),
    "overall_band_share": {b: round(sum(band_count[(c, b)] for c in scores) / (10 * N_PAIRS), 3) for b in ("Cool", "Open", "Warm", "Glow")},
    "categories": rows,
    "band_counts": {cat: {b: band_count[(cat, b)] for b in ("Cool", "Open", "Warm", "Glow")} for cat in scores},
    "pairs_with_any_glow": any_glow, "pairs_with_any_warm_or_glow": any_warm_or_glow, "pairs_all_cool": all_cool,
    "signals": {s: {"min": min(v), "median": pct(v, 50), "p90": pct(v, 90), "max": max(v), "zero_share": round(v.count(0) / len(v), 3)} for s, v in signals.items()},
}
OUT.write_text(json.dumps(summary, indent=1) + "\n")
print(json.dumps({k: summary[k] for k in ("people", "pairs", "chart_seconds", "pair_seconds", "pairs_with_any_warm_or_glow_share", "pairs_all_cool_share", "overall_band_share")}))
for r in rows:
    print(f"{r['category']:14} mean {r['mean']:5} p10 {r['p10']:3} med {r['median']:3} p90 {r['p90']:3} p99 {r['p99']:3} max {r['max']:3} zero {r['zero_share']:.3f} | Cool {r['cool_share']:.3f} Open {r['open_share']:.3f} Warm {r['warm_share']:.3f} Glow {r['glow_share']:.3f}")
```
