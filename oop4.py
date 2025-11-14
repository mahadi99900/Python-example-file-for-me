class person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age
    def hello(self):
        print(f"my name is {self.name} and my age is {self.age}") 
    def hi(self):
        print(f"my friend name is {self.name} ane his age is {self.age}") 
p1 = person("mahadi")
p2 = person("hasan",10)  
print(p1.name,p1.age)
print(p2.name,p2.age) 
p1.hello()
p2.hello() 
p2.hi()     