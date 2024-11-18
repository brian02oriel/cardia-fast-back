from typing import Protocol

class Diagnosis(Protocol):
    def make_diagnosis(self, code) -> float:
        ''' Contains the logic that compute the diagnosis based on the input '''
        pass