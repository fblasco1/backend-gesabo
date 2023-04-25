from fastapi import FastAPI

from app.v1.router.user_router import router as user_router
from app.v1.router.juicio_router import router as juicio_router

app = FastAPI()

app.include_router(user_router)
app.include_router(juicio_router)