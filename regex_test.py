import re 

txt = "Hello, How Are You?"
a = re.findall("^Hello",txt)

if a:
    print("yes")
else:
    print("no")    
 