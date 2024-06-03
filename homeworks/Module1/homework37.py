import time
from threading import Thread
import queue
global i
i = 0
class Table():
    def __init__(self, number):
        super(Table, self).__init__()
        self.number = number
        is_busy = 0
        self.is_busy = is_busy
        customer = 0
        self.customer = customer

class Cafe():
    def __init__(self, q):
        super(Cafe, self).__init__()
        self.q = queue.Queue()
    def customer_arrival(self):
        count_is_busy = 0
        global i
        cs = 1
        while cs < 20:
            value = cs
            if i >= len(tables):
                i = 0
            if self.q.not_empty == True:
                value = self.q.get(block=True)
            print(f"\nПосетитель номер {cs} прибыл")
            Cafe.serve_customer(self, customer = value)
            cs += 1
            for elem in range(len(tables)):
                if tables[elem].is_busy == 1:
                    count_is_busy += 1
                    if count_is_busy == len(tables):
                        self.q.put(cs)
                        print(f"\nПосетитель номер {cs} ожидает свободный стол. (помещение в очередь)")
                        print(list(self.q.queue))
                        count_is_busy = 0
            i += 1
        print(f"\n КЛИЕНТОВ БОЛЬШЕ НЕТ!")
        for elem in range(len(tables)):
            print(tables[elem].number, tables[elem].customer, tables[elem].is_busy)

    def serve_customer(self, customer = 0):
        global i
        if tables[i].is_busy == 0:
            tables[i].is_busy = 1
            tables[i].customer = customer
            print(f"Посетитель номер {tables[i].customer} сел за стол {tables[i].number}. (начало обслуживания)")
            time.sleep(5)
            print(f"Посетитель номер {tables[i].customer} покушал и ушёл. (конец обслуживания)")
            tables[i].is_busy = 0
            tables[i].customer = 0
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