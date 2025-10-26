from pydantic import BaseModel
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None  # или: str | None = None

class STask(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int