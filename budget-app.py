
"""
Budget App
==========

A simple budget management application that tracks deposits,
withdrawals and transfers across different spending categories.

Features:
- Create budget categories.
- Deposit and withdraw money.
- Check category balances.
- Transfer money between categories.
- Display a formatted transaction ledger.
- Generate a spending percentage chart.
"""


class Category:
    """
    Represents a budget category.

    Each category has a name and a ledger containing
    all its deposits and withdrawals.
    """

    def __init__(self, name):
        # Store the category name.
        self.name = name

        # Store all transactions for this category.
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Add money to the category.

        Args:
            amount: Amount of money to deposit.
            description: Optional transaction description.
        """

        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        """
        Withdraw money if sufficient funds are available.

        Withdrawals are stored as negative amounts.

        Returns:
            True if successful, False otherwise.
        """

        if self.check_funds(amount):

            self.ledger.append({
                "amount": -amount,
                "description": description
            })

            return True

        return False

    def get_balance(self):
        """
        Calculate the current balance.

        Adds all deposits and withdrawals together.
        """

        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfer money to another budget category.

        Args:
            amount: Amount to transfer.
            category: Destination Category object.

        Returns:
            True if successful, False otherwise.
        """

        if self.check_funds(amount):

            # Withdraw from the source category.
            self.withdraw(amount, f"Transfer to {category.name}")

            # Deposit into the destination category.
            category.deposit(amount, f"Transfer from {self.name}")

            return True

        return False

    def check_funds(self, amount):
        """
        Check whether enough money is available.

        Returns True if the balance covers the amount,
        otherwise returns False.
        """

        return self.get_balance() >= amount

    def __str__(self):
        """
        Return a formatted representation of the category.

        Displays the category name, transaction history
        and current balance.
        """

        # Centre the category name within 30 characters.
        result = self.name.center(30, "*") + "\n"

        # Display each transaction.
        for item in self.ledger:

            # Limit descriptions to 23 characters.
            # Left-align descriptions and right-align amounts.
            result += (
                f"{item['description'][:23]:23}"
                f"{item['amount']:7.2f}\n"
            )

        # Display the final balance.
        result += f"Total: {self.get_balance()}"

        return result


def create_spend_chart(categories):
    """
    Generate a bar chart showing spending percentages
    across different budget categories.

    Only withdrawals are counted as spending.
    Deposits are ignored.

    Percentages are rounded down to the nearest 10.

    Args:
        categories: A list of Category objects.

    Returns:
        A formatted string representing the spending chart.
    """

    # Handle an empty category list.
    if not categories:
        return "Percentage spent by category\n"

    total_amount = 0
    total_spent = []

    # Calculate total withdrawals for each category.
    for category in categories:

        category_spending = 0

        for item in category.ledger:

            # Withdrawals are negative, so use abs()
            # to get their positive spending value.
            if item["amount"] < 0:
                category_spending += abs(item["amount"])

        total_spent.append(category_spending)
        total_amount += category_spending

    # Handle categories with no withdrawals.
    # Avoid division by zero.
    if total_amount == 0:
        percentages = [0] * len(categories)

    else:
        percentages = []

        # Calculate each category's percentage of total spending.
        for category_spending in total_spent:

            percentage = int(
                category_spending / total_amount * 10
            ) * 10

            percentages.append(percentage)

    # Start building the chart.
    chart = "Percentage spent by category\n"

    # Generate percentage levels from 100 down to 0.
    for percentage_level in range(100, -1, -10):

        # Display the percentage label.
        chart += str(percentage_level).rjust(3) + "| "

        # Draw the bars for each category.
        for percentage in percentages:

            if percentage >= percentage_level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Draw the horizontal line beneath the bars.
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Find the longest category name.
    longest_name = max(
        len(category.name) for category in categories
    )

    # Display category names vertically.
    for letter_index in range(longest_name):

        chart += "     "

        for category in categories:

            # Display one letter from each category name.
            if letter_index < len(category.name):
                chart += category.name[letter_index] + "  "
            else:
                chart += "   "

        # Avoid an extra newline at the end of the chart.
        if letter_index < longest_name - 1:
            chart += "\n"

    return chart


# --------------------------------------------------
# Example usage / testing
# --------------------------------------------------

if __name__ == "__main__":

    # Create budget categories.
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    # Add deposits.
    food.deposit(900, "Initial deposit")
    clothing.deposit(900, "Initial deposit")
    auto.deposit(900, "Initial deposit")

    # Add withdrawals.
    food.withdraw(45.67, "Groceries")
    food.withdraw(30.50, "Lunch")

    clothing.withdraw(20, "New shirt")

    auto.withdraw(15, "Fuel")

    # Test a transfer.
    food.transfer(50, clothing)

    # Display individual category ledgers.
    print(food)
    print()
    print(clothing)
    print()
    print(auto)

    # Display spending chart.
    print()
    print(create_spend_chart([food, clothing, auto]))
