# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------

import os
import json
from datetime import datetime

DATA_FILE="data.json"

def load_data():
  if not os.path.exists(Data_file):
    return {
      "expenses": [], "budgets":{"overall": None, "categories":{}}
    }

try:
  with open(Data_file, "r") as f:
    data = json.load(f)


except (json.JSONDecodeError, IOError):
  data={
    "expenses": [], "budgets": { "overall": None, "categories": {} }
  }
  return data


def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except IOError:
        print("Error: Could not save data to file.")



def input_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")



def input_float(prompt):
    while True:
        value_str = input(prompt).strip()
        try:
            value = float(value_str)
            if value <= 0:
                print("Amount must be positive.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a valid amount.")



def show_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. View Budget")
    print("5. Monthly Summary & Budget Alerts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()
    return choice
  


def monthly_summary(data):
    expenses = data.get("expenses", [])
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    month = input("\nEnter month in format YYYY-MM (e.g., 2025-11): ").strip()
    if len(month) != 7 or month[4] != "-":
        print("Invalid month format.")
        return

    total_for_month = 0.0
    category_totals = {}

    for e in expenses:
        if e["date"].startswith(month):
            amt = e["amount"]
            total_for_month += amt
            cat = e["category"]
            category_totals[cat] = category_totals.get(cat, 0.0) + amt

    if total_for_month == 0:
        print(f"No expenses found for {month}.")
        return

    print(f"\n--- Summary for {month} ---")
    print(f"Total spending: {total_for_month:.2f}")
    print("Spending by category:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: {amt:.2f}")

    budgets = data.get("budgets", {"overall": None, "categories": {}})
    overall_budget = budgets.get("overall")
    category_budgets = budgets.get("categories", {})

    print("\n--- Budget Status ---")
    if overall_budget is not None:
        if total_for_month > overall_budget:
            print(f"WARNING: Overall spending exceeded budget ({total_for_month:.2f} > {overall_budget:.2f})")
        else:
            remaining = overall_budget - total_for_month
            print(f"Overall spending is within budget. Remaining: {remaining:.2f}")
    else:
        print("Overall budget not set.")

    for cat, amt in category_totals.items():
        if cat in category_budgets:
            cat_budget = category_budgets[cat]
            if amt > cat_budget:
                print(f"WARNING: '{cat}' category exceeded budget ({amt:.2f} > {cat_budget:.2f})")
            else:
                remaining = cat_budget - amt
                print(f"'{cat}' category within budget. Remaining: {remaining:.2f}")
        else:
            print(f"No budget set for category '{cat}'.")



def view_expenses(data):
    expenses = data.get("expenses", [])
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n--- View Expenses ---")
    print("1. View all expenses")
    print("2. Filter by category")
    print("3. Filter by date range")
    choice = input("Enter your choice (1-3): ").strip()

    filtered = expenses

    if choice == "2":
        category = input("Enter category to filter by: ").strip()
        filtered = [e for e in expenses if e["category"].lower() == category.lower()]

    elif choice == "3":
        start_date = input_date("Enter start date (YYYY-MM-DD): ")
        end_date = input_date("Enter end date (YYYY-MM-DD): ")
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        if end < start:
            print("End date cannot be earlier than start date.")
            return
        filtered = []
        for e in expenses:
            d = datetime.strptime(e["date"], "%Y-%m-%d")
            if start <= d <= end:
                filtered.append(e)

    if not filtered:
        print("No expenses found for the selected filter.")
        return

    print("\nID |Date    |Category  |Amount    |Description")
    print("-" * 60)
    for e in filtered:
        print(f"{e['id']:2d} | {e['date']} | {e['category']:<10} | {e['amount']:8.2f} | {e['description']}")
    print("-" * 60)
    total = sum(e["amount"] for e in filtered)
    print(f"Total for these expenses: {total:.2f}")



def add_exp(data):
    print("\n--- Add New Expense ---")
    date = input_date("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel, Shopping): ").strip()
    description = input("Enter description: ").strip()
    amount = input_float("Enter amount: ")

    expenses = data.get("expenses", [])

    if expenses:
        new_id = max(expense.get("id", 0) for expense in expenses) + 1
    else:
        new_id = 1

    expense = {
        "id": new_id,
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    data["expenses"] = expenses
    save_data(data)
    print("Expense added successfully!")



def set_budget(data):
    print("\n--- Set Budget ---")
    print("1. Set overall monthly budget")
    print("2. Set category-wise monthly budget")
    choice = input("Enter your choice (1-2): ").strip()

    budgets = data.get("budgets", {"overall": None, "categories": {}})

    if choice == "1":
        amount = input_float("Enter overall monthly budget amount: ")
        budgets["overall"] = amount
        print(f"Overall monthly budget set to {amount:.2f}")

    elif choice == "2":
        category = input("Enter category name: ").strip()
        amount = input_float(f"Enter monthly budget for category '{category}': ")
        budgets.setdefault("categories", {})
        budgets["categories"][category] = amount
        print(f"Budget for category '{category}' set to {amount:.2f}")

    else:
        print("Invalid choice. Returning to main menu.")
        return

    data["budgets"] = budgets
    save_data(data)



def view_budgets(data):
    budgets = data.get("budgets", {"overall": None, "categories": {}})
    print("\n--- Current Budgets ---")
    overall = budgets.get("overall")
    if overall is None:
        print("Overall budget: Not set")
    else:
        print(f"Overall budget: {overall:.2f}")

    categories = budgets.get("categories", {})
    if not categories:
        print("No category-wise budgets set.")
    else:
        print("Category-wise budgets:")
        for cat, amt in categories.items():
            print(f"  {cat}: {amt:.2f}")



def main():
    data = load_data()

    while True:
        choice = show_menu()

        if choice == "1":
            add_expense(data)
        elif choice == "2":
            view_expenses(data)
        elif choice == "3":
            set_budget(data)
        elif choice == "4":
            view_budgets(data)
        elif choice == "5":
            monthly_summary(data)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()



# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
