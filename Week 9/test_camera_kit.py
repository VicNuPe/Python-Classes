import unittest
from camera_kit import CameraKit


class CameraKitTests(unittest.TestCase):
    def setUp(self):
        self.kit = CameraKit("Canon", "EOS R8", 90.00)

    def test_new_kit_is_available(self):
        self.assertFalse(self.kit.is_booked())

    def test_book_changes_status(self):
        self.kit.book()
        self.assertTrue(self.kit.is_booked())

    def test_return_changes_status(self):
        self.kit.book()
        self.kit.return_item()
        self.assertFalse(self.kit.is_booked())

    def test_return_without_booking(self):
        self.kit.return_item()
        self.assertFalse(self.kit.is_booked())


if __name__ == "__main__":
    unittest.main()
