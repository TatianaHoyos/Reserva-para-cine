from app.domain.entities.movie import Movie
# en esta clase no hay un import de el adaptador o repositorio de la db
class MoviesUseCase:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def listar_peliculas(self):
        movies_data =  self.movie_repository.get_all_movies()
        return [Movie(**movie) for movie in movies_data]
     

    # def crear(self):
    #     self.movie_repository.crear_pelicula()
    #     return "se creo"