from flask import Flask, url_for


app = Flask(__name__)
port = 8080
host = "127.0.0.1"


@app.route("/")
def slash():
    return '</br>'.join(["Миссия Колонизация Марса",
                         f'<a href="/promotion">Рекламная кампания</a>',
                         f'<a href="/slogan">Девиз</a>',
                         f'<a href="/image_mars">Изображение Марса</a>'])


@app.route("/promotion")
def promotion():
    return '</br>'.join(["Человечество вырастает из детства.",
                         "Человечеству мала одна планета.",
                         "Мы сделаем обитаемыми безжизненные пока планеты.",
                         "И начнем с Марса!",
                         "Присоединяйся!"])


@app.route("/image_mars")
def image_mars():
    return '</br>'.join(["<h1>Жди нас, Марс!</h1>",
                         f'''<img src="{url_for('static', filename='img/image_mars.jpg')}"''',
                         "Жди нас, Марс!"])


@app.route("/slogan")
def slogan():
    return "И на Марсе будут яблони цвести!"


if __name__ == '__main__':
    app.run(port=port, host=host)
