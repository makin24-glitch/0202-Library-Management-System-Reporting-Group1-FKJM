# Library Management System

## Overview

This project is a Python-based **Library Management System** developed for an Object-Oriented Programming course.

The system demonstrates:

* Object-oriented design (inheritance, composition, polymorphism)
* Use of abstract base classes
* Separation of concerns between data, domain logic, and execution
* Adapter pattern for loading installed sample data

No external APIs or databases are required. All data ships with the program.

---

## Project Structure

```
project_root/
│
├── catalog.py              # Catalog domain class
├── checkout.py             # Checkout transaction logic
├── member.py               # Member domain class
├── abstract_library_item.py# Abstract base class for items
├── adapters.py             # Adapter for loading sample data
├── demo.py                 # Demo / entry point (run this)
│
├── data/
│   └── sample_data.py      # Installed sample data
│
└── index.md                # This file
```

---

## Requirements

* Python **3.9+**
* No third-party libraries required

---

## Installation

1. Clone or download the repository
2. Ensure all files remain in the same relative structure shown above
3. No package installation is required

---

## Running the Demo (Local)

From the project root directory:

```bash
python demo.py
```

This will:

* Initialize the catalog
* Load sample items
* Create a member
* Perform a checkout
* Process a return
* Display final system state

---

## Running the Demo (Google Colab)

1. Upload the entire project folder to Colab **or** upload all `.py` files maintaining structure
2. In a Colab cell, run:

```python
!python demo.py
```

Ensure that the `data/` folder is uploaded as well.

---

## Expected Output

You should see output similar to:

```
=== Library Management System Demo ===

Catalog initialized:
Main Library Catalog: 6 items (X available, Y checked out)

Member created:
Alice Johnson (MEM001) - Active | Fines: $0.00

Item selected for checkout:
<item details>

Checkout completed:
<checkout details>

Return processed:
{'fine': <amount>, 'status': 'returned'}

Final Member State:
<member details>

Final Catalog State:
<catalog details>

=== Demo Complete ===
```

Exact values may vary based on sample data.

---

## Notes for Reviewers / Graders

* `demo.py` is the intended execution entry point
* No UI is required to verify functionality
* Sample data is intentionally simple and installed with the program
* All logic follows documented docstrings and comments

---

## Author

Developed as part of an academic project to demonstrate object-oriented programming principles.
