# Sales Reconciliation System

## Version 2: Object-Oriented Programming

A Python-based sales reconciliation system for managing branch sales reports and identifying discrepancies between recorded sales and amounts banked.

Version 2 is a refactored version of the original application. The core functionality from Version 1 has been reorganized using **Object-Oriented Programming (OOP)** to give different parts of the application clearer responsibilities.

---

### Version 2

The application was redesigned using OOP.

The main goal was to move from simply writing code that works to **structuring the application around the entities and responsibilities within the problem**.

---

## OOP Structure

The application currently uses two main classes.

### `SalesReport`

Represents a single branch's sales report.

It stores:

* Branch
* M-Pesa sales
* Cash sales
* Card sales
* Total banked

It also calculates:

* Total sales
* Variance
* Reconciliation status

Example:

```python
report = SalesReport(
    "Nairobi",
    50000,
    20000,
    10000,
    80000
)
```

### `ReconciliationSystem`

Manages multiple `SalesReport` objects.

Its responsibilities include:

* Adding reports
* Finding reports
* Displaying reports
* Editing reports
* Deleting reports
* Validating branch names
* Managing the collection of reports

---

## Reconciliation Logic

The system records:

* M-Pesa
* Cash
* Card
* Total Banked

### Total Sales

```text
Total Sales = M-Pesa + Cash + Card
```

### Variance

```text
Variance = Total Banked - Total Sales
```

### Status

| Variance | Status         |
| -------- | -------------- |
| Negative | Underbanked ⬇️ |
| Positive | Overbanked ⬆️  |
| Zero     | Reconciled ✅   |

---

## Key OOP Concepts Practiced

### Classes and Objects

The application models individual sales reports as `SalesReport` objects and the overall reporting system as a `ReconciliationSystem` object.

### Encapsulation

The data and calculations associated with a sales report are kept together inside the `SalesReport` class.

### Methods

Operations such as finding, adding, editing, and deleting reports are implemented as methods belonging to the system that manages them.

### Separation of Responsibilities

The two classes have different roles:

```text
SalesReport
    ↓
Individual report data + calculations

ReconciliationSystem
    ↓
Management of multiple reports
```

This makes the structure easier to understand and extend.

### Reusable Logic

The `find_report()` method provides a single way to locate a report by branch rather than repeating the same search logic in multiple operations.

---

## Input Validation

The application validates user input before processing it.

It handles:

* Invalid menu choices
* Invalid branch names
* Non-numeric amounts
* Negative amounts
* Duplicate branch reports
* Attempts to access reports that do not exist
* Invalid delete confirmations

---

## Technologies

* Python
* Object-Oriented Programming
* Classes and Objects
* Methods
* Lists
* Dictionaries
* Functions
* Conditional statements
* Loops
* Exception handling

No external Python packages are required.

---

## Current Limitations

At this stage, reports are stored only in memory.

When the program closes, the reports are lost.

Persistent storage is intentionally **not included in Version 2**. This will be addressed in Version 3.

The application also remains a terminal-based program. A graphical interface will be introduced later.

---

## Development Roadmap

The project is being developed progressively:

```text
Version 1 → Core Python
Version 2 → Object-Oriented Programming
Version 3 → Data Persistence
Version 4 → Graphical User Interface
Version 5 → Reporting & Analytics
```

Each version introduces a new layer of functionality without skipping the underlying concepts.

---

## Current Status

**Version 2: Complete**

The core application has been refactored into an object-oriented structure and tested through the main user workflows.

The next stage is **Version 3: Data Persistence**, where the application will learn to save and retrieve reports instead of keeping them only in memory.
