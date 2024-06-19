# Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.-
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).
import inspect
import pprint
import sys
class turn_onOff:
    human = "Человек"
    def __init__(self):
        self.sw = {"Включено":1, "Выключено":0}
    def switch(self):
        print(self.sw["Включено"])
def ntrospection_info(obj):
    pprint.pprint(f"Type:{type(obj)}, methods and attributes:{[method for method in dir(obj) if method.startswith('__') is False]}, module:{inspect.getmodule(obj)}")

obj1 = turn_onOff
ntrospection_info(obj1)