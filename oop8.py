class info:
    def __init__(m,name,age,password):
        m.name = name
        m.age = age
        m.__password = password
    def name_show(m):
        return m.name
    def age_show(m):
        return m.age
    def pass_show(m):
        return m.__password    
a = info("mahadi",18,";'6#:৳6'#*")
print(a.name_show())
print(a.age_show()) 
print(a.pass_show())               