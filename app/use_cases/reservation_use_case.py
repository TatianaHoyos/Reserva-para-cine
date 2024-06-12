from app.domain.entities.reservation import Reservation

class ReservationUseCase:
    def __init__(self, reservation_repository):
        self.reservation_repository = reservation_repository

    def crear_reserva(self, movie_id, function_id, room_id, seats):
        
        # reserva = Reservation(id=None, movie=movie_id, function=function_id, seats=seats)
        reserva = {
            'movie_id': movie_id,
            'function_id': function_id,
            'room_id': room_id,
            'seats': seats
            }
        self.reservation_repository.save_reservation(reserva)

        return "ok"
