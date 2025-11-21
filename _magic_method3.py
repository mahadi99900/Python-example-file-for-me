class Person:
    def __init__(self,):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value
    def __getitem__(self,key,):
        return self.data[key]
    def __delitem__(self,key):
        del self.data[key]
           
p = Person()
p["name"]  = "mahadi"
p["age"]  = 18

del p["age"]

print(p.data)
   