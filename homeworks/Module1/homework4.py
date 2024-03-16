immutable_var = (1, 'var', True)
print(immutable_var)
while True: #конструкция позволит выполнить программу дальше, даже если будет ошибка
    try:
        immutable_var[1] = 3
        # Сообщение TypeError: 'tuple' object does not support item assignment
        # означает, что тип кортеж не может быть изменен.
    except (TypeError):
        print('error')
        break
#---------------------------------------------------
mutable_list = [0, 'novar', False]
num = 0 #переменная для подбора номера в списке
while num<len(mutable_list): #Конструкция позволит изменить значения быстрее, чем вписывать вручную
    mutable_list[num]=num+1
    num=num+1
print(mutable_list)
