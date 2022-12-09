class Account:

  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def showBalance(self):
    print("This account contains $" + str(self.balance) + ".00.")

  def deposit(self, amount):
    self.balance += amount
    print("$" + str(amount) + ".00 has been deposted to this account.")
    print("The account now contains $" + str(self.balance) + ".00.")

  def withdraw(self, amount):
    if amount > self.balance:
        print("You can not overdraw your account.")
    else:
        self.balance -= amount
        print("$" + str(amount) + ".00 has been withdrawn from this account.")
        print("The account now contains $" + str(self.balance) + ".00.")

moneys = Account("Dan", 50)
print()
moneys.deposit(80)
print()
moneys.withdraw(90)
print()
moneys.showBalance()