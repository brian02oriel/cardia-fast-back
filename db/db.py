from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

class DBConnnection:
    """
    Singleton pattern implementation for MongoDB connection
    """
    _instance = None
    _client: Optional[AsyncIOMotorClient] = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnnection, cls).__new__(cls)
            cls._instance._client = None
        return cls._instance

    async def connect(self, connection_string: str, db_name: str):
        """Connect to MongoDB database"""
        if self._client is None:
            try:
                logger.info("Connecting to MongoDB...")
                self._client = AsyncIOMotorClient(connection_string)
                # Verify connection is successful
                await self._client.admin.command('ping')
                self._db = self._client[db_name]
                logger.info(f"Connected to MongoDB: {db_name}")
            except ConnectionFailure:
                logger.error("Failed to connect to MongoDB: {connection_string}")
                raise

    async def disconnect(self):
        """Close the database connection"""
        if self._client is not None:
            logger.info("Closing connection to MongoDB...")
            self._client.close()
            self._client = None
            logger.info("MongoDB connection closed")

    @property
    def db(self):
        """Return database instance"""
        return self._db

    @property
    def client(self):
        """Return client instance"""
        return self._client