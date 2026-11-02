class employee():
    start_time= "10 AM"
    end_time="6 PM"
    
    
class admin(employee):
    def __init__(self,role):
        self.role=role
        
        
class accountant(admin):# admin class employee class ke inherit kore sob variable nise..r accountant class admin class ke i herit kore employee and admin duita class ke inherit korse
    
    def __init__(self, role,salary):
        super().__init__(role)
        self.salary=salary
        
        
    def accountant_info(self):
        print(f"Start time: {self.start_time}   End time: {self.end_time} Role: {self.role} Salary: {self.salary}")
        
        
#===========================================================================

ACC1=accountant("moderator", 25000)
ACC1.accountant_info()