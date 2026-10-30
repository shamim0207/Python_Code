# Create a student class with private attributes _name,_roll_no, and _marks.
# Provide getter and setter methods with validation (e.g., marks cannot be
# negative, roll number has to be between 1 &100&name cannot be empty)



class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        if name and name.strip(): 
            self.__name = name
        else:
            print("Error: Name cannot be empty!")
            self.__name = "Unknown"


    def get_roll_no(self):
        return self.__roll_no
        
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100: 
            self.__roll_no = roll_no
        else:
            print(f"Error: Roll number {roll_no} is invalid! Must be between 1 & 100.")
            self.__roll_no = None

    def get_marks(self):
        return self.__marks
        
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Error: Marks cannot be negative!")
            self.__marks = 0


    def display_info(self):
        print(f"Student Name: {self.__name}, Roll: {self.__roll_no}, Marks: {self.__marks}")



class CollegeStudent(Student):
    def __init__(self, name, roll_no, marks, department):
        super().__init__(name, roll_no, marks)
        self.department = department


    def display_info(self):
        print(f"[College Student] Name: {self.get_name()}, Roll: {self.get_roll_no()}, Marks: {self.get_marks()}, Department: {self.department}")


#======================================================


s1 = CollegeStudent("Shamim", 45, 85, "Computer Science")
s1.display_info()  



s2 = CollegeStudent("", 150, -20, "Physics")
s2.display_info()
        
        
        
