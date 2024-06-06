from app.domain.entities.movie import Movie
# en esta clase no hay un import de el adaptador o repositorio de la db
class ConfiguratonUseCase:
    def __init__(self, movie_repository, room_repository, funtion_repository):
        self.movie_repository = movie_repository

    def crear_datos(self):
        movie_repository.insert_movies()
        room_repository.insert_rooms()
        funtion_repository.insert_funtion()
        

    def eliminar_datos(self):
        movie_repository.delete_all_movie()
        room_repository.delete_all_rooms()
        funtion_repository.delete_all_funtion()
