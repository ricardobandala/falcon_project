import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, DateTime, Integer, String
from base import base_model


class WorkCategoryModel(base_model):

    __tablename__ = 'work_category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)

    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(512))

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class WorkCategorySchema(Schema, TableTimeStampSchema):

    id = fields.Integer()

    name = fields.String()
    description = fields.String()

    @post_load
    def create_model(self, _model, data):
        return WorkCategoryModel(**data)