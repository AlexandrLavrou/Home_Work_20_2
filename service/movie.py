from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self,dao: MovieDAO):
            self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def create(self,data):
        return self.dao.create(data)


    def get_all(self, filters=None):

        movies = self.dao.session.query(Movie)

        if filters:
            if 'director_id' in filters:
                movies = movies.filter(Movie.director_id == filters['director_id'])
            if 'genre_id' in filters:
                movies = movies.filter(Movie.genre_id == filters['genre_id'])
            if 'year' in filters:
                movies = movies.filter(Movie.year == filters['year'])

        return movies.all()

    def update(self, data):
        movie_id = data.get("id")
        movie = self.get_one(movie_id)

        self.dao.update(movie)

    def update2(self, movie_id, data):
        """Update an existing movie."""
        movie = self.dao.get_one(movie_id)
        if not movie:
            raise ValueError(f"Movie with ID {movie_id} not found.")

        for key, value in data.items():
            setattr(movie, key, value)

        return self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)