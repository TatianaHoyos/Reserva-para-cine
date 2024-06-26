from app.domain.entities.movie import Movie
from app.domain.entities.funtion import Funtion
class FuntionUseCase:
    def __init__(self, funtion_repository, room_repository, reservation_repository):
        self.funtion_repository = funtion_repository
        self.room_repository = room_repository
        self.reservation_repository = reservation_repository

    def listar_funtion(self, movie_id):
        # Obtener datos de funciones
        funtion_data = self.funtion_repository.get_all_funtions(movie_id)

        # Obtener IDs de funciones
        funtions_ids = list({int(function['id']) for function in funtion_data})

        # Obtener asientos ocupados
        reservations = self.reservation_repository.consultar_reservaciones(funtions_ids)

        # Obtener IDs de salas
        room_ids = list({int(function['room_id']) for function in funtion_data})

        # Obtener datos de salas
        room_data = self.room_repository.get_all_rooms_by_funtions(room_ids)
        room_dict = {room['id']: room for room in room_data}

        # Crear objetos Funtion
        functions = []
        for function in funtion_data:
            room = room_dict.get(function['room_id'])
            movie = function['movie_id']
            if room:
                capacity = room['capacidad']
                rows = capacity // 10
                cols = 10
                seats = []

                for r in range(rows):
                    row_label = chr(65 + r)  # Genera las letras A, B, C, etc.
                    for c in range(cols):
                        seat_label = f"{row_label}{c + 1}"
                        seats.append({"label": seat_label, "available": True})

                # Marcar los asientos ocupados como no disponibles
                for reservation in reservations:
                    if reservation['function_id'] == function['id']:
                        reserved_seats = reservation['seats']
                        for reserved_seat in reserved_seats:
                            for seat in seats:
                                if seat['label'] == reserved_seat:
                                    seat['available'] = False

                function['seats'] = seats
            function['movie_id'] = function['movie_id']
            functions.append(function)

        return functions
