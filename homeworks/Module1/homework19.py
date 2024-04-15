class Building:
    total = 0 #Создайте новый класс Buiding с атрибутом total
    def __init__(self):
        Building.total += 1 #Создайте инициализатор для класса Buiding,
        # который будет увеличивать атрибут количества созданных объектов класса Building total

Building_massive = []
while len(Building_massive) < 40: #В цикле создайте 40 объектов класса Building и выведите их на экран командой print
    new_build = Building()
    Building_massive.append(new_build)
for x in Building_massive:
    print(x)
print(Building.total)
