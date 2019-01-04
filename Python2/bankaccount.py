class BankAccount(object):
  balance = 0
  
  def __init__(self,name):
    self.name = name 
  def __repr__(self):
    return "Account belongs to %s" %self.name
    return "Balance: $%.2f" % self.balance
    
  def show_balance(self):
    print "Balance: $%.2f" % self.balance
    return
  def deposit(self,amount):
    self.amount = amount
    if self.amount <= 0:
      print 'Can not be negative number'
      return
    else:
      print "Deposit Amount is: $%.2f" % self.amount
      self.balance += self.amount
      self.show_balance()
  def withdraw(self,amount):
    self.amount = amount
    if self.amount > self.balance:
      print 'Insufficent Funds'
      return
    
    else:
      print 'Withdrawn: $%.2f' %self.amount
      self.balance -= self.amount
      self.show_balance()
 

my_account = BankAccount('John')



def bank():
	
  print my_account
  
  while True:
    ans = raw_input('What would you like to do today:\n D: Deposit\n W: Withdraw\n S: Show Balance\n X: Quit: ')
  
    ans = ans.upper()
    if ans == 'D':
      amount = raw_input('Please enter the amount you would like to deposit: ')
      amount = float(amount)
      my_account.deposit(amount)
      print 'Deposit of %.2f Successful' %amount
      my_account.show_balance()
	
    elif ans == 'W':
      amount = raw_input('Please enter the amount you would like to withdraw: ')
      amount = float(amount)
      my_account.withdraw(amount)
      my_account.show_balance()
    
    elif ans == 'S':
      my_account.show_balance()
    
    
    
    
    elif ans == 'X':
      print 'Goodbye for now...'
      break
    
    else:
      print 'Invalid Input, please try again!'
 
bank()