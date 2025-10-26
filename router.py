from fastapi import APIRouter
from fastapi import Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)

@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_task() -> list[STask]:
    list_of_tasks = await TaskRepository.find_all()
    return list_of_tasks