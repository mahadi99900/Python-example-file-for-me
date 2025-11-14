import random 

b = random.randrange(1,50)
c = int(input("enter you like number; "))

if b < c:
    print("your number is high")
    print(f"random number is {b}")
elif b > c:
    print("your number is low")
    print(f"random number is {b}")
else:
    print("your number is correct")
    print(f"random number is {b}")    