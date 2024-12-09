from abc import ABC, abstractmethod

from pydantic import BaseModel

class CustomSelectOption(BaseModel):
    code: str
    label: str

class Fields(BaseModel):
    options: list[CustomSelectOption]

class Diagnosis(ABC):
    code: str
    """ Abstract base class for Diagnosis."""
    @abstractmethod
    def make_diagnosis(self, options: Fields)-> float:
        pass

class DiagnosisFactory(ABC):
    @abstractmethod
    def create_diagnosis(self)->Diagnosis:
        pass  