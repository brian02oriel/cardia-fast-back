import logging
from typing import Any
from pymongo import ASCENDING
from pymongo.asynchronous.database import AsyncDatabase
import config
from db.db import DBConnnection

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class DBUtils:
    def __init__(self):
        pass
    async def get_database(self) -> AsyncDatabase:
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
    
    async def get_indexes(self, db: AsyncDatabase, collection_name: str):
        collection = db[collection_name]
        indexes = await (await collection.list_indexes()).to_list(length=None)
        index_names = [index['name'] for index in indexes]
        logger.info(f"Indexes in {collection_name}: {index_names}")
        return index_names
    
    async def drop_index(self, db: AsyncDatabase, collection_name: str, index_name: str):
        if(index_name == "_id_"):
            logger.warning("Cannot drop the default _id index.")
            return
        collection = db[collection_name]
        await collection.drop_index(index_name)
        logger.info(f"Index deleted: {index_name}")
    
    async def create_index(self, db: AsyncDatabase, collection_name: str, index_name: str, fields: list[str], unique: bool = False):
        collection = db[collection_name]
        index = [(field, ASCENDING) for field in fields]
        await collection.create_index(index, name=index_name, unique=unique)
        logger.info(f"Index created: {index}")
    
    async def drop_view(self, db: AsyncDatabase, view_name: str):
        collection = await self.get_collection(db, view_name)
        if collection.name:
            await collection.drop()
            logger.info(f"View dropped: {view_name}")
        else:
            logger.warning(f"View {view_name} does not exist.")
    async def create_view(self, db: AsyncDatabase, collection_name: str, view_name: str, pipeline: dict[Any, Any], delete_duplicate: bool = True):
        collection = await self.get_collection(db, view_name)
        if delete_duplicate:
            await collection.drop()
            logger.info(f"View dropped {view_name}")
        await db.command(
            {'create' : view_name,
            'viewOn' : collection_name,
            'pipeline' : pipeline}
        )
        logger.info(f"View created: {view_name}")