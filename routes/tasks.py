from fastapi import APIRouter, HTTPException
from models import NewTask
from data import tasks, users
from services.users_logic import get_user
from services.tasks_logic import get_task, get_task_by_user


router = APIRouter(prefix="/tasks")


@router.get("")
def get_tasks():
    return tasks


@router.get("/{id}")
def get_user_tasks(id: int):

    user = get_user(users, id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")                    

    task_by_user = get_task_by_user(tasks, id)

    return task_by_user


@router.post("")
def post_tasks(data: NewTask):

    user = get_user(users, data.user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="user not found")                    
        
    new_task = {
        "id": len(tasks) + 1, 
        "task": data.task, 
        "user_id": data.user_id
    }

    tasks.append(new_task)

    return new_task


@router.put("/{id}")
def put_tasks_by_id(id: int, data: NewTask):

    user = get_user(users, data.user_id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")                    

    task = get_task(tasks, id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")   

    task["task"] = data.task
    task["user_id"] = data.user_id

    return task

