from fastapi import APIRouter
import TAGS

settings_router = APIRouter

# Settings Entity
@settings_router.post('/settings', tags=TAGS['SETTINGS'])
def create():
    # TODO: Create new settings
    return ''

@settings_router.get('/settings/{id}', tags=TAGS['SETTINGS'])
def get():
    # TODO: Get specific settings by user
    return ''
