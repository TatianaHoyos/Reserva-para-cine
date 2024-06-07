from flask import render_template, request
from app import app
from app.domain.entities.movie import Movie
from app.adapters.database.movie_repository import MovieRepository
from app.adapters.database.room_repository import RoomRepository
from app.adapters.database.funtion_repository import FuntionRepository
from app.use_cases.movies_use_case import MoviesUseCase
from app.use_cases.funtion_use_case import FuntionUseCase
from app.use_cases.configuration_use_case import ConfiguratonUseCase

@app.route('/')
def movie_list():
    movie_repository = MovieRepository()  # Instancia el repositorio de películas
    movies_use_case = MoviesUseCase(movie_repository)
    movies = movies_use_case.listar_peliculas()
    return render_template('index.html', movies=movies)

@app.route('/reserva')
def reserva():
    movie_id = request.args.get('movie')
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  # No pasar room_repository
    funtion_use_case = FuntionUseCase(funtion_repository, room_repository)
    funtions = funtion_use_case.listar_funtion(movie_id)
    return render_template('reserva.html', funtions=funtions)

@app.route('/iniciardatos')
def iniciardatos():
    movie_repository = MovieRepository()
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  # No pasar room_repository
    configuration_use_case = ConfiguratonUseCase(movie_repository, room_repository, funtion_repository)
    configuration_use_case.crear_datos()
    return "se crearon los datos"

@app.route('/eliminardatos')
def eliminardatos():
    movie_repository = MovieRepository()
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  # No pasar room_repository
    configuration_use_case = ConfiguratonUseCase(movie_repository, room_repository, funtion_repository)
    configuration_use_case.eliminar_datos()
    return "se eliminaron los datos"
