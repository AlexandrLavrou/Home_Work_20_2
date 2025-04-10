# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self,session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def create(self,data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def get_all(self):
        return self.session.query(Movie)

    def get_by_director(self,director_id):
        movies = self.get_all().filter(Movie.director_id == director_id)
        return movies

    def get_by_genre(self, genre_id):
        movies = self.get_all().filter(Movie.genre_id == genre_id)
        return movies

    def get_by_year(self, year):
        movies = self.get_all().filter(Movie.year == year)
        return movies

    def update(self, movie):

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie_id):
        movie = self.get_one(movie_id)

        self.session.delete(movie)
        self.session.commit()

