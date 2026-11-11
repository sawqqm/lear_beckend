from uuid import uuid4

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"]
)

#TASKS

class TaskSchema(BaseModel):
    id: str
    title: str
    completed: bool


class TaskCreateSchema(BaseModel):
    title: str


class TaskUpdataShema(BaseModel):
    title: str | None = None
    completed: bool | None = None


tasks: list[TaskSchema] = []


@app.get("/tasks")
def read_tasks() -> list[TaskSchema]:
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4()), title=payload.title, completed=False)
    tasks.append(new_task)
    return new_task


@app.patch("/tasks/{tasks_id}")
def updata_task(payload: TaskUpdataShema, tasks_id: str):
    for task in tasks:
        if task.id == tasks_id:
            if payload.title:
                task.title = payload.title
            if payload.completed is not None:
                task.completed = payload.completed is not None
            return task


@app.delete("/tasks/{tasks_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(tasks_id: str):
    for task in tasks:
        if task.id == tasks_id:
            tasks.remove(task)



#CATEGORIES

class CategoriesSchema(BaseModel):
    id: str
    name: str
    completed: bool
    
    
class CategoriesCreateSchema(BaseModel):
    name: str
    
    
class CategoriesUpdateSchema(BaseModel):
    name: str | None = None
    completed: bool | None = None
    

categories: list[CategoriesSchema] = []

@app.get("/categories")
def read_categorys() -> list[CategoriesSchema]:
    return categories

@app.post("/categories", status_code=status.HTTP_201_CREATED)
def create_categories(payload: CategoriesCreateSchema) -> CategoriesSchema:
    new_categories = CategoriesSchema(id= str(uuid4()), name=payload.name, completed=False)
    categories.append(new_categories)
    return new_categories


@app.patch("/categories/{categories_id}")
def update_categories(payload: CategoriesUpdateSchema, categories_id: str):
    for category in categories:
        if category.id == categories_id:
            if payload.name:
                category.name = payload.name
            if payload.completed is not None:
                category.completed = payload.completed is not None
                
                
@app.delete("/categories/{categories_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categories(categories_id: str):
    for category in categories:
        if category.id == categories_id:
            categories.remove(category)
