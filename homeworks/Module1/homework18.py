class Buiding():
    def __init__(self, numberOfFloor, buildingType):
        self.numberOfFloor = numberOfFloor
        self.buildingType = buildingType
    def __eq__(self, House):
        return (self.buildingType == House.buildingType) and (self.numberOfFloor == House.numberOfFloor)
House1 = Buiding(14, 'Хрущ')
House2 = Buiding(14, 'Хрущ')
print(House1 == House2)
