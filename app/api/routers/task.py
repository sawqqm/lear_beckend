from fastapi import APIRouter, Depends, status, HTTPException
from app.api.dependencies import get_task_service
from app.schemas.task import TaskSchema, TaskCreateSchema, TaskUpdataShema
from app.services.task import TaskService

router_task = APIRouter(prefix="/tasks")


@router_task.get("")
def read_tasks(task_service: TaskService = Depends(get_task_service)) -> list[TaskSchema]:
    return task_service.list_tasks()


@router_task.post("", status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreateSchema, 
    task_service: TaskService = Depends(get_task_service) 
    ) -> TaskSchema:
    return task_service.create_task(task_create=payload)

@router_task.patch("/{tasks_id}")
def updata_task(
    payload: TaskUpdataShema, 
    tasks_id: str , 
    task_service: TaskService = Depends(get_task_service)
    ) -> TaskSchema:
    try:
        return task_service.update_task(tasks_id=tasks_id,task_update=payload) )
    execpt TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")

@router_task.delete(
    "/{tasks_id}", status_code=status.HTTP_204_NO_CONTENT,
    task_service: TaskService = Depends(get_task_service))
def delete_task(tasks_id: str ) -> None:
    try:
        return task_service.delete_task(tasks_id=tasks_id)
    execpt TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")