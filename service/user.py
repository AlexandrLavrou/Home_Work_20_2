import base64
import hashlib
import hmac

from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_ALGO, TOKEN_ALGO, TOKEN_SECRET
from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self,user_id):
        return self.dao.get_one(user_id)

    def get_by_name(self, username):
        return self.dao.get_by_name(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):

        user_pass = data.get("password")
        data["password"] = self.get_hash(user_pass)
        return self.dao.create(data)

    def update(self, user_data):

        return self.dao.update(user_data)

    def delete(self, user_id):
        return self.dao.delete(user_id)


    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            PWD_ALGO,
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))
    # .decode("utf-8", "ignore"))

    def check_user(self, user_data, is_refresh=False):

        user = self.get_by_name(user_data.get("username"))
        if not user:
            abort(400)
        if not is_refresh:
            if not self.compare_passwords(user.password, user_data):
                abort(401, "Invalid username or password")
        return user

    def compare_passwords(self, password_hash, user_data):
        decoded_password_hash = base64.b64decode(password_hash)

        other_password = user_data.get("password")
        user_password = base64.b64decode(self.get_hash(other_password))
        return hmac.compare_digest(decoded_password_hash, user_password)













