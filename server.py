from flask import Flask, url_for


app = Flask(__name__)
port = 8080
host = "127.0.0.1"


@app.route("/")
def slash():
    return '</br>'.join(["<h1>Миссия Колонизация Марса</h1>",
                         f'<a href="/promotion">Рекламная кампания</a>',
                         f'<a href="/slogan">Девиз</a>',
                         f'<a href="/image_mars">Изображение Марса</a>',
                         f'<a href="/promotion_image">Реклама с картинкой</a>'])


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
                         f'''<img src="{url_for('static', filename='img/image_mars.jpg')}">''',
                         "Жди нас, Марс!"])


@app.route("/slogan")
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                <html lang="ru">
                <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
                </head>
                <body>
                    <h1>Жди нас, марс!</h1>
                    <img src="{url_for('static', filename='img/image_mars.jpg')}">
                    <p class="p1"><br>Человечество вырастает из детства.</p>
                    <p class="p2"><br>Человечеству мала одна планета.</p>
                    <p class="p3"><br>Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class="p4"><br>И начнем с Марса!</p>
                    <p class="p5"><br>Присоединяйся!</p>
                </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=port, host=host)
