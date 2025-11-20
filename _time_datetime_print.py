import time
from datetime import datetime

while True:
    a = datetime.now()
    b = a.strftime("%f")
    t = time.localtime()
    print(time.strftime(f"%A %B Day:%d time: %I:%M:%S.{b} %p", t), end='\r')