from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="CogniCart Engine-1")

app.include_router(router)

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "engine-1"
    }
