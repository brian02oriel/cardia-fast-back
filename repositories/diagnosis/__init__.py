from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from db.db import get_database
from repositories.diagnosis.model import CreateDiagnosisModel, DiagnosisByPatient, DiagnosisFilters

class DiagnosisRepository():
    def __init__(self):
        self.db = None
        self.collection_name = 'diagnosis'
    async def __get_collection__(self):
        if self.db is None:
            self.db = await get_database()
        return self.db[self.collection_name]
    
    async def create_diagnosis(self, data: CreateDiagnosisModel)->  str:
        collection = await self.__get_collection__()
        res = await collection.insert_one(data)
        return str(res.inserted_id)
    
    async def get_diagnosis(self, filters: DiagnosisFilters):
        # Create a collection of symptoms 
        # Create a collection of differential
        pass