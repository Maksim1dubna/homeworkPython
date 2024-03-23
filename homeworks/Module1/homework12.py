def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['advert',False,7]
values_dict ={'a':'no', 'b':True, 'c':11}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [8,'yeah']
print_params(*values_list_2, 42)






