from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import base_model
from components import database
from models import *


def database_creator():
    engine = create_engine(database.uri)
    base_model.metadata.create_all(bind=engine)


if __name__ == '__main__':

    database_creator()

    engine = create_engine(database.uri)
    Session = sessionmaker(bind=engine)
    session = Session()


    user0 = user.UserModel(
        username='ricardobandala',
        password='password',
        is_active=True
    )

    user1 = user.UserModel(
        username='john_lennon',
        password='imagine',
        is_active=False
    )
    session.add(user0)
    # session.add(user1)
    session.commit()
    session.close()
