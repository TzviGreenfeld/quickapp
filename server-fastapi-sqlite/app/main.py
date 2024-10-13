from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="users db app",
    description="much CRUD, very REST",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to restrict access to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug_mode = os.getenv('DEBUG')

@app.get("/")
async def root():
    return {
        "database_url": database_url,
        "secret_key": secret_key,
        "debug_mode": debug_mode
    }