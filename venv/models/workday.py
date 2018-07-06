import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from base import base_model, TableTimeStampSchema
# from time_block import TimeBlockSchema


class WorkdayModel(base_model):

    __tablename__ = 'workday'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    # workday_id_user_id = ForeignKeyConstraint(
    # ['user_id', 'workday_id'],
    # ['user.id', 'workday.id']
    # name=fkc_workday_user
    # )

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    start_time = Column(DateTime, default=datetime.datetime.now, nullable=False)
    stop_time = Column(DateTime)
    time_blocks = relationship('TimeBlockModel', backref="workday")

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class WorkdaySchema(Schema, TableTimeStampSchema):

    id = fields.Integer()

    user_id = fields.Integer()
    start_time = fields.DateTime()
    stop_time = fields.DateTime()
    # time_block = fields.Nested(TimeBlockSchema, many=True)

    created = fields.DateTime(dump_only=True)
    modified = fields.DateTime(dump_only=True)
    deleted = fields.DateTime(dump_only=True)


    @post_load
    def create_model(self, _model, data):
        return WorkdayModel(**data)
