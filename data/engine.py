from sqlalchemy import create_engine
from data import schemas

class DB:

    def  __init__(self):
        self.engine = create_engine("mysql://root@localhost/redditdatastore")
        self.connection = self.engine.connect()

    def close_connection(self):
        self.connection.close()

    def start_transaction(self):
        self.engine.begin()
