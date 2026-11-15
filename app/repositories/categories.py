from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.categories import CategoriesORM


class CategoriesRepository:
    def __init__(self, db: Session) -> None:
        self.db = db 
    def get_all_categories(self) -> list[CategoriesORM]:
        return self.db.scalars(select(CategoriesORM)).all()
    
    def get_category_by_id(self, category_id: str) -> CategoriesORM:
        return self.db.get(CategoriesORM, category_id)
    
    def create_category(self, name: str) -> CategoriesORM:
        new_category = CategoriesORM(name = name, completed=False)
        self.db.add(new_category)
        return new_category
    
    def delete_category(self, category: CategoriesORM) -> None:
        self.db.delete(category)