from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import RESOURCE_SERVICE

router = APIRouter(prefix="/api/reserve", tags=["Reserve"])

@router.get("/rooms")
async def list_rooms(request: Request):
    return await forward(
        request,
        f"{RESOURCE_SERVICE}/rooms",
        "resource",
        cache_key="rooms_list"
    )

@router.post("/rooms/{room_id}")
async def reserve_room(room_id: str, request: Request):
    return await forward(
        request,
        f"{RESOURCE_SERVICE}/rooms/{room_id}",
        "resource"
    )

@router.get("/my-reservations")
async def my_reservations(request: Request):
    return await forward(
        request,
        f"{RESOURCE_SERVICE}/reservations/me",
        "resource",
        cache_key="my_reservations"
    )
