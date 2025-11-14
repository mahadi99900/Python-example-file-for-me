class a:
    ##error dibe "self" na dile
    def see():
        print("you can see")
    
class b:
    def hunt(self):
        print("you can hunt")
    
class c(a):
    pass
    
class d(b):
    pass
    
class e(a,b):
    pass 
    
C = c()
D = d()
E = e()

D.hunt()