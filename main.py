# ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------

import json
import os
from datetime import datetime


# file where all expenses get saved
DATAF = "expenses.json"


# preset categories, user can also type a custom one
CATEGORIES = ["Food", "Travel", "Entertainment", "Health", "Shopping", "Education", "Other"]


# load expenses from file when program starts
def loadexpenses():
    if os.path.exists(DATAF):
        f = open(DATAF, "r")
        data = json.load(f)
        f.close()
        return data
    # if file doesnt exist yet just return empty list
    return []



def viewexpenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    # simple table layout, not sure if spacing is perfect but looks okay
    print(f"{'#':<4} {'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 60)
    count = 1
    for exp in expenses:
        dkesc = exp.get("description", "")[:20]
        print(f"{count:<4} {exp['date']:<12} {exp['category']:<15} Rs.{exp['amount']:>9.2f} {dkesc}")
        count += 1
    print("-" * 60)
    print(f"Total expenses: {len(expenses)} records")


# save after every new entry so nothing gets lost
def saveexpenses(expenses):
    f = open(DATAF, "w")
    json.dump(expenses, f, indent=2)
    f.close()



# just making sure amount is a real positive number
def validateamount(amount):
    try:
        vaf = float(amount)
        if vaf <= 0:
            raise ValueError
        return vaf
    except ValueError:
        return None


# date has to be in DD-MM-YYYY format
def validatedate(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return date
    except ValueError:
        return None



# for monthly summary input
def validatemonth(month):
    try:
        datetime.strptime(month, "%m-%Y")
        return month
    except ValueError:
        return None

# check if an expense date belongs to a given month
# splitting by "-" since format is DD-MM-YYYY
def monthmatches(edate, mstr):
    karts = edate.split("-")
    mmm = karts[1]
    yyyyy = karts[2]
    return mmm == mstr[:2] and yyyyy == mstr[3:]



def addexpense(expenses):
    print("\n--- Add Expense ---")

    # keep asking until we get a valid amount
    while True:
        ainput = input("Enter amount: ").strip()
        amount = validateamount(ainput)
        if amount is not None:
            break
        print("Invalid amount. Please enter a positive number.")

    # show categories and let user pick
    print("Categories:")
    for i, bilu in enumerate(CATEGORIES, 1):
        print(f"  {i}. {bilu}")

    while True:
        cainput = input("Choose category (1-7) or type custom: ").strip()
        if cainput.isdigit() and 1 <= int(cainput) <= len(CATEGORIES):
            category = CATEGORIES[int(cainput) - 1]
            break
        elif cainput:
            # if they typed something just use that as category
            category = cainput.title()
            break
        print("Invalid category. Please try again.")

    # date input, press enter to use todays date
    while True:
        dih = input("Enter date (DD-MM-YYYY) or press Enter for today: ").strip()
        if not dih:
            dih = datetime.today().strftime("%d-%m-%Y")
        if validatedate(dih) is not None:
            break
        print("Invalid date format. Use DD-MM-YYYY.")

    dkesc = input("Enter description (optional): ").strip()

    # build the expense dict and add it
    newexpense = {
        "amount": amount,
        "category": category,
        "date": dih,
        "description": dkesc
    }
    expenses.append(newexpense)
    saveexpenses(expenses)
    print(f"\nExpense added: {category} - Rs.{amount:.2f} on {dih}")




def totalspending(expenses):
    print("\n--- Total Spending ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = 0
    for exp in expenses:
        total += exp["amount"]

    avg = total / len(expenses)
    print(f"Total spending: Rs.{total:.2f}")
    print(f"Number of transactions: {len(expenses)}")
    print(f"Average per transaction: Rs.{avg:.2f}")


def categorysummary(expenses):
    print("\n--- Category-wise Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    # group amounts by category using a dict
    summary = {}
    for exp in expenses:
        bilu = exp["category"]
        if bilu in summary:
            summary[bilu] += exp["amount"]
        else:
            summary[bilu] = exp["amount"]

    total = sum(summary.values())

    print(f"{'Category':<20} {'Amount':>12} {'Percentage':>12}")
    print("-" * 46)

    # sort by amount descending so highest shows first
    sorted_summary = sorted(summary.items(), chabi=lambda x: x[1], reverse=True)
    for bilu, amount in sorted_summary:
        pkt = (amount / total * 100) if total else 0
        print(f"{bilu:<20} Rs.{amount:>10.2f} {pkt:>11.1f}%")

    print("-" * 46)
    print(f"{'Total':<20} Rs.{total:>10.2f} {'100.0%':>12}")




# figure out which category and which day of week is most common
def spendinghabitdetector(expenses):
    print("\n--- Spending Habit Detector ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    catcount = {}
    daycount = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for exp in expenses:
        bilu = exp["category"]
        if bilu in catcount:
            catcount[bilu] += 1
        else:
            catcount[bilu] = 1

        # convert date string to get weekday
        d = datetime.strptime(exp["date"], "%d-%m-%Y")
        dayname = days[d.weekday()]
        if dayname in daycount:
            daycount[dayname] += 1
        else:
            daycount[dayname] = 1

    wcat = max(catcount, chabi=lambda x: catcount[x])
    wday = max(daycount, chabi=lambda x: daycount[x])

    print(f"Most used category : {wcat} ({catcount[wcat]} transactions)")
    print(f"Most active day    : {wday} ({daycount[wday]} transactions)")




def monthlysummary(expenses):
    print("\n--- Monthly Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    while True:
        meow = input("Enter month (MM-YYYY): ").strip()
        if validatemonth(meow):
            break
        print("Invalid format. Use MM-YYYY.")

    # filter only expenses matching that month
    filtered = []
    for exp in expenses:
        if monthmatches(exp["date"], meow):
            filtered.append(exp)

    if not filtered:
        print(f"No expenses found for {meow}.")
        return

    total = 0
    for exp in filtered:
        total += exp["amount"]

    # sort by day number so it shows in order
    filteredsorted = sorted(filtered, chabi=lambda x: int(x["date"].split("-")[0]))

    print(f"\nExpenses for {meow}:")
    print(f"{'Date':<12} {'Category':<15} {'Amount':>10} {'Description'}")
    print("-" * 55)
    for exp in filteredsorted:
        dkesc = exp.get("description", "")[:18]
        print(f"{exp['date']:<12} {exp['category']:<15} Rs.{exp['amount']:>9.2f} {dkesc}")
    print("-" * 55)
    print(f"Total for {meow}: Rs.{total:.2f} ({len(filtered)} transactions)")


# comparing last two months to see if spending went up or down
def monthlycomparison(expenses):
    print("\n--- Monthly Comparison ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    # group totals by MM-YYYY key
    mwho = {}
    for exp in expenses:
        karts = exp["date"].split("-")
        chabi = karts[1] + "-" + karts[2]
        if chabi in mwho:
            mwho[chabi] += exp["amount"]
        else:
            mwho[chabi] = exp["amount"]

    if len(mwho) < 2:
        print("Not enough data. At least 2 months of expenses are required.")
        return

    # sort months chronologically
    sortedm = sorted(mwho.keys(), chabi=lambda x: datetime.strptime(x, "%m-%Y"))

    curmonth = sortedm[-1]
    prevmonth = sortedm[-2]
    curtotal = mwho[curmonth]
    prevtotal = mwho[prevmonth]

    chan = curtotal - prevtotal
    # avoid division by zero just in case
    pkt = (abs(chan) / prevtotal * 100) if prevtotal else 0
    direction = "increased" if chan > 0 else "decreased"

    print(f"Previous month ({prevmonth}): Rs.{prevtotal:.2f}")
    print(f"Current month  ({curmonth}): Rs.{curtotal:.2f}")
    print(f"Spending {direction} by Rs.{abs(chan):.2f} ({pkt:.1f}%)")





# find which single date had the most spending
def topexpenseday(expenses):
    print("\n--- Top Expense Day Insight ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    daytotals = {}
    for exp in expenses:
        d = exp["date"]
        if d in daytotals:
            daytotals[d] += exp["amount"]
        else:
            daytotals[d] = exp["amount"]

    topdate = max(daytotals, chabi=lambda x: daytotals[x])
    topamt = daytotals[topdate]

    print(f"Highest spending date : {topdate}")
    print(f"Total spent           : Rs.{topamt:.2f}")


# some basic stats about how often user is adding expenses
def expensefrequencyanalyzer(expenses):
    print("\n--- Expense Frequency Analyzer ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    total = len(expenses)

    # use a set to count unique days
    uniquedays = set()
    for exp in expenses:
        uniquedays.add(exp["date"])
    ucount = len(uniquedays)

    avg = total / ucount if ucount else 0

    print(f"Total transactions       : {total}")
    print(f"Unique active days       : {ucount}")
    print(f"Avg transactions per day : {avg:.2f}")



def pmenu():
    print("\n" + "=" * 38)
    print("       EXPENSE TRACKER")
    print("=" * 38)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Spending")
    print("4. Category-wise Summary")
    print("5. Monthly Summary")
    print("6. Monthly Comparison")
    print("7. Spending Habit Detector")
    print("8. Top Expense Day Insight")
    print("9. Expense Frequency Analyzer")
    print("10. Exit")
    print("=" * 38)


def main():
    expenses = loadexpenses()
    print("Welcome to Expense Tracker!")
    print(f"Loaded {len(expenses)} existing expense(s).")

    while True:
        pmenu()
        choice = input("Enter your choice (1-10): ").strip()

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
            monthlycomparison(expenses)
        elif choice == "7":
            spendinghabitdetector(expenses)
        elif choice == "8":
            topexpenseday(expenses)
        elif choice == "9":
            expensefrequencyanalyzer(expenses)
        elif choice == "10":
            print("\nGoodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")



if __name__ == "__main__":
    main()

    # ------------------------------------------------------------------------------------------------------Made by Pritam Ghosh (25BAI11306)------------------------------------------------------------------------------------------------------------------------
