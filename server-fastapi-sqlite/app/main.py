from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from fastapi.middleware.cors import CORSMiddleware

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
