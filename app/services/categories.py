from sqlalchemy.orm import Session

from app.repositories.categories import CategoriesRepository
from app.schemas.categories import (
    CategoriesCreateSchema,
    CategoriesSchema,
    CategoriesUpdateSchema,
)


class CategoriesNotFound(Exception):
    pass


class CategoriesService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.categories_repository = CategoriesRepository(db)
    def list_categories(self) -> list[CategoriesSchema]:
        categories_orm = self.categories_repository.get_all_categories()
        return [CategoriesSchema.model_validate(categories) for categories in categories_orm]
    
    def create_category(self, categories_create: CategoriesCreateSchema) -> CategoriesSchema:
        categories_orm = self.categories_repository.create_category(name=categories_create.name)
        self.db.commit()
        return CategoriesSchema.model_validate(categories_orm)
    
    def update_category(
        self,
        category_id: str,
        categories_update: CategoriesUpdateSchema) -> CategoriesSchema:
        
    
        category_for_update = self.categories_repository.get_category_by_id(category_id=category_id)
        if not category_for_update:
            raise CategoriesNotFound("Category not found")
        if categories_update.name is not None:
            category_for_update.name = categories_update.name
        if categories_update.completed is not None:
            category_for_update.completed = categories_update.completed
        self.db.commit()
        return CategoriesSchema.model_validate(category_for_update)
        
    def delete_category(self, category_id: str) -> None:
        category_for_delete = self.categories_repository.get_category_by_id(category_id=category_id)
        if not category_for_delete:
            raise CategoriesNotFound("Category not found")
        self.categories_repository.delete_category(category_for_delete)
        self.db.commit()