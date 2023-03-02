import threading
import time
from threading import Thread, BoundedSemaphore, current_thread

max_connections = 5
pool = threading.BoundedSemaphore(value=max_connections)


def test():
    with pool:
        print(current_thread().name)
        time.sleep(6)


for i in range(10):
    Thread(target=test, name=f"thr-{i}").start()
