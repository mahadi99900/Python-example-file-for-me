try:
    a = int(input("input your first number: "))
except:
    print("please enter your valid number ")
    exit()

try:
    b = input("Choose your favorite mathematical symbol ( +, -, ×, ÷, %) : ")
except:
    print("invalid symbol")
    exit()

try:
    c = int(input("input your second number: "))
except:
    print("please enter your valid number")
    exit()


if b == "-":
    if a > c:
        r = a - c
    else:
        r = c - a

elif b == "+":
    r = a + c

elif b == "*":
    r = a * c

elif b == "/":
    if c == 0:
        r = "Zero দিয়ে ভাগ করা যায় না!"
    else:
        r = a / c

elif b == "%":
    r = a % c

else:
    r = "Invalid symbol"



for x in range(20):
    print(f"result: {r}") 
    