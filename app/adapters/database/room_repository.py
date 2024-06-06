from tinydb import TinyDB

# Definir la clase RoomRepository
class RoomRepository:
    def __init__(self):
        self.db = TinyDB("cine.json")

    def insert_rooms(self):
        room_table = self.db.table('room')
        rooms = [
            {'nombre': 'Sala 1', 'capacidad': 100},
            {'nombre': 'Sala 2', 'capacidad': 150},
            {'nombre': 'Sala 3', 'capacidad': 120},
            {'nombre': 'Sala 4', 'capacidad': 200}
        ]
        room_table.insert_multiple(rooms)

# Crear una instancia de RoomRepository
repo = RoomRepository()

# Insertar los registros
repo.insert_rooms()
