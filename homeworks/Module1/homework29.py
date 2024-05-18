def is_odd(x):
    return x % 2
my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
def pow_2(x):
    return x*x


result = map(pow_2, filter(is_odd, my_list))
print(list(result))
