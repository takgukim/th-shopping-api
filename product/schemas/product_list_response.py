from pydantic import BaseModel

from product.schemas.product_response import ProductResponse

class ProductListResponse(BaseModel):
    product_count: int
    products: list[ProductResponse]

    class Config:
        orm_mode = True
