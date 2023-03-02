import random
import time
import multiprocessing


def test(q):
    val = random.randint(0,10)
    q.put(str(val))


queue = multiprocessing.Queue()
pr_list = []

if __name__ == "__main__":
    for i in range(10):
        pr = multiprocessing.Process(target=test, args=(queue,))
        pr_list.append(pr)
        pr.start()
        print(queue.get())
        pr.join()

    for i in pr_list:
        i.join()

    for elem in iter(queue.get, None):
        print(elem)
