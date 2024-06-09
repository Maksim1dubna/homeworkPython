import time
from threading import Thread
import queue
class Table():
    def __init__(self, number):
        super(Table, self).__init__()
        self.number = number
        self.is_busy = 0
        self.customer = 0

class Cafe():
    def __init__(self, q):
        super(Cafe, self).__init__()
        self.q = queue.Queue(5)
    def customer_arrival(self):
        i = 0
        while True:
            if self.q.full() == True:
                print("\033[31mБОЛЬШЕ КЛИЕНТОВ НЕ БУДЕТ!")
                i = 0
                break
            i+= 1
            print(f"\033[37mПосетитель номер {i} прибыл.")
            self.q.put(i)
            print(f"\033[37mПосетитель номер {i} ожидает свободный стол. (помещение в очередь)")
            time.sleep(1)
    def serve_customer(self, customer = 0):
        while True:
            if self.q.empty() != True:
                for i in range(len(tables)):
                    if tables[i].is_busy == 0:

                        tables[i].customer = self.q.get()
                        print(f"\033[33mПосетитель номер {tables[i].customer} сел за стол {tables[i].number}. (начало обслуживания)")
                        if self.q.empty() == True:
                            break
                        tables[i].is_busy = 1

            time.sleep(5)
            for i in range(len(tables)):
                if tables[i].is_busy == 1:
                    print(f"\033[33mПосетитель номер {tables[i].customer} покушал и ушёл. (конец обслуживания)")
                    tables[i].is_busy = 0
                    tables[i].customer = 0
            print(list(self.q.queue))
            if self.q.empty() == True:
                return

table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(Table)
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_serve_thread = Thread(target=cafe.serve_customer)
customer_arrival_thread.start()
customer_serve_thread.start()
customer_arrival_thread.join()
customer_serve_thread.join()