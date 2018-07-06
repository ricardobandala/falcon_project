import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Boolean, Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from base import base_model, TableTimeStampSchema


class UserModel(base_model):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)

    username = Column(String(255), nullable=True, unique=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)
    user_profile = relationship('UserProfileModel', backref='user')

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class UserSchema(Schema, TableTimeStampSchema):

    id = fields.Integer()

    user_name = fields.String()
    password = fields.String()
    is_active = fields.Boolean()

    # @post_load
    # def create_model(self, _model, data):
    #     return UserModel(**data)
