import random 

while True:
    a = input("do you want to play  this game[y/n]")
    if a == "":
        print(random.randint(1,100))
        continue
    else:
        print("game is over")
        break    
        
