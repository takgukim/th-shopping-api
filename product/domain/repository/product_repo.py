from abc import ABCMeta, abstractmethod
from product.domain.product import Product

class IProductRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_products(self, start_page: int, end_page: int) -> list[Product]:
        raise NotImplementedError
    
    def get_product_count() -> int:
        raise NotImplementedError

    @abstractmethod
    def get_product(self, product_id: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def save(self, product: Product) -> Product:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def update_usg_flag(self, product_id: int, updates: Product) -> Product:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, product_id: int) -> Product:
        raise NotImplementedError
    
    @abstractmethod
    def soft_delete(self, product_id: int, deletes: Product) -> Product:
        raise NotImplementedError