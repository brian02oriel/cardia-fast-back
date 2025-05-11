from fastapi import Depends

from db.utils import DBUtils
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisFilters

class DiagnosisRepository():
    def __init__(self):
        self.db = None
        self.collection_name = 'diagnosis'
    
    async def create_diagnosis(self, data: CreateDiagnosisModel)->  str:
        db_utils = DBUtils()
        collection = await db_utils.get_collection(db=self.db, collection_name=self.collection_name)
        res = await collection.insert_one(data)
        return str(res.inserted_id)
    
    async def get_diagnosis(self, filters: DiagnosisFilters):
        # Create a collection of symptoms 
        # Create a collection of differential
        pass