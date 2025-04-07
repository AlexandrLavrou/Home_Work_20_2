from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service
from dao.model.user import UserSchema

auth_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        user_data = request.json
        user_name = user_data.get("username", None)
        user_pass = user_data.get("password", None)
        if None in [user_name, user_pass]:
            abort(401)

        return auth_service.generate_tokens(user_data)

    def put(self):
        req_json = request.json
        tokens = auth_service.update_tokens(req_json)
        return tokens




