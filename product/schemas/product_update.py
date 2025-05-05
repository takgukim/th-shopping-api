from pydantic import BaseModel, Field

class ProductUpdate(BaseModel):
    name: str = Field(None, min_length=5, max_length=30, example="아이패드 에어13")

    class Config:
        orm_mode = True
