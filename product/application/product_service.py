from fastapi import HTTPException, status

from dependency_injector.wiring import inject, Provide

from product.domain.product import Product
from product.domain.repository.product_repo import IProductRepository

from product.schemas.product_create import ProductCreate
from product.schemas.product_update import ProductUpdate

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

    def create_product(self, product_create : ProductCreate) -> Product:

        product: Product = Product(
            code=product_create.code,
            name=product_create.name,
            price=product_create.price
        )

        new_product = self.product_repo.save(product)

        return new_product
    
    def update_product(self, product_id: int, product_update: ProductUpdate) -> Product:
     
        product = self.product_repo.get_product(product_id)

        if product_update.name:
            product.name = product_update.name

        if product_update.price:
            product.price = product_update.price

        self.product_repo.update(product)

        return product
    
    def delete_product(self, product_id: int):

        product = self.product_repo.get_product(product_id)

        self.product_repo.delete(product_id)

        return product