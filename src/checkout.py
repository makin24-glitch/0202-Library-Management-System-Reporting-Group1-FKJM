from datetime import timedelta

class Checkout:
    def __init__(self, checkout_id, member, item, checkout_date):
        # Check if the member is active
        if not member.active:
            raise ValueError("Member is not active")

        # Check if the item can be checked out
        if item.status != "available":
            raise ValueError("Item is not available")

        self._checkout_id = checkout_id
        self._member = member
        self._item = item
        self._checkout_date = checkout_date

        # Calculate when the item is due
        loan_period = item.calculate_loan_period()
        self._due_date = self.calculate_due_date(checkout_date, loan_period)

        self._return_date = None
        self._status = "active"

        # Change item status so no one else can borrow it
        item.status = "checked_out"

    def checkout_id(self):
        return self._checkout_id

    def member(self):
        return self._member

    def item(self):
        return self._item

    def checkout_date(self):
        return self._checkout_date

    def due_date(self):
        return self._due_date

    def status(self):
        return self._status

    # This function figures out the due date
    def calculate_due_date(self, checkout_date, loan_period):
        return checkout_date + timedelta(days=loan_period)

    # This creates a dictionary with checkout info
    def generate_record(self):
        record = {
            "checkout_id": self._checkout_id,
            "member_id": self._member.member_id,
            "item_id": self._item.item_id,
            "checkout_date": self._checkout_date,
            "due_date": self._due_date,
            "status": self._status
        }
        return record

    # This runs when the item is returned
    def process_return(self, return_date):
        self._return_date = return_date

        # Calculate fine if returned late
        fine = self._member.calculate_fines(
            self._due_date, return_date, 0.25
        )

        # Update item and checkout status
        self._item.status = "available"
        self._status = "returned"

        return {
            "fine": fine,
            "status": self._status
        }

    def __str__(self):
        return (
            "Checkout " + str(self._checkout_id) +
            ": " + self._member.name +
            " borrowed " + self._item.title
        )

    def __repr__(self):
        return "Checkout(" + str(self._checkout_id) + ")"
