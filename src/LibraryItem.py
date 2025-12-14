"""
Concrete library item classes for the Library Management System.

This module defines specific library items (Book, DVD, Journal) that inherit
from AbstractLibraryItem and follow the interface requirements.
"""

from abstract_library_item import AbstractLibraryItem  # assuming your ABC is in this file


class Book(AbstractLibraryItem):
    """Concrete class representing a book."""

    def __init__(self, item_id: str, title: str, author: str, status: str = "available"):
        """
        Initialize a Book object.

        Args:
            item_id (str): Unique ID for the book
            title (str): Book title
            author (str): Book author
            status (str, optional): Availability status ("available"/"checked_out")
        """
        super().__init__(item_id, title, "Book", status)
        self.author = author
        # self.transactions and self.tags inherited from ABC

    def calculate_loan_period(self):
        """Calculate loan period for a book. Future logic: typically 14 days."""
        return 14

    def calculate_replacement_cost(self):
        """Calculate replacement cost for a book."""
        return 25.00

    def __str__(self):
        return f"{self.title} by {self.author} ({self.item_id})"


class DVD(AbstractLibraryItem):
    """Concrete class representing a DVD."""

    def __init__(self, item_id: str, title: str, runtime_minutes: int, status: str = "available"):
        """
        Initialize a DVD object.

        Args:
            item_id (str): Unique ID
            title (str): DVD title
            runtime_minutes (int): Duration in minutes
            status (str, optional): Availability
        """
        super().__init__(item_id, title, "DVD", status)
        self.runtime_minutes = runtime_minutes

    def calculate_loan_period(self):
        """Calculate loan period for a DVD. Future logic: typically 7 days."""
        return 7

    def calculate_replacement_cost(self):
        """Calculate replacement cost for a DVD."""
        return 40.00

    def __str__(self):
        return f"{self.title} ({self.runtime_minutes} mins) [{self.item_id}]"


class Journal(AbstractLibraryItem):
    """Concrete class representing a journal."""
