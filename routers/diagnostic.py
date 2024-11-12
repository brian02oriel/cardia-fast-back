from fastapi import APIRouter
import TAGS

diagnostic_router = APIRouter

# Register Entity
@diagnostic_router.post('/new', tags=TAGS['REGISTER'])
def create():
    # TODO: Calculate new diagnostics
    # TODO: Save patient and diagnostic
    return ''

@diagnostic_router.get('/get', tags=TAGS['REGISTER'])
def get():
    # Pass filters as params
    # TODO: Get every register
    return ''

@diagnostic_router.post('/delete', tags=TAGS['REGISTER'])
def delete():
    # TODO: Add logical delete
    return ''