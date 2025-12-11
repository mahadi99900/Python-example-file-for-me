import time
import threading

lock = threading.Lock()

dict = {
  "a":1,
  "b":2,
  "c":3,
  "d":4,
  "e":5
}
def myd():
    for i,j in dict.items():
        with lock:
            time.sleep(1)
            print(i,j)
def myh():
    for h in range(5):
        with lock:
            time.sleep(1)
            print('h')
        
t1 = threading.Thread(target=myd)
t2 = threading.Thread(target=myh)

t1.start()
t2.start()

    