from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class UserPublic(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(UserPublic):
    password: str


users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "DcUeh@example.com",
        "disabled": False,
        "password": "123456",
    },
    "janedoe": {
        "username": "janedoe",
        "full_name": "Jane Doe",
        "email": "6mUeh@example.com",
        "disabled": True,
        "password": "654321",
    },
}


def search_user(username: str):
    if username in users_db:
        return users_db[username]


async def get_current_user(token: str = Depends(oauth2)):
    if user := search_user(token):
        return user
    else:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = search_user(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserDB(**user_dict)
    hashed_password = user.password
    if hashed_password != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/", response_model=list[UserPublic])
async def read_users():
    return [
        {"username": user.username, "email": user.email} for user in users_db.values()
    ]


@router.get("/users/me")
async def read_users_me(current_user: UserPublic = Depends(get_current_user)):
    return UserPublic(
        username=current_user["username"],
        full_name=current_user["full_name"],
        email=current_user["email"],
        disabled=current_user["disabled"],
    )
