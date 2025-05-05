from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    code: str
    name: str

    class Config:
        orm_mode = True
