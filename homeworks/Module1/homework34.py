import time
from threading import Thread

def print_numbers():
    for i in range(10):
        print(i+1)
        time.sleep(0.5)
def print_letters():
    for i in range(ord('a'),ord('j')+1):
        print(chr(i))
        time.sleep(0.5)
thread1 = Thread(target=print_numbers)
thread2 = Thread(target=print_letters)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
