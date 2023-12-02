from fastapi import FastAPI
import app.config.mongo_config
from app.routes import router as services_router

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"ok": True}

app.include_router(services_router)