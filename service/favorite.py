from dao.favorite import FavoriteDAO


class FavoriteService:

    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_one(self, favorite_id):
        return self.dao.get_one(favorite_id)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, favorite_id):
        return self.dao.delete(favorite_id)

    def get_by_movie(self, movie_id, user_id):
        return self.dao.get_by_movie_and_user(movie_id, user_id)

    def get_by_user(self, user_id):
        return self.dao.get_by_user(user_id)
