from flask import render_template, request, jsonify, url_for
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

@app.route('/confirmar_reserva', methods=['POST'])
def confirmar_reserva():
    data = request.get_json()
    selected_seats = data.get('selectedSeats')
    # Aquí puedes procesar los asientos seleccionados y realizar las acciones necesarias
    # Por ejemplo, guardar la reserva en la base de datos
 
    # Redirige a la página de confirmación de reserva
    return jsonify({'redirect': url_for('reserva_confirmada')})

# @app.route('/reserva_confirmada')
# def reserva_confirmada():
#     return render_template('reserva_confirmada.html')
@app.route('/')
def index():
    # Suponiendo que 'funtions' es una lista de funciones que obtienes de tu base de datos
    funtions = [
        {
            'id': 1,
            'movie_id': 'Inception',
            'room_id': 'Sala 1',
            'date': '2024-06-15',
            'hora': '18:00',
            'seats': [{'label': 'A1', 'available': True}, {'label': 'A2', 'available': False}, {'label': 'A3', 'available': True}]
        },
        {
            'id': 2,
            'movie_id': 'Inception',
            'room_id': 'Sala 2',
            'date': '2024-06-15',
            'hora': '20:00',
            'seats': [{'label': 'B1', 'available': True}, {'label': 'B2', 'available': True}, {'label': 'B3', 'available': False}]
        }
    ]
    return render_template('reserva.html', funtions=funtions)

@app.route('/reserva_confirmada')
def reserva_confirmada():
    function_id = request.args.get('function', 'No especificado')
    seats = request.args.get('seats', 'No especificado')
    function_text = request.args.get('functionText', 'No especificado')
    return render_template('reserva_confirmada.html', function_id=function_id, seats=seats, function_text=function_text)
