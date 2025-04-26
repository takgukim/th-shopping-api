from abc import ABCMeta, abstractclassmethod
from product.domain.product import Product

class IProductRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def save(self, product: Product):
        raise NotImplementedError