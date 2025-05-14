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

class Seller(Base):

    __tablename__ = "th_sellers"

    __table_args__ = {"comment": "판매자 정보 테이블"}

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), 
        primary_key=True,
        autoincrement=True, 
        comment="판매자 테이블 Primary Key"
    )
    business_code: Mapped[str] = mapped_column(String(10), nullable=False, index=True, comment="사업자등록번호") 
    owner_name: Mapped[str] = mapped_column(String(50), nullable=False, index=True, comment="대표자명")
    compony_name: Mapped[str] = mapped_column(String(80), nullable=False, index=True, comment="업체명")
    adress: Mapped[int] = mapped_column(String(140), nullable=True, comment="업체주소")
    tel: Mapped[str] = mapped_column(String(15), nullable=True, comment="전화번호")
    phone: Mapped[str] = mapped_column(String(15), nullable=True, comment="개인전화")
    view_flag: Mapped[int] = mapped_column(TINYINT(1, unsigned=True), default=0, nullable=False, comment="노출여부")
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