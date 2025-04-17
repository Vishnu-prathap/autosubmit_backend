
from fastapi import FastAPI
from repository.db_config import client
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/check-db")
def check_db():
    try:
        client.admin.command('ping')
        return JSONResponse(content={"status": "✅ MongoDB is connected!"})
    except Exception as e:
        return JSONResponse(content={"status": "❌ Error", "message": str(e)}, status_code=500)