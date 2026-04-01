from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import RESOURCE_SERVICE

router = APIRouter(prefix="/api/shuttle", tags=["Shuttle"])

@router.get("/routes")
async def get_routes(request: Request):
    return await forward(
        request,
        f"{RESOURCE_SERVICE}/shuttle/routes",
        "resource",
        cache_key="shuttle_routes"
    )

@router.get("/location")
async def get_live_location(request: Request):
    return await forward(
        request,
        f"{RESOURCE_SERVICE}/shuttle/location",
        "resource",
        cache_key="shuttle_location"
    )
