class great():
    def hello(self,a):
        self.a = a
        return a
class english(great):
    pass
    
class bb(english):
    pass   
         
g = great()
print(g.hello(10))      