"""Exception hierarchy for DB adapter."""
from __future__ import annotations

from typing import List, Optional, Sequence


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


class RetiredBridgeConfiguration(AdapterError):
    code = "retired_bridge_configuration"

    def __init__(self, retired_keys: Sequence[str]):
        self.retired_keys = tuple(sorted(retired_keys))
        super().__init__(
            "retired_bridge_configuration:" + ",".join(self.retired_keys),
            attempts=[],
            code=self.code,
        )


class SqlExecError(AdapterError):
    code = "sql_exec_error"


class TxError(AdapterError):
    code = "tx_error"


class IntrospectionError(AdapterError):
    code = "introspection_error"
