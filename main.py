from fastapi import FastAPI
from routes import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)


# url local: http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hello FastAPI!"


# url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}
