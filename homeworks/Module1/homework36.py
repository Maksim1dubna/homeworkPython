import threading
import time
from threading import Thread
from threading import Lock
global warriors
warriors = 100
class Knight(Thread):
    def __init__(self, name, skill, lock):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill
        self.Knight_lock = lock
    def run(self):
        global warriors
        print(f"{self.name}, на нас напали!")
        while warriors >= 0:
            self.Knight_lock.acquire()
            warriors -= self.skill
            self.Knight_lock.release()
            if warriors <= 0:
                warriors = 0
            print(f"\033[37m{self.name} отбивается, осталось {warriors} врагов!\n")
            if warriors == 0:
                print(f"\033[33mВрагов нет!")
                break
            time.sleep(0.5)
        print(f"\033[33m{self.name} одержал победу!")
class Enemy(Thread):
    def __init__(self, name, skill, lock):
        super(Enemy, self).__init__()
        self.name = name
        self.skill = skill
        self.Enemy_lock = lock
    def run(self):
        global warriors
        print(f"{self.name}, напал на нас!")
        while warriors > 0:
            self.Enemy_lock.acquire()
            print(f"\033[37m{self.name} нападает")
            warriors += self.skill
            self.Enemy_lock.release()
            print(f"\033[37m Враг получает подкрепление! У противника осталось {warriors} воинов\n")
            if warriors < 0:
                warriors = 0
                print(f"\033[33mПротивник {self.name} проиграл")
                break
            if warriors >= 200:
                print(f"\033[33mПротивник {self.name} победил")
                break
            time.sleep(0.5)
lock = threading.Lock()
knight1 = Knight("Arthas", 20, lock = lock)
Enemy1 = Enemy("Volandemort", 10, lock = lock)

Enemy1.start()
knight1.start()
Enemy1.join()
knight1.join()

print("\033[31mВсе битвы закончились!")