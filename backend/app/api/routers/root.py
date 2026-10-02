"""Health and metadata endpoints."""

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root():
    return {"message": "Todo API", "version": "1.0.0"}
