from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        return self.session.query(Genre).get(genre_id)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self,data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()


