from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "CogniCart Engine-1 running"}
