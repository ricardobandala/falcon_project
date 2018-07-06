from marshmallow import fields
from sqlalchemy.ext.declarative import declarative_base

base_model = declarative_base()


class TableTimeStampSchema:
    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime(dump_only=True)
