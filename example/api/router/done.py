from fastapi import APIRouter

router = APIRouter()

@router.put("/tasks/{task_id}/done", response_model=None, tags=["example"])
async def mark_task_as_done(task_id: int):
    pass

@router.delete("/tasks/{task_id}/done", response_model=None, tags=["example"])
async def unmark_task_as_done(task_id: int):
    pass