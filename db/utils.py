from motor.motor_asyncio import AsyncIOMotorDatabase
import config
from db.db import DBConnnection

class DBUtils:
    def __init__(self):
        pass
    async def get_database(self) -> AsyncIOMotorDatabase:
        db_instance = DBConnnection()
        if db_instance.client is None:
            connection_string = config.get_settings().MONGO_URI
            db_name = config.get_settings().DB_NAME
            await db_instance.connect(connection_string, db_name)
        return db_instance.db

    async def get_collection(self, db, collection_name):
        if db is None:
            db = await self.get_database()
        return db[collection_name]