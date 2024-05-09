class Not10(Exception):
    def __init__(self, message):
        self.message = message
class NotN(Exception):
    def __init__(self, message):
        self.message = message
def divide_numbers(a, b): # добавить обработку ZeroDivisionError, TypeError
    if b==10:
        raise Not10("Не понял?! Ты зачем на 10 делишь?")
    return a / b
def showList(my_list):
    item = 'N'
    if item in my_list:
        raise NotN("Запрещаю N!")
    return my_list
try:
    print(divide_numbers(1, 10))
except Not10:
    print("Это ты сделал зря....")
    raise
else:
    print("Ну ладно... сойдет")
finally:
    print("Завершено")

a = 1, 2, 'N'
try:
    print(showList(a))
except NotN:
    print("N буква запрещена")
    raise
else:
    print("Ну ладно... печатаем")
finally:
    print("Остановка")