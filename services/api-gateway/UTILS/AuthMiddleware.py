from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from UTILS.Services import AUTH_SERVICE
import httpx

PUBLIC_PATHS = [
    "/api/auth/login",
    "/api/auth/register",
    "/api/auth/refresh"
]

async def verify_jwt(request: Request, call_next):
    path = request.url.path

    # general paths dont need token verification
    if any(path.startswith(p) for p in PUBLIC_PATHS):
        return await call_next(request)

    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse(status_code=401, content={"detail": "Missing Authorization header"})

    # Token verifying
    try:
        async with httpx.AsyncClient(timeout=0.4) as client:
            resp = await client.get(
                f"{AUTH_SERVICE}/auth/verify",
                headers={"Authorization": token},
            )

        if resp.status_code != 200:
            return JSONResponse(status_code=401, content={"detail": "Invalid or expired token"})

    except:
        raise HTTPException(503, "Auth service unavailable")

    return await call_next(request)
