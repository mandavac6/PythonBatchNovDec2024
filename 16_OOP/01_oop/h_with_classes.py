"""
Purpose: Solving Bank account management problem, using classes
"""


class Account:
    def __init__(self, name):
        self.balance = 0
        self.account_holder = name

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawl(self, amount):
        self.balance = self.balance - amount

    def display_balance(self):
        return f"Account Balance for {self.account_holder} is {self.balance}"


if __name__ == "__main__":
    tom = Account("tom")
    print(vars(tom))

    gronk = Account("gronk")
    print(vars(gronk))
    print("Initially", gronk.display_balance())

    gronk.deposit(1000)
    print("After Deposit", gronk.display_balance())

    gronk.withdrawl(400)
    print("After withdrawl", gronk.display_balance())

    print("----------------------------")
    jule = Account("jule")
    print(vars(jule))

    print("Initially", jule.display_balance())

    jule.deposit(300)
    print("After Deposit", jule.display_balance())

    jule.withdrawl(100)
    print("After withdrawl", jule.display_balance())