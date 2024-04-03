from typing import List
from fastapi import APIRouter

from src.server.routes.search import router as search_router

__all__: List[APIRouter] = [
    search_router
]