
from datetime import datetime


print("=" * 75)
print("                    PERSONAL EXPENSE TRACKER")
print("=" * 75)

print("                  Developed by: Paribartan Kalathoki")
print("=" * 75)


# Initialize variables
income = 0
expenses = 0
balance = 0

transactions = []


name = input("\nEnter your name: ")

print("\nWelcome", name, "!")
print("Let's manage your money wisely.")


# Main Menu

while True:

    balance = income - expenses

    print("\n" + "=" * 55)
    print("                     MAIN MENU")
    print("=" * 55)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")

    print("=" * 55)

    choice = input("Enter your choice (1-5): ")


    # 1. ADD INCOME

    if choice == "1":

        print("\n" + "-" * 55)
        print("                    ADD INCOME")
        print("-" * 55)

        income_title = input("Enter income title: ")

        try:
            income_amount = float(input("Enter income amount: "))

            income_date = input("Enter transaction date (YYYY-MM-DD): ")

            datetime.strptime(income_date, "%Y-%m-%d")

            if income_amount > 0 and income_title.strip() != "":

                income += income_amount

                transactions.append({
                    "type": "Income",
                    "title": income_title,
                    "amount": income_amount,
                    "date": income_date
                })

                print("\nIncome added successfully!")
                print("Title  :", income_title)
                print("Amount :", income_amount)
                print("Date   :", income_date)

            else:
                print("Invalid amount or title!")

        except ValueError:
            print("Invalid amount or date!")
            print("Please enter a valid amount and date.")


    # 2. ADD EXPENSE

    elif choice == "2":

        print("\n" + "-" * 55)
        print("                    ADD EXPENSE")
        print("-" * 55)

        expense_title = input("Enter expense title: ")

        try:
            expense_amount = float(input("Enter expense amount: "))

            expense_date = input("Enter transaction date (YYYY-MM-DD): ")

            datetime.strptime(expense_date, "%Y-%m-%d")

            balance = income - expenses

            if expense_amount > 0 and expense_amount <= balance and expense_title.strip() != "":

                expenses += expense_amount

                transactions.append({
                    "type": "Expense",
                    "title": expense_title,
                    "amount": expense_amount,
                    "date": expense_date
                })

                print("\nExpense added successfully!")
                print("Title  :", expense_title)
                print("Amount :", expense_amount)
                print("Date   :", expense_date)

            else:
                print("Insufficient balance or invalid details!")

        except ValueError:
            print("Invalid amount or date!")
            print("Please enter a valid amount and date.")


    # 3. VIEW TRANSACTIONS

    elif choice == "3":

        print("\n" + "=" * 80)
        print("                         TRANSACTION HISTORY")
        print("=" * 80)

        if len(transactions) == 0:

            print("No transactions found.")

        else:

            print("{:<5} {:<12} {:<22} {:<15} {:>12}".format(
                "No.", "Type", "Title", "Date", "Amount"
            ))

            print("-" * 80)

            for i, transaction in enumerate(transactions, start=1):

                print("{:<5} {:<12} {:<22} {:<15} {:>12.2f}".format(
                    i,
                    transaction["type"],
                    transaction["title"],
                    transaction["date"],
                    transaction["amount"]
                ))

            print("-" * 80)

            print("Total Income   :", income)
            print("Total Expenses :", expenses)
            print("Current Balance:", income - expenses)


    # 4. VIEW BALANCE

    elif choice == "4":

        balance = income - expenses

        print("\n" + "=" * 55)
        print("                    ACCOUNT SUMMARY")
        print("=" * 55)

        print("Customer Name      :", name)

        print("-" * 55)

        print("Total Income       :", income)
        print("Total Expenses     :", expenses)

        print("-" * 55)

        print("Available Balance  :", balance)

        print("=" * 55)


    # 5. EXIT

    elif choice == "5":

        print("\n" + "=" * 55)
        print("          THANK YOU FOR USING OUR TRACKER!")
        print("=" * 55)

        print("Goodbye", name, "!")
        print("Keep saving and managing your money wisely.")

        print("=" * 55)

        break


    # INVALID CHOICE

    else:

        print("\nInvalid choice!")
        print("Please select an option between 1 and 5.")
