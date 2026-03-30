# Expense Tracker

A simple yet powerful **command-line expense tracking application** built with Python. It helps you record, categorize, and analyze your daily spending — with data that persists across sessions via a local JSON file.

---

## Project Structure
```
expense-tracker/
├── Project_Rrport.md       #Project report
├── main.py                  # Main application file
├── expenses.json            # Auto-generated data storage file
└── README.md                # Project documentation
```

---

## Features

- **Add Expenses**: Record amount, category, date, and an optional description
- **View All Expenses**: Display a formatted table of every recorded transaction
- **Total Spending**: See cumulative spend, transaction count, and average per transaction
- **Category-wise Summary**: Breakdown of spending per category with percentages
- **Monthly Summary**: Filter and total expenses by a specific month
- **Persistent Storage**: All data is saved to `expenses.json` automatically

---

## Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required, uses only the Python standard library

### Installation

1. Clone or download the repository:
```bash
git clone https://github.com/Kaito106/Vityarthi_Fundamental_of_AIML_Project.git
cd Vityarthi_Fundamental_of_AIML_Project
```

2. Run the application:
```bash
python main.py
```

That's it; no setup, no dependencies, no virtual environment needed.

---

## Usage

When you run the program, you'll see the main menu:
```
========================================
       EXPENSE TRACKER
========================================
  1. Add Expense
  2. View All Expenses
  3. Total Spending
  4. Category-wise Summary
  5. Monthly Summary
  6. Exit
========================================
Enter your choice (1-6):
```

### 1. Adding an Expense

Enter the amount, choose a category, provide a date in `DD-MM-YYYY` format (or press Enter for today), and optionally add a description.
```
--- Add Expense ---
Enter amount: 250
Categories:
  1. Food
  2. Travel
  3. Entertainment
  4. Health
  5. Shopping
  6. Education
  7. Other
Choose category (1-7) or type custom: 1
Enter date (DD-MM-YYYY) or press Enter for today: 30-03-2026
Enter description (optional): Lunch at cafe

Expense added: Food - ₹250.00 on 30-03-2026
```

### 2. Viewing All Expenses
```
--- All Expenses ---
#    Date         Category        Amount      Description
------------------------------------------------------------
1    30-03-2026   Food            ₹   250.00  Lunch at cafe
2    29-03-2026   Travel          ₹   120.00  Bus fare
3    28-03-2026   Shopping        ₹   850.00  Stationery
------------------------------------------------------------
Total expenses:                  3 records
```

### 3. Total Spending
```
--- Total Spending ---
Total spending: ₹1220.00
Number of transactions: 3
Average per transaction: ₹406.67
```

### 4. Category-wise Summary
```
--- Category-wise Summary ---
Category                Amount      Percentage
----------------------------------------------
Shopping            ₹    850.00        69.7%
Food                ₹    250.00        20.5%
Travel              ₹    120.00         9.8%
----------------------------------------------
Total               ₹   1220.00       100.0%
```

### 5. Monthly Summary
```
--- Monthly Summary ---
Enter month (MM-YYYY): 03-2026

Expenses for 03-2026:
Date         Category        Amount      Description
-------------------------------------------------------
28-03-2026   Shopping        ₹   850.00  Stationery
29-03-2026   Travel          ₹   120.00  Bus fare
30-03-2026   Food            ₹   250.00  Lunch at cafe
-------------------------------------------------------
Total for 03-2026: ₹1220.00 (3 transactions)
```

---

## Data Storage

All expenses are stored locally in `expenses.json` in the following format:
```json
[
  {
    "amount": 250.0,
    "category": "Food",
    "date": "30-03-2026",
    "description": "Lunch at cafe"
  },
  {
    "amount": 120.0,
    "category": "Travel",
    "date": "29-03-2026",
    "description": "Bus fare"
  }
]
```

The file is created automatically on the first run and updated after every new entry.

---

## Expense Categories

| #  | Category      |
|----|---------------|
| 1  | Food          |
| 2  | Travel        |
| 3  | Entertainment |
| 4  | Health        |
| 5  | Shopping      |
| 6  | Education     |
| 7  | Other         |

> You can also type a **custom category** name instead of choosing from the list.

---

## Input Validation

The program validates all user inputs:

| Field  | Format        | Example      |
|--------|---------------|--------------|
| Amount | Positive number | `250` or `99.50` |
| Date   | `DD-MM-YYYY`  | `30-03-2026` |
| Month  | `MM-YYYY`     | `03-2026`    |

Invalid inputs prompt the user to re-enter without crashing the program.

---

## Technologies Used

| Component        | Details                        |
|------------------|--------------------------------|
| Language         | Python 3.x                     |
| Data Storage     | JSON (local file)              |
| Libraries        | `json`, `os`, `datetime` (all built-in) |
| Interface        | Command Line Interface (CLI)   |

---

## Future Improvements

- [ ] Export reports to CSV or PDF
- [ ] Set monthly budgets with overspend alerts
- [ ] Graphical charts using `matplotlib`
- [ ] Edit or delete existing expense entries
- [ ] Multi-currency support
- [ ] GUI version using Tkinter or a web frontend

---

## License

This project is open source and free to use for educational purposes.

---
# Author
Pritam Ghosh
25BAI11306
