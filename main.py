import uvicorn
from fastapi import FastAPI
from routes import router as services_router

app = FastAPI(title="Vikings Healthcare Ecommerce Project")
app.include_router(services_router ,prefix="/service")

@app.get("/health")
async def read_root():
    return {"ok": True}

# uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)