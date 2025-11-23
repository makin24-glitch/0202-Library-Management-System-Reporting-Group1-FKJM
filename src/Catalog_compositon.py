class Catalog:
    """
    Represents the library's catalog of all items.
    Demonstrates composition: Catalog "has-a" collection of LibraryItem objects.
    
    This class integrates the following original method:
    - search_catalog(query, catalog_data)
    """
    
    def __init__(self, catalog_name):
        """
        Initialize a catalog with validation.
        
        Args:
            catalog_name (str): Name of the catalog (e.g., "Main Library Catalog")
            
        Validation:
            - Ensure catalog_name is non-empty string
            
        Private Attributes:
            _catalog_name: Name of the catalog
            _items: Dictionary storing LibraryItem objects (COMPOSITION)
                   Key: item_id, Value: LibraryItem object
            _total_items: Count of items in catalog
        """
        # Validate catalog_name
        # Initialize private _items as empty dictionary
        # Set _total_items to 0
        pass
    
    # Property decorators
    @property
    def catalog_name(self):
        """str: Get the catalog name."""
        # Return private _catalog_name
        pass
    
    @property
    def total_items(self):
        """int: Get the total number of items in catalog."""
        # Return private _total_items or len(_items)
        pass
    
    def add_item(self, item):
        """
        Add a library item to the catalog.
        
        Args:
            item (LibraryItem): LibraryItem object to add
            
        Returns:
            bool: True if successfully added, False otherwise
            
        Validation:
            - Ensure item is a LibraryItem instance
            - Ensure item_id doesn't already exist in catalog
            - Raise ValueError if validation fails
            
        Logic:
            - Add item to _items dictionary with item_id as key
            - Increment _total_items
            - Return True
        """
        pass
    
    def remove_item(self, item_id):
        """
        Remove a library item from the catalog.
        
        Args:
            item_id (str): ID of item to remove
            
        Returns:
            bool: True if successfully removed, False if not found
            
        Logic:
            - Check if item_id exists in _items
            - If exists, remove from dictionary
            - Decrement _total_items
            - Return True if removed, False if not found
        """
        pass
    
    def get_item(self, item_id):
        """
        Retrieve a specific item from the catalog.
        
        Args:
            item_id (str): ID of item to retrieve
            
        Returns:
            LibraryItem: Item object if found, None otherwise
            
        Logic:
            - Look up item_id in _items dictionary
            - Return LibraryItem object or None
        """
        pass
    
    # Integrated method from original: search_catalog(query, catalog_data)
    def search_catalog(self, query, catalog_data):
        """
        Search the catalog for items matching a query.
        
        ORIGINAL METHOD: search_catalog(query, catalog_data)
        
        Args:
            query (str): Search term(s) entered by user
            catalog_data (dict/list): Complete catalog of library items
                                     (can use self._items as catalog_data)
        
        Returns:
            list: List of matching LibraryItem objects
            
        Search Logic:
            - Convert query to lowercase for case-insensitive search
            - Iterate through all items in catalog_data
            - Check if query appears in:
                - Item title
                - Item type
                - Item ID
                - Any other searchable attributes
            - Add matching items to results list
            - Return list of matches (empty list if no matches)
        """
        pass
    
    def get_available_items(self):
        """
        Get all items that are currently available for checkout.
        
        Returns:
            list: List of available LibraryItem objects
            
        Logic:
            - Iterate through all items in _items
            - Filter for items where status == "available"
            - Return list of available items
        """
        pass
    
    def get_checked_out_items(self):
        """
        Get all items that are currently checked out.
        
        Returns:
            list: List of checked out LibraryItem objects
            
        Logic:
            - Iterate through all items in _items
            - Filter for items where status == "checked_out"
            - Return list of checked out items
        """
        pass
    
    def __str__(self):
        """
        User-friendly string representation.
        
        Returns:
            str: Human-readable catalog description
            
        Format:
            "{catalog_name}: {total_items} items ({available_count} available, {checked_out_count} checked out)"
        """
        pass
    
    def __repr__(self):
        """
        Developer-friendly string representation.
        
        Returns:
            str: Unambiguous representation of the Catalog object
            
        Format:
            "Catalog(catalog_name='...', total_items=...)"
        """
        pass

