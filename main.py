import time
import threading


def get_data(data):
    while True:
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)



thr = threading.Thread(target=get_data, args=(str(time.time()),), name="thr-1")
thr.start()

# for i in range(50):
#     print(f"current - {i}")
#     time.sleep(1)
#
#     if i % 10 == 0:
#         print("Active thread: ",threading.active_count())
#         print("Enumerate: ", threading.enumerate())
#         print("thr-1 is alive: ", thr.is_alive() )

# print("name: ", threading.main_thread().name)
# threading.main_thread().setName("My_thread")
# print("name: ", threading.main_thread().name)