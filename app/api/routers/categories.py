from fastapi import APIRouter, Depends, status, HTTPException
from app.api.dependencies import get_categories_service
from app.schemas.categories import CategoriesSchema, CategoriesCreateSchema, CategoriesUpdateSchema
from app.services.categories import CategoriesService

router_categories = APIRouter(prefix="/categories")

@router_categories.get("")
def read_categories(categories_service: CategoriesService = Depends(get_categories_service)) -> list[CategoriesSchema]:
    return categories_service.list_categories()


@router_categories.post("", status_code=status.HTTP_201_CREATED)
def create_categories(
    payload: CategoriesCreateSchema, 
    categories_service: CategoriesService = Depends(get_categories_service)
    ) -> CategoriesSchema:
    return categories_service.create_categories(categories_create=payload)


@router_categories.patch("/categories/{categories_id}")
def update_categories(
    payload: CategoriesUpdateSchema, 
    categories_id: str,
    categories_service: CategoriesService = Depends(get_categories_service)
    ) -> CategoriesSchema:
    try:
        return categories_service.update_categories(categories_id=categories_id, categories_update=payload)
    except CategoriesNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")  
                    
@router_categories.delete("/categories/{categories_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categories(
    categories_id: str, 
    categories_service: CategoriesService = Depends(get_categories_service)
    ) -> None:
    try:
        return categories_service.delete_categories(categories_id=categories_id)
    except CategoriesNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")