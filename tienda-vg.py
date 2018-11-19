from flask import Flask, jsonify
import sys, os.path
sys.path.append("src/")
import videojuegos

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/status')
def status():
    return jsonify(status="Ok")

@app.route('/')
def index():
    return jsonify({
        "Busqueda de videojuego por ID":{
            "ruta" : "/obtenervg/<id>",
            "salida" : "Videojuego cuyo ID sea igual al id de la url"
        },
        "Obtencion de todos los videojuegos guardados":{
            "ruta" : "/videojuegos",
            "salida" : "Vector con todos los nombres de los videojuegos almacenados"
        },
        "Adicion de videojuego":{
            "ruta" : "/addvg/<videojuego>",
            "salida" : "Devuelve true si se ha aniadido el juego indicado en la url, false en caso contrario"
        },
        "Busqueda de ID de videojuego":{
            "ruta" : "/findvg/<nombre videojuego>",
            "salida" : "Devuelve el ID del videojuego asociado al nombre indicado en la url, devuelve -1 si no encuentra nada"
        },
        "Borrado de videojuego":{
            "ruta" : "/deletevg/<idvg>",
            "salida" : "Devuelve true si el borrado del juego indicado en la url ha sido correcto, false en caso contrario"
        }
    })

@app.route('/obtenervg/<idvg>')
def obtenervg(idvg):
    vg = videojuegos.Videojuegos()
    idvg = int(idvg)
    return jsonify(Videojuego=vg.getVideojuego(idvg))

@app.route('/videojuegos')
def vgs():
    vg = videojuegos.Videojuegos()
    return jsonify(Videojuegos=vg.getVideojuegos())

@app.route('/addvg/<nombrevg>')
def addvg(nombrevg):
    vg = videojuegos.Videojuegos()
    return jsonify(Return=vg.aniadeVideojuego(nombrevg))

@app.route('/findvg/<nombrevg>')
def findvg(nombrevg):
    vg = videojuegos.Videojuegos()
    print(type(vg))
    return jsonify(Encontrado=vg.encuentraVideojuego(nombrevg))

@app.route('/deletevg/<nombrevg>')
def deletevg(nombrevg):
    vg = videojuegos.Videojuegos()
    return jsonify(Return=vg.borraVideojuego(nombrevg))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
