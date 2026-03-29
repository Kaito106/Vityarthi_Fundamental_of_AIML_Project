# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        return None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return date_str
    except ValueError:
        return None

def validate_month(month_str):
    try:
        datetime.strptime(month_str, "%m-%Y")
        return month_str
    except ValueError:
        return None

def month_matches(expense_date, month_str):
    # expense_date is DD-MM-YYYY, month_str is MM-YYYY
    parts = expense_date.split("-")
    return parts[1] == month_str[:2] and parts[2] == month_str[3:]

CATEGORIES = ["Food", "Travel", "Entertainment", "Health", "Shopping", "Education", "Other"]

def add_expense(expenses):
    print("\n--- Add Expense ---")

    while True:
        amount_str = input("Enter amount: ").strip()
        amount = validate_amount(amount_str)
        if amount is not None:
            break
        print("Invalid amount. Please enter a positive number.")

    print("Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        cat_input = input("Choose category (1-7) or type custom: ").strip()
        if cat_input.isdigit() and 1 <= int(cat_input) <= len(CATEGORIES):
            category = CATEGORIES[int(cat_input) - 1]
            break
        elif cat_input:
            category = cat_input.title()
            break
        print("Invalid category. Please try again.")

    while True:
        date_str = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
        if not date_str:
            date_str = datetime.today().strftime("%d-%m-%Y")
        date = validate_date(date_str)
        if date is not None:
            break
        print("Invalid date format. Use DD-MM-YYYY.")

    description = input("Enter description (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "date": date_str,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"\nExpense added: {category} - ₹{amount:.2f} on {date_str}")

def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'#':<4} {'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 60)
    for i, exp in enumerate(expenses, 1):
        desc = exp.get("description", "")[:20]
        print(f"{i:<4} {exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:>9.2f} {desc}")
    print("-" * 60)
    print(f"{'Total expenses:':<32} {len(expenses)} records")

def total_spending(expenses):
    print("\n--- Total Spending ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: ₹{total:.2f}")
    print(f"Number of transactions: {len(expenses)}")
    print(f"Average per transaction: ₹{total/len(expenses):.2f}")

def category_summary(expenses):
    print("\n--- Category-wise Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    total = sum(summary.values())
    print(f"{'Category':<20} {'Amount':>12} {'Percentage':>12}")
    print("-" * 46)
    for cat, amount in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        pct = (amount / total * 100) if total else 0
        print(f"{cat:<20} ₹{amount:>10.2f} {pct:>11.1f}%")
    print("-" * 46)
    print(f"{'Total':<20} ₹{total:>10.2f} {'100.0%':>12}")

def monthly_summary(expenses):
    print("\n--- Monthly Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    while True:
        month_str = input("Enter month (MM-YYYY): ").strip()
        if validate_month(month_str):
            break
        print("Invalid format. Use MM-YYYY.")

    filtered = [exp for exp in expenses if month_matches(exp["date"], month_str)]
    if not filtered:
        print(f"No expenses found for {month_str}.")
        return

    total = sum(exp["amount"] for exp in filtered)
    # Sort by day for chronological display
    filtered_sorted = sorted(filtered, key=lambda x: x["date"].split("-")[0])

    print(f"\nExpenses for {month_str}:")
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 55)
    for exp in filtered_sorted:
        desc = exp.get("description", "")[:18]
        print(f"{exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:>9.2f} {desc}")
    print("-" * 55)
    print(f"Total for {month_str}: ₹{total:.2f} ({len(filtered)} transactions)")

def print_menu():
    print("\n" + "=" * 40)
    print("       EXPENSE TRACKER")
    print("=" * 40)
    print("  1. Add Expense")
    print("  2. View All Expenses")
    print("  3. Total Spending")
    print("  4. Category-wise Summary")
    print("  5. Monthly Summary")
    print("  6. Exit")
    print("=" * 40)

def main():
    expenses = load_expenses()
    print("Welcome to Expense Tracker!")
    print(f"Loaded {len(expenses)} existing expense(s).")

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_spending(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            monthly_summary(expenses)
        elif choice == "6":
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
