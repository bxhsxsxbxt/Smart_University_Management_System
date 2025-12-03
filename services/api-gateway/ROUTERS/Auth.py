from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import AUTH_SERVICE

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.post("/register")
async def register(request: Request):
    return await forward(request, f"{AUTH_SERVICE}/auth/register", "auth")

@router.post("/login")
async def login(request: Request):
    return await forward(request, f"{AUTH_SERVICE}/auth/login", "auth")

@router.post("/refresh")
async def refresh(request: Request):
    return await forward(request, f"{AUTH_SERVICE}/auth/refresh", "auth")

@router.get("/verify")
async def verify(request: Request):
    return await forward(request, f"{AUTH_SERVICE}/auth/verify", "auth")
