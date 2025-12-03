from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import IOT_SERVICE

router = APIRouter(prefix="/api/iot", tags=["IoT"])

@router.get("/sensor")
async def get_sensor(request: Request):
    return await forward(
        request,
        f"{IOT_SERVICE}/iot/sensor",
        "iot",
        cache_key="iot_sensor"
    )
