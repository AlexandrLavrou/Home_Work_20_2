# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

# Пример

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dbase.db'
    # DATABASE_PATH = os.path.join("database", 'dbase.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    JSONIFY_PRETTYPRINT_REGULAR = True

    DIRECTOR_PATH = "jsons/director_list.json"
    GENRE_PATH = "jsons/genre_list.json"
    MOVIE_PATH = "jsons/movie_list.json"


