
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.categories import CategoriesService
from app.services.task import TaskService



def get_task_service(db: Session = Depends(get_db)):
    return TaskService()

def get_categories_service():
    return CategoriesService()