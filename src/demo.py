"""
Demo script for the Library Management System.

This script is intended for graders and reviewers to quickly verify that
core system functionality works as expected without requiring a UI.

It demonstrates:
- Catalog initialization
- Loading installed sample data via adapter
- Member creation
- Checkout workflow
- Return workflow
"""

from datetime import date, timedelta

from catalog import Catalog
from checkout import Checkout
from member import Member
from adapters import load_sample_data_into_catalog
from data.sample_data import SAMPLE_ITEMS


def run():
    """
    Execute a simple end-to-end demo of the system.
    """

    print("\n=== Library Management System Demo ===\n")

    # 1. Initialize catalog
    catalog = Catalog("Main Library Catalog")
    load_sample_data_into_catalog(catalog, SAMPLE_ITEMS)

    print("Catalog initialized:")
    print(catalog)
    print()

    # 2. Create member
    member = Member(
        member_id="MEM001",
        name="Alice Johnson",
        email="alice@example.com",
        join_date=date.today()
    )

    print("Member created:")
    print(member)
    print()

    # 3. Select item
    item = catalog.get_item("B001")

    print("Item selected for checkout:")
    print(item)
    print()

    # 4. Checkout item
    checkout = Checkout(
        checkout_id="CHK001",
        member=member,
        item=item,
        checkout_date=date.today()
    )

    print("Checkout completed:")
    print(checkout)
    print()

    # 5. Simulate late return
    return_date = date.today() + timedelta(days=5)
    return_summary = checkout.process_return(return_date)

    print("Return processed:")
    print(return_summary)
    print()

    # 6. Final state
    print("Final Member State:")
    print(member)
    print()

    print("Final Catalog State:")
    print(catalog)

    print("\n=== Demo Complete ===\n")


if __name__ == "__main__":
    run()
