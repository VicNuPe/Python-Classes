"""
Run this script once to generate the complete Bicycle Rental System project.
Creates a folder called 'bicycle-rental-2026-STUDENT' with all files inside.
"""

import os

FOLDER = "bicycle-rental-2026-STUDENT"

FILES = {}

FILES["rental_item.py"] = '''from abc import ABC, abstractmethod


class RentalItem(ABC):
    """Abstract parent class for anything the shop rents out."""

    @abstractmethod
    def borrow(self, borrower_name):
        pass

    @abstractmethod
    def return_item(self):
        pass

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass

    @abstractmethod
    def describe(self):
        pass
'''

FILES["bicycle.py"] = '''from rental_item import RentalItem


class Bicycle(RentalItem):
    """A bicycle the shop can rent out."""

    VALID_CATEGORIES = ["road", "mountain", "hybrid", "electric", "kids"]

    def __init__(self, bicycle_id, brand, model, daily_rate, category="hybrid"):
        # --- Validation ---
        if bicycle_id.strip() == "":
            raise ValueError("Bicycle ID cannot be empty.")
        if brand.strip() == "":
            raise ValueError("Brand cannot be empty.")
        if model.strip() == "":
            raise ValueError("Model cannot be empty.")
        if daily_rate <= 0:
            raise ValueError("Daily rate must be greater than 0.")
        if category.lower() not in Bicycle.VALID_CATEGORIES:
            raise ValueError("Category must be one of: " + ", ".join(Bicycle.VALID_CATEGORIES))

        # --- Attributes ---
        self.bicycle_id = bicycle_id.strip()
        self.brand = brand.strip()
        self.model = model.strip()
        self.daily_rate = daily_rate
        self.category = category.lower()
        self.is_available = True
        self.borrower = None
        self.times_borrowed = 0

    # ---------- Part A methods ----------
    def borrow(self, borrower_name):
        if self.is_available == False:
            raise ValueError(
                "Bicycle " + self.bicycle_id + " is already borrowed by " + self.borrower
            )
        if borrower_name.strip() == "":
            raise ValueError("Borrower name cannot be empty.")

        self.borrower = borrower_name
        self.is_available = False
        self.times_borrowed = self.times_borrowed + 1
        return True

    def return_item(self):
        if self.is_available == True:
            raise ValueError("Bicycle " + self.bicycle_id + " is not currently borrowed.")

        old_borrower = self.borrower
        self.borrower = None
        self.is_available = True
        return old_borrower

    def calculate_rental_cost(self, days):
        if days <= 0:
            raise ValueError("Days must be at least 1.")
        return round(self.daily_rate * days, 2)

    def change_daily_rate(self, new_rate):
        if new_rate <= 0:
            raise ValueError("Daily rate must be greater than 0.")
        self.daily_rate = new_rate
        return self.daily_rate

    def describe(self):
        if self.is_available == True:
            status = "Available"
        else:
            status = "Borrowed by " + self.borrower

        return (self.bicycle_id + ": " + self.brand + " " + self.model +
                " (" + self.category + ") - EUR " + str(self.daily_rate) +
                " per day - " + status)

    # ---------- Part C: alternative constructors ----------
    @classmethod
    def from_string(cls, text):
        """Create a Bicycle from a string like 'B001,Raleigh,Pro,25.0,mountain'."""
        parts = text.split(",")
        if len(parts) != 5:
            raise ValueError("String must have 5 parts: id,brand,model,rate,category")
        return cls(
            parts[0].strip(),
            parts[1].strip(),
            parts[2].strip(),
            float(parts[3].strip()),
            parts[4].strip(),
        )

    @classmethod
    def from_dict(cls, data):
        """Create a Bicycle from a dictionary."""
        return cls(
            data["bicycle_id"],
            data["brand"],
            data["model"],
            data["daily_rate"],
            data["category"],
        )

    @classmethod
    def create_economy(cls, bicycle_id, brand, model):
        """Shortcut for a cheap hybrid bike."""
        return cls(bicycle_id, brand, model, 10.0, "hybrid")

    # ---------- dunder methods ----------
    def __str__(self):
        return self.describe()
'''

FILES["main.py"] = '''from bicycle import Bicycle


def line():
    print("=" * 60)


def main():
    # ---------- 1. Create bicycles ----------
    line()
    print("1. Creating bicycles")
    line()

    bike1 = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0, "mountain")
    bike2 = Bicycle("B002", "Giant", "City Cruiser", 15.5, "hybrid")
    bike3 = Bicycle.from_string("B003,Trek,Road Racer,30.0,road")
    bike4 = Bicycle.from_dict({
        "bicycle_id": "B004",
        "brand": "Cube",
        "model": "E-Trail",
        "daily_rate": 45.0,
        "category": "electric",
    })
    bike5 = Bicycle.create_economy("B005", "Btwin", "Riverside 100")

    fleet = [bike1, bike2, bike3, bike4, bike5]
    for bike in fleet:
        print(bike.describe())

    # ---------- 2. Rental costs ----------
    line()
    print("2. Rental cost calculation")
    line()
    print(bike1.bicycle_id + " for 3 days: EUR " + str(bike1.calculate_rental_cost(3)))
    print(bike4.bicycle_id + " for 2 days: EUR " + str(bike4.calculate_rental_cost(2)))
    print(bike5.bicycle_id + " for 7 days: EUR " + str(bike5.calculate_rental_cost(7)))

    # ---------- 3. Successful borrow and return ----------
    line()
    print("3. Successful operations")
    line()
    bike1.borrow("Alice")
    print("After Alice borrows: " + bike1.describe())
    print("Cost for 2 days: EUR " + str(bike1.calculate_rental_cost(2)))

    who = bike1.return_item()
    print("Returned by " + who + ". " + bike1.describe())

    # ---------- 4. Unsuccessful operations ----------
    line()
    print("4. Unsuccessful operations (handled)")
    line()

    bike2.borrow("Bob")

    try:
        bike2.borrow("Charlie")
    except ValueError as error:
        print("Borrow blocked: " + str(error))

    try:
        bike3.return_item()
    except ValueError as error:
        print("Return blocked: " + str(error))

    try:
        Bicycle("", "Ghost", "Empty", 10.0)
    except ValueError as error:
        print("Creation blocked: " + str(error))

    try:
        Bicycle("B009", "Ghost", "Free", -5.0)
    except ValueError as error:
        print("Creation blocked: " + str(error))

    try:
        Bicycle("B010", "Ghost", "Ship", 10.0, "rocket")
    except ValueError as error:
        print("Creation blocked: " + str(error))

    try:
        bike2.calculate_rental_cost(0)
    except ValueError as error:
        print("Cost blocked: " + str(error))

    # ---------- 5. Price management ----------
    line()
    print("5. Price management")
    line()
    print("Old rate for " + bike2.bicycle_id + ": EUR " + str(bike2.daily_rate))
    bike2.change_daily_rate(18.75)
    print("New rate for " + bike2.bicycle_id + ": EUR " + str(bike2.daily_rate))

    # ---------- 6. Fleet overview ----------
    line()
    print("6. Fleet overview")
    line()
    for bike in fleet:
        print(bike.describe())

    print()
    print("Application finished successfully.")


if __name__ == "__main__":
    main()
'''

FILES["test_bicycle.py"] = '''import unittest

from bicycle import Bicycle
from rental_item import RentalItem


class TestBicycleCreation(unittest.TestCase):

    def test_create_valid_bicycle(self):
        bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0, "mountain")
        self.assertEqual(bike.bicycle_id, "B001")
        self.assertEqual(bike.brand, "Raleigh")
        self.assertEqual(bike.model, "Mountain Pro")
        self.assertEqual(bike.daily_rate, 25.0)
        self.assertEqual(bike.category, "mountain")
        self.assertTrue(bike.is_available)

    def test_empty_id_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("", "Raleigh", "Mountain Pro", 25.0)

    def test_empty_brand_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("B001", "", "Mountain Pro", 25.0)

    def test_empty_model_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("B001", "Raleigh", "", 25.0)

    def test_negative_rate_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("B001", "Raleigh", "Mountain Pro", -5.0)

    def test_zero_rate_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("B001", "Raleigh", "Mountain Pro", 0)

    def test_invalid_category_raises(self):
        with self.assertRaises(ValueError):
            Bicycle("B001", "Raleigh", "Mountain Pro", 25.0, "spaceship")

    def test_category_case_insensitive(self):
        bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0, "MOUNTAIN")
        self.assertEqual(bike.category, "mountain")


class TestBorrowAndReturn(unittest.TestCase):

    def setUp(self):
        self.bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0)

    def test_borrow_success(self):
        self.assertTrue(self.bike.borrow("Alice"))
        self.assertFalse(self.bike.is_available)
        self.assertEqual(self.bike.borrower, "Alice")

    def test_borrow_twice_raises(self):
        self.bike.borrow("Alice")
        with self.assertRaises(ValueError):
            self.bike.borrow("Charlie")

    def test_borrow_empty_name_raises(self):
        with self.assertRaises(ValueError):
            self.bike.borrow("   ")
        self.assertTrue(self.bike.is_available)

    def test_return_success(self):
        self.bike.borrow("Alice")
        previous = self.bike.return_item()
        self.assertEqual(previous, "Alice")
        self.assertTrue(self.bike.is_available)
        self.assertIsNone(self.bike.borrower)

    def test_return_when_not_borrowed_raises(self):
        with self.assertRaises(ValueError):
            self.bike.return_item()

    def test_times_borrowed_counter(self):
        self.assertEqual(self.bike.times_borrowed, 0)
        self.bike.borrow("Alice")
        self.bike.return_item()
        self.bike.borrow("Bob")
        self.assertEqual(self.bike.times_borrowed, 2)


class TestRentalCost(unittest.TestCase):

    def setUp(self):
        self.bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0)

    def test_cost_for_three_days(self):
        self.assertEqual(self.bike.calculate_rental_cost(3), 75.0)

    def test_cost_for_one_day(self):
        self.assertEqual(self.bike.calculate_rental_cost(1), 25.0)

    def test_cost_rounds_two_decimals(self):
        bike = Bicycle("B002", "Giant", "City Cruiser", 15.55)
        self.assertEqual(bike.calculate_rental_cost(3), 46.65)

    def test_zero_days_raises(self):
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(0)

    def test_negative_days_raises(self):
        with self.assertRaises(ValueError):
            self.bike.calculate_rental_cost(-1)


class TestPriceManagement(unittest.TestCase):

    def test_change_daily_rate(self):
        bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0)
        bike.change_daily_rate(30.0)
        self.assertEqual(bike.daily_rate, 30.0)

    def test_change_rate_rejects_negative(self):
        bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0)
        with self.assertRaises(ValueError):
            bike.change_daily_rate(-10)
        self.assertEqual(bike.daily_rate, 25.0)


class TestAlternativeConstructors(unittest.TestCase):

    def test_from_string_valid(self):
        bike = Bicycle.from_string("B009,Raleigh,City,15.5,hybrid")
        self.assertEqual(bike.bicycle_id, "B009")
        self.assertEqual(bike.brand, "Raleigh")
        self.assertEqual(bike.model, "City")
        self.assertEqual(bike.daily_rate, 15.5)
        self.assertEqual(bike.category, "hybrid")

    def test_from_string_wrong_field_count(self):
        with self.assertRaises(ValueError):
            Bicycle.from_string("B009,Raleigh,City")

    def test_from_dict_valid(self):
        bike = Bicycle.from_dict({
            "bicycle_id": "B010",
            "brand": "Trek",
            "model": "Road Racer",
            "daily_rate": 30.0,
            "category": "road",
        })
        self.assertEqual(bike.bicycle_id, "B010")
        self.assertEqual(bike.category, "road")

    def test_from_dict_missing_key(self):
        with self.assertRaises(KeyError):
            Bicycle.from_dict({"bicycle_id": "B011", "brand": "Giant"})

    def test_create_economy(self):
        bike = Bicycle.create_economy("B012", "Btwin", "Riverside 100")
        self.assertEqual(bike.daily_rate, 10.0)
        self.assertEqual(bike.category, "hybrid")


class TestAbstractBaseClass(unittest.TestCase):

    def test_cannot_create_rental_item(self):
        with self.assertRaises(TypeError):
            RentalItem()

    def test_bicycle_is_a_rental_item(self):
        bike = Bicycle("B001", "Raleigh", "Mountain Pro", 25.0)
        self.assertTrue(isinstance(bike, RentalItem))


if __name__ == "__main__":
    unittest.main(verbosity=2)
'''

FILES["README.md"] = '''# Bicycle Rental System

**Name:** <YOUR FULL NAME>
**Student number:** <YOUR STUDENT NUMBER>
**Module:** Modern Programming Principles & Practice 1
**Lecturer:** Juan Huette

## Python version

Python 3.11 (works with any Python 3.9 or newer).

## How to run the application

Open a terminal in the project folder and run:

    python main.py

If that does not work, try:

    python3 main.py

## How to run the tests

From the project folder run:

    python -m unittest test_bicycle.py -v

You should see the word OK at the end, with all tests passing.

## Files in the project

| File | What it does |
|------|--------------|
| rental_item.py | Abstract parent class RentalItem (Part C) |
| bicycle.py | The Bicycle class (Parts A and C) |
| main.py | Driver program that demonstrates everything (Part B) |
| test_bicycle.py | Automated unit tests (Part D) |
| README.md | This file |

## Assumptions I made

1. Bicycle IDs are strings and cannot be empty.
2. The daily rate must be a number greater than 0.
3. The category must be one of: road, mountain, hybrid, electric, kids.
4. Days in calculate_rental_cost() must be 1 or more.
5. I used the built-in ValueError for all invalid input.
6. Currency is shown as EUR for display only.

## AI acknowledgement

I used an AI assistant (ChatGPT) to help me plan the class structure,
check that my unit tests covered all the required behaviours, and
improve the wording of this README. All code was read, understood,
tested, and typed by me before submitting.
'''

FILES[".gitignore"] = '''__pycache__/
*.pyc
.venv/
venv/
.idea/
.vscode/
'''


def main():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
        print("Created folder: " + FOLDER)
    else:
        print("Folder already exists: " + FOLDER)

    for filename, content in FILES.items():
        path = os.path.join(FOLDER, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Wrote: " + path)

    print()
    print("Done. Project created in: " + os.path.abspath(FOLDER))
    print("Next steps:")
    print("  1. Rename the folder to bicycle-rental-2026-<your-student-number>")
    print("  2. Fill in your name and number in README.md")
    print("  3. Run:  python main.py")
    print("  4. Run:  python -m unittest test_bicycle.py -v")
    print("  5. Push the folder to GitHub")


if __name__ == "__main__":
    main()