import time
import threading


def test():
    while True:
        print("test")
        time.sleep(1)


threading.Timer(4, test).start()

while True:
    print('111')
    time.sleep(2)