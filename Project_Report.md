# Project Report: Expense Tracker

**Project Title:** Expense Tracker
**Language:** Python 3.x
**Interface:** Command Line (CLI)
**Storage:** JSON (Local File)
**Domain:** Personal Finance Management

---

## 1. Abstract

The Expense Tracker is a Python-based command-line application designed to help users record, categorize, and analyze their daily expenses. All data is stored locally in a JSON file, ensuring persistence across sessions. The project covers core programming concepts such as functions, lists, dictionaries, file I/O, and input validation. It also includes four AI-style analysis features that derive insights from historical spending data without using any external libraries or machine learning frameworks.

---

## 2. Introduction

Managing personal finances is a common challenge, especially for students and young individuals who tend to lose track of small daily expenses. Without a structured way to record and review spending, it becomes difficult to plan budgets or identify problem areas.

This project provides a simple, terminal-based solution that anyone can run without installing additional software. The user can log expenses, view them, and get meaningful summaries — all from a single Python file.

---

## 3. Objectives

- Allow users to add and store daily expenses with category and date
- Display all recorded expenses in a readable format
- Calculate total spending and category-wise breakdowns
- Support monthly filtering for time-based analysis
- Provide AI-style insights based on stored historical data
- Persist data across sessions using a local JSON file

---

## 4. Key Features

### 4.1 Core Features

| Feature | Description |
|---------|-------------|
| Add Expense | Record amount, category, date (DD-MM-YYYY), and description |
| View All Expenses | Display all transactions in a formatted table |
| Total Spending | Show total amount, transaction count, and average per transaction |
| Category-wise Summary | Group expenses by category with percentage breakdown |
| Monthly Summary | Filter and display expenses for a specific month (MM-YYYY) |

### 4.2 AI Analysis Features

| Feature | Description |
|---------|-------------|
| Monthly Comparison | Compares the two most recent months and shows percentage change |
| Spending Habit Detector | Identifies the most used category and most active day of the week |
| Top Expense Day Insight | Finds the single date with the highest total spending |
| Expense Frequency Analyzer | Reports total transactions, unique active days, and daily average |

---

## 5. System Design

### 5.1 Data Structure

Each expense is stored as a dictionary with four fields:

```json
{
  "amount": 250.0,
  "category": "Food",
  "date": "30-03-2026",
  "description": "Lunch at cafe"
}
```

All expense dictionaries are collected in a Python list and written to `expenses.json`.

### 5.2 Function Overview

| Function | Purpose |
|----------|---------|
| `loadexpenses()` | Reads and returns data from `expenses.json` on startup |
| `saveexpenses()` | Writes the current expense list back to `expenses.json` |
| `validateamount()` | Ensures the entered amount is a positive number |
| `validatedate()` | Checks that date input follows DD-MM-YYYY format |
| `validatemonth()` | Checks that month input follows MM-YYYY format |
| `monthmatches()` | Checks whether an expense date belongs to a given month |
| `addexpense()` | Collects input and adds a new expense to the list |
| `viewexpenses()` | Prints all expenses in a formatted table |
| `totalspending()` | Calculates and displays total, count, and average |
| `categorysummary()` | Groups and displays spending by category with percentages |
| `monthlysummary()` | Filters expenses by month and shows totals |
| `monthlycomparison()` | Compares the last two months and shows percentage change |
| `spendinghabitdetector()` | Finds most frequent category and most active weekday |
| `topexpenseday()` | Identifies the date with the highest cumulative spending |
| `expensefrequencyanalyzer()` | Calculates transaction frequency statistics |
| `printmenu()` | Displays the main menu |
| `main()` | Runs the menu loop and routes user input to functions |

### 5.3 Program Workflow

```
Start
  |
  v
Load expenses.json
  |
  v
Display Menu
  |
  v
User selects option (1-10)
  |
  +---> Add Expense       --> Save to JSON --> Back to Menu
  +---> View Expenses     --> Display Table --> Back to Menu
  +---> Total Spending    --> Show Stats --> Back to Menu
  +---> Category Summary  --> Show Breakdown --> Back to Menu
  +---> Monthly Summary   --> Filter + Display --> Back to Menu
  +---> Monthly Compare   --> Analyse + Display --> Back to Menu
  +---> Habit Detector    --> Analyse + Display --> Back to Menu
  +---> Top Expense Day   --> Analyse + Display --> Back to Menu
  +---> Frequency Stats   --> Analyse + Display --> Back to Menu
  +---> Exit              --> End Program
```

---

## 6. Input Validation

All inputs are validated before use. If invalid, the user is prompted to re-enter without the program crashing.

| Field | Expected Format | Example |
|-------|----------------|---------|
| Amount | Positive number | `199.50` |
| Date | `DD-MM-YYYY` | `30-03-2026` |
| Month | `MM-YYYY` | `03-2026` |
| Category | Number (1-7) or custom text | `1` or `Groceries` |

---

## 7. AI Analysis: Logic Explained

### Monthly Comparison
All expenses are grouped by `MM-YYYY` key. The two most recent months are identified by sorting chronologically. The percentage change is calculated as:

```
change% = (|current - previous| / previous) * 100
```

### Spending Habit Detector
Two dictionaries are built, one counting transactions per category, another counting transactions per weekday (using `datetime.weekday()`). The key with the maximum count is selected from each.

### Top Expense Day Insight
A dictionary maps each unique date to its cumulative spending total. The date with the highest value is returned using `max()`.

### Expense Frequency Analyzer
Total transactions come from `len(expenses)`. Unique active days are counted using a `set` of all dates. The average is computed as:

```
avg = total transactions / unique active days
```

---

## 8. Technologies Used

| Component | Details |
|-----------|---------|
| Language | Python 3.6+ |
| Data Storage | JSON (local file — `expenses.json`) |
| Libraries | `json`, `os`, `datetime` (all standard library) |
| Interface | Command Line Interface (CLI) |

---

## 9. Sample Output

### Add Expense
```
--- Add Expense ---
Enter amount: 150
  1. Food
  2. Travel
  ...
Choose category (1-7) or type custom: 1
Enter date (DD-MM-YYYY) or press Enter for today: 30-03-2026
Enter description (optional): Dinner

Expense added: Food - Rs.150.00 on 30-03-2026
```

### Monthly Comparison
```
--- Monthly Comparison ---
Previous month (02-2026): Rs.3200.00
Current month  (03-2026): Rs.4100.00
Spending increased by Rs.900.00 (28.1%)
```

### Spending Habit Detector
```
--- Spending Habit Detector ---
Most used category : Food (18 transactions)
Most active day    : Saturday (12 transactions)
```

---

## 10. Conclusion

The Expense Tracker meets all its defined objectives — providing a clean, fully functional tool for personal finance management using only Python's standard library. The modular function-based structure keeps the code organised and easy to extend. The four AI analysis features add practical value by turning raw expense data into actionable insights without any external dependencies.

---

## 11. Future Improvements

- Export reports to CSV or PDF
- Add ability to edit or delete existing entries
- Set monthly budget limits with overspend warnings
- Visualise spending trends using `matplotlib`
- Build a GUI version using Tkinter or a web interface


# Author
Pritam Ghosh
25BAI11306
