def run():
    """
    Entry point for program execution.

    Demonstrates:
    - Catalog population via adapter
    - Member creation
    - Item checkout
    - Item return and fine calculation
    """

    print("\n=== Library Management System Demo ===\n")

    # ─────────────────────────────
    # 1. Initialize Catalog
    # ─────────────────────────────
    catalog = Catalog("Main Library Catalog")
    load_sample_data_into_catalog(catalog, SAMPLE_ITEMS)

    print("Catalog initialized:")
    print(catalog)
    print()

    # ─────────────────────────────
    # 2. Create Member
    # ─────────────────────────────
    member = Member(
        member_id="MEM001",
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

    print("Item selected for checkout:")
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

    print("Checkout completed:")
    print(checkout)
    print()

    # ─────────────────────────────
    # 5. Simulate Return (Late)
    # ─────────────────────────────
    return_date = date.today() + timedelta(days=5)

    return_summary = checkout.process_return(return_date)

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
