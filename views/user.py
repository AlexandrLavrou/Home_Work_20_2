from flask import request
from flask_restx import Namespace, Resource

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

        return user

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


    @auth_required
    def put(self):
        pass



