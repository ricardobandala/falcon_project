from marshmallow import Schema, fields, post_load
from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from base import base_model
from factory import ModelIdMixin, ModelTimeStampMixin, SchemaIdMixin, SchemaTimeStampMixin


class UserModel(base_model, ModelIdMixin, ModelTimeStampMixin):
    __tablename__ = 'user'
    username = Column(String(255), nullable=True, unique=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean(255), nullable=False)
    account_id = Column(Integer, ForeignKey('account.id'), index=True, nullable=False)


class UserSchema(Schema, SchemaIdMixin, SchemaTimeStampMixin):
    user_name = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    password = fields.String()
    is_active = fields.Boolean()
    account_id = fields.Integer()

    @post_load
    def create_model(self, _model, data):
        return UserModel(**data)
