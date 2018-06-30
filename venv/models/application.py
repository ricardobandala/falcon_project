# from marshmallow import Schema, fields, post_load
# from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
# from base import base_model
#
#
# class ApplicationModel(base_model):
#     __tablename__ = 'application'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#
#     name = Column(String(255), nullable=False)
#     is_active = Column(Boolean(255), nullable=False)
#     users
#
# class ApplicationSchema(Schema):
#
#     id = fields.Integer()
#
#     name = fields.String()
#     is_active = fields.Boolean()
#
#     @post_load
#     def create_model(self, _model, data):
#         return ApplicationModel(**data)
