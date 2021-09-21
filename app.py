from fastapi import FastAPI

from get_logger import get_logger

app = FastAPI()

logger = get_logger()


@app.get('/')
async def info():
    try:
        logger.info('works')
        # with open('./docker_volume/a.txt', mode='w') as file:
        #     file.write('works')
        return 'works'
    except Exception as e:
        return str(e)
