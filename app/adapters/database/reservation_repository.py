from tinydb import TinyDB, Query

class ReservationRepository:
    def __init__(self):
        self.db = TinyDB("reservation.json")
        self.reservation_table = self.db.table("reservation")

    def consultar_reservaciones(self, id_funtions):
        reservation_table = self.reservation_table
        Reservation = Query()
        result = reservation_table.search(Reservation.function_id.one_of(id_funtions))
        print(id_funtions)
        print(result)
        return result

    def save_reservation(self, reservation):
        result = self.reservation_table.insert({
            'movie_id': reservation['movie_id'],
            'function_id': int(reservation['function_id']),
            'room_id' : reservation['room_id'],
            'seats': reservation['seats']
        })
        return result

         
    def delete_all_reservation(self):
       self.reservation_table.truncate()