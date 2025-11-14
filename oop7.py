class info:
    def __init__(self,name,age,password):
        self.name = name
        self.age = age
        self.__password = password
    def show_info(self):
        print(f"your name is {self.name} your age is {self.age}")
    def show_hide(self):
        print(f"your password is {self.__password}")  
        
p1 = info("mahadi",18,"%6##*'ynx")
p1.show_info()
p1.show_hide()