from abc import ABC, abstractmethod

from pydantic import BaseModel


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

    """ Abstract base class for Diagnosis."""
    @abstractmethod
    def make_diagnosis(self, options: list[Option])-> float:
        pass

class DiagnosisFactory(ABC):
    @abstractmethod
    def create_diagnosis(self)->Diagnosis:
        pass  