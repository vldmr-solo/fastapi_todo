from pydantic import BaseModel

class UserData(BaseModel):
    name: str
    age: int

class NewTask(BaseModel):
    task: str
    user_id: int

