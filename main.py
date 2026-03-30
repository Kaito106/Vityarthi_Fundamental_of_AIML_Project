# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
import json
import os
from datetime import datetime

DATAFILE = "expenses.json"

def loadexpenses():
    if os.path.exists(DATAFILE):
        with open(DATAFILE, "r") as f:
            return json.load(f)
    return []

def saveexpenses(expenses):
    with open(DATAFILE, "w") as f:
        json.dump(expenses, f, indent=2)

def validateamount(amount):
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        return None

def validatedate(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return date
    except ValueError:
        return None

def validatemonth(month):
    try:
        datetime.strptime(month, "%m-%Y")
        return month
    except ValueError:
        return None

def monthmatches(expensedate, monthstr):
    parts = expensedate.split("-")
    return parts[1] == monthstr[:2] and parts[2] == monthstr[3:]

CATEGORIES = ["Food", "Travel", "Entertainment", "Health", "Shopping", "Education", "Other"]

def addexpense(expenses):
    print("\n--- Add Expense ---")

    while True:
        amountinput = input("Enter amount: ").strip()
        amount = validateamount(amountinput)
        if amount is not None:
            break
        print("Invalid amount. Please enter a positive number.")

    print("Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        catinput = input("Choose category (1-7) or type custom: ").strip()
        if catinput.isdigit() and 1 <= int(catinput) <= len(CATEGORIES):
            category = CATEGORIES[int(catinput) - 1]
            break
        elif catinput:
            category = catinput.title()
            break
        print("Invalid category. Please try again.")

    while True:
        dateinput = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
        if not dateinput:
            dateinput = datetime.today().strftime("%d-%m-%Y")
        date = validatedate(dateinput)
        if date is not None:
            break
        print("Invalid date format. Use DD-MM-YYYY.")

    description = input("Enter description (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "date": dateinput,
        "description": description
    }
    expenses.append(expense)
    saveexpenses(expenses)
    print(f"\nExpense added: {category} - ₹{amount:.2f} on {dateinput}")

def viewexpenses(expenses):
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

def totalspending(expenses):
    print("\n--- Total Spending ---")
    if not expenses:
        print("No expenses recorded yet.")
        return
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spending: ₹{total:.2f}")
    print(f"Number of transactions: {len(expenses)}")
    print(f"Average per transaction: ₹{total/len(expenses):.2f}")

def categorysummary(expenses):
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

def monthlysummary(expenses):
    print("\n--- Monthly Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    while True:
        monthinput = input("Enter month (MM-YYYY): ").strip()
        if validatemonth(monthinput):
            break
        print("Invalid format. Use MM-YYYY.")

    filtered = [exp for exp in expenses if monthmatches(exp["date"], monthinput)]
    if not filtered:
        print(f"No expenses found for {monthinput}.")
        return

    total = sum(exp["amount"] for exp in filtered)
    filteredsorted = sorted(filtered, key=lambda x: x["date"].split("-")[0])

    print(f"\nExpenses for {monthinput}:")
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 55)
    for exp in filteredsorted:
        desc = exp.get("description", "")[:18]
        print(f"{exp['date']:<12} {exp['category']:<15} ₹{exp['amount']:>9.2f} {desc}")
    print("-" * 55)
    print(f"Total for {monthinput}: ₹{total:.2f} ({len(filtered)} transactions)")

def printmenu():
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
    expenses = loadexpenses()
    print("Welcome to Expense Tracker!")
    print(f"Loaded {len(expenses)} existing expense(s).")

    while True:
        printmenu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            addexpense(expenses)
        elif choice == "2":
            viewexpenses(expenses)
        elif choice == "3":
            totalspending(expenses)
        elif choice == "4":
            categorysummary(expenses)
        elif choice == "5":
            monthlysummary(expenses)
        elif choice == "6":
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
    # ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
