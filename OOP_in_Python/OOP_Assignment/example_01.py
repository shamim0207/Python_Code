class bank_account():
    def __init__(self, owner_name, account_number, balance):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        
    def deposite(self, deposite_balance):
        self.balance += deposite_balance  
        print(f"Deposited {deposite_balance}. {self.owner_name}'s current balance is {self.balance}")
        
    def withdraw(self, withdraw_balance):
        if withdraw_balance > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= withdraw_balance 
            print(f"Withdrew {withdraw_balance}. {self.owner_name}'s current balance is {self.balance}")
        
    def check_balance(self):
         print(f"{self.owner_name}'s account balance is {self.balance}")
         
#======================================================

acc1 = bank_account("Shamim", 1071070009473, 100_000)
acc1.deposite(50_000)
acc1.withdraw(25_000)
acc1.check_balance()