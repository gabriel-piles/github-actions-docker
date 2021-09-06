from fastapi import FastAPI
import sys

app = FastAPI()


@app.get('/info')
async def info():
    return sys.version
