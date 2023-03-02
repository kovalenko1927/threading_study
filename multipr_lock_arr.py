import multiprocessing
import random

# lock = multiprocessing.Lock()
#
#
# def get_value(l):
#     l.acquire()
#     pr_name = multiprocessing.current_process().name
#     print(f"Process [{pr_name}] is running")
#     pass


# if __name__ == "__main__":
#     multiprocessing.Process(target=get_value, args=(lock,)).start()
#     multiprocessing.Process(target=get_value, args=(lock,)).start()
import time


def add_value(locker, array, index):
    with locker:
        num = random.randint(0,20)
        v_time = time.ctime()
        array[index] = num
        print(f"array[{index}] = {num}, sleep = {v_time}")
        time.sleep(num)



lock = multiprocessing.Lock()
arr = multiprocessing.Array("i", range(10))
process = []

if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=add_value, args=(lock, arr, i))
        process.append(pr)
        pr.start()

    for i in process:
        i.join()

    print(list(arr))