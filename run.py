from flask import Flask, render_template
from tinydb import TinyDB

app = Flask(__name__,  template_folder='app/web/templates')

# Crear o cargar la base de datos
db = TinyDB('DbCine.json')

@app.route('/')
def index():
    # Obtener todos los datos de la base de datos
    peliculas = db.all()
    return render_template('index.html', peliculas=peliculas)

if __name__ == '__main__':
    app.run(debug=True)

print()