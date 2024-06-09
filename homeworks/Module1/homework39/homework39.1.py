from flask import Flask
# Flask — это легковесный веб-фреймворк для языка Python,
# который предоставляет минимальный набор инструментов для создания веб-приложений.
# На нём можно сделать и лендинг, и многостраничный сайт с кучей плагинов и сервисов.
#
#
# Задача. Вывести Hello world, но на сайте.
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()