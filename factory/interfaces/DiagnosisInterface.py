from abc import ABC, abstractmethod

class Diagnosis(ABC):
    """ Abstract base class for Diagnosis."""
    @abstractmethod
    def make_diagnosis(self)-> float:
        pass

class DiagnosisFactory(ABC):
    @abstractmethod
    def create_diagnosis(self)->Diagnosis:
        pass  