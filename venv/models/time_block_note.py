import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from base import base_model, TemplateModel, TableTimeStampSchema


class TimeBlockNoteModel(base_model, TemplateModel):
    __tablename__ = 'time_block_note'
    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    time_block_id = Column(Integer, ForeignKey('time_block.id'), nullable=False)
    content = Column(String(1024))

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class TimeBlockNoteSchema(Schema, TableTimeStampSchema):
    id = fields.Integer()

    user = fields.Nested('UserSchema')
    time_block = fields.Nested('TimeBlockSchema', exclude=('time_block_note',))

    user_id = fields.Integer()
    time_block_id = fields.Integer()
    content = fields.String()

    @post_load
    def create_model(self, _model, data):
        return TimeBlockNoteModel(**data)
