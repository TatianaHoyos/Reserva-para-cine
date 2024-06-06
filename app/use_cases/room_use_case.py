from app.domain.entities.movie import Movie
# en esta clase no hay un import de el adaptador o repositorio de la db
class MoviesUseCase:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def listar_salas(self):
        room_data =  self.room_repository.get_all_rooms()
        return [Movie(**movie) for movie in movies_data]
     
