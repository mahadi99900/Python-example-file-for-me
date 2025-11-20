cont = {}
def showcont():
    for key,value in cont.items():
        print(f"Name is {key} Number is {value}")
while True:
    choice = input("1.add contract\n"
                   "2.search contract\n"
                   "3.display contract\n"
                   "4.edit contract\n"
                   "5.delete contract\n"
                   "6.exit\n"
                   "please enter your number (1-6); ")
    if choice == "1":
        name = input("enter your name; ")  
        number = input("enter your number; ") 
        cont[name] = number
        print(f"contract saver successfully Name;{name} Number; {number}")
    elif choice == "2":
        cont_search = input("search the contract; ")  
        if cont_search in cont:
            print(f"{cont_search} this number is {cont[cont_search]}") 
        else:
            print("contract is not founded")    
    elif choice == "3":
        if not cont:
            print("contract list is empty ")
        else:
            showcont()
    elif choice == "4":
        cont_edit = input("Edit your contract; ") 
        if cont_edit in cont:
            phone = input("Enter your number; ")
            cont[cont_edit] = phone
            print("contract is update successfully ") 
            showcont()
        else:
            print(f"{cont_edit} is not founded")
    elif choice == "5":
        showcont()
        del_cont = input("which contract do you want to delete: ")
        if del_cont in cont:
            del_confrm = input("Do you want this contract? y/n: ")
            if del_confrm == "y" or del_confrm == "Y":
                cont.pop(del_cont)
                showcont()
                print("contract delete successfully ")
            elif del_confrm == "N" or del_confrm == "n":
                print("this contract is not deleted ")
            else:
                print("please select y/n ")
                continue 
        else:
            print("contract is not founded")
    elif choice == "6":
        break
    else:
        continue