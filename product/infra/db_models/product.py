#from sqlalchemy import String, INTEGER

# mysql의 unsigned를 써야하기 때문에
from sqlalchemy import String
from sqlalchemy.dialects.mysql import INTEGER 

from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Product(Base):

    __tablename__ = "th_products"

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(8), nullable=False, index=True) 
    name: Mapped[str] = mapped_column(String(30), nullable=False, index=True)