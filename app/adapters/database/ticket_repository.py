from tinydb import TinyDB

class TicketRepository:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)
        self.ticket_table = self.db.table("ticket")

    def create_empty_table(self):
        if not self.ticket_table.all():
            self.ticket_table.insert({'idFuncion': 0, 'numero_asiento': 0, 'precio': 0.0, 'vendido': False})
