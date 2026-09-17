# Branch Sales Manager — Version 4 (GUI)

A desktop GUI for recording and reconciling branch sales, built with Python's
built-in `tkinter`. Add, edit, search, and delete branch reports; totals,
variance, and reconciliation status are calculated and saved automatically.

This is Version 4 of a 5-part rebuild of the same project:
V1 Core Python → V2 OOP → V3 Data persistence → **V4 GUI** → V5 Reporting & analytics

## Try it yourself

**Requirements:** Python 3.8+ (tkinter ships with the standard installer on
Windows and macOS — see `requirements.txt` for Linux setup if needed).

To run the application locally, run the following commands from your terminal.
Windows users:
```bash
git clone https://github.com/gloriamaleche-data/Python_projects.git
cd "Python_projects/Branch Sales Manager/Version 4 - GUI with Tkinter"
py gui.py
```
macOS/Linux users:
```bash
git clone https://github.com/gloriamaleche-data/Python_projects.git
cd "Python_projects/Branch Sales Manager/Version 4 - GUI with Tkinter"
python3 gui.py
```
**N/B** The application has currently been tested on Windows.
## Files

- `gui.py` — the interface: forms, the report summary panel, and the reports table
- `reconciliation.py` — the underlying logic: `SalesReport` and `ReconciliationSystem`, unchanged in behavior from Version 3
- `reports.json` — where your reports are saved between runs

## What changed from Version 3

The reconciliation logic, persistence, and duplicate-checking didn't change.
Only the interface did ; `input()` and `print()` calls were replaced with
`tkinter` widgets, form fields, and a live-updating table.