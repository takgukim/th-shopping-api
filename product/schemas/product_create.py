from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    code: str = Field(None, min_length=8, max_length=8, example="12345678")
    name: str = Field(None, min_length=5, max_length=30, example="아이패드 에어13")