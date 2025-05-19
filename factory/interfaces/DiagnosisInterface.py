from abc import ABC, abstractmethod
from enum import Enum

from pydantic import BaseModel

class ESeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Option(BaseModel):
    value: str
    label: str

class PredictedDiagnosis(BaseModel):
    name: str
    code: str
    diagnosis: float
    symptoms: list[Option]
    differential: Option
    severity: ESeverity

class Rules(BaseModel):
    count: int
    percentage: float

class Factors(BaseModel):
    code: str
    points: int

class Diagnosis(ABC):
    name: str
    code: str
    """ Rules """
    @abstractmethod
    def get_rules(self)->list[Rules]:
        pass


    """ Factors """
    @abstractmethod
    def get_factors(self)->list[Factors]:
        pass

    """ Abstract class for Severity."""
    @abstractmethod
    def get_severity(self, diagnosis: float)-> ESeverity:
        pass

    """ Abstract base class for Diagnosis."""
    @abstractmethod
    def make_diagnosis(self, differential: Option, options: list[Option])-> PredictedDiagnosis:
        pass

class DiagnosisFactory(ABC):
    @abstractmethod
    def create_diagnosis(self)->Diagnosis:
        pass  