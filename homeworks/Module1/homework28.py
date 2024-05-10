import warnings
def divide_numbers(a, b):
    warnings.simplefilter('ignore')
    try:
        if b <= 0.01:
            warnings.warn("Ты близок к 0....")
            warnings.simplefilter("always")
            warnings.warn("А теперь есть предупреждения...")
            warnings.simplefilter("error")
            warnings.warn("Но нет! Это ОШИБКА!")
        return a / b
    except ZeroDivisionError:
        print("Я тебя предупреждал...")
    except UserWarning as e:
        print(e)
print(divide_numbers(1,0.001))
