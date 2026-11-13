from uuid import uuid4
from contextlib import asynccontextmanager
 
from fastapi import FastAPI, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker



DATABASE_URL = "postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)



class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))

class TaskORM(Base):
    __tablename__ = "tasks"
    
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    
class CategoriesORM(Base):
    __tablename__ = "categories"
    
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield 


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"],
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


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
        
def task_orm_to_model(task_orm: TaskORM) -> TaskSchema:
    return TaskSchema(id=task_orm.id, title=task_orm.title, completed=task_orm.completed) 


@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)) -> list[TaskSchema]:
    task_from_db = db.scalars(select(TaskORM)).all()
    return [task_orm_to_model(task) for task in task_from_db]


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreateSchema, db: Session = Depends(get_db)) -> TaskSchema:
    new_task = TaskORM(title=payload.title, completed=False)
    db.add(new_task)
    db.commit()
    return task_orm_to_model(new_task)


@app.patch("/tasks/{tasks_id}")
def updata_task(payload: TaskUpdataShema, tasks_id: str, db: Session = Depends(get_db)) -> TaskSchema:
    task_for_update = db.get(TaskORM, tasks_id)
    if payload.title:
        task_for_update.title = payload.title
    if payload.completed is not None:
        task_for_update.completed = payload.completed
    
    db.commit()
    return task_orm_to_model(task_for_update)


@app.delete("/tasks/{tasks_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(tasks_id: str, db: Session = Depends(get_db)) -> None:
   task_for_delete = db.get(TaskORM, tasks_id)
   db.delete(task_for_delete)
   db.commit()  


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
    

def categories_orm_to_model(categories_orm: CategoriesORM) -> CategoriesSchema:
    return CategoriesSchema(id=categories_orm.id, name=categories_orm.name, completed=categories_orm.completed) 


@app.get("/categories")
def read_categorys(db: Session = Depends(get_db)) -> list[CategoriesSchema]:
    categories_from_db = db.scalars(select(CategoriesORM)).all()
    return [categories_orm_to_model(category) for category in categories_from_db]

@app.post("/categories", status_code=status.HTTP_201_CREATED)
def create_categories(payload: CategoriesCreateSchema, db: Session = Depends(get_db)) -> CategoriesSchema:
    new_category = CategoriesORM(name=payload.name, completed=False)
    db.add(new_category)
    db.commit()
    return categories_orm_to_model(new_category)


@app.patch("/categories/{categories_id}")
def update_categories(payload: CategoriesUpdateSchema, categories_id: str, db: Session = Depends(get_db)) -> CategoriesSchema:
    category_for_update = db.get(CategoriesORM, categories_id)
    if payload.name:
        category_for_update.name = payload.name
    if payload.completed is not None:
        category_for_update.completed = payload.completed
    
    db.commit()
    return categories_orm_to_model(category_for_update)
                
                
@app.delete("/categories/{categories_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categories(categories_id: str, db: Session = Depends(get_db)) -> None:
    category_for_delete = db.get(CategoriesORM, categories_id)
    db.delete(category_for_delete)
    db.commit()
