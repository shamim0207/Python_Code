class teacher:
    start_time= "10 AM"
    end_time="6 PM"
    salary=10000
    
    
class student:
    subject="math"
    tuition_fee=5000
    
    
class TA (teacher,student):
    def __init__(self):
        super().__init__()
        
        
    def TA_INFO(self):
        print(f"TA INFO: \n Start Time: {self.start_time} \n End Time: {self.end_time} \n Salary: {self.salary} \n Tuition Fee: {self.tuition_fee}")
        
        
        
        
#=================================================

TA1=TA()
TA1.TA_INFO()
    