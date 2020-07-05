# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def create_account(self):
        account = 2312389347347
        self.account = account
        print("Account No. {} is created for {}".format(self.account, self.name))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def transfer_balance(self):
        pass

c = Customer("Dikshya")
c.create_account()