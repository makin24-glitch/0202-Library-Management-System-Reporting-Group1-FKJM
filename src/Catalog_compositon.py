from abstract_library_item import AbstractLibraryItem


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
        if not isinstance(catalog_name, str) or not catalog_name.strip():
            raise ValueError("catalog_name must be a non-empty string")

        # Initialize private attributes
        self._catalog_name = catalog_name
        self._items = {}
        self._total_items = 0

    # ------------------------------------------------------------------
    # Property decorators
    # ------------------------------------------------------------------
    @property
    def catalog_name(self):
        """str: Get the catalog name."""
        return self._catalog_name

    @property
    def total_items(self):
        """int: Get the total number of items in catalog."""
        return len(self._items)

    # ------------------------------------------------------------------
    # Core catalog operations
    # ------------------------------------------------------------------
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
        if not isinstance(item, AbstractLibraryItem):
            raise TypeError("Item must be a LibraryItem instance")

        if item.item_id in self._items:
            raise ValueError(f"Item with ID '{item.item_id}' already exists")

        self._items[item.item_id] = item
        self._total_items += 1
        return True

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
        if item_id in self._items:
            del self._items[item_id]
            self._total_items -= 1
            return True

        return False

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
        return self._items.get(item_id)

    # ------------------------------------------------------------------
    # Integrated method from original: search_catalog(query, catalog_data)
    # ------------------------------------------------------------------
    def search_catalog(self, query):
        """
        Search the catalog for items matching a query.

        ORIGINAL METHOD: search_catalog(query, catalog_data)

        Args:
            query (str): Search term(s) entered by user

        Returns:
            list: List of matching LibraryItem objects

        Search Logic:
            - Convert query to lowercase for case-insensitive search
            - Iterate through all items in catalog
            - Check if query appears in:
                - Item title
                - Item type
                - Item ID
            - Add matching items to results list
            - Return list of matches (empty list if no matches)
        """
        if not isinstance(query, str):
            return []

        query = query.lower()
        results = []

        for item in self._items.values():
            if (
                query in item.title.lower()
                or query in item.item_type.lower()
                or query in item.item_id.lower()
            ):
                results.append(item)

        return results

    # ------------------------------------------------------------------
    # Availability helpers
    # ------------------------------------------------------------------
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
        return [
            item for item in self._items.values()
            if item.status == "available"
        ]

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
        return [
            item for item in self._items.values()
            if item.status == "checked_out"
        ]

    # ------------------------------------------------------------------
    # String representations
    # ------------------------------------------------------------------
    def __str__(self):
        """
        User-friendly string representation.

        Returns:
            str: Human-readable catalog description

        Format:
            "{catalog_name}: {total_items} items ({available_count} available, {checked_out_count} checked out)"
        """
        available = len(self.get_available_items())
        checked_out = len(self.get_checked_out_items())

        return (
            f"{self.catalog_name}: {self.total_items} items "
            f"({available} available, {checked_out} checked out)"
        )

    def __repr__(self):
        """
        Developer-friendly string representation.

        Returns:
            str: Unambiguous representation of the Catalog object

        Format:
            "Catalog(catalog_name='...', total_items=...)"
        """
        return (
            f"Catalog(catalog_name='{self.catalog_name}', "
            f"total_items={self.total_items})"
        )
