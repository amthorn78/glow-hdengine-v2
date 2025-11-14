"""Exception hierarchy for DB adapter."""
from __future__ import annotations

from typing import List, Optional


class AdapterError(RuntimeError):
    """Base adapter error carrying a symbolic code."""

    code = "adapter_error"

    def __init__(self, message: str | None = None, *, attempts: Optional[List[str]] = None, code: str | None = None):
        super().__init__(message or (code or self.code))
        self.attempts = attempts or []
        if code is not None:
            self.code = code


class PrimaryUnavailable(AdapterError):
    code = "primary_unavailable"


class BridgeUnavailable(AdapterError):
    code = "bridge_unavailable"


class BridgeUnsupported(AdapterError):
    code = "bridge_unsupported"


class SqlExecError(AdapterError):
    code = "sql_exec_error"


class TxError(AdapterError):
    code = "tx_error"


class IntrospectionError(AdapterError):
    code = "introspection_error"
