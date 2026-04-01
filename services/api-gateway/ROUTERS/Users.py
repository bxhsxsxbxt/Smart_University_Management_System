from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import USER_SERVICE

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/me")
async def me(request: Request):
    return await forward(request, f"{USER_SERVICE}/users/me", "user", cache_key="users_me")

@router.put("/me")
async def update_me(request: Request):
    return await forward(request, f"{USER_SERVICE}/users/me", "user")

@router.get("/{uid}")
async def get_user(uid: str, request: Request):
    return await forward(request, f"{USER_SERVICE}/users/{uid}", "user", cache_key=f"user_{uid}")

@router.get("/")
async def list_users(request: Request):
    return await forward(request, f"{USER_SERVICE}/users", "user", cache_key="users_list")
