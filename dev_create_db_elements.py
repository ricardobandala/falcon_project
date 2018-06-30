from sqlalchemy import create_engine
from base import base_model
from components import database
# from sqlalchemy.ext.declarative import declarative_base

from models import *


def database_creator():
    engine = create_engine(database.uri)
    base_model.metadata.create_all(bind=engine)


if __name__ == '__main__':
    database_creator()


