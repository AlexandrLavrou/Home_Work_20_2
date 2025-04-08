import pytest

from dao.model.movie import Movie
from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        print(movies[0].title)
        assert movies[0].title == "Йеллоустоун"
        assert len(movies) == 3

    def test_create(self):
        movie_data = {
        "title": "Омерзительная восьмерка",
        "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
        "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
        "year": 2015,
        "rating": 7.8,
        "genre_id": 4,
        "director_id": 2,
    }
        movie = self.movie_service.create(movie_data)
        assert isinstance(movie, Movie) == True
        assert movie.id is not None

    def test_update(self):
        movie = {
        "title": "Омерзительная восьмерка",
        "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
        "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
        "year": 2015,
        "rating": 7.8,
        "genre_id": 4,
        "director_id": 2,
        "id": 2
    }
        self.movie_service.update(movie)


    def test_update2(self):
        movie = {
        "title": "Омерзительная восьмерка",
        "description": "США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.",
        "trailer": "https://www.youtube.com/watch?v=lmB9VWm0okU",
        "year": 2015,
        "rating": 7.8,
        "genre_id": 4,
        "director_id": 2,
        "id": 2
    }
        self.movie_service.update2(movie)

    def test_delete(self):
        self.movie_service.delete(1)

