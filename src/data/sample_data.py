"""
Installed sample data for the Library Dashboard.

This module contains static, in-memory data used by the application
to demonstrate system behavior without requiring external setup.
"""

# --------------------
# MEMBERS
# --------------------

SAMPLE_MEMBERS = [
    {
        "member_id": "M001",
        "name": "Alice Johnson",
        "member_type": "Student"
    },
    {
        "member_id": "M002",
        "name": "Brian Smith",
        "member_type": "Faculty"
    },
    {
        "member_id": "M003",
        "name": "Carmen Lee",
        "member_type": "Student"
    },
    {
        "member_id": "M004",
        "name": "David Patel",
        "member_type": "Guest"
    }
]

# --------------------
# LIBRARY ITEMS
# --------------------

SAMPLE_BOOKS = [
    {
        "item_id": "B100",
        "title": "Python Basics",
        "author": "J. Doe",
        "category": "Technology",
        "status": "available"
    },
    {
        "item_id": "B101",
        "title": "Data Science 101",
        "author": "A. Ng",
        "category": "Technology",
        "status": "checked_out"
    },
    {
        "item_id": "B102",
        "title": "World History",
        "author": "M. Brown",
        "category": "History",
        "status": "available"
    },
    {
        "item_id": "B103",
        "title": "Creative Writing",
        "author": "L. King",
        "category": "Literature",
        "status": "maintenance"
    }
]

# --------------------
# CHECKOUT / LOAN RECORDS
# --------------------

SAMPLE_LOANS = [
    {
        "loan_id": "L9001",
        "member_id": "M001",
        "item_id": "B101",
        "checkout_date": "2025-02-01",
        "due_date": "2025-02-15",
        "return_date": None
    },
    {
        "loan_id": "L9002",
        "member_id": "M003",
        "item_id": "B100",
        "checkout_date": "2025-01-10",
        "due_date": "2025-01-24",
        "return_date": "2025-01-26"
    }
]


# --------------------
# SAMPLE ITEMS
# --------------------

SAMPLE_ITEMS = [
    {
        "type": "Book",
        "item_id": "B001",
        "title": "Python Basics",
        "author": "Jane Doe",
        "status": "available"
    },
    {
        "type": "DVD",
        "item_id": "D010",
        "title": "OOP Explained",
        "runtime_minutes": 90,
        "status": "checked_out"
    },
    {
        "type": "Journal",
        "item_id": "J100",
        "title": "Data Science Today",
        "volume": "12",
        "issue": "3",
        "status": "available"
    }
]
