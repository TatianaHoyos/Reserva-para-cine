from app.domain.entities.reservation import Reservation

class ReservationUseCase:
    def __init__(self, reservation_repository, room_repository, movie_repository):
        self.reservation_repository = reservation_repository
        self.room_repository = room_repository
        self.movie_repository = movie_repository

    def crear_reserva(self, movie_id, function_id, room_id, seats):
        
        # 
        reserva = {
            'movie_id': movie_id,
            'function_id': function_id,
            'room_id': room_id,
            'seats': seats
            }
        reserva_id = self.reservation_repository.save_reservation(reserva)

        room = self.room_repository.get_room_by_id(room_id)
        movie = self.movie_repository.get_movie_by_id(movie_id)


        reserva_result = Reservation(id=reserva_id, movie=movie, function="",room=room, seats=seats)
        return reserva_result
