class main:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    def show(self):
        return f"Name: {self.name} age: {self.age}"
        
        
class child(main):
    def __init__(self,name,age,roll):
        super().__init__(name,age,)
        self.roll = roll
    def d_show(self):
        de = self.show()
        print(f"{de} and my Roll {self.roll}")    
        
person = child("mahadi",10,-1)
person.d_show()
    
    