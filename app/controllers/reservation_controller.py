from flask import render_template, request, jsonify, url_for, redirect, session

from app import app
from app.adapters.database.reservation_repository import ReservationRepository
from app.domain.entities.movie import Movie
from app.adapters.database.movie_repository import MovieRepository
from app.adapters.database.room_repository import RoomRepository
from app.adapters.database.funtion_repository import FuntionRepository
from app.adapters.database.reservation_repository import ReservationRepository
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
    reservation_repository = ReservationRepository()
    funtion_use_case = FuntionUseCase(funtion_repository, room_repository,reservation_repository)
    funtions = funtion_use_case.listar_funtion(movie_id)
    return render_template('reserva.html', funtions=funtions)


@app.route('/confirmar_reserva', methods=['POST'])
def confirmar_reserva():
    data = request.get_json()
    seats = data.get('selectedSeats')
    function_id = data.get('function_id')
    movie_id = data.get('movie_id')
    room_id = data.get('room_id')

    reservation_repository = ReservationRepository()  
    reservation_use_case = ReservationUseCase(reservation_repository)
    reserva = reservation_use_case.crear_reserva(movie_id, function_id, room_id, seats)

    # Asegúrate de que reserva es serializable (convertir a dict si es necesario)
    if hasattr(reserva, 'to_dict'):
        reserva = reserva.to_dict()
     # Guardar la reserva en la sesión
    session['reserva'] = reserva

    # Responder con la URL de redirección
    return jsonify({'redirect': url_for('reserva_confirmada')})

@app.route('/reserva_confirmada', methods=['GET'])
def reserva_confirmada():
    # Obtener la reserva desde la sesión
    reserva = session.get('reserva', None)
    return render_template('reserva_confirmada.html', reserva=reserva)
