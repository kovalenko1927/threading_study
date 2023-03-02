import time
import multiprocessing


def test():
    for _ in range(3):
        print(f"{multiprocessing.current_process().name} - {time.ctime()}")
        time.sleep(1)


pr = multiprocessing.Process(target=test, name="prc-1")

if __name__ == "__main__":
    pr.start()
    time.sleep(3)
    pr.terminate()
    print(pr.is_alive())
    print(pr.pid)
    print(multiprocessing.current_process())
    pr.join()
    print("ALL PROCESS IS STOPPING")

