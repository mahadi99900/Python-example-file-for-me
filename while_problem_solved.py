
def mahadi():
    a = int(input("enter a number; "))
    b = int(input("enter a number; "))
    c = input("enter a symbol; ")
    if c == "-":
        r = a - b
    
    elif c == "+":
        r = a + b 
        
    elif c == "*":
        r = a * b
        
    elif c == "/":
        r = a / b
        
    else:
        print("wrong symbol")
        
    print(r)    
    
    return r
    
g = mahadi()   
 
x = 1    
while x < g:
    print(x)
    x = x + 1
    