from pydantic import BaseModel, Field

class ProductSoftDelete(BaseModel):
    deleted_user: str = Field(..., min_length=2, max_length=50, example="삭제자 이름을 입력해주세요.")

    class Config:
        orm_mode = True
