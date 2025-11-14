anwar = input("tumi ki game khelte chau? [yes/no]")

if anwar == "yes":
    print("welcome is our game")
    answer = input("tumi ki jongle e jete chau? [yes/no]")
    if answer == "yes":
        print("tumi sekhane bager sathe lorai korbe naki horin dorbe?")
        answar = input("[bag/horin]")
        if answar == "horin":
            print("tumi horin dore felecho! you are win!!")
        else:
            print("bag tomak kheye feleche")    
    else:
        print("tahole game over ")
            
else:
    print("game is over")