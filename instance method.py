class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"my name is {self.name},and my age is {self.age}")    
a = student("mahadi",18)    
a.show()
    
    
    