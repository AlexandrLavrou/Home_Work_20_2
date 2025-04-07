from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director


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

