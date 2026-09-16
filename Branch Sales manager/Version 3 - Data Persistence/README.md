# Sales Reconciliation System

## Version 3: Data Persistence

A Python-based sales reconciliation system for managing branch sales reports and identifying discrepancies between recorded sales and amounts banked.

Version 3 builds on the Object-Oriented Programming structure introduced in Version 2 by adding **data persistence**. Reports can now be stored in a JSON file and retrieved when the application is run again.

---

## Project Progression

### Version 1

Built the core terminal application using procedural Python.

Features included:

* Add reports
* View reports
* Search reports
* Edit reports
* Delete reports
* Calculate total sales
* Calculate variance
* Identify reconciliation status
* Input validation

### Version 2

Refactored the application using Object-Oriented Programming.

The system was divided into two main classes:

* `SalesReport` - represents an individual branch report and handles its calculations.
* `ReconciliationSystem` - manages multiple reports and their operations.

### Version 3

Introduces **data persistence using JSON**.

The application can now:

* Save reports to a JSON file
* Load previously saved reports
* Preserve data between program sessions
* Reconstruct saved data into `SalesReport` objects

---

## Current Features

* Add branch sales reports
* View all reports
* Search for a branch report
* Edit existing reports
* Delete reports
* Calculate total sales
* Calculate variance
* Determine reconciliation status
* Validate user input
* Prevent duplicate branch reports
* Save report data to JSON
* Load saved reports when the application starts

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

## Technologies

* Python
* Object-Oriented Programming
* JSON
* File Handling
* Exception Handling

No external Python packages are required.

---

## Project Structure

```text
Sales Reconciliation System/
│
├── sales_reconciliation.py
├── reports.json
└── README.md
```

`reports.json` is used to persist report data between program sessions.

---

## What I Am Learning

Version 3 is focused on understanding how an application moves beyond temporary in-memory data.

The key concepts are:

* JSON data structures
* Serialization and deserialization
* Reading from files
* Writing to files
* Converting Python objects into storable data
* Reconstructing Python objects from stored data
* Handling missing or invalid files

The goal is not simply to make the program save data, but to understand **how persistence fits into application design**.

---

## Development Roadmap

The project is being developed progressively rather than building the final application all at once.

```text
Version 1 → Core Python
Version 2 → Object-Oriented Programming
Version 3 → Data Persistence
Version 4 → Graphical User Interface
Version 5 → Reporting & Analytics
```

Each version builds on the previous one while introducing a new layer of functionality.

---

## Current Status

**Version 3: In Development**

The current focus is implementing JSON-based persistence while maintaining the OOP structure established in Version 2.
