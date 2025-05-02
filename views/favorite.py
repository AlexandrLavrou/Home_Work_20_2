from flask import request
from flask_restx import Namespace, Resource

from container import favorite_service, auth_service
from dao.model.favorite import FavoriteSchema
from utils.auth import auth_required

favorite_ns = Namespace('favorites')

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)

@favorite_ns.route('/movies')
class FavoritesView(Resource):

    @auth_required
    def get(self):

        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        user_id = user.id
        favorites = favorite_service.get_by_user(user_id)

        return favorites_schema.dump(favorites), 200

@favorite_ns.route('/movies/<int:movie_id>')
class FavoriteView(Resource):

    @auth_required
    def post(self, movie_id):
        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        favorite = {
            "user_id": user.id,
            "movie_id": movie_id
        }

        favorite_service.create(favorite)

        return "", 201
    @auth_required
    def delete(self, movie_id):

        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)


        favorite = favorite_service.get_by_movie(movie_id, user.id)

        if not favorite:
            return "", 404

        favorite_service.delete(favorite.id)
        return "", 204



