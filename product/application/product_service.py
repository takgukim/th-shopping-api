from fastapi import HTTPException, status

from dependency_injector.wiring import inject, Provide

from product.domain.product import Product
from product.domain.repository.product_repo import IProductRepository

class ProductService:
    @inject
    def __init__(
        self,
        product_repo: IProductRepository,
    ):
        self.product_repo = product_repo

    def get_products(self, start_page: int, end_page: int) -> tuple[int, list[Product]]:
        new_start_page = (start_page - 1) * end_page

        products = self.product_repo.get_users(new_start_page, end_page)

        # 현재 제품 카운트 가져온다
        # 추후 검색 조건 넣을 경우 검색되는거만 조회되도록 할 것 
        product_count = self.product_repo.get_product_count()

        return {
            "product_count" : product_count,
            "products" : products,
        }
    
    def get_product(self, product_id: int) -> Product: 

        exist_count = self.product_repo.get_check_id(product_id)

        if exist_count < 1:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="제품 코드를 확인해주세요") 

        product = self.product_repo.get_user(product_id)

        return product

    def create_product(self, code: str, name: str) -> Product:

        product: Product = Product(
            code=code,
            name=name,
        )

        new_product = self.product_repo.save(product)

        return new_product