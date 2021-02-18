class Category:
  def __init__(self, category):
    self.name = category
    self.ledger = []

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description = ""):
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -abs(amount), "description": description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for transaction in self.ledger:
      balance += transaction['amount']
    return balance

  def transfer(self, amount, category):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount, "Transfer from " + self.name)
      return True
    else:
      return False

  def check_funds(self, amount):
    if (amount > self.get_balance()):
      return False
    else:
      return True

  def __str__(self):
    result = "*" * (15 - int(len(self.name)/2)) + self.name + "*" * (15 - int(len(self.name)/2))
    for transaction in self.ledger:
      amount = "{:.2f}".format(transaction['amount'])
      description = transaction['description'][:23]
      result += "\n" + description + " " * (30 - len(description) - len(amount)) + str(amount)
    result += "\nTotal: " + str(self.get_balance())
    return result

  def spent(self):
    spent = 0
    for transaction in self.ledger:
      if (transaction['amount'] < 0):
        spent += abs(transaction['amount'])
    return spent

  def get_name(self):
    return self.name

def create_spend_chart(categories):
  result = "Percentage spent by category\n"
  total = 0
  for category in categories:
    total += category.spent()
  for i in range(10, -1, -1):
    result += "{0:3d}".format(i * 10) + "| "
    for category in categories:
      if (round((category.spent()/total)*100, 1) > i*10):
        result += "o  "
      else:
        result += "   "
    result += "\n"
  result += "    ----------"

  length = []
  for category in categories:
    length.append(len(category.get_name()))
  i = 0
  while (max(length) > i):
    result += "\n     "
    for category in categories:
      if (len(category.get_name()) > i):
        result += category.get_name()[i] + "  "
      else:
        result += "   "
    i += 1
  return result