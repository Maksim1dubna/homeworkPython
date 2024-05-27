import time
from threading import Thread
class Knight(Thread):
    def __init__(self, name, skill):
        super(Knight, self).__init__()
        self.name = name
        self.skill = skill
    def run(self):
        day = 0
        warriors = 100
        print(f"{self.name}, на нас напали!")
        while warriors > 0:
            warriors -= self.skill
            if warriors < 0:
                warriors = 0
            day += 1
            print(f"\033[37m{self.name} сражается {day} день(дня)..., осталось {warriors} воинов\n")
            time.sleep(0.5)
        print(f"\033[33m{self.name} одержал победу спустя {day} дней!")

knight1 = Knight("Sir Korneplod", 10)
knight2 = Knight("Artas", 9)
knight1.start()
knight2.start()
knight1.join()
knight2.join()

print("\033[31mВсе битвы закончились!")