from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, genre_id):
        return self.dao.get_one(genre_id)

    def get_all(self):
        return self.dao.get_all()