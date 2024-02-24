class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0

    def __str__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            line_description = item["description"][:23].ljust(23)
            line_amount = "{:.2f}".format(item["amount"])[:7].rjust(30 - len(line_description))
            ledger += line_description + line_amount + "\n"
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.description)
            category.deposit(amount, "Transfer from " + self.description)
            return True
        return False

    def check_funds(self, amount):
        return self.balance >= amount


def create_spend_chart(categories):
    spent_amounts = [sum(item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories]
    total_spent = sum(spent_amounts)
    spent_percentages = [(amount / total_spent) * 100 for amount in spent_amounts]

    header = "Percentage spent by category\n"
    chart = ""
    for percentage in range(100, -1, -10):
        chart += str(percentage).rjust(3) + "|"
        for spent_percentage in spent_percentages:
            chart += " o " if spent_percentage >= percentage else "   "
        chart += " \n"

    max_length = max(len(category.description) for category in categories)
    descriptions = [category.description.ljust(max_length) for category in categories]
    footer = "    " + "-" * (3 * len(categories) + 1) + "\n"
    for line in zip(*descriptions):
        footer += "    " + "   ".join(line) + " \n"

    return (header + chart + footer).rstrip("\n")


# Example usage:
food_category = Category("Food")
entertainment_category = Category("Entertainment")
food_category.deposit(1000, "Initial deposit")
food_category.withdraw(10.15, "Groceries")
entertainment_category.deposit(200, "Initial deposit")
entertainment_category.withdraw(45, "Concert tickets")

print(create_spend_chart([food_category, entertainment_category]))
