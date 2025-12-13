0202 – Library Management System Reporting & Analytics Dashboard

INST 326 – Object-Oriented Programming
Group 1 (FKJM)

This repository will serve as the primary codebase moving forward for all phases of the project.

🏗️ Introduction

This project implements a Library / Information Center Management Dashboard that provides reporting and analytics capabilities to support library staff, administrators, and stakeholders in managing operations more effectively.

The system addresses common challenges in the library domain—such as tracking circulation, analyzing user engagement, and producing operational reports—by offering automated data processing, structured reporting, and clear CLI-based visual output.

💡 Problem Statement

Modern libraries and information centers often struggle with:

Inefficient resource tracking across books, digital media, and facilities

Manual, error-prone reporting workflows reliant on spreadsheets

Limited insight into user engagement and borrowing behavior

Insufficient data to support budgeting and funding decisions

These challenges reduce operational efficiency, limit service optimization, and make it difficult to demonstrate institutional value.

This project addresses these issues by providing automated reporting, real-time analytics, and actionable insights through a structured, object-oriented system.

🎯 Project Scope & Features
📊 User Analytics & Engagement

Track active borrowers and visitor statistics

Display demographic groupings (students, faculty, community members)

Monitor membership growth trends over time

📚 Circulation & Collection Insights

Track checkouts, renewals, and returns

Identify popular titles, genres, and authors

Flag overdue items and fines

💻 Resource Utilization

Report digital resource usage (e-books, databases)

Visualize study room and computer lab usage

Compare resource demand versus availability

💵 Financial & Budget Reporting

Track revenue from fines, fees, and memberships

Compare budget allocation against actual spending

Generate financial summaries for administrative review

✨ Optional / Future Enhancements

Automated alerts and notifications (overdue items, resource shortages)

Customizable dashboard views and filters

Predictive analytics for acquisition and demand forecasting

🗂️ Project Structure
├── README.md
├── src/
├── docs/
├── examples/
└── requirements.txt

⚙️ Installation & Setup
Prerequisites

Python 3.8 or higher

Git

Command-line / terminal access

Installation
git clone https://github.com/your-team/0202-Library-Management-System-Reporting-Group1-FKJM.git
cd 0202-Library-Management-System-Reporting-Group1-FKJM
pip install -r requirements.txt

Run the CLI Dashboard
python main.py

🚀 Quick Start

Once launched, the CLI presents the main menu:

=================================
LIBRARY MANAGEMENT DASHBOARD
=================================
1. Search Catalog
2. Check Out Item
3. Return Item
4. View Member Info
5. Calculate Fines
6. Exit
=================================
Enter your choice:

🧪 Usage Examples (Subject to Change)
validate_member_id(member_id)

Checks whether a member ID is valid before processing transactions.

Input: str
Output: bool

member_id = "MEM12345"
is_valid = validate_member_id(member_id)


CLI Output:

✓ Valid member - Alice Johnson
Proceed with checkout? (y/n):

calculate_due_date(checkout_date, loan_period)

Determines the return deadline for a checkout.

calculate_due_date("2024-11-01", 14)

DUE DATE: November 15, 2024

compute_overdue_fine(due_date, return_date, daily_rate)

Calculates overdue fines based on return date.

compute_overdue_fine("2024-11-15", "2024-11-20", 0.50)

OVERDUE FINE: $2.50

search_catalog(query, catalog_data)

Searches the catalog for matching items.

results = search_catalog("python", catalog_data)

Found 2 results for "python"

update_item_status(item_id, new_status)

Updates item availability during checkout or return.

Status: available → checked_out
✓ Status updated successfully

🔄 Method Integration Workflow

Complete Checkout Process

Validate member

Search catalog

Check availability

Generate checkout record

Update item status

Display confirmation

🧩 Method Organization
Validation

validate_member_id()

check_item_availability()

Calculations

calculate_due_date()

compute_overdue_fine()

Data Management

generate_checkout_record()

update_item_status()

Display & Search

format_item_display()

search_catalog()

🏛️ System Architecture
User Input (CLI)
   ↓
Validation Layer
   ↓
Business Logic Layer
   ↓
Data Management Layer
   ↓
Display Layer
   ↓
User Output (CLI)

🧬 Object-Oriented Design
Inheritance Hierarchy
AbstractLibraryItem
├── Book
├── DVD
└── Journal

Polymorphism

Shared interfaces with item-specific behavior

Methods such as calculate_loan_period() and format_display() behave differently per item type

CLI interacts with all items uniformly

Composition

Catalog contains LibraryItem objects

Checkout links Member and LibraryItem

Members may have multiple active checkouts

🎯 Design Summary

Composition defines object relationships

Polymorphism enables flexible, reusable behavior

Together they produce a scalable, maintainable, object-oriented system

🤝 Contribution Guidelines
Phase Assignments

Phase 1 – Methods

Jordan Mutunzi: validate_member_id, calculate_due_date

Keran Leukeu: compute_overdue_fine, check_item_availability

Mayowa Akinrodoye: format_item_display, generate_checkout_record

Francis Okeagu: search_catalog, update_item_status

Phase 2 – Classes

Jordan: Member, Checkout

Keran: LibraryItem, Book

Mayowa: Catalog, DVD

Francis: Journal, CLI

Phase 3 – Advanced OOP

Jordan: Abstract classes & inheritance refactor

Keran: Polymorphism & testing

Mayowa: Composition & architecture documentation

Francis: Integration testing & demos

👥 Contributors

Jordan Mutunzi · Keran Leukeu · Mayowa Akinrodoye · Francis Okeagu
