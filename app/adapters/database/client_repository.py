from tinydb import TinyDB

# Definir la clase ClientRepository
class ClientRepository:
    def __init__(self):
        self.db = TinyDB("cine.json")

    def insert_clients(self):
        client_table = self.db.table('client')
        clients = [
            {'nombre': 'Juan Pérez'},
            {'nombre': 'María López'},
            {'nombre': 'Carlos García'},
            {'nombre': 'Ana Martínez'},
            {'nombre': 'Luis Rodríguez'}
        ]
        client_table.insert_multiple(clients)

# Crear una instancia de ClientRepository
repo = ClientRepository()

# Insertar los registros
repo.insert_clients()
