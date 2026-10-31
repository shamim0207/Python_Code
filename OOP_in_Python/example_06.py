from abc import ABC
class employee(ABC):
    def calc_salary():
        pass
    
    
    
class intern(employee):
    def calc_salary(self,name,role,salary):
        print(f"your name is {name}\n your role is {role}\n and your salary is {salary}")
        


class full_time_emplyee(employee):
    def calc_salary(self,name,role,salary):
            print(f"your name is {name}\n your role is {role}\n and your salary is {salary}")

#===============================================================================

intern=intern()
intern.calc_salary("Shamim","Intern", 5000)



full_time_emplyee=full_time_emplyee()
full_time_emplyee.calc_salary("hamim","Full time employee", 25000)