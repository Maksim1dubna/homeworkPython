def get_math_func(n):
    if n==1:
        def plus_minus(x):
            return x - 1
    elif n==2:
        def plus_minus(x):
            return x + 1
    else:
        raise Exception("Не та цифра")
    return plus_minus

def pow2_func(n):
    return n**2

class multiply_func:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return n * self.value


list_test = [1, 8, 11]
result = map(get_math_func(n=2), list_test)
print(list(result))
pow2 = lambda x: x**2
print(pow2(2))
print(pow2_func(6))


multiply_op = multiply_func(20)
print(multiply_op(3))

