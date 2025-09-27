import os, re, glob
from adapter.logging_filter import log_startup_line

class EnvGuardError(Exception):
    def __init__(self, code: str, message: str, details=None):
        # Standard typed error: code/message/details; str(e) == message
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details

