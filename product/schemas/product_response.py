from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    code: str
    name: str
    price: int

    class Config:
        orm_mode = True
