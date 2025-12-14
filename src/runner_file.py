"""
Demo runner for the Library Management System.

This module demonstrates:
- Loading sample data
- Catalog population via adapter
- Member creation
- Checkout flow
- Return flow
"""

from datetime import date

from catalog import Catalog
from checkout import Checkout
from member import Member
from data.sample_data import SAMPLE_ITEMS
from adapters import load_sample_data_into_catalog




def run():
    """
    Entry point for demo execution.

    Demonstrates:
    1. Catalog initialization
    2. Sample data loading
    3. Member creation
    4. Checkout transaction
    5. Return transaction
    """

    print("\n=== Library Management System Demo ===\n")

    # ─────────────────────────────
    # 1. Initialize Catalog
    # ─────────────────────────────
    catalog = Catalog("Main Library Catalog")
    load_sample_data_into_catalog(catalog, SAMPLE_ITEMS)

    print(f"Catalog initialized: {catalog}")
    print()

    # ─────────────────────────────
    # 2. Create Member
    # ─────────────────────────────
    member = Member(
        member_id="MEM1001",
        name="Alice Johnson",
        email="alice@example.com",
        join_date=date.today()
    )

    print("Member created:")
    print(member)
    print()

    # ─────────────────────────────
    # 3. Select Item
    # ─────────────────────────────
    item = catalog.get_item("B001")
    print("Selected item for checkout:")
    print(item)
    print()

    # ─────────────────────────────
    # 4. Checkout Item
    # ─────────────────────────────
    checkout = Checkout(
        checkout_id="CHK001",
        member=member,
        item=item,
        checkout_date=date.today()
    )

    member.add_checked_out_item(item)

    print("Checkout completed:")
    print(checkout)
    print()

    # ─────────────────────────────
    # 5. Return Item (simulate late return)
    # ─────────────────────────────
    return_date = date.today().replace(day=date.today().day + 5)

    return_summary = checkout.process_return(return_date)
    member.remove_checked_out_item(item.item_id)

    print("Return processed:")
    print(return_summary)
    print()

    # ─────────────────────────────
    # 6. Final System State
    # ─────────────────────────────
    print("Final Member State:")
    print(member)
    print()

    print("Final Catalog State:")
    print(catalog)

    print("\n=== Demo Complete ===\n")
