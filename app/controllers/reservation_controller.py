from flask import render_template
from app import app
from app.domain.entities.movie import Movie

@app.route('/')
def movie_list():
    # Simulación de consulta a la base de datos para obtener lista de películas
    movies = [Movie("Movie 1"), Movie("Movie 2"), Movie("Movie 3")]
    return render_template('index.html', movies=movies)
