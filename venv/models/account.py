# from marshmallow import Schema, fields, post_load
# from sqlalchemy import Boolean, Column, String
# from sqlalchemy.orm import relationship
# from base import base_model
# from factory import ModelIdMixin, ModelTimeStampMixin, SchemaIdMixin, SchemaTimeStampMixin
#
#
# class AccountModel(base_model, ModelIdMixin, ModelTimeStampMixin):
#     __tablename__ = 'account'
#     name = Column(String(255), nullable=False)
#     is_active = Column(Boolean, default=False)
#     users = relationship('UserModel')
#
#
# class AccountSchema(Schema, SchemaIdMixin, SchemaTimeStampMixin):
#     name = fields.String()
#     is_active = fields.Boolean()
#
#     @post_load
#     def create_model(self, data):
#         return AccountModel(**data)