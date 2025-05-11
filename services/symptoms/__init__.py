from repositories.symptoms import SymptomsRepository
from repositories.symptoms.model import Symptoms, SymptomsFilters


class SymptomsService:
    def __init__(self):
        pass
    async def get_symptoms(self, filters: SymptomsFilters | None = None)-> list[Symptoms]:
        repository = SymptomsRepository()
        res: list[Symptoms] = await repository.get_symptoms(filters=filters)
        return res