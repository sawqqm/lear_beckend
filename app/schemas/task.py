from pydantic import BaseModel

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