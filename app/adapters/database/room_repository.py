from tinydb import TinyDB, Query

# Definir la clase RoomRepository
class RoomRepository:
    def __init__(self):
        self.db = TinyDB("rooms.json")
    
    def get_all_rooms(self):
        return self.db.table('rooms').all()

    def get_all_rooms_by_funtions(self, rooms_ids):
        room_table = self.db.table('room')

        Room = Query()
        return room_table.search(Room.id.one_of(rooms_ids))

    def insert_rooms(self):
        room_table = self.db.table('room')
        rooms = [
            {'id': 1 ,'nombre': 'Sala 1', 'tipo_sala': 'Normal', 'capacidad': 100},
            {'id': 1 ,'nombre': 'Sala 1', 'tipo_sala': 'Normal', 'capacidad': 100},
            {'id': 2 ,'nombre': 'Sala 2', 'tipo_sala': 'Normal', 'capacidad': 150},
            {'id': 3 ,'nombre': 'Sala 3', 'tipo_sala': 'Normal', 'capacidad': 120},
            {'id': 4 ,'nombre': 'Sala 4', 'tipo_sala': 'Normal', 'capacidad': 200}
        ]
        room_table.insert_multiple(rooms)

    def delete_all_rooms(self):
        room_table = self.db.table('room')
        room_table.truncate()