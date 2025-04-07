# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request, jsonify
# Пример
from flask_restx import Resource, Namespace, ValidationError

from container import movie_service
from dao.model.movie import MovieSchema
from utils.auth import auth_required, admin_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        year = request.args.get('year', type=int)

        filters={}
        if director_id:
            filters['director_id'] = director_id
        if genre_id:
            filters['genre_id'] = genre_id
        if year:
            filters['year'] = year


        movies = movie_service.get_all(filters)
        return movies_schema.dump(movies), 200

    def post(self):
        request_json = request.json
        movie = movie_service.create(request_json)
        return "", 201

@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @auth_required
    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, movie_id):
        try:
            updated_data = movie_schema.load(request.json)
            movie = movie_service.update(updated_data)
            return movie_schema.dump(movie), 204
        except ValueError as e:
            return jsonify(f"error: {e}")

    @admin_required
    def put2(self, movie_id):
        try:
            data = movie_schema.load(request.json)
            movie = movie_service.update2(movie_id, data)
            return movie_schema.dump(movie), 200
        except ValueError as e:
            return {"error": str(e)}, 404
        except ValidationError as e:
            return {"error": str(e)}, 400

    @admin_required
    def delete(self, movie_id):
        deleted = movie_service.delete(movie_id)
        if deleted:
            return "", 204
        return "", 404

