"""Concrete camera kit: inheritance, booking rules and rate changes."""

from rental_item import RentalItem


class CameraKit(RentalItem):
    def __init__(
        self, brand: str, model: str,
        asset_tag: str, kit_type: str, daily_rate: float
    ) -> None:
        super().__init__(brand, model, daily_rate)
        if not asset_tag or not asset_tag.strip():
            raise ValueError("Asset tag cannot be empty")
        if not kit_type or not kit_type.strip():
            raise ValueError("Kit type cannot be empty")
        self.asset_tag = asset_tag.strip()
        self.kit_type = kit_type.strip()

    def display(self) -> str:
        return (
            f"{self.brand} {self.model} | {self.kit_type} | "
            f"Tag: {self.asset_tag} | Rate: €{self.daily_rate:.2f} | "
            f"Booked: {self._booked}"
        )

    def book(self) -> bool:
        if self._booked:
            return False
        self._booked = True
        return True

    def return_item(self) -> None:
        self._booked = False

    def is_booked(self) -> bool:
        return self._booked

    def check_rate(self) -> float:
        return self.daily_rate

    def change_rate(self, new_rate: float) -> None:
        if new_rate <= 0:
            raise ValueError("Daily rate must be greater than zero")
        self.daily_rate = float(new_rate)

    def calculate_cost(self, days: int) -> float:
        """Week 9 extension: price = rental days * daily rate."""
        if isinstance(days, bool) or not isinstance(days, int) or days <= 0:
            raise ValueError("Rental days must be a positive whole number")
        return days * self.daily_rate
