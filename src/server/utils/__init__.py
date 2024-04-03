import time, os, json
from os import path
import logging
from src.server.core.tfidf import create_tf_idf

logger = logging.getLogger("uvicorn.info")

def build_assets():
    logger.info("Checking for assets")
    asset_dir = os.listdir(path.join(os.getcwd(), "src", "server", "assets"))
    required_assets = ["content.json","titles.json","IDF.json"]
    if any([x not in asset_dir for x in required_assets]):
        logger.warn("Assets not found. Trying to create assets")
        created = create_tf_idf()
        if created:
            logger.info("Successfully created the assets.")
        else:
            logger.warn("Unable to create the assets. Exiting!!")
            exit(1)