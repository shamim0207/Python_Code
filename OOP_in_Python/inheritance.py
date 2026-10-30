class employee():
    start_time= "10 AM"
    
    end_time="6 PM"
    


class teacher(employee):
    def __init__(self,subject):
        self.subject=subject

    def teacher_info(self):
        print(f"Start time: {self.start_time}   End time: {self.end_time} Subject: {self.subject}")    
        
        
class admin(employee):
    def __init__(self,role):
        self.role=role
        
    def adminView(self):
        print(f"Start time: {self.start_time}   End time: {self.end_time} Role: {self.role}")    
                
        
#=============================================

T1=teacher("Math")
T1.teacher_info()



A1=admin("Modaratore")
A1.adminView()