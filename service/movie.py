from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self,dao: MovieDAO):
            self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def create(self,data):
        return self.dao.create(data)

    def get_all(self, filters=None, page=1, per_page=12):
        query = self.dao.get_all()

        if filters:
            if 'director_id' in filters:
                query = query.filter(Movie.director_id == filters['director_id'])
            if 'genre_id' in filters:
                query = query.filter(Movie.genre_id == filters['genre_id'])
            if 'year' in filters:
                query = query.filter(Movie.year == filters['year'])

        total = query.count()
        movies = query.offset((page - 1) * per_page).limit(per_page).all()
        return movies, total

    def update(self, data):
        movie_id = data.get("id")
        movie = self.get_one(movie_id)

        self.dao.update(movie)

    def update2(self, data):
        """Update an existing movie."""
        movie_id = data.get("id")
        movie = self.dao.get_one(movie_id)
        if not movie:
            raise ValueError(f"Movie with ID {movie_id} not found.")

        for key, value in data.items():
            setattr(movie, key, value)

        return self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)