import threading
import time

def main():
    thread_fun()
    print("Execute after thread function")

def thread_fun():
    threads = []
    for i in range(0,10):
        t = threading.Thread(target=each_thread, args=(i,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()


def each_thread(idx):
    time.sleep(5)
    print(f'Thread: {idx}')

# Calling main function
main()