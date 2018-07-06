import datetime
from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from base import base_model, TableTimeStampSchema
# from user import UserSchema
# from workday import WorkdaySchema
# from work_category import WorkCategorySchema


class TimeBlockModel(base_model):

    __tablename__ = 'time_block'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    workday_id = Column(Integer, ForeignKey('workday.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('work_category.id'), nullable=False)

    time_length = Column(DateTime, nullable=False)
    start_time = Column(DateTime, default=datetime.datetime.now, nullable=False)
    stop_time = Column(DateTime)
    interruptions = Column(Integer, default=0)
    time_block_notes = relationship("TimeBlockNoteModel", backref="time_block")

    created = Column(DateTime, default=datetime.datetime.now)
    modified = Column(DateTime, onupdate=datetime.datetime.now)
    deleted = Column(DateTime)


class TimeBlockSchema(Schema, TableTimeStampSchema):

    id = fields.Integer()

    # user = fields.Nested(UserSchema)
    # workday = fields.Nested(WorkdaySchema)
    # work_category = fields.Nested(WorkCategorySchema)

    time_length = fields.DateTime()
    start_time = fields.DateTime()
    stop_time = fields.DateTime()
    interruptions = fields.Integer()
    note = fields.String()

    @post_load
    def create_model(self, _model, data):
        return TimeBlockModel(**data)
