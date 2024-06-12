from flask import render_template, request, redirect, url_for
from app import app
from app.adapters.database.reservation_repository import ReservationRepository
from app.domain.entities.movie import Movie
from app.adapters.database.movie_repository import MovieRepository
from app.adapters.database.room_repository import RoomRepository
from app.adapters.database.funtion_repository import FuntionRepository
from app.use_cases.movies_use_case import MoviesUseCase
from app.use_cases.funtion_use_case import FuntionUseCase
from app.use_cases.configuration_use_case import ConfiguratonUseCase
from app.use_cases.reservation_use_case import ReservationUseCase

@app.route('/')
def movie_list():
    movie_repository = MovieRepository()  
    movies_use_case = MoviesUseCase(movie_repository)
    movies = movies_use_case.listar_peliculas()
    return render_template('index.html', movies=movies)

@app.route('/reserva')
def reserva():
    movie_id = request.args.get('movie_id')
    if movie_id is None:
        # Manejar el caso en que movie_id es None, por ejemplo, redirigir a otra página o mostrar un mensaje de error
        return "Error: No se proporcionó un ID de película."
    
    room_repository = RoomRepository()
    funtion_repository = FuntionRepository()  
    funtion_use_case = FuntionUseCase(funtion_repository, room_repository)
    funtions = funtion_use_case.listar_funtion(movie_id)
    return render_template('reserva.html', funtions=funtions, movie_id=movie_id)

@app.route('/reservar', methods=['POST'])
def reservar():
    movie_id = request.form['movie_id']
    function_id = request.form['function_id']
    seats = request.form['selectedSeats']

    reservation_repository = ReservationRepository()  
    reservation_use_case = ReservationUseCase(reservation_repository)
    reservation_use_case.crear_reserva(movie_id, function_id, seats)

    return redirect(url_for('confirmacion'))
