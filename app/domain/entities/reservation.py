class Reservation:
    def __init__(self, id, movie, function, room, seats):
        self.id = id
        self.movie = movie
        self.function = function
        self.room = room
        self.seats = seats

    def to_dict(self):
        return {
            'id': self.id,
            'movie': self.movie,
            'function': self.function,
            'room': self.room,
            'seats': self.seats
        }