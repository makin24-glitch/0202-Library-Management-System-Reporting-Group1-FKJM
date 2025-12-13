from abc import ABC, abstractmethod

class AbstractLibraryItem(ABC):
    """
    Abstract base class for all library items.

    This class defines the interface that all library item types must implement,
    ensuring consistent behavior across different item types.
    """

    def __init__(self, item_id, title, item_type, status="available"):
        if not item_id or not isinstance(item_id, str):
            raise ValueError("item_id must be a non-empty string")
        if not title:
            raise ValueError("title must be provided")
        if status not in {"available", "checked_out"}:
            raise ValueError("Invalid status")

        
        """
        Initialize a library item.

        Args:
            item_id (str): Unique identifier for the item
            title (str): Human-readable title of the item
            item_type (str): Type of item (Book, DVD, Journal, etc.)
            status (str, optional): Availability status ("available" or "checked_out")
        """
        self.item_id = item_id
        self.title = title
        self.item_type = item_type
        self.status = status
        # Placeholder for future composition relationships
        self.transactions = []  # E.g., list of checkouts or history
        self.tags = []          # E.g., keywords or categories

    
    @abstractmethod
    def calculate_loan_period(self) -> int:
        pass

    @abstractmethod
    def calculate_replacement_cost(self) -> float:
        pass


class Book(AbstractLibraryItem):
    def __init__(self, item_id, title, author, status="available"):
        super().__init__(item_id, title, "Book", status)
        self.author = author

    def calculate_loan_period(self):
        return 14

    def calculate_replacement_cost(self):
        return 25.00

    def __str__(self):
        return f"{self.title} by {self.author} ({self.item_id})"

class Journal(AbstractLibraryItem):
    def __init__(self, item_id, title, volume, issue, status="available"):
        super().__init__(item_id, title, "Journal", status)
        self.volume = volume
        self.issue = issue

    def calculate_loan_period(self):
        return 3

    def calculate_replacement_cost(self):
        return 30.00

    def __str__(self):
        return f"{self.title} Vol:{self.volume} Issue:{self.issue} ({self.item_id})"
