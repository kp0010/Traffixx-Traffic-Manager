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
        rep = f"{self.id =}, {self.name =}"
        return rep


class Database:
    def __init__(self, echo=False):
        self.engine = sqlalchemy.create_engine(SQLURI, echo=echo)
        self.Base = Base
        self.create_tables()

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)

    def add_new_user(self, id, name, password, phone, email):
        with Session(self.engine) as sesh:
            new_user = User(id=id, name=name, password=password, phone=phone, email=email)

            sesh.add(new_user)
            sesh.commit()


if __name__ == '__main__':
    db = Database(echo=False)

    # db.add_new_user("KP0011", "Kartikkk", "asjdflksjdf", phone="9230423234", email="kasdfas@gmail.com")

    with Session(db.engine) as session:
        user = session.execute(select(User).filter_by(id="KP0011")).one_or_none()
        print(user)
        session.commit()
