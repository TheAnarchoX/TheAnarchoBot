from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data import schemas

class DB:

    def  __init__(self):
        self.engine = create_engine("mysql://root@localhost/redditdatastore")
        self.connection = self.engine.connect()
        self.session = sessionmaker(bind=self.engine)


