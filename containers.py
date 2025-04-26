from dependency_injector import containers, providers
from product.application.product_service import ProductService

from product.infra.repository.product_repo import ProductRepository

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=["product"],
    )

    product_repo = providers.Factory(ProductRepository)
    product_service = providers.Factory(ProductService, product_repo=product_repo)