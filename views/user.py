from flask import request
from flask_restx import Namespace, Resource, abort

from container import user_service
from dao.model.user import UserSchema
from utils.auth import admin_required, auth_required

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        user_data = request.json

        if user_service.get_by_name(user_data.get('email')):
            abort(409, f"User with email: {user_data.get('email')} already exist")

        if None in [user_data.get('email'), user_data.get('password'), user_data.get('role')]:
            abort(400, "email, password and role can`t be null")

        user = user_service.create(user_data)
        return "", 201, {"Location": f"{request.base_url}/{user.id}"}

@user_ns.route('/<int:user_id>')
class UserView(Resource):
    @auth_required
    def get(self, user_id):
        user = user_service.get_one(user_id)
        return user_schema.dump(user), 200

    @admin_required
    def delete(self, user_id):
        deleted = user_service. delete(user_id)
        if deleted:
            return "", 204

        return "", 404




