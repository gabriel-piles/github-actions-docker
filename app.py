from fastapi import FastAPI
from data import Data
from get_logger import get_logger

app = FastAPI()

logger = get_logger()


@app.get('/')
async def info():
    logger.info('info')
    return Data(paragraphs=['a']).json()
