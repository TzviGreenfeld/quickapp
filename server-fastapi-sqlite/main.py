from fastapi import FastAPI
from routes.user_routes import router as user_router

app = FastAPI(
    title="users db app",
    description="much CRUD, very REST",
    version="0.1.0",
)

app.include_router(user_router)
