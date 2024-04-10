class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        return self.numberOfFloors
floors = House()
f = input('Введите этаж: ')
print('Этаж номер:',floors.setNewNumberOfFloors(floors=f))




