from app.domain.entities.reservation import Reservation

class ReservationUseCase:
    def __init__(self, reservation_repository):
        self.reservation_repository = reservation_repository

    def crear_reserva(self, movie_id, function_id, seats):
        # Verificar si movie_id es None antes de intentar crear la reserva
        if movie_id is None:
            raise ValueError("No se proporcionó un ID de película para la reserva.")
        
        # Crear la reserva solo si movie_id no es None
        reserva = Reservation(id=None, movie=movie_id, function=function_id, seats=seats)
        self.reservation_repository.save_reservation(reserva)
