class Vehicle:
    vehicle_type = "none"
class Car:
    price = 1000000
    def horse_powers(self, pw):
        return pw
class Nissan(Car, Vehicle):
    price = 1000
    vehicle_type = 'Маслкар'
    def horse_powers(self, pw = 200):
        return pw
car1 = Nissan();
print(car1.vehicle_type, car1.price)