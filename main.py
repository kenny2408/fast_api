from fastapi import FastAPI

app = FastAPI()


# url local: http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hello FastAPI!"

# url local: http://127.0.0.1:8000/url	
@app.get("/url")
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}
