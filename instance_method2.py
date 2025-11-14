class car:
    def __init__(self,name,model,value,for_sell):
        self.name = name
        self.model = model
        self.value = value
        self.for_sell = for_sell
    def show(self):
        print(f" Model name is {self.name}\n and model is {self.model}\n and this value is {self.value}\n and this for sell? {self.for_sell}")   
class vehicle(car):
    pass # or None
car1 = vehicle("yamaha","hh54","10M",True)
car2 = vehicle("hoonda","shx5","2M",False) 
car3 = vehicle("hero","cys6","30M",True)
car4 = vehicle("R15","cjs6","3M",True)   

car1.show()
car2.show()
car3.show()
car4.show()