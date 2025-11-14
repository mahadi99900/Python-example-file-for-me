def file():
    b = open("file.txt","r")
    c = b.read()
    b.close()
    return c 
while True:
    choose = input("1 add your contract\n"
    "2 list your contract; ")
    if choose == "1":
        name = input("enter your contract name; ")
        number = input("enter your contract nambur; ")
        with open("file.txt","a") as a:
            a.write(f"{name} - {number}\n")
        print("saved")
    elif choose == "2":
        s = file()
        print(f"your contact list is \n{s}")
    else:
        continue