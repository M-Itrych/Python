class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        res = ""
        res += f"{self.category}".center(30, "*") + "\n"
        for item in self.ledger:
            res += f"{item[1][:23]}"
            res += f"{item[0]:.2f}".rjust(30 - len(item[1][:23]), " ") + "\n"
        return res

    def deposit(self, amount, description=""):
        self.ledger.append([amount / 1, description])

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append([amount * -1, description])
        return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item[0]

        return balance

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.ledger.append([amount * -1, f"Transfer to {destination.category}"])
        destination.deposit(amount, f"Transfer from {self.category}")
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    spend_data = []
    all_spendings = 0
    for category in categories:
        total_spend = 0
        for item in category.ledger:
            if item[0] < 0:
                total_spend += item[0] * -1
        all_spendings += round(total_spend, 2)
        spend_data.append([category.category, round(total_spend, 2)])

    procent_data = []

    for item in spend_data:
        procent_data.append([item[0], round((item[1] / all_spendings * 100) / 10)*10])

    res = ""
    res = "Percentage spent by category\n"
    count = 100
    for i in range(11):
        res += f"{count}|".rjust(4, " ")
        for item in procent_data:
            if round(item[1] / 10)*10 - 10 >= count:
                res += " 0 "
            else:
                res += "   "
            if procent_data.index(item) == len(procent_data) - 1:
                res += "\n"
        count -= 10

    category_names = []
    for item in procent_data:


    return res
