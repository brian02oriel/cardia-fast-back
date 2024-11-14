from typing import Protocol

class Diagnostic(Protocol):
    code: str
    def __init__(self):
        super().__init__()

    def compute(self) -> int:
        pass
