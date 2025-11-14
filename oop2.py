class animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eating(self):
        print(f"now {self.name} is eating") 
    def sleeping(self):
        print(f"now {self.name} is sleeping")
class Cat(animal):
    def speak(self):
        print("meu")
class Mous(animal):
    pass
class Dog(animal):
    pass
dog = Dog("mely")        
mous = Mous("herry")       
cat = Cat("citi")    

print(dog.name)
print(dog.is_alive)
dog.eating()
cat.speak()