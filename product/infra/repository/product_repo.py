from fastapi import HTTPException
from utils.db_utils import row_to_dict

from database import SessionLocal, engine

from sqlalchemy import text

from product.domain.repository.product_repo import IProductRepository
from product.domain.product import Product as ProductVO
from product.infra.db_models.product import Product

class ProductRepository(IProductRepository):

    def get_users(self, start_page: int, end_page: int) -> list[ProductVO]:
        
        with engine.connect() as conn:
            query = text("SELECT id, code, name FROM th_product LIMIT :start_page, :end_page")

            result = conn.execute(query, {"start_page" : start_page, "end_page" : end_page}).mappings()

            return [dict(row) for row in result]

    def save(self, product: ProductVO) -> ProductVO:
        
        new_product = Product(
            code = product.code,
            name = product.name,
        )

        with SessionLocal() as db:

            try:
                db = SessionLocal()
                db.add(new_product)
            finally:
                db.commit()
                db.refresh(new_product)

        return new_product