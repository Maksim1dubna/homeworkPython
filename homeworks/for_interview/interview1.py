from random import randint
int_list = []


for i in range(0, 10):
    int_list.append(randint(-10, 10))

int_list = [float(i) for i in int_list if i > 0]
print(int_list)