from sqlalchemy.orm import Session

from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreateSchema, TaskSchema, TaskUpdateSchema


class TaskNotFound(Exception):
    pass

class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)
        
    def list_tasks(self) -> list[TaskSchema]:
        tasks_orm = self.task_repository.get_all_tasks()
        return [TaskSchema.model_validate(task) for task in tasks_orm]
     
    def create_task(self, task_id: str, task_create: TaskCreateSchema) -> TaskSchema:
        task_orm =self.task_repository.create_task(title=task_create.title)
        self.db.commit()
        return TaskSchema.model_validate(task_orm)
    
    def update_task(self, task_id: str, task_updata: TaskUpdateSchema) -> TaskSchema:
        task_for_update = self.task_repository.get_tasks_by_id(task_id=task_id)
    
        task_for_update = self.task_repository.get_tasks_by_id(task_id=task_id)
        if not task_for_update:
            raise TaskNotFound("Task not found")
        if task_updata.title is not None:
            task_for_update.title = task_updata.title
        if task_updata.completed is not None:
            task_for_update.completed = task_updata.completed
        self.db.commit()
        return TaskSchema.model_validate(task_for_update)
    
    def delete_task_by_id(self, task_id: str) -> None:
        task_for_delete = self.task_repository.get_tasks_by_id(task_id=task_id)
        if not task_for_delete:
            raise TaskNotFound("Task not found") 
        self.task_repository.delete_task(task_for_delete)
        self.db.commit()
           

    
        