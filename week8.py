class BankAccount():
  def __init__(self, accountnumber, balance):
    self.accountnumber = accountnumber
    self.balance = balance
  def getAccountInfo(self):
    return(self.accountnumber + " is your account number and your balance is " + self.balance + ".")
    
  
print ("Welcome to banking online!")
while True:
  try:
    getbalance = str(input("Please enter if you would like to withdraw, deposit or get balance? "))
    break
  except:
    print ("To withdraw or deposit, please go to following page.")
  
class checking(BankAccount):
  def __init__(self, fees, minimumbalance):
    self.fees =  fees
    self.minimumbalance = minimumbalance
  def getCheckingInfo(self):
    return(self.fees + " are your account monthly fees" + self.minimumbalance + " is your minimum balance. ")
class savings(BankAccount):
  def __init__(self, interestrate):
    self.interestrate =  interestrate
  def getSavingsInfo(self):
    return("Your account balance plus your interest rate of 2% is " + self.interestrate)
    

checking = BankAccount("182931", "$100")
print("Checking- " + checking.getAccountInfo())
print("\n")
savings = BankAccount("19204328", "$25")
print("Savings- " +savings.getAccountInfo())
print("\n")
checking =  ("$5" , "$50")
print("With checking, you have " + checking.getCheckingInfo())
print("\n")
savings = savings ("2% iterest rate making your balance $25.50")
print("In your savings you have $25 with a " + savings.getSavingsInfo())
print("\n")
