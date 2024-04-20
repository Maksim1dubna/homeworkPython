class Car:
    price = 1000000
    def horse_powers(self, pw):
        return pw

class Nissan(Car):
    price = 1000
    def horse_powers(self, pw = 200):
        return pw
class Kia(Car):
    price = 2000
    def horse_powers(self, pw = 300):
        return pw
car1 = Nissan()
car2 = Kia()
print(car1.price, car1.horse_powers())
print(car2.price, car2.horse_powers())