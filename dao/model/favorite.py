from marshmallow import Schema, fields

from setup_db import db


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    user = db.relationship("User")
    movie = db.relationship("Movie")

class FavoriteSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    movie_id = fields.Int()

    user = fields.Pluck("UserSchema", "email")
    movie = fields.Pluck("MovieSchema", "title")
