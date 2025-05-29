from promotions import Promotion

class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def __str__(self):
        return f"{self.name} - ${self.price}, Quantity: {self.quantity}"

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        promo_info = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_info}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available.")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price



class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def is_active(self) -> bool:
        return True  # Always active, even if quantity is 0

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return quantity * self.price  # No quantity deduction

    def show(self) -> str:
        return f"{self.name} (Non-Stocked), Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of this product.")
        return super().buy(quantity)

