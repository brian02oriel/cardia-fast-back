
from pydantic import TypeAdapter
from db.utils import DBUtils
from repositories.symptoms.model import Symptoms, SymptomsFilters


class SymptomsRepository:
    def __init__(self):
        self.db = None
        self.collection_name = 'symptoms'

    async def get_symptoms(self, filters: SymptomsFilters | None = None)->list[Symptoms]:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name=self.collection_name)
        pipeline: list[dict] = []
        if filters and filters.search:
            search = {
                "$or": [
                    {"label": {"$regex": filters.search, "$options": "i"}},
                    {"value": {"$regex": filters.search, "$options": "i"}}
                ]
            }
            pipeline.append(search)
        if filters and filters.value:
            field = {
                "value": {"$in": filters.value}
            }
            pipeline.append(field)
        
        cursor = collection.aggregate(pipeline)
        res: list[Symptoms] = []
        async for doc in cursor:
            res.append(Symptoms(**doc))
        return res