from app.domain.entities.movie import Movie
from app.domain.entities.funtion import Funtion
# en esta clase no hay un import de el adaptador o repositorio de la db
class FuntionUseCase:
    def __init__(self, funtion_repository ,room_repository):
        self.funtion_repository = funtion_repository
        self.room_repository = room_repository


    def listar_funtion(self, movie_id):
        # Obtener datos de funciones
        funtion_data = self.funtion_repository.get_all_funtions(movie_id)
        
        # Obtener IDs de salas
        room_ids = list({int(function['room_id']) for function in funtion_data})

        # Obtener datos de salas
        room_data = self.room_repository.get_all_rooms_by_funtions(room_ids)
        print(room_data)
        # Convertir room_data en un diccionario
        room_dict = {room['id']: room for room in room_data}
        
        # Crear objetos Funtion
        functions = []
        for function in funtion_data:
            room = room_dict.get(function['room_id'])
            movie = function['movie_id']  # Asumiendo que movie es un objeto o ID ya obtenido
            
            # Si es necesario, puedes obtener el objeto movie basado en movie_id aquí
            # movie = get_movie_by_id(function['movie_id'])
            
            seats = room.get('seats', []) if room else []  # Obtener asientos de room_data si están disponibles
            function_obj = Funtion(
                id=function['id'],
                movie=movie,
                room=room,
                date=function['date'],
                hora=function['hora'],
                seats=seats
            )
            functions.append(function_obj)

        return functions