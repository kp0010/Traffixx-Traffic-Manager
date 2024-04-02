import os

import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, select

SQLURI = "sqlite:///users"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=True)

    def __repr__(self):

class Database:
    def __init__(self, echo=False):
        self.engine = sqlalchemy.create_engine(SQLURI, echo=echo)
        self.Base = Base

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    db = Database(echo=False)

    with Session(db.engine) as session:
        # kp = User(id="KP0012", name="Kartik Parab", password="kartikcrs", phone="987654322",
        #           email="kartikcr709@gmail.com")
        #
        # session.add(kp)

        user = session.execute(select(User).filter_by(id="KP0010")).one_or_none()

        print(user)

        session.commit()
