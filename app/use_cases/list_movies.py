class ListMoviesUseCase:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def execute(self):
        return self.movie_repository.get_all_movies()