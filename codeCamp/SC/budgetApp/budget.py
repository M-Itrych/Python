class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        res = f"{self.name}".center(30, "*") + "\n"
        for x in self.ledger:
            res += f"{x["description"][:23]}"
            res += f"{x["amount"]:.2f}".rjust(30 - len(x["description"][:23]), " ") + "\n"
        res += f"Total: {self.get_balance():.2f}"
        return res

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount * 1.0, "description": desc})

    def withdraw(self, amount, desc=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": amount * -1.0, "description": desc})
        return True

    def get_balance(self):
        bal = 0
        for category in self.ledger:
            bal += category["amount"]
        return bal

    def transfer(self, amount, transfer_to):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {transfer_to.name}")
        transfer_to.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True


def create_spend_chart(categories):
    spent_data = []
    all_spent = 0
    for category in categories:
        total_spent = 0
        category_name = category.name
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent += item["amount"]
        all_spent += total_spent
        spent_data.append({"category": category_name, f"spent": total_spent})

    res = ""
    for i in range(100, -10, -10):
        res += f"{i}|".rjust(4, " ")
        for data in spent_data:
            if (data["spent"] / all_spent) * 100 >= i:
                if spent_data.index(data) == len(spent_data) - 1:
                    res += " o "
                else:
                    res += " o "

        res += "\n"

    res += f"    ".ljust(len(spent_data)*3 + 4, "-") + "\n"

    max_len = max(len(data["category"]) for data in spent_data)
    for i in range(max_len):
        res += "     "
        for data in spent_data:
            if i < len(data["category"]):
                res += f" {data['category'][i]} "
            else:
                res += "   "
        res += "\n"

    return res

