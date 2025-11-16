class me:
    def __init__(self,name):
        self.name = name
    def m_show(self):
        print(f'my name is {self.name}')
class my_f(me):
    def __init__(self,name):
        self.name = name
        super().__init__(name)
    def f_show(self):
        print(f'my friend name is {self.name}') 
class my_b(my_f):
    def __init__(self,name):
        super().__init__(name)
        self.name = name
    def b_show(self):
        print(f"my brother name is {self.name}")
p = my_b("mahadi")
p.m_show()
p.f_show()
p.b_show()           
                               