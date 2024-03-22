from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)

# Iniciar el server: uvicorn users:app --reload


# Entidad user

"""
@router.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "John",
            "surname": "Doe",
            "age": 25,
            "url": "https://fastapi.tiangolo.com",
        },
        {
            "name": "Jane",
            "surname": "Diu",
            "age": 26,
            "url": "https://fastapi.tiangolo.com",
        },
        {
            "name": "Mat",
            "surname": "Dao",
            "age": 27,
            "url": "https://fastapi.tiangolo.com",
        },
    ]
"""


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str


users_list = [
    User(id=1, name="John", surname="Doe", age=25, url="https://fastapi.tiangolo.com"),
    User(id=2, name="Jane", surname="Diu", age=26, url="https://fastapi.tiangolo.com"),
    User(id=3, name="Mat", surname="Dao", age=27, url="https://fastapi.tiangolo.com"),
]


@router.get("/")
async def users():
    return users_list


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except Exception:
        return {"error": "user not found"}


# Path
@router.get("/{id}")
async def get_user(id: int):
    return search_user(id)


# Query
@router.get("/query")
async def get_user_query(id: int):
    return search_user(id)


@router.post("/create_user", response_model=User, status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="user already exists")
    users_list.append(user)
    return user


@router.put("/update_user")
async def update_user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    return user if found else {"error": "user not found"}


@router.delete("/delete_user/{id}")
async def delete_user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            users_list.pop(index)
            found = True
    return saved_user if found else {"error": "user not found"}
