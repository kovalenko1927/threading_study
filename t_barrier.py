import time
import random
import threading
from threading import current_thread, Barrier


def test(barrier):
    slp = random.randint(10,15)
    print(f"[{current_thread().name}] run in ({time.ctime()})")
    time.sleep(slp)

    barrier.wait()
    print(f"[{current_thread().name}] -> ({time.ctime()})")


bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()
