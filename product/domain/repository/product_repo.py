from abc import ABCMeta, abstractmethod
from product.domain.product import Product

class IProductRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_check_id(self, product_id: int) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def get_product_count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_users(self, start_page: int, end_page: int) -> list[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def get_user(self, product_id: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def save(self, product: Product) -> Product:
        raise NotImplementedError