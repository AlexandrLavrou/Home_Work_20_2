import pytest

from dao.model.genre import Genre
from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(3)

        assert genre is not None
        assert genre.id is not None
        # assert isinstance(movie1, )

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert genres[0].name == "Mystic"
        assert genres[2].name == "Horror"
        assert len(genres) > 0

    def test_create(self):
        genre_data = {"name": "Mystirius"}
        genre = self.genre_service.create(genre_data)
        assert isinstance(genre, Genre) == True
        assert genre.id is not None

    def test_update(self):
        misticus = {"id": 5, "name": "Misticus"}
        self.genre_service.update(misticus)

    def test_delete(self):
        self.genre_service.delete(1)

