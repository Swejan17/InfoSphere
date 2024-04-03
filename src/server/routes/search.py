from fastapi import APIRouter
from src.server.core.query_processing import process_query, read_by_id

router = APIRouter(prefix="/api")

@router.get("/search")
async def search(q: str = ""):
    if not len(q):
        return {
            "error": "no input"
        }
    return process_query(q)

@router.get("/findById/{id}")
async def findById(id: str):
    return  read_by_id(id)