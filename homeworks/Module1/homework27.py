class Not10(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
class NotN(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message
def showStuff(stuff):
    if type(stuff) == tuple:
        if 'N' in stuff:
            raise NotN("Запрещаю N!")
    else:
        if stuff==10:
            raise Not10("Не понял?! Ты зачем переменную == 10 сделал?")
    return stuff
try:
    a = 10
    print(showStuff(a), type(a))
except Not10:
    print("Это ты сделал зря c цифрой 10....")
except NotN:
    print("N буква запрещена")
else:
    print("Ну ладно... печатаем")
finally:
    print("Остановка")