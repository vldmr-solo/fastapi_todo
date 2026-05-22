from fastapi import APIRouter, HTTPException
from models import NewTask
from data import tasks, users
from services.tasks_logic import find_task, get_task_by_user
from services.users_logic import find_user

router = APIRouter(prefix="/tasks")


@router.get("")
def get_tasks():
    return tasks


@router.post("")
def post_tasks(data: NewTask):

    user = find_user(data.user_id)

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
def put_tasks(id: int, data: NewTask):

    task = find_task(id)

    if not task:
        raise HTTPException(status_code=404, detail="task not found")   

    task.update({
        "task": data.task, 
        "user_id": data.user_id
    })

    return task


@router.get("/users/{id}/tasks")
def get_user_tasks(id: int):
    
    user = find_user(id)

    if not user:
        raise HTTPException(status_code=404, detail="user not found")                    

    return get_task_by_user(id)



'''
вопросы: 
зачем {id} в @router.put в tasks.py, если есть в models.py класс NewTask с ид и таск
ок ли делать проверки на наличие юзера и таска в пост и пут
как улучишить put
как работает current_user

'''