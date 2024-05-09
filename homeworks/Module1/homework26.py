def string_to_int(s): # добавить обработку ValueError
    try:
        return int(s)
    except ValueError:
        return f"ValueError {s}"
def read_file(filename): # добавить обработку FileNotFoundError, IOError
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"FileNotFoundError {filename}"
    except IOError:
        return f"IOError {filename}"
def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    try:
        a / b
    except a==0:
        return "ZeroDivisionError"
    except TypeError:
        return "TypeError"
def access_list_element(lst, index): # добавить обработку IndexError, TypeError
    try:
        return lst[index]
    except IndexError:
        return "IndexError"
    except TypeError:
        return "TypeError"

print(string_to_int("a"))
print(read_file("file.txt"))
print(divide_numbers(0,1))
print(access_list_element(1,0))