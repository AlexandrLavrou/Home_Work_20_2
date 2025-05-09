import base64
import hashlib
import hmac

from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_ALGO
from dao.user import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self,user_id):
        return self.dao.get_one(user_id)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):

        user_pass = data.get("password")
        data["password"] = self.get_hash(user_pass)
        return self.dao.create(data)

    def update(self, user):

        return self.dao.update(user)

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

    def update_password(self, user_id, password):

        user = self.get_one(user_id)
        user.password = self.get_hash(password)
        updated_user = self.update(user)

        return updated_user



    def check_user(self, user_data, is_refresh=False):

        user = self.get_by_email(user_data.get("email"))
        other_password = user_data.get("password")

        if not user:
            abort(400)
        if not is_refresh:
            if not self.compare_passwords(user.password, other_password):
                abort(401, "Invalid username or password")
        return user

    def compare_passwords(self, password_hash, other_password):
        decoded_password_hash = base64.b64decode(password_hash)
        user_password = base64.b64decode(self.get_hash(other_password))
        return hmac.compare_digest(decoded_password_hash, user_password)













