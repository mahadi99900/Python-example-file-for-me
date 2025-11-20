import random as r
import time as t
i = 1
while True:
    rn1 = r.randint(1,50)
    rn2 = r.randint(51,501)
    num = list(range(rn1,rn2))
    print(f"list{i}: {num}",end="\r")
    i += 1
    t.sleep(1)