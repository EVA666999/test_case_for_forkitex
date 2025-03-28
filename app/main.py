from fastapi import FastAPI

from app.routers import balance

app = FastAPI()

app.include_router(balance.router)
