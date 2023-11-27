from fastapi import FastAPI
import app.config.mongo_config

app = FastAPI()

@app.get("/health")
async def read_root():
    return {"ok": True}