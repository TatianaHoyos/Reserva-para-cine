from flask import render_template, request
from app import app
from app.domain.entities.movie import Movie


@app.route('/')
def movie_list():
    # Simulación de consulta a la base de datos para obtener lista de películas
    movies = [
        {"id": 1, "title": "Película 1", "synopsis": "Sinopsis de la película 1", "duration": "120 min", "poster": "https://via.placeholder.com/300x400", "release_date": "2024-06-10"},
        {"id": 2, "title": "Película 2", "synopsis": "Sinopsis de la película 2", "duration": "140 min", "poster": "https://via.placeholder.com/300x400", "release_date": "2024-06-15"},
        {"id": 3, "title": "Película 3", "synopsis": "Sinopsis de la película 3", "duration": "130 min", "poster": "https://via.placeholder.com/300x400", "release_date": "2024-06-20"}
    ]
    return render_template('index.html', movies=movies)

@app.route('/reserva')
def reserva():
    movie_id = request.args.get('movie')
    return render_template('reserva.html', movie_id=movie_id)
