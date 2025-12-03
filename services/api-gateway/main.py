from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ROUTERS import Auth, Users, Market, Shuttle, Reserve, Exam, IOT
from UTILS.AuthMiddleware import verify_jwt

app = FastAPI(title="University Platform API Gateway")

# to connect with front end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JWT Middleware
@app.middleware("http")
async def jwt_middleware(request, call_next):
    return await verify_jwt(request, call_next)

# Routes
app.include_router(Auth.router)
app.include_router(Users.router)
app.include_router(Market.router)
app.include_router(Shuttle.router)
app.include_router(Reserve.router)
app.include_router(Exam.router)
app.include_router(IOT.router)
