import unittest
from tests._test_utils import *  # noqa

from Member import Member
from LibraryItem import LibraryItem
from Checkout import Checkout

class TestUnitMember(unittest.TestCase):
    def test_member_creation(self):
        m = Member("M001", "Alice Johnson", "Student")
        self.assertEqual(m.member_id, "M001")
        self.assertEqual(m.name, "Alice Johnson")
        self.assertEqual(m.member_type, "Student")

    def test_member_invalid_id_raises(self):
        with self.assertRaises(ValueError):
            Member("", "Alice", "Student")


class TestUnitLibraryItem(unittest.TestCase):
    def test_item_creation(self):
        item = LibraryItem("B100", "Python Basics", "J. Doe", "Technology")
        self.assertEqual(item.item_id, "B100")
        self.assertEqual(item.title, "Python Basics")

    def test_item_invalid_id_raises(self):
        with self.assertRaises(ValueError):
            LibraryItem("", "Title", "Author", "Category")


class TestUnitCheckout(unittest.TestCase):
    def test_checkout_creation(self):
        c = Checkout("B100", "M001")
        self.assertEqual(c.item_id, "B100")
        self.assertEqual(c.member_id, "M001")

    def test_checkout_missing_ids_raise(self):
        with self.assertRaises(ValueError):
            Checkout("", "M001")
        with self.assertRaises(ValueError):
            Checkout("B100", "")

if __name__ == "__main__":
    unittest.main()

