from fastapi import APIRouter, HTTPException
from models import UserData
from data import users
from services.users_logic import find_user

router = APIRouter(prefix="/user")


@router.get("")
def get_users():
    return users


@router.post("")
def post_users(data: UserData):

    new_user = {
        "id": len(users) + 1,
        "name": data.name,
        "age": data.age
    }

    users.append(new_user)

    return new_user


@router.get("/{id}")
def get_user(id: int):
    user = find_user(id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")
       


'''
вопросы: 
нужно ли делать проверку age на тип данных и тд в post_users

'''