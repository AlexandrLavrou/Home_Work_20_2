

from flask import request
from flask_restx import Namespace, Resource, abort, fields

from container import auth_service, user_service
from dao.model.user import UserSchema
from utils.auth import auth_required

auth_ns = Namespace('auth', description='Authentication')

auth_model = auth_ns.model("Auth", {
    "email": fields.String(required=True, description="Email пользователя"),
    "password": fields.String(required=True, description="Пароль")
})

tokens_model = auth_ns.model("Tokens", {
    "access_token": fields.String(description="JWT access token"),
    "refresh_token": fields.String(description="JWT refresh token"),
})


user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_ns.route('/register')
class AuthRegisterView(Resource):

    @auth_ns.expect(auth_model)
    @auth_ns.response(201, "User successfully registered")
    @auth_ns.response(401, "Incorret data")
    def post(self):
        """register new user"""
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

    @auth_ns.expect(auth_model)
    @auth_ns.response(200, "Tokens awarded", model=tokens_model)
    @auth_ns.response(401, "Wrong email or password")
    def post(self):
        user_data = request.json
        return auth_service.generate_tokens(user_data)

    @auth_ns.expect(tokens_model)
    @auth_ns.response(200, "Tokens updated", model=tokens_model)
    @auth_ns.response(401, "Invalid refresh token")
    @auth_required
    def put(self):
        req_json = request.json
        tokens = auth_service.update_tokens(req_json)
        return tokens




