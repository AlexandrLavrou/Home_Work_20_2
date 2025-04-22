import calendar
import datetime


import jwt
from flask import request
from flask_restx import abort
from werkzeug.exceptions import Unauthorized

from constants import TOKEN_SECRET, TOKEN_ALGO
from container import user_service
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_access_token(self, user):
        min30 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=30)
        user_data = {
            "email": user.email,
            "role": user.role,
            "exp": calendar.timegm(min30.timetuple())
        }
        access_token = jwt.encode(user_data, TOKEN_SECRET, TOKEN_ALGO)
        return access_token

    def get_token_from_headers(self):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise Unauthorized("Authorisation header is missing")

        token = auth_header.split("Bearer ")[-1].strip()
        return token

    def get_user_from_token(self,token):

        user_data = jwt.decode(token, TOKEN_SECRET, TOKEN_ALGO)
        if not user_data:
            abort(401)
        email = user_data.get("email")
        user = user_service.get_by_email(email)
        return user


    def generate_refresh_token(self, user):
        days130 = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=130)
        user_data = {
            "email": user.email,
            "role": user.role,
            "exp": calendar.timegm(days130.timetuple())
        }
        refresh_token = jwt.encode(user_data, TOKEN_SECRET, TOKEN_ALGO)
        return refresh_token

    def generate_tokens(self, user_data):
        user = self.user_service.check_user(user_data)

        password_hash = user.password
        if not self.user_service.compare_passwords(password_hash, user_data):
            abort(401)

        return {
            "access_token": self.generate_access_token(user),
            "refresh_token": self.generate_refresh_token(user)
        }

    def update_tokens(self, req_json):
        refresh_token = req_json.get("refresh_token")
        if refresh_token is None:
            abort(401)
        data = jwt.decode(jwt=refresh_token, key=TOKEN_SECRET, algorithms=[TOKEN_ALGO])

        user = self.user_service.check_user(data, is_refresh=True)

        return {
            "access_token": self.generate_access_token(user),
            "refresh_token": self.generate_refresh_token(user)
        }


