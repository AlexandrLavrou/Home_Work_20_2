from flask_restx import Resource, Namespace

from container import genre_service
from dao.model.genre import GenreSchema
from utils.auth import auth_required

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @auth_required
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
