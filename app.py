from fastapi import FastAPI
from data import Data

app = FastAPI()


@app.get('/')
async def info():
    return Data(paragraphs=['a']).json()
