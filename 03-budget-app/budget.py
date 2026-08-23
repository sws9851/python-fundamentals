class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger: list[dict] = []

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self) -> float:
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, receiver: "Category") -> bool:
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {receiver.name}")
        receiver.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount: float) -> bool:
        return self.get_balance() >= amount

    def __str__(self) -> str:
        lines = [f"{self.name:*^30}"]
        for item in self.ledger:
            amount = f"{item['amount']:.2f}"[:7]
            lines.append(f"{item['description']:<23.23}{amount:>7}")
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def total_spent(category: Category) -> float:
    return -sum(item["amount"] for item in category.ledger if item["amount"] < 0)


def create_spend_chart(categories: list[Category]) -> str:
    """Bar chart of each category's share of total spending, floored to 10% steps."""
    spent = [total_spent(category) for category in categories]
    total = sum(spent)
    # float division, so a share landing exactly on a boundary can tip either way
    percentages = [int(amount / total * 100 // 10) * 10 for amount in spent]

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        bars = "".join("o  " if percent >= level else "   " for percent in percentages)
        lines.append(f"{level:>3}| {bars}")

    lines.append("    " + "-" * (3 * len(categories) + 1))

    longest_name = max(len(category.name) for category in categories)
    padded = [category.name.ljust(longest_name) for category in categories]
    for position in range(longest_name):
        letters = "".join(f"{name[position]}  " for name in padded)
        lines.append(f"     {letters}")

    return "\n".join(lines)
