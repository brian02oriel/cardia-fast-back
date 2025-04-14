from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from db.db import DBConnnection

class DiagnosisRepository:
    def __init__(self, db: AsyncIOMotorDatabase = Depends(DBConnnection.db)):
        self.db = db
        self.collection = db['diagnosis']

    async def create_diagnosis(self, diagnosis):
        res = await self.collection.insert_one(diagnosis)
        return res.inserted_id