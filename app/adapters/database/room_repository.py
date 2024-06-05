from tinydb import TinyDB

#sala
class RoomRepository:
    def __init__(self):
        self.db = TinyDB("DBsala.json")

    def get_all_salas(self):
        return self.db.all()

    def crear_salas(self):
     self.dbsala.insert_multiple([
            {"id": 1, "title": "Película 1", "synopsis": "Sinopsis de la película 1", "duration": "120 min", "poster": "https://via.placeholder.com/300x400", "clasification": "Drama","release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "El Padrino",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Drama", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Interestelar", "synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Ciencia ficción", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Titanic",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Romance", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "La La Land", "synopsis": "Sinopsis de la película 1", "duration": "120 min", "poster": "https://via.placeholder.com/300x400","clasification": "Musical","release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "El Señor de los Anillos: La Comunidad del Anillo","synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400", "clasification": "Fantasía","release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Harry Potter y la piedra filosofal",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Fantasía", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "El Rey León", "synopsis": "Sinopsis de la película 1", "duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Animación", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Matrix",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Acción", "release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Forrest Gump",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Drama","release_date": "2024-06-10","language": "Inglés"},
            {"id": 1,"title": "Gladiador",  "synopsis": "Sinopsis de la película 1","duration": "120 min","poster": "https://via.placeholder.com/300x400","clasification": "Acción","release_date": "2024-06-10","language": "Inglés"},
        ])



