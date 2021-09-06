from fastapi import FastAPI
import sys

app = FastAPI()


@app.get('/')
async def info():
    return sys.version
