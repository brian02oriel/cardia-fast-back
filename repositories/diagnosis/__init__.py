from fastapi import Depends

from db.utils import DBUtils
from factory.interfaces.DiagnosisInterface import Option
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisFilters, PatientDiagnosisResponse

class DiagnosisRepository():
    def __init__(self):
        self.db = None
    
    async def create_diagnosis(self, data: CreateDiagnosisModel)->  str:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis')
        res = await collection.insert_one(data)
        return str(res.inserted_id)
    
    async def get_diagnosis(self, filters: DiagnosisFilters | None = None)->list[PatientDiagnosisResponse]:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis_view')
        pipeline = []
        if filters and not filters.search:
            pipeline.append({
                field: { '$in': filters[field]}
            } for field in filters if filters[field])
        if filters and filters.search and not filters.personId and not filters.firstName and not filters.lastName and not filters.email:
            pipeline.append({
                '$or': [
                    { 'personId': { '$regex': filters.search, '$options': 'i' }},
                    { 'firstName': { '$regex': filters.search, '$options': 'i' }},
                    { 'lastName': { '$regex': filters.search, '$options': 'i' }},
                    { 'email': { '$regex': filters.search, '$options': 'i' }}
                ]
            })

        res = await collection.aggregate(pipeline)
        res: list[PatientDiagnosisResponse] = [PatientDiagnosisResponse(**doc) async for doc in res]
        return res