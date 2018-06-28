from marshmallow import Schema, fields, post_load
from sqlalchemy import Boolean, Column, String, Integer, ForeignKey
from base import base_model
from factory import ModelIdMixin, ModelTimeStampMixin, SchemaIdMixin, SchemaTimeStampMixin


class ApplicationModel(base_model, ModelIdMixin, ModelTimeStampMixin):
    __tablename__ = 'application'
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean(255), nullable=False)


class ApplicationSchema(Schema, SchemaIdMixin, SchemaTimeStampMixin):
    name = fields.String()
    is_active = fields.Boolean()

    @post_load
    def create_model(self, _model, data):
        return ApplicationModel(**data)
