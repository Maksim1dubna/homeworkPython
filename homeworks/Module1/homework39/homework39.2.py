import requests
# Requests — это модуль для языка Python,
# который используют для упрощения работы с HTTP-запросами.
# Он удобнее и проще встроенного Urllib

#Задача. Прочитать код с сайта
response = requests.get('https://stackoverflow.com/questions/18810777/how-do-i-read-a-response-from-python-requests')
print(response.text)