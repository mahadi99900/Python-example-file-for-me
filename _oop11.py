class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def p_show(self):
        print(f"Name; {self.name} age; {self.age}") 
class worker:
    def __init__(self,titel,selary):
        self.titel = titel
        self.selary = selary
    def w_show(self):
        print(f"Titel; {self.titel} Selary; {self.selary}") 
class show(person,worker):
    def __init__(self,name,age,titel,selary):
        person.__init__(self,name,age)
        worker.__init__(self,titel,selary)
    def s_show(self):
        print(f"Name; {self.name} Age; {self.age} Titel; {self.titel} Selary; {self.selary}")
        
        
p1 = show("Mahadi",18,"CEO",10000)
p1.s_show()
p1.w_show()
p1.p_show()          