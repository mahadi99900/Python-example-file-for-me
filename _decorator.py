def say_hello(func):
    def name():
        print("start")
        func()
        print("done")
    return name
@say_hello
def hello():
    print("hello") 
    
hello()          