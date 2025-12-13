# services/checkout_service.py

from checkout import Checkout


def create_checkout(checkout_id, member, item, checkout_date):
    """
    Service function that creates a Checkout transaction.

    Raises:
        ValueError if checkout cannot proceed
    """
    if not member.active:
        raise ValueError("Member account is inactive")

    if item.status != "available":
        raise ValueError("Item is not available")

    checkout = Checkout(
        checkout_id=checkout_id,
        member=member,
        item=item,
        checkout_date=checkout_date
    )

    return checkout
