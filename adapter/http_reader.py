from __future__ import annotations
from flask import Blueprint, Response, request
from adapter.etag_core import reader_response
from engine.stable.sercanon import serialize
import hashlib

bp = Blueprint("reader", __name__)

def _emit_demo_public_bytes_and_hash() -> tuple[bytes, str]:
    # Minimal success envelope (schema-legal, numeric-free)
    env = {
        "reader_version": "v1",
        "eligible": False,
        "categories": [],
        "meta": {"engine_tag": "dev", "invocation_tag": "local-smoke"},
        "release_id": "0"*64,
    }
    # Preimage = env without idempotence_hash
    pre_b = serialize(env)                 # bytes, single LF (canonical)
    h = hashlib.sha256(pre_b).hexdigest()  # lowercase hex
    env["idempotence_hash"] = h
    public_bytes = serialize(env)          # final literal bytes (LF-terminated)
    return public_bytes, h

@bp.route("/reader", methods=["GET", "HEAD"])
def reader():
    public_bytes, id_hash = _emit_demo_public_bytes_and_hash()
    status, headers, body = reader_response(
        public_bytes=public_bytes,
        id_hash_hex=id_hash,
        if_none_match=request.headers.get("If-None-Match"),
        method=request.method,
    )
    return Response(body, status=status, headers=headers, mimetype="application/json; charset=utf-8")
