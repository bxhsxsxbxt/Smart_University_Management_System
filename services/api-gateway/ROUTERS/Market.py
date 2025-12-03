from fastapi import APIRouter, Request
from UTILS.Proxy import forward
from UTILS.Services import MARKET_SERVICE

router = APIRouter(prefix="/api/market", tags=["Market"])

@router.get("/products")
async def list_products(request: Request):
    return await forward(
        request,
        f"{MARKET_SERVICE}/products",
        "market",
        cache_key="market_products"
    )

@router.get("/products/{pid}")
async def get_product(pid: str, request: Request):
    return await forward(
        request,
        f"{MARKET_SERVICE}/products/{pid}",
        "market",
        cache_key=f"market_product_{pid}"
    )

@router.post("/products")
async def create_product(request: Request):
    return await forward(
        request,
        f"{MARKET_SERVICE}/products",
        "market"
    )

@router.delete("/products/{pid}")
async def delete_product(pid: str, request: Request):
    return await forward(
        request,
        f"{MARKET_SERVICE}/products/{pid}",
        "market"
    )
