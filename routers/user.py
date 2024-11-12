from fastapi import APIRouter
import TAGS

user_router = APIRouter

# User Entity
@user_router.post('/new', tags=TAGS['USER'])
def create():
    # TODO: Create new user
    return ''

@user_router.get('/get/{id}', tags=TAGS['USER'])
def get():
    # TODO: Get specific user
    return ''

@user_router.put('/delete', tags=TAGS['USER'])
def put():
    # TODO: Edit user info
    return ''

@user_router.post('/delete', tags=TAGS['USER'])
def delete():
    # TODO: Add logical delete
    return ''