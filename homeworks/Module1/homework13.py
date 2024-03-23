def test(a = 1, b = True, c = 'zero'):
    print(a, b, c)

def recurse(n):
    if n == 1:
        return 1
    answer = n * recurse(n-1)
    return answer

test()
print(recurse(5))