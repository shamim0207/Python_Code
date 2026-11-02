class employee():
    def get_designation(self):
        print("Designation= Admin")
        
        
        
        
class teacher(employee):
    def get_designation(self):
            print("Designation= teacher")
            
            
#===============================================

t1=teacher()
t1.get_designation()