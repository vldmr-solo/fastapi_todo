from fastapi import APIRouter, HTTPException
from models import UserData
from data import users
from services.users_logic import get_user

router = APIRouter(prefix="/user")


@router.get("")
def get_users():
    return users


@router.get("/{id}")
def get_user_by_id(id: int):
    
    user = get_user(users, id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    return user

@router.post("")
def post_users(data: UserData):

    new_user = {
        "id": len(users) + 1,
        "name": data.name,
        "age": data.age
    }

    users.append(new_user)

    return new_user

