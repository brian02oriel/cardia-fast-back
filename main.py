from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from routers.user import user_router
from routers.diagnosis import diagnosis_router
from routers.settings import settings_router

import TAGS

app = FastAPI()
app.title = 'Cardia Fast API'
app.version = '0.0.1'

app.include_router(user_router)
app.include_router(diagnosis_router)
app.include_router(settings_router)


@app.get('/', tags=TAGS['HOME'])
def read_root():
    return {'Hello': 'World'}