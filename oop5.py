class info:
    def person(name,age):
        name = name
        age = age
        print(name,age)
        
user = info.person("mahadi",17)


class info1:
    def person1(name,age):
        name = name
        age = age
        return name,age
user1 = info1.person1("hasan",18)
print(user1)       
print(type(user))
print(type(user1))

class math:
    def some(a,b):
        a = a
        b = b
        return a + b
user2 = math.some(10,20)
print(user2)       
 
class math1:
    def __init__(my,x,y): # init মান return করতে পারে না 
        my.x = x
        my.y = y
    def show(my):
        return my.x + my.y    
mm = math1(10,10) 
print(mm.show())

class math2:
    def __init__(self,p,q):
        self.p = p
        self.q = q
        s = p + q
        print(s)
math2(100,20)               