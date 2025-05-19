from fastapi import Depends

from db.utils import DBUtils
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisFilters, PatientDiagnosisResponse

class DiagnosisRepository():
    def __init__(self):
        self.db = None
    
    async def create_diagnosis(self, data: CreateDiagnosisModel)->  str:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis')
        res = await collection.insert_one(data)
        return str(res.inserted_id)
    
    async def get_diagnosis(self, filters: DiagnosisFilters)->list[PatientDiagnosisResponse]:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name='diagnosis_view')
        pipelines = []
        res = await collection.find().to_list()
        return res