# Preimage-hash coupling helpers (import-safe)
from __future__ import annotations
from typing import Dict, Tuple
import hashlib
from .sercanon import serialize, dumps_minified_sorted

def preimage_bytes(envelope_without_hash: Dict) -> bytes:
    """Serialize the preimage (no idempotence_hash) to canonical bytes (exactly one LF)."""
    return serialize(envelope_without_hash)

def compute_hash(preimage: bytes) -> str:
    """Return sha256 hex of given bytes."""
    return hashlib.sha256(preimage).hexdigest()

def finalize_envelope(envelope_without_hash: Dict) -> Tuple[Dict, bytes, str]:
    """
    Compute preimage bytes, sha256 hex, then return:
      (final_envelope_with_hash, final_bytes, hash_hex)
    Final bytes are canonical JSON (UTF-8) with exactly one trailing LF.
    """
    pre_b = preimage_bytes(envelope_without_hash)
    h = compute_hash(pre_b)
    final_env = dict(envelope_without_hash, idempotence_hash=h)
    final_b = serialize(final_env)
    return final_env, final_b, h
