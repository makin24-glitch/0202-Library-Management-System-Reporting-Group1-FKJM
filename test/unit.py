import unittest
import os, sys
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from Member import Member
from LibraryItem import Book, DVD
from Catalog_compositon import Catalog

class TestUnitMember(unittest.TestCase):
    def test_member_valid(self):
        m = Member("MEM01", "Alice", "alice@test.com", date.today())
        self.assertTrue(m.active)
        self.assertEqual(m.fines_owed, 0.0)

    def test_member_invalid_id_raises(self):
        with self.assertRaises(ValueError):
            Member("BAD", "Alice", "alice@test.com", date.today())

class TestUnitItems(unittest.TestCase):
    def test_book_loan_period(self):
        book = Book("B1", "Python", "Doe")
        self.assertEqual(book.calculate_loan_period(), 14)

    def test_dvd_loan_period(self):
        dvd = DVD("D1", "Movie", 120)
        self.assertEqual(dvd.calculate_loan_period(), 7)

class TestUnitCatalog(unittest.TestCase):
    def test_catalog_add_get_remove(self):
        c = Catalog("Main")
        book = Book("B2", "Test", "Author")
        c.add_item(book)
        self.assertIsNotNone(c.get_item("B2"))
        self.assertTrue(c.remove_item("B2"))
        self.assertIsNone(c.get_item("B2"))

if __name__ == "__main__":
    unittest.main()

