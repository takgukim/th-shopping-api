from fastapi import APIRouter 

import example.api.schemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task], tags=["example"])
async def list_tasks():
    return [task_schema.Task(id=1, title="첫번째 ToDO 작업")]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse, tags=["example"])
async def create_task(task_body: task_schema.TaskCreate):
    # **dict는 title=task_body.title, done=task_body.done과 같음
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse, tags=["example"])
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict(), tags=["example"])

@router.delete("/tasks/{task_id}", tags=["example"])
async def delete_task(task_id: int):
    return