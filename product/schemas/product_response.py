from pydantic import BaseModel, Field

class ProductResponse(BaseModel):
    id: int
    code: str
    name: str
    price: int
    use_flag: int = Field(..., ge = 0, le=1, example="제품 상태 변경 값을 입력하세요.")

    class Config:
        orm_mode = True
