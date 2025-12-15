import unittest
from tests._test_utils import *  # noqa

from Catalog_compositon import CatalogComposition
from Member import Member
from LibraryItem import LibraryItem

class TestSystemEndToEnd(unittest.TestCase):
    def test_end_to_end_workflow(self):
        catalog = CatalogComposition()
        catalog.add_member(Member("M999", "System User", "Student"))
        catalog.add_item(LibraryItem("B999", "System Book", "Sys", "Tech"))

        catalog.checkout_item("B999", "M999")
        catalog.return_item("B999")

        item = catalog.get_item("B999")
        self.assertEqual(item.status.lower(), "available")

if __name__ == "__main__":
    unittest.main()

