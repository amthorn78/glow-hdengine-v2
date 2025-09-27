from __future__ import annotations
from flask import Blueprint, Response, request
from adapter.etag_core import reader_response
from engine.stable.sercanon import serialize
import hashlib, os

bp = Blueprint("reader", __name__)

def _demo_public_bytes_and_hash() -> tuple[bytes, str]:
    # Minimal Reader v1 envelope for smoke runs; single serializer + one LF
    env = {
        "reader_version": "v1",
        "eligible": False,
        "categories": [],
        "meta": {
            "engine_tag": os.getenv("ENGINE_TAG", "dev"),
            "invocation_tag": "SMOKE",
        },
        "release_id": "0"*64,
    }
    # Hash coupling on the preimage (envelope WITHOUT idempotence_hash)
    pre_b = serialize(env)
    h = hashlib.sha256(pre_b).hexdigest()
    env["idempotence_hash"] = h
    public_b = serialize(env)
    return public_b, h

@bp.route("/reader", methods=["GET", "HEAD"])
def reader():
    public_b, h = _demo_public_bytes_and_hash()
    status, headers, body = reader_response(
        public_b,
        h,
        if_none_match=request.headers.get("If-None-Match"),
        method=request.method,
    )
    # Body is empty on 304 and on HEAD hits/misses per reader_response
    return Response(body, status=status, headers=headers, mimetype="application/json; charset=utf-8")
