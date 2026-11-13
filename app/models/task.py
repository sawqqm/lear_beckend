from sqlalchemy.orm import  Mapped, mapped_column

from .base import Base


class TaskORM(Base):
    __tablename__ = "tasks"
    
    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)
    
class CategoriesORM(Base):
    __tablename__ = "categories"
    
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)