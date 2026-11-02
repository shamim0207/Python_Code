class student:
    #constructor
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        print(f"My name is {name} and my student Id is {id} and lastly my age is {age}")
        
    #method
    def Information(self):
        print(f"name: {self.name}  ID: {self.id}")

#==============================================================


student_01 = student("shamim", "0112230207", 25)
print(student_01)

student_02=student("tahsan","0112230208",25)
print(student_02)

#method call
student_01.Information()