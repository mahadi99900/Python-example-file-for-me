class Person:
    def __init__(self,):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value
p = Person()
p["name"]  = "mahadi"
p["age"]  = 18
print(p.data)   