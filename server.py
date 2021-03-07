from flask import Flask, url_for, request
from io import BytesIO
from PIL import Image


app = Flask(__name__)
port = 8080
host = "127.0.0.1"


@app.route("/")
def slash():
    return '</br>'.join(["<h1>Миссия Колонизация Марса</h1>",
                         f'<a href="/slogan">Девиз</a>',
                         f'<a href="/promotion">Рекламная кампания</a>',
                         f'<a href="/image_mars">Изображение Марса</a>',
                         f'<a href="/promotion_image">Реклама с картинкой</a>',
                         f'<a href="/astronaut_selection">Отбор астронавтов</a>'])


@app.route("/slogan")
def slogan():
    return "И на Марсе будут яблони цвести!"


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


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == "GET":
        return f'''<!doctype html>
                    <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
                    </head>
                    <body>
                    <h1 align="center">Анкета претендента</h1>
                    <h2 align="center">на участие в миссии</h2>
                    <div class="form">
                        <form class="login_form" method="post" enctype="multipart/form-data">
                            <input type="text" placeholder="Введите фамилию" name="surname"><br>
                            <input type="text" placeholder="Введите имя" name="name"><br><br>
                            <input type="email" name="email" placeholder="Введите адрес почты"><br>
                            <label for="education">Какое у вас образование?</label><br>
                            <select name="education">
                                <option>основное общее образование</option>
                                <option>среднее (полное) общее образование</option>
                                <option>среднее профессиональное образование</option>
                                <option>высшее образование — бакалавриат; специалитет</option>
                                <option>высшее образование — магистратура</option>
                            </select>
                            <div>
                                <label for="profession">Какая у вас основная профессия?</label><br>
                                <input type="checkbox" name="profession" value="research_engineer">
                                <label>инженер-исследователь</label><br>
                                <input type="checkbox" name="profession" value="pilot"><label>пилот</label><br>
                                <input type="checkbox" name="profession" value="builder"><label>строитель</label><br>
                                <input type="checkbox" name="profession" value="doctor"><label>врач</label><br>
                                <input type="checkbox" name="profession" value="terraforming_engineer">
                                <label>инженер по терраформированию</label><br>
                                <input type="checkbox" name="profession" value="climatologist">
                                <label>климатолог</label><br>
                                <input type="checkbox" name="profession" value="astrogeologist">
                                <label>астрогеолог</label><br>
                                <input type="checkbox" name="profession" value="drone_pilot">
                                <label>пилот дронов</label><br>
                            </div>
                            <label for="radio">Укажите пол</label><br>
                            <input type="radio" name="gender" value="male" checked> Мужской<br>
                            <input type="radio" name="gender" value="female"> Женский<br>
                            <label for="about">Почему вы хотите принять участие в миссии?</label><br>
                            <textarea name="about" rows="3"></textarea><br>
                            <div>
                                <label for="">Приложите фотографию</label><br>
                                <input type="file" name="file">
                            </div>
                            <div>
                                <input type="checkbox" name="ready" value="1">
                                <label for="ready" value="Готов">Готовы остаться на Марсе?</label><br>
                            </div>
                            <button type="submit">Отправить</button>
                        </form>
                    </div>
                    </body>
                    </html>'''
    elif request.method == "POST":
        print("Анкета нового претендента")
        print("Фамилия:", request.form.get("surname"))
        print("Имя:", request.form.get("name"))
        print("Образование:", request.form.get("education"))
        print("Профессия:", request.form.get("profession"))
        print("Пол:", request.form.get("gender"))
        print("Почему вы хотите принять участие в миссии?:\n", request.form.get("about"))
        print("Готовы остаться на Марсе?:\n", request.form.get("ready"))
        return "<h1 align='center'>Спасибо за прохождение анкеты</h1>" \
               "<h3 align='center'><a href='/'>Вернуться на главную страницу</a></h3>"


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <h2>Эта планета близка к земле;</h2>
                    <p class="p4"><br>У неё есть несколько спутников;</p>
                    <p class="p2"><br>На ней есть полезные ископаемые;</p>
                    <p class="p3"><br>Там есть высокие горы;</p>
                    <p class="p1"><br>И наконец она просто красива;</p>
                  </body>
                </html>'''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="ru">
                <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
                </head>
                <body>
                <h1>Результаты отбора</h1>
                <h2>Претендента на участие в миссии {nickname}:</h2>
                <p class="p3"><br>Поздравляем! Ваш рейтинг после {level} этапа отбора</p>
                составляет {rating}!
                <p class="p5"><br>Желаем удачи</p>
                </body>
                </html>'''


photo = ""


@app.route("/load_photo", methods=["POST", "GET"])
def load_photo():
    global photo
    if request.method == "GET":
        return f'''<!doctype html>
                    <html lang="ru">
                    <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" href="{url_for("static", filename="css/style.css")}">
                    </head>
                    <body>
                    <h1 align="center">Загрузка фотографии</h1>
                    <h2 align="center">для участия в миссии</h2>
                    <div class="form">
                        <form class="login_form" method="post" enctype="multipart/form-data">
                            <label for="">Приложите фотографию</label><br>
                            <input type="file" name="file"><br>
                            <img src="{photo}"><br>
                            <button type="submit">Отправить</button>
                        </form>
                    </div>
                    </body>
                    </html>'''
    elif request.method == "POST":
        with open("static/img/load_image.png", "wb") as i:
            i.write(request.files["file"].read())
        photo = "static/img/load_image.png"
        return "<h2 align='center'>Фотография успешно отправлена, <a href='/load_photo'>вернуться назад</a>.</h2>"


if __name__ == '__main__':
    app.run(port=port, host=host)
