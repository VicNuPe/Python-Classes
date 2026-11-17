from rental_item import RentalItem
from datetime import datetime, timedelta


class CameraKit(RentalItem):
    def __init__(self, brand: str, model: str, daily_rate: float) -> None:
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Brand cannot be empty")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model cannot be empty")
        if isinstance(daily_rate, bool) or not isinstance(daily_rate, (int, float)):
            raise ValueError("Daily rate must be a number")
        if not 0 <= daily_rate < float("inf"):
            raise ValueError("Daily rate must be a finite, non-negative number.")

        self.brand = brand
        self.model = model
        self.daily_rate = float(daily_rate)
        self._booked = False
        self._rented_at = None
        self._return_by = None
        self._rental_days = 0

    @property
    def booked(self) -> bool:
        return self._booked

    def display(self) -> None:
        print("=" * 40)
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Daily rate: €{self.daily_rate:.2f}")
        print(f"Booked: {self._booked}")
        print(f"Date & time rented:    {self._rented_at}")
        print(f"Date & time to return: {self._return_by}")

    def book(self) -> None:
        if self._booked:
            print("Camera kit is already booked")
        else:
            days = int(input("How many days would you like to rent? "))
            self._booked = True
            self._rental_days = days
            self._rented_at = datetime.now()
            self._return_by = self._rented_at + timedelta(days=days)
            print("Camera kit has been booked")

    def return_item(self) -> None:
        if self._booked:
            self._booked = False
            self._rented_at = None
            self._return_by = None
            self._rental_days = 0
            print("Camera kit has been returned")
        else:
            print("Camera kit has not been booked")

    def is_booked(self) -> bool:
        return self._booked
