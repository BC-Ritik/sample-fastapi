from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/status")
def read_status():
    return {"message": "Server is up & running!"}


@app.get("/dashboard")
def get_dashboard():
    return {"message": "you have successfully hit dashboard API!"}

