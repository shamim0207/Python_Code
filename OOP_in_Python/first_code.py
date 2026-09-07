class student_info:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
        

#==============================================================


stu1=student_info("bob", 112230205, "cse")
stu2=student_info("carrol", 112230207, "cse")

print(stu1.name,stu1.id,stu1.dept)
print(stu2.name,stu2.id,stu2.dept)