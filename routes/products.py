from fastapi import APIRouter


router = APIRouter(
    prefix="/products", tags=["products"], responses={404: {"description": "Not found"}}
)


products_list = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 200},
    {"id": 3, "name": "Product 3", "price": 300},
]


@router.get("/")
async def get_products():
    return products_list


@router.get("/{id}")
async def get_product(id: int):
    return products_list[id - 1]
