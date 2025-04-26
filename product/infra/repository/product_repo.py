from fastapi import HTTPException
from utils.db_utils import row_to_dict

from database import SessionLocal

from product.domain.repository.product_repo import IProductRepository
from product.domain.product import Product as ProductVO
from product.infra.db_models.product import Product

class ProductRepository(IProductRepository):
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