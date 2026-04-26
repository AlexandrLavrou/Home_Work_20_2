from flask_restx import Namespace, Resource, abort, fields

from container import favorite_service, auth_service
from dao.model.favorite import FavoriteSchema
from utils.auth import auth_required

favorite_ns = Namespace('favorites', description='Favorite control')

favorite_model = favorite_ns.model("Favorite", {
    "id": fields.Integer(readOnly=True),
    "user_id": fields.Integer(required=True),
    "movie_id": fields.Integer(required=True),
})

favorite_schema = FavoriteSchema()
favorites_schema = FavoriteSchema(many=True)

@favorite_ns.route('/movies')
class FavoritesView(Resource):

    @auth_required
    @favorite_ns.marshal_with(favorite_model)
    def get(self):
        """Getting the list of favorite movies from the current user"""
        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        user_id = user.id
        favorites = favorite_service.get_by_user(user_id)

        return favorites, 200

@favorite_ns.route('/movies/<int:movie_id>')
class FavoriteView(Resource):

    @auth_required
    def post(self, movie_id):
        """Add movie to favorite"""
        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        favorite = {
            "user_id": user.id,
            "movie_id": movie_id
        }
        favorite_check = favorite_service.get_by_movie_and_user(movie_id, user.id)
        if favorite_check:
            abort(400, "movie already in favorite")
        favorite_service.create(favorite)

        return "", 201

    @auth_required
    def delete(self, movie_id):
        """Delete movie from favorite"""
        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)
        favorite = favorite_service.get_by_movie_and_user(movie_id, user.id)
        if not favorite:
            return "", 404
        favorite_service.delete(favorite.id)
        return "", 204



