from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    john = Director(id=1, name="John")
    lola = Director(id=2, name="lola")
    helga = Director(id=3, name="Helga")

    director_dao.get_one = MagicMock(return_value=helga)
    director_dao.get_all = MagicMock(return_value=[john, lola, helga])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()
    return director_dao

@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    mystic = Genre(id=1, name="Mystic")
    sifi = Genre(id=2, name="Sifi")
    horror = Genre(id=3, name="Horror")

    genre_dao.get_one = MagicMock(return_value=mystic)
    genre_dao.get_all = MagicMock(return_value=[mystic, sifi, horror])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        title = "Йеллоустоун",
        description = "Владелец реки»",
        trailer = "https://www.youtube.com/watch?v=UKei_d0cbP4",
        year = 2018,
        rating = 8.6,
        genre_id = 17,
        director_id = 1,
        id = 1)

    movie2 = Movie(
        title="какойто фильм",
        description="сожитель  реки»",
        trailer="https://www.youtube.com/watch?v=0cbP4",
        year=2025,
        rating=1.6,
        genre_id=1,
        director_id=3,
        id=2)

    movie3 = Movie(
        title="какойто фильм 2",
        description="сожритель украденной руки»",
        trailer="https://www.youtube.com/watch?v=0cbP4",
        year=1980,
        rating=4.6,
        genre_id=2,
        director_id=2,
        id=3)

    movie_dao.get_one = MagicMock(return_value=movie3)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()
