"""Magic10 v2 dormant integration layer (HDE-CONJ010.4; HDE-EPIC043 WU-PR-03).

From two gate masks, an admitted v2 bundle and an explicit ``release_id``, this
module produces, by calling existing code only:

* the ``magic10_result.v2`` value (``compute_magic10_v2``);
* the intrinsic cache key ``magic10:v2:<pair_key>``
  (``magic10_v2_intrinsic_cache_key``);
* the validated ``magic10_compat_result.v2`` value, with narrative keys from
  ``route_keys`` in both normalized directions; nothing is rescored or clamped;
* its canonical bytes (``emit_public``), the one producer of the bytes both
  internal surfaces will print (PF05 parity);
* the Reader v1 and Reader v2 projections of a v2 result
  (``emit_reader_public_envelope``), bands only.

It restates the rules of v1's ``_route``, ``_key``, ``_augment`` and
``validate_compat_result`` (``engine/compat/compute.py``) without importing
them. Eligibility, party resolution, orientation, the self-pair carrier, the
cache lookup and store, provider seams and the PF05 error-token mapping stay
with the switch (HDE-EPIC043 WU-PR-09). The result depends only on the two
masks, so (A, B) and (B, A) give the same value and bytes.

Stated limits:

* The compat v2 schema bytes are read from the repository root and cannot be
  checked against the bundle, which carries no identity for the result schemas;
  the release manifest binds them from the cut. The schema document stays the
  guard, and no value is returned unvalidated.
* The narrative router reads its pack relative to the working directory, as it
  does for v1.
* Importing this module reads no file. The first Reader projection imports
  ``engine.runtime.public``, which reads the packaged manifest at import.

Reached from production since the switch (HDE-EPIC043 WU-PR-09), through
``engine/compat/compute.py``.
"""
from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from pathlib import Path

import jsonschema
from jsonschema import validators

from engine.config.magic10_v2_loader import (
    MAGIC10_V2_COMPAT_RESULT_SCHEMA,
    Magic10V2Bundle,
    magic10_v2_intrinsic_cache_key,
)
from engine.config.registry_loader import SchemaValidationError
from engine.magic10_v2.calculation import Magic10V2Result, compute_magic10_v2
from engine.narratives.constants import MISSING_NARRATIVE_KEY
from engine.narratives.router import route_keys
from engine.presenter.emitter import emit_public

COMPAT_RESULT_SCHEMA_PATH = "schemas/magic10_compat_result_v2.schema.json"
# Documentary: the existing projection function stays the guard for the version.
READER_VERSIONS = ("v1", "v2")

INPUT_INVALID = "M10V2_COMPAT_INPUT_INVALID"
NARRATIVE_KEY_INVALID = "M10V2_COMPAT_NARRATIVE_KEY_INVALID"
RESULT_INVALID = "M10V2_COMPAT_RESULT_INVALID"
PROJECTION_REFUSED = "M10V2_COMPAT_PROJECTION_REFUSED"

_ROOT = Path(__file__).resolve().parents[2]
_HARMONY = "harmony"
# Compiled validators keyed by the SHA-256 of the schema bytes they were built from.
_VALIDATORS: dict[str, object] = {}

Router = Callable[..., Mapping[str, str]]


@dataclass(frozen=True, slots=True)
class Magic10V2Evaluation:
    """One pair's v2 result, its cache key and its canonical compat v2 bytes.

    The bytes are the one stored form of the ``magic10_compat_result.v2`` value,
    so the value and the bytes cannot diverge.
    """

    result: Magic10V2Result
    cache_key: str
    compat_bytes: bytes

    def compat_payload(self) -> dict[str, object]:
        """Return a new ``magic10_compat_result.v2`` object decoded from ``compat_bytes``."""
        return json.loads(self.compat_bytes)


def evaluate_magic10_v2(
    mask_a: int, mask_b: int, bundle: Magic10V2Bundle, release_id: str, *, router: Router | None = None
) -> Magic10V2Evaluation:
    """Evaluate one pair over an explicit admitted v2 bundle and ``release_id``.

    Refusals (``SchemaValidationError``): first the calculation's, kernel's and
    signals' own, propagated unchanged (``M10V2_CALC_RELEASE_ID_INVALID`` before
    anything is read); then this module's ``M10V2_COMPAT_*`` codes.
    """
    result = compute_magic10_v2(mask_a, mask_b, bundle, release_id)
    value = compat_result_v2(result, bundle, router=router)
    return Magic10V2Evaluation(result=result, cache_key=intrinsic_cache_key_v2(result), compat_bytes=emit_public(value))


def intrinsic_cache_key_v2(result: Magic10V2Result) -> str:
    """Return ``magic10:v2:<pair_key>`` through the loader's one construction."""
    _require(result, Magic10V2Result, "result")
    return magic10_v2_intrinsic_cache_key(result.pair_key)


def compat_result_v2(
    result: Magic10V2Result, bundle: Magic10V2Bundle, *, router: Router | None = None
) -> dict[str, object]:
    """Return the validated ``magic10_compat_result.v2`` value of one v2 result.

    Each category's keys come from the router in the normalized lo→hi
    (``a_to_b``) and hi→lo (``b_to_a``) directions, which must agree on
    ``shared_key``. Scores, bands and signals are copied from the result.
    """
    _require(result, Magic10V2Result, "result")
    _require(bundle, Magic10V2Bundle, "bundle")
    route = route_keys if router is None else router
    rows = []
    for category in result.categories:
        lo_to_hi = _route(route, category.category_id, category.band, "a_to_b")
        hi_to_lo = _route(route, category.category_id, category.band, "b_to_a")
        shared = _key(lo_to_hi, "shared_key", category.category_id)
        if shared != _key(hi_to_lo, "shared_key", category.category_id):
            raise SchemaValidationError(
                NARRATIVE_KEY_INVALID,
                "the two directions disagree on shared_key",
                {"category_id": category.category_id, "field": "shared_key"},
            )
        rows.append({
            "category_id": category.category_id,
            "score": category.score,
            "band": category.band,
            "shared_key": shared,
            "personal_lo_to_hi_key": _key(lo_to_hi, "personal_key", category.category_id),
            "personal_hi_to_lo_key": _key(hi_to_lo, "personal_key", category.category_id),
        })
    value: dict[str, object] = {
        "schema": MAGIC10_V2_COMPAT_RESULT_SCHEMA,
        "config_id": result.config_id,
        "release_id": result.release_id,
        "pair_key": result.pair_key,
        "signals": [{"signal_id": signal.signal_id, "q": signal.q} for signal in result.signals],
        "categories": rows,
    }
    validate_compat_result_v2(value, bundle, release_id=result.release_id, pair_key=result.pair_key)
    return value


def validate_compat_result_v2(value: object, bundle: Magic10V2Bundle, *, release_id: str, pair_key: str) -> None:
    """Validate a compat v2 value against the schema document and the bundle's identity.

    Checks, in order: the schema (strict integers: a ``bool`` is not an
    integer), then ``release_id``, ``config_id``, ``pair_key``, the category
    order and the signal order. A failure is ``M10V2_COMPAT_RESULT_INVALID``
    with ``details["check"]`` naming the check.
    """
    _require(bundle, Magic10V2Bundle, "bundle")
    try:
        _validator().validate(value)
    except jsonschema.ValidationError:
        raise _invalid("schema") from None
    registry = bundle.registry
    order = list(registry.magic10_order)
    if value["release_id"] != release_id:
        raise _invalid("release_id")
    if value["config_id"] != bundle.configuration["config_id"]:
        raise _invalid("config_id")
    if value["pair_key"] != pair_key:
        raise _invalid("pair_key")
    if [row["category_id"] for row in value["categories"]] != order:
        raise _invalid("category_order")
    signal_order = [signal for category in order for signal in registry.magic10_caps[category].inputs]
    if [row["signal_id"] for row in value["signals"]] != signal_order:
        raise _invalid("signal_order")


def reader_projection_v2(result: Magic10V2Result, reader_version: str) -> tuple[bytes, dict[str, object]]:
    """Return the Reader projection of an eligible v2 result: canonical bytes and envelope.

    ``"v1"`` projects the one ``harmony`` band and ``"v2"`` the ten bands in the
    result's governed order; both are numeric-free. ``engine_tag`` and
    ``invocation_tag`` come from ``identity_meta()``; ``release_id`` is the
    result's explicit one. A refusal by the projection function becomes
    ``M10V2_COMPAT_PROJECTION_REFUSED`` with its reason.
    """
    _require(result, Magic10V2Result, "result")
    from engine.runtime.public import emit_reader_public_envelope

    if reader_version == "v1":
        selection = {"harmony_band": next(item.band for item in result.categories if item.category_id == _HARMONY)}
    elif reader_version == "v2":
        selection = {"categories": [{"id": item.category_id, "band": item.band} for item in result.categories]}
    else:
        selection = {}
    try:
        return emit_reader_public_envelope(
            eligible=True, reader_version=reader_version, release_id=result.release_id, **selection
        )
    except ValueError as exc:
        raise SchemaValidationError(
            PROJECTION_REFUSED, "the Reader projection refused its input", {"reason": str(exc)}
        ) from None


def _validator():
    raw = _ROOT.joinpath(COMPAT_RESULT_SCHEMA_PATH).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    cached = _VALIDATORS.get(digest)
    if cached is None:
        schema = json.loads(raw.decode("utf-8"))
        strict = validators.extend(
            jsonschema.Draft202012Validator,
            type_checker=jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
                "integer", lambda checker, value: type(value) is int
            ),
        )
        strict.check_schema(schema)
        cached = _VALIDATORS[digest] = strict(schema)
    return cached


def _route(route: Router, category: str, band: str, perspective: str) -> Mapping[str, str]:
    keys = route(category, band, perspective)
    if not isinstance(keys, Mapping):
        raise SchemaValidationError(
            NARRATIVE_KEY_INVALID, "the router returned no key mapping", {"category_id": category, "field": None}
        )
    return keys


def _key(keys: Mapping[str, str], field: str, category: str) -> str:
    value = keys.get(field)
    if not isinstance(value, str) or not value or value == MISSING_NARRATIVE_KEY:
        raise SchemaValidationError(
            NARRATIVE_KEY_INVALID, "a narrative key is missing", {"category_id": category, "field": field}
        )
    return value


def _invalid(check: str) -> SchemaValidationError:
    return SchemaValidationError(RESULT_INVALID, "the compat v2 value does not validate", {"check": check})


def _require(value: object, expected: type, argument: str) -> None:
    if type(value) is not expected:
        raise SchemaValidationError(INPUT_INVALID, f"{argument} must be a {expected.__name__}", {"argument": argument})
