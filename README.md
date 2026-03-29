# 💰 Expense Tracker

A CLI-based personal expense tracking app built with Python. Records, categorizes, and analyzes your spending with data saved locally in JSON.

---

## 📁 Project Structure
```
expense-tracker/
├── main.py         # Main application
├── expenses.json   # Auto-generated data file
└── README.md
```

---

## 🚀 Getting Started

**Requirements:** Python 3.6+ — no external libraries needed.
```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
python main.py
```

---

## ✨ Features

| Option | Feature |
|--------|---------|
| 1 | Add Expense — amount, category, date, description |
| 2 | View All Expenses |
| 3 | Total Spending — sum, count, and average |
| 4 | Category-wise Summary — with percentages |
| 5 | Monthly Summary — filter by `MM-YYYY` |
| 6 | Exit |

---

## 📋 Input Formats

| Field  | Format       | Example      |
|--------|--------------|--------------|
| Amount | Positive number | `250.00` |
| Date   | `DD-MM-YYYY` | `30-03-2026` |
| Month  | `MM-YYYY`    | `03-2026`    |

Categories: Food, Travel, Entertainment, Health, Shopping, Education, Other — or enter a custom name.

---

## 💾 Data Storage

Expenses are saved automatically to `expenses.json` after every entry.

---

## 🛠️ Built With

Python 3 · `json` · `os` · `datetime` — all standard library.

---

## 📄 License

Open source — free to use for educational purposes.
