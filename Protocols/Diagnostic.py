from typing import Protocol

class Diagnostic(Protocol):
    def __init__(self):
        super().__init__()

    def compute(self) -> int:
        pass
