from fastapi import FastAPI
import logging
from src.server.routes import __all__ as ROUTES


app = FastAPI()
logger = logging.getLogger("uvicorn.info")


for router in ROUTES:
    app.include_router(router)
