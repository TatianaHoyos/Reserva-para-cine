from tinydb import TinyDB, Query

class FuntionRepository:
    def __init__(self):
        self.db = TinyDB("funtion.json")
    
    def get_all_funtions(self, movie_id):
        funtion_table = self.db.table('funtion')
        Function = Query()
        results = funtion_table.search(Function.movie_id == int(movie_id))
        return results

    def insert_funtion(self):
        funtion_table = self.db.table('funtion')
        funtion = [
            {"id": 1, "movie_id": 1, "room_id": 1, "date": "20/05/2024", "hora": "6:00 p.m"},
            {"id": 2, "movie_id": 1, "room_id": 1, "date": "20/05/2024", "hora": "8:00 p.m"},
            {"id": 3, "movie_id": 1, "room_id": 1, "date": "20/05/2024", "hora": "10:00 p.m"},
            {"id": 4, "movie_id": 2, "room_id": 2, "date": "20/05/2024", "hora": "6:00 p.m"},
            {"id": 5, "movie_id": 2, "room_id": 2, "date": "20/05/2024", "hora": "8:00 p.m"},
            {"id": 6, "movie_id": 2, "room_id": 2, "date": "20/05/2024", "hora": "10:00 p.m"},
            {"id": 7, "movie_id": 3, "room_id": 3, "date": "20/05/2024", "hora": "6:00 p.m"},
            {"id": 8, "movie_id": 3, "room_id": 3, "date": "20/05/2024", "hora": "8:00 p.m"},
            {"id": 9, "movie_id": 3, "room_id": 3, "date": "20/05/2024", "hora": "10:00 p.m"}
            ]

        funtion_table.insert_multiple(funtion)

    def delete_all_funtion(self):
        funtion_table = self.db.table('funtion')
        funtion_table.truncate()
