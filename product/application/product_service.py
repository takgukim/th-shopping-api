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

    def create_product(self, code: str, name: str) -> Product:

        product: Product = Product(
            id=0,
            code=code,
            name=name,
        )

        new_product = self.product_repo.save(product)

        return new_product