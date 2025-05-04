from abc import ABCMeta, abstractmethod
from product.domain.product import Product

class IProductRepository(metaclass=ABCMeta):

    @abstractmethod
    def get_users(self, start_page: int, end_page: int):
        raise NotImplementedError

    @abstractmethod
    def save(self, product: Product):
        raise NotImplementedError