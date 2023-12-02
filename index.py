import uvicorn
from main import app

if __name__ == "__main__":
    host = 'localhost'
    port = 8000
    uvicorn.run(app=app, host=host, port=port)
    