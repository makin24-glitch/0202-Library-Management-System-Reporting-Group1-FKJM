class LibraryItem:
    """
    Represents a general item in the library catalog.
    Serves as the base class for specific item types (Book, DVD, Journal).
    """
    
    def __init__(self, item_id, title, item_type, loan_period=14):
        """
        Initialize a library item with validation.
        
        Args:
            item_id (str): Unique identifier for the item
            title (str): Title of the item
            item_type (str): Type of item ('book', 'dvd', 'journal')
            loan_period (int): Number of days item can be borrowed (default: 14)
            
        Raises:
            ValueError: If item_id or title is empty, or loan_period is negative
            TypeError: If parameters are not the correct type
        """
        # Validation
        if not isinstance(item_id, str) or not item_id.strip():
            raise ValueError("Item ID must be a non-empty string")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        if not isinstance(loan_period, int) or loan_period < 0:
            raise ValueError("Loan period must be a non-negative integer")
        
        # Private attributes (encapsulation)
        self._item_id = item_id
        self._title = title
        self._item_type = item_type
        self._loan_period = loan_period
        self._status = "available"  # Default status
    
    # Property decorators for controlled access
    @property
    def item_id(self):
        """str: Get the item ID (read-only)."""
        '''return self._item_id'''
    
    @property
    def title(self):
        """str: Get the item title."""
        '''return self._title'''
    
    @title.setter
    def title(self, value):
        """Set the item title with validation."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        '''self._title = value'''
    
    @property
    def item_type(self):
        """str: Get the item type (read-only)."""
        '''return self._item_type'''
    
    @property
    def loan_period(self):
        """int: Get the loan period in days."""
        '''return self._loan_period'''
    
    @property
    def status(self):
        """str: Get the current status of the item."""
        '''return self._status'''
    
    # Integrated methods from your 8 core functions
    def check_availability(self, item_id, catalog):
        """
        Check if a specific item is available in the catalog.
        
        Args:
            item_id (str): Unique identifier for the library item
            catalog (dict/list): Collection of library items with status
        
        Returns:
            bool: True if available, False if checked out
        """
        # This method checks ANY item in the catalog, not just this instance
        '''if isinstance(catalog, dict):
            if item_id in catalog:
                return catalog[item_id].get("status") == "available"
        return False'''
    
    def format_display(self, item_data):
        """
        Format item information for clean CLI display.
        
        Args:
            item_data (dict): Dictionary containing item information
        
        Returns:
            str: Formatted string representation of the item
        """
      
        '''item_id = item_data.get("id", "N/A")
        title = item_data.get("title", "Unknown")
        item_type = item_data.get("type", "Unknown")
        status = item_data.get("status", "unknown")
        
        status_symbol = "✓" if status == "available" else "✗"
        return (
            f"╔════════════════════════════════════════╗\n"
            f"║ [{item_id}] {title:<30} ║\n"
            f"║ Type: {item_type:<10} | Status: {status_symbol} {status:<10} ║\n"
            f"╚════════════════════════════════════════╝"
        )'''
    
    def update_status(self, item_id, new_status):
        """
        Update the status of a library item.
        
        Args:
            item_id (str): ID of item to update
            new_status (str): New status value ('available', 'checked_out', 'maintenance')
        
        Returns:
            bool: True if update successful, False otherwise
            
        Raises:
            ValueError: If new_status is not a valid status value
        """
        valid_statuses = ["available", "checked_out", "maintenance", "lost"]
        #if new_status not in valid_statuses:
            #raise ValueError(f"Status must be one of {valid_statuses}")
        
        # Update this instance if the item_id matches
        #if self._item_id == item_id:
            #self._status = new_status
            #return True
        
        #return False
    
    # String representation methods
    def __str__(self):
        """
        User-friendly string representation for display.
        
        Returns:
            str: Human-readable description of the item
        """
        #status = "Available" if self._status == "available" else f"{self._status.replace('_', ' ').title()}"
        #return f"{self._title} ({self._item_type}) - {status}"
    
    def __repr__(self):
        """
        Developer-friendly string representation for debugging.
        
        Returns:
            str: Unambiguous representation of the LibraryItem object
        """
        #return (f"LibraryItem(item_id='{self._item_id}', title='{self._title}', "
                #f"item_type='{self._item_type}', loan_period={self._loan_period}, "
                #f"status='{self._status}')")
