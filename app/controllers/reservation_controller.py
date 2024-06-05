from flask import render_template, request
from app import app
from app.domain.entities.movie import Movie

from app.adapters.database.movie_repository import MovieRepository
from app.use_cases.list_movies import ListMoviesUseCase

@app.route('/')
def movie_list():
    movie_repository = MovieRepository() #creo la instancia (liquido)
    list_movies_use_case = ListMoviesUseCase(movie_repository)
    movies = list_movies_use_case.listar()
    return render_template('index.html', movies=movies)

@app.route('/reserva')
def reserva():
    movie_id = request.args.get('movie')
    return render_template('reserva.html', movie_id=movie_id)


@app.route('/crear')
def crear():
    movie_repository = MovieRepository()
    list_movies_use_case = ListMoviesUseCase(movie_repository)
    list_movies_use_case.crear()
    return render_template('reserva.html', movie_id=1)
