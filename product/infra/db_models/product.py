from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Product(Base):

    __tablename__ = "th_product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(8), nullable=False, index=True) 
    name: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

