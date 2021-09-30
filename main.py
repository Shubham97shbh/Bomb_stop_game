BLAST = '< iframe src = "https://giphy.com/embed/oe33xf3B50fsc" width = "480" height = "480" frameBorder = "0" class ="giphy-embed" allowFullScreen ></iframe >'
CHANCE_1 = '<iframe src = "https://giphy.com/embed/xUNd9YJwF6ifDUnqNi" width = "480" height = "270" frameBorder = "0" class ="giphy-embed" allowFullScreen ></iframe >'
CHANCE_2 = '<iframe src="https://giphy.com/embed/xUOxeXt41UOYRusw4E" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'
Win = '<iframe src="https://giphy.com/embed/Snqaxrj6zDUE3OI5FB" style="text-align:center width="480" height="270"></iframe>'
Home = '<h1 style=color:"blue;font-size:17">You have to go to the home page::<b>https://127.0.0.1:5000/</b></h1>'
from flask import Flask
import random

app = Flask(__name__)

with open("Display.html", "r") as file:
    html_front_view = file.read()
with open('result_display.html', 'r') as file:
    html_back_view = file.read()


class input_:
    def __init__(self):
        self.password = 0
        self.count = 0
        self.value = 0
        self.html = ''


user = input_()


@app.route('/')
def display():
    user.count = 0
    user.password = random.randint(0, 10)
    return html_front_view


def check(function):
    def call(*args, **kwargs):
        bomb_number = args[0].password
        user_guess = (args[0].value)
        if args[0].count < 3:
            if user_guess < bomb_number:
                args[0].count = args[0].count + 1
                function(
                    html_back_view + f'<h1 style="color:red;font-size:20;">Wrong number: {user_guess}</h1><h2>Chance left {3 - args[0].count}</h2>' + CHANCE_1 + '<p>Hint: Guessed number is SMALLER than actual number</p>')
            elif user_guess > bomb_number:
                args[0].count = args[0].count + 1
                function(
                    html_back_view + f'<h1 style="color:red;font-size:20;">Wrong number: {user_guess}</h1><h2>Chance left {3 - args[0].count}</h2>' + CHANCE_2 + '<h3>Hint: Guessed number is LARGER than actual number</h3>')
            else:
                function(
                    html_back_view + f'<h1 style="color:red;font-size:20;">Correct number: {user_guess}</h1><h1>You have saved your city by {3 - args[0].count} chances left.</h1>' + Win+Home)
        else:
            function(
                '<h1 style="text-align:center;color:red;font-size:20;">Sorry Your city has been destroyed</h1>' + BLAST+Home)

    return call


@check
def user_check_answer(text):
    user.html = text
    return text


@app.route('/<int:value>')
def user_input(value):
    user.value = int(value)
    user_check_answer(user)
    return user.html

if __name__ == "__main__":
    app.run(debug=True)
