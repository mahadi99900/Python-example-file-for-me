class student:
    class_year = 2025
    num_student = 0
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_student += 1
    def show(self):
        print(f"student name is {self.name} and age is {self.age}")
        
student1 = student("mahadi",10) 
student2 = student("hasan",30)
student3 = student("imran",18) 
student4 = student("rakib",37)

print(student.num_student)