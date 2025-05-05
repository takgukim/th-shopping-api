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

        products = self.product_repo.get_products(new_start_page, end_page)

        return products
    
    def get_product(self, product_id: int) -> Product: 

        product = self.product_repo.get_product(product_id)

        return product

    def create_product(self, code: str, name: str) -> Product:

        product: Product = Product(
            code=code,
            name=name,
        )

        new_product = self.product_repo.save(product)

        return new_product
    
    def update_product(self, product_id: int, name: str) -> Product:
     
        product = self.product_repo.get_product(product_id)

        if name:
            product.name = name

        self.product_repo.update(product)

        return product
    
    def delete_product(self, product_id: int):

        product = self.product_repo.get_product(product_id)

        self.product_repo.delete(product_id)

        return product