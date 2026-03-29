# Expense Tracker — Project Report

**Project Title:** Expense Tracker
**Technology:** Python 3.x (Standard Library)
**Type:** Command-Line Application
**Domain:** Personal Finance Management

---

## 1. Abstract

The Expense Tracker is a Python-based CLI application that helps users record, categorize, and analyze daily expenses. Data is stored persistently in a local JSON file. The project demonstrates practical use of core Python concepts — lists, dictionaries, functions, file I/O, and input validation — to solve a real-world problem.

---

## 2. Introduction

Many individuals, especially students, struggle to monitor daily spending, which leads to poor financial planning. This project addresses that gap by providing a simple, structured tool to log transactions and review spending patterns over time — requiring no external libraries or internet connection.

---

## 3. Key Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | Add Expense | Record amount, category, date (DD-MM-YYYY), and description |
| 2 | View All Expenses | Display all transactions in a formatted table |
| 3 | Total Spending | Show cumulative total, count, and average |
| 4 | Category-wise Summary | Breakdown by category with percentages |
| 5 | Monthly Summary | Filter and total expenses by MM-YYYY |
| 6 | Persistent Storage | Auto-save and load via `expenses.json` |

---

## 4. System Design

### 4.1 Data Structure

Each expense is stored as a dictionary inside a list:

```json
{
  "amount": 250.0,
  "category": "Food",
  "date": "30-03-2026",
  "description": "Lunch at cafe"
}
```

### 4.2 Functions

| Function | Purpose |
|----------|---------|
| `load_expenses()` | Load data from `expenses.json` on startup |
| `save_expenses()` | Write updated list to `expenses.json` |
| `add_expense()` | Collect and store a new expense entry |
| `view_expenses()` | Print all records in a formatted table |
| `total_spending()` | Calculate and display spending totals |
| `category_summary()` | Group and aggregate expenses by category |
| `monthly_summary()` | Filter expenses by month and display totals |
| `validate_amount()` | Ensure amount is a positive number |
| `validate_date()` | Ensure date follows DD-MM-YYYY format |
| `validate_month()` | Ensure month follows MM-YYYY format |
| `main()` | Run the menu loop |

### 4.3 Workflow

```
Start → Load expenses.json → Show Menu → User selects option
  → Execute function → Save (if new data) → Return to menu → Exit
```

---

## 5. Input Validation

All user inputs are validated before processing. Invalid entries prompt the user to re-enter without crashing the program.

| Field | Format | Example |
|-------|--------|---------|
| Amount | Positive number | `199.50` |
| Date | `DD-MM-YYYY` | `30-03-2026` |
| Month | `MM-YYYY` | `03-2026` |

---

## 6. Technologies Used

| Component | Details |
|-----------|---------|
| Language | Python 3.6+ |
| Storage | JSON (local file) |
| Libraries | `json`, `os`, `datetime` — all built-in |
| Interface | Command Line (CLI) |

---

## 7. Conclusion

The Expense Tracker successfully meets its objectives — recording, categorizing, and analyzing personal expenses through a clean, menu-driven interface. The use of JSON ensures data persistence without requiring a database. The modular, function-based structure keeps the code readable and easy to extend.

---

## 8. Future Improvements

- Export reports to CSV or PDF
- Budget limits with overspend alerts
- Edit or delete existing entries
- Visual charts using `matplotlib`
- GUI version using Tkinter or a web frontend

---
## Author:
Pritam Ghosh
25BAI11306
