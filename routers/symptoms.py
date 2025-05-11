from fastapi import APIRouter

from TAGS import TAGS
from repositories.symptoms.model import Symptoms, SymptomsFilters
from services.symptoms import SymptomsService


symptoms_router = APIRouter()

# Register Entity
@symptoms_router.get('/api/symptoms', tags=TAGS['SYMPTOMS'])
async def get(filters: SymptomsFilters | None = None)->list[Symptoms]:
    symptoms = SymptomsService()
    res: list[Symptoms] = await symptoms.get_symptoms(filters=filters)
    return res