from contextlib import asynccontextmanager
from fastapi import FastAPI
from pymongo import ASCENDING
import uvicorn
import config
from db.db import DBConnnection
from db.utils import DBUtils
from routers.user import user_router
from routers.symptoms import symptoms_router
from routers.diagnosis import diagnosis_router
from routers.settings import settings_router
from TAGS import TAGS
from fastapi.middleware.cors import CORSMiddleware

db_connection = DBConnnection()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_connection.connect(config.get_settings().MONGO_URI, config.get_settings().DB_NAME)
    db_utils = DBUtils()
    await db_utils.create_index(
        db_connection.db, 
        'diagnosis', 
        'text_field_index', 
        ['firstName', 'lastName', 'age', 'personId', 'email'],
        unique=False)
    await db_utils.create_view(
        db_connection.db, 
        'diagnosis', 
        'diagnosis_view', 
        [
            {
                '$group': {
                '_id': "$personId",
                'firstName': { '$first': "$firstName" },
                'lastName': { '$first': "$lastName" },
                'age': { '$first': "$age" },
                'email': { '$first': "$email" },
                'differential': { '$first': "$differential" },
                    'count': { '$sum': 1 },
                }
            },
            { 
                '$match': { 
                'count': { '$gt': 1 } 
                } 
            },
            {
                '$project': {
                '_id': "$documents._id",
                'personId': "$_id",
                'firstName': 1,
                'lastName': 1,
                'age': 1,
                'email': 1,
                'differential': 1,
                'count': 1
                }
            },
        ]
    )
    yield
    await db_connection.disconnect()

app = FastAPI(lifespan=lifespan)

app.title = 'Cardia Fast API'
app.version = '0.0.1'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(symptoms_router)
app.include_router(diagnosis_router)
app.include_router(settings_router)



@app.get('/', tags=TAGS['HOME'])
def read_root():
    return {'Hello': 'World'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)