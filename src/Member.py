class Member:
    """
    Represents a library member/patron.
    
    This class integrates the following original methods:
    - validate_member_id(member_id)
    - compute_overdue_fine(due_date, return_date, daily_rate)
    """
    
    def __init__(self, member_id, name, email, join_date):
        """
        Initialize a library member with validation.
        
        Args:
            member_id (str): Unique member identifier (e.g., "MEM12345")
            name (str): Full name of the member
            email (str): Email address
            join_date (str/date): Date member joined the library
            
        Validation:
            - Ensure member_id follows format (non-empty, specific pattern)
            - Ensure name is non-empty string
            - Ensure email contains '@' symbol
            - Validate join_date is valid date
            
        Private Attributes:
            _member_id: Unique identifier (read-only)
            _name: Member's full name
            _email: Member's email address
            _join_date: Date joined library
            _active: Account status (default: True)
            _fines_owed: Current outstanding fines (default: 0.0)
        """

         self._member_id = member_id
        self._name = name
        self._email = email
        self._join_date = join_date
        self._active = True  # default status
        
        # Validate all parameters
        # Set private attributes
        pass
    
    # Property decorators
    @property
    def member_id(self):
        """str: Get the member ID (read-only)."""
        # Return private _member_id
        pass
    
    @property
    def name(self):
        """str: Get the member's name."""
        # Return private _name
        pass
    
    @name.setter
    def name(self, value):
        """Set the member's name with validation."""
        # Validate non-empty string
        # Set private _name
        pass
    
    @property
    def email(self):
        """str: Get the member's email."""
        # Return private _email
        pass
    
    @email.setter
    def email(self, value):
        """Set the member's email with validation."""
        # Validate email format (contains @)
        # Set private _email
        pass
    
    @property
    def active(self):
        """bool: Get whether the member account is active."""
        # Return private _active
        pass
    
    @property
    def fines_owed(self):
        """float: Get the total fines owed by the member."""
        # Return private _fines_owed
        pass
    
    # Integrated method from original: validate_member_id(member_id)
    def validate_id(self, member_id):
        """
        Verify that a member ID is valid.
        
        ORIGINAL METHOD: validate_member_id(member_id)
        
        Args:
            member_id (str): The member's unique identifier
        
        Returns:
            bool: True if valid, False otherwise
            
        Validation Logic:
            - Check member_id is non-empty string
            - Check member_id follows expected format (e.g., starts with "MEM")
            - Check member_id length is appropriate
            - Return True if all checks pass
        """
        pass
    
    # Integrated method from original: compute_overdue_fine(due_date, return_date, daily_rate)
    def calculate_fines(self, due_date, return_date, daily_rate):
        """
        Calculate overdue fines for late returns.
        
        ORIGINAL METHOD: compute_overdue_fine(due_date, return_date, daily_rate)
        
        Args:
            due_date (str/date): When item should have been returned
            return_date (str/date): When item was actually returned
            daily_rate (float): Fine amount per day overdue
        
        Returns:
            float: Total fine amount owed
            
        Calculation Logic:
            - Convert dates to comparable format if needed
            - Calculate days_overdue = return_date - due_date
            - If days_overdue <= 0, return 0.0
            - Otherwise, calculate fine = days_overdue * daily_rate
            - Add fine to member's _fines_owed
            - Return fine amount
        """
        pass
    
    def pay_fine(self, amount):
        """
        Record a fine payment.
        
        Args:
            amount (float): Amount being paid
            
        Returns:
            float: Remaining balance after payment
            
        Logic:
            - Validate amount is positive
            - Subtract amount from _fines_owed
            - Ensure _fines_owed doesn't go negative
            - Return new balance
        """
        pass
    
    def deactivate(self):
        """
        Deactivate member account (e.g., membership expired or terminated).
        
        Logic:
            - Set _active to False
            - Prevent new checkouts when inactive
        """
        pass
    
    def __str__(self):
        """
        User-friendly string representation.
        
        Returns:
            str: Human-readable member description
            
        Format:
            "{name} ({member_id}) - Active/Inactive | Fines: ${fines_owed}"
            Example: "Alice Johnson (MEM12345) - Active | Fines: $2.50"
        """
        pass
    
    def __repr__(self):
        """
        Developer-friendly string representation.
        
        Returns:
            str: Unambiguous representation of the Member object
            
        Format:
            "Member(member_id='...', name='...', email='...', active=..., fines_owed=...)"
        """
