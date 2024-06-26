from fastapi import FastAPI
from routes import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


# url local: http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hello FastAPI!"


# url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url": "https://fastapi.tiangolo.com/"}
