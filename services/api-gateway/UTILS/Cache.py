import redis.asyncio as redis
import json

try:
    redis_client = redis.from_url(
        "redis://localhost:6379",
        decode_responses=True
    )
except Exception:
    redis_client = None


async def get_cache(key: str):
    if redis_client is None:
        return None
    try:
        return await redis_client.get(key)
    except:
        return None


async def set_cache(key: str, data, ttl=10):
    if redis_client is None:
        return
    if isinstance(data, (dict, list)):
        data = json.dumps(data)
    try:
        await redis_client.set(key, data, ex=ttl)
    except:
        pass
