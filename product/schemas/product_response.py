from pydantic import BaseModel, Field

class ProductResponse(BaseModel):
    id: int
    code: str
    name: str
    price: int
    use_flag: int

    class Config:
        orm_mode = True
