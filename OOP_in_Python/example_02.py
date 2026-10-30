class bank_account():
    def __init__(self,name,acc_no,balance):
        self.name=name
        self.acc_no=acc_no
        self.__balance=balance #private
        
        
    def get_balance(self): #getter method
        return self.__balance
    
    
    def update_balance(self,newBalnce): #setter method
        self.__balance=newBalnce
      
        
        
#===================================================

acc_01=bank_account("shamim", 1031030009473, 100_000)
#acc_01.get_balance()
#print(acc_01.get_balance())

acc_01.update_balance(200_000)

acc_01.get_balance()
print(acc_01.get_balance())
