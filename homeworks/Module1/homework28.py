import warnings
def divide_numbers(a, b):
    try:
        a / b
        if b < 0.01:
            warnings.warn("Ты близок к 0....")
    except ZeroDivisionError:
        print("Я тебя предупреждал...")
    except UserWarning as e:
        print(e)


print(divide_numbers(1,0.001))