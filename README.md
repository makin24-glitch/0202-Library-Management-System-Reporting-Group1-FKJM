# 0202-Library-Management-System-Reporting-Group1-FKJM
Reporting and Analytics Dashboard Project for INST 326 Object-Oriented Programming

(This will be our final repo that will be used to complete Project 3 requirements and final submission )

## 🏗️ Introduction 
This project focuses on building a **Library/Information Center Management Dashboard** that provides **reporting and analytics tools** to help library staff, administrators, and stakeholders manage operations more efficiently.  

The system is designed to solve key challenges in the library domain—such as tracking resource usage, generating accurate reports, and understanding user engagement—by offering **automated data visualization and insights**.

---

## 💡 Problem Statement  
Modern libraries and information centers face several operational challenges:  

- ❌ **Inefficient resource tracking** – Difficult to monitor usage across books, e-resources, and facilities.  
- 🧾 **Manual and error-prone reporting** – Time-consuming spreadsheet-based workflows.  
- 📉 **Unclear user engagement** – Limited insight into who uses library services and how.  
- 💰 **Uninformed financial decisions** – Lack of supporting data for budgeting and demonstrating impact.  

These issues reduce efficiency, limit service quality, and make it hard to justify funding.  

Our dashboard provides **automated reporting**, **real-time analytics**, and **actionable insights**—empowering decision-makers to optimize operations and showcase the library’s value.  

---

## 🎯 Project Scope and Features  

### 📊 User Analytics & Engagement  
- Track **active borrowers** and **visitor statistics**  
- View **demographic breakdowns** (e.g., students, faculty, community)  
- Monitor **membership growth trends**

### 📚 Circulation & Collection Insights  
- Display **checkouts, renewals, and returns**  
- Identify **popular titles, genres, and authors**  
- Highlight **overdue items** and **fines collected**

### 💻 Resource Utilization  
- Report **digital resource usage** (e-books, databases)  
- Visualize **study room and computer lab usage**  
- Compare **resource availability vs. demand**

### 💵 Financial & Budget Reporting  
- Track **revenue** from fines, fees, and memberships  
- Compare **budget allocation vs. actual spending**  
- Generate **financial summaries** for decision-making

---

## ✨ Nice-to-Have Features  
- 🔔 **Automated Alerts & Notifications** – Reminders for overdue items, resource shortages, or budget thresholds.  
- ⚙️ **Customization** – Personalized dashboard views and data filters.  
- 🤖 **Predictive Analytics & Recommendations** – Suggest new acquisitions based on borrowing trends.

---

## 🗂️ Project Structure
[README](README.md) – This file  
[Source](src)  
[Documents](docs)  
[Examples](examples)  
[Requirements](requirements.txt)  

---
## Setup instructions (how to run CLI)

# Prerequisites
- Python 3.8 or higher
- Git for version control
- Terminal/Command Line access

# Installation Steps
  1. Clone the repository
    git clone https://github.com/your-team/0202-Library-Management-System-Reporting-Group1-FKJM.git
     cd 0202-Library-Management-System-Reporting-Group1-FKJM
     
  2. Install dependencies (if any)
      pip install -r requirements.txt
  
  3. Run the CLI Dashboard


# Quick Start
      Once the program starts, you'll see the main menu:
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


---

## Usage Examples* 
(' * ' - to be changed)

### Validating a Member ID - validate_member_id(member_id)
Description: Check if a member ID is valid before processing checkout
Input: member_id (string)
Output: True/False
Example: validate_member_id("MEM12345") → True

## Usage Example:
    member_id = "MEM12345"
    is_valid = validate_member_id(member_id)
    # Result: True
## CLI Context: 
    Enter Member ID: MEM12345
    System: ✓ Valid member - Alice Johnson
    Proceed with checkout? (y/n):

### Calculating Due Date - calculate_due_date(checkout_date, loan_period)
Description: Determine when an item must be returned
Input: checkout_date (date), loan_period (integer days)
Output: due_date (date)
Example: calculate_due_date("2024-11-01", 14) → "2024-11-15"

## Usage Example:
    checkout_date = "2024-11-01"
    loan_period = 14  # days
    due_date = calculate_due_date(checkout_date, loan_period)
    # Result: "2024-11-15"
## CLI Context: 
    Checked out: November 1, 2024
    Loan period: 14 days
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    DUE DATE: November 15, 2024
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Compute Overdue Fine - compute_overdue_fine(due_date, return_date, daily_rate) 
Description: Calculate the fine amount when an item is returned late
Input:
    due_date (date/string) - When item should have been returned
    return_date (date/string) - When item was actually returned
    daily_rate (float) - Fine amount per day overdue

Output:
fine_amount (float) - Total fine owed

## Usage Example:
    due_date = "2024-11-15"
    return_date = "2024-11-20"
    daily_rate = 0.50  # $0.50 per day
    fine = compute_overdue_fine(due_date, return_date, daily_rate)
    # Result: $2.50 (5 days × $0.50/day)
## CLI Context: 
    Item due: November 15, 2024
    Returned: November 20, 2024
    Days overdue: 5
    Fine rate: $0.50/day
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    OVERDUE FINE: $2.50
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Please collect payment before checkout

### Check_item_availability - check_item_availability(item_id, catalog)
Description: Verify if a specific item is currently available for checkout
Input:
    item_id (string) - Unique identifier for the library item
    catalog (dict/list) - Collection of library items with status
Output:
    Boolean - True if available, False if checked out

## Usage Example:
    item_id = "BOOK001"
    catalog = {
        "BOOK001": {"title": "Python Guide", "status": "available"},
        "DVD002": {"title": "Tutorial Video", "status": "checked_out"}
    }
    is_available = check_item_availability(item_id, catalog)
    # Result: True
## CLI Context: 
    Search result: BOOK001 - Python Programming Guide
    Status check: ✓ Available for checkout
    
    Search result: DVD002 - Tutorial Video  
    Status check: ✗ Currently checked out (due back: Nov 25)

### Format Item Display - format_item_display(item_data)
Description: Format item information for clean display in the command-line interface
Input:
    item_data (dict) - Dictionary containing item information

Output:
    formatted_string (string) - Nicely formatted text for CLI display

## Usage Example:
    item_data = {
    "id": "BOOK001",
    "title": "Python Programming Guide",
    "type": "Book",
    "author": "Jane Smith",
    "status": "available"
    }
    display = format_item_display(item_data)
## Result: 
    ╔════════════════════════════════════════╗
    ║ [BOOK001] Python Programming Guide    ║
    ║ Type: Book | Author: Jane Smith       ║
    ║ Status: ✓ Available                   ║
    ╚════════════════════════════════════════╝
## CLI Context: 
    Select item to view details: 1

    Item Details:
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ID: BOOK001
    Title: Python Programming Guide
    Type: Book
    Author: Jane Smith
    Status: Available
    Loan Period: 14 days
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Press Enter to continue...

### Generate Checkout Record - generate_checkout_record(member_id, item_id, checkout_date)
Description: Create a complete checkout transaction record
Input:
    member_id (string) - ID of member checking out item
    item_id (string) - ID of item being checked out
    checkout_date (date/string) - Date of checkout
Output:
    checkout_record (dict) - Complete transaction record

## Usage Example:
    member_id = "MEM12345"
    item_id = "BOOK001"
    checkout_date = "2024-11-01"
    record = generate_checkout_record(member_id, item_id, checkout_date)
## Result: 
    {
    "checkout_id": "CHK20241101001",
    "member_id": "MEM12345",
    "item_id": "BOOK001",
    "checkout_date": "2024-11-01",
    "due_date": "2024-11-15",
    "status": "active"
    }
## CLI Context: 
Checkout confirmed!

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            CHECKOUT RECEIPT
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Transaction ID: CHK20241101001
    Member: Alice Johnson (MEM12345)
    Item: Python Programming Guide (BOOK001)
    Checked Out: November 1, 2024
    Due Date: November 15, 2024
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Thank you for using the library!


###Search Catalog - search_catalog(query, catalog_data)
Description: Search the library catalog for items matching a query
Input:
    query (string) - Search term(s) entered by user
    catalog_data (dict/list) - Complete catalog of library items
Output:
    results (list) - List of matching items

## Usage Example:
    query = "python"
    catalog_data = {
        "BOOK001": {"title": "Python Programming Guide", "type": "Book"},
        "BOOK002": {"title": "Java Development", "type": "Book"},
        "DVD001": {"title": "Python Tutorial Video", "type": "DVD"}
    }
    results = search_catalog(query, catalog_data)
## Result: 
    [
    {"id": "BOOK001", "title": "Python Programming Guide", "type": "Book"},
    {"id": "DVD001", "title": "Python Tutorial Video", "type": "DVD"}
    ]
## CLI Context: 
    Enter search term: python
    Searching catalog...
    
    Found 2 results for "python":
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    1. [BOOK001] Python Programming Guide
       Type: Book | Status: Available
       
    2. [DVD001] Python Tutorial Video  
       Type: DVD | Status: Checked Out
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    Enter item number for details or 0 to return:

### Update Item Status - update_item_status(item_id, new_status)
Description: Change the status of a library item (e.g., available → checked_out)
Input:
    item_id (string) - ID of item to update
    new_status (string) - New status value ("available", "checked_out", "maintenance", etc.)
Output:
    success (boolean) - True if update successful, False otherwise

## Usage Example:
    item_id = "BOOK001"
    new_status = "checked_out"
    success = update_item_status(item_id, new_status)
    # Result: True
## CLI Context: 
    Processing checkout...
    Updating item status: BOOK001
    Status: available → checked_out
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ✓ Status updated successfully
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    Later during return:
    Processing return...
    Updating item status: BOOK001
    Status: checked_out → available
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ✓ Item returned and now available
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

(more methods to come)

## Method Integration Workflow (tentative)
  #  Complete Checkout Process:
    Step 1: Validate member
    → validate_member_id("MEM12345") → True ✓
  
    Step 2: Search for item
      → search_catalog("python", catalog) → Shows results
    
    Step 3: Check availability
      → check_item_availability("BOOK001", catalog) → True ✓
      → format_item_display(item_data) → Shows formatted details
    
    Step 4: Process checkout
      → generate_checkout_record("MEM12345", "BOOK001", "2024-11-01")
      → calculate_due_date("2024-11-01", 14) → "2024-11-15"
      → update_item_status("BOOK001", "checked_out")
    
    Step 5: Display confirmation
      → "Checkout complete! Due: November 15, 2024"

---
### Method overview and organization
Our library dashboard uses 8 core methods organized into 4 functional areas:
## 1. Validation Methods (2 methods)
  These methods ensure data integrity before processing:
  
  validate_member_id() - Verifies member exists in system
  check_item_availability() - Confirms item can be checked out

## 2. Calculation Methods (2 methods)
  These methods perform date and financial calculations:
  
  calculate_due_date() - Computes return deadline based on loan period
  compute_overdue_fine() - Calculates late fees based on days overdue

## 3. Data Management Methods (2 methods)
  These methods create and update records:
  
  generate_checkout_record() - Creates complete checkout transaction
  update_item_status() - Changes item availability status

## 4. Display & Search Methods (2 methods)
  These methods handle user interface and data retrieval:
  
  format_item_display() - Formats item info for CLI presentation
  search_catalog() - Finds items matching search query
## System Architecture
    User Input (CLI)
        ↓
    Validation Layer (validate_member_id, check_item_availability)
          ↓
    Business Logic Layer (calculate_due_date, compute_overdue_fine)
          ↓
    Data Layer (generate_checkout_record, update_item_status)
          ↓
    Display Layer (format_item_display, search_catalog)
          ↓
    User Output (CLI)

### Method Integration
Our methods work together to create complete workflows:

  Checkout Flow: Uses 6 methods (validate → search → check → generate → calculate → update)
  Return Flow: Uses 3 methods (compute → update → format)
  Search Flow: Uses 2 methods (search → format)

---
###Contribution Guidelines

Team Member Assignments
Phase 1 - Method Implementation:
  Jordan Mutunzi: validate_member_id, calculate_due_date
  Keran Leukeu: compute_overdue_fine, check_item_availability
  Mayowa Akinrodoye: format_item_display, generate_checkout_record
  Francis Okeagu: search_catalog, update_item_status

Phase 2 - Class Implementation (Project 02):
  Jordan: Member class, Checkout class
  Keran: LibraryItem class, Book class
  Mayowa: Catalog class, DVD class
  Francis: Journal class, CLI interface

Phase 3 - Advanced OOP (Project 03):
  Jordan: AbstractLibraryItem, inheritance refactoring
  Keran: Polymorphism demonstration, test suite
  Mayowa: Composition relationships, architecture documentation
  Francis: Demo scripts, integration testing

Communication
  Team Meetings: Weekly on Mondays at 6 PM
  Code Reviews: Within 24 hours of PR submission
  Questions/Issues: Post in team Discord channel
  Blockers: Tag team in GitHub issue immediately
  
---

### Inheritance Hierarchies
## AbstractLibraryItem hierarchy 
    **AbstractLibraryItem** (Abstract Base Class - that uses the simple library item)  
      **Book** — printed or digital reading material  
      **DVD** — optical media for movies or video content  
      **Journal** — periodicals, academic publications, or magazines  

---

Document polymorphism examples (for Project 03)
Details here...
---



---

## 👥 Contributors  
Team Members: Jordan Mutunzi, Keran Leukeu, Mayowa Akinrodoye, and Francis Okeagu*  
