from fastapi import HTTPException, status
from utils.db_utils import row_to_dict

from datetime import datetime

from database import SessionLocal, engine

from sqlalchemy import text

from product.domain.repository.product_repo import IProductRepository
from product.domain.product import Product as ProductVO
from product.infra.db_models.product import Product

class ProductRepository(IProductRepository):

    def get_products(self, start_page: int, end_page: int) -> tuple[int, list[ProductVO]]:
        with SessionLocal() as db:
            query = db.query(Product)\
                .filter_by(deleted_datetime = None)
            
            total = query.count()

            # 페이징
            products = query.limit(end_page).offset(start_page).all()

        return {
            "product_count" : total,
            "products" : products
        }
    
    def get_product(self, product_id: int) -> ProductVO:
        with SessionLocal() as db:
            product = db.query(Product)\
                .filter_by(deleted_datetime = None)\
                .filter(Product.id == product_id)\
                .first()

            if not product:
                raise HTTPException(status.HTTP_404_NOT_FOUND, detail="제품 정보를 찾을 수 없습니다") 

        return product

    def save(self, product: ProductVO) -> ProductVO:
        
        new_product = Product(
            code = product.code,
            name = product.name,
            price = product.price,
            created_user = product.created_user,
            created_datetime = datetime.now().replace(microsecond=0)
        )

        with SessionLocal() as db:

            try:
                db = SessionLocal()
                db.add(new_product)
            finally:
                db.commit()
                db.refresh(new_product)

        return new_product
    
    def update(self, updates: ProductVO) -> ProductVO:

        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == updates.id).first()
    
            product.name = updates.name
            product.price = updates.price
            product.updated_user = updates.updated_user
            product.updated_datetime = datetime.now().replace(microsecond=0)
            
            db.add(product)
            db.commit()

        return product
    
    def update_usg_flag(self, product_id: int, updates: ProductVO) -> Product:

        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()
    
            product.use_flag = updates.use_flag
            product.updated_user = updates.updated_user
            product.updated_datetime = datetime.now().replace(microsecond=0)
            
            db.add(product)
            db.commit()
            db.refresh(product)

        return product
    
    def delete(self, product_id: int) -> ProductVO:
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()

            if product.use_flag == 1:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="사용 중인 제품은 삭제 할 수 없습니다.") 

            db.delete(product)
            db.commit()

        return product
    
    def soft_delete(self, product_id: int, deletes: ProductVO) -> Product:
        with SessionLocal() as db:
            product = db.query(Product).filter(Product.id == product_id).first()

            if product.use_flag == 1:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, detail="사용 중인 제품은 삭제 할 수 없습니다.") 
    
            product.deleted_user = deletes.deleted_user
            product.deleted_datetime = datetime.now().replace(microsecond=0)
            
            db.add(product)
            db.commit()

        return product