from tinydb import TinyDB

class ReservationRepository:
    def __init__(self):
        self.db = TinyDB("reservation.json")
        self.reservation_table = self.db.table("reservation")

    # def create_empty_table(self):
    #     if not self.reservation_table.all():
    #         self.reservation_table.insert({'id': 0, "movie_id": 0, "function_id": 0, 'seats': ''})

    def save_reservation(self, reservation):
        result = self.reservation_table.insert({
            'movie_id': reservation['movie_id'],
            'function_id': reservation['function_id'],
            'room_id' : reservation['room_id'],
            'seats': reservation['seats']
        })
        return result