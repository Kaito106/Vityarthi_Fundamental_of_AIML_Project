# Expense Tracker

A CLI-based personal expense tracking application built with Python. Stores data in a local JSON file so nothing is lost between sessions.

---

## Project Structure

```
Vityarthi_Fundamental_of_AIML_Project/
├── Project_Report.md # Project Report
├── main.py           # Main application
├── expenses.json     # Auto-generated data file
└── README.md
```

---

## Getting Started

**Requirements:** Python 3.6+, no external libraries needed.

```bash
git clone https://github.com/Kaito106/Vityarthi_Fundamental_of_AIML_Project.git
cd Vityarthi_Fundamental_of_AIML_Project
python main.py
```

---

## Menu Options

```
========================================
       EXPENSE TRACKER
========================================
  1. Add Expense
  2. View All Expenses
  3. Total Spending
  4. Category-wise Summary
  5. Monthly Summary
  6. Monthly Comparison
  7. Spending Habit Detector
  8. Top Expense Day Insight
  9. Expense Frequency Analyzer
  10. Exit
========================================
```

---

## Features

### Core

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | Add Expense | Enter amount, category, date, and optional description |
| 2 | View All Expenses | Formatted table of all recorded transactions |
| 3 | Total Spending | Cumulative total, transaction count, and average |
| 4 | Category-wise Summary | Spending per category with percentages |
| 5 | Monthly Summary | Filter and view expenses by MM-YYYY |

### AI Analysis

| Option | Feature | Description |
|--------|---------|-------------|
| 6 | Monthly Comparison | Compares the two most recent months with percentage change |
| 7 | Spending Habit Detector | Finds most used category and most active day of the week |
| 8 | Top Expense Day Insight | Shows the date with the highest total spending |
| 9 | Expense Frequency Analyzer | Transactions count, unique active days, and daily average |

---

## Input Formats

| Field | Format | Example |
|-------|--------|---------|
| Amount | Positive number | `250` or `99.50` |
| Date | `DD-MM-YYYY` | `30-03-2026` |
| Month | `MM-YYYY` | `03-2026` |

Categories: Food, Travel, Entertainment, Health, Shopping, Education, Other — or type a custom name.

---

## Data Storage

Expenses are saved automatically to `expenses.json` after every entry.

```json
[
  {
    "amount": 250.0,
    "category": "Food",
    "date": "30-03-2026",
    "description": "Lunch at cafe"
  }
]
```

---

## Built With

Python 3: `json`, `os`, `datetime` (standard library only)

---

## License

Open source: free to use for educational purposes.

---
# Author
Pritam Ghosh
25BAI11306
