from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="template api",
    description="wow",
    version="0.1.0",
)

app.include_router(router)
