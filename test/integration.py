import unittest
from tests._test_utils import *  # noqa

from Catalog_compositon import CatalogComposition
from Member import Member
from LibraryItem import LibraryItem

class TestIntegrationCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = CatalogComposition()

    def test_add_member_and_item(self):
        start_m = len(self.catalog.members)
        start_i = len(self.catalog.items)

        self.catalog.add_member(Member("M900", "Test User", "Student"))
        self.catalog.add_item(LibraryItem("B900", "Test Book", "Tester", "Tech"))

        self.assertEqual(len(self.catalog.members), start_m + 1)
        self.assertEqual(len(self.catalog.items), start_i + 1)

    def test_checkout_and_return_flow(self):
        self.catalog.add_member(Member("M901", "Checkout User", "Student"))
        self.catalog.add_item(LibraryItem("B901", "Checkout Book", "Author", "Tech"))

        # If your method names differ, tell me what they are and I’ll adjust.
        self.catalog.checkout_item("B901", "M901")
        item = self.catalog.get_item("B901")
        self.assertNotEqual(item.status.lower(), "available")

        self.catalog.return_item("B901")
        item2 = self.catalog.get_item("B901")
        self.assertEqual(item2.status.lower(), "available")

if __name__ == "__main__":
    unittest.main()

