class BankAccount():
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        
        
    def deposit(self, amount):
        # your code here
        self.balance += amount
        print(self.balance)
        return self
    
    def withdraw(self, amount):
        # your code here
        self.balance - amount
        if (self.balance - amount) > 0:
            self.balance -= amount
            print("insufficient funds: charging a $5 fee, your balance is {self.balance}")
            return self
        
    def display_account_info(self):
        # your code here
        print(self.balance)
        return self
    
    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        else:
            print("account balance is negative")
        return self
    

Anthony = BankAccount(.2, 500)
Tom = BankAccount(.2,400)

Anthony.deposit(100).deposit(600).deposit(1000).yield_interest().display_account_info()
Tom.deposit(200).deposit(55.55).withdraw(200).display_account_info()