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

class DiagnosisBody(BaseModel):
    firstName: str
    lastName: str
    personId: str
    email: str
    differential: list[Option]
    symptoms: list[Option]

class DiagnosisResponse(BaseModel):
    name: str
    code: str
    diagnosis: float
    symptoms: list[Option]
    differential: list[Option]
    severity: ESeverity

class Rules(BaseModel):
    count: int
    percentage: float

class Factors(BaseModel):
    code: str
    points: int

class Diagnosis(ABC):

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
    def make_diagnosis(self, differential: list[Option], options: list[Option])-> DiagnosisResponse:
        pass

class DiagnosisFactory(ABC):
    @abstractmethod
    def create_diagnosis(self)->Diagnosis:
        pass  