from tinydb import TinyDB

db = TinyDB('DbCine.json')

db.insert_multiple([
    {'titulo': 'El Padrino', 'genero': 'Drama', 'fecha_estreno': '1972-03-24', 'idioma': 'Inglés'},
    {'titulo': 'Interestelar', 'genero': 'Ciencia ficción', 'fecha_estreno': '2014-11-07', 'idioma': 'Inglés'},
    {'titulo': 'Titanic', 'genero': 'Romance', 'fecha_estreno': '1997-12-19', 'idioma': 'Inglés'},
    {'titulo': 'La La Land', 'genero': 'Musical', 'fecha_estreno': '2016-12-25', 'idioma': 'Inglés'},
    {'titulo': 'El Señor de los Anillos: La Comunidad del Anillo', 'genero': 'Fantasía', 'fecha_estreno': '2001-12-19', 'idioma': 'Inglés'},
    {'titulo': 'Harry Potter y la piedra filosofal', 'genero': 'Fantasía', 'fecha_estreno': '2001-11-16', 'idioma': 'Inglés'},
    {'titulo': 'El Rey León', 'genero': 'Animación', 'fecha_estreno': '1994-06-15', 'idioma': 'Inglés'},
    {'titulo': 'Matrix', 'genero': 'Acción', 'fecha_estreno': '1999-03-31', 'idioma': 'Inglés'},
    {'titulo': 'Forrest Gump', 'genero': 'Drama', 'fecha_estreno': '1994-06-23', 'idioma': 'Inglés'},
    {'titulo': 'Gladiador', 'genero': 'Acción', 'fecha_estreno': '2000-05-05', 'idioma': 'Inglés'}
])

print(db.all())
