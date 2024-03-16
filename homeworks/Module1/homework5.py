#список
my_list = ['apple', 'banana', 'orange', 'kiwi','mango']
print(my_list)
print(my_list[0],my_list[-1])
print(my_list[2:5])
my_list[2] = 'guava'
print(my_list)
#словарь
my_dict = {'Кот':'cat', 'Тигр':'tiger', 'Волк':'Wolf'}
print(my_dict)
print(my_dict['Тигр'])
my_dict.setdefault('Слон','elephant')
print(my_dict)