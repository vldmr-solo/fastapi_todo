# FastApi Todo Api

Simple backend API build with FastApi

## Features

- Users API
- Posts API
- User posts relationship
- CRUD operations

---

## Tech Stack

- Python
- FastAPI
- Pydentic

---

## Run project

'''bash
uvicorn main:app --reload
'''

---

## Endpoints

### Users

GET /users
POST /users
GET /users/{id}

---

### Tasks

GET /tasks
POST /tasks
PUT /tasks/{id}
GET /users/{id}/tasks

---

## Project Structure

/project

todo_api/

├── main.py
├── data.py
├── models.py
├── routes/
│   ├── __init__.py
│   ├── users.py
│   └── tasks.py

---

## Status

Learning backend development with FastAPI.