

from flask import request
from flask_restx import Namespace, Resource, abort

from container import auth_service, user_service
from dao.model.user import UserSchema
from utils.auth import auth_required

auth_ns = Namespace('auth')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        user_data = request.json
        user_email = user_data.get("email", None)
        user_pass = user_data.get("password", None)
        if None in [user_email, user_pass]:
            abort(401)

        user = user_service.create(user_data)
        return "", 201, {"Location": f"{request.base_url}/{user.id}"}

        # return auth_service.generate_tokens(user_data)
@auth_ns.route('/login')
class AuthLoginView(Resource):
    def post(self):
        user_data = request.json
        return auth_service.generate_tokens(user_data)

    @auth_required
    def put(self):
        req_json = request.json
        tokens = auth_service.update_tokens(req_json)
        return tokens




