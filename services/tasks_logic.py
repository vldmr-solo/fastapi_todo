def get_task(tasks, task_id: int):
    for task in tasks:
        if task.get("id") == task_id:
            return task
    
    return None
    

def get_task_by_user(tasks, user_id: int):
    result = []

    for task in tasks:
        if task.get("user_id") == user_id:
            result.append(task)
    
    return result    