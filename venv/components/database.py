from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

uri = 'sqlite:///work_management.db'


class Database:
    def __init__(self):
        self.engine = create_engine(uri)
        self.Session = sessionmaker(bind=self.engine)

    def process_request(self, req, resp):
        req.context['session'] = self.Session()

    def process_response(self, req, resp, resource, req_succeeded):
        req.context['session'].close()
