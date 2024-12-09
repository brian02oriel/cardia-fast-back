from fastapi import APIRouter
from TAGS import TAGS

user_router = APIRouter()

# User Entity
@user_router.post('/user', tags=TAGS['USER'])
def create():
    # TODO: Create new user
    return ''

@user_router.get('/user/{id}', tags=TAGS['USER'])
def get():
    # TODO: Get specific user
    return ''

@user_router.put('/user', tags=TAGS['USER'])
def put():
    # TODO: Edit user info
    return ''

@user_router.delete('/user', tags=TAGS['USER'])
def delete():
    # TODO: Add logical delete
    return ''