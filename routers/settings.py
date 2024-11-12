from fastapi import APIRouter
import TAGS

settings_router = APIRouter

# Settings Entity
@settings_router.post('/new', tags=TAGS['SETTINGS'])
def create():
    # TODO: Create new settings
    return ''

@settings_router.get('/get/{id}', tags=TAGS['SETTINGS'])
def get():
    # TODO: Get specific settings by user
    return ''
