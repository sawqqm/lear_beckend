from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import TaskORM


class CategoriesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db 
    def get_all_categories(self) -> list[TaskORM]:
        return self.db.scalars(select(TaskORM)).all()
    
    def get_category_by_id(self, category_id: str) -> TaskORM:
        return self.db.get(TaskORM, category_id)
    
    def create_category(self, name: str) -> TaskORM:
        new_category = TaskORM(name = name, completed=False)
        self.db.add(new_category)
        self.db.commit()
        return new_category
    
    def delete_category(self, TaskORM) -> None:
        self.db.delete(TaskORM)