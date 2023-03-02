import time
import threading


def get_data(data):
    for i in range(5):
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)

thr.start()
time.sleep(1)
print("finish")