class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance      # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn", amount)
        else:
            print("Not enough balance!")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Prajith", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.get_balance())
acc.withdraw(5000)
