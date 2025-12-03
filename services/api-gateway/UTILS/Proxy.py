import httpx
import json
from fastapi import Request, HTTPException
from UTILS.CircuitBreaker import circuit_breakers
from UTILS.Cache import get_cache, set_cache

TIMEOUT = 0.4
CACHEABLE_METHODS = ["GET"]


async def forward(request: Request, url: str, service: str, cache_key=None):
    breaker = circuit_breakers[service]

    # Circuit Breaker
    breaker.allow()

    # Cache
    if request.method in CACHEABLE_METHODS and cache_key:
        cached = await get_cache(cache_key)
        if cached:
            try:
                return json.loads(cached)
            except:
                return cached

    # Extract headers 
    headers = dict(request.headers)

    try:
        body = await request.body()
    except:
        body = None

    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            resp = await client.request(
                method=request.method,
                url=url,
                headers=headers,
                content=body,
            )

        # Parse JSON or raw text
        if "application/json" in resp.headers.get("content-type", ""):
            data = resp.json()
        else:
            data = resp.text

        breaker.success()

        if cache_key and request.method in CACHEABLE_METHODS:
            await set_cache(cache_key, data)

        return data

    except Exception:
        breaker.failure()
        raise HTTPException(502, f"{service} service unavailable")
