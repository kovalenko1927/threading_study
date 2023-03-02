import time
import threading

value = 0
locker = threading.Lock()

def inc_value():
    global value
    while True:
        locker.acquire()
        value +=1
        time.sleep(1)
        print(value)
        locker.release()


for i in range(5):
    threading.Thread(target=inc_value).start()


