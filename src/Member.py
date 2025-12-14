from typing import Dict
from abstract_library_item import AbstractLibraryItem


class Member:
    """
    Represents a library member/patron.

    This class models the *person* using the library system.
    It focuses on identity, account status, and item ownership,
    while delegating transaction logic (dates, fines) to Checkout.

    Integrated original responsibilities:
    - validate_member_id(member_id)
    - account activation / deactivation
    - fine tracking and payment

    Added architectural responsibilities:
    - Composition: Member "has-a" collection of LibraryItem objects
    - Borrowing eligibility checks
    """

    def __init__(self, member_id: str, name: str, email: str, join_date):
        """
        Initialize a library member with validation.

        Args:
            member_id (str): Unique member identifier (e.g., "MEM12345")
            name (str): Full name of the member
            email (str): Email address
            join_date (str/date): Date member joined the library

        Validation:
            - member_id must be valid format
            - name must be non-empty
            - email must contain '@'

        Private Attributes:
            _member_id (str): Unique identifier (read-only)
            _name (str): Member's full name
            _email (str): Member's email
            _join_date (str/date): Join date
            _active (bool): Account status
            _fines_owed (float): Outstanding fines

            _checked_out_items (dict): COMPOSITION
                Key: item_id
                Value: AbstractLibraryItem
        """
        if not self.validate_id(member_id):
            raise ValueError("Invalid member ID format")

        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")

        if "@" not in email:
            raise ValueError("Invalid email address")

        self._member_id = member_id
        self._name = name
        self._email = email
        self._join_date = join_date
        self._active = True
        self._fines_owed = 0.0

        # Composition: items currently checked out by this member
        self._checked_out_items: Dict[str, AbstractLibraryItem] = {}

    # ─────────────────────────────
    # Properties
    # ─────────────────────────────

    @property
    def member_id(self):
        """str: Read-only member ID."""
        return self._member_id

    @property
    def name(self):
        """str: Member name."""
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def email(self):
        """str: Member email."""
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value

    @property
    def active(self):
        """bool: Whether the account is active."""
        return self._active

    @property
    def fines_owed(self):
        """float: Outstanding fines."""
        return self._fines_owed

    @property
    def checked_out_items(self):
        """dict: Items currently checked out by the member."""
        return self._checked_out_items

    # ─────────────────────────────
    # Integrated Original Methods
    # ─────────────────────────────

    def validate_id(self, member_id: str) -> bool:
        """
        Verify that a member ID is valid.

        ORIGINAL METHOD: validate_member_id(member_id)

        Rules:
            - Non-empty string
            - Starts with 'MEM'
            - Reasonable length
        """
        return (
            isinstance(member_id, str)
            and member_id.startswith("MEM")
            and len(member_id) >= 5
        )

    def pay_fine(self, amount: float) -> float:
        """
        Record a fine payment.

        Args:
            amount (float): Payment amount

        Returns:
            float: Remaining balance
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive")

        self._fines_owed = max(0.0, self._fines_owed - amount)
        return self._fines_owed

    # ─────────────────────────────
    # Borrowing & Composition Logic
    # ─────────────────────────────

    def can_checkout(self) -> bool:
        """
        Determine if the member is eligible to check out items.

        Rules:
            - Account must be active
            - No outstanding fines
        """
        return self._active and self._fines_owed == 0.0

    def add_checked_out_item(self, item: AbstractLibraryItem):
        """
        Register an item as checked out by this member.

        Called by Checkout after successful validation.
        """
        self._checked_out_items[item.item_id] = item

    def remove_checked_out_item(self, item_id: str):
        """
        Remove an item from the member's checked-out list.

        Called by Checkout during returns.
        """
        self._checked_out_items.pop(item_id, None)

    # ─────────────────────────────
    # Account Control
    # ─────────────────────────────

    def deactivate(self):
        """
        Deactivate the member account.
        Prevents future checkouts.
        """
        self._active = False

    # ─────────────────────────────
    # String Representations
    # ─────────────────────────────

    def __str__(self):
        status = "Active" if self._active else "Inactive"
        return (
            f"{self._name} ({self._member_id}) - {status} | "
            f"Fines: ${self._fines_owed:.2f} | "
            f"Items Checked Out: {len(self._checked_out_items)}"
        )

    def __repr__(self):
        return (
            f"Member(member_id='{self._member_id}', "
            f"name='{self._name}', email='{self._email}', "
            f"active={self._active}, fines_owed={self._fines_owed})"
        )
