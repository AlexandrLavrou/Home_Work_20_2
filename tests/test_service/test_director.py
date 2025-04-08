import pytest

from dao.model.director import Director
from service.director import DirectorService


class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors[0].name == "John"
        assert len(directors) == 3

    def test_create(self):
        director_data = {"name": "Markus"}
        director = self.director_service.create(director_data)
        assert isinstance(director, Director) == True
        assert director.id is not None

    def test_update(self):
        markus = {"id": 5, "name": "Markus"}
        self.director_service.update(markus)

    def test_delete(self):
        self.director_service.delete(1)

