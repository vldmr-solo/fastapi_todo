from fastapi import APIRouter, HTTPException
from models import UserData
from data import users

router = APIRouter(prefix="/user")


def find_user(user_id: int):
    for user in users:
        if user.get("id") == user_id:
            return user
    
    return None


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