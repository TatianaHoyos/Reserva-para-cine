from tinydb import TinyDB,Query

# Definir la clase MovieRepository
class MovieRepository:
    def __init__(self):
        self.db = TinyDB("DbCine.json")

    def get_all_movies(self):
        return self.db.table('movies').all()

    def get_movie_by_id(self, movie_id):
        movie_table = self.db.table('movies')
        Movie = Query()
        results = movie_table.search(Movie.id == int(movie_id))
        return results


    def insert_movies(self):
        movies_table = self.db.table('movies')
        movies = [
            {"id": 1, "title": "Película 1", "synopsis": "Sinopsis de la película 1", "duration": "120 min", "poster": "https://via.placeholder.com/300x400", "clasification": "Drama","release_date": "2024-06-10","language": "Inglés"},
            {"id": 2,"title": "El Padrino",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Drama", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 3,"title": "Interestelar", "synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Ciencia ficción", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 4,"title": "Titanic",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Romance", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 5,"title": "La La Land", "synopsis": "Sinopsis de la película 1", "duration": "120 min", "poster": "https://via.placeholder.com/300x400","clasification": "Musical","release_date": "2024-06-10","language": "Inglés"},
            {"id": 6,"title": "El Señor de los Anillos: La Comunidad del Anillo","synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400", "clasification": "Fantasía","release_date": "2024-06-10","language": "Inglés"},
            {"id": 7,"title": "Harry Potter y la piedra filosofal",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Fantasía", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 8,"title": "El Rey León", "synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Animación", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 9,"title": "Matrix",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Acción", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 10,"title": "Forrest Gump",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Drama","release_date": "2024-06-10","language": "Inglés"},
            {"id": 11,"title": "Gladiador",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Acción","release_date": "2024-06-10","language": "Inglés"}
        ]
        movies_table.insert_multiple(movies)

        
    def delete_all_movie(self):
        movies_table = self.db.table('movies')
        movies_table.truncate()