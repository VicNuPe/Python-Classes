import unittest

from camera_kit import CameraKit
from rental_item import RentalItem


def sample_kit() -> CameraKit:
    return CameraKit("Canon", "R6", "CAM-001", "Mirrorless", 45.0)


class TestCameraKit(unittest.TestCase):
    def test_constructor_sets_properties(self) -> None:
        kit = sample_kit()
        self.assertEqual(kit.brand, "Canon")
        self.assertEqual(kit.asset_tag, "CAM-001")
        self.assertEqual(kit.check_rate(), 45.0)
        self.assertFalse(kit.is_booked())

    def test_invalid_constructor_values_raise_value_error(self) -> None:
        cases = [
            ("", "R6", "CAM-001", "Mirrorless", 45.0),
            ("Canon", " ", "CAM-001", "Mirrorless", 45.0),
            ("Canon", "R6", "", "Mirrorless", 45.0),
            ("Canon", "R6", "CAM-001", " ", 45.0),
            ("Canon", "R6", "CAM-001", "Mirrorless", 0.0),
        ]
        for args in cases:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    CameraKit(*args)

    def test_book_twice_then_return(self) -> None:
        kit = sample_kit()
        self.assertTrue(kit.book())
        self.assertFalse(kit.book())
        self.assertTrue(kit.is_booked())
        kit.return_item()
        self.assertFalse(kit.is_booked())
        self.assertTrue(kit.book())

    def test_change_rate_accepts_positive_value(self) -> None:
        kit = sample_kit()
        kit.change_rate(49.5)
        self.assertEqual(kit.check_rate(), 49.5)

    def test_invalid_rate_keeps_original_value(self) -> None:
        kit = sample_kit()
        with self.assertRaises(ValueError):
            kit.change_rate(-1.0)
        self.assertEqual(kit.check_rate(), 45.0)

    def test_display_includes_key_information(self) -> None:
        message = sample_kit().display()
        self.assertIn("Canon R6", message)
        self.assertIn("CAM-001", message)
        self.assertIn("€45.00", message)

    def test_cannot_construct_abstract_rental_item(self) -> None:
        with self.assertRaises(TypeError):
            RentalItem("Canon", "R6", 45.0)


if __name__ == "__main__":
    unittest.main()


class TestRentalCost(unittest.TestCase):
    def test_calculate_three_day_rental(self) -> None:
        self.assertEqual(sample_kit().calculate_cost(3), 135.0)

    def test_rejects_invalid_rental_days(self) -> None:
        for days in [0, -2, 1.5, True]:
            with self.subTest(days=days):
                with self.assertRaises(ValueError):
                    sample_kit().calculate_cost(days)
