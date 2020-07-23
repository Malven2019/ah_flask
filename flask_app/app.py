from flask import Flask, render_template
import requests


def create_app():
    app = Flask(__name__)  # variable controlled by the scope of the project

    @app.route('/')
    def home():
        return "success the flask app is running"

    @app.route('/render')
    def window():

        return render_template('home.html')

    @app.route('/insert/<word>')
    def insert(word):
        return render_template('insert.html', word=word)

    @app.route('/dog')
    def dog():
        message = requests.get(
            'https://dog.ceo/api/breeds/image/random').json()
        return render_template('dog.html', picture=message['message'])

    return app
