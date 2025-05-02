from dao.model.favorite import Favorite


class FavoriteDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, favorite_id):
        return self.session.query(Favorite).get(favorite_id)

    def create(self, data):
        favorite = Favorite(**data)
        self.session.add(favorite)
        self.session.commit()

    def delete(self, favorite_id):
        favorite = self.get_one(favorite_id)
        self.session.delete(favorite)
        self.session.commit()

    def get_by_movie_and_user(self, movie_id, user_id):
        favorite = self.session.query(Favorite).filter(Favorite.movie_id == movie_id, Favorite.user_id == user_id).first()
        return favorite

    def get_by_user(self, user_id):
        favorites = self.session.query(Favorite).filter(Favorite.user_id == user_id)
        return favorites