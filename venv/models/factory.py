import datetime
from sqlalchemy import Column, DateTime, Integer, String
from marshmallow import Schema, fields


class ModelIdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class ModelTimeStampMixin:
    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class SchemaIdMixin:
    id = fields.Integer()


class SchemaTimeStampMixin:
    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime(dump_only=True)
