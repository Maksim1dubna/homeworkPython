from nim_engine import *

put_stone()
while True:
    print('Текущая позиция:')
    print(get_bunches())
    pos = input('Откуда берем?: ')
    qua = input('Сколько берем?: ')
    take_from_bunch(position=pos, quantity=qua)
    if is_gameover():
        break