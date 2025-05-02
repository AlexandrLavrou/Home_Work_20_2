from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service, user_service
from dao.model.user import UserSchema
from utils.auth import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()
@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):

        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        user_data = request.json

        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        if user_data.get('name'):
            user.name = user_data.get('name')
        if user_data.get('surname'):
            user.surname = user_data.get('surname')
        if user_data.get('favorite_genre'):
            user.favorite_genre = user_data.get('favorite_genre')

        user_service.update(user)

@user_ns.route('/password')
class UserPasswordView(Resource):
    @auth_required
    def put(self):

        token = auth_service.get_token_from_headers()
        user = auth_service.get_user_from_token(token)

        user_passwords = request.json
        password_1 = user_passwords.get('password_1')
        password_2 = user_passwords.get('password_2')

        if None in [password_1, password_2]:
            abort(400, "Password can't be None")

        if password_1 != password_2:
            abort(400, "Password is not match")

        if user_service.compare_passwords(user.password, password_1):
            abort(400, "Password have to be new")

        return user_service.update_password(user.id, password_1), 200





