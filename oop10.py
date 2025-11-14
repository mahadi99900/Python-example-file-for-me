class person:
    def __init__(self,name,selary):
        self.name = name
        self.selary = selary
    def details(self):
        print(f"Worker name; {self.name}") 
        print(f"Worker selary; {self.selary}")
        print("\n")
first = person("mahadi",1000)
second = person("hasan",2000)
third = person("siyam",3000)

first.details() 
second.details()
third.details()

class my:
    def details(self,name,age):
        print(f"\nmy name is {name} and my age is {age}")
a = my()
a.details("mahadi",18)        