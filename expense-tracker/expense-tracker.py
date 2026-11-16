
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

# Income and Expense Categories

income_categories = [
    "Salary",
    "Freelancing",
    "Business",
    "Investment",
    "Gift",
    "Other"
]

expense_categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Education",
    "Other"
]


# Welcome Screen

name = input("\nEnter your name: ")

print("\n" + "=" * 55)
print("Welcome", name + "!")
print("Let's manage your money wisely.")
print("=" * 55)


# Main Menu

while True:

    balance = income - expenses

    print("\n" + "=" * 55)
    print("                     MAIN MENU")
    print("=" * 55)

    print("  1. Add Income")
    print("  2. Add Expense")
    print("  3. View Transactions")
    print("  4. View Balance")
    print("  5. Delete Transaction")
    print("  6. Exit")

    print("=" * 55)

    choice = input("Enter your choice (1-6): ")


    # 1. ADD INCOME

    if choice == "1":

        print("\n" + "-" * 55)
        print("                    ADD INCOME")
        print("-" * 55)

        income_title = input("Enter income title: ")

        try:

            income_amount = float(input("Enter income amount: "))

            print("\nSelect Income Category:\n")

            for i, category in enumerate(income_categories, start=1):
                print("  ", i, ".", category)

            category_choice = int(input("\nEnter category choice: "))

            if 1 <= category_choice <= len(income_categories):

                income_category = income_categories[category_choice - 1]

                income_date = input(
                    "Enter transaction date (YYYY-MM-DD): "
                )

                datetime.strptime(income_date, "%Y-%m-%d")

                if income_amount > 0 and income_title.strip() != "":

                    income += income_amount

                    transactions.append({
                        "type": "Income",
                        "title": income_title,
                        "category": income_category,
                        "amount": income_amount,
                        "date": income_date
                    })

                    print("\n" + "-" * 55)
                    print("       INCOME ADDED SUCCESSFULLY!")
                    print("-" * 55)

                    print("Title    :", income_title)
                    print("Category :", income_category)
                    print("Amount   : {:.2f}".format(income_amount))
                    print("Date     :", income_date)

                    print("-" * 55)

                else:
                    print("\n[ERROR] Invalid amount or title!")

            else:
                print("\n[ERROR] Invalid category choice!")

        except ValueError:

            print("\n[ERROR] Invalid input! Please enter valid details.")


    # 2. ADD EXPENSE

    elif choice == "2":

        print("\n" + "-" * 55)
        print("                    ADD EXPENSE")
        print("-" * 55)

        expense_title = input("Enter expense title: ")

        try:

            expense_amount = float(input("Enter expense amount: "))

            print("\nSelect Expense Category:\n")

            for i, category in enumerate(expense_categories, start=1):
                print("  ", i, ".", category)

            category_choice = int(input("\nEnter category choice: "))

            if 1 <= category_choice <= len(expense_categories):

                expense_category = expense_categories[category_choice - 1]

                expense_date = input(
                    "Enter transaction date (YYYY-MM-DD): "
                )

                datetime.strptime(expense_date, "%Y-%m-%d")

                balance = income - expenses

                if (expense_amount > 0
                        and expense_amount <= balance
                        and expense_title.strip() != ""):

                    expenses += expense_amount

                    transactions.append({
                        "type": "Expense",
                        "title": expense_title,
                        "category": expense_category,
                        "amount": expense_amount,
                        "date": expense_date
                    })

                    print("\n" + "-" * 55)
                    print("       EXPENSE ADDED SUCCESSFULLY!")
                    print("-" * 55)

                    print("Title    :", expense_title)
                    print("Category :", expense_category)
                    print("Amount   : {:.2f}".format(expense_amount))
                    print("Date     :", expense_date)

                    print("-" * 55)

                else:
                    print("\n[ERROR] Insufficient balance or invalid details!")

            else:
                print("\n[ERROR] Invalid category choice!")

        except ValueError:

            print("\n[ERROR] Invalid input! Please enter valid details.")


    # 3. VIEW TRANSACTIONS

    elif choice == "3":

        print("\n" + "=" * 105)
        print("                         TRANSACTION HISTORY")
        print("=" * 105)

        if len(transactions) == 0:

            print("\n              No transactions found.")

        else:

            print("{:<5} {:<12} {:<20} {:<16} {:<15} {:>15}".format(
                "No.",
                "Type",
                "Title",
                "Category",
                "Date",
                "Amount"
            ))

            print("-" * 105)

            for i, transaction in enumerate(transactions, start=1):

                print("{:<5} {:<12} {:<20} {:<16} {:<15} {:>15.2f}".format(
                    i,
                    transaction["type"],
                    transaction["title"],
                    transaction["category"],
                    transaction["date"],
                    transaction["amount"]
                ))

            print("-" * 105)

            print("Total Income   : {:.2f}".format(income))
            print("Total Expenses : {:.2f}".format(expenses))
            print("Current Balance: {:.2f}".format(income - expenses))

        print("=" * 105)


    # 4. VIEW BALANCE

    elif choice == "4":

        balance = income - expenses

        print("\n" + "=" * 55)
        print("                    ACCOUNT SUMMARY")
        print("=" * 55)

        print("Customer Name      :", name)

        print("-" * 55)

        print("Total Income       : {:.2f}".format(income))
        print("Total Expenses     : {:.2f}".format(expenses))

        print("-" * 55)

        print("Available Balance  : {:.2f}".format(balance))

        print("=" * 55)


    # 5. DELETE TRANSACTION

    elif choice == "5":

        print("\n" + "=" * 105)
        print("                    DELETE TRANSACTION")
        print("=" * 105)

        if len(transactions) == 0:

            print("\nNo transactions available to delete!")

        else:

            print("{:<5} {:<12} {:<20} {:<16} {:<15} {:>15}".format(
                "No.",
                "Type",
                "Title",
                "Category",
                "Date",
                "Amount"
            ))

            print("-" * 105)

            for i, transaction in enumerate(transactions, start=1):

                print("{:<5} {:<12} {:<20} {:<16} {:<15} {:>15.2f}".format(
                    i,
                    transaction["type"],
                    transaction["title"],
                    transaction["category"],
                    transaction["date"],
                    transaction["amount"]
                ))

            print("-" * 105)

            try:

                transaction_tobe_deleted = int(
                    input("\nEnter transaction number to delete: ")
                )

                if 1 <= transaction_tobe_deleted <= len(transactions):

                    confirmation_to_delete = input(
                        "Are you sure you want to delete this transaction? (yes/no): "
                    )

                    if confirmation_to_delete.lower() == "yes":

                        deleted_transaction = transactions.pop(
                            transaction_tobe_deleted - 1
                        )

                        if deleted_transaction["type"] == "Income":

                            income -= deleted_transaction["amount"]

                        else:

                            expenses -= deleted_transaction["amount"]

                        balance = income - expenses

                        print("\n" + "-" * 55)
                        print("       TRANSACTION DELETED SUCCESSFULLY!")
                        print("-" * 55)

                        print("Deleted Title :", deleted_transaction["title"])
                        print("Deleted Amount: {:.2f}".format(
                            deleted_transaction["amount"]
                        ))
                        print("Updated Balance: {:.2f}".format(balance))

                    else:

                        print("\n[INFO] Transaction deletion cancelled!")

                else:

                    print("\n[ERROR] Invalid transaction number!")

            except ValueError:

                print("\n[ERROR] Please enter a valid transaction number!")

        print("=" * 55)


    # 6. EXIT

    elif choice == "6":

        print("\n" + "=" * 55)
        print("          THANK YOU FOR USING OUR TRACKER!")
        print("=" * 55)

        print("Goodbye", name, "!")
        print("Keep saving and managing your money wisely.")

        print("=" * 55)

        break


    # INVALID CHOICE

    else:

        print("\n[ERROR] Invalid choice!")
        print("Please select an option between 1 and 6.")
