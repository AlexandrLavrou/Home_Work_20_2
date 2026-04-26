

from flask import request, jsonify

from flask_restx import Resource, Namespace, ValidationError, fields

from container import movie_service
from dao.model.movie import MovieSchema
from utils.auth import auth_required, admin_required

movie_ns = Namespace('movies', description="Movie management")

movie_model = movie_ns.model("Movie", {
    "id": fields.Integer(readonly=True, description="movie ID"),
    "title": fields.Integer(required=True, description="movie title"),
    "description": fields.Integer(required=True, description="description"),
    "trailer": fields.Integer(description="link to trailer"),
    "year": fields.Integer(description="year"),
    "rating": fields.Integer(description="rating"),
    "date_added": fields.Integer(description="data added"),
    "genre_id": fields.Integer(description="ID genre"),
    "director_id": fields.Integer(description="ID director")
    })

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    @movie_ns.doc(params={
        'director_id': 'filtred by director',
        'genre_id': 'filtred by genre',
        'year': 'filtred by year',
        'status': 'new — show new movies (last 2 weak)',
        'page': 'page number (по умолчанию 1)',
        'per_page': 'Кол-во элементов на странице (по умолчанию 12)'
    })
    @movie_ns.marshal_with(movie_model,as_list=True, code=200)
    def get(self):
        """Get all movies with filters sorts and pagination"""
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        year = request.args.get('year', type=int)

        status = request.args.get('status', type=str)
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=12, type=int)

        filters={}
        if director_id:
            filters['director_id'] = director_id
        if genre_id:
            filters['genre_id'] = genre_id
        if year:
            filters['year'] = year

        movies = movie_service.get_all(filters, page, per_page, status=status)
        return movies, 200

    @movie_ns.expect(movie_model)
    @movie_ns.marshal_with(movie_model, code=201)
    def post(self):
        """Add new movie"""
        request_json = request.json
        movie = movie_service.create(request_json)
        return movie, 201


@movie_ns.route('/<int:movie_id>')
@movie_ns.param('movie_id', 'movie ID')
class MovieView(Resource):
    @auth_required
    @movie_ns.marshal_with(movie_model)
    def get(self, movie_id):
        """get movie by ID"""
        movie = movie_service.get_one(movie_id)
        return movie, 200

    @admin_required
    @movie_ns.expect(movie_model)
    @movie_ns.marshal_with(movie_model, code=204)
    def put(self, movie_id):
        """update movie """
        try:
            updated_data = movie_schema.load(request.json)
            movie = movie_service.update(updated_data)
            return movie, 204
        except ValueError as e:
            return jsonify(f"error: {e}")

    @admin_required
    @movie_ns.expect(movie_model)
    @movie_ns.marshal_with(movie_model, code=200)
    def put2(self, movie_id):
        try:
            data = movie_schema.load(request.json)
            movie = movie_service.update2(movie_id, data)
            return movie, 200
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

