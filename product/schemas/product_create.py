from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    code: str = Field(None, min_length=8, max_length=8, example="12345678")
    name: str = Field(None, min_length=5, max_length=30, example="아이패드 에어13")
    price: int = Field(None, ge = 100, le=1000000, example="금액은 100원 이상부터 100만원까지 가능합니다.")