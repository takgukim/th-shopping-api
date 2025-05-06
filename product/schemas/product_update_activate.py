from pydantic import BaseModel, Field

class ProductUpdateActivate(BaseModel):
    use_flag: int = Field(..., ge = 0, le=1, example="제품 상태 변경 값을 입력하세요 - 0: 사용안함, 1: 사용함")
    updated_user: str = Field(..., min_length=2, max_length=50, example="등록자 이름을 입력해주세요.")

    class Config:
        orm_mode = True
