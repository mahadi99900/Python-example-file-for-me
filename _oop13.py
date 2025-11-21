import math

class Shape:
    def __init__(self,colour,is_filled):
        self.colour = colour
        self.is_filled = is_filled
    def describe(self):
        print(f"It is colour:{self.colour} and {'filled' if self.is_filled else 'not filled'}")
            
class Circle(Shape):
    def __init__(self,colour,is_filled,radius):
        super().__init__(colour,is_filled)
        self.radius = radius
    def describe(self):
        print(f"πr^2 = {math.pi * self.radius * self.radius}")   
        super().describe()

class Square(Shape):
    def __init__(self,colour,is_filled,width):
        super().__init__(colour,is_filled)
        self.width = width
    def describe(self):
        print(f"width^2 = {pow(self.width,2)}")
        super().describe()    
    
class Triangle(Shape):
    def __init__(self,colour,is_filled,width,height):
        super().__init__(colour,is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"(width × height) / 2 ={(self.width * self.height) / 2 }") 
        super().describe()      
        
c = Circle(colour="blue",is_filled=True,radius=5)          
s = Square(colour="red",is_filled=False,width=10)
t = Triangle(colour="yellow",is_filled=True,width=7,height=10)

c.describe()
s.describe()
t.describe()