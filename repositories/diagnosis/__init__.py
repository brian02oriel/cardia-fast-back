from fastapi import Depends
from pydantic import TypeAdapter
from db.utils import DBUtils
from factory.interfaces.DiagnosisInterface import Option
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisFilters, DiagnosisResponse, PatientDiagnosisResponse, PatientDiagnosisSummary

class DiagnosisRepository():
    def __init__(self):
        self.db = None
    
    async def create_diagnosis(self, data: CreateDiagnosisModel)->  str:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis')
        res = await collection.insert_one(data)
        return str(res.inserted_id)
    
    async def get_diagnosis(self, personId: str)->list[PatientDiagnosisResponse]:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis')

        res = collection.find({'personId': personId})
        return [TypeAdapter(PatientDiagnosisResponse).validate_python(doc) for doc in await res.to_list(length=None)]
    
    async def get_diagnosis_summary(self, filters: DiagnosisFilters | None = None)->list[PatientDiagnosisSummary]:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis_view')
        pipeline = []
        if not filters.search and (filters.personId or filters.firstName or filters.lastName or filters.email):
            pipeline.append({
                field: { '$in': filters[field]}
            } for field in filters if filters[field])
        if filters and filters.search and not filters.personId and not filters.firstName and not filters.lastName and not filters.email:
            pipeline.append(
                {
                    '$match': {
                        '$or': [
                            { 'personId': { '$regex': filters.search, '$options': 'i' }},
                            { 'firstName': { '$regex': filters.search, '$options': 'i' }},
                            { 'lastName': { '$regex': filters.search, '$options': 'i' }},
                            { 'email': { '$regex': filters.search, '$options': 'i' }}
                        ]
                    }
        })

        res = await collection.aggregate(pipeline)
        res: list[PatientDiagnosisSummary] = [PatientDiagnosisSummary(**doc) async for doc in res]
        return res