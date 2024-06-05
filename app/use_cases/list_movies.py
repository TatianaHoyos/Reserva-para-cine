from app.domain.entities.movie import Movie

class ListMoviesUseCase:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self):
        movies_data =  self.movie_repository.get_all_movies()
        return [Movie(**movie) for movie in movies_data]
     