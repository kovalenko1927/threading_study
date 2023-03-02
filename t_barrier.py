import time
import random
import threading
from threading import current_thread, Barrier


def test(barrier):
    slp = random.randint(10,15)
    print(f"Поток - [{current_thread().name}] запущен в ({time.ctime()})")
    time.sleep(slp)

    barrier.wait()
    print(f"Поток - [{current_thread().name}] преодолел барьер в ({time.ctime()})")


bar = threading.Barrier(5)
for i in range(5):
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()