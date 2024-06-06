from tinydb import TinyDB

class ReservationRepository:
    def __init__(self, db_file):
        self.db = TinyDB(db_file)
        self.reservation_table = self.db.table("reservation")

    def create_empty_table(self):
        if not self.reservation_table.all():
            self.reservation_table.insert({'idCliente': 0, 'idBoleto': 0, 'fecha_reserva': ''})

