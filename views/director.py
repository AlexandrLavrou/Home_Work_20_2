from flask_restx import Resource, Namespace

from container import director_service
from dao.model.director import DirectorSchema
from utils.auth import auth_required

director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @auth_required
    def get(self, director_id):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200
