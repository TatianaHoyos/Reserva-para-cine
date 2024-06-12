from flask import render_template, request, jsonify, url_for
from app import app
from app.domain.entities.movie import Movie
from app.adapters.database.movie_repository import MovieRepository
from app.adapters.database.room_repository import RoomRepository
from app.adapters.database.funtion_repository import FuntionRepository
from app.adapters.database.reservation_repository import ReservationRepository
from app.use_cases.movies_use_case import MoviesUseCase
from app.use_cases.funtion_use_case import FuntionUseCase
from app.use_cases.configuration_use_case import ConfiguratonUseCase


@app.route('/iniciardatos')
def iniciardatos():
    movie_repository = MovieRepository()
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  # No pasar room_repository
    reservation_repository = ReservationRepository()
    configuration_use_case = ConfiguratonUseCase(movie_repository, room_repository, funtion_repository, reservation_repository)
    configuration_use_case.crear_datos()
    return "se crearon los datos"

@app.route('/eliminardatos')
def eliminardatos():
    movie_repository = MovieRepository()
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  # No pasar room_repository
    reservation_repository = ReservationRepository()
    configuration_use_case = ConfiguratonUseCase(movie_repository, room_repository, funtion_repository, reservation_repository)
    configuration_use_case.eliminar_datos()
    return "se eliminaron los datos"