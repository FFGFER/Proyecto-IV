from flask import Flask, jsonify
import videojuegos

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return jsonify(status="Ok")

@app.route('/videojuegos')
def vgs():
    vg = videojuegos.Videojuegos()
    return jsonify(vg.getVideojuegos())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
