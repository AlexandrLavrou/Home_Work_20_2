import json

from container import movie_dao, director_dao, genre_dao



class DataLoader:
    @staticmethod
    def load_movies(json_file):
        with open(json_file, 'r') as file:
            movies_data = json.load(file)
        for movie_data in movies_data:
            movie_dao.create(movie_data)


    @staticmethod
    def load_director(json_file):
        with open(json_file, 'r') as file:
            director_data = json.load(file)
        for director_data in director_data:
            director_dao.create(director_data)

    @staticmethod
    def load_genre(json_file):
        with open(json_file, 'r') as file:
            genre_data = json.load(file)
        for genre_data in genre_data:
            genre_dao.create(genre_data)

