from typing import Iterable
from interfaces import PriceCalculator


class Product:
    def __init__(self, *, name: str, category: str, price_in_cents: int):
        self.name = name
        self.category = category
        self.price_in_cents = price_in_cents
        if self.price_in_cents < 0:
            raise ValueError("product price cannot be negative")

    def __str__(self) -> str:
        return self.name


class SimplePriceCalculator:
    def calculate_total_price(self, products: Iterable[Product]) -> int:
        return sum(product.price_in_cents for product in products)


class Checkout:
    def __init__(self, price_calculator: PriceCalculator) -> None:
        self.price_calculator = price_calculator
        self._scanned_items: list[Product] = []

    def scan(self, product: Product) -> None:
        self._scanned_items.append(product)

    def get_total_price_in_cents(self) -> int:
        return self.price_calculator.calculate_total_price(
            self._scanned_items
        )

    def get_scanned_items(self) -> list[Product]:
        return self._scanned_items.copy()
