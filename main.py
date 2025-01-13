from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/status")
def read_status():
    return {"message": "Server is up & running!"}

