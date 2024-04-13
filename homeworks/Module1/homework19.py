class Building:
    total = 0
    def __init__(self):
        Building.total += 1

Building_massive = []
while len(Building_massive) < 40:
    new_build = Building()
    Building_massive.append(new_build)
for x in Building_massive:
    print(x)
print(len(Building_massive))
