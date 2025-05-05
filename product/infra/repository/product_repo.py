from fastapi import HTTPException
from utils.db_utils import row_to_dict

from database import SessionLocal, engine

from sqlalchemy import text

from product.domain.repository.product_repo import IProductRepository
from product.domain.product import Product as ProductVO
from product.infra.db_models.product import Product

class ProductRepository(IProductRepository):

    def get_check_id(self, product_id : int) -> int:
         with engine.connect() as conn:
            query = text("""
                SELECT count(id) AS cnt
                FROM th_products 
                WHERE id = :id
            """)

            result = conn.execute(query, {
                "id" : product_id
            }).mappings()

            data = result.fetchone()

            return data.cnt
         
    def get_product_count(self) -> int:
        with engine.connect() as conn:
            query = text("""
                SELECT count(id) AS cnt
                FROM th_products
            """)

            result = conn.execute(query).mappings()

            data = result.fetchone()

            return data.cnt

    def get_users(self, start_page: int, end_page: int) -> list[ProductVO]:
        
        with engine.connect() as conn:
            query = text("""
                SELECT id, code,  name 
                FROM th_products 
                LIMIT :start_page, :end_page
            """)

            result = conn.execute(query, {
                "start_page" : start_page, 
                "end_page" : end_page
            }).mappings()

            return [dict(row) for row in result]
    
    def get_user(self, product_id: int) -> ProductVO:
        with engine.connect() as conn:
            query = text("""
                SELECT id, code,  name 
                FROM th_products 
                WHERE id = :id
            """)

            result = conn.execute(query, {
                "id" : product_id
            }).mappings()

            return result.fetchone()

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