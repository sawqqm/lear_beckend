from pydantic import BaseModel, ConfigDict


class CategoriesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str
    completed: bool
        
    
class CategoriesCreateSchema(BaseModel):
    name: str
    
    
class CategoriesUpdateSchema(BaseModel):
    name: str | None = None
    completed: bool | None = None