from pydantic import BaseModel, Field

from db.model import MongoBaseModel


class Symptoms(MongoBaseModel):
    value: str
    label: str

class SymptomsFilters(BaseModel):
    value: list[str] = []
    search: str = ''