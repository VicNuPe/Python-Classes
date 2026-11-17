"""Shared properties and compulsory behaviour for rental items."""

from abc import ABC, abstractmethod


class RentalItem(ABC):
    def __init__(self, brand: str, model: str, daily_rate: float) -> None:
        if not brand or not brand.strip():
            raise ValueError("Brand cannot be empty")
        if not model or not model.strip():
            raise ValueError("Model cannot be empty")
        if daily_rate <= 0:
            raise ValueError("Daily rate must be greater than zero")

        self.brand = brand.strip()
        self.model = model.strip()
        self.daily_rate = float(daily_rate)
        self._booked = False

    @abstractmethod
    def display(self) -> str:
        """Describe this item for the user."""
        ...
