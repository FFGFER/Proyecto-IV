from flask import Flask, render_template, session, redirect, url_for, escape, request, jsonify
from jinja2 import Markup
import videojuegos

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return jsonify(status="Ok")

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/videojuegos')
def videojuegos():
    vg = videojuegos.Videojuegos()
    juegos = vg.getVideojuegos()
    jsonvg = jsonify(juegos)
    return render_template('videojuegos.html',vgs=juegos,json=jsonvg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
