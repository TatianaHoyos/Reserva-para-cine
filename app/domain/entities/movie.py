class Movie:
    def __init__(self, id, title, synopsis, duration, poster, clasification, release_date, language):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.duration = duration
        self.poster = poster
        self.clasification = clasification
        self.release_date = release_date
        self.language = language
       

    def __repr__(self):
        return f'<Movie {self.title}>'