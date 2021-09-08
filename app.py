from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def info():
    try:
        with open('./docker_volume/a.txt', mode='w') as file:
            file.write('works')
        return 'works'
    except Exception as e:
        return str(e)
