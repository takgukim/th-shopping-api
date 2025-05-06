#from sqlalchemy import String, INTEGER

# mysql의 unsigned를 써야하기 때문에
from sqlalchemy import String, text

from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.mysql import TINYINT

from sqlalchemy.sql import func

from sqlalchemy import DateTime
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Product(Base):

    __tablename__ = "th_products"

    __table_args__ = {"comment": "제품 기본정보 테이블"}

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), 
        primary_key=True,
        autoincrement=True, 
        comment="제품 테이블 Primary Key"
    )
    code: Mapped[str] = mapped_column(String(8), nullable=False, index=True, comment="제품 고유 코드") 
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True, comment="제품명")
    price: Mapped[int] = mapped_column(INTEGER(unsigned=True), default = 0, comment="제품 가격")
    use_flag: Mapped[int] = mapped_column(TINYINT(1), default=0, nullable=False, comment="현재 판매 또는 사용중인 제품")
    created_user: Mapped[str] = mapped_column(
        String(50), 
        nullable=False,
        server_default=text("'system'"),
        comment="등록자 - 아이디 정보 생성시 아이디+이름으로 표기 예정"
    )
    created_datetime: Mapped[datetime] = mapped_column(
        DateTime, 
        nullable=False,
        server_default=func.now(),
        comment="등록시각"
    )
    updated_user: Mapped[str] = mapped_column(
        String(50), 
        nullable=True,
        comment="수정자 - 아이디 정보 생성시 아이디+이름으로 표기 예정"
    )
    updated_datetime: Mapped[datetime] = mapped_column(
        DateTime, 
        nullable=True,
        comment="수정시각"
    )
    deleted_user: Mapped[str] = mapped_column(
        String(50), 
        nullable=True,
        comment="삭제자 - 아이디 정보 생성시 아이디+이름으로 표기 예정"
    )
    deleted_datetime: Mapped[datetime] = mapped_column(
        DateTime, 
        nullable=True,
        comment="삭제시각"
    )