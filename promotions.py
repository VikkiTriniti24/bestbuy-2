from abc import ABC, abstractmethod
import math

class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass

class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        total = product.price * quantity
        discount = total * (self.percent / 100)
        return total - discount

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * product.price * 1.5) + (remainder * product.price)

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity: int) -> float:
        full_price_quantity = quantity - (quantity // 3)
        return full_price_quantity * product.price
