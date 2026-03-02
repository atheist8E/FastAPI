import os
import httpx
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def hello(name: str = "World"):
    return {"message": f"Hello {name}!", "status": "Cloud Run is running"}

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port = int("8000"))