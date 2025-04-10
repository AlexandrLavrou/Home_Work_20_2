
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restx import Api

from config import Config
from load_data import DataLoader
from setup_db import db, init_db
from views.auth import auth_ns
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns
from views.user import user_ns


# def create_app(config: Config = Config(), **kwargs) -> Flask:
#     application = Flask(__name__)
#     application.config.from_object(config)
#     application.app_context().push()
#     return application

def create_app(config=None):
    from config import Config
    app = Flask(__name__)
    app.config.from_object(config or Config)
    return app



def configure_app(app: Flask):
    init_db(app)
    migrate = Migrate(app, db)
    api = Api(app)
    api.add_namespace(movie_ns, path='/movies')
    api.add_namespace(director_ns, path='/directors')
    api.add_namespace(genre_ns, path='/genre')
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(user_ns, path='/users')



def load_files(app):
    with app.app_context():

        try:
            DataLoader.load_movies(Config.MOVIE_PATH)
            DataLoader.load_director(Config.DIRECTOR_PATH)
            DataLoader.load_genre(Config.GENRE_PATH)
            print("Data successfully loaded.")
        except Exception as e:
            print(f"Data loading error: {e}")
#
if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_files(app)
    app.run(debug=True)
