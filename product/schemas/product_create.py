from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    code: str = Field(..., min_length=8, max_length=8, example="12345678")
    name: str = Field(..., min_length=5, max_length=30, example="아이패드 에어13")
    price: int = Field(..., ge = 100, le=1000000, example="금액은 100원 이상부터 100만원까지 가능합니다.")
    created_user: str = Field(..., min_length=2, max_length=50, example="등록자 이름을 입력해주세요.")