from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CategoriesORM(Base):
    __tablename__ = "categories"
    
    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)