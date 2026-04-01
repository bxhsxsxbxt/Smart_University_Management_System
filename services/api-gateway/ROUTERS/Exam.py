from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import EXAM_SERVICE

router = APIRouter(prefix="/api/exam", tags=["Exam"])

@router.get("/schedule")
async def get_exam_schedule(request: Request):
    return await forward(
        request,
        f"{EXAM_SERVICE}/exam/schedule",
        "exam",
        cache_key="exam_schedule"
    )

@router.get("/{exam_id}")
async def get_exam(exam_id: str, request: Request):
    return await forward(
        request,
        f"{EXAM_SERVICE}/exam/{exam_id}",
        "exam",
        cache_key=f"exam_{exam_id}"
    )

@router.post("/request")
async def submit_request(request: Request):
    return await forward(
        request,
        f"{EXAM_SERVICE}/exam/request",
        "exam"
    )
