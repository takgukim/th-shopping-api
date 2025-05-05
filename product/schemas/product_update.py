from pydantic import BaseModel, Field

class ProductUpdate(BaseModel):
    name: str = Field(None, min_length=5, max_length=30, example="아이패드 에어13")
    price: int = Field(None, ge = 100, le=1000000, example="금액은 100원 이상부터 100만원까지 가능합니다.")

    class Config:
        orm_mode = True
