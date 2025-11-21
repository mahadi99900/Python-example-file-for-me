class person:
    def __init__(self,name,age,roll):
        self.name = name
        self.age = age
        self.roll = roll
    def __str__(self):
        return f"my name is {self.name} and my age is {self.age} and my roll is {self.roll}"
    def __eq__(self,other):
        return self.name == other.name     
    def __lt__(self,other):
        return self.age < other.age
    def __gt__(self,other):
        return self.age > other.age 
    def __add__(self,other):
        return self.age + other.age
    def __contains__(self,nam):
        return nam in self.name
    def __getitem__(self,key):
        if key == "name":
            return self.name
        elif key == "age":
            return self.age
        elif key == "roll":
            return self.roll
        else:
            return f"\n'{key}' is not founded"
    def __repr__(self):
        return f"person name {self.name} and age {self.age} and roll {self.roll}"        
    def __len__(self):
        return len(self.name)
    
                        
p1 = person("mahadi",20,-1)
p2 = person("hasan",18,-1)
p3 = person("mahmud",19,-3)
   
#print(p1)
#print(p1 == p2)
#print(p1 < p2)
#print(p1 > p2)
#print(p1 + p2)
#print("hasan" in p2)
#print(p1["name"],p1["age"],p1["roll"])        
#print(repr(p1))
#print(len(p1))
    