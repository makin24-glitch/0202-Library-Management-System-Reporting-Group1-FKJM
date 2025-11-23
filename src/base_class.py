from abc import ABC, abstractmethod

class AbstractLibraryItem(ABC):
    """
    Abstract base class for all library items.

    This class defines the interface that all library item types must implement,
    ensuring consistent behavior across different item types.
    """

    def __init__(self, item_id, title, item_type, status="available"):
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
    def calculate_loan_period(self):
        """
        Calculate the loan period for this item.

        Returns:
            int: Loan period in days
        """
        pass

    @abstractmethod
    def calculate_replacement_cost(self):
        """
        Calculate the replacement cost for this item.

        Returns:
            float: Replacement cost
        """
        pass


  @abstractmethod
  def calculate_replacement_cost():
    """ Calculates replacement costs
        Returns: replacement cost
    """
    pass
