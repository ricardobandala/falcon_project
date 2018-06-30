import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from base import base_model
from user import UserSchema


class UserProfileModel(base_model):

    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # application_id = Column(Integer, ForeignKey('application.id'), nullable=False)

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class UserProfileSchema(Schema):

    id = fields.Integer()

    first_name = fields.String()
    last_name = fields.String()
    user = fields.Nested(UserSchema)
    # application = fields.Nested(ApplicationSchema)

    @post_load
    def create_model(self, _model, data):
        return UserProfileModel(**data)
