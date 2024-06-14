from app.domain.entities.movie import Movie
# en esta clase no hay un import de el adaptador o repositorio de la db
class ConfiguratonUseCase:
    def __init__(self, movie_repository, room_repository, funtion_repository, reservation_repository):
        self.movie_repository = movie_repository
        self.room_repository =  room_repository
        self.funtion_repository =  funtion_repository
        self.reservation_repository = reservation_repository

    def crear_datos(self):
        self.movie_repository.insert_movies()
        self.room_repository.insert_rooms()
        self.funtion_repository.insert_funtion()
        

    def eliminar_datos(self):
        self.movie_repository.delete_all_movie()
        self.room_repository.delete_all_rooms()
        self.funtion_repository.delete_all_funtion()
        self.reservation_repository.delete_all_reservation()
